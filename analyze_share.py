#!/usr/bin/python

import os
import sys
import csv
from collections import OrderedDict


class AnalyzeShare:
    """Class to parse csv file and analyze

    shares from differect company across time.
    """

    def __init__(self, data_file=None):
        self.data_file = data_file

    def get_data_file(self):
        """Get data file from user"""
        attempt = 0
        while(attempt < 5):
            file_path = raw_input(u"Enter file path: \n")
            self.data_file = file_path
            is_valid = self.validate_file()

            if not is_valid:
                #Increase attempt counter
                attempt += 1
            else:
                break

        if attempt == 5:
            print "Oops!! All attempt exausted. It seems you don't remember correct filename."
            sys.exit(0)

    def validate_file(self):
        #check if file is present and can be read
        try:
            csv_file = open(self.data_file, 'rb')
            csv_file.close()
        except IOError, e:
            print e
            self.data_file = None
            return False

        #validate file extension
        ext = os.path.splitext(self.data_file)[1]
        if ext != '.csv':
            print "File format is invalid. Only csv file is supported."
            self.data_file = None
            return False

        return True

    def read_data(self):
        if not self.data_file or not self.validate_file():
            self.get_data_file()

        with open(self.data_file, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]

        return parsed_data

    def get_max_share_price(self):
        share_data = self.read_data()
        final_data_dict = OrderedDict()

        #Extract company names from heading
        comapny_names = share_data.pop(0)[2:]

        #Initialize final dict to be returned with blank data
        for name in comapny_names:
            final_data_dict[name] = {'price': 0, 'year': '', 'month': ''}

        for row in share_data:
            year, month = row[:2]
            price = row[2:]

            #Check each row and store max price for each company
            for name, price in zip(comapny_names, map(int, price)):
                if final_data_dict[name]['price'] < price:
                    final_data_dict[name] = {'price': price, 'year': year, 'month': month}

        return final_data_dict


if __name__ == '__main__':
    file_path = None
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    analyze_share = AnalyzeShare(file_path)
    analyzed_data = analyze_share.get_max_share_price()

    # Print result
    print "\nCompany Name\tYear\tMonth\tPrice\n"
    for name, data in analyzed_data.iteritems():
        print "{0}\t{year}\t{month}\t{price}".format(name, **data)
