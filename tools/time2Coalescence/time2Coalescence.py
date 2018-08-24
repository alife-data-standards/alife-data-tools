import json
import csv
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-path', type=str, metavar='PATH', default = '',  help='path to files - default : none (will read files in current directory)', required=False)
parser.add_argument('-file', type=str, metavar='NAME', default = 'lineageData.csv',  help='name of data file. default : lineageData.csv', required=False)
parser.add_argument('-verbose', action='store_true', default = False, help='adding this flag will provide more text output while running (useful if you are working with a lot of data to make sure that you are not hanging) - default (if not set) : OFF', required=False)

args = parser.parse_args()

filePath = args.path
filename = args.file
fileName = filePath + filename

with open(filePath+filename, 'r') as fp:
    data = json.load(fp)


parentData = {}
birthData = {}
lastBirthDate = -1

lineNumber = 0

print("loading data",end='')


for key in data:
    if lineNumber%10000 == 0:
        print('.',end='',flush=True)
    lineNumber += 1
    parentData[int(key)] = [int(p) for p in data[key]['ancestors']]
    parentData[int(key)].sort()
    birthData[int(key)] = int(data[key]['origin_time'])
    lastBirthDate = max(lastBirthDate,birthData[int(key)])

print() # newline after all data has been loaded
print('last orgs were born at time',lastBirthDate,flush=True)

lastGenerationAncestors = {}
for ID in birthData:
    if birthData[ID] == lastBirthDate:
        lastGenerationAncestors[ID] = parentData[ID]
        
parentList = []

for ID in lastGenerationAncestors:
    parentList.append(ID);

while 1:
    if(args.verbose):
        print("at time",birthData[parentList[0]],"... considering",len(parentList),"orgs.",parentList,flush = True)
    newParentList = []
    foundUnique = False # we have not found any unique parents lists
    first = True
    firstParentsList = []
    for ID in parentList:
        if first:
            firstParentsList = parentData[ID]
            first = False
        else:
            if parentData[ID] != firstParentsList:
                foundUnique = True # we are not done
        for parent in parentData[ID]:
            if parent not in newParentList:
                newParentList.append(parent)
    parentList = newParentList;
    if(birthData[parentList[0]] == -1):
        print('reached organism with time of birth -1. There is no MRCA(s)')
        exit(1)
    if not foundUnique: # all orgs do have the same parents list
        oldestBirth = min([birthData[x] for x in parentList])
        print('\nCoalescence found at time', oldestBirth, '\n ', lastBirthDate - oldestBirth,'time steps before oldest organism was born.\nMRCA(s) has ID(s):',parentList)
        exit(1)
