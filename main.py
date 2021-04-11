#!/usr/bin/env python3.8

from user import User
from credential import Credential

def create_user(name,login,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,login,password)
    return new_user
  
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user() 
    
# def login_user(login,password):
#     """
#     function that checks whether a user exists and then logs the user in.
#     """
    
    
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
    
def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()    
  
def create_credential(application,username,passcode):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(application,username,passcode)
    return new_credential
  
def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential() 
    
def del_credential(credential):
    '''
    Function to delete user credentials
    '''
    credential.delete_credential()
    
def find_credential(application):
    '''
    Function that finds a user account credential by the application name and returns the credential
    '''
    return Credential.find_by_application(application) 
  
def check_existing_credential(application):
    '''
    Function that check if a user account exists with that application name and return a Boolean
    '''
    return Credential.credential_exist("application")    
    
def display_credential():
    '''
    Function that returns all the user's credentials
    '''
    return Credential.display_credential()      
    
    
def main():
    print("Hello Welcome to Kit Locker. What is your name?")
    name = input()

    print(f"Hello {name}. What would you like to do?")
    print('\n')
    
    while True:
                    print("Use these short codes : cu - create new account, lu - login to account, du - display account info, ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("Name ....")
                            name = input()

                            print("Username ...")
                            login = input()

                            print("Password ...")
                            password = input()

                            save_user(create_user(name, login, password)) # create and save new credential.
                            print ('\n')
                            print(f"Account creation successful. New User {login} created")
                            print ('\n')
                            
                    
                    elif short_code == 'du':

                            if display_user():
                                    print("Here are your account details:")
                                    print('\n')

                                    for user in display_user():
                                            print(f"Name: {user.name} \
                                                  Username: {user.login}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You don't have a registered Kit account. Please create one if you wish to proceed.")
                                    print('\n')
                                            
                    elif short_code == "lu":
                            print("*"*50)
                            print("Proceed to login")
                            print("Please enter your username and password:")
                            print('*' * 50)
                            login = input("Username: ")
                            password = input("Password: ")
                            # login = login_user(login,password)
                            # if login_user == login:
                                # print(f"Hello {login}.Welcome to your Kit Locker acount")  
                                # print('\n')   
                                
                                
                    while True:
                        print("Use these short codes : cc - create account credential, dc - display account info, fc -find account by application, ex -exit the credentials list ")

                        short_code = input().lower()

                        if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("Application name ....")
                            application = input()

                            print("Username ...")
                            username = input()

                            print("Passcode ...")
                            passcode = input()


                            save_credential(create_credential(application,username,passcode)) # create and save new credential.
                            print ('\n')
                            print(f"Account login {username} created for {application}")
                            print ('\n')

                        elif short_code == 'dc':

                            if display_credential():
                                    print("Here is a list of all your account usernames and passwords")
                                    print('\n')

                                    for credential in display_credential():
                                            print(f"{credential.application} {credential.username} .....{credential.passcode}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You don't seem to have any credentials saved yet")
                                    print('\n')

                        elif short_code == 'fc':

                            print("Enter the application name you want to search for; e.g., Facebook, Twitter, e.t.c,")

                            search_application = input()
                            if check_existing_credential(search_application):
                                    search_credential = find_credential(search_application)
                                    print(f"{search_credential.username} {search_credential.passcode}")
                                    print('-' * 20)

                                    print(f"Application name.......{search_credential.application}")
                                    print(f"Username.......{search_credential.username}")
                            else:
                                    print("Account does not exist")  
                                    
                    # elif short_code == "ex":
                    #         print("Thanks for using Kit Locker. See you next time!")
                    #         break
                    # else:
                    #          print("I really didn't get that. Please use the short codes")
                                                                           
        
if __name__ == '__main__':

    main()        