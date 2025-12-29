CSV Automation Script

A small Python script that automates repetitive CSV cleanup tasks.

This tool is designed for operations and internal data workflows where CSV files often contain duplicates, inconsistent date formats, or invalid rows.

---

Features

- Removes empty rows
- Removes duplicate records by (id, date)
- Normalizes date formats to YYYY-MM-DD
- Converts numeric fields (amount) to numbers
- Handles invalid rows safely without crashing

---

Requirements

- Python 3.10 or newer
- No external dependencies

---

Usage

Run the script from the project directory.

python main.py

---

How to try with sample data

1. Download the sample input file
   sample_input.csv

2. Copy it as input.csv in the project directory (Windows)

copy sample_input.csv input.csv

3. Run the script

python main.py

4. The script will generate

output.csv

5. The expected result format can be checked in

sample_output.csv

---

Input / Output

Input

File name: input.csv

Required columns:
- id
- date
- amount

Rows with missing or invalid required fields are skipped.

Output

File name: output.csv

Cleaned and normalized CSV file.

---

Use case

- Automating manual CSV processing for operations teams
- Cleaning exported data from internal tools
- Reducing repetitive spreadsheet work

---

Notes

- Rows with invalid dates or numeric values are ignored
- If no valid rows remain, the script exits gracefully with a message
