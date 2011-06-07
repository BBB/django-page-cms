"""Django page CMS test suite module"""
import unittest
from gerbi.tests.test_functionnal import FunctionnalTestCase
from gerbi.tests.test_unit import UnitTestCase
from gerbi.tests.test_regression import RegressionTestCase
from gerbi.tests.test_pages_link import LinkTestCase

def suite():
    suite = unittest.TestSuite()
    from gerbi import settings
    if not settings.GERBI_ENABLE_TESTS:
        return suite
    suite.addTest(unittest.makeSuite(UnitTestCase))
    suite.addTest(unittest.makeSuite(RegressionTestCase))
    suite.addTest(unittest.makeSuite(LinkTestCase))
    # being the slower test I run it at the end
    suite.addTest(unittest.makeSuite(FunctionnalTestCase))
    return suite
