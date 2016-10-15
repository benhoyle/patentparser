# -*- coding: utf-8 -*-

from .nlpfunctions import get_number, detect_category, determine_entities, \
                        detect_dependency, nouns, split_into_features, \
                        split_into_features, 

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
        self.number, self.text = self.get_number()
        # Get category
        self.category = self.detect_category()
        # Get dependency
        self.dependency = self.detect_dependency()
        
        # Tokenise text into words
        self.words = nltk.word_tokenize(self.text)
        # Label parts of speech - uses averaged_perceptron_tagger as downloaded above
        self.pos = nltk.pos_tag(self.words)
        
        #Split claim into features
        self.features = self.split_into_features()



