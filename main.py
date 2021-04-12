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
    
def login_user(login,password):
    """
    function that checks whether a user exists and then logs the user in.
    """
    return User.user_exists(login,password)
    
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
    
def delete_credential(credential):
    '''
    Function to delete user credentials
    '''
    credential.delete_credential()
    
def find_credential(application):
    '''
    Function that finds a user account credential by the application name and returns the credential
    '''
    return Credential.find_by_application_name(application) 
  
def check_existing_credential(application):
    '''
    Function that check if a user account exists with that application name and return a Boolean
    '''
    return Credential.credential_exist(application)    
    
def display_credential():
    '''
    Function that returns all the user's credentials
    '''
    return Credential.display_credential()      
    
def create_generated_passcode(name):
    '''
    Function that generates a passcode for the user account 
    Args:
        name : the name of the account
    '''
    passcode = Credential.generate_passcode()

    return passcode   
    
def main():
    print("Hello Welcome to Kit Locker. What is your name?")
    name = input()

    print(f"Hello {name}. What would you like to do?")
    print('\n')
    
    while True:
                    print("Use these short codes :\n cu - create new account\n lu - login to account\n du - display account info\n lo - log out of user account")

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
                            continue
                            
                    
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
                                    
                    elif short_code == "lo":
                                    print('\n')   
                                    print("Thanks for using Kit Locker. See you next time!")
                                    break             
                                             
                    elif short_code == "lu":
                            print("*"*50)
                            print("Proceed to login")
                            print("Please enter your username and password:")
                            print('*' * 50)
                            login = input("Username: ")
                            password = input("Password: ")
                            if login_user(login,password):
                               print("Login Successful")
                               print('\n')  
                            else:
                               print('\n')  
                               print("Account does not exist")    
                               print('\n')  
                                
                    while True:
                        print("Use these short codes :\n cc - create account credential\n da - display account info\n fc -find account by application\n d - delete account\n ex -exit the credentials list")

                        short_code = input().lower()

                        if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("Application name ....")
                            application = input()

                            print("Username ...")
                            username = input()

                            while True:
                                print(" op - To type your own pasword if you already have an account\n gp - To generate random Password")
                                passcode_choice = input().lower().strip()
                                if passcode_choice == 'op':
                                    passcode = input("Enter Your Own Password\n")
                                    break
                                elif passcode_choice == 'gp':
                                    passcode = Credential.generate_passcode()
                                    break
                                else:
                                    print("Invalid password please try again")


                            save_credential(create_credential(application,username,passcode)) # create and save new credential.
                            print ('\n')
                            print(f"Account login {username} created for {application}")
                            print ('\n')

                        elif short_code == 'da':

                            if display_credential():
                                print("Here is a list of all your account usernames and passwords:")
                                print('\n')

                                for credential in display_credential():
                                    print(f"Application: {credential.application_name}\n Username: {credential.account_username}\n Password: {credential.pass_code}")

                                    print('\n')
                            else:
                                print('\n')
                                print("You don't seem to have any credentials saved yet")
                                print('\n')

                        elif short_code == 'fc':
                            print("Enter the application name you want to search for; e.g., Facebook, Twitter, e.t.c,")
                            search_application = input()
                            if check_existing_credential(application):
                                search_credential = find_credential(search_application)
                                print ('\n')
                                print("Account exists. Your credentials are:")
                                print(f"Username: {search_credential.account_username}")
                                print(f"Password: {search_credential.pass_code}")
                                print('-' * 20)
                                print ('\n')
                            else:
                                print('\n')
                                print("Account does not exist")
                                print ('\n') 
                                continue 
                                
                        elif short_code == "d":
                            print ('\n') 
                            print("Enter the application name of the account you want to delete")
                            search_application = input()
                            if check_existing_credential(application):
                                search_credential = find_credential(search_application)
                                print("_"*50)
                                search_credential.delete_credential()
                                print('\n')
                                print(f"Your {search_credential.application_name} account has been successfully deleted!!!")
                                print('\n')
                            else:
                                print("Account does not exist")
                                print('\n')        
                                    
                        elif short_code == "ex":
                            print("Go back to main page")
                            break
                        else:
                            print("Please try again")
                                                                           
        
if __name__ == '__main__':

    main()        