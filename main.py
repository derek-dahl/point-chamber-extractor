from extractor import fetch_data
from parser import json_to_csv

# URL for the JSON data
DATA_URL = "https://pr.chambernation.workers.dev/?https://www.chamberorganizer.com/members/mem_xml/LEHI_members.json?v=_kzi1fhvpd"

if __name__ == "__main__":
    # Step 1 Fetch the data
    try:
        fetch_data(DATA_URL)
    except Exception as e:
        print(f"Error: {e}")

    # Step 2: Convert the data into a CSV
    try:
        json_to_csv()
    except Exception as e:
        print(f"Error converting data to CSV: {e}")
        exit(1)
