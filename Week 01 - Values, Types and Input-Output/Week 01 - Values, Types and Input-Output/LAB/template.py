"""
RECORD CHECK - my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 03/10/2026

Run it: python template.py
"""

# ==================================================================== INPUT

label = input("Hostname: ")
first = float(input("Disk space used (GB): "))
second = float(input("Total disk space (GB): "))


# ================================================================== PROCESS

difference = first - second

if second != 0:
    percent = (first / second) * 100
else:
    percent = 0


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Used        : {first:>10.2f} GB")
print(f"  Total       : {second:>10.2f} GB")
print(f"  Difference  : {difference:>+10.2f} GB")

if second != 0:
    print(f"  Percent     : {percent:>9.2f} %")
else:
    print("  Percent     : Cannot calculate (total is zero)")

print(f"  Free        : {second - first:>10.2f} GB")

print("=" * 34)
