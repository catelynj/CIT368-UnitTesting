from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        li = ['15646', '17701', '17028', '10101', '00000']
        #HAPPY PATH
        for string in li:
            self.assertTrue(Validate.zip(string))

    def test_zip_bad(self):
        #ABUSE
        f = open("./blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))
            
    def test_age(self):
        #HAPPY PATH
        ages = range(1, 18)
        for age in ages:
            self.assertTrue(Validate.minor(age))
            
        for age in range(18,150):
            self.assertFalse(Validate.minor(age))

if __name__ == '__main__':
    unittest.main()
