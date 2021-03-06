from functools import partial
from smarty.utils import get_data_filename
from unittest import TestCase

import smarty

class TestUtils(TestCase):
    def test_parse_odds_file(self):
        """
        Testing parse_odds_file and get_data_filename
        """
        # parse_odds_file uses get_data_filename so this run checks both
        odds = smarty.utils.parse_odds_file('odds_files/atom_index_odds.smarts', verbose = True)
        odds = smarty.utils.parse_odds_file('odds_files/bond_OR_bases.smarts')
        self.assertIsNone(odds[1], msg = "Parsing odds file with no odds should give None as the second entry")
