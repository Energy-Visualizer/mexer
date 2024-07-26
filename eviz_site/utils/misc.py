# misc.py contains miscellaneous utility functions for the Mexer project
#
# Function included don't neccessarily have a better place to go
# and aren't big enough to have their own file
#
# Because the contents of this file are unrelated,
# imports should be kept by their respective functions
# to keep them as individual as possible
#
# Authors: Kenny Howes - kmh67@calvin.edu
#          Edom Maru
################################################

from time import time
def time_view(v):
    '''Wrapper to time how long it takes to deliver a view

    Inputs:
        v, function: the view to time

    Outputs:
        A function which wil prints how long the given view took to run
    '''

    def wrap(*args, **kwargs):
        t0 = time()
        ret = v(*args, **kwargs)
        t1 = time()
        print(f"Time to run {v.__name__}: {t1 - t0}")
        return ret

    return wrap

import sys
from os import devnull
class Silent():
    '''Used as a context manager to silence anything in its block'''

    real_stdout = sys.stdout # Store the original stdout
    real_stderr = sys.stderr # Store the original stderr
    instance = None # Class variable to store the singleton instance

    def __new__(cls):
        '''Implement the Singleton pattern to ensure only one instance of Silent is created.
        
        Outputs:
            Silent: The single instance of the Silent class.
        '''
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __enter__(self):
        '''Called when entering the context manager block.
        Redirects stdout and stderr to /dev/null.
        '''
        self.dn = open(devnull, "w") # Open /dev/null for writing
        sys.stdout = self.dn  # Redirect stdout to /dev/null
        sys.stderr = self.dn # Redirect stderr to /dev/null

    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''
        Called when exiting the context manager block.
        Restores the original stdout and stderr, and closes the /dev/null file.

        Inputs:
            exc_type: The type of the exception that caused the context to be exited.
            exc_value: The instance of the exception that caused the context to be exited.
            exc_traceback: A traceback object encoding the stack trace.
        '''
        self.dn.close()  # Close the /dev/null file
        sys.stdout = self.real_stdout # Restore the original stdout
        sys.stderr = self.real_stderr # Restore the original stderr

from uuid import uuid4
import pickle
from eviz.models import EmailAuthCodes, PassResetCodes, EvizUser
from eviz.forms import SignupForm
def new_email_code(account_info: SignupForm) -> str:
    """Generate a new email verification code and save associated account information.

    Inputs:
        form: A form object containing account setup information.

    Outputs:
        str: A unique verification code.
    """
    code = str(uuid4()) # Generate a unique code using UUID
    account_info = pickle.dumps(account_info) # serialize the account info for storing it in the database 
    EmailAuthCodes(code=code, account_info=account_info).save() # save account setup info to database
    return code

def new_reset_code(user: EvizUser) -> str:
    """Generate a new password reset code and save associated user.

    Inputs:
        user: A User object containing account setup information.

    Outputs:
        str: A unique verification code.
    """
    code = str(uuid4()) # Generate a unique code using UUID
    PassResetCodes(code = code, user = user).save() # save code and user to database
    return code

def valid_passwords(password1: str, password2: str) -> bool:
    
    return (
        type(password1) == str and type(password2) == str
        and
        password1 == password2 # passwords must be the same
        and
        len(password1) >= 8 # password must be at least 8 characters
        and
        sum([c.isnumeric() for c in password1]) > 0 # password must have at least one number
        and
        sum([c.isupper() for c in password1]) > 0 # password must have at least one capital letter
    )


from django.contrib.auth.models import User
def iea_valid(user: User, query: dict) -> bool:
    '''Ensure that a give user's query does not give out IEA data if not authorized

    Inputs:

        user, user info from the HTTP request (for Django requsests: request.user): the user whose authorizations need to be checked

        query, a dict: the query to investigate

    Output:

        the boolean value of if a user's query is valid (True) or not (False)
    '''

    # will short curcuit if the data is free,
    # so everything past the "or" will not be checked if not neccessary
    return (
        # free data
        (
            query.get("dataset", None) != "IEAEWEB2022"
            and query.get("ieamw", None) == "MW"
        )
        or
        # authorized to get proprietary data
        (user.is_authenticated and user.has_perm("eviz.get_iea"))
    )