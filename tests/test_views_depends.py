# -*- coding: utf-8 -*-
"""
    tests/test_views_depends.py

"""
import unittest

import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class TestViewsDepends(unittest.TestCase):
    '''
    Test views and depends
    '''

    def setUp(self):
        """
        Set up data used in the tests.
        this method is called before each test function execution.
        """
        trytond.tests.test_tryton.install_module('party_merge')

    def test0005views(self):
        '''
        Test views.
        '''
        test_view('party_merge')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends)
    )
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
