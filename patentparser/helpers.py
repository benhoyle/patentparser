# -*- coding: utf-8 -*-

# Generic helper functions

def check_list(listvar):
    if not isinstance(listvar, list):
        listvar = [listvar]
    return listvar
    
def safeget(dct, *keys):
    """ Recursive function to safely access nested dicts or return None. 
    param dict dct: dictionary to process
    param string keys: one or more keys"""
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct