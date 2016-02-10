"""
Created on 09.02.2016

@author: Paul Kalauner 5BHIT
"""
import unittest
from CsvExampleController import CsvExampleController
from CsvExampleModel import CsvExampleModel


class TestAllgemein(unittest.TestCase):
    def test_valid_csv_1row(self):
        truedict = {'Spalte1': 'z1s1', 'Spalte2': 'z1s2'}
        self.model = CsvExampleModel()
        self.model.read_file("tests/file_1row.csv")
        for cur in self.model.data_list:
            for key in cur:
                self.assertEqual(cur[key], truedict[key])

    def test_valid_csv_2rows(self):
        truelist = [{'Spalte1': 'z1s1', 'Spalte2': 'z1s2'}, {'Spalte1': 'z2s1', 'Spalte2': 'z2s2'}]
        self.model = CsvExampleModel()
        self.model.read_file("tests/file_1row.csv")
        for i in range(len(self.model.data_list)):
            for key in self.model.data_list[i]:
                self.assertEqual(self.model.data_list[i][key], truelist[i][key])

    def test_controler_valid_csv(self):
        truelist = [{'Spalte1': 'z1s1', 'Spalte2': 'z1s2'}, {'Spalte1': 'z2s1', 'Spalte2': 'z2s2'}, {'Spalte1': 'z3s1', 'Spalte2': 'z3s2'}]
        c = CsvExampleController()
        c.read_file()
        for i in range(len(c.model.data_list)):
            for key in c.model.data_list[i]:
                self.assertEqual(c.model.data_list[i][key], truelist[i][key])

    def test_not_existing_file(self):
        self.model = CsvExampleModel()
        self.assertRaises(FileNotFoundError, self.model.read_file, "notexisting.csv")

    def test_empty_csv_file(self):
        self.model = CsvExampleModel()
        self.assertRaises(Exception, self.model.read_file, "empty.csv")


if __name__ == "__main__":
    unittest.main()
