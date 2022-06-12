import unittest
import os

class MyTestCase(unittest.TestCase):
    def test_textfile_exist(self):
        expected = True
        actual = os.path.isfile("C:\\Users\\dgrus\\Course\\tasks.txt")
        self.assertEqual(expected, actual)  # add assertion here

    def test_database_exist(self):
        expected = True
        actual = os.path.isfile("C:\\Users\\dgrus\\Course\\reminder.sql")
        self.assertEqual(expected, actual)  # add assertion here

    def test_databaseconf_exist(self):
        expected = True
        actual = os.path.isfile("C:\\Users\\dgrus\\Course\\database_config.py")
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()
