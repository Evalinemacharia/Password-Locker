
import unittest # Importing the unittest module
from user import User # Importing the User class
class TestUser(unittest.TestCase): 

    
    
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("evalinemacharia99@gmail.com", "@19998906Eva") #new User created

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []

    

    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "Evalinemacharia")
        self.assertEqual(self.new_user.password, "@19998906Eva")



    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

        

    def test_save_mutliple_users(self):
        '''
        check whether you can store more than one user
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

       
    def test_delete_user(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)




    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("Evalinemacharia")
        self.assertEqual(found_user.username, self.new_user.username)



if __name__ == '__main__':
  unittest.main()
