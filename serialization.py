import csv

if __name__ == '__main__':
    f = open('./data/Nagumo.csv', 'w')
    writer = csv.writer(f)

    for time in ['000', '005', '010', '015', '020', '025', '030', '035', '040', '045', '050']:
        name = './Nagumo/Div50_' + time + '.0000.csv'
        f = open(name, 'r')
        dataReader = csv.reader(f)

        
        for row in dataReader:
            print row
        data = [['lat', 'lon', 'value']]
        writer.writerows(data)

