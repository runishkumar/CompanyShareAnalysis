#!/usr/bin/python

import os
import sys
import csv
import unittest
import random
import analyze_share


class RandomCSVFile(unittest.TestCase):
    """Class to generate random csv file for test case"""

    def setUp(self):
        # setup required data for test case
        self.csv_test_file = 'test.csv'

        #Companies in test.csv
        self.companies = ['Company-1', 'Company-2', 'Company-3', 'Company-4', 'Company-5', 'Company-6', 'Company-7']

        #MAx values from test.csv
        self.correct_data = {
            'Company-1': {'price': 964, 'year': '1991', 'month': 'Sep'},
            'Company-2': {'price': 958, 'year': '1995', 'month': 'Sep'},
            'Company-3': {'price': 990, 'year': '1993', 'month': 'Dec'},
            'Company-4': {'price': 954, 'year': '1995', 'month': 'Mar'},
            'Company-5': {'price': 950, 'year': '1993', 'month': 'Mar'},
            'Company-6': {'price': 978, 'year': '1990', 'month': 'Dec'},
            'Company-7': {'price': 926, 'year': '1993', 'month': 'Sep'}
        }


class TestResult(RandomCSVFile):
    """Write test case to validate result"""

    def test_share_analysis(self):
        analyzed_data = analyze_share.get_max_price_analysis(self.csv_test_file)

        #compare price data
        self.assertEqual(analyzed_data['Company-1']['price'], 964)
        self.assertEqual(analyzed_data['Company-2']['price'], 958)
        self.assertEqual(analyzed_data['Company-3']['price'], 990)
        self.assertEqual(analyzed_data['Company-4']['price'], 954)
        self.assertEqual(analyzed_data['Company-5']['price'], 950)
        self.assertEqual(analyzed_data['Company-6']['price'], 978)
        self.assertEqual(analyzed_data['Company-7']['price'], 926)

        #compare overall data
        self.assertEqual(analyzed_data['Company-1'], self.correct_data['Company-1'])
        self.assertEqual(analyzed_data['Company-2'], self.correct_data['Company-2'])
        self.assertEqual(analyzed_data['Company-3'], self.correct_data['Company-3'])
        self.assertEqual(analyzed_data['Company-4'], self.correct_data['Company-4'])
        self.assertEqual(analyzed_data['Company-5'], self.correct_data['Company-5'])
        self.assertEqual(analyzed_data['Company-6'], self.correct_data['Company-6'])
        self.assertEqual(analyzed_data['Company-7'], self.correct_data['Company-7'])


if __name__ == "__main__":
    unittest.main()
