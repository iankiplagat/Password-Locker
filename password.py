class User:
    """
    Class that generates new instances of users
    """

    user_list = [] # Empty user list

    def __init__(self, first_name, last_name, phone_number, email, user_name, password):

        '''
        __init__ method that helps us define properties for our objects.

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.user_name = user_name
        self.password = password

        