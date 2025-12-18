import streamlit as st

def show_report():
    st.markdown("## 📄 Harvard’s Artifacts Collection Analysis Report")

    st.markdown("""
This report documents an end-to-end data analytics project developed using the Harvard Art Museums open-access API. 
The project focuses on collecting, processing, storing, and analyzing cultural artifact data using Python, SQL, and an ETL framework.

---

### 1. Project Objective
The primary objective of this project is to extract artifact data from the Harvard Art Museums API, transform complex JSON data into a structured relational format, store it in a database, and generate meaningful insights using SQL queries.

---

### 2. Data Source
The data for this project is obtained from the Harvard Art Museums public API. This API provides detailed metadata about artifacts, including classification, department, culture, media details, and color information.

---

### 3. ETL Methodology

**Extract**  
Python is used to fetch artifact data from the API with pagination to collect more than 2500 records per classification.

**Transform**  
The extracted JSON data is cleaned, flattened, and normalized into separate tables for metadata, media, and color attributes.

**Load**  
The transformed data is stored in a SQLite relational database for analysis.

---

### 4. Database Design
The database is designed using a relational model and consists of three main tables:
- **Artifact Metadata** – stores general information about artifacts  
- **Artifact Media** – stores image and media-related information  
- **Artifact Colors** – stores detailed color attributes of artifacts  

---

### 5. SQL Analysis
All analytical insights in this project are derived using SQL queries.  
The project includes:
- **20 mandatory SQL queries**, and  
- **10 additional learner-framed queries**  

These queries explore trends across centuries, departments, media usage, and color distributions.

---

### 6. Streamlit Application
A Streamlit web application is developed to provide an interactive interface for data collection and analysis.  
Users can:
- Trigger API data extraction  
- Store data in the database  
- Execute SQL queries  
- View results in tabular format  

---

### 7. Conclusion
This project demonstrates a complete real-world data analytics workflow involving API integration, ETL processing, relational database design, SQL-based analysis, and interactive visualization.  
It showcases practical skills relevant to data analytics and data engineering roles.
""")
