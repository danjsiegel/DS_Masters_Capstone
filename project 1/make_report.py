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
        data.sort(key=operator.attrgetter('appearancesInComics'), reverse=True)
        return data[0:10]

def markdownWriter(outputMDFile, topTenAvengers):
    with open(outputMDFile, 'w') as mdWriter:
        for record in range(len(topTenAvengers)):
            mdWriter.writelines(("#",str((record+ 1))+". ", topTenAvengers[record].name, '\n\n'))
            mdWriter.writelines(("*Number of Appearances:", str(topTenAvengers[record].appearancesInComics), '\n'))
            mdWriter.writelines(("*Year Joined:", str(topTenAvengers[record].joinYear), '\n'))
            mdWriter.writelines(("*Years Since Joining:", str(topTenAvengers[record].yearsSince), '\n'))
            mdWriter.writelines(("*URL:", topTenAvengers[record].assignedURL, '\n\n'))
            mdWriter.writelines(("## Notes\n\n"+topTenAvengers[record].notesData, '\n\n'))


if __name__ == "__main__":
    csvToRead = argumentExists(1)
    csvToCreate = argumentExists(2)
    top10 = readCSVData(csvToRead)
    markdownWriter(csvToCreate,top10)
