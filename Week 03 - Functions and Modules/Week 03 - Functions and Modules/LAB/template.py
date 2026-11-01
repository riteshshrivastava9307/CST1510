"""
RECORD CHECK - Ritesh Shrivastava
Lane: IT
Date: 1 November 2026

Run it with: python template.py
This version checks multiple records until you type "quit".
"""

def status_of(percent):
    """Return a status based on the percentage of the limit used."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference from the limit and the percentage used."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>13}")
    print("=" * 34)


over_limit_count = 0

while True:
    label = input("Enter hostname (or 'quit' to stop): ").strip()
    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Records OVER LIMIT: {over_limit_count}")
