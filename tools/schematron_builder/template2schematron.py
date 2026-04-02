#!/usr/bin/env python3
"""
template2schematron.py

Uses lxml if available for robust comment handling; falls back to xml.etree.ElementTree.

Usage (non-positional arguments):
    python template2schematron.py \
        -t TEMPLATE_FILE \
        -x XSD_FILE \
        -i INPUT_FOLDER \
        -o OUTPUT_FILE \
        [-v]

Example:
    python template2schematron.py \
        --template mytemplate.xml \
        --xsd schema.xsd \
        --input-folder fragments \
        --output out.sch \
        --verbose
"""

import sys
import os
import re
import argparse

# Prefer lxml if available
try:
    import lxml.etree as LET
    from lxml.etree import Element as LET_Element, Comment as LET_Comment
    HAS_LXML = True
except Exception:
    LET = None
    HAS_LXML = False
    import xml.etree.ElementTree as ET
    from xml.etree.ElementTree import Element as ET_Element, Comment as ET_Comment

# Markers and regexes
START_MARKER = "ch-start"
END_MARKER = "ch-stop"
RE_NOTE = re.compile(r'\bch-note\s*:\s*(.*)', re.IGNORECASE)
RE_NOTICE = re.compile(r'\bch-notice\s*:\s*(.*)', re.IGNORECASE)  # treated like ch-note
RE_USAGE = re.compile(r'\bch-usage\s*:\s*(\w+)', re.IGNORECASE)
RE_REFERENCED = re.compile(r'\bch-referenced\b', re.IGNORECASE)
RE_REFERENCED_ALT = re.compile(r'\breferenced\b', re.IGNORECASE)
RE_REFERENCED_WITH_ARGS = re.compile(r'\bch-referenced\s*:\s*(.+)', re.IGNORECASE)
RE_ALLOWED_ENUMS = re.compile(r'\bch-allowed-enums\s*:\s*(.+)', re.IGNORECASE)
RE_DEPRECATED = re.compile(r'\bch-deprecated\b', re.IGNORECASE)
RE_CLASS_ID_MUST_EXIST = re.compile(r'\bch-class-id-must-exist\b', re.IGNORECASE)

# Known ch-commands (for warning on unknown ones)
KNOWN_CH_COMMANDS = {
    'ch-note',
    'ch-notice',
    'ch-usage',
    'ch-referenced',
    'ch-allowed-enums',
    'ch-deprecated',
    'ch-class-id-must-exist',
    'ch-start',
    'ch-stop',
}
RE_CH_COMMAND = re.compile(r'\b(ch-[a-zA-Z0-9_-]+)', re.IGNORECASE)

# Verbose debug toggle (set via CLI)
VERBOSE = False


def usage():
    print(
        "Usage: python template2schematron.py "
        "-t TEMPLATE_FILE -x XSD_FILE -i INPUT_FOLDER -o OUTPUT_FILE "
        "[-v]",
        file=sys.stderr,
    )
    sys.exit(2)


