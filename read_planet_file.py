def get_csv_list():
    """
    """
    with open('planets/bodies.csv') as planetfile :
        read_data = planetfile.read()
        data_lines = read_data.split('\n')
        planet_data = []
        for line in data_lines :
            line_data = line.split(',')
            planet_data.append(line_data)

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

        Returns: a list that contains the index of the non-empty 
        row and the corresponding header text
    """
    header_info = [[], []]
    for idx, entry in enumerate(stripped_list[0]) # Assume first list item is header info
        if entry != '':
            header_info[0] = idx
            header_info[1] = entry
    return header_info

def populate_planet_info(stripped_list, header_info)
    planets = [{}]
    for idx, entry in enumerate(stripped_list):
        if idx == 0: # Skip header row
            break
        else:
            for entry in header_info[0]:
                planet[idx][entry] = stripped_list[idx]


