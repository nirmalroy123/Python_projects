import pywhatkit
import time

birthdays = [
    {
        "name": "Rahul",
        "phone": "+911234567890",
        "message": "Happy Birthday Rahul! "
    },

    {
        "name": "Arun",
        "phone": "+919876543210",
        "message": "Happy Birthday Arun! "
    }
]

hour = 11
minute = 0

for person in birthdays:

    pywhatkit.sendwhatmsg(
        person["phone"],
        person["message"],
        hour,
        minute
    )

    print(f"Scheduled message for {person['name']}")

    minute += 2

    time.sleep(5)