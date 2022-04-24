# !/usr/bin/env python3.8
from credentials import Credentials
from user import User
# THE user create account##
def create_useraccount(username, password):
    new_user = User(username,password)
    return new_user

def save_user(user):
     '''
    Function to save user account
    '''
    contact.save_account()

