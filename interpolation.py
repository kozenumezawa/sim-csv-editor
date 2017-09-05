import csv
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import json

def read_detail_data():
    f = open('./Nagumo/detail_data.csv', 'r')
    data_reader = csv.reader(f)

    one_data = []
    for (i, row) in enumerate(data_reader):
        if i == 0:
            print row   # print label
            continue
        one_data.append(row[2])
    return np.array(one_data, np.float32)


def compared_to_detail():
    f = open('./data/Nagumo.csv', 'r')
    data_reader = csv.reader(f)

    one_data = {
        't': [],
        'x': []
    }

    time = [i for i in range(0, 55, 5)]

    for (t, row) in zip(time, data_reader):
        one_data['t'].append(t)
        one_data['x'].append(row[50 * (10 - 1) + (25 - 1)])


    t = np.array(one_data['t'], np.float)
    x = np.array(one_data['x'], np.float)

    tck = interpolate.splrep(t, x)

    tnew = np.array([i for i in range(0, 55, 1)], np.float)
    xnew = interpolate.splev(tnew, tck, der=0)

    tdetail = np.array([float(i / 10) for i in range(0, 501, 1)], np.float)
    xdetail = read_detail_data()

    plt.figure()
    plt.plot(t, x, 'x', tnew, xnew, 'b', tdetail, xdetail)


if __name__ == '__main__':
    f = open('./data/Nagumo.csv', 'r')
    data_reader = csv.reader(f)

    all_data = []
    for i in range(2500):
        all_data.append([])

    time = [i for i in range(0, 55, 5)]

    for (t, row) in zip(time, data_reader):
        for (idx, scalar) in enumerate(row):
            all_data[idx].append(scalar)

    all_data = np.array(all_data, np.float32)

    t = np.array(time, np.float)

    tck_list = []
    interpolate_list = []
    t_detail = np.array([float(i / 10) for i in range(0, 501, 1)], np.float)
    for (idx, x) in enumerate(all_data):
        tck_list.append(interpolate.splrep(t, x))
        x_new =  interpolate.splev(t_detail, tck_list[idx], der=0)
        interpolate_list.append(x_new.tolist())

    # print(interpolate_list.shape) = (2500, 501)

    saveJSON = {
        'allTimeSeries': interpolate_list[::-1], # reverse interpolate_list
        'width': 50
    }
    f = open("./data/NagumoInterpolate.json", "w")
    json.dump(saveJSON, f)
    f.close()
