# import helper class
import helper
import time

# intialize Helper class
_helper = helper.Helper()

# check if user is logged in
if(_helper.isLogin):

    # launch welcome screen
    _helper.welcome()
    
else:
    print(_helper.login())