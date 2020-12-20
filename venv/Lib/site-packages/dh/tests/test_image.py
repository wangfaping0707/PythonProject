"""
Unit tests for `dh.image`.
"""

import tempfile
import unittest

import numpy as np

import dh.data
import dh.image


class Test(unittest.TestCase):
    def test_save_load_decode(self):
        # images to be saved
        (_, filename) = tempfile.mkstemp(suffix=".png")
        C8  = dh.data.lena()
        C16 = np.array(C8, dtype="uint16")
        G8  = dh.image.asgray(C8)
        G16 = dh.image.asgray(C16)

        for I in (C8, C16, G8, G16):
            for color in (None, False, True):
                # save image
                dh.image.save(filename, I)

                # load image from file
                J = dh.image.load(filename, color=color)

                # decode image from byte array
                with open(filename, "rb") as f:
                    K = dh.image.decode(f.read(), color=color)

                # make sure that load and decode are identical
                self.assertEqual(J.shape, K.shape)
                self.assertEqual(J.dtype, K.dtype)
                self.assertTrue(np.all(J == K))

                # expected image
                if color or ((color is None) and dh.image.iscolor(I)):
                    E = dh.image.ascolor(I)
                else:
                    E = dh.image.asgray(I)

                # compare loaded image with expected image
                self.assertEqual(J.dtype, E.dtype)
                self.assertEqual(J.shape, E.shape)
                if color in (None, True):
                    # if I is a color image and color=False, then the conversion to gray scale will be performed by OpenCV, which is different than dh.image.asgray
                    self.assertTrue(np.all(J == E))


    def test_stack(self):
        # images
        L = dh.data.lena()
        M = dh.image.convert(dh.data.M(300, 200).astype("uint16"), "uint8")
        G1 = dh.data.grid([350, 500])
        G2 = dh.data.grid([200, 200])
        P = dh.data.pal()

        # test default stacking
        S = dh.image.stack([[L, M], [G1, G2], [P]])
        self.assertEqual(S.shape, (1438, 768, 3))
        self.assertEqual(S.dtype, np.uint8)
        self.assertAlmostEqual(S.mean(), 89.258657616674398)

        # test default stacking with a 1D image vector (one row)
        S = dh.image.stack([L, M, G1, G2, P])
        self.assertEqual(S.shape, (576, 2180, 3))
        self.assertEqual(S.dtype, np.uint8)
        self.assertAlmostEqual(S.mean(), 78.503944741760108)

        # test stacking with padding
        S = dh.image.stack([[L, M], [G1, G2], [P]], padding=32)
        self.assertEqual(S.shape, (1566, 832, 3))
        self.assertEqual(S.dtype, np.uint8)
        self.assertAlmostEqual(S.mean(), 75.658089981006654)

        # test stacking with forced dtype
        S = dh.image.stack([[L, M], [G1, G2], [P]], dtype="float")
        self.assertEqual(S.shape, (1438, 768, 3))
        self.assertEqual(S.dtype, np.float)
        self.assertAlmostEqual(S.mean(), 0.35003395143793881)

        # test stacking with forced gray mode
        S = dh.image.stack([[L, M], [G1, G2], [P]], gray=True)
        self.assertEqual(S.shape, (1438, 768))
        self.assertEqual(S.dtype, np.uint8)
        self.assertAlmostEqual(S.mean(), 89.139465982846545)

    def test_text(self):
        I = dh.data.lena()
        dh.image.text(I, "The quick brown fox jumps over the lazy dog.")
        for nChannel in range(3):
            self.assertEqual(I[0, 0, nChannel], 0)
        self.assertAlmostEqual(I.mean(), 121.48126602172852)

    def test_convert_fromBool(self):
        # create bool image
        L = dh.data.lena()
        L = dh.image.asgray(L)
        L = (L > 127)
        m = L.mean()

        C = dh.image.convert(L, "uint8")
        self.assertAlmostEqual(C.mean(), 255.0 * m)

        C = dh.image.convert(L, "uint16")
        self.assertAlmostEqual(C.mean(), 65535.0 * m)

        C = dh.image.convert(L, "float")
        self.assertAlmostEqual(C.mean(), m)

    def test_convert_toFloat(self):
        L = dh.data.lena()

        # test conversion to float
        C = dh.image.convert(L, "float")
        self.assertEqual(C.shape, (512, 512, 3))
        self.assertEqual(C.dtype, np.float)
        self.assertAlmostEqual(C.mean(), 0.50285637550104678)

    def test_colorize(self):
        I = dh.data.lena()
        C = dh.image.colorize(I, "jet")
        self.assertEqual(I.shape, C.shape)
        self.assertEqual(C[128, 256, 1], 174)
        self.assertEqual(C[256, 128, 2], 64)
        ms = (180.22365951538086, 99.051216125488281, 105.41025161743164)
        for nChannel in range(3):
            mHat = I[:, :, nChannel].mean()
            self.assertAlmostEqual(mHat, ms[nChannel])

    def test_colorize_all(self):
        """
        Colorize slope image with all available colormaps
        """

        # slope image
        I = np.arange(256).reshape(1, -1).astype("uint8")
        self.assertEqual(I.shape, (1, 256))

        # use each colormap...
        cs = dh.data.colormaps()
        self.assertIsInstance(cs, dict)
        self.assertGreaterEqual(len(cs), 75)
        for (cName, c) in cs.items():
            # ... to colorize the slope and check the result
            C = dh.image.colorize(I, c)
            self.assertEqual(I.shape + (3,), C.shape)
            for nPixel in range(256):
                if nPixel in c:
                    # check colorized result vs. colormap
                    for nChannel in range(3):
                        self.assertEqual(C[0, nPixel, nChannel], c[nPixel][nChannel])
                else:
                    # no color available in colormap - should be colored as black
                    for nChannel in range(3):
                        self.assertEqual(C[0, nPixel, nChannel], 0)

    def test_gamma(self):
        I = dh.data.lena()
        G = dh.image.gamma(I, 0.5)
        self.assertEqual(I.shape, G.shape)
        self.assertAlmostEqual(G.mean(), 174.81550725301108)

    def test_resize(self):
        I = dh.data.lena()
        R = dh.image.resize(I, 0.5)
        self.assertEqual(R.shape, (256, 256, 3))

    def test_tir(self):
        self.assertEqual(
            dh.image.tir(np.array([-3.81, 2.97]) * 0.5),
            (-2, 1)
        )

    #def test_