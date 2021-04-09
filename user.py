class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self, first_name, last_name, number, email, user_name, password):
        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.user_name = user_name
        self.password = password

    user_list = []  # Empty user list

    # Init method up here
    def save_user(self):
        """
        save_user method saves contact objects into user_list
        """

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
