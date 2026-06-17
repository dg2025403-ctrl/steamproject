import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="리뷰 분석", page_icon="⭐", layout="wide")

df = load_data()

st.title("⭐ 리뷰의 가치: 평점이 높으면 무조건 대박일까?")

st.markdown("""
긍정 리뷰율과 흥행점수의 관계를 산점도로 분석합니다.
""")

sample = df[df["total_reviews"] >= 50].copy()

fig = px.scatter(
    sample,
    x="positive_rate",
    y="흥행점수",
    size="total_reviews",
    hover_name="name",
    title="긍정 리뷰율과 흥행점수의 관계",
    labels={
        "positive_rate": "긍정 리뷰율(%)",
        "흥행점수": "흥행점수",
        "total_reviews": "전체 리뷰 수"
    },
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

corr = sample["positive_rate"].corr(sample["흥행점수"])

st.metric("긍정 리뷰율과 흥행점수의 상관계수", f"{corr:.2f}")

st.info("""
상관계수가 1에 가까울수록 긍정 리뷰율과 흥행점수가 함께 증가하는 경향이 강하다는 뜻입니다.
하지만 평점이 높아도 리뷰 수나 동시 접속자가 적으면 흥행점수는 낮을 수 있습니다.
""")
