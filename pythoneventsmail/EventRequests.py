from dotenv import load_dotenv, find_dotenv
import os
import requests
from datetime import datetime

class EventsRequest:
    """Object used for making SeatGeek API requests and extracting relevant data for email"""
    def __init__(self, user_preferences):
        """Initializes a new EventsRequest object"""
        self._user_preferences = user_preferences
        self._events = []
        
    def get_events(self):
        """Sends Seat Geek API request and extracts data"""
        client_id = os.getenv('client_id')
        client_secret = os.getenv('client_secret')
        password = os.getenv('password')

        # SeatGeek Query
        # Per page: 10 (default)
        # page: 1 (default)
        event_type = self._user_preferences["event type"]
        coordinates = self._user_preferences["location"]
        radius = self._user_preferences["range"]

        lat = coordinates["lat"]
        lon = coordinates["lon"]
        
        print('query params', event_type, lat, lon, radius)

        try:
            response = requests.get(
                f'https://api.seatgeek.com/2/events?lat={lat}&lon={lon}&range={radius}mi&client_id={client_id}&type={event_type}&&client_secret={client_secret}')
            
            events = response.json()['events']

            # Extract relevant event data and append to list
            for event in events:
                title = event['title']
                ticket_url = event['url']
                date = event['datetime_local']

                date_time_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
                event_month = date_time_obj.strftime('%B')
                event_day = date_time_obj.day

                venue = event['venue']
                venue_name = venue['name_v2']
                city = venue['city']
                state = venue['state']

                performers = event['performers']
                performer = performers[0]
                image_url = performer['image']

                formatted_event = {'formatted_title': title, 'formatted_ticket_url': ticket_url, 'formatted_month': event_month,
                                'formatted_day': str(event_day), 'formatted_venue_name': venue_name, 'formatted_city': city,
                                'formatted_state': state, 'formatted_image_url': image_url,
                                }

                self._events.append(formatted_event)
        except Exception as e:
            print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
            print("There was an error with the request for the events you've specified.")
            
        
    def get_events_list(self):
        """Returns list of events from the most recent Seat Geek API request"""
        return self._events