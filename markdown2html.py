#!/usr/bin/python3
'''
A markdown2html script
'''
import os
import sys
import re


def markdown2html(mark_content):
    """Creates a heading pattern for html syntax"""
    heading_patterns = [
        (re.compile(r'###### (.*)'), r'<h6>\1</h6>'),
        (re.compile(r'##### (.*)'), r'<h5>\1</h5>'),
        (re.compile(r'#### (.*)'), r'<h4>\1</h4>'),
        (re.compile(r'### (.*)'), r'<h3>\1</h3>'),
        (re.compile(r'## (.*)'), r'<h2>\1</h2>'),
        (re.compile(r'# (.*)'), r'<h1>\1</h1>')
    ]

    html_content = mark_content

    for pattern, replacement in heading_patterns:
        html_content = pattern.sub(replacement, html_content)

    """ Detects and convert ordered and unordered lists"""
    lines = html_content.split('\n')
    in_unordered_list = False
    in_ordered_list = False
    unordered_list_items = []
    ordered_list_items = []

    def generate_list_html(items, list_type):
        html_list = f'<{list_type}>\n' + ''.join(f'    <li>{item}</li>\n' for item in items) + f'</{list_type}>'
        return html_list

    for line in lines:
        if line.startswith('- '):
            if in_ordered_list:
                yield generate_list_html(ordered_list_items, 'ol')
                ordered_list_items = []
                in_ordered_list = False
            unordered_list_items.append(line[2:])
            in_unordered_list = True
        elif line.startswith('* '):
            if in_unordered_list:
                yield generate_list_html(unordered_list_items, 'ul')
                unordered_list_items = []
                in_unordered_list = False
            ordered_list_items.append(line[2:])
            in_ordered_list = True
        else:
            if in_unordered_list:
                yield generate_list_html(unordered_list_items, 'ul')
                unordered_list_items = []
                in_unordered_list = False
            if in_ordered_list:
                yield generate_list_html(ordered_list_items, 'ol')
                ordered_list_items = []
                in_ordered_list = False
            yield line

    if unordered_list_items:
        yield generate_list_html(unordered_list_items, 'ul')
    if ordered_list_items:
        yield generate_list_html(ordered_list_items, 'ol')


def main():
    """Checks if the script takes only 2 arguments."""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    """Checks if the input file exists"""
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, 'r') as infile:
        markdown_content = infile.read()

    html_content = ''.join(markdown2html(markdown_content))

    with open(output_file, 'w') as outfile:
        outfile.write(html_content)

    sys.exit(0)


if __name__ == "__main__":
    main()
