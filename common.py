#!/usr/bin/env python
from os import remove


def fs_cleanup():
    for fname in ('fruits.fs', 'fruits.fs.index', 'fruits.fs.lock',
                  'fruits.fs.tmp'):
        try:
            remove(fname)
        except OSError:
            pass
