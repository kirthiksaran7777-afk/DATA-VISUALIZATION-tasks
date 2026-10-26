## 1. 📈 Shopify Stock Data Analysis

### Shopify Stock Data Understanding, Cleaning & Exploratory Analysis

This section focuses on understanding and preparing Shopify stock data for analysis.

### Activities

* Load the Shopify stock dataset.
* Inspect the dataset structure.
* Display the first and last records.
* Check data types.
* Check dataset information.
* Identify missing values.
* Remove duplicate records where required.
* Convert date columns into the appropriate date format.
* Generate descriptive statistics.
* Examine stock price and trading volume information.

### Key Stock Attributes

* Date
* Open
* High
* Low
* Close
* Adjusted Close
* Volume

### Tools Used

```text
Python
Pandas
NumPy
Matplotlib
```

---

###  Shopify Stock Visualization, Time-Series Analysis & Financial Insights

This section focuses on visualizing stock-price movements and extracting financial insights from the time-series data.

### Analysis Includes

* Stock price visualization
* Open, High, Low and Close price analysis
* Trading volume analysis
* Time-series visualization
* Identification of price movements and trends
* Analysis of changes in stock prices over time
* Financial interpretation of the observed patterns

### Objective

The objective is to understand how Shopify's stock price and trading volume change over time and present the observations through meaningful visualizations.

---

# 2.  Healthcare Data Analysis

## Healthcare Data Understanding, Cleaning & Exploratory Analysis

The healthcare notebook uses the `healthcare_dataset.csv` dataset.

The dataset contains **55,500 records** and includes patient, admission, hospital, insurance, billing, medication, and test-result information.

### Activities

* Load the healthcare dataset.
* Display the first and last records.
* Examine dataset structure.
* Check column names and data types.
* Check missing values.
* Generate descriptive statistics.
* Analyze billing amounts.
* Convert admission and discharge dates into datetime format.
* Calculate hospital stay duration.

### Important Attributes

* Name
* Age
* Gender
* Blood Type
* Medical Condition
* Date of Admission
* Doctor
* Hospital
* Insurance Provider
* Billing Amount
* Room Number
* Admission Type
* Discharge Date
* Medication
* Test Results

The dataset contains admission types such as **Emergency, Elective, and Urgent**.

### Stay Duration

A new feature called `Stay_Days` is created:

```python
df['Stay_Days'] = (
    df['Discharge Date'] -
    df['Date of Admission']
).dt.days
```

This calculates the number of days between admission and discharge.

### Billing Analysis

Descriptive statistics are calculated for `Billing Amount`, including:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

The notebook records 55,500 billing observations.

---

##  Healthcare Data Visualization, Cost Relationship & Policy Insights

This section focuses on using visual analysis to understand healthcare costs and relationships within the dataset.

### Analysis Includes

* Healthcare data visualization
* Billing amount analysis
* Hospital stay analysis
* Admission-type analysis
* Medical-condition analysis
* Demographic segmentation
* Cost relationship analysis
* Comparison of healthcare-related attributes

### Objective

The objective is to identify meaningful relationships between healthcare characteristics and billing amounts and use the observed patterns to discuss possible **policy-related insights**.

> **Note:** Policy insights should be treated as analytical observations from this dataset rather than general conclusions about real-world healthcare systems.

---

# 3.  Student Performance Data Analysis

## Student Performance Data Understanding, Cleaning & Feature Engineering

The student performance notebook uses `StudentsPerformance.csv`.

The dataset contains **1,000 student records** and 8 columns.

### Activities

* Load the student performance dataset.
* Display sample records.
* Check data types.
* Inspect dataset information.
* Check missing values.
* Generate descriptive statistics.
* Identify categorical columns.
* Standardize categorical values.
* Create new features for student performance.

### Dataset Attributes

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Math Score
* Reading Score
* Writing Score

The notebook confirms that the dataset contains no missing values in these columns.

### Data Cleaning

