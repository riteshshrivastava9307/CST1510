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

if first > second:
    status = "OVER LIMIT"
else:
    status = "OK"


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Used        : {first:>10.2f} GB")
print(f"  Total       : {second:>10.2f} GB")
print(f"  Status      : {status}")

print("=" * 34)