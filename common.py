#!/usr/bin/env python
from ZODB import DB, FileStorage
from os import remove


def fs_cleanup():
    for fname in ('fruits.fs', 'fruits.fs.index', 'fruits.fs.lock',
                  'fruits.fs.tmp'):
        try:
            remove(fname)
        except OSError:
            pass


def db_setup():
    """
    Open database connection
    storage -> database -> connection -> root node
    """
    fs_cleanup()
    storage = FileStorage.FileStorage('fruits.fs')
    db = DB(storage)
    connection = db.open()
    return (db, connection.root())
