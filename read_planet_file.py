#!/usr/bin/env python3


def get_csv_list(csv):
    """ This function reads in an input CSV file and
        separates the contents into a list of rows, which
        are separated by newlines in the file, with each
        row consisting of a list of the values, which are
        separated by commas in the file
        
        Args : a path to a comma-separated file

        Returns : a list with the contents of each row in
        the input CSV, separated into a list of entries
    """
    with open(csv) as planetfile :
        read_data = planetfile.read()
        data_lines = read_data.split('\n')
        planet_data = []
        for line in data_lines :
            line_data = line.split(',')
            planet_data.append(line_data)
    return planet_data


def strip_empty_csv_rows(raw_list):
    """ A function that takes a raw list of lists of strings
        representing entries from a CSV file. This function
        creates a new list that has the contents of the original
        list, but with entris that only had empty strings removed

        Args : A list of strings lists representing rows
        in a CSV file

        Returns : A list with contents of the input,
        with empty string lists removed
    """
    stripped_list = []
    for line in raw_list:
        for entry in line:
            if entry != '' :
                stripped_list.append(line[:])
                break
    return stripped_list


def get_header_info(stripped_list):
    """ A function that takes a list of list of strings
        representing entries from a CSV file. This function
        assumes that the first list item represents header
        information for the rest of the liste items. It will
        search for non-empty header items and return a list 
        that contains header information

        Args : A list of string lists representing rows in a 
        CSV file, with leading empty rows removed

        Returns: 
    """
    header_info = []
    for idx, entry in enumerate(stripped_list[0]): # Assume first list item is header info
        if entry != '':
            header_info.append({'name': entry,
                                'index': idx})
    return header_info


def populate_planet_info(stripped_list, header_info):
    planets = []
    for idx, row in enumerate(stripped_list):
        if idx != 0: # Skip header row
            planets.append({})
            for field in header_info:
                planets[-1][field['name']] = row[field['index']]
    return planets


def pull_planet_data(csv = 'planets/bodies.csv'):
    csv_data = get_csv_list(csv)
    stripped_csv = strip_empty_csv_rows(csv_data)
    header = get_header_info(stripped_csv)
    return populate_planet_info(stripped_csv, header)


if __name__ == '__main__':
    pdata = pull_planet_data()
    print(pdata)

