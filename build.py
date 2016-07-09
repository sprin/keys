#! /usr/bin/env python3
import argparse
import sys

import misaka

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Keys of Steffen Prince (sprin)</title>
</head>
<body>
<html>
<head>
</head>
<body>
<div>
{0}
</div>
</body>
</html>
"""


def main(args=None):
    md = sys.stdin.read()
    html = misaka.html(md, extensions=('fenced-code',))
    doc = TEMPLATE.format(html)
    sys.stdout.write(doc)


if __name__ == '__main__':
    sys.exit(main())
