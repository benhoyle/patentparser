# List of claim text to use as test cases
# Some borrowed from http://www.nolo.com/legal-encyclopedia/sample-patent-claims-common-inventions.html

# This is our labelled test data
claims = [
    {
    'number':1,
    'category':'system',
    'dependency':0,
    'text':"""
        1. A decoding system, comprising:
            a decoding engine running on a mobile device, the decoding engine in operation decoding signals produced from a read of a buyer's financial transaction card, the decoding engine in operation accepting and initializing incoming signals from the read of the buyer's financial transaction card until the signals reach a steady state, detecting the read of the buyer's financial transaction card once the incoming signals are in a steady state, identifying peaks in the incoming signals and digitizing the identified peaks in the incoming signals into bits;
            and
            a transaction engine running on the mobile device and coupled to the decoding engine, the transaction engine in operation receiving as its input decoded buyer's financial transaction card information from the decoding engine and serving as an intermediary between the buyer and a merchant, so that the buyer does not have to share his/her financial transaction card information with the merchant.
    """
    },
    {
    'number':12,
    'category':'system',
    'dependency':0,
    'text':"""
        12. A self-propelled vehicle, comprising:
            (a) a body carriage having rotatable wheels mounted thereunder for enabling said body carriage to roll along a surface
            (b) an engine mounted in said carriage for producing rotational energy, and
            (c) means for controllably coupling rotational energy from said engine to at least one of said wheels, 
            whereby said carriage can be self-propelled along said surface.
    """
    },
    {
    'number':5,
    'category':'system',
    'dependency':0,
    'text':"""
        5. A hand-held writing instrument comprising:
            (a) elongated core-element means that will leave a marking line if moved across paper or other similar surface, and
            (b) an elongated holder surrounding and encasing said elongated coreelement means, one portion of said holder being removable from an end thereof to expose an end of said core-element means so as to enable said core-element means to be exposed for writing,
            whereby said holder protects said coreelement means from breakage and provides an enlarged means for holding said core-element means conveniently.
    """
    },
    {
    'number':1,
    'category':'method',
    'dependency':0,
    'text':"""
        1. A computer implemented method of scoring a plurality of linked documents, comprising:
            obtaining a plurality of documents, at least some of the documents being linked documents, at least some of the documents being linking documents, and at least some of the documents being both linked documents and linking documents, each of the linked documents being pointed to by a link in one or more of the linking documents;
            assigning a score to each of the linked documents based on scores of the one or more linking documents and
            processing the linked documents according to their scores.
    """
    },
    {
    'number':4,
    'category':'method',
    'dependency':3,
    'text':"""
        4. The method of claim 3, wherein the assigning includes:
            identifying a weighting factor for each of the linking documents, the weighting factor being dependent on the URL, host, domain, author, institution, or last update time of the one or more linking documents, and
            adjusting the score of each of the one or more linking documents based on the identified weighting factor.
    """
    }
    ]