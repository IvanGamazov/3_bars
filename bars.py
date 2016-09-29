import json
from pprint import pprint


def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data


def get_biggest_bar(data):
    maxseats = max(data, key=lambda d: d['Cells']['SeatsCount'])
    for x in data:
        if x['Cells']['SeatsCount'] == maxseats['Cells']['SeatsCount']:
            pprint(x)


def get_smallest_bar(data):
    minseats = min(data, key=lambda d: d['Cells']['SeatsCount'])
    for x in data:
        if x['Cells']['SeatsCount'] == minseats['Cells']['SeatsCount']:
            pprint(x)


def get_closest_bar(data, longitude, latitude):
    nearest_bar = min(data, key=lambda x:((x['Cells']['geoData']['coordinates'][0] - longitude)**2 + (x['Cells']['geoData']['coordinates'][1] - latitude)**2))
    pprint(nearest_bar)


def main():
    filepath = input("Enter data file name --> ")
    data = load_data(filepath)
    pprint('--------------------Smallest Bars---------------------')
    get_smallest_bar(data)
    pprint('--------------------Biggest Bars---------------------')
    get_biggest_bar(data)
    pprint('--------------------Closest Bar---------------------')
    longitude = input("Enter your longitude --> ")
    latitude = input("Enter your latitude --> ")
    get_closest_bar(data, float(longitude), float(latitude))


if __name__ == '__main__':
    main()