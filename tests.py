import unittest
from dummy import getEven

# creating a brand new class but also get the attributes and functionality and
# methods coming from the unittest module
class TestFunction(unittest.TestCase):

    def test_empty(self):
        # assert whether or not something is equal
        # if getEven is an empty list it should return an empty list
        self.assertEqual(getEven([]), [])

        # input is all odd should return an empty list
    def test_all_odd(self):
        self.assertEqual(getEven([1,1,1]), [])

        # input is all even should return the entire list
    def test_all_even(self):
        self.assertEqual(getEven([2,2,4,6,8]), [2,2,4,6,8])
    
        # input is a mixute of even and odd return only even list
    def test_mix(self):
        self.assertEqual(getEven([1,2,45,6,8]), [2,6,8])
    


# run this python file if name is main
if __name__ == '__main__':
    # main() will run all the tests
    unittest.main()