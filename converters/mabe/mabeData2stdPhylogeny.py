import json
import csv
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-path', type=str, metavar='PATH', default = '',  help='path to files - default : none (will read files in current directory)', required=False)
parser.add_argument('-fileType', type=str, metavar='TYPE', default = 'snapshot',  help='type of file, snapshot or SSwD, default : snapshot', required=False)
parser.add_argument('-columnNames', type=str, metavar='COLUMN_NAME', default = [],  help='column names of data to read from source files - default : ID score_AVE timeOfBirth (will automatically include ancestors)',nargs='+', required=False)
parser.add_argument('-newColumnNames', type=str, metavar='COLUMN_NAME', default = [],  help='column names of data to be copied into new data file - default : ID score timeOfBirth (will automatically include parents)',nargs='+', required=False)
parser.add_argument('-updateRange', type=int, metavar=('FIRST','LAST','STEP'), default = [0,100,10],  help='update range first, last, step', nargs=3, required=True)
parser.add_argument('-verbose', action='store_true', default = False, help='adding this flag will provide more text output while running (useful if you are working with a lot of data to make sure that you are not hanging) - default (if not set) : OFF', required=False)

args = parser.parse_args()

if args.fileType == "SSwD":
    ancestorsColumnName = 'ancestors_LIST'
    filePrefix = 'SSwD_data_'
else:
    ancestorsColumnName = 'snapshotAncestors_LIST'
    filePrefix = 'snapshot_data_'

	
ofInterest = []
ofInterest.append('ID')
ofInterest.append(ancestorsColumnName)
ofInterest.append('timeOfBirth')
ofInterest = ofInterest + args.columnNames  # find these columns

ofInterestRenames = []
ofInterestRenames.append('ID')
ofInterestRenames.append('ancestors')
ofInterestRenames.append('origin_time')
ofInterestRenames = ofInterestRenames + args.newColumnNames # save them with these new column names

filePath = args.path
rawData = {}

mustGetHeader = True
for t in range(args.updateRange[0],args.updateRange[1]+1,args.updateRange[2]):
    fileName = filePath + filePrefix + str(t) + '.csv'
    with open(fileName, 'r') as csvfile:
        if(args.verbose):
            print('loading',fileName)

        data = csv.reader(csvfile, delimiter=',', quotechar='"')
        firstLineInFile = True
        for line in data:
            if firstLineInFile: # first line of file, do not recored to raw data
                firstLineInFile = False
                if mustGetHeader: # first line, of first file; keep it as header
                    origColumnNames = line
                    mustGetHeader = False
                    # get index of ID
                    IDIndex = line.index('ID')
            else:
                rawData[line[IDIndex]] = line # if same ID appears more then once, save the last appearance

                
ofInterestIndices = [origColumnNames.index(colName) for colName in ofInterest]

#construct a data object we can serialize
outData = {}

for orgID in rawData:
    dataOnThisLine = {}
    for colIndex,colName in zip(ofInterestIndices,ofInterestRenames):
        if rawData[orgID][colIndex][0] == '[':
            dataOnThisLine[colName]=[int(s) for s in rawData[orgID][colIndex][1:-1].split(',')]
        else:
            dataOnThisLine[colName]=rawData[orgID][colIndex]
    outData[orgID] = dataOnThisLine

csv_file = "lineage.csv"

print('saving',csv_file)
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=ofInterestRenames, lineterminator="\n")
    writer.writeheader()
    for orgID in rawData:
        writer.writerow(outData[orgID])

json_file = 'lineage.json'
print('saving',json_file)

with open(json_file, 'w') as fp:
    json.dump(outData, fp, sort_keys=False)
    