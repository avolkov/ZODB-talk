#!/usr/bin/env python

import pickle

#from pickle_write import Fruit


def load_stuff(name):
    fd = open(name, 'r')
    out = pickle.load(fd)
    fd.close()
    return out

if __name__ == "__main__":
    print "Loading dictionary"
    print load_stuff('fruits_dict.pkl')
    print
    print
    print "Loading objects"
    print load_stuff('fruits_obj.pkl')
    print
