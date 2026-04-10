#!/usr/bin/env python3
"""
template2schematron.py

Generates Schematron validation files from XML templates with special comment annotations.

Requires lxml for robust XML processing and XPath support.
Install: pip install lxml

Usage:
    python template2schematron.py \
        -t TEMPLATE_FILE \
        -x XSD_FILE \
        -i INPUT_FOLDER \
        -o OUTPUT_FILE \
        [-v] \
        [-r ROOT_ELEMENT]

Examples:
    # Process a single ch-profile template
    python template2schematron.py \
        -t templates/ch-profile_export-timetable_file.xml \
        -x xsd/xsd/NeTEx_publication.xsd \
        -i templates \
        -o generated/schematrons/ch-profile_export_timetable_file.sch \
        -v

    # Process all ch-profile templates (using shell loop)
    for template in templates/ch-profile_*.xml; do
        output="generated/schematrons/$(basename "$template" .xml).sch"
        python template2schematron.py \
            -t "$template" \
            -x xsd/xsd/NeTEx_publication.xsd \
            -i templates \
            -o "$output"
    done

    # Use a custom root element (default: PublicationDelivery)
    python template2schematron.py \
        -t templates/custom_template.xml \
        -x xsd/xsd/NeTEx_publication.xsd \
        -i templates \
        -o generated/schematrons/custom.sch \
        -r CustomRootElement
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Require lxml - it provides better XML handling and XPath support
try:
    import lxml.etree as ET
    from lxml.etree import Element, tostring
    HAS_LXML = True
except ImportError:
    print("ERROR: lxml is required for this script. Please install it with:", file=sys.stderr)
    print("pip install lxml", file=sys.stderr)
    sys.exit(1)

# Markers and regexes
START_MARKER = "ch-start"
END_MARKER = "ch-stop"
RE_NOTE = re.compile(r'\bch-note\s*:\s*(.*)', re.IGNORECASE)
RE_USAGE = re.compile(r'\bch-usage\s*:\s*(\w+)', re.IGNORECASE)
RE_SEE = re.compile(r'\bch-see\b', re.IGNORECASE)
RE_SEE_WITH_ARGS = re.compile(r'\bch-see\s*:\s*(.+)', re.IGNORECASE)
RE_ALLOWED_ENUMS = re.compile(r'\bch-allowed-enums\s*:\s*(.+)', re.IGNORECASE)
RE_DEPRECATED = re.compile(r'\bch-deprecated\b', re.IGNORECASE)
RE_CLASS_ID_MUST_EXIST = re.compile(r'\bch-class-id-must-exist\b', re.IGNORECASE)

# Known ch-commands (for warning on unknown ones)
KNOWN_CH_COMMANDS = {
    'ch-note',
    'ch-usage',
    'ch-see',
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
    """Read file content with UTF-8 encoding."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"ERROR: Cannot read file {path}: {e}", file=sys.stderr)
        raise


def write_file(path, content):
    """Write content to file, creating parent directories if needed."""
    try:
        d = os.path.dirname(path)
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"ERROR: Cannot write file {path}: {e}", file=sys.stderr)
        raise


def indent_et(elem, level=0):
    """In-place pretty-print indent for lxml elements."""
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
    """Extract regions between start and end markers."""
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
    """Wrap XML fragment with root element for parsing."""
    return '<?xml version="1.0" encoding="utf-8"?><__root__>' + fragment + '</__root__>'


def warn_on_unknown_ch_commands(comment_text, location_desc=''):
    """Warn about unknown ch-commands in comments."""
    found = set(cmd.lower() for cmd in RE_CH_COMMAND.findall(comment_text))
    unknown = {cmd for cmd in found if cmd not in KNOWN_CH_COMMANDS}
    if unknown:
        loc = f" at {location_desc}" if location_desc else ""
        print(
            f"Warning: unknown ch-commands{loc}: {', '.join(sorted(unknown))}",
            file=sys.stderr,
        )


