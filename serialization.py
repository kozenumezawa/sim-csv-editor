import csv

if __name__ == '__main__':
    f = open('./data/Nagumo.csv', 'w')
    writer = csv.writer(f)

    for time in ['000', '005', '010', '015', '020', '025', '030', '035', '040', '045', '050']:
        name = './Nagumo/Div50_' + time + '.0000.csv'
        f = open(name, 'r')
        data_reader = csv.reader(f)

        serial_data = []
        for row in data_reader:
            serial_data.extend(row)
        writer.writerows([serial_data])


    f = open('./data/SD.csv', 'w')
    writer = csv.writer(f)

    for time in ['000', '005', '010', '015', '020', '025', '030', '035', '040', '045', '050']:
        name = './SD/Div50_' + time + '.0000.csv'
        f = open(name, 'r')
        data_reader = csv.reader(f)

        serial_data = []
        for row in data_reader:
            serial_data.extend(row)
        writer.writerows([serial_data])
