"""
Defines EventsEmail object for sending events data with the given HTML template
"""
import os
import smtplib
import time
from email.message import EmailMessage
from email.mime.text import MIMEText
from template import HtmlTemplate
from jinja2 import Environment
from dotenv import load_dotenv, find_dotenv


class EventEmail:
    """Represents object user can use to send email with event info"""

    def __init__(self, events_list):
        """Initializes a new EventEmail object"""
        self._events = events_list

    def send_email(self):
        """Sends email with events"""

        load_dotenv(find_dotenv())

        # Create message base & fields for email
        msg = EmailMessage()
        msg["Subject"] = "Tonight's Featured Events in Your Area!"
        msg["From"] = os.getenv("sender_email")
        msg["To"] = os.getenv("receiver_email")

        # environment variables
        sender_email = os.getenv("sender_email")
        receiver_email = os.getenv("receiver_email")
        password = os.getenv("password")

        # EVENTS LIST
        events_list = self._events

        html_template = HtmlTemplate()

        print("EVENTS LIST: ", events_list)

        # Create html message from the template and then the values from each event
        events_html = MIMEText(
            Environment()
            .from_string(html_template.TEMPLATE)
            .render(
                title0=events_list[0]["formatted_title"],
                ticket_url0=events_list[0]["formatted_ticket_url"],
                month0=events_list[0]["formatted_month"],
                day0=events_list[0]["formatted_day"],
                venue0=events_list[0]["formatted_venue_name"],
                city0=events_list[0]["formatted_city"],
                state0=events_list[0]["formatted_state"],
                image_url0=events_list[0]["formatted_image_url"],
                title1=events_list[1]["formatted_title"],
                ticket_url1=events_list[1]["formatted_ticket_url"],
                month1=events_list[1]["formatted_month"],
                day1=events_list[1]["formatted_day"],
                venue1=events_list[1]["formatted_venue_name"],
                city1=events_list[1]["formatted_city"],
                state1=events_list[1]["formatted_state"],
                image_url1=events_list[1]["formatted_image_url"],
                title2=events_list[2]["formatted_title"],
                ticket_url2=events_list[2]["formatted_ticket_url"],
                month2=events_list[2]["formatted_month"],
                day2=events_list[2]["formatted_day"],
                venue2=events_list[2]["formatted_venue_name"],
                city2=events_list[2]["formatted_city"],
                state2=events_list[2]["formatted_state"],
                image_url2=events_list[2]["formatted_image_url"],
                title3=events_list[3]["formatted_title"],
                ticket_url3=events_list[3]["formatted_ticket_url"],
                month3=events_list[3]["formatted_month"],
                day3=events_list[3]["formatted_day"],
                venue3=events_list[3]["formatted_venue_name"],
                city3=events_list[3]["formatted_city"],
                state3=events_list[3]["formatted_state"],
                image_url3=events_list[3]["formatted_image_url"],
                title4=events_list[4]["formatted_title"],
                ticket_url4=events_list[4]["formatted_ticket_url"],
                month4=events_list[4]["formatted_month"],
                day4=events_list[4]["formatted_day"],
                venue4=events_list[4]["formatted_venue_name"],
                city4=events_list[4]["formatted_city"],
                state4=events_list[4]["formatted_state"],
                image_url4=events_list[4]["formatted_image_url"],
                title5=events_list[5]["formatted_title"],
                ticket_url5=events_list[5]["formatted_ticket_url"],
                month5=events_list[5]["formatted_month"],
                day5=events_list[5]["formatted_day"],
                venue5=events_list[5]["formatted_venue_name"],
                city5=events_list[5]["formatted_city"],
                state5=events_list[5]["formatted_state"],
                image_url5=events_list[5]["formatted_image_url"],
                title6=events_list[6]["formatted_title"],
                ticket_url6=events_list[6]["formatted_ticket_url"],
                month6=events_list[6]["formatted_month"],
                day6=events_list[6]["formatted_day"],
                venue6=events_list[6]["formatted_venue_name"],
                city6=events_list[6]["formatted_city"],
                state6=events_list[6]["formatted_state"],
                image_url6=events_list[6]["formatted_image_url"],
                title7=events_list[7]["formatted_title"],
                ticket_url7=events_list[7]["formatted_ticket_url"],
                month7=events_list[7]["formatted_month"],
                day7=events_list[7]["formatted_day"],
                venue7=events_list[7]["formatted_venue_name"],
                city7=events_list[7]["formatted_city"],
                state7=events_list[7]["formatted_state"],
                image_url7=events_list[7]["formatted_image_url"],
                title8=events_list[8]["formatted_title"],
                ticket_url8=events_list[8]["formatted_ticket_url"],
                month8=events_list[8]["formatted_month"],
                day8=events_list[8]["formatted_day"],
                venue8=events_list[8]["formatted_venue_name"],
                city8=events_list[8]["formatted_city"],
                state8=events_list[8]["formatted_state"],
                image_url8=events_list[8]["formatted_image_url"],
                title9=events_list[9]["formatted_title"],
                ticket_url9=events_list[9]["formatted_ticket_url"],
                month9=events_list[9]["formatted_month"],
                day9=events_list[9]["formatted_day"],
                venue9=events_list[9]["formatted_venue_name"],
                city9=events_list[9]["formatted_city"],
                state9=events_list[9]["formatted_state"],
                image_url9=events_list[9]["formatted_image_url"],
            ),
            "html",
        )

        msg.set_content(events_html, subtype="html")

        # Create secure SMTP connection
        start = time.time()
        try:
            smtp_ssl = smtplib.SMTP_SSL(host="smtp.gmail.com")
        except Exception as new_error:
            print(
                "ErrorType : {}, Error : {}".format(type(new_error).__name__, new_error)
            )
            smtp_ssl = None

        print("Connection Object : {}".format(smtp_ssl))
        print("Total Time Taken  : {:,.2f} Seconds".format(time.time() - start))

        # Log in to email account
        print("\nLogging In.....")
        resp_code, response = smtp_ssl.login(sender_email, password)

        print("Response Code : {}".format(resp_code))
        print("Response      : {}".format(response.decode()))

        # Send email
        print("\nSending Mail..........")

        msg.set_content(events_html, subtype="html")

        response = smtp_ssl.sendmail(sender_email, receiver_email, msg.as_string())

        print("List of Failed Recipients : {}".format(response))

        # Log out
        print("\nLogging Out....")
        resp_code, response = smtp_ssl.quit()

        print("Response Code : {}".format(resp_code))
        print("Response      : {}".format(response.decode()))
