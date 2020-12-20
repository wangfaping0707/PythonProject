"""
Unit tests of this package.

The tests can be run from Python via `run()`. This has the advantage of being
available even if the package was installed via wheel or similar means.
Otherwise, it is advisable to use the `check-tests.sh` script located in the
script dir of the package, which also includes doctests.
"""

import doctest
import os.path
import pkgutil
import unittest

import dh


def run():
    # collect unit tests
    testSuite = unittest.TestLoader().discover(os.path.dirname(__file__))

    # TODO: collect doctests
    for (_, name, _) in pkgutil.iter_modules(dh.__path__, prefix="dh."):
        module = __import__(name)
        testSuite.addTest(doctest.DocTestSuite(module))

    # run tests
    unittest.TextTestRunner(verbosity=2).run(testSuite)
