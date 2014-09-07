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
    print "**root node containing 'fruit' child"
    print root_node
    print "**fruit' child"
    print root_node['fruit']
    # add vegetable node
    root_node['vegetable'] = vegetable
    transaction.commit()
    print "**fruits & vegetables"
    print root_node
    print
    print
    print "**transaction history"
    print len(db.undoInfo())

    print "** undo last transaction"
    #last_transaction = db.undoInfo()[0]
    db.undo(db.undoInfo()[0]['id'])
    #db.undo(db.undoInfo()[0]['id'])
    print root_node
    transaction.commit()
    print len(db.undoInfo())
    import ipdb; ipdb.set_trace()
