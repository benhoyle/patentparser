import re
from nltk.tokenize import sent_tokenize

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
    return dependency

def detect_category(text):
    """Attempts to determine and return a string containing the claim category, initially from a choice of two: (method or process - "method") OR (system/product/apparatus - "system")
        param string text: the claim text as a string
    """
    p = re.compile('(A|An|The)\s([\w-]+\s)*(method|process)\s(of|for)?')
    located = p.search(text)
    if located:
        return "method"
    else:
        return "system"
        
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
    return featurelist
    
def extract_claims(text):
    """ Attempts to extract claims as a list from a large text string.
    param string text: string containing several claims
    """
    sent_list = sent_tokenize(text)
    # On a test string this returned a list with the claim number and then the
    # claim text as separate items
    claims_list = [" ".join(sent_list[i:i+2]) for i in xrange(0, len(sent_list), 2)]
    return claims_list