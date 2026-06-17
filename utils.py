import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data():

    dtype_dict = {
        "title":"string",
        "all_genres":"string",
        "developers":"string",
        "publishers":"string",
        "is_multiplayer":"string"
    }

    df = pd.read_csv(
        "all_data.csv",
        low_memory=False,
        dtype=dtype_dict
    )

    return df
