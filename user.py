class User:
    """
    Class that generates new instances of users.
    """

    def __init__(self, name, login, user_password):
        # docstring removed for simplicity

        self.name = name
        self.login = login
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
    def user_exists(cls, login,password):
      '''
      confirm user details in the users_list to authenticate access
  
      Args:
      username: name keyed in by user to login
      password: password used by user to login
      '''
      for user in cls.user_list:
        if user.login == login and user.user_password == password:
          return user
        

    @classmethod
    def display_user(cls):
        """
        method that returns the user list
        """
        return cls.user_list
