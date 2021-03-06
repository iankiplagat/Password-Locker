import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    # Items up here .......

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("name", "login", "password")  # create user object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.name, "name")
        self.assertEqual(self.new_user.login, "login")
        self.assertEqual(self.new_user.user_password, "password")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the user list
        """
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    # setup and class creation up here
    def tearDown(self):
        """
            tearDown method that does clean up after each test case has run.
            """
        User.user_list = []

    def test_save_multiple_user(self):
        """
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            """
        self.new_user.save_user()
        test_user = User("name", "login", "password")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
            test_delete_user to test if we can remove a user from our user list
            """
        self.new_user.save_user()
        test_user = User("name", "login", "password")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_display_all_user(self):
        """
        method that returns a list of all user saved
        """

        self.assertEqual(User.display_user(), User.user_list)


if __name__ == '__main__':
    unittest.main()
