# Weather Data Processing Pipeline

## 1. Introduction

This project is a weather data processing pipeline that ingests raw weather data, cleans it, transforms it, generates a report, and provides a visualization. The focus is to ensure accurate, consistent, and clean weather data, making it ready for analysis.

## 2. Step-by-Step Instructions to Run the Pipeline Locally

### Prerequisites

* Python 3.x installed on your system.
* Required Python libraries installed: `pandas`, `numpy`, `matplotlib`.

### Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

### Directory Setup (already done, only new dataset)

* Place your raw weather data file (named `wather_data.csv`) inside the `./data/` directory.
* The script will automatically create an `./outputs/` directory for all outputs (transformed data, report, and visualization).

### Running the Pipeline

```bash
python weather_pipeline.py
```

## 3. Approach and Challenges

### Approach

* **Ingestion:** The raw data is ingested using `pandas.read_csv`.
* **Cleaning:** The data is cleaned by standardizing date formats, handling missing values, and filtering out invalid weather conditions.
* **Transformation:** Celsius temperatures are converted to Fahrenheit (added one more column).
* **Report Generation:** A text report is created, showing the top 5 cities by average temperature.
* **Visualization:** A bar chart is generated, displaying average temperatures by city.

### Challenges

* Handling multiple date formats and ensuring consistent standardization (Multiple Date formats)
* Efficiently removing rows with unknown or invalid weather conditions without affecting valid data. (Mixed between 'Unknown' and 'unknown')

## 4. Sample Output and Visualization

* Transformed data saved as `transformed_weather_data.csv` in the `./outputs/` directory.
* Text report saved as `report.txt` in the same directory.
* Visualization saved as `temp_chart.png`.
* Compare both the data transformed using EDA process and data data automation process (both same outputs)
## 5. Detailed Exploratory Data Analysis (EDA)

* The EDA process involves analyzing the distribution of temperatures, detecting missing values, and understanding weather condition distributions.
* Date formats are identified using visualizations
* Key statistics, missing value patterns, and top weather conditions are explored.
* Visualizations are used for better insight into temperature distributions across cities.
* The pipeline is designed for flexibility, allowing easy modification of the data cleaning process (Just following the specified tasks)

