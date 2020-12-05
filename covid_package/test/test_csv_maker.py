import unittest
import os

from covid_package.script.csv_maker import country_check


class TestCovid19(unittest.TestCase):
    """Performs unittest on the country_check function
    """

    def setUp(self):
        """Creates a temporary file
        """
        self.temporary_file = "/tmp/temporary_file"
        f = open(self.temporary_file, "w")
        f.close()

    def test_valid_datafile(self):
        """Tests the function with the correct path
        """
        df = country_check(path="covid_package/csv/country_list.csv")
        self.assertTrue(df)

    def test_no_datafile(self):
        """Tests the function with an inexisting file
        """
        df = country_check(path="questofilenonesiste")
        self.assertFalse(df)

    def test_empty_datafile(self):
        """Tests the function with an empty file that we created before
        """
        df = country_check(path=self.temporary_file)
        self.assertFalse(df)

    def test_invalid_datafile(self):
        """Tests the function with an invalid file
        """
        df = country_check(path="meme.jpeg")
        self.assertFalse(df)

    def tearDown(self):
        """Removes the temporary file
        """
        os.remove(self.temporary_file)
