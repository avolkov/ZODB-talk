#!/usr/bin/env python

import transaction
import persistent
from ZODB import DB, FileStorage

from common import fs_cleanup

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
    fs_cleanup()
    storage = FileStorage.FileStorage('fruits.fs')
    db = DB(storage)
    connection = db.open()
    return (db, connection.root())


class Fruit(persistent.Persistent):
    def __init__(self, name, color, weight):
        self.name, self.color, self.weight = name, color, weight

    def __repr__(self):
        return "<name: %s color: %s weight: %d>" % \
            (self.name, self.color, self.weight)

if __name__ == '__main__':
    _, root_node = db_setup()

    for k, v in fruit.iteritems():
        root_node[k] = Fruit(k, v['color'], v['weight'])
    transaction.commit()
    print "*root node is"
    print root_node
