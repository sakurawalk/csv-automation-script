import csv
import os
import sys
from datetime import datetime

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"
REQUIRED_COLUMNS = {"id", "date", "amount"}


def normalize_date(date_str: str) -> str:
    """Try multiple date formats and normalize to YYYY-MM-DD."""
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""


def main():
    # --- Input file check ---
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found.")
        sys.exit(1)

    seen_rows = set()
    cleaned_rows = []

    try:
        with open(INPUT_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # --- Column check ---
            if not reader.fieldnames:
                print("Error: input.csv has no header row.")
                sys.exit(1)

            if not REQUIRED_COLUMNS.issubset(reader.fieldnames):
                print(
                    "Error: input.csv must contain columns: "
                    + ", ".join(sorted(REQUIRED_COLUMNS))
                )
                sys.exit(1)

            for row in reader:
                row_id = row.get("id", "").strip()
                amount = row.get("amount", "").strip()
                date_raw = row.get("date", "").strip()

                # Skip empty required fields
                if not row_id or not amount or not date_raw:
                    continue

                normalized_date = normalize_date(date_raw)
                if not normalized_date:
                    continue

                try:
                    amount_value = float(amount)
                except ValueError:
                    continue

                row_key = (row_id, normalized_date)
                if row_key in seen_rows:
                    continue

                seen_rows.add(row_key)
                cleaned_rows.append(
                    {
                        "id": row_id,
                        "date": normalized_date,
                        "amount": amount_value,
                    }
                )

    except Exception as e:
        print(f"Unexpected error while reading '{INPUT_FILE}': {e}")
        sys.exit(1)

    # --- Empty result check ---
    if not cleaned_rows:
        print("No valid rows after cleanup.")
        sys.exit(0)

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=["id", "date", "amount"]
            )
            writer.writeheader()
            writer.writerows(cleaned_rows)

    except Exception as e:
        print(f"Unexpected error while writing '{OUTPUT_FILE}': {e}")
        sys.exit(1)

    print(f"Processed {len(cleaned_rows)} rows successfully.")


if __name__ == "__main__":
    main()
