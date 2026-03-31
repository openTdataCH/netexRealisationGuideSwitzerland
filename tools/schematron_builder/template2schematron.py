#!/usr/bin/env python3
"""
template2schematron.py

Usage:
    python template2schematron.py <template_file> <xsd_file> <input_folder> <output_file>

Recognizes comment directives:
  - ch-note: <text>
  - ch-usage: mandatory|forbidden
  - ch-referenced
  - ch-allowed-enums: val1 val2 val3

See code for behaviour details.
"""
import sys
import os
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

# Markers
START_MARKER = "ch-start"
END_MARKER = "ch-end"

RE_NOTE = re.compile(r'\bch-note\s*:\s*(.*)', re.IGNORECASE)
RE_USAGE = re.compile(r'\bch-usage\s*:\s*(\w+)', re.IGNORECASE)
RE_REFERENCED = re.compile(r'\bch-referenced\b', re.IGNORECASE)
RE_REFERENCED_ALT = re.compile(r'\breferenced\b', re.IGNORECASE)
RE_ALLOWED_ENUMS = re.compile(r'\bch-allowed-enums\s*:\s*(.+)', re.IGNORECASE)

def usage():
    print("Usage: python template2schematron.py <template_file> <xsd_file> <input_folder> <output_file>")
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
    return '<?xml version="1.0" encoding="utf-8"?><__root__>' + fragment + '</__root__>'

def parse_usage_and_notes_from_comments(comment_text):
    notes = RE_NOTE.findall(comment_text)
    usages = RE_USAGE.findall(comment_text)
    referenced = bool(RE_REFERENCED.search(comment_text) or RE_REFERENCED_ALT.search(comment_text))
    allowed_match = RE_ALLOWED_ENUMS.search(comment_text)
    allowed = []
    if allowed_match:
        vals = allowed_match.group(1).strip()
        # split on whitespace; keep tokens as-is
        allowed = [v for v in re.split(r'\s+', vals) if v != '']
    return {
        'notes': [n.strip() for n in notes] if notes else [],
        'usages': [u.strip().lower() for u in usages] if usages else [],
        'referenced': referenced,
        'allowed_enums': allowed
    }

def local_name(tag):
    if tag is None:
        return ''
    m = re.match(r'\{.*\}(.*)', tag)
    return m.group(1) if m else tag

class SchematronBuilder:
    def __init__(self, xsd_path):
        self.xsd_path = xsd_path
        self.schema = Element('schema', attrib={'xmlns': 'http://purl.oclc.org/dsdl/schematron'})
        title = SubElement(self.schema, 'title')
        title.text = 'Generated schematron from template'
        self.pattern = SubElement(self.schema, 'pattern', attrib={'id': 'p1'})
        self.processed_files = set()
        self.rules_created = 0

    def add_comment_to_rule(self, parent, text):
        parent.append(ET.Comment(' ' + text + ' '))

    def add_rule_presence(self, context_xpath, element_name, note_text=None):
        rule = SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        SubElement(rule, 'assert', attrib={'test': f'count({element_name}) &gt; 0'}).text = f'{element_name} must be present'
        self.rules_created += 1

    def add_rule_absence(self, context_xpath, element_name, note_text=None):
        rule = SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        SubElement(rule, 'assert', attrib={'test': f'count({element_name}) = 0'}).text = f'{element_name} must NOT be present'
        self.rules_created += 1

    def add_rule_allowed_enums(self, context_xpath, element_name, allowed_list, note_text=None):
        """
        Generate an assertion that element_name's string value must be one of allowed_list.
        We create a rule targeting the element's parent context (or '.' if element itself is the context)
        and use an assert like: count(element_name[. = ('a','b')]) &gt; 0
        """
        if not allowed_list:
            return
        # produce a CSV of quoted values for XPath literal lists
        # Note: XPath 1.0 doesn't have sequence literals; we use multiple equality ORs instead
        ors = ' or '.join([f"{element_name} = '{val}'" for val in allowed_list])
        rule = SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        SubElement(rule, 'assert', attrib={'test': ors}).text = f'{element_name} must be one of: {" ".join(allowed_list)}'
        self.rules_created += 1

    def tostring(self):
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(self.schema, encoding='unicode')

