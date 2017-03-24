import csv
import pickle


def csvToObjPick(filepath):
    reader = csv.reader(open(filepath))
    result = {}
    for row in reader:
        key = row[0]
        if key in result:
            pass
        result[key] = row[1:]
    pickle.dump(result, open('dataObj.p', 'wb'))

def retObjFromPick():
    result = pickle.load(open('dataObj.p','rb'))
    return result

data = retObjFromPick()
print(data['nox'])
