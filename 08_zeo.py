#!/usr/bin/env python

from ZEO import ClientStorage
from ZODB import DB

if __name__ == '__main__':
    addr = 'localhost', 9001
    storage = ClientStorage.ClientStorage(addr)
    db = DB(storage)
    conn = db.open()
    root_node = conn.root()
    print "Sample retrieved persistent data:"
    print root_node['data'][33]
