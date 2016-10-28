# -*- coding: utf-8 -*-

# NLP Functions

# == IMPORTS =============================================================#
import re
import nltk
import itertools
# == IMPORTS END =========================================================#

# ========================== Claim Functions =============================#

def traverse(t, np=False):
    try:
        t.label()
    except AttributeError:
        # This is then a tuple e.g. ('A', 'DT') which is a leaf of the tree
        if np:
            print(t[0], end=" ")
    else:
        # Now we know that t.node is defined
        if "S" in t.label():
            for child in t:
                traverse(child)
        elif "NP" in t.label():
            for child in t:
                traverse(child, np=True)
            print("")

def ends_with(s1, s2):
    """See if s1 ends with s2."""
    pattern = re.compile(r'(' + re.escape(s2) + ')$')
    located = pattern.search(s1)
    if located:
        return True
    else:
        return False
            
def nouns(pos):
    """ Return the nouns from the claim.
    param: pos - list of tuples from nltk pos tagger"""
    return [word for word, part in pos if "NN" in part]

def get_words(text):
    """ Tokenise text into words. """
    words = nltk.word_tokenize(text)
    return words
    
def get_pos(words):
    """ Label parts of speech - uses averaged_perceptron_tagger """
    pos = nltk.pos_tag(words)
    return pos

def remove_ref_nums(text):
    """ Remove reference numerals from the claim text. """
    pass


def get_number(text):
    """Extracts the claim number from the text."""
    p = re.compile('\d+\.')
    located = p.search(text)
    if located:
        # Set claim number as digit before fullstop
        number = int(located.group()[:-1])
        text = text[located.end():].strip()
    else:
        number = None
        text = text
    return number, text
    
def detect_category(text):
    """Attempts to determine and return a string containing the claim category."""
    p = re.compile('(A|An|The)\s([\w-]+\s)*(method|process)\s(of|for)?')
    located = p.search(text)
    # Or store as part of claim object property?
    if located:
        return "method"
    else:
        return "system"

def determine_entities(pos):
    """ Determines noun entities within a patent claim.
    param: pos - list of tuples from nltk pos tagger"""
    # Define grammar for chunking
    grammar = '''
        NP: {<DT|PRP\$> <VBG> <NN.*>+} 
            {<DT|PRP\$> <NN.*> <POS> <JJ>* <NN.*>+}
            {<DT|PRP\$>? <JJ>* <NN.*>+ }
        '''
    cp = nltk.RegexpParser(grammar)
    # Or store as part of claim object property?
    
    # Option: split into features / clauses, run over clauses and then re-correlate
    return cp.parse(pos)
    
def print_nps(pos):
    ent_tree = determine_entities(pos)
    traverse(ent_tree)

def detect_dependency(text):
    """Attempts to determine if the claim set out in text is dependent - if it is dependency is returned - if claim is deemed independent 0 is returned as dependency """
    p = re.compile('(of|to|with|in)?\s(C|c)laims?\s\d+((\sto\s\d+)|(\sor\s(C|c)laim\s\d+))?(,\swherein)?')
    located = p.search(text)
    if located:
        num = re.compile('\d+')
        dependency = int(num.search(located.group()).group())
    else:
        # Also check for "preceding claims" or "previous claims" = claim 1
        pre = re.compile('\s(preceding|previous)\s(C|c)laims?(,\swherein)?')
        located = pre.search(text)
        if located:
            dependency = 1
        else:
            dependency = 0
    # Or store as part of claim object property?
    return dependency

def split_into_features(text):
    """ Attempts to split a claim into features.
    param string text: the claim text as a string
    """
    featurelist = []
    startindex = 0
    #split_re = r'(.+;\s*(and)?)|(.+,.?(and)?\n)|(.+:\s*)|(.+\.\s*$)'
    split_expression = r'(;\s*(and)?)|(,.?(and)?\n)|(:\s*)|(\.\s*$)'
    p = re.compile(split_expression)
    for match in p.finditer(text):
        feature = {}
        feature['startindex'] = startindex
        endindex = match.end()
        feature['endindex'] = endindex
        feature['text'] = text[startindex:endindex]
        featurelist.append(feature)
        startindex = endindex
    # Try spliting on ';' or ',' followed by '\n' or ':'
    #splitlist = filter(None, re.split(r";|(,.?\n)|:", text))
    # This also removes the characters - we want to keep them - back to search method?
    # Or store as part of claim object property?
    return featurelist
    
def label_nounphrases(ptree):
    """ Label noun phrases in the output from pos chunking. """
    subtrees = ptree.subtrees(filter=lambda x: x.label()=='NP')
    
    # build up mapping dict - if not in dict add new entry id+1; if in dict label using key
    mapping_dict = {}
    pos_to_np = []
    for st in subtrees:
        np_string = " ".join([leaf[0] for leaf in st.leaves() if leaf[1] != ("DT" or "PRP$")])
        np_id = mapping_dict.get(np_string, None)
        if not np_id:
            # put ends_with here
            nps = [i[0] for i in mapping_dict.items()]
            ends_with_list = [np for np in nps if ends_with(np_string, np)]
            if ends_with_list:
                np_id = mapping_dict[ends_with_list[0]]
            else:
                np_id = len(mapping_dict)+1
                mapping_dict[np_string] = np_id
        pos_to_np.append((st.parent_index(), np_id))
    return (pos_to_np, mapping_dict)
    
# ========================== Claimset Functions ============================#
def clean_data(claim_data):
    """ Cleans and checks claim data returned from EPO OPS. """
    
    # If claims_data is a single string attempt to split into a list
    if not isinstance(claim_data, list):
        claim_data = extract_claims(claim_data)
    
    claims = [get_number(claim) for claim in claims_list]
    
    for claim_no in range(1, len(claims)):
        if claims[claim_no-1][0] != claim_no:
            pass
            
    # Checks
    # - len(claims) = claims[-1] number
    # - 

def extract_claims(text):
    """ Attempts to extract claims as a list from a large text string.
    param string text: string containing several claims
    """
    sent_list = nltk.tokenize.sent_tokenize(text)
    # On a test string this returned a list with the claim number and then the
    # claim text as separate items
    claims_list = [" ".join(sent_list[i:i+2]) for i in xrange(0, len(sent_list), 2)]
    return claims_list
