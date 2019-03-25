import main
import unittest

testingList = main.UsersList(main.list)
testingUser = main.User("KARIN","GLUZMAN","female","27","020")

class TestFindMatching(unittest.testcase):

    def test_that_matching_gender_not_equal_to_mine(self):
                mine_gender = testingUser.gender
                self.assertNotEqual(mine_gender, testingList.find_matching(testingUser))