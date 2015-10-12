#! /usr/bin/env python3
'''
Menu uses the Wok module to download the menu information from
UW-Madison's NetNutrition website and present it in a text-based
interface.
'''
import argparse
import wok
import libs.input

LOC_MAPPINGS = {
    'gordons': 1,
    'coffee': 30,
    'bean and creamery': 30,
    'dejope': 31,
    'flm': 31,
    'four lakes market': 31,
    'grab': 54,
    'grab and go': 54,
    'liz': 54,
    'lw': 54,
    'ew': 54,
    'elizabeth waters': 54,
    'liz waters': 54,
    'newells': 67,
    'newell': 67,
    'newells deli': 67,
    'rhetas': 72,
    'rhetas market': 72,
    'chad': 72,
    'carsons': 98,
    'carsons market': 98,
    'que rico': 109,
    'eagles wing': 111
}

parser = argparse.ArgumentParser()
parser.add_argument('location')
args = parser.parse_args()

if args.location in LOC_MAPPINGS:
    locid = LOC_MAPPINGS[args.location]
else:
    print('Sorry, that location is not known.')
    quit()

w = wok.Wok()
w.fetch_locations()
loc = w.get_location(locid)
loc.fetch_stations()

station = None
while not station:
    for station in loc.stations:
        print('%i: %s' % (station.id, station.name))

    try:
        stationid = libs.input.ask_user_int('Station ID:')
        station = loc.get_station(stationid)
    except IndexError:
        print('That Station ID does not exist. Please try again')

station.fetch_menus()
for menu in station.menus:
    menu.fetch_items()
for menu in station.menus:
    print('Menu: %s: %s' % (menu.datetext, menu.timeofday))
    for item in menu.items:
        print('  {0:50}{1:20}{2:7}'.format(item.name, item.servingsize, item.price))


