#!/usr/bin/env python3

import sys
import pprint

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
            clean_line = []
            for item in line:
                clean_line.append(item.strip())
            planet_data.append(line_data)
    return planet_data


def strip_empty_csv_rows(raw_list):
    """ A function that takes a raw list of lists of strings
        representing entries from a CSV file. This function
        creates a new list that has the contents of the original
        list, but with entries that only had empty strings removed

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


def get_text_within_parenthesis(string):
    lidx = string.find('(')+1
    ridx = string.find(')', lidx)
    new_string = string[lidx:ridx]
    return new_string


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
            short_name = entry.split()[0]
            if entry.find('(') != -1:
                field_name = entry[:entry.find('(')].lower().strip()
                units = get_text_within_parenthesis(entry).lower(); # text within parenthesis
            else:
                field_name = entry.lower()
                units = None
            header_info.append({'field_name_short': short_name,
                                'field_name': field_name,
                                'units': units,
                                'column': idx})
    return header_info


def get_planet_name(row, header_info):
    """ This function takes a row from the stripped CSV
        list and the dictionary containing the CSV header
        information and returns the name of the planet. It
        makes the assumption that there is a header entry
        with the name 'name' (case-insensitive)

        Args: row - a list that contains the contents of a single
        CSV row of planet data
        header_info - a dictionary that contains the header
        titles and their column positions

        Returns: A string representing name of the planet
    """
    for field in header_info:
        if field['field_name'].lower() == 'name':
            return row[field['column']].lower()



def populate_planet_info(stripped_list, header_info):
    """ This function takes the stripped, formatted data
        from the CSV file and populates a dictionary of planet
        information

        Args: stripped_list - a list of string lists representing rows in a 
        CSV file, with leading empty rows removed
        header_info - a dictionary that contains the header
        titles and their column positions

        Returns: a dictionary contaning planet entries with
        each planet as a dictionary entry, and each
        dictionary value contains another dictionary of planet
        facts, as determined by the fields in header_info
    """
    planets = {}
    for idx, row in enumerate(stripped_list):
        if idx != 0: # Skip header row
            planet = {}
            planet_name = get_planet_name(row, header_info)
            for field in header_info:
                planet[field['field_name']] = { 'value' : row[field['column']],
                                                'units' : field['units'],}
            planets[planet_name] = planet
            del planets[planet_name]['name']
    return planets


def pull_planet_data(csv = 'planets/bodies.csv'):
    """ Opens the given CSV file and creates a dictionary
        of planetary data from the information within

        Args: csv - the path to the planetary body CSV file
        The first non-empty row of the file must contain header
        data and one of the header fields must be 'name' (case-insenitive)

        Returns: a dictionary contaning planet entries with
        each planet as a dictionary entry, and each
        dictionary value contains another dictionary of planet
        facts, as determined by the information in csv
    """
    csv_data = get_csv_list(csv)
    stripped_csv = strip_empty_csv_rows(csv_data)
    header = get_header_info(stripped_csv)
    return populate_planet_info(stripped_csv, header)


if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent = 4)
    try:
        if len(sys.argv) > 1:
            pdata = pull_planet_data(sys.argv[1])
        else:
            pdata = pull_planet_data()
        pp.pprint(pdata)
    except FileNotFoundError as ferror:
        print(f"Sorry, {ferror.filename} was not found! Aborting...")

