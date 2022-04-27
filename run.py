# !/usr/bin/env python3.8
from credentials import Credentials
# from user import User
# THE user create account##
def create_useraccount(username, password):
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    method save user  account
    ''' 
    user.save_user()
# def save_user(user):
#      '''
#     Function to save user account
#     '''
#     user.save_user()

  
def   save_credetials(credentials): 
    '''
    Function to save credentials account
    '''
    credentials.save_credentials()

def  create_credentials(account,email,passlock):
    '''
    Function for credentials
    '''
    new_cred = Credentials(account,email,passlock)
    return new_cred

def display_cred():
    '''
    function for displaying saved credentials
    '''
    return Credentials.displaying_cred() 

# def main():
#     print("Welcome to Password Locker! Enter yuor username:")  
#     name = input ()
#     print(f"{name}, Sign up to continue")
#     print('\n')
#     print()
#     print("Reply with  : cc - Sign Up,  ex -exit ")
    
   

def main():
    # Dealing user class first
    print("Welcome to Password Locker! Please enter your name:  ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print('\n')
    print("*" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("*" * 80)

    while True:
        short_code = input().lower()

        if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            save_user(create_useraccount(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
            
            #working with credentials now###
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80) 

        
if __name__ == '__main__':
    main()  






    

    # if __name__ == '__main__':
    #     main()  