# Point Chamber Extractor

This project extracts business data from the Point Chamber of Commerce website and converts it into a structured CSV file for easy readability and analysis.

## Features

- **Data Extraction**: Fetches structured JSON data directly from the endpoint.
- **Dynamic Parsing**: Converts JSON data to a clean CSV format with all available fields.
- **Flexible Configuration**: Automatically handles optional fields and dynamically generated data.

## Project Structure

```
point_chamber_extractor/
├── extractor.py       # Extracts data from the endpoint and saves as JSON
├── parser.py          # Converts JSON data to CSV
├── main.py            # Orchestrates extraction and parsing
├── .gitignore         # Excludes unnecessary files from version control
├── business_data.json # Generated JSON data (ignored in Git)
├── business_data.csv  # Generated CSV file (ignored in Git)
├── install.sh         # One-line script to set up and run the project
```

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

### Installation

#### **Option 1: One-Liner Installation (Recommended)**
For the easiest setup, run this command to automatically install dependencies and extract data:
```bash
curl -sSL https://raw.githubusercontent.com/derek-dahl/point-chamber-extractor/master/install.sh | bash
```

#### **Option 2: Manual Setup**
```bash
# Clone the repository
git clone https://github.com/your-username/point-chamber-extractor.git
cd point-chamber-extractor

# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the extractor
python3 main.py
```

## Example Output

### JSON Example
```json
{
  "12345678901": {
    "business_name": "Acme Solutions",
    "first_name": "John",
    "last_name": "Doe",
    "address_1": "1234 Innovation Drive",
    "city": "Techville",
    "state_province": "CA",
    "zip_postal": "90210",
    "email": "contact@acmesolutions.com",
    "member_type": "Gold"
  }
}
```

### CSV Example
```csv
Business Name,First Name,Last Name,Address 1,City,State,ZIP,Email,Member Type
Acme Solutions,John,Doe,1234 Innovation Drive,Techville,CA,90210,contact@acmesolutions.com,Gold
Beta Corp,Jane,Smith,5678 Market St,Biztown,NY,10001,info@betacorp.com,Silver
```

## Configuration

### `.gitignore`
```text
business_data.json  # Generated JSON data
business_data.csv   # Generated CSV file
__pycache__/        # Python cache files
```

### Change the Endpoint
To use a different data source, update the `DATA_URL` variable in `main.py`:
```python
DATA_URL = "https://new-api-endpoint.example.com"
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributions

Feel free to fork this repository, submit pull requests, or raise issues for improvements. 🎉

