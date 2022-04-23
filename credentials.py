class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

        #########Assign propety to credentil list#########
    def __init__(self, account , email , passlock):
    
        self.account = account
        self.email = email
        self.passlock = passlock


        #########save credentials##########

    def save_cred(self):
        '''
        self credentials in cred_list
        '''
        Credentials.cred_list.append(self)

        ############Delete credentils#########

    def delete_contact(self):

        '''
        delete_credentials method deletes a saved contact from the credentials_list
        '''

        Credentials.credentials_list.remove(self)  

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a account and returns a account that matches that account.

        Args:
            number:account to search for
        Returns :
            credential of person that matches the account.
        '''

        for cred in cls.cred_list:
            if cred.account == account:
                return cred  
    @classmethod
    def cred_exist(cls,account):
        '''
        Method that checks if a cred exists from the credentials list.
        Args:
            number: account to search if it exists
        Returns :
            Boolean: True or false depending if the Cred exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                    return True

        return False  
    @classmethod
    def display_cred(cls):
        '''
        method that returns the contact list
        '''
        return cls.cred_list            