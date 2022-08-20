import unittest
from Gateway import *

class myFirstTest(unittest.TestCase):
    """
    checks The Executability of Design Patterns Scripts

    """
    def test_design_patterns(self):
        instance = product.pricelist
        self.assertTrue(sepah(), 'Wrong Dargah')
        self.assertEqual(instance, None, 'Wrong_valuity')



