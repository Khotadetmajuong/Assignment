import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Redirect print to a log file
log_file = open('analysis_output.txt', 'w', encoding='utf-8')
def log_print(*args, **kwargs):
    print(*args, **kwargs)
    print(*args, **kwargs, file=log_file)

# Use seaborn's default style
sns.set_theme()

print("Loading and preparing data...")
df = pd.read_csv('climate_action_data.csv')

# Clean the data
df = df.replace('error', np.nan)

# Convert numeric columns
numeric_columns = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                  'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values with median for numeric columns
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

print("\n1. Variables Influencing Fertilizer Recommendations:")
# Calculate correlations with fertilizer recommendations
correlations = df[numeric_columns].corr()['Fertilizer_Recommended(kg/ha)'].sort_values(ascending=False)
print("\nCorrelation with Fertilizer Recommendations:")
print(correlations)

# Create a bar plot of correlations
plt.figure(figsize=(10, 6))
correlations.drop('Fertilizer_Recommended(kg/ha)').plot(kind='bar')
plt.title('Correlation of Variables with Fertilizer Recommendations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('fertilizer_correlations.png')
plt.close()

print("\n2. Crop Types by Average Soil Moisture:")
# Calculate average soil moisture by crop type
crop_moisture = df.groupby('Crop_Type')['Soil_Moisture(%)'].agg(['mean', 'std']).sort_values('mean', ascending=False)
print("\nAverage Soil Moisture by Crop Type:")
print(crop_moisture)

# Create a bar plot of average soil moisture by crop type
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Crop_Type', y='Soil_Moisture(%)')
plt.title('Average Soil Moisture by Crop Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('crop_moisture.png')
plt.close()

print("\n3. Irrigation Analysis for High-Temperature Crops:")
# Analyze crops with temperature above 30°C
high_temp_crops = df[df['Temperature(C)'] > 30].groupby('Crop_Type').agg({
    'Temperature(C)': ['mean', 'std'],
    'Soil_Moisture(%)': ['mean', 'std'],
    'Irrigation_Recommended(mm)': ['mean', 'std']
}).round(2)

print("\nAnalysis of Crops with Temperature > 30°C:")
print(high_temp_crops)

# Create a scatter plot of temperature vs irrigation
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Temperature(C)', y='Irrigation_Recommended(mm)', hue='Crop_Type')
plt.title('Temperature vs Irrigation by Crop Type')
plt.axvline(x=30, color='r', linestyle='--', label='30°C Threshold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('temperature_irrigation.png')
plt.close()

# Calculate irrigation adjustment recommendations
print("\nIrrigation Adjustment Recommendations:")
for crop in high_temp_crops.index:
    avg_temp = high_temp_crops.loc[crop, ('Temperature(C)', 'mean')]
    avg_moisture = high_temp_crops.loc[crop, ('Soil_Moisture(%)', 'mean')]
    avg_irrigation = high_temp_crops.loc[crop, ('Irrigation_Recommended(mm)', 'mean')]
    
    # Calculate recommended adjustment
    temp_factor = (avg_temp - 30) / 5  # Increase irrigation by 20% for every 5°C above 30
    moisture_factor = (50 - avg_moisture) / 10  # Increase irrigation by 10% for every 10% below optimal moisture
    
    adjustment = avg_irrigation * (1 + temp_factor + moisture_factor)
    
    print(f"\n{crop}:")
    print(f"Average Temperature: {avg_temp:.1f}°C")
    print(f"Average Soil Moisture: {avg_moisture:.1f}%")
    print(f"Current Irrigation: {avg_irrigation:.1f} mm")
    print(f"Recommended Irrigation: {adjustment:.1f} mm")
    print(f"Adjustment: +{(adjustment - avg_irrigation):.1f} mm")

log_print("\nExporting cleaned dataset...")
df.to_csv('cleaned_precision_agriculture_data.csv', index=False)
log_print("Analysis complete! Check the generated visualizations and the cleaned dataset.")
log_file.close() 