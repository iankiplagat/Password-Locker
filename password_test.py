import unittest # Importing the unittest module
from password import User # Importing the password class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = User("Ian","Kiplagat","0742579020","ianjkiplagat@gmail.com","kasparov-creat","IAN") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"Ian")
        self.assertEqual(self.new_password.last_name,"Kiplagat")
        self.assertEqual(self.new_password.phone_number,"0742579020")
        self.assertEqual(self.new_password.email,"ianjkiplagat@gmail.com")
        self.assertEqual(self.new_password.user_name,"kasparov-creat")
        self.assertEqual(self.new_password.password,"IAN")


if __name__ == '__main__':
    unittest.main()