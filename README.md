# Yuva-intern-logistics-
📌 Project Overview

This project is part of my Week 3 Logistics Data Analyst Internship task at YuvaIntern.

The main objective of this project is to explore logistics data using Python, Pandas, Matplotlib, and Seaborn and understand how data visualization can help identify patterns related to delivery time, transportation costs, shipment volume, and logistics performance.

The dataset used in this project is a hypothetical logistics dataset created using Python for analysis and visualization practice.

🎯 Objectives
Explore and understand the logistics dataset.
Calculate basic descriptive statistics.
Analyze relationships between important logistics variables.
Study delivery-time patterns.
Compare transportation costs across vehicle types.
Compare shipment volume across regions.
Analyze monthly shipment-volume trends.
Identify important correlations between logistics variables.
Generate useful insights and recommendations.
📊 Dataset

The dataset contains 1,000 shipment records with information including:

Column	Description
Shipment_ID	Unique shipment number
Region	Shipment region
Vehicle_Type	Type of vehicle used
Distance_km	Shipment distance in kilometres
Shipment_Volume_kg	Shipment volume in kg
Fuel_Cost	Fuel-related cost
Delivery_Time_days	Delivery time in days
Transportation_Cost	Transportation cost
Shipment_Date	Shipment date
Delay_Status	Whether the shipment was delayed
🔧 Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
📈 Visualizations

The project generates the following visualizations:

Distribution of Delivery Times
Delivery Time vs Distance
Transportation Cost by Vehicle Type
Total Shipment Volume by Region
Monthly Shipment Volume Trend
Correlation Heatmap

These charts are used to make the relationships and trends in the data easier to understand.

🔍 Key Findings

Some of the main observations from the analysis are:

Distance has a strong positive relationship with delivery time.
Longer-distance shipments generally require more delivery time.
Distance also has a noticeable relationship with transportation cost.
Central and North have higher total shipment volumes compared with some other regions.
Shipment volume changes considerably from month to month.
Transportation costs vary across different vehicle types, but vehicle type alone does not explain all cost differences.
Shipments taking more than 7 days were classified as delayed for the analysis.

▶️ How to Run

Clone or download the repository and install the required libraries:

pip install -r requirements.txt

Then run:

python logistics_analysis.py

The script will generate the dataset and save the visualization files in the visualizations folder.

💡 Recommendations

Based on the analysis, the following actions could be considered:

Monitor long-distance routes separately.
Use shipment-volume trends for capacity planning.
Compare vehicle performance using distance, volume and fuel cost together.
Track delayed shipments and investigate repeated delays.
In a real logistics project, include additional factors such as traffic, weather, loading time and fuel-price changes.
⚠️ Note

This is a hypothetical logistics dataset created for an internship learning task. The results are intended to demonstrate data analysis and visualization techniques and should not be interpreted as actual company logistics performance.

👨‍💻 Author

Suraj Kumar
Logistics Data Analyst Intern
YuvaIntern – Week 3 Task
