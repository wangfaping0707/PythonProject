"""
Unit tests for `dh.utils`.
"""

import io
import unittest

import dh.utils


class Test(unittest.TestCase):
    def test_cycle(self):
        x = (item for item in [1, "two", 3.0, None])
        y = [1, "two", 3.0, None, 1, "two"]
        yHat = list(dh.utils.cycle(x, 6))
        self.assertEqual(y, yHat)

    def test_eqvalue_equal(self):
        for value in (1, "1", 1.0, (1.0,), [1.0,]):
            x = (value for _ in range(10))
            y = value
            yHat = dh.utils.eqvalue(x)
            self.assertEqual(y, yHat)

    def test_eqvalue_raise(self):
        x = [1, 2, 1]
        with self.assertRaises(ValueError):
            dh.utils.eqvalue(x)

    def test_flatten(self):
        self.assertEqual(
            list(dh.utils.flatten(1, ("two",), [[3.0]], [None, [int, []]])),
            [1, "two", 3.0, None, int]
        )

    def test_unique(self):
        x = [1, 2, 1, 3, 3.0, "2", 2, None, False, 1, [], (), [], ()]
        y = [1, 2, 3, "2", None, False, [], ()]
        yHat = list(dh.utils.unique(x))
        self.assertEqual(y, yHat)

    def test_which(self):
        x = [True, 1, -1, 2, 1.0, float("inf"), [False], {"a": False}, False, 0, 0.0, None, [], {}]
        self.assertEqual(
            list(dh.utils.which(x)),
            [0, 1, 2, 3, 4, 5, 6, 7]
        )

    def test_JsonConfigParser(self):
        # values to be tested
        values = (False, True, 0, 1, -1, 1.0, -1e100, "A string", '"Another String"', [True, 1, "a"], [["x"]])
        keys = tuple("entry{}".format(nValue) for (nValue, _) in enumerate(values))

        # set up config parser
        config = dh.utils.JsonConfigParser()
        config.add_section("Test")

        # store values in the config and write it to (virtual) file
        for (key, value) in zip(keys, values):
            config.set("Test", key, value)
        f = io.StringIO()
        config.write(f)
        f.seek(0)

        # re-load the config
        config = dh.utils.JsonConfigParser()
        config.read_file(f)

        # check values
        for (key, value) in zip(keys, values):
            v = config.get("Test", key)
            self.assertEqual(value, v)

