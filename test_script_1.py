import csv
from datetime import datetime

def cicleDT(reader, idx):
    mySet = set()
    
    for i in range(1, len(reader)):
        if reader[i][idx] not in mySet:
            mySet.add(reader[i][idx])
    return mySet

def cicleInt(reader, idx):
    mySet = set()

    for i in range(1, len(reader)):
        if reader[i][idx] not in mySet:
            mySet.add(int(reader[i][idx]))
    return mySet

def makeTitle(reader):
    resultData = [[]]

    mySet = cicleInt(reader, 1)
    tmpList = list(mySet)
    tmpList.sort()

    for elem in tmpList:
        resultData[0].append(str(elem))
        resultData[0].append(str(elem))
    resultData[0].insert(0, "Date/Pos")
    return resultData

def makeTableDict(reader, setOfDates, posLst):
    tmpDictSum = {}

    for date in setOfDates:
        tmpDictSum.setdefault(date, {})
        for pos in posLst:
            tmpDictSum[date][pos] = 0

    for elDate in setOfDates:
        for row in reader:
            if elDate == row[3]:
                if row[1] not in tmpDictSum[elDate]:
                    tmpDictSum[elDate][row[1]] = float(row[2])
                if row[1] in tmpDictSum[elDate]:
                    tmpDictSum[elDate][row[1]] += float(row[2])

    for keys, vals in tmpDictSum.items():
        for keys1, vals1 in vals.items():
            tmpDictSum[keys][keys1] = round(vals1, 2)
    return tmpDictSum

def makeLsts(reader):
    datesLst, posLst = [], []

    for i in range(len(reader)):
        if i == 0:
            continue
        if reader[i][3] not in datesLst:
            datesLst.append(reader[i][3])
        if int(reader[i][1]) not in posLst:
            posLst.append(int(reader[i][1]))
    posLst = sorted(posLst, reverse=False)
    for i in range(len(posLst)):
        posLst[i] = str(posLst[i])
    return datesLst , posLst

def makeTable(resultData, reader):
    mySet = cicleDT(reader, 3)
    datesLst, posLst = makeLsts(reader)
    myDict = makeTableDict(reader, mySet, posLst)
    datesLst = sorted(datesLst, key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), reverse=False)
    cnt = 1
    for date in datesLst:
        dateSum = 0
        resultData.append([])
        resultData[cnt].append(date)
        for _, value in myDict[date].items():
            dateSum += value
        for pos in posLst:
            resultData[cnt].append(myDict[date][str(pos)])
            resultData[cnt].append(str(int(myDict[date][pos] / dateSum * 100)) + "%")
        cnt += 1
    return resultData

def test_script_1():
    readerList = []
    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            readerList.append(row)
        resultData = makeTitle(readerList)
        resultData = makeTable(resultData, readerList)
        myFile = open('data_out.csv', 'w')
        with myFile:
            writer = csv.writer(myFile, delimiter=';')
            writer.writerows(resultData)

if __name__ == '__main__':
    test_script_1()
