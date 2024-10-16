"""Module that will cover test cases"""
import unittest
import os
import myapp

class TestMyApp(unittest.TestCase):
    """Class where the basic test will be performed"""
    def test_app_exist(self):
        """Method testing if the app itself exists"""
        app = myapp.PDFConverter()
        print(app)
        self.assertIsNotNone(app)

    def test_asserts_exist(self):
        """Check that the pdf used here works"""
        cwd = os.getcwd()
        pdf = os.path.join(cwd,"..","Assets","Run locally backend.pdf")
        self.assertTrue(os.path.isfile(pdf))

    def test_asserts_format_correct_return(self):
        """Test to check if is STR the output"""
        output = myapp.format_file("")
        self.assertIsInstance(output, str)

if __name__ == '__main__':
    unittest.main()
