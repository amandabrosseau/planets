#!/usr/bin/env python3
worlds = { "mercury" : "burning",
           "venus"   : "greenhousy",
           "earth"   : "comfy",
           "mars"    : "ruddy",
           "jupiter" : "biggly",
           "saturn"  : "ringy",
           "neptune" : "bluey",
           "uranus"  : "buttly",
           "pluto"   : "NOT A PLANET", }


def solar_sys_info():
    """ Instructional function that takes input from the user and prints
        information to the screen about the corresponding planet.

    Args: none

    Returns: none """
    print("\nHello, it is time to learn about the planets!")
    
    while True :
        planet = input("What planet would you like to learn about?\n Enter Q to quit\n").lower()
        if planet == "q" :
            print("No more learning today...")
            break
        else :
            try :
                print("The planet {0}, is {1}!\n".format(planet, worlds[planet]))
            except KeyError :
                print("This isn't grade school, I know that's not a  planet!\n")
            except :
                print("No idea what went wrong here...")


if __name__ == '__main__':
    solar_sys_info()