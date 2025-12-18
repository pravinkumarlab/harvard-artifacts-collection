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
# SESSION STATE
# ─────────────────────────────────────────────
if "stage" not in st.session_state:
    st.session_state.stage = None

if "raw_data" not in st.session_state:
    st.session_state.raw_data = None

if "dfs" not in st.session_state:
    st.session_state.dfs = None

# ─────────────────────────────────────────────
# HOME illustrates only content
# ─────────────────────────────────────────────
if selected == "Home":
    show_home()

# ─────────────────────────────────────────────
# QUERIES PAGE (MAIN APPLICATION)
# ─────────────────────────────────────────────
elif selected == "Queries":

    st.subheader("Artifact Data Collection & Analysis")

    # ───────── STEP BUTTONS
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
            ["Paintings", "Coins", "Sculpture", "Manuscripts", "Photographs", "Drawings", 
             "Prints", "Textile Arts", "Archival Material", "Fragments", "Seals", "Straus Materials"]
        )

        if st.button("Collect Data Now"):
            with st.spinner("Fetching data from Harvard Art Museums API..."):
                records = fetch_objects(classification)
                meta, media, colors = transform(records)

                st.session_state.raw_data = {
                    "Metadata": meta.to_dict(orient="records"),
                    "Media": media.to_dict(orient="records"),
                    "Colours": colors.to_dict(orient="records")
                }

                st.session_state.dfs = (meta, media, colors)

            st.success("Data collected successfully")

        # RAW JSON DISPLAY ONLY
        if st.session_state.raw_data:
            st.markdown("### Raw API Data")

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

                st.success("Data inserted successfully")

            # ─── FETCH FROM DATABASE (NOT SESSION)
            st.markdown("### Inserted Data")

            meta_db = pd.read_sql(
                "SELECT * FROM artifact_metadata ORDER BY classification",
                engine
            )
            media_db = pd.read_sql(
                "SELECT * FROM artifact_media",
                engine
            )
            colors_db = pd.read_sql(
                "SELECT * FROM artifact_colors",
                engine
            )

            t1, t2, t3 = st.tabs([
                "Artifacts Metadata",
                "Artifacts Media",
                "Artifacts Colours"
            ])

            with t1:
                st.dataframe(meta_db, use_container_width=True)

            with t2:
                st.dataframe(media_db, use_container_width=True)

            with t3:
                st.dataframe(colors_db, use_container_width=True)

    # ─────────────────────────────────────────
    # STAGE 3 — SQL QUERIES
    # ─────────────────────────────────────────
    elif st.session_state.stage == "sql":

        st.subheader("SQL Queries")

        query_name = st.selectbox(
            "Select a SQL Query",
            list(QUERIES.keys())
        )

        if st.button("Run Query"):
            df = pd.read_sql(QUERIES[query_name], engine)
            st.dataframe(df, use_container_width=True)

# ─────────────────────────────────────────────
# REPORT PAGE
# ─────────────────────────────────────────────
elif selected == "Report":
    show_report()