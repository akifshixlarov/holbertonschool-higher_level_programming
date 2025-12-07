#!/usr/bin/python3
"""Sending invitations module"""

import os


def generate_invitations(template, attendees):
    """Function that generates invitations"""

    if not template:
        print("Template must be filled")
        return

    if not isinstance(template, str):
        print(f"Template must be a string, not {type(template).__name__}")
        return

    if not attendees:
        print("You must fill attendees with a list of dictionaries")
        return

    if not isinstance(attendees, list):
        print(f"Attendees must be a list, not {type(attendees).__name__}")
        return

    invalid_items = [item for item in attendees if not isinstance(item, dict)]
    if invalid_items:
        print("Item in attendees must be a dictionary")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if not value:
                value = "N/A"
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, str(value))

        filename = f"output_{index}.txt"
        if os.path.exists(filename):
            print(f"{filename} already exists")
            continue

        with open(filename, "w") as file:
            file.write(invitation)
