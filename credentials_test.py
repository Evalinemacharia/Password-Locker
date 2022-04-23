import unittest
from credentials import Credentials
# import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("GitHub", "evalinemacharia99@gmail.com","@19998906Eva")
    

        #######check initialization##########

    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "GitHub")
        self.assertEqual(self.new_cred.email, "evalinemacharia99@gmail.com")
        self.assertEqual(self.new_cred.passlock, "@19998906Eva")

    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []  

##save 
    def test_save_multiple_co(self):
            
        
        self.new_cred.save_cred()
        
        self.assertEqual(len(Credentials.cred_list),1)
    

if __name__ == '__main__':
    unittest.main()        