import streamlit as st

def show_home():
    st.markdown("### ETL | SQL Analytics | Streamlit Dashboard")
    st.markdown("_" * 40)

    st.markdown("""
### 📌 Project Overview
The Harvard Art Museums provide open access to a vast collection of cultural artifacts through a public API.
This project implements a complete end-to-end data pipeline to extract, transform, store, and analyze artifact data using Python, SQL, and Streamlit.

The solution follows an ETL-driven analytical approach:
- Python for API integration, data transformation, and automation
- SQL for structured storage and analytical insights
- Streamlit for interactive data exploration

All insights are generated purely through SQL queries.
""")

    st.markdown("_" * 40)

    st.markdown("""
### 🎯 Problem Statement
- Collect 2500+ artifact records programmatically
- Normalize nested JSON into relational tables
- Perform SQL-based analysis
- Enable interactive exploration via Streamlit
""")

    st.markdown("_" * 40)

    st.markdown("""
### 🧠 Skills & Tools Used
- Python (requests, pandas)
- SQL (Joins, Aggregations, Subqueries)
- SQLite Database
- Streamlit
- REST API & Pagination
""")

    st.markdown("_" * 40)

    st.markdown("""
### 🏛️ Domain
Cultural Heritage Analytics / Digital Humanities
""")

    st.markdown("_" * 40)

    st.markdown("""
### 🗄 Database Tables
- artifact_metadata
- artifact_media
- artifact_colors
""")

    st.markdown("_" * 40)

    st.markdown("""
### ▶️ Run Instructions
```bash
pip install -r requirements.txt
streamlit run app.py
""")
    st.markdown("_" * 40)

    st.markdown("""

    ✅ Project Highlights

        End-to-end ETL

        API Pagination

        SQL-driven analytics

        Interactive dashboard
        """)

