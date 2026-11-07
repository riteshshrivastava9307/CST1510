"""
RECORD CHECK - my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 7 November 2026

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean and parse one messy server record."""

    line = raw_line.strip().lower()
    parts = line.split(",")

    hostname = parts[0].strip()

    fields = {}

    for item in parts[1:]:
        key, value = item.strip().split("=", 1)
        fields[key.strip()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }


def status_of(record):
    """Determine server status using its usage percentage."""

    percent = (record["used"] / record["total"]) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    "  srv-03 , USED=45 , TOTAL=100 ",
    "Srv-04, used=95, total=100",
    "  SRV-05 , Used=101 , Total=100  "
]

with open("server_records.txt", "w") as file:
    for raw_record in raw_records:
        file.write(raw_record + "\n")


# =============================================================== PROCESS + OUTPUT

total_records = 0
flagged_records = 0

with open("server_records.txt", "r") as file:
    for raw_record in file:
        try:
            record = parse_line(raw_record)
            status = status_of(record)

            print(record, "|", status)

            total_records += 1

            if status != "OK":
                flagged_records += 1

        except (ValueError, KeyError, IndexError, ZeroDivisionError) as error:
            print("Error:", error)


print("\n--- FINAL SUMMARY ---")
print("Total records:", total_records)
print("Flagged records:", flagged_records)


# ========================================================================== 
# ERROR TEST

try:
    parse_line("SRV-06,used=unknown,total=100")
except ValueError as error:
    print("\nInvalid input test:", error)
