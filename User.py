# class User:
#     def __init__(self,username,password):

#         '''
#         __init__ method that helps us define properties for our objects.

#         Args:
#             username: New credentials username.
#             password : New password password.
           
#         '''
#     def __init__(self,username,password):

#       # docstring removed for simplicity

#         self.username = username
#         self.password = password
class Contact:
    """
    Class that generates new instances of credentials.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,username,password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
              
    def save_user(self):

        # '''
        # save_contact method saves contact objects into contact_list
        # '''

        User.user_list.append(self)  

    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)

    @classmethod
    def find_user(cls, username):
        '''
        find username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user    
    



