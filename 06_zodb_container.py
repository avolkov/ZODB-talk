#!/usr/bin/env python

import transaction
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList

from itertools import cycle

from common import db_setup

fruit = {
    'apple': {"color": "red", "weight": 182},
    'banana': {"color": "yellow", "weight": 118},
    'pear': {"color": "green", "weight": 192}

}

season_fruit = {
    'apple': {'color': 'yellow', 'weight': 191},
    'peach': {'color': 'yellow/red', 'weight': 150},
    'corn cob': {'color': 'green', 'weight': 160},
    'watermellon': {'color': 'green/black', 'weight': 3523}

}


class Fruit(PersistentMapping):
    '''
    dictionary-like persistent container object
    '''
    def __init__(self, name):
        super(self.__class__, self).__init__()
        self.name = name


class Basket(PersistentList):
    '''
    list-like persistent container object
    '''
    def __init__(self, name):
        super(self.__class__, self).__init__()
        self.name = name


def persistent_fruit(k, v):
    f = Fruit(k)
    for kv, vv in v.iteritems():
        f[kv] = vv
    return f


if __name__ == "__main__":
    _, root_node = db_setup()

    for k, v in fruit.iteritems():
        f = Fruit(k)
        #import ipdb; ipdb.set_trace()
        f['color'] = v['color']
        f['weight'] = v['weight']
        root_node[k] = f
    transaction.commit()
    print "Persistent Fruit: ",
    print root_node
    print "Modifying Persistent Fruit (pear):",
    root_node['pear']['color'] = 'yellow'
    transaction.commit()
    print root_node['pear']

    basket = Basket("Season's harvest")
    harvest = (
        x for x in cycle(
            (persistent_fruit(k, v) for k, v in season_fruit.iteritems())
        )
    )

    for k in range(100):
        basket.append(harvest.next())
    root_node['basket'] = basket
    transaction.commit()
    print "Basket length: %d" % len(root_node['basket'])
    random_fruit = root_node['basket'][33]
    print "Random Fruit: ",
    print random_fruit.name,
    print random_fruit
