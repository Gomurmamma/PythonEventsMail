
class UserInputs:
    """Object used for collecting user inputs for API request"""
    
    def __init__(self):
        """Initializes UserInputs object instance along"""
        self._event_type: str = ''  # "concert", "" 
        self._location = {}  # { lat: float, lon: float}
        self._radius = 30    # radius in miles
        self._events_sorting = {"datetime_utc": True, "datetime_local": False, 
                                "announce_date": False, 
                                "id": False, 
                                "score": False, 
                                "direction": {"asc": True, 
                                              "desc": False}
                                } 
        self._performers_sorting = {"datetime_utc": True, "datetime_local": False, 
                                "announce_date": False, 
                                "id": False, 
                                "score": False, 
                                "direction": {"asc": True, 
                                              "desc": False}}
    
    