from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///harvard.db")

def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS artifact_metadata (
            id INTEGER PRIMARY KEY,
            title TEXT,
            culture TEXT,
            period TEXT,
            century TEXT,
            medium TEXT,
            dimensions TEXT,
            description TEXT,
            department TEXT,
            classification TEXT,
            accessionyear INTEGER,
            accessionmethod TEXT
        )
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS artifact_media (
            objectid INTEGER,
            imagecount INTEGER,
            mediacount INTEGER,
            colorcount INTEGER,
            rank INTEGER,
            datebegin INTEGER,
            dateend INTEGER
        )
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS artifact_colors (
            objectid INTEGER,
            color TEXT,
            spectrum TEXT,
            hue TEXT,
            percent REAL,
            css3 TEXT
        )
        """))

def insert_dataframe(df, table_name):
    df.to_sql(table_name, engine, if_exists="append", index=False)
