# -*- coding: utf-8 -*-

import patentparser.nlpfunctions

#from patentparser.nlpfunctions import get_number, detect_category, determine_entities, \
                        #detect_dependency, nouns, split_into_features, \
                        #split_into_features, get_words, get_pos 

#Download NLTK modules if not already present
#nltk.download("punkt")
#nltk.download("stopwords")
#nltk.download("averaged_perceptron_tagger")

class ApplnState:
    """ Object to model a state of a patent document. """
    pass

class PatentDoc:
    """ Object to model a patent document. """
    pass

class Description:
    """ Object to model a patent description. """
    pass

class Claimset:
    """ Object to model a claim set. """ 
    pass

class Figures:    
    """ Object to model a set of patent figures. """
    pass

class Claim:
    """ Object to model a patent claim."""

    def __init__(self, claimstring):
        """ Initiate claim object with string containing claim text."""
        # Load text
        self.text = claimstring
        # Check for and extract claim number
        self.number, self.text = patentparser.nlpfunctions.get_number(claimstring)
        # Get category
        self.category = patentparser.nlpfunctions.detect_category(self.text)
        # Get dependency
        self.dependency = patentparser.nlpfunctions.detect_dependency(self.text)
        
        # Tokenise text into words
        self.words = patentparser.nlpfunctions.get_words(self.text)
        # Label parts of speech - uses averaged_perceptron_tagger as downloaded above
        self.pos = patentparser.nlpfunctions.get_pos(self.words)
        # Apply chunking into noun phrases
        (self.word_data, self.mapping_dict) = patentparser.nlpfunctions.label_nounphrases(self.pos)
        
        #Split claim into features
        self.features = patentparser.nlpfunctions.split_into_features(self.text)

    def json(self):
        """ Provide words as JSON. """
        # Add consecutive numbered ids for Reactgit@github.com:benhoyle/python-epo-ops-client.git
        #words = [{"id": i, "word":word, "pos":part} for i, (word, part) in list(enumerate(self.pos))]
        words = [{"id": i, "word":word, "pos":part, "np":np} for i, (word, part, np) in list(enumerate(self.word_data))]
        return {"claim":{ "words":words }}

