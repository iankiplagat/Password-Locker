import unittest  # Importing the unittest module
from credential import Credential  # Importing the credential class
import pyperclip

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    # Items up here .......

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("application", "username", "passcode")  # create credential object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.application_name, "application")
        self.assertEqual(self.new_credential.account_username, "username")
        self.assertEqual(self.new_credential.pass_code, "passcode")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into
         the credential list
        """
        self.new_credential.save_credential()  # saving the new credential
        self.assertEqual(len(Credential.credential_list), 1)

    # setup and class creation up here
    def tearDown(self):
        """
            tearDown method that does clean up after each test case has run.
            """
        Credential.credential_list = []

    def test_save_multiple_credential(self):
        """
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            """
        self.new_credential.save_credential()
        test_credential = Credential("application", "username", "passcode")  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """
            test_delete_credential to test if we can remove a credential from our credential list
            """
        self.new_credential.save_credential()
        test_credential = Credential("application", "username", "passcode")  # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting a credential object
        self.assertEqual(len(Credential.credential_list), 1)
        
    def test_generate_passcode(self):
        '''
        Test case to test random password generation
        '''
        
        generated_passcode = self.new_credential.generate_passcode()

        self.assertEqual( len(generated_passcode), 8 )       

    def test_display_all_credential(self):
        """
        method that returns a list of all credential saved
        """

        self.assertEqual(Credential.display_credential(), Credential.credential_list)
        
    def test_find_credential_by_application(self):
        '''
        test to check if we can find a credential by the application name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("application", "username", "passcode") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_application("application")

        self.assertEqual(found_credential.account_username,test_credential.account_username)
    
        
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("application", "username", "passcode") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("application")

        self.assertTrue(credential_exists) 
        
    def test_copy_account_username(self):
        '''
        Test to confirm that we are copying the username from a found credential
        '''

        self.new_credential.save_credential()
        Credential.copy_account_username("application")

        self.assertEqual(self.new_credential.account_username,pyperclip.paste())   


if __name__ == '__main__':
    unittest.main()
