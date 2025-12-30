# 🏛️ Harvard’s Artifacts Collection Analysis  
**ETL | SQL Analytics | Streamlit Dashboard**

---

## 📌 Project Overview
The Harvard Art Museums provide open access to a vast collection of cultural artifacts through a public API.  
This project implements a **complete end-to-end data pipeline** to extract, transform, store, and analyze artifact data using **Python, SQL, and Streamlit**.

The solution follows an **ETL-driven analytical approach**, where:
- **Python** is used for API integration, data transformation, and automation
- **SQL** is used for structured storage and all analytical insights
- **Streamlit** is used to build an interactive data exploration interface

All insights are generated **purely through SQL queries**, ensuring transparency and analytical rigor.

---

## 🎯 Problem Statement
The objective of this project is to:
- Programmatically collect large-scale artifact data (2500+ records) from the Harvard Art Museums API
- Normalize complex JSON data into relational database tables
- Perform analytical exploration using SQL
- Enable interactive querying and exploration through a Streamlit application

This project demonstrates real-world skills in **API handling, pagination, ETL design, relational modeling, and SQL analytics**.

---

## 🧠 Skills & Tools Used
- **Python**
  - requests (API integration)
  - pandas (data transformation)
- **SQL**
  - Joins
  - Aggregations
  - Filtering
  - Grouping
  - Subqueries
- **SQLite Database**
- **Streamlit** (Interactive Web Application)
- REST API & Pagination Handling
- Data Cleaning & Normalization

🚫 ORM-based analytics are **not used**  
✔ All analytical insights are derived using **raw SQL queries**

---

## 🏛️ Domain
**Cultural Heritage Analytics / Digital Humanities**

---

## 🗂 Data Source Description
| Source | Description |
|------|------------|
| Harvard Art Museums API | Open-access API providing artifact metadata, media, and color information |

---

## 🔄 ETL Pipeline Description

### **Extract**
- Data is fetched from the Harvard Art Museums API using a valid API key
- Pagination is implemented (`size = 100`) to collect **2500+ records per classification**
- Only classifications with sufficient object counts are selected for analysis

### **Transform**
- Nested JSON responses are cleaned and flattened
- Data is normalized into three logical entities:
  - Artifact metadata
  - Media-related attributes
  - Color-level details

### **Load**
- Transformed data is inserted into a relational SQLite database
- Tables are created programmatically if they do not exist

---

## 🗄 Database Schema

### **artifact_metadata**
Stores general artifact information
- id
- title
- culture
- period
- century
- medium
- dimensions
- description
- department
- classification
- accessionyear
- accessionmethod

### **artifact_media**
Stores media-related information
- objectid
- imagecount
- mediacount
- colorcount
- rank
- datebegin
- dateend

### **artifact_colors**
Stores color-level details
- objectid
- color
- spectrum
- hue
- percent
- css3

---

## 🔍 SQL Analytics

### ✔ Mandatory Queries
The project includes **20 SQL queries** as required, covering:
- Artifact metadata analysis
- Media statistics
- Color distribution
- Temporal filtering
- Multi-table join operations

### ➕ Additional Learner-Framed Queries
In addition to the required queries, **10 custom SQL queries** were designed to derive deeper insights, such as:
- Artifact distribution across centuries
- Department-wise dominance
- Most common mediums used
- Media richness by classification
- Data completeness checks
- Color usage trends and dominance

These additional queries demonstrate **independent analytical thinking beyond the given requirements**.

---

## 🖥️ Streamlit Application Features
- Classification selection
- Automated data collection via API
- SQL database insertion
- Execution of predefined SQL queries
- Display of query results in tabular format
- Support for exploratory and custom analysis

---

## ▶️ How to Run the Project

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure
```
harvard-artifacts-project/
│── app.py
│── etl.py
│── database.py
│── sql_queries.py
│── config.py
│── requirements.txt
│── harvard.db
│── README.md
```

---