Categorical columns are standardized using:

```python
df[col] = df[col].str.strip().str.title()
```

This removes unnecessary spaces and standardizes capitalization.

### Feature Engineering

Two new features are created.

#### Average Score

```python
df['average_score'] = (
    df['math score'] +
    df['reading score'] +
    df['writing score']
) / 3
```

#### Total Score

```python
df['total_score'] = (
    df['math score'] +
    df['reading score'] +
    df['writing score']
)
```

These features provide an overall measure of student performance.

---

# 🛠️ Technologies Used

| Technology                      | Purpose                             |
| ------------------------------- | ----------------------------------- |
| Python                          | Programming and analysis            |
| Pandas                          | Data loading, cleaning and analysis |
| NumPy                           | Numerical operations                |
| Matplotlib                      | Data visualization                  |
| Seaborn                         | Statistical visualization           |
| Google Colab / Jupyter Notebook | Development environment             |

---

# 📁 Project Structure

```text
Data-Analysis-Project/
│
├── Shopify/
│   ├── Shopify_Stock_Analysis.ipynb
│   └── Shopify_Stock_Data.csv
│
├── Healthcare/
│   ├── Healthcare 1.ipynb
│   └── healthcare_dataset.csv
│
├── Student-Performance/
│   ├── Untitled16.ipynb
│   └── StudentsPerformance.csv
│
└── README.md
```

---

# 🔄 Overall Data Analysis Workflow

```text
          Dataset
             ↓
      Data Understanding
             ↓
       Data Inspection
             ↓
       Data Cleaning
             ↓
    Missing Value Checking
             ↓
      Data Transformation
             ↓
   Feature Engineering
             ↓
  Exploratory Data Analysis
             ↓
       Visualization
             ↓
       Relationship Analysis
             ↓
          Insights
```

---

# 🎯 Project Objectives

### Shopify Stock

* Understand stock-market data.
* Clean and prepare stock data.
* Visualize stock-price movements.
* Perform time-series analysis.
* Identify financial patterns from the available data.

### Healthcare

* Understand healthcare records.
* Clean and transform healthcare data.
* Analyze billing and hospital stays.
* Explore relationships between healthcare variables.
* Develop dataset-based policy insights.

### Student Performance

* Understand student demographic and score data.
* Clean categorical attributes.
* Check data quality.
* Create `average_score` and `total_score`.
* Perform feature engineering for performance analysis.

---

# 📊 Key Learning Outcomes

Through these projects, the following Python data-analysis skills are demonstrated:

* Reading CSV and Excel datasets
* DataFrame operations
* Data inspection
* Data cleaning
* Missing-value analysis
* Duplicate detection
* Date and time conversion
* Descriptive statistics
* Feature engineering
* Time-series analysis
* Data visualization
* Relationship analysis
* Interpretation of analytical results

---

# 🚀 How to Run the Project

### 1. Install Python

Install Python 3.x on your system.

### 2. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

### 3. Open Jupyter Notebook

```bash
jupyter notebook
```

or use **Google Colab**.

### 4. Upload the Required Dataset

Keep the corresponding dataset in the same working directory as the notebook.

### 5. Run the Notebook

Run the cells sequentially from top to bottom.

---

#  Conclusion

This project demonstrates a complete introductory data-analysis workflow using three different domains:

**Financial Data → Healthcare Data → Educational Data**

The Shopify analysis focuses on **stock understanding, visualization, time-series analysis, and financial insights**.

The Healthcare analysis focuses on **data understanding, cleaning, visualization, cost relationships, and policy insights**.

The Student Performance analysis focuses on **data understanding, cleaning, and feature engineering**.

Together, these notebooks demonstrate how Python can be used to transform raw datasets into structured information and meaningful analytical insights.
#  King County House Price Prediction

##  Project Overview

This project focuses on analyzing the **King County House Sales dataset** and developing a machine-learning model to predict residential house prices.

