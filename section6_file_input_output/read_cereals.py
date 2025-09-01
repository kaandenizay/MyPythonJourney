import csv

DATA_PATH = '../data/'
csv_filename = 'cereal_grains.csv'

with open(DATA_PATH + csv_filename, encoding='utf-8', newline='') as csv_file:
    # reader = csv.reader(csv_file)
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    """
    QUOTE_NONNUMERIC tells that all non-numeric values have been quoted
    """
    for row in reader:
        print(row)
