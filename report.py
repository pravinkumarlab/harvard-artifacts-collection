import streamlit as st

def show_report():
    st.markdown("## 📄 Project Summary Report")

    st.markdown("""
This project demonstrates a complete ETL and SQL analytics workflow using real-world museum data from the Harvard Art Museums API.

The solution includes:
- Automated API data extraction with pagination
- JSON normalization into relational tables
- SQL-based analytical exploration
- Interactive Streamlit dashboard

All insights are derived purely through SQL queries.
""")
