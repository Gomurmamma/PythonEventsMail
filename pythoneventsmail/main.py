"""
Defines the Python Events Mail cli
"""
from event_email import EventEmail
from events_request import EventsRequest
from user_inputs import UserInputs

def main():
    """Calls the CLI sequence for sending an email of events of specified preference"""
    user_inputs = UserInputs()

    user_inputs.get_user_event_type_preference()
    user_inputs.get_user_location_preference()
    user_inputs.get_user_range_preference()

    user_preferences = user_inputs.get_user_preferences()

    events_request = EventsRequest(user_preferences)

    events_request.get_events()

    events_list = events_request.get_events_list()

    email_message = EventEmail(events_list)

    email_message.send_email()

if __name__ == "__main__":
    main()
    