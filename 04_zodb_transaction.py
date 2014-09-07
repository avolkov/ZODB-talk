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
    import pdb; pdb.set_trace()
    print "**fruit' child"
    print root_node['fruit']
    # add vegetable node
    root_node['vegetable'] = vegetable
    transaction.commit()
    print "**fruits & vegetables"
    print root_node
    import pdb; pdb.set_trace()
    print
    print "**transaction history length: ",
    print len(db.undoInfo())
    import pdb; pdb.set_trace()
    print "** undo last transaction: "
    last_transaction = db.undoInfo()[0]
    db.undo(last_transaction['id'])
    print "** transaction not yet committed"
    print root_node
    import pdb; pdb.set_trace()
    transaction.commit()
    print "** addition of vegetables is undone"
    print root_node
    import pdb; pdb.set_trace()
    print "** history log grew: ",
    print len(db.undoInfo())
