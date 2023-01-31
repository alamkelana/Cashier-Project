"""
Function for printing in colors using ANSI code
later it will be used in Store.py and main.py to print in colors based on different conditions
"""

def printRed(text): 
    print("\033[91m {}\033[00m" .format(text))
 
 
def printGreen(text): 
    print("\033[92m {}\033[00m" .format(text))
 
 
def printYellow(text): 
    print("\033[93m {}\033[00m" .format(text))