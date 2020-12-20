"""
Unit tests for `dh.data`.
"""

import unittest

import dh.data


class Test(unittest.TestCase):
    def test_lena(self):
        L = dh.data.lena()
        self.assertEqual(L.shape, (512, 512, 3))
        self.assertEqual(str(L.dtype), "uint8")
        self.assertEqual(L[128, 256, 0], 219)
        self.assertEqual(L[256, 128, 1], 118)
        self.assertAlmostEqual(L.mean(), 128.22837575276694)

    def test_pal(self):
        P = dh.data.pal()
        self.assertEqual(P.shape, (576, 768, 3))
        self.assertEqual(str(P.dtype), "uint8")
        self.assertEqual(P[256, 128, 0], 122)
        self.assertEqual(P[384, 256, 1], 220)
        self.assertAlmostEqual(P.mean(), 121.3680261682581)
