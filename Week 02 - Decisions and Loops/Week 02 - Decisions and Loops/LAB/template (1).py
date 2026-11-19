"""
RECORD CHECK  -  my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 01/11/2026

Run it:   python template.py
"""


label = input("Enter hostname: ")
value = float(input("Enter GB used: "))
limit = float(input("Enter total GB: "))


if value > limit:
    status = "OVER LIMIT"
else:
    status = "OK"


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Used   : {value:>10.2f} GB")
print(f"  Total  : {limit:>10.2f} GB")
print(f"  Status : {status}")

print("=" * 34)