def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(path, content):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def indent_et(elem, level=0):
    """In-place pretty‑print indent for xml.etree.ElementTree elements."""
    i = "\n" + ("  " * level)
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent_et(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if not elem.tail or not elem.tail.strip():
            elem.tail = i


def extract_regions(text, start_marker=START_MARKER, end_marker=END_MARKER):
    lines = text.splitlines(keepends=True)
    results, collecting, buf = [], False, []
    for line in lines:
        if not collecting and start_marker in line:
            collecting = True
            buf.append(line)
            continue
        if collecting:
            buf.append(line)
            if end_marker in line:
                results.append(''.join(buf))
                buf = []
                collecting = False
    if collecting and buf:
        results.append(''.join(buf))
    return results


def wrap_fragment(fragment):
    # Use XML declaration and artificial root
    return '<?xml version="1.0" encoding="utf-8"?><__root__>' + fragment + '</__root__>'


def warn_on_unknown_ch_commands(comment_text, location_desc=''):
    found = set(cmd.lower() for cmd in RE_CH_COMMAND.findall(comment_text))
    unknown = {cmd for cmd in found if cmd not in KNOWN_CH_COMMANDS}
    if unknown:
        loc = f" at {location_desc}" if location_desc else ""
        print(
            f"Warning: unknown ch-commands{loc}: {', '.join(sorted(unknown))}",
            file=sys.stderr,
        )


def parse_usage_and_notes_from_comments(comment_text):
    # ch-note
    notes = RE_NOTE.findall(comment_text) or []
    # ch-notice treated like ch-note
    notices = RE_NOTICE.findall(comment_text) or []
    all_notes = notes + notices

    usages = RE_USAGE.findall(comment_text)

    referenced_names = []
    args_match = RE_REFERENCED_WITH_ARGS.search(comment_text)
    if args_match:
        vals = args_match.group(1).strip()
        referenced_names = [v for v in re.split(r'\s+', vals) if v != '']
    else:
        if RE_REFERENCED.search(comment_text) or RE_REFERENCED_ALT.search(comment_text):
            referenced_names = ['__DEFAULT__']

    allowed_match = RE_ALLOWED_ENUMS.search(comment_text)
    allowed = []
    if allowed_match:
        vals = allowed_match.group(1).strip()
        allowed = [v for v in re.split(r'\s+', vals) if v != '']

    deprecated = bool(RE_DEPRECATED.search(comment_text))
    class_id_must_exist = bool(RE_CLASS_ID_MUST_EXIST.search(comment_text))

    return {
        'notes': [n.strip() for n in all_notes] if all_notes else [],
        'usages': [u.strip().lower() for u in usages] if usages else [],
        'referenced_names': referenced_names,
        'allowed_enums': allowed,
        'deprecated': deprecated,
        'class_id_must_exist': class_id_must_exist,
    }


def local_name(tag):
    if tag is None:
        return ''
    # strip namespace if present
    m = re.match(r'\{.*\}(.*)', tag)
    return m.group(1) if m else tag


# Node utilities abstracting lxml vs ET
def parse_xml_fragment(fragment_text):
    """Parse wrapped fragment text and return a root element (lxml or ET)."""
    if HAS_LXML:
        return LET.fromstring(fragment_text.encode('utf-8'))
    else:
        return ET.fromstring(fragment_text)


def iter_children(node):
    """Return list of direct children in order."""
    if HAS_LXML:
        return list(node)
    else:
        return list(node)


def is_comment(node):
    """Detect comment nodes for current parser."""
    if HAS_LXML:
        return isinstance(node, LET._Comment)
    else:
        try:
            if node.tag is ET.Comment:
                return True
        except Exception:
            pass
        try:
            if isinstance(node.tag, str) and node.tag.lower() == 'comment':
                return True
        except Exception:
            pass
        return False


# Schematron builder (using ET to build output; this is independent from parsing library)
import xml.etree.ElementTree as OUT_ET
from xml.etree.ElementTree import Element as OUT_Element, SubElement as OUT_SubElement

SCHEMATRON_NS = "http://purl.oclc.org/dsdl/schematron"
SCH_PREFIX = "sch"


class SchematronBuilder:
    def __init__(self, xsd_path):
        self.xsd_path = xsd_path

        # Root with explicit prefix and queryBinding (xslt2)
        attrib = {
            f'xmlns:{SCH_PREFIX}': SCHEMATRON_NS,
            'queryBinding': 'xslt2',
        }

        self.schema = OUT_Element(
            f'{SCH_PREFIX}:schema',
            attrib=attrib
        )
        title = OUT_SubElement(self.schema, f'{SCH_PREFIX}:title')
        title.text = 'Generated schematron from template'
        self.pattern = OUT_SubElement(self.schema, f'{SCH_PREFIX}:pattern', attrib={'id': 'p1'})
        self.processed_files = set()
        self.rules_created = 0

    def add_comment_to_rule(self, parent, text):
        parent.append(OUT_ET.Comment(' ' + text + ' '))

    def _ns_name(self, element_name):
        """Return the element name unchanged (no namespace prefixing)."""
        return element_name

    def _ns_context(self, context_xpath):
        """Return context unchanged, except keep '.' as-is."""
        if context_xpath == '.' or not context_xpath:
            return '.'
        return context_xpath

    def add_rule_presence(self, context_xpath, element_name, note_text=None):
        ctx = self._ns_context(context_xpath)
        rule = OUT_SubElement(self.pattern, f'{SCH_PREFIX}:rule', attrib={'context': ctx})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        ns_elem = self._ns_name(element_name)
        OUT_SubElement(
            rule,
            f'{SCH_PREFIX}:assert',
            attrib={'test': f'count(.//{ns_elem}) > 0'}
        ).text = f'{element_name} must be present'
        self.rules_created += 1

    def add_rule_absence(self, context_xpath, element_name, note_text=None):
        ctx = self._ns_context(context_xpath)
        rule = OUT_SubElement(self.pattern, f'{SCH_PREFIX}:rule', attrib={'context': ctx})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        ns_elem = self._ns_name(element_name)
        OUT_SubElement(
            rule,
            f'{SCH_PREFIX}:assert',
            attrib={'test': f'count(.//{ns_elem}) = 0'}
        ).text = f'{element_name} must NOT be present'
        self.rules_created += 1

    def add_rule_allowed_enums(self, context_xpath, element_name, allowed_list, note_text=None):
        if not allowed_list:
            return
        ctx = self._ns_context(context_xpath)
        ns_elem = self._ns_name(element_name)
        ors = ' or '.join([f"{ns_elem} = '{val}'" for val in allowed_list])
        rule = OUT_SubElement(self.pattern, f'{SCH_PREFIX}:rule', attrib={'context': ctx})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        OUT_SubElement(
            rule,
            f'{SCH_PREFIX}:assert',
            attrib={'test': ors}
        ).text = f'{element_name} must be one of: {" ".join(allowed_list)}'
        self.rules_created += 1

    def add_rule_deprecated(self, context_xpath, element_name, note_text=None):
        ctx = self._ns_context(context_xpath)
        rule = OUT_SubElement(self.pattern, f'{SCH_PREFIX}:rule', attrib={'context': ctx})
        base_note = f'DEPRECATED: {element_name} is deprecated'
        if note_text:
            full_note = f'{base_note}; {note_text}'
        else:
            full_note = base_note
        self.add_comment_to_rule(rule, full_note)

        ns_elem = self._ns_name(element_name)
        OUT_SubElement(
            rule,
            f'{SCH_PREFIX}:assert',
            attrib={'test': f'count(.//{ns_elem}) = 0'}
        ).text = f'{element_name} is deprecated and should not be used'
        self.rules_created += 1

    def add_rule_class_id_must_exist(self, context_xpath, element_name, id_value, note_text=None):
        """
        Add a rule that checks that an element with the same name and @id = id_value exists.
        Example test for element_name='TypeOfProductCategory', id_value='12312':
            count(//TypeOfProductCategory[@id='12312']) > 0
        """
        if not id_value:
            # No id on the element, nothing we can check
            return
        ctx = self._ns_context(context_xpath)
        rule = OUT_SubElement(self.pattern, f'{SCH_PREFIX}:rule', attrib={'context': ctx})
        base_note = (
            f'{element_name} with id="{id_value}" must exist somewhere in the document'
        )
        if note_text:
            full_note = f'{base_note}; {note_text}'
        else:
            full_note = base_note
        self.add_comment_to_rule(rule, full_note)

        ns_elem = self._ns_name(element_name)
        test_expr = f"count(//{ns_elem}[@id='{id_value}']) > 0"
        OUT_SubElement(
            rule,
            f'{SCH_PREFIX}:assert',
            attrib={'test': test_expr}
        ).text = (
            f'An element {element_name} with id="{id_value}" must exist'
        )
        self.rules_created += 1

    def tostring(self):
        # Pretty-print before serializing
        indent_et(self.schema)
        xml = OUT_ET.tostring(self.schema, encoding='unicode')

        # Unescape '>' only inside sch:assert/@test attributes
        # This keeps the XML valid while ensuring the operator is literal.
        xml = re.sub(r'(test=")([^"]*)(")', lambda m: m.group(1) + m.group(2).replace('&gt;', '>') + m.group(3), xml)

        return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml


def find_files_for_candidate(input_folder, candidate_filename):
    matches = []
    for root, dirs, files in os.walk(input_folder):
        if candidate_filename in files:
            matches.append(os.path.join(root, candidate_filename))
    return matches


def _process_fragment_root(rootfrag, parent_tag_local, builder, input_folder):
    nodes = iter_children(rootfrag)
    for node in nodes:
        if is_comment(node):
            if VERBOSE:
                print("Fragment comment:", repr(node.text))
            ctext = (node.text or '').strip()
            warn_on_unknown_ch_commands(
                ctext,
                location_desc=f"fragment under parent '{parent_tag_local or 'ROOT'}'"
            )
            parsed = parse_usage_and_notes_from_comments(ctext)
            notes = parsed['notes']
            usages = parsed['usages']
            referenced_names = parsed['referenced_names']
            allowed_enums = parsed['allowed_enums']
            deprecated = parsed['deprecated']
            class_id_must_exist = parsed['class_id_must_exist']

            note_text = '; '.join(notes) if notes else None

            context = parent_tag_local if parent_tag_local else '.'
            elem_name = parent_tag_local or '.'

            if any(u == 'forbidden' for u in usages):
                builder.add_rule_absence(context, elem_name, note_text=note_text)
            if any(u == 'mandatory' for u in usages):
                builder.add_rule_presence(context, elem_name, note_text=note_text)
            if deprecated:
                builder.add_rule_deprecated(context, elem_name, note_text=note_text)
            if allowed_enums:
                builder.add_rule_allowed_enums(
                    context,
                    elem_name,
                    allowed_enums,
                    note_text=note_text
                )
            # class-id-must-exist not handled here (no attributes context)

            if referenced_names:
                tokens = []
                if all(t == '__DEFAULT__' for t in referenced_names):
                    tokens = ['__DEFAULT__']
                else:
                    for t in referenced_names:
                        if t != '__DEFAULT__':
                            tokens.append(t)
                    if '__DEFAULT__' in referenced_names:
                        tokens.append('__DEFAULT__')
                for token in tokens:
                    candidates = []
                    if token == '__DEFAULT__':
                        if parent_tag_local:
                            candidates.append(f'{parent_tag_local}.xml')
                    else:
                        candidates.append(
                            token if token.lower().endswith('.xml') else f'{token}.xml'
                        )
                    for candidate in candidates:
                        for found_path in find_files_for_candidate(input_folder, candidate):
                            ab = os.path.abspath(found_path)
                            if ab in builder.processed_files:
                                continue
                            builder.processed_files.add(ab)
                            if VERBOSE:
                                print(f"Processing referenced file: {ab}")
                            try:
                                txt = read_file(found_path)
                            except Exception as e:
                                print(
                                    f'Warning: cannot read referenced file {found_path}: {e}',
                                    file=sys.stderr
                                )
                                continue
                            regions = extract_regions(txt)
                            if not regions:
                                regions = [txt]
                            for r in regions:
                                wrapped = wrap_fragment(r)
                                try:
                                    subfrag = parse_xml_fragment(wrapped)
                                except Exception as e:
                                    print(
                                        f'Warning: parse error in referenced file {found_path}: {e}',
                                        file=sys.stderr
                                    )
                                    continue
                                _process_fragment_root(subfrag, parent_tag_local, builder, input_folder)
        else:
            # element node - call element processing
            context = parent_tag_local if parent_tag_local else '.'
            process_element_tree(
                node,
                builder,
                context_xpath=context,
                input_folder=input_folder,
                ancestor_forbidden=False
            )


def process_element_tree(elem, builder, context_xpath='.', input_folder='.', ancestor_forbidden=False):
    if ancestor_forbidden:
        return
    tag_local = local_name(elem.tag if HAS_LXML else elem.tag)
    if VERBOSE:
        print("Processing element:", tag_local, "context:", context_xpath)

    nodes = iter_children(elem)
    child_elements = []
    child_comments = []
    for node in nodes:
        if is_comment(node):
            child_comments.append(node)
        else:
            child_elements.append(node)

    for comment_node in child_comments:
        ctext = (comment_node.text or '').strip()
        warn_on_unknown_ch_commands(ctext, location_desc=f"element '{tag_local}'")
        parsed = parse_usage_and_notes_from_comments(ctext)
        notes = parsed['notes']
        usages = parsed['usages']
        referenced_names = parsed['referenced_names']
        allowed_enums = parsed['allowed_enums']
        deprecated = parsed['deprecated']
        class_id_must_exist = parsed['class_id_must_exist']

        note_text = '; '.join(notes) if notes else None

        if any(u == 'forbidden' for u in usages):
            builder.add_rule_absence(context_xpath, tag_local, note_text=note_text)
        if any(u == 'mandatory' for u in usages):
            builder.add_rule_presence(context_xpath, tag_local, note_text=note_text)
        if deprecated:
            builder.add_rule_deprecated(context_xpath, tag_local, note_text=note_text)
        if allowed_enums:
            builder.add_rule_allowed_enums(
                context_xpath,
                tag_local,
                allowed_enums,
                note_text=note_text
            )

        if class_id_must_exist:
            # Use the element's @id value
            id_value = elem.get('id') if not HAS_LXML else elem.get('id')
            builder.add_rule_class_id_must_exist(
                context_xpath,
                tag_local,
                id_value,
                note_text=note_text
            )

        if referenced_names:
            tokens = []
            if all(t == '__DEFAULT__' for t in referenced_names):
                tokens = ['__DEFAULT__']
            else:
                for t in referenced_names:
                    if t != '__DEFAULT__':
                        tokens.append(t)
                if '__DEFAULT__' in referenced_names:
                    tokens.append('__DEFAULT__')
            for token in tokens:
                candidates = []
                if token == '__DEFAULT__':
                    candidates.append(f'{tag_local}.xml')
                else:
                    candidates.append(
                        token if token.lower().endswith('.xml') else f'{token}.xml'
                    )
                for candidate in candidates:
                    for found_path in find_files_for_candidate(input_folder, candidate):
                        ab = os.path.abspath(found_path)
                        if ab in builder.processed_files:
                            continue
                        builder.processed_files.add(ab)
                        if VERBOSE:
                            print(f"Processing referenced file: {ab}")
                        try:
                            txt = read_file(found_path)
                        except Exception as e:
                            print(
                                f'Warning: cannot read referenced file {found_path}: {e}',
                                file=sys.stderr
                            )
                            continue
                        regions = extract_regions(txt)
                        if not regions:
                            regions = [txt]
                        for r in regions:
                            wrapped = wrap_fragment(r)
                            try:
                                rootfrag = parse_xml_fragment(wrapped)
                            except Exception as e:
                                print(
                                    f'Warning: parse error in referenced file {found_path}: {e}',
                                    file=sys.stderr
                                )
                                continue
                            _process_fragment_root(rootfrag, tag_local, builder, input_folder)

    for child in child_elements:
        # context for children is the current element name
        process_element_tree(
            child,
            builder,
            context_xpath=tag_local,
            input_folder=input_folder,
            ancestor_forbidden=False
        )


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Generate Schematron from XML template and fragments."
    )
    parser.add_argument(
        '-t', '--template',
        required=True,
        help='Template XML file containing ch-start/ch-stop regions.'
    )
    parser.add_argument(
        '-x', '--xsd',
        required=True,
        help='XSD file (optional for validation, but path is stored).'
    )
    parser.add_argument(
        '-i', '--input-folder',
        required=True,
        help='Folder with referenced XML fragment files.'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output Schematron (.sch) file.'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging.'
    )
    return parser.parse_args(argv[1:])


