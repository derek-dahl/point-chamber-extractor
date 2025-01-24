import requests
import json

def fetch_data(url, output_file="business_data.json"):
    """Fetch data from the given URL and save it as a JSON file."""
    # Send a GET request to fetch the JSON data
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Save the data to a file
        with open(output_file, "w") as json_file:
            json.dump(data, json_file, indent=2)

        print(f"Extracted {len(data)} businesses.")
        return data
    else:
        raise Exception(f"Failed to fetch the data. Status code: {response.status_code}")
