#!/usr/bin/env python3.8

from user import User
from credential import Credential

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
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
    