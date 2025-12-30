import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from etl import fetch_objects, transform
from database import init_db, insert_dataframe, engine
from sql_queries import QUERIES
from home import show_home
from report import show_report

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Harvard’s Artifacts Collection",
    layout="wide"
)

st.markdown(
    "<h2 style='text-align:center;'>🏛️ Harvard’s Artifacts Collection</h2>",
    unsafe_allow_html=True
)

# ─────────────────────────────────────────────
# SIDEBAR MENU
# ─────────────────────────────────────────────
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "Queries", "Report"],
        icons=["house", "database", "file-earmark-text"],
        default_index=0
    )

# ─────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# ─────────────────────────────────────────────
if "stage" not in st.session_state:
    st.session_state.stage = None

if "raw_data" not in st.session_state:
    st.session_state.raw_data = None

if "dfs" not in st.session_state:
    st.session_state.dfs = None

if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

# ─────────────────────────────────────────────
# HOME PAGE
# ─────────────────────────────────────────────
if selected == "Home":
    show_home()

# ─────────────────────────────────────────────
# QUERIES PAGE (MAIN APPLICATION)
# ─────────────────────────────────────────────
elif selected == "Queries":

    st.subheader("Artifact Data Collection & Analysis")

    # HOW TO USE (UNCHANGED UI)
    st.info("""
    ### 🧭 How to Use This Application

    **Step 1 – Collect Data**  
    Select an artifact classification and fetch real-time data from the Harvard Art Museums API.

    **Step 2 – Migrate to SQL**  
    Transform the collected JSON data and store it in a structured SQLite database.

    **Step 3 – Run SQL Queries**  
    Execute predefined analytical SQL queries to explore artifact metadata, media, and color insights.
    """)
    # ───────── STEP BUTTONS (UNCHANGED)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("▶ Collect Data"):
            st.session_state.stage = "collect"

    with c2:
        if st.button("▶ Migrate to SQL"):
            st.session_state.stage = "migrate"

    with c3:
        if st.button("▶ SQL Queries"):
            st.session_state.stage = "sql"

    st.markdown("---")

    # ─────────────────────────────────────────
    # STAGE 1 — COLLECT DATA
    # ─────────────────────────────────────────
    if st.session_state.stage == "collect":

        classification = st.selectbox(
            "Select Classification",
            [
                "Paintings", "Coins", "Sculpture", "Manuscripts",
                "Photographs", "Drawings", "Prints",
                "Textile Arts", "Archival Material",
                "Fragments", "Seals", "Straus Materials"
            ]
        )

        if st.button("Collect Data Now"):
            with st.spinner("Fetching data from Harvard Art Museums API..."):
                records = fetch_objects(classification)
                meta, media, colors = transform(records)

                st.session_state.dfs = (meta, media, colors)
                st.session_state.raw_data = {
                    "Metadata": meta.to_dict(orient="records"),
                    "Media": media.to_dict(orient="records"),
                    "Colours": colors.to_dict(orient="records")
                }

            st.success("Data collected successfully")

        # RAW DATA PREVIEW (OPTIONAL, SAFE)
        if st.session_state.raw_data:
            st.markdown("### Raw API Data Preview")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("#### Metadata")
                st.json(st.session_state.raw_data["Metadata"][:5])

            with col2:
                st.markdown("#### Media")
                st.json(st.session_state.raw_data["Media"][:5])

            with col3:
                st.markdown("#### Colours")
                st.json(st.session_state.raw_data["Colours"][:5])

    # ─────────────────────────────────────────
    # STAGE 2 — MIGRATE TO SQL
    # ─────────────────────────────────────────
    elif st.session_state.stage == "migrate":

        st.subheader("Insert the Collected Data")

        if st.session_state.dfs is None:
            st.warning("Please collect data first.")
        else:
            if st.button("Insert into Database"):
                init_db()
                meta, media, colors = st.session_state.dfs

                insert_dataframe(meta, "artifact_metadata")
                insert_dataframe(media, "artifact_media")
                insert_dataframe(colors, "artifact_colors")

                st.session_state.db_ready = True
                st.success("Data inserted successfully")

        # ─────────────────────────────────────────
        # SHOW INSERTED DATA (THREE TABLES)
        # ─────────────────────────────────────────
        if st.session_state.db_ready:

            st.markdown("## 🏺 Artifacts Metadata")
            meta_db = pd.read_sql("SELECT * FROM artifact_metadata ORDER BY classification",engine)
            st.dataframe(meta_db, use_container_width=True)

            st.markdown("## 🖼️ Artifacts Media")
            media_db = pd.read_sql("SELECT * FROM artifact_media",engine)
            st.dataframe(media_db, use_container_width=True)

            st.markdown("## 🎨 Artifacts Colours")
            colors_db = pd.read_sql("SELECT * FROM artifact_colors",engine)
            st.dataframe(colors_db, use_container_width=True)

    # ─────────────────────────────────────────
    # STAGE 3 — SQL QUERIES
    # ─────────────────────────────────────────
    elif st.session_state.stage == "sql":

        if not st.session_state.db_ready:
            st.warning("Please migrate data to SQL before running queries.")
        else:
            st.subheader("SQL Queries")

            query_name = st.selectbox(
                "Select a SQL Query",
                list(QUERIES.keys())
            )

            if query_name == "14. Colors by Object ID":

                # ─── Fetch all existing artifact IDs
                artifact_ids = pd.read_sql("SELECT DISTINCT objectid FROM artifact_colors ORDER BY objectid",engine)
                object_id = st.selectbox("Select Artifact ID",artifact_ids["objectid"])

                if st.button("Run Query"):
                    query = QUERIES[query_name].format(object_id)
                    df = pd.read_sql(query, engine)
                    st.dataframe(df, use_container_width=True)

            else:
                if st.button("Run Query"):
                    df = pd.read_sql(QUERIES[query_name], engine)
                    st.dataframe(df, use_container_width=True)

# ─────────────────────────────────────────────
# REPORT PAGE
# ─────────────────────────────────────────────
elif selected == "Report":
    show_report()
