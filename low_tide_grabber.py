import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re


locations_of_interest = {
    "Half Moon Bay, California": {"url": "https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest"},
    "Huntington Beach, California": {"url": "https://www.tide-forecast.com/locations/Huntington-Beach/tides/latest"},
    "Providence, Rhode Island": {"url": "https://www.tide-forecast.com/locations/Providence-Rhode-Island/tides/latest"},
    "Wrightsville Beach, North Carolina": {"url": "https://www.tide-forecast.com/locations/Wrightsville-Beach-North-Carolina/tides/latest"}
}


def find_daylight_low_tides(location_dict):
    """
    A function for parsing a location's tide data from www.tide-forecast.com to find upcoming daylight low tide
    events for tide pool exploration
    """

    for name, details in location_dict.items():
        print("\n%s searching for daylight low tides..." % name)

        # get location page's full html
        html = requests.get(details["url"]).content

        # create a BeautifulSoup object that can be used to find the CDATA
        soup = BeautifulSoup(html, 'html.parser')
        # get the one script tag that contains the data of interest
        script_data = soup.find_all('script', string=re.compile("window.FCGON"))[0]

        # load the json data into a dictionary
        tide_data = json.loads(str(script_data.text).split('window.FCGON = ')[1].split(';\n//')[0])

        # loop over the daily tide data, detect daylight low tide events
        for tide_day in tide_data['tideDays']:
            # first grab this day's sunrise and sunset timestamps
            this_day_sunrise_utc = datetime.utcfromtimestamp(tide_day['sunrise'])
            this_day_sunset_utc = datetime.utcfromtimestamp((tide_day['sunset']))

            # investigate each individual tide data point. If it meets the criteria perform celebratory print!
            for datum in tide_day['tides']:

                if datum['type'] == 'low':  # only interested in low tide events
                    low_tide_utc = datetime.utcfromtimestamp(datum['timestamp'])

                    if (this_day_sunrise_utc < low_tide_utc) & (low_tide_utc < this_day_sunset_utc):    # during daylight?
                        # Daylight low tide event detected! Print the local time and height details:
                        print("\tDaylight low tide found:\n\t\tTime: %s %s (local time)\n\t\tHeight: %0.1f ft" % (tide_day["date"], datum["time"], datum['height'] * 3.28084))


if __name__ == "__main__":
    find_daylight_low_tides(locations_of_interest)
