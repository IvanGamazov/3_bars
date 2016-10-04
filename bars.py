import json
from pprint import pprint


def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data


def get_biggest_bar(data):
    biggest_bars = []
    maxseats = max(data, key=lambda d: d['Cells']['SeatsCount'])
    for bar in data:
        if bar['Cells']['SeatsCount'] == maxseats['Cells']['SeatsCount']:
            biggest_bars.append(bar['Cells']['Name'])
    return biggest_bars


def get_smallest_bar(data):
    smallest_bars = []
    minseats = min(data, key=lambda d: d['Cells']['SeatsCount'])
    for bar in data:
        if bar['Cells']['SeatsCount'] == minseats['Cells']['SeatsCount']:
            smallest_bars.append(bar['Cells']['Name'])
    return smallest_bars


def get_closest_bar(data, longitude, latitude):
    nearest_bar = min(data, key=lambda bar: (
        (bar['Cells']['geoData']['coordinates'][0] - longitude) ** 2
        + (bar['Cells']['geoData']['coordinates'][1] - latitude) ** 2
    )
                      )
    return nearest_bar['Cells']['Name']


def main():
    filepath = input("Enter data file name --> ")
    data = load_data(filepath)
    pprint('--------------------Smallest Bars---------------------')
    smallest_bars =  get_smallest_bar(data)
    for bar in smallest_bars:
        print(bar)

    pprint('--------------------Biggest Bars---------------------')
    biggest_bars = get_biggest_bar(data)
    for bar in biggest_bars:
        print(bar)

    pprint('--------------------Closest Bar---------------------')
    longitude = input("Enter your longitude --> ")
    latitude = input("Enter your latitude --> ")
    nearest_bar = get_closest_bar(data, float(longitude), float(latitude))
    print(nearest_bar)


if __name__ == '__main__':
    main()
