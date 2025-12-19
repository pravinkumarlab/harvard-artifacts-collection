import streamlit as st

def show_home():
    st.markdown("## 🏛️ Harvard’s Artifacts Collection")
    st.markdown("### ETL | SQL Analytics | Streamlit Dashboard")
    st.markdown("---")

    st.markdown("""
**Project Goal:**  
Build an end-to-end ETL pipeline using the Harvard Art Museums API to extract, transform, store, and analyze cultural artifact data using SQL and Streamlit.
""")

    st.markdown("""
**Workflow:**
1. Extract data from API
2. Transform JSON to relational format
3. Load into SQLite database
4. Analyze using SQL queries
""")

    st.markdown("""
**Technologies Used:**
- Python
- SQL
- SQLite
- Streamlit
""")