def parse_usage_and_notes_from_comments(comment_text):
    """Parse ch-commands from comment text and return structured data."""
    # ch-note
    notes = RE_NOTE.findall(comment_text) or []
    all_notes = notes

    usages = RE_USAGE.findall(comment_text)

    see_names = []
    args_match = RE_SEE_WITH_ARGS.search(comment_text)
    if args_match:
        vals = args_match.group(1).strip()
        see_names = [v for v in re.split(r'\s+', vals) if v != '']
    else:
        if RE_SEE.search(comment_text):
            see_names = ['__DEFAULT__']

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
    """Extract local name from potentially namespaced tag."""
    if tag is None:
        return ''
    # strip namespace if present
    m = re.match(r'\{.*\}(.*)', tag)
    return m.group(1) if m else tag


def find_files_for_candidate(input_folder, candidate_filename):
    """Find all files matching candidate filename in input folder tree."""
    matches = []
    for root, dirs, files in os.walk(input_folder):
        if candidate_filename in files:
            matches.append(os.path.join(root, candidate_filename))
    return matches


# Schematron builder using lxml
SCHEMATRON_NS = "http://purl.oclc.org/dsdl/schematron"
SCH_PREFIX = "sch"
NETEX_NS = "http://www.netex.org.uk/netex"


