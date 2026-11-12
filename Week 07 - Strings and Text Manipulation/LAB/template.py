"""
RECORD CHECK - My Version
=========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 12 November 2026

Run it: python template.py
"""


def parse_line(raw_line):
    """Clean and parse one server record."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)

    hostname = hostname_part.strip()
    fields = {}

    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }


def status_of(used, total):
    """Return the server usage status."""
    percentage = (used / total) * 100

    if percentage >= 100:
        return "OVER LIMIT"
    elif percentage >= 90:
        return "WARNING"
    else:
        return "OK"


raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03 , used=45,total=100 ",
    "SRV-04, Used=90 , Total=100",
    "  SRV-05 , USED=25 , TOTAL=50  "
]

with open("server_records.txt", "w") as file:
    for record in raw_records:
        file.write(record + "\n")


total_records = 0
flagged_records = 0

with open("server_records.txt", "r") as file:
    for raw_record in file:
        record = parse_line(raw_record)
        status = status_of(record["used"], record["total"])

        print(record)
        print(record["hostname"], ":", status)

        total_records += 1

        if status != "OK":
            flagged_records += 1

print("\nSummary")
print("Total records:", total_records)
print("Flagged records:", flagged_records)