"""
RECORD CHECK
============

Name  : Ritesh Shrivastava
Lane  : Cyber
Date  : 18 October 2026
"""


# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print(f"Label: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Status: {status}")
    print("------------------------")


# ====================================================================== STORE

def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


try:
    records = load_records("records.txt")

except FileNotFoundError:
    print("Error: records.txt was not found.")
    records = []


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

for record in records:
    difference, percent, status = check_record(
        record["value"],
        record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

    if status == "OVER LIMIT":
        over_limit_count += 1


if records:
    print(f"{over_limit_count} of {len(records)} were over limit")