class SchematronBuilder:
    def __init__(self, xsd_path):
        self.xsd_path = xsd_path
        self.processed_files = set()
        self.rules_created = 0
        
        # Create root schema element with namespaces
        # Use proper namespace handling for lxml
        NSMAP = {
            SCH_PREFIX: SCHEMATRON_NS,
            'netex': NETEX_NS
        }
        
        self.schema = Element('{' + SCHEMATRON_NS + '}schema', nsmap=NSMAP)
        self.schema.set('queryBinding', 'xslt2')
        
        # Add namespace declaration
        self.ns = Element('{' + SCHEMATRON_NS + '}ns', nsmap=NSMAP)
        self.ns.set('prefix', 'netex')
        self.ns.set('uri', NETEX_NS)
        self.schema.append(self.ns)
        
        # Add title
        self.title = Element('{' + SCHEMATRON_NS + '}title', nsmap=NSMAP)
        self.title.text = 'Generated schematron from template'
        self.schema.append(self.title)
        
        # Create pattern
        self.pattern = Element('{' + SCHEMATRON_NS + '}pattern', nsmap=NSMAP)
        self.pattern.set('id', 'p1')
        self.schema.append(self.pattern)
        
        # Maintain mapping from context XPath to rule element
        self._rules_by_context = {}

    def add_comment_to_rule(self, rule, text):
        """Add XML comment to a rule element."""
        rule.append(ET.Comment(' ' + text + ' '))

    def _ns_name(self, element_name):
        """Return element name prefixed with netex: unless it's '.' or empty."""
        if not element_name or element_name == '.':
            return element_name
        # If element_name already contains a colon, assume it's already namespaced
        if ':' in element_name:
            return element_name
        return f'netex:{element_name}'

    def _ns_context(self, context_xpath):
        """
        Normalize rule context:
        - Keep '.' as-is.
        - If the context already starts with '//' or '.', return as-is.
        - Otherwise, prefix '//' (the system expects double-slash absolute contexts).
        """
        if not context_xpath or context_xpath == '.':
            return '.'
        # We assume callers pass fully-built element paths like 'netex:PublicationDelivery/netex:frames/...'
        ctx = context_xpath
        if ctx.startswith('//') or ctx.startswith('.'):
            return ctx
        return f'//{ctx}'

    def _get_or_create_rule(self, context_xpath, note_text=None):
        """
        Return an existing rule element for the given context, or create one.
        Attach the comment note_text only when creating the rule.
        """
        ctx = self._ns_context(context_xpath)
        if ctx in self._rules_by_context:
            rule = self._rules_by_context[ctx]
            if note_text:
                self.add_comment_to_rule(rule, note_text)
            return rule
        
        # Use proper namespace for rule element
        NSMAP = {SCH_PREFIX: SCHEMATRON_NS}
        rule = Element('{' + SCHEMATRON_NS + '}rule', nsmap=NSMAP)
        rule.set('context', ctx)
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        self._rules_by_context[ctx] = rule
        self.pattern.append(rule)
        self.rules_created += 1
        return rule

    def add_assert_or_report(self, context_xpath, test_expr, message, kind='assert', note_text=None):
        """
        Add either an assert or a report to the rule for context_xpath.
        kind: 'assert' (default) or 'report'
        test_expr: XPath expression string for the test attribute
        message: text node for the assert/report
        """
        rule = self._get_or_create_rule(context_xpath, note_text=note_text)
        
        # Use proper namespace for assert/report elements
        NSMAP = {SCH_PREFIX: SCHEMATRON_NS}
        elem_name = '{' + SCHEMATRON_NS + '}' + kind
        elem = Element(elem_name, nsmap=NSMAP)
        elem.set('test', test_expr)
        elem.text = message
        rule.append(elem)

    def add_rule_presence(self, parent_context_xpath, element_name, note_text=None):
        """Add rule requiring element presence."""
        if not parent_context_xpath:
            return  # no parent (top-level), skip presence rule
        ns_elem = self._ns_name(element_name)
        test = f'count({ns_elem}) > 0'
        self.add_assert_or_report(parent_context_xpath, test, f'{element_name} must be present', kind='assert', note_text=note_text)

    def add_rule_absence(self, parent_context_xpath, element_name, note_text=None):
        """Add rule requiring element absence."""
        if not parent_context_xpath:
            return  # no parent (top-level), skip absence rule
        ns_elem = self._ns_name(element_name)
        test = f'count({ns_elem}) = 0'
        self.add_assert_or_report(parent_context_xpath, test, f'{element_name} must NOT be present', kind='assert', note_text=note_text)

    def add_rule_allowed_enums(self, context_xpath, element_name, allowed_list, note_text=None):
        """Add rule restricting element value to allowed enumerations."""
        if not allowed_list:
            return
        # If element_name == '.', test the value of the current context element.
        if element_name == '.' or not element_name:
            ors = ' or '.join([f". = '{val}'" for val in allowed_list])
            test = f'({ors})'
            self.add_assert_or_report(context_xpath, test, f'Value must be one of: {" ".join(allowed_list)}', kind='assert', note_text=note_text)
        else:
            ns_elem = self._ns_name(element_name)
            ors = ' or '.join([f"{ns_elem} = '{val}'" for val in allowed_list])
            test = f'({ors})'
            self.add_assert_or_report(context_xpath, test, f'{element_name} must be one of: {" ".join(allowed_list)}', kind='assert', note_text=note_text)

    def add_rule_deprecated(self, parent_context_xpath, element_name, note_text=None):
        """Add rule marking element as deprecated."""
        if not parent_context_xpath:
            return
        base_note = f'DEPRECATED: {element_name} is deprecated'
        full_note = f'{base_note}; {note_text}' if note_text else base_note
        ns_elem = self._ns_name(element_name)
        test = f'count({ns_elem}) = 0'
        self.add_assert_or_report(parent_context_xpath, test, f'{element_name} is deprecated and should not be used', kind='assert', note_text=full_note)

    def add_rule_class_id_must_exist(self, context_xpath, element_name, id_value, note_text=None):
        """
        Produce a report that an element with the given id must exist somewhere in the document.
        Attach at the element's own absolute context (if available).
        """
        if not id_value:
            return
        base_note = f'{element_name} with id="{id_value}" must exist somewhere in the document'
        full_note = f'{base_note}; {note_text}' if note_text else base_note
        ns_elem = self._ns_name(element_name)
        test_expr = f"count(//{ns_elem}[@id='{id_value}']) > 0"
        self.add_assert_or_report(context_xpath, test_expr, f'An element {element_name} with id="{id_value}" must exist', kind='report', note_text=full_note)

    def tostring(self):
        """Serialize schematron to XML string with proper formatting."""
        # Pretty-print before serializing
        indent_et(self.schema)
        xml = tostring(self.schema, encoding='unicode', pretty_print=True)
        
        # Unescape '>' only inside sch:assert/@test and sch:report/@test attributes
        xml = re.sub(
            r'((?:test=")([^"]*)("))',
            lambda m: m.group(1).replace('&gt;', '>'),
            xml
        )
        # ensure XML declaration
        return '<?xml version="1.0" encoding="UTF-8"?>' + xml


