#!/usr/bin/env python3.8

from user import User
from credential import Credential

def create_user(name,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(name,username,password)
    return new_user
  
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user() 
    
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
    print("Hello Welcome to Kit password locker. What is your name?")
    name = input()

    print(f"Hello {name}. What would you like to do?")
    print('\n')
    
    while True:
                    print("Use these short codes : cc - create new account, dc - display account info, fc -find user, ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("Name ....")
                            name = input()

                            print("Username ...")
                            username = input()

                            print("Password ...")
                            password = input()

                            save_users(create_user(name,username, password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {username} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is your details")
                                    print('\n')

                                    for user in display_user():
                                            print(f"{user.name} {user.username} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You don't have a registered Kit account. Please create one if you wish to proceed.")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")
    
    while True:
                    print("Use these short codes : cc - create account credential, dc - display account info, fc -find account application, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("Application name ....")
                            application = input()

                            print("Last name ...")
                            username = input()

                            print("Phone number ...")
                            passcode = input()

                            print("Email address ...")
                            e_address = input()


                            save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
                            
                            
if __name__ == '__main__':

    main()        