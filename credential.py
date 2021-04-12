import pyperclip
import random
import string

class Credential:
    """
    Class that generates new instances of credential
    """

    def __init__(self, application_name, account_username, pass_code):
        # docstring removed for simplicity

        self.application_name = application_name
        self.account_username = account_username
        self.pass_code = pass_code

    credential_list = []  # Empty credential list

    # Init method up here
    def save_credential(self):
        """
        save_credential method saves credential objects into credential_list
        """

        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes a saved credential from the credential_list
        """

        Credential.credential_list.remove(self)
        
    @classmethod
    def generate_passcode(cls):
        '''
        Method that generates a random alphanumeric passcode
        '''
        # Length of the generated passcode
        size = 8

        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        passcode = ''.join(random.choice(alphanum) for num in range(size) )
        
        return passcode
    

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list
    
    @classmethod
    def find_by_application_name(cls,application_name):
        '''
        Method that takes in the application name and returns a credential that matches that application.

        Args:
            application: Application name to search for
        Returns :
            Credentials of user account that matches the application name.
        '''

        for credential in cls.credential_list:
            if credential.application_name == application_name:
                return credential
    
    @classmethod
    def credential_exist(cls,application):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            application: Application name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.application_name == application:
                    return True

        return False
    
    @classmethod
    def copy_account_username(cls,application):
        credential_found = Credential.find_by_application(application)
        pyperclip.copy(credential_found.account_username)
