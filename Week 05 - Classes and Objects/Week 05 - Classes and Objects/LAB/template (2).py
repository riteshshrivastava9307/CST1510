"""
RECORD CHECK - my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 18 October 2026

Run it: python template.py
"""


# ==================================================================== CLASS

class Record:
    """Represent a record with its label, value and limit."""

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit


# ==================================================================== OBJECTS

record1 = Record("srv-01", 87, 120)
record2 = Record("srv-02", 120, 100)
record3 = Record("srv-03", 45, 100)


# ==================================================================== OUTPUT

records = [record1, record2, record3]

for record in records:

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label : {record.label}")
    print(f"  Value : {record.value}")
    print(f"  Limit : {record.limit}")

    print("=" * 34)