def find_file_by_tagname(input_folder, tagname):
    target = f'{tagname}.xml'
    for root, dirs, files in os.walk(input_folder):
        for f in files:
            if f == target:
                return os.path.join(root, f)
    return None

def process_element_tree(elem, builder, context_xpath='.', input_folder='.', ancestor_forbidden=False):
    if ancestor_forbidden:
        return

    # gather directives from direct child comments
    notes = []
    usages = []
    referenced = False
    allowed_enums = []
    for node in list(elem):
        if node.tag is ET.Comment:
            parsed = parse_usage_and_notes_from_comments((node.text or '').strip())
            notes.extend(parsed['notes'])
            usages.extend(parsed['usages'])
            if parsed['referenced']:
                referenced = True
            if parsed['allowed_enums']:
                allowed_enums.extend(parsed['allowed_enums'])

    tag_local = local_name(elem.tag)
    is_forbidden = any(u == 'forbidden' for u in usages)
    is_mandatory = any(u == 'mandatory' for u in usages)

    if is_forbidden:
        builder.add_rule_absence(context_xpath, tag_local, note_text='; '.join(notes) if notes else None)
        return

    if is_mandatory:
        builder.add_rule_presence(context_xpath, tag_local, note_text='; '.join(notes) if notes else None)

    if allowed_enums:
        # create rule that the element's value must be one of allowed_enums
        # context: we keep same context_xpath as for presence rules (parent)
        builder.add_rule_allowed_enums(context_xpath, tag_local, allowed_enums, note_text='; '.join(notes) if notes else None)

    # process referenced files if any
    if referenced:
        found = find_file_by_tagname(input_folder, tag_local)
        if found:
            ab = os.path.abspath(found)
            if ab not in builder.processed_files:
                builder.processed_files.add(ab)
                try:
                    txt = read_file(found)
                except Exception as e:
                    print(f'Warning: cannot read referenced file {found}: {e}', file=sys.stderr)
                else:
                    regions = extract_regions(txt)
                    if not regions:
                        regions = [txt]
                    for r in regions:
                        wrapped = wrap_fragment(r)
                        try:
                            root = ET.fromstring(wrapped)
                        except ET.ParseError as e:
                            print(f'Warning: parse error in referenced file {found}: {e}', file=sys.stderr)
                            continue
                        for child in list(root):
                            if child.tag is ET.Comment:
                                continue
                            process_element_tree(child, builder, context_xpath=f'.//{tag_local}', input_folder=input_folder, ancestor_forbidden=False)
        else:
            print(f'Warning: referenced file for element {tag_local} not found under {input_folder}', file=sys.stderr)

    # recurse into children
    for child in list(elem):
        if child.tag is ET.Comment:
            continue
        process_element_tree(child, builder, context_xpath=f'.//{tag_local}', input_folder=input_folder, ancestor_forbidden=False)

def main(argv):
    if len(argv) != 5:
        usage()
    _, template_path, xsd_path, input_folder, output_path = argv

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
        print('Warning: no regions found between markers; attempting to process entire file', file=sys.stderr)
        regions = [txt]

    builder = SchematronBuilder(xsd_path)

    for region in regions:
        wrapped = wrap_fragment(region)
        try:
            root = ET.fromstring(wrapped)
        except ET.ParseError as e:
            print(f'Error parsing extracted region: {e}', file=sys.stderr)
            continue
        for child in list(root):
            if child.tag is ET.Comment:
                continue
            process_element_tree(child, builder, context_xpath='.', input_folder=input_folder, ancestor_forbidden=False)

    out = builder.tostring()
    write_file(output_path, out)
    print(f'Wrote schematron to {output_path}. Rules created: {builder.rules_created}')

if __name__ == '__main__':
    main(sys.argv)

