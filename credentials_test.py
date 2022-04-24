#  import unittest
#  from credentials import Credentials
#  import pyperclip

#  class TestCredentials(unittest.TestCase):

#      def setUp(self):
#          '''
#          setup before a test is run
#          '''
#          self.new_cred = Credentials("GitHub", "evalinemacharia99@gmail.com","@19998906Eva")
    

#         #######check initialization##########

#      def test_init(self):
#          '''
#          check if instances initialize as expected
#          '''
#          self.assertEqual(self.new_cred.account, "GitHub")
#          self.assertEqual(self.new_cred.email, "evalinemacharia99@gmail.com")
#          self.assertEqual(self.new_cred.passlock, "@19998906Eva")

#      def tearDown(self):
#          '''
#          clear list before any test is run
#          '''
#          Credentials.cred_list = []  

#      ##save 
#      def test_save_multiple_cred(self):
            
        
#          self.new_cred.save_cred()
        
#          self.assertEqual(len(Credentials.cred_list),1)

#      def test_save_multiple_cred(self):
          
#          self.new_cred.save_cred()
#          test_cred = Credentials("Instagram","testuser","password") # new credentials
#          test_cred.save_cred()
#          self.assertEqual(len(Credentials.cred_list),2)  
#      def test_delete_credentials(self):
#          '''
#          test if you can delete credentials test
#          '''
#          self.new_cred.save_cred()
#          test_cred = Credentials("Instagram", "testuser","password")
#          test_cred.save_cred()
#          self.new_cred.delete_cred()
#          self.assertEqual(len(Credentials.cred_list), 1)    

#  def test_search_for_cred(self):
#         '''
#         test if credentials can be searched for
#         '''
#         self.new_cred.save_cred()
#         test_cred = Credentials("Twitter", "testuser","password")
#         test_cred.save_cred()
#         find_cred= Credentials.find_account("Twitter")
#         self.assertEqual(find_cred.account, test_cred.account)
        
#         ############11th test########### confirm accounts credentials##########

#     def test_confirm_cred_exists(self):
#         '''
#         confirm that credentials actually exists
#         '''
#         self.new_cred.save_cred()
#         test_cred = Credentials("Twitter", "testuser","password")
#         test_cred.save_cred()
#         cred_exists = Credentials.cred_exists("Twitter")
#         self.assertTrue(cred_exists)


#         #################test 12th########Display credentials###########

        
#     def test_display_credentials(self):
#         '''
#         test if all credentials can be displayed
#         '''
#         self.assertEqual(Credentials.display_cred(), Credentials.cred_list)



#         #########copy password#########test 13th#####

#     def test_copy_password(self):
#         '''
#         test whether generated password can be copied
#         '''
#         self.new_cred.save_cred()
#         Credentials.copy_passlock("vinceobindi1005")
#         self.assertEqual(self.new_cred.passlock, pyperclip.paste())            

#  if __name__ == '__main__':
#     unittest.main()        



# ModuleNotFoundError: No module named 'user'
import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        setup before a test is run
        '''
        self.new_cred = Credentials("GitHub", "evalinemacharia99@gmail.com   ", "@19998906Eva")
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.cred_list = []

        #######check initialization##########

    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "GitHub")
        self.assertEqual(self.new_cred.email, "evalinemacharia99@gmail.com")
        self.assertEqual(self.new_cred.passlock, "@19998906Eva")

        ############7th test############

    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

        ##############8th test ##########saving multiple credentials###########

    def test_saving_multiple_creds(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Twitter", "testuser","password")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)

        ############9th test#######deleting credentials#######

    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Twitter", "testuser","password")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)


        ##############10th test############search for credentials#######

    def test_search_for_cred(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Twitter", "testuser","password")
        test_cred.save_cred()
        find_cred= Credentials.find_account("Twitter")
        self.assertEqual(find_cred.account, test_cred.account)
        
        ############11th test########### confirm accounts credentials##########

    def test_confirm_cred_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Twitter", "testuser","password")
        test_cred.save_cred()
        cred_exists = Credentials.cred_exists("Twitter")
        self.assertTrue(cred_exists)


        #################test 12th########Display credentials###########

        
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)



        #########copy password#########test 13th#####

    def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_cred.save_cred()
        Credentials.copy_passlock("@19998906Eva")
        self.assertEqual(self.new_cred.passlock, pyperclip.paste())            
