#!/usr/bin/env python

import transaction
from ZODB import DB, FileStorage

from common import fs_cleanup

fruit = {
    'apple': {"color": "red", "weight": 182},
    'banana': {"color": "yellow", "weight": 118},
    'pear': {"color": "green", "weight": 192}

}


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


if __name__ == "__main__":
    _, root_node = db_setup()
    # print empty db
    print root_node
    # add child node
    root_node['fruit'] = fruit
    print root_node
    transaction.commit()
