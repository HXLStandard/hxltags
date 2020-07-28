""" Compile a model for matching text headers to HXL hashtags

The input data should be in the format produced by the hdx-hashtag-crawler module:

https://github.com/HXLStandard/hdx-hashtag-crawler

Save the model to disk, then load it for use with the hxltags.lookup module

Command-line use:

    $ python3 -m hxltags.compiler raw-hashtag-output.csv > compiled-model.json

Python use:

    from hxltags.compiler import build_model

    model = build_model("raw-hashtag-output.csv")

"""

import hxl, json, sys

from hxltags.common import tokenise, explode

def build_model(filename):
    """ Build a model for classifying headers """
    model = {}
    source = hxl.data(filename, allow_local=True)
    for i, row in enumerate(source.dedup("meta+header,meta+tagspec,meta+hash")):
        header = row.get("#meta+header")
        tagspec = row.get("meta+tagspec")

        if not header:
            continue

        tokens = tokenise(header)
        for seg in explode(tokens):
            if not seg in model:
                model[seg] = {}
            if tagspec in model[seg]:
                model[seg][tagspec] += 1
            else:
                model[seg][tagspec] = 1

    return model


#
# Run from the command line
#

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <raw-input-data>".format(sys.argv[0]), file=sys.stderr)
        exit(2)

    model = build_model(sys.argv[1])
    json.dump(list(model.items()), sys.stdout)
    
