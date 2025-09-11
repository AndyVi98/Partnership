"""
temp_functions.py

This script contains a temperature converter from fahrenheit to celsius, and  a classifier for the celsius values from 0 to 4

Author: Andy Vidal and Joshua Pimentel

"""
def temp_classifier(temp_celsius):
    """
    This function adds a class to your temp_celsius.
    The following uses an if/else/elif to return different values
    Bear in mind that the temp_celsius must remain the same all through 
    """
    if temp_celsius < 600:
        return 0
    elif 600 <= temp_celsius <800:
        return 1
    elif 800 <= temp_celsius <1000:
        return 2
    elif 1000 <= temp_celsius <1200:
        return 3
    else:
        return 4

def fahr_to_celsius(temp_celsius):
    return (temp_celsius - 32)/1.8