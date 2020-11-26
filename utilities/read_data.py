import csv

def getCSVData(fileName):

    # create an empty list to store rows
    rows = []

    # open the CSV file
    dataFile = open(fileName, "r")

    # create a CSV reader from the CSV file
    reader = csv.reader(dataFile)

    # skip the headers
    next(reader)

    # add rows from the reader to list
    for row in reader:
        rows.append(row)
    return rows