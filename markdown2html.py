#!/usr/bin/python3
'''
A markdown2html script
'''
import os
import sys


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

    # Convert Markdown to HTML
    try:
        import markdown
    except ImportError:
        print("The 'markdown' package is required.", file=sys.stderr)
        sys.exit(1)

    html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as outfile:
        outfile.write(html_content)

    sys.exit(0)


if __name__ == "__main__":
    main()
