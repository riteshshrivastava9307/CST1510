"""
RECORD CHECK - My Version
=========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 12 November 2026

Run it: python template.py
"""

# ==================================================================== FUNCTION

def parse_line(raw_line):
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


# ======================================================================== DATA

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03 , used=45,total=100 ",
    "SRV-04, Used=90 , Total=100",
    "  SRV-05 , USED=25 , TOTAL=50  "
]


# ====================================================================== OUTPUT

for raw_record in raw_records:
    record = parse_line(raw_record)
    print(record)