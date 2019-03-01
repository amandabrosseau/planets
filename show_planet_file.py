#!/usr/bin/env python3

from read_planet_file import pull_planet_data

def show_planet_file(csv = 'planets/bodies.csv'):
    """
    """
    planet_data = pull_planet_data(csv)

    print("\nHello! We now have more facts about planets!\n")

    while True:
        planet = input("What planet would you like to learn about?\n Enter Q to quit\n").lower()
        if planet == "q":
            print("No more learning today...")
            break
        else :
            try :
                print("\nHere are the facts you can learn about {0}: {1}".format(planet, list(planet_data[planet])))
                attribute = input("What would you like to learn?\n Enter Q to quit\n").lower()
                if attribute == 'q':
                    print("No more learning today...")
                    break
                else:
                    try:
                        print("\n The {0} of {1} is {2}".format(attribute, planet, planet_data[planet][attribute]))
                    except:
                        print("Sorry, you must type one of the attributes exactly")
            except KeyError :
                print("We're sorry, that planet is not in our database!\n")