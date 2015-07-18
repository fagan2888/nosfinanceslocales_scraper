# -*- coding: utf-8 -*-

import sys
import unittest2

from unipath import Path
sys.path.append(Path(__file__).ancestor(2))

from localfinance.parsing import DocumentMapping

"""
class AccountTestCase(unittest2.TestCase):
    def test_account(self):
        account = Account()
        account.add_node('localtax', name=u'Impôts Locaux')
        account.add_node('other_tax', name=u'Autres impôts et taxes')
        account.add_node('allocation', name=u'Dotation globale de fonctionnement')
        account.add_node('operating_revenues_A', name=u'TOTAL DES PRODUITS DE FONCTIONNEMENT = A', type='section')
        account.add_edges('operating_revenues_A', ['localtax', 'other_tax', 'allocation'])

    def test_find(self):
        account = Account()
        account.add_node('localtax', name=u'Impôts Locaux', other=u'test')
        account.add_node('localtax2', name=u'Impôts Locaux', other=u'test2')
        self.assertEqual(len(account.find_node(**{'name': u'Impôts Locaux'})), 2)
        self.assertEqual(len(account.find_node(**{'name': u'Impôts Locaux',
                                                  'other':u'test2'})), 1)

    def test_root(self):
        account = make_city_account()
        self.assertEqual(account.root, 'root')
"""

if __name__ == '__main__':
    unittest2.main()

