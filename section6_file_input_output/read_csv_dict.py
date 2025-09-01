import csv

DATA_PATH = '../data/'
cereals_filename = 'cereal_grains.csv'

with open(DATA_PATH + cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
