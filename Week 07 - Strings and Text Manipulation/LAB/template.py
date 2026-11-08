"""
RECORD CHECK - my version

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 8 November 2026
"""

# FUNCTIONS

def parse_line(raw_line):
    """Clean and parse one server record."""
    line = raw_line.strip().lower()
    hostname, rest = line.split(",", 1)

    data = {}

    for item in rest.split(","):
        key, value = item.split("=", 1)
        data[key.strip()] = float(value.strip())

    return {
        "hostname": hostname.strip(),
        "used": data["used"],
        "total": data["total"]
    }


def status_of(record):
    """Check server usage status."""
    percent = record["used"] / record["total"] * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# INPUT

raw_records = []

with open("messy_lines.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# PROCESS AND OUTPUT

total = 0
flagged = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)

        print(record, "|", status)

        total += 1

        if status != "OK":
            flagged += 1

    except (ValueError, KeyError, ZeroDivisionError) as error:
        print("Error:", error)


# FINAL SUMMARY

print("\nTotal records:", total)
print("Flagged records:", flagged)


# INVALID INPUT TEST

try:
    parse_line("SRV-06,used=unknown,total=100")
except ValueError as error:
    print("\nInvalid input:", error)