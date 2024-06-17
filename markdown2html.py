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

    return html_content


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

    html_content = markdown2html(markdown_content)

    with open(output_file, 'w') as outfile:
        outfile.write(html_content)

    sys.exit(0)


if __name__ == "__main__":
    main()
