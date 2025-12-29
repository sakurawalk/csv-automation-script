import csv
from datetime import datetime

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"

def normalize_date(date_str):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return ""

seen_rows = set()
cleaned_rows = []

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row["id"] or not row["amount"]:
            continue

        row_key = (row["id"], row["date"])
        if row_key in seen_rows:
            continue

        seen_rows.add(row_key)
        row["date"] = normalize_date(row["date"])
        row["amount"] = float(row["amount"])

        cleaned_rows.append(row)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned_rows[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_rows)

print(f"Processed {len(cleaned_rows)} rows.")
