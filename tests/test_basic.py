# -*- coding: utf-8 -*-

from .context import patentparser
from .testdata_claims import claims

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        """Pre-test activities."""
        self.claims = claims
    
    def test_number(self):
        """ Check claim numbers are being extracted correctly. """
        for claim in claims:
            print(claim['text'][0:100])
            c = patentparser.Claim(claim['text'])
            num = c.number
            print(num)
            assert claim['number'] == num
    
    def test_category(self):
        """ Check extraction of claim category. """
        for claim in claims:
            print(claim['text'][0:100])
            c = patentparser.Claim(claim['text'])
            cat = c.detect_category()
            print(cat)
            assert claim['category'] == cat
    
    def test_dependency(self):
        """ Check dependency extraction. """
        for claim in claims:
            print(claim['text'][0:100])
            c = patentparser.Claim(claim['text'])
            dep = c.detect_dependency()
            print(dep)
            assert claim['dependency'] == dep

if __name__ == '__main__':
    unittest.main()