The dataset contains **21,613 house-sale records** with information about property size, bedrooms, bathrooms, location, condition, construction quality, waterfront status, and other characteristics that may influence house prices.

The primary objective of this project is to build a **regression model** that can predict the sale price of a house based on its features.

---

## Objectives

The main objectives of this project are:

- Understand and explore the house-sales dataset.
- Perform exploratory data analysis (EDA).
- Clean and preprocess the data.
- Identify important factors affecting house prices.
- Perform feature engineering.
- Build machine-learning regression models.
- Compare model performance.
- Evaluate predictions using appropriate regression metrics.
- Identify the most important features influencing house prices.

---

##  Dataset

The dataset is stored in:

```text
kc_house_data.csv
```

### Dataset Information

| Property | Value |
|---|---:|
| Number of records | 21,613 |
| Number of columns | 21 |
| Target variable | `price` |
| Problem type | Regression |
| Geographic area | King County, Washington |

---

## 🧾 Dataset Columns

| Column | Description |
|---|---|
| `id` | Unique identifier for each property |
| `date` | Date on which the house sale was recorded |
| `price` | Sale price of the house |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Interior living area in square feet |
| `sqft_lot` | Total lot area in square feet |
| `floors` | Number of floors |
| `waterfront` | Indicates whether the property has a waterfront location |
| `view` | Quality of the property's view |
| `condition` | Overall condition of the property |
| `grade` | Overall construction/design quality |
| `sqft_above` | Living area above ground level |
| `sqft_basement` | Basement area in square feet |
| `yr_built` | Year the property was originally built |
| `yr_renovated` | Year the property was renovated |
| `zipcode` | ZIP code of the property |
| `lat` | Latitude |
| `long` | Longitude |
| `sqft_living15` | Average living area of the 15 nearest properties |
| `sqft_lot15` | Average lot area of the 15 nearest properties |

---

##Target Variable

The target variable for this project is:

```text
price
```

`price` represents the actual sale price of the property.

The machine-learning problem can therefore be represented as:

```text
House Features → Machine Learning Model → Predicted House Price
```

---

#  Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the structure of the dataset and discover relationships between different variables.

### Data Loading

```python
import pandas as pd

df = pd.read_csv("kc_house_data.csv")

print(df.head())
print(df.shape)
print(df.info())
```

### Summary Statistics

```python
print(df.describe())
```

This helps identify:

- Mean
- Median
- Minimum
- Maximum
- Standard deviation
- Quartiles

for the numerical variables.

---

##  Checking Missing Values

```python
print(df.isnull().sum())
```

Missing values should be identified before training a machine-learning model.

Possible strategies include:

- Removing missing records
- Filling numerical values with the median
- Filling categorical values with the mode
- Using advanced imputation techniques

---

##  Checking Duplicate Records

```python
print(df.duplicated().sum())
```

Duplicate records should be investigated and removed if they represent duplicate observations.

---

#  Data Visualization

Visualization helps understand relationships between house characteristics and prices.

### House Price Distribution

```python
import matplotlib.pyplot as plt

plt.hist(df["price"], bins=50)
plt.xlabel("House Price")
plt.ylabel("Number of Houses")
plt.title("Distribution of House Prices")
plt.show()
```

House prices are typically right-skewed, with a relatively small number of very expensive properties.

---

##  Living Area vs Price

```python
plt.scatter(df["sqft_living"], df["price"], alpha=0.3)
plt.xlabel("Living Area (sqft)")
plt.ylabel("Price")
plt.title("Living Area vs House Price")
plt.show()
```

This analysis can help determine whether larger living areas are associated with higher property prices.

---

##  Bedrooms vs Price

```python
import seaborn as sns

sns.boxplot(x="bedrooms", y="price", data=df)
plt.title("Bedrooms vs House Price")
plt.show()
```

This helps analyze how house prices vary according to the number of bedrooms.

---

##  Grade vs Price

