import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv")

    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    df["positive"] = pd.to_numeric(df["positive"], errors="coerce").fillna(0)
    df["negative"] = pd.to_numeric(df["negative"], errors="coerce").fillna(0)
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
    df["initialprice"] = pd.to_numeric(df["initialprice"], errors="coerce").fillna(0)
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0)
    df["ccu"] = pd.to_numeric(df["ccu"], errors="coerce").fillna(0)
    df["average_forever"] = pd.to_numeric(df["average_forever"], errors="coerce").fillna(0)

    df["total_reviews"] = df["positive"] + df["negative"]
    df["positive_rate"] = np.where(
        df["total_reviews"] > 0,
        df["positive"] / df["total_reviews"] * 100,
        0
    )

    df["price_won"] = df["price"] / 100
    df["initial_price_won"] = df["initialprice"] / 100

    df["owners_min"] = df["owners"].astype(str).str.extract(r"([\d,]+)")[0]
    df["owners_min"] = df["owners_min"].str.replace(",", "", regex=False)
    df["owners_min"] = pd.to_numeric(df["owners_min"], errors="coerce").fillna(0)

    df["흥행점수"] = (
        np.log1p(df["owners_min"]) * 35
        + np.log1p(df["total_reviews"]) * 25
        + df["positive_rate"] * 0.3
        + np.log1p(df["ccu"]) * 20
        + np.log1p(df["average_forever"]) * 10
    )

    df["가격대"] = pd.cut(
        df["price_won"],
        bins=[-1, 0, 5, 10, 20, 40, 10000],
        labels=["무료", "5달러 이하", "10달러 이하", "20달러 이하", "40달러 이하", "40달러 초과"]
    )

    df["할인율구간"] = pd.cut(
        df["discount"],
        bins=[-1, 0, 25, 50, 75, 100],
        labels=["할인 없음", "1~25%", "26~50%", "51~75%", "76~100%"]
    )

    return df
