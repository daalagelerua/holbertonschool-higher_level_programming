#!/usr/bin/python3


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string")
        return

    if not isinstance (attendees, list):
        print("Attendees must be a list")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return
        
    # Processing attendees
    for i, attendee in enumerate(attendees, start=1):
        # Replacement of missing values by "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Creation of template message
        invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        # Generate output file
        output_filename = f"output_{i}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
            print(f"Generated file : {output_filename}")
        except Exception as e:
            print(f"Error in {output_filename} : {e}")
