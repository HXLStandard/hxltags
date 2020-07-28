""" Look up a HXL tagspec based on a text header

First, build and save a JSON-formatted model using the hxltags.compiler module.

Command-line use:

    $ python3 -m hxltags.lookup my-saved-model.json

Python use:

    from hxltags.compiler import load_model, lookup_header

    with open("my-saved-model.json", "r") as stream:
        model = load_model(stream)
        results = lookup_header("Number of people affected", model)

"""

import json, sys
from hxltags.common import tokenise, explode

def load_model(stream):
    model = {}
    for item in json.load(stream):
        model[tuple(item[0])] = item[1]
    return model

def lookup_header(header, model):
    results = {}
    tokens = tokenise(header)
    for seg in explode(tokens):
        if seg in model:
            l = len(seg) # the longer the segment, the higher the weight
            for tagspec in model[seg]:
                if not tagspec in results:
                    results[tagspec] = 0
                results[tagspec] += model[seg][tagspec] * l

    r = list(results.items())
    r.sort(reverse=True, key=lambda i: i[1])
    return r


#
# Called from the command-line
#
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <compiled-model>".format(sys.argv[0]), file=sys.stderr)
        exit(2)
        
    filename = sys.argv[1]
    with open(filename, "r") as stream:
        model = load_model(stream)

    s = input("\nColumn header: ")
    while s:
        matches = lookup_header(s, model)
        for i, match in enumerate(matches):
            if i >= 5:
                break
            print("  ", match[0], match[1])
        s = input("\nColumn header: ")
