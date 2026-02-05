import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output_content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(output_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