def ns_join(builder, parent_path, local):
    """Join a local element name onto a namespaced absolute path."""
    ns = builder._ns_name(local)
    return ns if not parent_path else f'{parent_path}/{ns}'


def _process_fragment_root(rootfrag, builder, base_context_path, parent_context_path, element_local_name, input_folder):
    """
    Process a referenced fragment for element `element_local_name`.
    
    - base_context_path: absolute path to the element itself (e.g., .../netex:Operator)
    - parent_context_path: absolute path to the element's parent (e.g., .../netex:organisations)
    - element_local_name: local name (e.g., Operator)
    
    Top-level comments in the fragment are applied to the element (or its parent where relevant).
    The fragment's top-level element that matches element_local_name is treated as the SAME context
    (no extra /Operator appended), to avoid .../Operator/Operator.
    """
    nodes = list(rootfrag)
    for node in nodes:
        if isinstance(node, ET._Comment):
            if VERBOSE:
                print("Fragment comment:", repr(node.text))
            ctext = (node.text or '').strip()
            warn_on_unknown_ch_commands(
                ctext,
                location_desc=f"fragment for '{element_local_name}'"
            )
            parsed = parse_usage_and_notes_from_comments(ctext)
            notes = parsed['notes']
            usages = parsed['usages']
            referenced_names = parsed['referenced_names']
            allowed_enums = parsed['allowed_enums']
            deprecated = parsed['deprecated']
            class_id_must_exist = parsed['class_id_must_exist']

            note_text = '; '.join(notes) if notes else None

            # Apply usage/deprecation to the parent context about the element itself
            if any(u == 'forbidden' for u in usages):
                builder.add_rule_absence(parent_context_path, element_local_name, note_text=note_text)
            if any(u == 'mandatory' for u in usages):
                builder.add_rule_presence(parent_context_path, element_local_name, note_text=note_text)
            if deprecated:
                builder.add_rule_deprecated(parent_context_path, element_local_name, note_text=note_text)
            # Allowed enums at the element itself (value check at element context)
            if allowed_enums:
                builder.add_rule_allowed_enums(base_context_path, '.', allowed_enums, note_text=note_text)
            # class-id-must-exist at fragment top-level: we don't have the id value here; skip

            # referenced_names at fragment top-level: rare; if provided, treat as further inclusions under element context
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
                        candidates.append(f'{element_local_name}.xml')
                    else:
                        candidates.append(token if token.lower().endswith('.xml') else f'{token}.xml')
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
                                print(f'Warning: cannot read referenced file {found_path}: {e}', file=sys.stderr)
                                continue
                            regions = extract_regions(txt)
                            if not regions:
                                regions = [txt]
                            for r in regions:
                                wrapped = wrap_fragment(r)
                                try:
                                    subfrag = ET.fromstring(wrapped.encode('utf-8'))
                                except Exception as e:
                                    print(f'Warning: parse error in referenced file {found_path}: {e}', file=sys.stderr)
                                    continue
                                # Recurse: still under same element context for its top-level
                                _process_fragment_root(subfrag, builder, base_context_path, parent_context_path, element_local_name, input_folder)
        else:
            # Element node within the fragment
            node_local = local_name(node.tag)
            if node_local == element_local_name:
                # Treat this element as the SAME context as the referencing element
                process_element_tree(
                    node,
                    builder,
                    parent_context_path=parent_context_path,
                    input_folder=input_folder,
                    is_ref_root=True,
                    current_context_path=base_context_path
                )
            else:
                # If fragment provides children directly (without wrapping <element_local_name>),
                # process them as children of the element context.
                process_element_tree(
                    node,
                    builder,
                    base_context_path,
                    input_folder=input_folder,
                    is_ref_root=False
                )


