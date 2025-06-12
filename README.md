# 🛒 Ecommerce Price Tracker

A complete data engineering and analytics pipeline that tracks and analyzes ecommerce product pricing, discounts, and brand performance using PySpark, BigQuery, and dbt.

---

## 📌 Project Overview

This project demonstrates how to build a scalable data pipeline for ecommerce price tracking. It involves data cleaning, transformation, modeling, and analytics-ready output using modern data tools and best practices.

---

## 🧱 Tech Stack

- **PySpark** – for scalable data cleaning and transformation
- **Google BigQuery** – for cloud-based data storage and querying
- **dbt (Data Build Tool)** – for modular SQL modeling, testing, and documentation
- **Parquet/CSV** – for intermediate data storage

---

## ✅ Features

- Cleans raw ecommerce product data
- Calculates discount percentages and flags discounted products
- Parses and standardizes product categories
- Aggregates average final price by brand
- Flags high-rated products (rating ≥ 4.0)
- Builds analytics-ready tables using dbt
- (Optional) Ready for dashboarding in Power BI, Looker Studio, or Metabase

---

## 🧪 Data Pipeline Steps

### 1. **Data Cleaning & Transformation (PySpark)**
- Removed unnecessary columns
- Handled missing values
- Standardized data types (prices, ratings, timestamps)
- Parsed categories into arrays
- Calculated `discount_pct`, `is_discounted`, and other flags
- Saved outputs in Parquet and CSV formats

### 2. **Data Warehouse (BigQuery)**
- Loaded 3 datasets:
  - `transformed_data`
  - `high_rated_products`
  - `avg_brand_price`

### 3. **Data Modeling (dbt)**
- Created staging models for each dataset
- Built a final model `product_summary` with:
  - Product metadata
  - Discount and rating flags
  - Brand-level price comparison
- Added tests and documentation
- Generated dbt docs for easy exploration

---

## 📊 Final Output: `product_summary`

An analytics-ready table that includes:
- Product details
- Discount and rating flags
- Average brand price
- Price comparison indicators

---

