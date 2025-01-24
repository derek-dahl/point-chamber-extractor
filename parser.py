import json
import csv

def json_to_csv(input_file="business_data.json", output_file="business_data.csv"):
    """Convert JSON data to a CSV file."""
    # Load the JSON data
    with open(input_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Collect all unique fields dynamically
    fields = set()
    for entry in data.values():
        fields.update(entry.keys())

    # Sort fields for consistency
    fields = sorted(fields)

    # Write to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write header
        writer.writerow(fields)

        # Write rows
        for entry in data.values():
            writer.writerow([entry.get(field, "") for field in fields])

    print(f"CSV file successfully created: {output_file}")