def process_element_tree(elem, builder, parent_context_path='', input_folder='.', is_ref_root=False, current_context_path=None):
    """
    - parent_context_path: absolute path string of the parent element (without leading '//').
    - is_ref_root + current_context_path: when True, 'elem' corresponds to an already-established
      absolute element path (current_context_path). Do not append the element name again.
    """
    tag_local = local_name(elem.tag)
    if VERBOSE:
        print("Processing element:", tag_local, "parent context:", parent_context_path, "is_ref_root:", is_ref_root)

    # Determine this element's absolute path (no leading '//' internally)
    if is_ref_root and current_context_path:
        elem_abs_path = current_context_path              # e.g., netex:.../netex:Operator
        parent_abs_path = parent_context_path             # e.g., netex:.../netex:organisations
    else:
        elem_abs_path = ns_join(builder, parent_context_path, tag_local)
        parent_abs_path = parent_context_path


    # Partition direct children
    nodes = list(elem)
    child_elements = []
    child_comments = []
    for node in nodes:
        if isinstance(node, ET._Comment):
            child_comments.append(node)
        else:
            child_elements.append(node)

    # Handle comments that annotate THIS element
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

        # Apply usage/deprecation about this element at its parent's context (direct child checks)
        if any(u == 'forbidden' for u in usages):
            builder.add_rule_absence(parent_abs_path, tag_local, note_text=note_text)
        if any(u == 'mandatory' for u in usages):
            builder.add_rule_presence(parent_abs_path, tag_local, note_text=note_text)
        if deprecated:
            builder.add_rule_deprecated(parent_abs_path, tag_local, note_text=note_text)

        # Allowed enums on this element's own value: attach at element's absolute path, test '.'
        if allowed_enums:
            builder.add_rule_allowed_enums(
                elem_abs_path,
                '.',
                allowed_enums,
                note_text=note_text
            )

        # class-id-must-exist: attach at element's absolute path, using the element's own @id
        if class_id_must_exist:
            id_value = elem.get('id')
            builder.add_rule_class_id_must_exist(
                elem_abs_path,
                tag_local,
                id_value,
                note_text=note_text
            )

        # Handle referenced fragments for this element
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
                                rootfrag = ET.fromstring(wrapped.encode('utf-8'))
                            except Exception as e:
                                print(
                                    f'Warning: parse error in referenced file {found_path}: {e}',
                                    file=sys.stderr
                                )
                                continue
                            # Base context is the element itself; parent context is its parent
                            _process_fragment_root(
                                rootfrag,
                                builder,
                                base_context_path=elem_abs_path,
                                parent_context_path=parent_abs_path,
                                element_local_name=tag_local,
                                input_folder=input_folder
                            )

    # Recurse into child elements; they will append to elem_abs_path
    for child in child_elements:
        process_element_tree(
            child,
            builder,
            parent_context_path=elem_abs_path,
            input_folder=input_folder,
            is_ref_root=False
        )


def _parent_of_abs_path(abs_path: str) -> str:
    """Return the parent path of an absolute namespaced path, or '' if none."""
    if not abs_path or '/' not in abs_path:
        return ''
    return abs_path.rsplit('/', 1)[0]


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
    parser.add_argument(
        '-r', '--root-element',
        default='PublicationDelivery',
        help='Root element to start processing from (default: PublicationDelivery).'
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
    root_element = args.root_element

    # Validate inputs
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
            root = ET.fromstring(wrapped.encode('utf-8'))
        except Exception as e:
            print(f'Error parsing extracted region: {e}', file=sys.stderr)
            continue

        # Start traversal from the specified root element
        root_element_found = False
        for node in list(root):
            if isinstance(node, ET._Comment):
                # We ignore top-level comments for schematron generation in this absolute-path mode
                ctext = (node.text or '').strip()
                warn_on_unknown_ch_commands(ctext, location_desc="top-level template region")
                # No top-level asserts created (no '.' contexts).
                continue
            else:
                node_local = local_name(node.tag)
                if node_local == root_element:
                    # Start absolute path at the specified root element (no parent)
                    process_element_tree(
                        node,
                        builder,
                        parent_context_path='',
                        input_folder=input_folder,
                        is_ref_root=False
                    )
                    root_element_found = True
                else:
                    # Skip non-root elements to enforce a single absolute root
                    if VERBOSE:
                        print(f"Skipping top-level element '{node_local}' (only {root_element} is used as absolute root).")

        if not root_element_found:
            print(f"Warning: Root element '{root_element}' not found in template. No rules generated.", file=sys.stderr)

    out = builder.tostring()
    write_file(output_path, out)
    print(f'Wrote schematron to {output_path}. Rules created: {builder.rules_created}')


if __name__ == '__main__':
    main(sys.argv)