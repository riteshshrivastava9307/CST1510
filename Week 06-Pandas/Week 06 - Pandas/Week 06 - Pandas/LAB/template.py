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
import matplotlib.pyplot as plt

# ==================================================================== LOAD

df = pd.read_csv("Week 06-Pandas/Week 06 - Pandas/Week 06 - Pandas/LAB/servers.csv")


# ================================================================= PROCESS

df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT

print("Complete DataFrame:")
print(df)

print("\nServers that need attention:")
print(df[df["status"] != "OK"])

print("\nCount per status:")
print(df.groupby("status").size())

df.to_csv("servers_report.csv", index=False)

df["status"].value_counts().plot(kind="bar")

plt.title("Server Status Count")
plt.xlabel("Status")
plt.ylabel("Number of Servers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("server_status.png")
plt.show()
