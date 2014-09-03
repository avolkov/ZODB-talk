#!/usr/bin/env python

import pickle

fruit = {
    'apple': {"color": "red", "weight": 182},
    'banana': {"color": "yellow", "weight": 118},
    'pear': {"color": "green", "weight": 192}

}


class Fruit(object):
    def __init__(self, name, color, weight):
        self.name, self.color, self.weight = name, color, weight

    def __repr__(self):
        return "<name: %s color: %s weight: %d>" % \
            (self.name, self.color, self.weight)


def save_dict():
    fname = open('fruits_dict.pkl', 'w')
    pickle.dump(fruit, fname, pickle.HIGHEST_PROTOCOL)
    fname.close()


def save_obj():
    fruits = []
    fname = open('fruits_obj.pkl', 'w')
    for name, opt in fruit.iteritems():
        fruits.append(Fruit(name, opt['color'], opt['weight']))
    pickle.dump(fruits, fname, pickle.HIGHEST_PROTOCOL)
    fname.close()


if __name__ == "__main__":
    save_dict()
    save_obj()
