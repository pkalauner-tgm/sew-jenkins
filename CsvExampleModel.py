"""
Autor: Paul Kalauner 5BHIT
"""
import csv


class CsvExampleModel(object):

    def __init__(self):
        self.data_list = []

    def read_file(self, filename):
        with open(filename) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, dialect=dialect)
            for row in reader:
                self.data_list.append(row)
