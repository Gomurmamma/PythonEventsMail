"""
Defines the UserInputs class for collecting user's event preferences
"""
import os
from dotenv import load_dotenv, find_dotenv
import requests
from requests.structures import CaseInsensitiveDict


class UserInputs:
    """Object used for collecting user event preferences"""

    def __init__(self):
        """Initializes UserInputs object instance along"""
        self._event_type = {
            "concert": True,
            "sports": False,
            "comedy": False,
            "theatre": False,
        }
        self._location = {"lat": 40.650002, "lon": -73.949997}
        self._radius = 30  # radius in miles

    def get_user_event_type_preference(self):
        """Prompts user for event detail and updates object's event_type dict"""
        event_type = input(
            "What event type are you looking for? (Options: 'concert', 'sports', 'comedy',) : "
        )

        for event in self._event_type:
            if event == event_type:
                self._event_type[event_type] = True
            elif event != event_type:
                self._event_type[event] = False

    def get_user_location_preference(self):
        """Prompts user for location preference"""
        location_details = {
            "city": "Brooklyn",
            "state": "NY",
            "zipcode": 11232,
            "country": "USA",
        }

        print(
            "Where are you looking for events? I'll ask for each detail one at a time."
        )

        location_details["city"] = input("What city? : ")
        location_details["state"] = input("What state? (ex. NY, CA, TX, SC) : ")
        location_details["zipcode"] = int(input("What zipcode? : "))

        load_dotenv(find_dotenv())
        geocoding_api_key = os.getenv("geocoding_api_key")

        location_str = (
            f"{location_details['city']}%20{location_details['state']}"
            f"%20{location_details['zipcode']}%20{location_details['country']}&apiKey={geocoding_api_key}"
        )

        url = "https://api.geoapify.com/v1/geocode/search?text=" + location_str

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"

        try:
            response = requests.get(url, headers=headers, timeout=5)

            data = response.json()
            self._location["lat"] = data["features"][0]["geometry"]["coordinates"][1]
            self._location["lon"] = data["features"][0]["geometry"]["coordinates"][0]
        except Exception as new_error:
            print(
                "ErrorType : {}, Error : {}".format(type(new_error).__name__, new_error)
            )
            print("There was an error with the City, State, or zipcode you enetered.")

    def get_user_range_preference(self):
        """Prompts user for their range preference and stores to object"""
        self._radius = int(
            input(
                "How many miles should the search range be from your location? (Enter a positive integer): "
            )
        )

    def get_user_preferences(self):
        """Returns dict of user's preferences"""
        user_preferences = {}

        event_types = self._event_type
        event_type = ""

        for category in event_types:
            if event_types[category] == True:
                event_type = category

        user_preferences["event type"] = event_type
        user_preferences["location"] = self._location
        user_preferences["range"] = self._radius

        return user_preferences
