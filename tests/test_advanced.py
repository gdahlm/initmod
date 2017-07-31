# -*- coding: utf-8 -*-
"""Advanced test cases"""
import unittest
from .context import initmod


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases class"""

    def test_hellowworld(self):
        """simple template test"""
        self.assertIsNone(initmod.helloworld())


if __name__ == '__main__':
    unittest.main()
