# This file serve as main init file to load core module neccessary to run this program
# helper module is imported to load the Helper class which contains
# the logic and functionalities of this program.
# 
# To run this program, run directly from this file `atm.py`

# import helper class
import helper

# Entry point of ATM Simulation Program
def init():
    # intialize Helper class
    _helper = helper.Helper()
 
    # check if user is logged in
    if(_helper.isLogin):

        # launch welcome screen
        _helper.welcome()
        
    else:
        print(_helper.login()) 
        
        
if __name__ == '__main__':
    
   init()