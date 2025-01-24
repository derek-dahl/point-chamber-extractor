# Point Chamber Extractor

This project extracts business data from the Point Chamber of Commerce website and converts it into a structured CSV file for easy readability and analysis.

## Features

- **Data Extraction**: Fetches structured JSON data directly from the endpoint.
- **Dynamic Parsing**: Converts JSON data to a clean CSV format with all available fields.
- **Flexible Configuration**: Automatically handles optional fields and dynamically generated data.

## Project Structure

## How It Works

1. **Data Extraction**:

   - The `extractor.py` script fetches business data from the API endpoint.
   - The data is saved as `business_data.json`.

2. **Data Parsing**:
   - The `parser.py` script processes `business_data.json` and converts it to `business_data.csv`.
   - All fields in the JSON are dynamically included in the CSV.

## How to Use

### Prerequisites

- Python 3.7 or later
- `requests` library (to install: `pip install requests`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/point-chamber-extractor.git
   cd point-chamber-extractor
   ```
