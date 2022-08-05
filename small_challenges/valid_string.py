# Write a code in Python to find out whether a given string S is a valid regex or not.

import re

def valid_string():
    # compiling the pattern for alphanumeric string
    pat = re.compile(r"[A-Za-z0-9]+")
    
    # Prompts the user for input string
    test = input("Enter the string: ")

    # Checks whether the whole string matches the re.pattern or not
    if re.fullmatch(pat, test):
        print(f"'{test}' is an alphanumeric string!")
    else:
        print(f"'{test}' is NOT a alphanumeric string!")
        
valid_string()