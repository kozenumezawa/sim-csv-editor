import csv
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

if __name__ == '__main__':
    f = open('./data/Nagumo.csv', 'r')
    writer = csv.writer(f)
    data_reader = csv.reader(f)

    one_data = {
        't': [],
        'x': []
    }

    time = [i for i in range(0, 55, 5)]

    for (t, row) in zip(time, data_reader):
        one_data['t'].append(t)
        one_data['x'].append(row[0])

    t = np.array(one_data['t'], np.float)
    x = np.array(one_data['x'], np.float)

    tck = interpolate.splrep(t, x)

    tnew = np.array([i for i in range(0, 55, 1)], np.float)
    xnew = interpolate.splev(tnew, tck, der=0)

    plt.figure()
    plt.plot(t, x, 'x', tnew, xnew, 'b')

    plt.legend(['True', 'Cubic Spline'])
    plt.show()