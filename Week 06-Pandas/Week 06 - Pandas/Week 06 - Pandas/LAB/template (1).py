"""
RECORD CHECK - my version
===========================

Name  : Ritesh Shrivastava
Lane  : IT
Date  : 7 November 2026

Run it: python template.py

Work through the numbered sections in order.
"""

import pandas as pd


# Read CSV file
df = pd.read_csv("servers.csv")


# Calculate percentage
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100


# Print DataFrame
print("Complete DataFrame:")
print(df)