""" Build a machine-learning model mapping text headers to HXL hashtags """

import hxl
from textblob.classifiers import NaiveBayesClassifier as NBC

INPUT="inputs/20200720-hxl-tags-atts.csv"
""" Input data for supervised learning """

TEST_SAMPLE=100
""" Save every nth example for the test corpus """

training_corpus = []
""" Corpus of header+tagspec tuples for training the model """

test_corpus = []
""" Corpus of header+tagspec tuples for testing the model """

print("Building corpora...")

# Read the data from the HXL file
source = hxl.data(INPUT, allow_local=True)
for i, row in enumerate(source.dedup("meta+header,meta+tagspec,meta+hash")):
    header = hxl.datatypes.normalise_string(row.get("#meta+header"))
    tagspec = row.get("meta+tagspec")
    if len(header) > 0:
        if (i % TEST_SAMPLE) == 0:
            test_corpus.append((header, tagspec))
        else:
            training_corpus.append((header, tagspec))

print("{} entries in training corpus".format(len(training_corpus)))
print("{} entries in test corpus".format(len(test_corpus)))

# Build the model and show the most-informative features
print("Building model...")
model = NBC(training_corpus)
model.show_informative_features(10)

# Test the model's accuracy against the test corpus
print("Testing accuracy...")
print("Accuracy is {}".format(model.accuracy(test_corpus)))
