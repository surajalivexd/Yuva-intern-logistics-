import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ---------------------------------------------------------
# 1. Setup
# ---------------------------------------------------------

np.random.seed(42)

OUTPUT_DIR = Path("visualizations")
OUTPUT_DIR.mkdir(exist_ok=True)

DATA_FILE = Path("data/logistics_data.csv")


# ---------------------------------------------------------
# 2. Create a hypothetical logistics dataset
# ---------------------------------------------------------

n = 1000

regions = ["North", "South", "East", "West", "Central"]
vehicle_types = ["Truck", "Van", "Mini Truck", "Container"]

data = pd.DataFrame({
    "Shipment_ID": range(1, n + 1),
    "Region": np.random.choice(regions, n),
    "Vehicle_Type": np.random.choice(vehicle_types, n),
    "Distance_km": np.random.randint(20, 1200, n),
    "Shipment_Volume_kg": np.random.randint(50, 5000, n),
    "Fuel_Cost": np.random.uniform(500, 15000, n),
    "Delivery_Time_days": np.random.uniform(1, 12, n)
})

# Add realistic relationships between variables

data["Transportation_Cost"] = (
    1200
    + (data["Distance_km"] * 8)
    + (data["Shipment_Volume_kg"] * 1.5)
    + data["Fuel_Cost"] * 0.35
    + np.random.normal(0, 1500, n)
)

data["Transportation_Cost"] = data["Transportation_Cost"].clip(lower=500)

# Make delivery time somewhat dependent on distance
data["Delivery_Time_days"] = (
    1.5
    + data["Distance_km"] / 180
    + np.random.normal(0, 1, n)
)

data["Delivery_Time_days"] = data["Delivery_Time_days"].clip(lower=1)

# Add dates for monthly analysis
data["Shipment_Date"] = pd.date_range(
    start="2025-01-01",
    periods=n,
    freq="D"
)

data["Delay_Status"] = np.where(
    data["Delivery_Time_days"] > 7,
    "Delayed",
    "On Time"
)

# Round numerical values
data["Distance_km"] = data["Distance_km"].round(2)
data["Shipment_Volume_kg"] = data["Shipment_Volume_kg"].round(2)
data["Fuel_Cost"] = data["Fuel_Cost"].round(2)
data["Transportation_Cost"] = data["Transportation_Cost"].round(2)
data["Delivery_Time_days"] = data["Delivery_Time_days"].round(2)

# Save dataset
DATA_FILE.parent.mkdir(exist_ok=True)
data.to_csv(DATA_FILE, index=False)

print("Dataset created successfully.")
print(f"Rows: {data.shape[0]}")
print(f"Columns: {data.shape[1]}")


# ---------------------------------------------------------
# 3. Basic EDA
# ---------------------------------------------------------

print("\n========== DATASET INFORMATION ==========")
print(data.info())

print("\n========== FIRST 5 ROWS ==========")
print(data.head())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(data.describe())

print("\n========== MISSING VALUES ==========")
print(data.isnull().sum())

print("\n========== DUPLICATES ==========")
print(data.duplicated().sum())


# ---------------------------------------------------------
# 4. Central tendency
# ---------------------------------------------------------

print("\n========== CENTRAL TENDENCY ==========")

metrics = [
    "Distance_km",
    "Shipment_Volume_kg",
    "Fuel_Cost",
    "Delivery_Time_days",
    "Transportation_Cost"
]

for column in metrics:
    print(f"\n{column}")
    print("Mean:", round(data[column].mean(), 2))
    print("Median:", round(data[column].median(), 2))
    print("Std Dev:", round(data[column].std(), 2))


# ---------------------------------------------------------
# 5. Correlation analysis
# ---------------------------------------------------------

numeric_columns = [
    "Distance_km",
    "Shipment_Volume_kg",
    "Fuel_Cost",
    "Delivery_Time_days",
    "Transportation_Cost"
]

correlation_matrix = data[numeric_columns].corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation_matrix.round(2))


# ---------------------------------------------------------
# 6. Visualization 1
# Delivery Time Distribution
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    data["Delivery_Time_days"],
    bins=25,
    kde=True
)

