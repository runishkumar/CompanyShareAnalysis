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
        self.start_year = random.randint(1990, 2000)  # Random Start Year
        self.end_year = random.randint(2001, 2013)  # Random End Year
        self.years = range(self.start_year, self.end_year)
        self.months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.share_values = range(100, 1000)
        self.no_companies = random.randint(1, 10)  # Random Company Number
        self.no_entries = (self.end_year - self.start_year) * 12
        self.csv_header = ['Year', 'Month']
        self.test_dict = {}
        self.csv_test_file = 'test.csv'

        #generate hearder for test csv file
        for i in range(self.no_companies):
            comp_name = "Company-{0}".format(i + 1)
            self.csv_header.append(comp_name)
            self.test_dict[comp_name] = {'price': 0, 'year': '', 'month': ''}

        # Generate csv file along with the data with max price for comparison
        with open(self.csv_test_file, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.csv_header)

            for year in self.years:
                for month in self.months:
                    csv_data = [year, month]

                    for cmpny in range(self.no_companies):
                        random_share_value = random.choice(self.share_values)
                        csv_data.append(random_share_value)
                        company_index = "Company-{0}".format(cmpny + 1)

                        if self.test_dict[company_index]['price'] < random_share_value:
                            self.test_dict[company_index] = {'price': random_share_value, 'year': year, 'month': month}

                    writer.writerow(csv_data)


class TestResult(RandomCSVFile):
    """Write test case to validate result"""

    def test_share_analysis(self):
        analyzed_data = analyze_share.get_max_price_analysis(self.csv_test_file)

        for comp_name, comp_data in analyzed_data.iteritems():
            self.assertEqual(int(comp_data['price']), int(self.test_dict[comp_name]['price']))
            self.assertEqual(int(comp_data['year']), int(self.test_dict[comp_name]['year']))
            self.assertEqual(comp_data['month'], self.test_dict[comp_name]['month'])


if __name__ == "__main__":
    unittest.main()
