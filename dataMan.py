import csv
import pickle
import math

# noinspection PyGlobalUndefined
global mean_key
mean_key = []
# noinspection PyGlobalUndefined
global var_key
var_key = []
# noinspection PyGlobalUndefined
global data
global norm_data


def pickle_csv(file_path):
    reader = csv.reader(open(file_path))
    global data
    data = {}
    for row in reader:
        key = row[0]
        if key in data:
            pass
        data[key] = row[1:]
    pickle.dump(data, open('dataObj.p', 'wb'))
    print('[+}Read data and stored with pickle')


def load_all_data():
    print("[+] Loading data")
    global data
    data = pickle.load(open('dataObj.p', 'rb'))
    global norm_data
    norm_data = pickle.load(open('norm_dataObj.p', 'rb'))
    global mean_key
    mean_key = pickle.load(open('mean_keyObj.p','rb'))
    global var_key
    var_key = pickle.load(open('var_keyObj.p', 'rb'))
    print("[+] Data loaded")


def update_keys():
    print('[+]Udating keys')

    global mean_key
    mean_key = []
    global var_key
    var_key = []

    k = 0
    for i in data:
        tot = 0
        n = 0
        for j in data[i]:
            tot += float(j)
            n += 1
        mean_key.append(tot/n)
        k += 1

    k = 0
    for i in data:
        tot = 0
        n = 0
        for j in data[i]:
            tot += ((float(j) - mean_key[k]) * (float(j) - mean_key[k]))
            n += 1
        var_key.append(math.sqrt(tot / n))
        k += 1

    print("[+]Keys updated")


def normalize():
    global norm_data
    norm_data = data
    k = 0
    print('[+]normalizing ')
    for i in data:
        for j in range(len(data[i])):
            norm_data[i][j] = (float(data[i][j])-mean_key[k])/var_key[k]
        k += 1

def save_all_data():
    print('[+]Saving all data')
    pickle.dump(data, open('dataObj.p', 'wb'))
    pickle.dump(norm_data, open('norm_dataObj.p', 'wb'))
    pickle.dump(mean_key, open('mean_keyObj.p', 'wb'))
    pickle.dump(var_key, open('var_keyObj.p', 'wb'))
    print('[+]Saved all data')

load_all_data()
update_keys()
normalize()
save_all_data()