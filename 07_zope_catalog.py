#!/usr/bin/env python

import json
import transaction
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList

from common import db_setup


def load_data(fname):
    fd = open(fname, 'r')
    data = fd.read().decode('utf-8')
    return json.loads(data)


if __name__ == '__main__':
    json_data = load_data('media/dataSep-7-2014.json')
    _, root_node = db_setup()
    root_node['data'] = PersistentList()
    for d in json_data:
        root_node['data'].append(PersistentMapping(d))
    transaction.commit()
    #import ipdb; ipdb.set_trace()
