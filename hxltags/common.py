""" Common library functions for the hxltags package """

import re

def normalise(s):
    """ Normalise a string """
    s = re.sub(r"[^\w-]+", " ", s)
    s = re.sub(r"  +", " ", s)
    s = re.sub(r"^[\s]+", "", s)
    s = re.sub(r"[\s]+$", "", s)
    return s.lower()

def tokenise(s):
    """ Tokenise a string around whitespace """
    return normalise(s).split(" ")

def explode(tokens):
    """ Explode a list of tokens into all possible lengths """
    l = len(tokens)
    for start in range(0, l):
        for span in range(0, l-start):
            yield tuple(tokens[start:start+span+1])

