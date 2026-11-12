"""
RECORD CHECK - my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 18 October 2026

Run it: python template.py
"""


class Record:
    """Represent a record with its label, value and limit."""

    def __init__(self, label, value, limit):
        """Store the label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage of the limit."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Load records from a file and return Record objects."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


try:
    records = load_records("records.txt")

except FileNotFoundError:
    print("Error: records.txt was not found.")
    records = []


over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label      : {record.label}")
    print(f"  Value      : {record.value}")
    print(f"  Limit      : {record.limit}")
    print(f"  Difference : {record.value - record.limit}")
    print(f"  Percentage : {(record.value / record.limit) * 100:.2f}%")
    print(f"  Status     : {record.status()}")

    print("=" * 34)

    if record.status() == "OVER LIMIT":
        over_limit_count += 1


if records:
    print()
    print(f"{over_limit_count} of {len(records)} were over limit")