def main(argv):
    global VERBOSE

    if len(argv) == 1:
        usage()

    args = parse_args(argv)
    template_path = args.template
    xsd_path = args.xsd
    input_folder = args.input_folder
    output_path = args.output
    VERBOSE = args.verbose

    if not os.path.isfile(template_path):
        print(f'Error: template file not found: {template_path}', file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(xsd_path):
        print(f'Warning: xsd file not found: {xsd_path}', file=sys.stderr)
    if not os.path.isdir(input_folder):
        print(f'Warning: input folder not found: {input_folder}', file=sys.stderr)

    txt = read_file(template_path)
    regions = extract_regions(txt)
    if not regions:
        print(
            'Warning: no regions found between markers; attempting to process entire file',
            file=sys.stderr
        )
        regions = [txt]

    builder = SchematronBuilder(xsd_path)

    for region in regions:
        wrapped = wrap_fragment(region)
        try:
            root = parse_xml_fragment(wrapped)
        except Exception as e:
            print(f'Error parsing extracted region: {e}', file=sys.stderr)
            continue

        for node in iter_children(root):
            if is_comment(node):
                ctext = (node.text or '').strip()
                warn_on_unknown_ch_commands(ctext, location_desc="top-level template region")
                parsed = parse_usage_and_notes_from_comments(ctext)
                notes = parsed['notes']
                usages = parsed['usages']
                referenced_names = parsed['referenced_names']
                allowed_enums = parsed['allowed_enums']
                deprecated = parsed['deprecated']
                class_id_must_exist = parsed['class_id_must_exist']

                note_text = '; '.join(notes) if notes else None

                if any(u == 'forbidden' for u in usages):
                    builder.add_rule_absence('.', '.', note_text=note_text)
                if any(u == 'mandatory' for u in usages):
                    builder.add_rule_presence('.', '.', note_text=note_text)
                if deprecated:
                    builder.add_rule_deprecated('.', '.', note_text=note_text)
                # class-id-must-exist does not make sense at top-level without an element

                if referenced_names:
                    tokens = []
                    if all(t == '__DEFAULT__' for t in referenced_names):
                        tokens = ['__DEFAULT__']
                    else:
                        for t in referenced_names:
                            if t != '__DEFAULT__':
                                tokens.append(t)
                        if '__DEFAULT__' in referenced_names:
                            tokens.append('__DEFAULT__')
                    for token in tokens:
                        if token == '__DEFAULT__':
                            continue
                        candidates = [
                            token if token.lower().endswith('.xml') else f'{token}.xml'
                        ]
                        for candidate in candidates:
                            for found_path in find_files_for_candidate(input_folder, candidate):
                                ab = os.path.abspath(found_path)
                                if ab in builder.processed_files:
                                    continue
                                builder.processed_files.add(ab)
                                if VERBOSE:
                                    print(f"Processing referenced file: {ab}")
                                try:
                                    txt = read_file(found_path)
                                except Exception as e:
                                    print(
                                        f'Warning: cannot read referenced file {found_path}: {e}',
                                        file=sys.stderr
                                    )
                                    continue
                                subregions = extract_regions(txt)
                                if not subregions:
                                    subregions = [txt]
                                for r in subregions:
                                    wrapped_r = wrap_fragment(r)
                                    try:
                                        rootfrag = parse_xml_fragment(wrapped_r)
                                    except Exception as e:
                                        print(
                                            f'Warning: parse error in referenced file {found_path}: {e}',
                                            file=sys.stderr
                                        )
                                        continue
                                    _process_fragment_root(rootfrag, None, builder, input_folder)
            else:
                process_element_tree(
                    node,
                    builder,
                    context_xpath='.',
                    input_folder=input_folder,
                    ancestor_forbidden=False
                )

    out = builder.tostring()
    write_file(output_path, out)
    print(f'Wrote schematron to {output_path}. Rules created: {builder.rules_created}')


if __name__ == '__main__':
    main(sys.argv)
