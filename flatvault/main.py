#!/usr/bin/python
"""
Decrypt, edit, and encrypt a file.
"""
from __future__ import print_function
import optparse
from flatvault import editor


def usage(name):
    return "Usage: %s <filename>" % name


def main():
    import sys
    if not len(sys.argv) == 2:
        print(usage(sys.argv[0]))
        raise SystemExit()

    editor.edit_file(sys.argv[1])


if __name__ == "__main__":
    main()
