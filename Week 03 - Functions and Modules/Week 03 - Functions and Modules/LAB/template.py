"""
RECORD CHECK - Ritesh Shrivastava
Lane: IT
Date: 1 November 2026

Run it with: python template.py
"""

# ================================================================ FUNCTION

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ==================================================================== INPUT

label = input("Enter hostname: ")
value = float(input("Enter GB used: "))
limit = float(input("Enter total GB: "))


# ================================================================== PROCESS

difference = limit - value
percent = (value / limit) * 100

status = status_of(percent)


# =================================================================== OUTPUT

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
