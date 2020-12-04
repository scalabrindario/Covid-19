import unittest
import os 

from covid_package.script.csv_maker import country_check


class TestCovid19(unittest.TestCase):

	def setUp(self):
		# we create a temporary file in order to test our function
		self.temporary_file = "/tmp/temporary_file"
		f = open(self.temporary_file, "w")
		f.close()

	def test_valid_datafile(self):
		df = country_check(path = "covid_package/csv/country_list.csv")
		self.assertTrue(df)

	def test_no_datafile(self):
		df = country_check(path = "questofilenonesiste")
		self.assertFalse(df)

	def test_empty_datafile(self):
		df = country_check(path = self.temporary_file)
		self.assertFalse(df)

	def test_invalid_datafile(self):
		df = country_check(path = "meme.jpeg")
		self.assertFalse(df)

	def tearDown(self):
		os.remove(self.temporary_file)