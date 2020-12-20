"""
Unit tests for `dh.ejson`.
"""

import fractions
import unittest

import dh.ejson


class Test(unittest.TestCase):
    def test_bytes(self):
        """
        JSON serialization and de-serialization of byte arrays.
        """
        x = bytes([225, 127, 98, 213])
        j = dh.ejson.dumps(x)
        xHat = dh.ejson.loads(j)
        self.assertIsInstance(xHat, bytes)
        self.assertEqual(x, xHat)

    def test_fraction(self):
        """
        JSON serialization and de-serialization of fractions.
        """
        x = fractions.Fraction(22, 7)
        j = dh.ejson.dumps(x)
        xHat = dh.ejson.loads(j)
        self.assertIsInstance(xHat, fractions.Fraction)
        self.assertEqual(x, xHat)
