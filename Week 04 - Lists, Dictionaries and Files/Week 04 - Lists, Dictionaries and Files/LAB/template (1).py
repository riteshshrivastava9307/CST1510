"""
RECORD CHECK
============

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 18 October 2026
"""


# ================================================================= FUNCTIONS

def check_record(value, limit):
    """Calculate the difference, percentage and status of a record."""

    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)

    print(f"  Used       : {value:.2f}")
    print(f"  Total      : {limit:.2f}")
    print(f"  Difference : {difference:.2f}")
    print(f"  Percentage : {percent:.2f}%")
    print(f"  Status     : {status}")

    print("=" * 34)


# ==================================================================== RECORDS

records = [
    {"label": "srv-01", "value": 87, "limit": 120},
    {"label": "srv-02", "value": 120, "limit": 100},
    {"label": "srv-03", "value": 45, "limit": 100}
]


# ================================================================== PROCESS

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
        over_limit_count = over_limit_count + 1


# ================================================================= SUMMARY

print()
print(f"{over_limit_count} of {len(records)} were over limit")