```python
sns.boxplot(x="grade", y="price", data=df)
plt.title("Grade vs House Price")
plt.show()
```

The `grade` variable represents the construction and design quality of the property and can be an important predictor of price.

---

# Correlation Analysis

Correlation can be used to understand relationships between numerical variables.

```python
correlation = df.corr(numeric_only=True)

print(correlation["price"].sort_values(ascending=False))
```

A heatmap can also be used:

```python
plt.figure(figsize=(14, 10))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")
plt.show()
```

Features such as `sqft_living`, `grade`, `bathrooms`, `view`, and geographic variables may show meaningful relationships with house prices.

---

#  Data Preprocessing

Before training machine-learning models, the data needs to be prepared.

## Date Conversion

The `date` column can be converted to a datetime format:

```python
df["date"] = pd.to_datetime(df["date"])
```

Additional features can then be extracted:

```python
df["sale_year"] = df["date"].dt.year
df["sale_month"] = df["date"].dt.month
```

---

##  House Age

A useful feature is the age of the property at the time of sale.

```python
df["house_age"] = df["sale_year"] - df["yr_built"]
```

This may provide more useful information to a model than the original construction year alone.

---

##  Renovation Feature

The `yr_renovated` column may contain `0` when a property has no recorded renovation.

A binary feature can be created:

```python
df["was_renovated"] = (df["yr_renovated"] > 0).astype(int)
```

---

## 📐 Total Living Area

A combined area feature can also be created:

```python
df["total_sqft"] = (
    df["sqft_living"] +
    df["sqft_basement"]
)
```

---

# Feature Engineering

Potential engineered features include:

- House age
- Whether the house was renovated
- Total square footage
- Sale year
- Sale month
- Square footage per bedroom
- Living-area-to-lot-area ratio
- Years since renovation
- Geographic clusters

Example:

```python
df["sqft_per_bedroom"] = (
    df["sqft_living"] / df["bedrooms"]
)

df["living_lot_ratio"] = (
    df["sqft_living"] / df["sqft_lot"]
)
```

Feature engineering can help machine-learning models identify patterns that are not directly represented by the original variables.

---

#  Machine Learning

This project is a **supervised learning regression problem**.

The input variables are the house characteristics, while the output variable is the house sale price.

```text
X = House Features
y = House Price
```

---

# ✂

House Price Visualization, Spatial Analytics and Real Estate Insights

Project Overview

This project analyzes house price data using Python and creates visualizations to understand the factors affecting property prices. The analysis focuses on living area, property grade, waterfront status, and geographical location.

Objectives

Analyze the relationship between living area and house price.

Visualize house price distributions across different property characteristics.

Analyze the geographical distribution of house prices using latitude and longitude.

Identify high value locations based on average property prices.

Generate basic real estate investment insights from the dataset.

Dataset

The project uses the Household_preprecessed.csv dataset. The dataset contains information about residential properties, including price, living area, grade, waterfront status, latitude, longitude, and ZIP code.

Technologies Used

Python

Pandas

Seaborn

Matplotlib

Google Colab

Visualizations

The project creates a regression plot showing the relationship between living area and price.

A box plot is used to compare prices based on waterfront status.

A geographical scatter plot shows house prices using latitude and longitude, with colors representing price levels.

The project also identifies the top high value ZIP codes based on average house price.

Real Estate Insights

The analysis helps identify locations with higher average property prices.

Larger living areas can be associated with higher property prices.

Waterfront properties can have different price distributions compared with non waterfront properties.

Geographical price patterns can help identify premium real estate areas.

High value ZIP codes can be considered for further real estate investment analysis.

How to Run

Upload Household_preprecessed.csv to Google Colab.

Open the Python code in a Colab notebook.

Run the code cells.

Review the generated visualizations and investment summary.

Conclusion

This project demonstrates how data visualization and spatial analysis can be used to understand residential property prices. The results can support further real estate research, location analysis, and investment decision making.
