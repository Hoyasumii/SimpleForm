"""
Project: SimpleForm
Author: Alan Reis Anjos
License: Creative Commons Attribution 4.0 International License
License Details: https://creativecommons.org/licenses/by/4.0/
"""

def isIterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False