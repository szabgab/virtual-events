from meetup_notifier import get_events
from meetup_notifier.meetup import MeetupEvent
from datetime import datetime, timedelta


groups = [
    ("code-mavens", "",       "English",    "Code Mavens 🦀 - 🐍 - 🐪"),
    ("pyweb-il",    "Python", "Hebrew",     "PyWeb-IL 🐍"),
    ("rust-tlv",    "Rust",   "Hebrew",     "Rust-TLV  🦀"),
    ]
print(groups)
exit()

for group in groups:
    events_url = f"https://www.meetup.com/{group}/"
    events = get_events(events_url)
    for event in events:
        #print(dir(event))
        #print()
        if event.location != "Online event":
            continue

        print(f"title: {event.name}")
        print(f"url: {event.link}")
        print(f"name: {group}") ## Should be the public name of the group
        print(f"address: https://www.meetup.com/{group}/")
        print(f"language: ?")
        print(f"category: ?")
        print(f"start: {event.date}")
        #print(event.description)
        #print(event.location_link)
        #print(event.venue)
        print()

