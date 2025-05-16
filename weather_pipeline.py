import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Directory Setup (for our original data and outputs)
DATA_DIR = "./data/"
OUTPUT_DIR = "./outputs/"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Data Ingestion (ingestion of the original data)
def ingest_data(file_path):
    return pd.read_csv(file_path)

# Data Cleaning Function
def clean_data(df):
    # Date Standardization Function
    def standardize_date(date_str):
        for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d.%m.%Y", "%m/%d/%Y", "%m-%d-%Y", "%d/%m/%Y"):
            try:
                return pd.to_datetime(date_str, format=fmt).strftime('%Y-%m-%d')
            except ValueError:
                continue
        return np.nan

    # Fill missing temperatures with city-wise average
    df["temperature_celsius"] = df.groupby('city')['temperature_celsius'].transform(lambda x: x.fillna(x.mean()))

    # Drop rows with missing dates
    df.dropna(subset=['date'], inplace=True)

    # Standardize date format using the standardize_date function
    df['date'] = df['date'].apply(standardize_date)

    # Remove rows with unknown weather condition (any case)
    df = df[df['weather_condition'].notna() & (~df['weather_condition'].str.lower().eq("unknown"))]

    return df

# Data Transformation
def transform_data(df):
    df['temperature_fahrenheit'] = df['temperature_celsius'] * 9 / 5 + 32
    return df

# Save Transformed Data
def save_transformed_data(df):
    df.to_csv(OUTPUT_DIR + "transformed_weather_data.csv", index=False)

# Generate Report
def generate_report(df):
    top_cities = df.groupby('city')['temperature_celsius'].mean().sort_values(ascending=False).head(5)
    report_path = OUTPUT_DIR + "report.txt"
    with open(report_path, "w") as file:
        file.write("Top 5 Cities by Average Temperature (°C)\n")
        file.write(str(top_cities))

# Bonus: Visualization
def generate_chart(df):
    avg_temp = df.groupby('city')['temperature_celsius'].mean().sort_values()
    plt.figure(figsize=(12, 8))
    avg_temp.plot(kind='barh', color='skyblue')
    plt.title("Average Temperature by City")
    plt.xlabel("Temperature (°C)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR + "temp_chart.png")

# Main Pipeline Function
def main():
    df = ingest_data(DATA_DIR + "wather_data.csv")
    df = clean_data(df)
    df = transform_data(df)
    save_transformed_data(df)
    generate_report(df)
    generate_chart(df)

if __name__ == "__main__":
    main()


