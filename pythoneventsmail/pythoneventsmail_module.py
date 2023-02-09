import os
from dotenv import load_dotenv, find_dotenv
import requests
from requests.structures import CaseInsensitiveDict

class UserInputs:
    """Object used for collecting user event preferences"""
    
    def __init__(self):
        """Initializes UserInputs object instance along"""
        self._event_type = { "concert": True,
                             "sports": False,
                             "comedy": False,
                             "theatre": False } 
        self._location = { "lat": 40.650002, 
                           "lon": -73.949997 }  
        self._radius = 30                       # radius in miles
        self._events_sorting = { "datetime_utc": True, 
                                "datetime_local": False, 
                                "announce_date": False, 
                                "id": False, 
                                "score": False, 
                                "direction": {"asc": True, 
                                              "desc": False} } 
        self._performers_sorting = { "datetime_utc": True, 
                                     "datetime_local": False, 
                                     "announce_date": False, 
                                     "id": False, 
                                     "score": False, 
                                     "direction": {"asc": True, 
                                                  "desc": False} }
    
    def get_user_event_type_preference(self):
        """Prompts user for event detail and updates object's event_type dict"""
        event_type = input("What event type are you looking for? ['concert', 'sports', comedy', or 'theatre]")
        
        for event in self._event_type:
            if event == event_type:
                self._event_type[event_type] = True
            elif event != event_type:
                self._event_type[event] = False
    
    def get_user_location_preference(self):
        """Prompts user for location preference"""
        location_details = { "city": "Brooklyn",
                             "state": "NY",
                              "zipcode": 11232,
                              "country": "USA" }
        
        print("Where should the event be?")
        
        location_details['city'] = input("What city?")
        location_details['state'] = input("What state? (ex. NY, CA, TX, SC)")
        location_details['zipcode'] = int(input("What zipcode?"))
        
        load_dotenv(find_dotenv())
        geocoding_api_key = os.getenv("geocoding_api_key")
        
        location_str = f"{location_details['city']}%20{location_details['state']}%20{location_details['zipcode']}%20{location_details['country']}&apiKey={geocoding_api_key}"

        url = "https://api.geoapify.com/v1/geocode/search?text=" + location_str
        

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        
        try:
            response = requests.get(url, headers=headers)
        
            data = response.json()
            self._location["lat"] = data["features"][0]["geometry"]["coordinates"][1]
            self._location["lon"] = data["features"][0]["geometry"]["coordinates"][0]
        except HTTPError:
            print("There was an error with the City, State, or zipcode you enetered.")
            response = input("Would you like to try again? (y/n): ")
            if response == 'y' or 'Y':
                get_user_location_preference(self)
    
    
    def get_user_radius_preference():
        """Prompts user for their radius preference in miles."""
        self._radius = int(input("Within what radius? (in miles): "))


    def get_user_events_sorting_preference():
        """Prompts user for their preference on how the events should be sorted"""
        response = input("What field should the events be sorted by? (datetime_utc, datetime_local, announce_date, id, score): ")
        
        for field in self._events_sorting:
            if response == field:
                self._events_sorting[field] = True
            elif response != field:
                self._events_sorting[field] = False
        
        response = input("In ascending or descending order?")
        
        if response == "ascending":
            self._events_sorting["direction"]["ascending"] = True
            self._events_sorting["direction"]["descending"] = False
            
    def get_user_performers_sorting_preference():
        """Prompts user for their preference on how the events should be sorted"""
        response = input("What field should the performers be sorted by? (datetime_utc, datetime_local, announce_date, id, score): ")
        
        for field in self._events_sorting:
            if response == field:
                self._events_sorting[field] = True
            elif response != field:
                self._events_sorting[field] = False
        
        response = input("In ascending or descending order?")
        
        if response == "ascending":
            self._events_sorting["direction"]["ascending"] = True
            self._events_sorting["direction"]["descending"] = False
    
    
    def get_user_preferences(self):
        """Returns dict of user's preferences"""
        user_preferences = {}
        
        user_preferences["event type"] = self._event_type
        user_preferences["location"] = self._location
        user_preferences["radius"] = self._radius
        user_preferences["events_sorting"] = self._events_sorting
        user_preferences["performers_sorting"] = self._performers_sorting
        
        return user_preferences

        