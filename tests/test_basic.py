# -*- coding: utf-8 -*-
"""Advanced test cases"""
import unittest
from .context import initmod  # pylint: disable=unused-import


class BasicTestSuite(unittest.TestCase):
    """Basic test cases class"""

    def test_truth(self):  # pylint: disable=no-self-use
        """Placeholder test"""
        assert True


if __name__ == '__main__':
    # execute only if run as a script
    unittest.main()
