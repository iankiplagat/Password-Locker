class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self, user_name, user_password):
        # docstring removed for simplicity

        self.user_name = user_name
        self.user_password = user_password

    user_list = []  # Empty user list

    # Init method up here
    def save_user(self):
        """
        save_user method saves user objects into user_list
        """

        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from the user_list
        """

        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        """
        method that returns the user list
        """
        return cls.user_list
