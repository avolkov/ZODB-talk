#!/usr/bin/env python

import json

import transaction
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList

from repoze.catalog.indexes.text import CatalogTextIndex
from repoze.catalog.catalog import Catalog
from repoze.catalog.query import Eq, Contains

from common import db_setup


## loading json data in the database
def load_json(fname):
    fd = open(fname, 'r')
    data = fd.read().decode('utf-8')
    return json.loads(data)


def load_data(fname, root_node):
    json_data = load_json(fname)
    root_node['data'] = PersistentList()
    for d in json_data:
        root_node['data'].append(PersistentMapping(d))

## preparing catalog


def get_email(obj, default):
    return obj['email'] if obj['email'] else default


def get_country(obj, default):
    return obj['country'] if obj['country'] else default


class PersistentCatalog(Catalog, PersistentMapping):
    index_count = 0

    def next_index(self):
        cur_index = self.index_count
        self.index_count += 1
        return cur_index


if __name__ == '__main__':
    _, root_node = db_setup()
    ## Load sample generated by http://www.generatedata.com/
    load_data('media/dataSep-7-2014.json', root_node)
    transaction.commit()
    ## Preparing catalog
    ## see http://docs.repoze.org/catalog/overview.html
    nodes = {}
    catalog = PersistentCatalog()
    root_node['catalog'] = catalog
    catalog['email'] = CatalogTextIndex(get_email)
    catalog['country'] = CatalogTextIndex(get_country)
    for d in root_node['data']:
        ni = catalog.next_index()
        nodes[ni] = d
        catalog.index_doc(ni, d)
    (q_count, q_result) = catalog.query(Eq('country', "Belgium"))
    print "Number of results: %d" % q_count
    print "Items:"
    for res in q_result.items():
        print nodes[res[0]]
