import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)

def load_data():

    usecols = [
        "title",
        "release_year",
        "all_genres",
        "is_multiplayer",

        "user_rating",
        "metacritic",

        "library_count",

        "avg_playtime_hours",

        "popularity_score",

        "engagement_score",

        "all_platforms"
    ]

    dtype_dict = {

        "title":"string",

        "all_genres":"string",

        "all_platforms":"string",

        "is_multiplayer":"string"

    }

    df = pd.read_csv(

        "all_data.csv",

        usecols=usecols,

        dtype=dtype_dict,

        low_memory=False

    )

    numeric_cols = [

        "release_year",

        "user_rating",

        "metacritic",

        "library_count",

        "avg_playtime_hours",

        "popularity_score",

        "engagement_score"

    ]

    for col in numeric_cols:

        df[col] = pd.to_numeric(

            df[col],

            errors="coerce"

        )

    return df
