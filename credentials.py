class credentials:
    """
    Class that generates new instances of contacts
    """
    def __init__(self,account,email,passlock):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account: New account.
            email : New email.
            passlock: New passlock.
            
        '''
class Contact:
    """
    Class that generates new instances of contacts.
    """

    def __init__(self,account,email,passlock):

      # docstring removed for simplicity

        self.account = account
        self.email = email
        self.passlock = passlock
class Contact:
    """
    Class that generates new instances of contacts.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account,email,passlock):

      # docstring removed for simplicity

        self.account = account
        self.email = email
        self.passlock = passlock
                
        