# ============================================
# AIOps Log Anomaly Detection
# ============================================

import pandas as pd
import matplotlib.pyplot as plt


# STEP 1: Create Sample Dataset

data = {
    "Timestamp": [
        "10:01", "10:02", "10:03", "10:04", "10:05",
        "10:06", "10:07", "10:08", "10:09", "10:10",
        "10:11", "10:12", "10:13", "10:14", "10:15",
        "10:16", "10:17", "10:18", "10:19", "10:20"
    ],

    "CPU": [
        45, 50, 55, 60, 95,
        48, 52, 65, 58, 62,
        55, 97, 60, 50, 68,
        72, 65, 92, 55, 48
    ],

    "Memory": [
        55, 60, 58, 62, 80,
        57, 65, 63, 60, 61,
        59, 85, 64, 62, 68,
        70, 66, 78, 60, 58
    ],

    "Response_Time": [
        120, 130, 140, 150, 420,
        125, 135, 160, 145, 155,
        140, 450, 150, 130, 165,
        170, 160, 410, 135, 125
    ]
}


# STEP 2: Create DataFrame

df = pd.DataFrame(data)

print("===== AIOps Log Anomaly Detection =====")

print("\nTotal records:", len(df))


# STEP 3: Calculate Basic Statistics

print("\n===== Basic Statistics =====")

print(df[["CPU", "Memory", "Response_Time"]].describe())


# STEP 4: Detect Anomalies

CPU_THRESHOLD = 80

df["Status"] = df["CPU"].apply(
    lambda cpu: "ANOMALY" if cpu > CPU_THRESHOLD else "NORMAL"
)


# STEP 5: Filter Anomalous Records

anomalies = df[df["Status"] == "ANOMALY"]

print("\nAnomalies detected:", len(anomalies))


# STEP 6: Print Anomalous Records

print("\n===== Anomalous Records =====")

print(
    anomalies[["Timestamp", "CPU", "Status"]]
    .to_string(index=False)
)


# STEP 7: Visualize Metrics

fig, axes = plt.subplots(3, 1, figsize=(12, 12))


# CPU Usage Graph

axes[0].plot(
    df["Timestamp"],
    df["CPU"],
    marker="o",
    label="CPU Usage"
)

axes[0].scatter(
    anomalies["Timestamp"],
    anomalies["CPU"],
    marker="x",
    s=120,
    label="Anomalies"
)

axes[0].axhline(
    y=CPU_THRESHOLD,
    linestyle="--",
    label="Threshold = 80%"
)

axes[0].set_title("CPU Usage and Anomalies")
axes[0].set_ylabel("CPU (%)")
axes[0].legend()


# Memory Usage Graph

axes[1].plot(
    df["Timestamp"],
    df["Memory"],
    marker="o"
)

axes[1].set_title("Memory Usage")
axes[1].set_ylabel("Memory (%)")


# Response Time Graph

axes[2].plot(
    df["Timestamp"],
    df["Response_Time"],
    marker="o"
)

axes[2].set_title("Response Time")
axes[2].set_ylabel("Response Time (ms)")
axes[2].set_xlabel("Timestamp")


# Format and Save Graph

for ax in axes:
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True)

plt.tight_layout()

plt.savefig("anomaly_graph.png")

plt.show()

print("\nGraph saved as anomaly_graph.png")