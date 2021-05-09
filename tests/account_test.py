import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")

        

    # Test an Account can add a Profile
    def test_account_add_profile(self):
        self.profile.append()
    # Test an Account can remove a given Profile
    def test_account_remove_profile(self):
        self.account.remove()
    # Test an Account can return a list of Profiles
    def test_return_list_of_profiles(self):
        return profile()
   
