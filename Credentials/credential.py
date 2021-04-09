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
    def display_credential(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list
    
    @classmethod
    def credential_exist(cls,username):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            username: Username to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_username == username:
                    return True

        return False
