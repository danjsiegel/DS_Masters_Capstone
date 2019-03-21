import csv
import sys
import operator
from msds510.avenger import *
from msds510.utils.conversion import *

def readCSVData(inputCSV):
    with open(inputCSV, 'r') as avg:
        reader = csv.reader(avg)
        header = next(reader)
        for keys in range(len(header)):
            header[keys]=make_nice_name(header[keys])
        data = [Avenger(dict(zip(header, row))) for row in reader]
        return [header, data]

def processedCSV(output, headers, input):
    with open(output, 'w', newline='') as written:
        newCSV = csv.writer(written)
        newCSV.writerow(headers)
        for row in input:
            singleAvenger = row.return_dict()
            row_to_write = []
            for header in headers:
                row_to_write.append(singleAvenger[header])
            newCSV.writerow(row_to_write)

if __name__ == "__main__":
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    if csvToRead and csvToCreate:
        csvData = readCSVData(csvToRead)
        processedCSV(csvToCreate, csvData[0], csvData[1])
