import argparse
import csv
import arrow
import googlemaps

MAPS_API_KEY = ''

gmaps = googlemaps.Client(key=MAPS_API_KEY)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--startpoint')
    parser.add_argument('-e', '--endpoint')
    parser.add_argument('-o', '--output')
    return parser.parse_args()


def write_out(filename, row):
    with open(filename, 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def run():
    args = parse_args()
    now = arrow.now()
    response = gmaps.directions(args.startpoint, args.endpoint, departure_time=now)
    name = response[0]['summary']
    duration = response[0]['legs'][0]['duration']['value']
    write_out(args.output, [now.format('YYYY-MM-DD HH:mm:ss'), args.startpoint, args.endpoint, name, duration])


if __name__ == '__main__':
    run()
