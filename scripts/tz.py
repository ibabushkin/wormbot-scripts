#!/usr/bin/env python
import csv
import os
from os.path import sep as PATH_SEP
import sys
import time

import requests


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = "data"
DATA_FILE = "timezones.csv"
DATA_PATH = os.path.join(SCRIPT_DIR, DATA_DIR, DATA_FILE)
if not os.path.isfile(DATA_PATH):
    print "Error: Couldn't find '{}'!".format(DATA_DIR, PATH_SEP, DATA_FILE)
    sys.exit(0)


class TimezoneDB(object):
    """TimezoneDB API implementation for looking up timezones."""

    def __init__(self, api_key):
        self.__api_key = api_key
        self.response_format = "json"


    @property
    def timezones(self):
        with open(DATA_PATH) as csv_file:
            zones = csv.reader(csv_file, delimiter=",", quotechar="\"")
            return [row for row in zones if row]


    def lookup(self, zone):
        """Looks up the timezone for the passed zone and returns it's results as json."""

        url = "https://api.timezonedb.com/" \
              "?format={fmt}&key={api_key}&zone={zone}"
        url = url.format(fmt=self.response_format, api_key=self.__api_key, zone=zone)
        r = requests.get(url)
        return r.json()


def is_valid_time_zone(tdb, timezone):
    return bool([tz for __, __, tz in tdb.timezones if tz == timezone])


def main(time_zone):
    tdb = TimezoneDB("--API KEY--")
    if not is_valid_time_zone(tdb, time_zone):
        print "Error: Invalid time zone, check http://ezl.ink/0b for a list."
        return 0

    json_data = tdb.lookup(time_zone)
    if json_data.get("status") == "FAIL":
        print json_data.get("message")
        return 0

    print "Time and date in {}: {}".format(time_zone,
                                           time.ctime(json_data.get("timestamp")))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        sys.exit(main(sys.argv[1]))

