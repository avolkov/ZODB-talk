#!/usr/bin/env python

import transaction
from ZODB import DB, FileStorage

fruit = {
    'apple': {"color": "red", "weight": 182},
    'banana': {"color": "yellow", "weight": 118},
    'pear': {"color": "green", "weight": 192}

}

vegetable = {
    'pickle': {"color": "green", "weight": 39}
}


def db_setup():
    """
    Open database connection
    storage -> database -> connection -> root node
    """
    storage = FileStorage.FileStorage('fruits.fs')
    db = DB(storage)
    connection = db.open()
    return (db, connection.root())


if __name__ == "__main__":
    db, root_node = db_setup()
    print "** display root node containing 'fruit' child"
    print root_node
    print "** display 'fruit' child"
    print root_node['fruit']
    print "** display transaction history"
    print db.undoInfo()
    print "** undo last transaction"
    db.undo(db.undoInfo()[0])
    print root_node
    import ipdb; ipdb.set_trace()
