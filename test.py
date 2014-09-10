#!/usr/bin/python

import os
import sys
import csv
import unittest
import random
from analyze_share import AnalyzeShare


class TestShareAnalysis(unittest.TestCase):
    """Write test case to validate result"""

    def setUp(self):
        # setup required data for test case
        self.csv_test_file = 'test.csv'

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

    def test_read_data(self):
        analyzed_data = AnalyzeShare(self.csv_test_file)
        test_data = analyzed_data.read_data()
        self.assertEqual(
            test_data[0],
            ['Year', 'Month', 'Company-1', 'Company-2', 'Company-3',
                'Company-4', 'Company-5', 'Company-6', 'Company-7']
        )

    def test_validate_file(self):
        #Validate correct file type
        a1_obj = AnalyzeShare(self.csv_test_file)
        self.assertEqual(a1_obj.validate_file(), True)

        #validate wrong file, file not exist
        a2_obj = AnalyzeShare('Random.csv')
        self.assertEqual(a2_obj.validate_file(), False)

        #validate wrong file type, txt is not supported
        a3_obj = AnalyzeShare('test.txt')
        self.assertEqual(a3_obj.validate_file(), False)

    def test_share_analysis(self):
        analyzed_data = AnalyzeShare(self.csv_test_file)
        a_data = analyzed_data.get_max_share_price()

        #compare price data
        self.assertEqual(a_data['Company-1']['price'], 964)
        self.assertEqual(a_data['Company-2']['price'], 958)
        self.assertEqual(a_data['Company-3']['price'], 990)
        self.assertEqual(a_data['Company-4']['price'], 954)
        self.assertEqual(a_data['Company-5']['price'], 950)
        self.assertEqual(a_data['Company-6']['price'], 978)
        self.assertEqual(a_data['Company-7']['price'], 926)

        #compare overall data
        self.assertEqual(a_data['Company-1'], self.correct_data['Company-1'])
        self.assertEqual(a_data['Company-2'], self.correct_data['Company-2'])
        self.assertEqual(a_data['Company-3'], self.correct_data['Company-3'])
        self.assertEqual(a_data['Company-4'], self.correct_data['Company-4'])
        self.assertEqual(a_data['Company-5'], self.correct_data['Company-5'])
        self.assertEqual(a_data['Company-6'], self.correct_data['Company-6'])
        self.assertEqual(a_data['Company-7'], self.correct_data['Company-7'])


if __name__ == "__main__":
    unittest.main()