plt.title("Distribution of Delivery Times")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Number of Shipments")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "delivery_time_distribution.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 7. Visualization 2
# Shipment Volume by Region
# ---------------------------------------------------------

region_volume = (
    data.groupby("Region")["Shipment_Volume_kg"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

region_volume.plot(kind="bar")

plt.title("Total Shipment Volume by Region")
plt.xlabel("Region")
plt.ylabel("Total Shipment Volume (kg)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "shipment_volume_by_region.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 8. Visualization 3
# Transportation Cost vs Distance
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=data,
    x="Distance_km",
    y="Transportation_Cost",
    alpha=0.6
)

sns.regplot(
    data=data,
    x="Distance_km",
    y="Transportation_Cost",
    scatter=False
)

plt.title("Transportation Cost vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Transportation Cost")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "transportation_cost_vs_distance.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 9. Visualization 4
# Delivery Time vs Distance
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=data,
    x="Distance_km",
    y="Delivery_Time_days",
    alpha=0.6
)

sns.regplot(
    data=data,
    x="Distance_km",
    y="Delivery_Time_days",
    scatter=False
)

plt.title("Delivery Time vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Delivery Time (Days)")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "delivery_time_vs_distance.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 10. Visualization 5
# Transportation Cost by Vehicle Type
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=data,
    x="Vehicle_Type",
    y="Transportation_Cost"
)

plt.title("Transportation Cost by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("Transportation Cost")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "cost_by_vehicle_type.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 11. Visualization 6
# Monthly Shipment Volume
# ---------------------------------------------------------

data["Month"] = data["Shipment_Date"].dt.to_period("M").astype(str)

monthly_volume = (
    data.groupby("Month")["Shipment_Volume_kg"]
    .sum()
)

plt.figure(figsize=(12, 6))

monthly_volume.plot(
    marker="o"
)

plt.title("Monthly Shipment Volume Trend")
plt.xlabel("Month")
plt.ylabel("Shipment Volume (kg)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_shipment_volume.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 12. Visualization 7
# Correlation Heatmap
# ---------------------------------------------------------

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Between Logistics Variables")
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "correlation_heatmap.png",
    dpi=300
)

plt.close()


# ---------------------------------------------------------
# 13. Additional Logistics KPIs
# ---------------------------------------------------------

total_shipments = len(data)

average_delivery_time = data["Delivery_Time_days"].mean()

average_transport_cost = data["Transportation_Cost"].mean()

delayed_shipments = (
    data["Delay_Status"] == "Delayed"
).sum()

delay_rate = (
    delayed_shipments / total_shipments
) * 100

total_volume = data["Shipment_Volume_kg"].sum()

print("\n========== LOGISTICS KPIs ==========")

print(
    "Total Shipments:",
    total_shipments
)

print(
    "Total Shipment Volume (kg):",
    round(total_volume, 2)
)

print(
    "Average Delivery Time (days):",
    round(average_delivery_time, 2)
)

print(
    "Average Transportation Cost:",
    round(average_transport_cost, 2)
)

print(
    "Delayed Shipment Rate:",
    round(delay_rate, 2),
    "%"
)


# ---------------------------------------------------------
# 14. Automatic analytical summary
# ---------------------------------------------------------

highest_volume_region = region_volume.idxmax()

cost_distance_corr = correlation_matrix.loc[
    "Distance_km",
    "Transportation_Cost"
]

distance_delivery_corr = correlation_matrix.loc[
    "Distance_km",
    "Delivery_Time_days"
]

print("\n========== KEY INSIGHTS ==========")

print(
    f"1. The {highest_volume_region} region has "
    f"the highest total shipment volume."
)

print(
    f"2. Distance and transportation cost have a "
    f"correlation of {cost_distance_corr:.2f}."
)

print(
    f"3. Distance and delivery time have a "
    f"correlation of {distance_delivery_corr:.2f}."
)

print(
    "4. Shipments with delivery times above "
    "7 days are classified as delayed."
)

print("\nAll visualizations have been saved successfully.")