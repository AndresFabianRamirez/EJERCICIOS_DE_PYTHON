import csv
def list_diccionario (csvFile):
    with open(csvFile) as csvFile:
        
        reader = csv.reader(csvFile, delimiter=(','))
        header =next (reader)
        listV = []
        for row in reader:
            parIterable = zip(header,row)
            dicTemp = {key:value for (key,value) in parIterable}
            listV.append(dicTemp)
    return listV
 