import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="가격 분석", page_icon="💰", layout="wide")

df = load_data()

st.title("💰 가격의 역설: 비싸면 정말 덜 팔릴까?")

st.markdown("""
게임 가격대별로 평균 흥행점수와 평균 추정 보유자 수를 비교합니다.
""")

price_stats = df.groupby("가격대", observed=False).agg(
    평균흥행점수=("흥행점수", "mean"),
    평균보유자수=("owners_min", "mean"),
    게임수=("name", "count")
).reset_index()

fig = px.bar(
    price_stats,
    x="가격대",
    y="평균흥행점수",
    text=price_stats["평균흥행점수"].round(1),
    title="가격대별 평균 흥행점수",
    template="plotly_dark"
)

fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 가격대별 분석표")
st.dataframe(price_stats, use_container_width=True)

st.info("""
분석 관점: 무료 게임이 무조건 흥행하는지, 또는 적절한 유료 가격대의 게임이 더 높은 흥행점수를 가지는지 확인할 수 있습니다.
""")
