#!/usr/bin/python

import os
import sys
import csv
from collections import OrderedDict


def get_max_price_analysis(file_path=None):
    """Function to analyse share data for different company

    from given csv file
    """
    if not file_path:
        file_path = raw_input(u"Enter file path: \n")

    try:
        csv_file = open(file_path, 'rb')
        csv_file.close()
    except IOError, e:
        print e
        sys.exit(0)

    ext = os.path.splitext(file_path)[1]
    if ext != '.csv':
        print "File format is invalid. Only csv file is supported."
        sys.exit(0)

    #Open csv file in read mode
    with open(file_path, 'rb') as share_data_file:
        share_data = csv.reader(share_data_file)
        final_data_dict = OrderedDict()

        #Extract company names from heading
        comapny_names = next(share_data)[2:]

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

    # Get analyzed data
    analyzed_data = get_max_price_analysis(file_path)

    # Print result
    print "\nCompany Name\tYear\tMonth\tPrice\n"
    for name, data in analyzed_data.iteritems():
        print "{0}\t{year}\t{month}\t{price}".format(name, **data)
