import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="흥행요인 분석", page_icon="🚀", layout="wide")

df = load_data()

st.title("🚀 핵심 흥행 요인 종합 분석")

st.markdown("""
동시 접속자, 평균 플레이 시간, 할인율이 흥행점수와 어떤 관계를 가지는지 분석합니다.
""")

top = df.sort_values("흥행점수", ascending=False).head(15)

fig1 = px.bar(
    top,
    x="흥행점수",
    y="name",
    orientation="h",
    title="흥행점수 TOP 15 게임",
    template="plotly_dark"
)

fig1.update_layout(yaxis={"categoryorder": "total ascending"})
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🎮 동시 접속자와 흥행점수")

sample = df[df["ccu"] > 0].copy()

fig2 = px.scatter(
    sample,
    x="ccu",
    y="흥행점수",
    hover_name="name",
    title="동시 접속자와 흥행점수의 관계",
    labels={
        "ccu": "동시 접속자 수",
        "흥행점수": "흥행점수"
    },
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("🏷️ 할인율별 평균 흥행점수")

discount_stats = df.groupby("할인율구간", observed=False).agg(
    평균흥행점수=("흥행점수", "mean"),
    평균보유자수=("owners_min", "mean"),
    게임수=("name", "count")
).reset_index()

fig3 = px.bar(
    discount_stats,
    x="할인율구간",
    y="평균흥행점수",
    text=discount_stats["평균흥행점수"].round(1),
    title="할인율 구간별 평균 흥행점수",
    template="plotly_dark"
)

fig3.update_traces(textposition="outside")
st.plotly_chart(fig3, use_container_width=True)

st.dataframe(discount_stats, use_container_width=True)

st.success("""
결론: 게임 흥행은 단순히 가격이나 할인 하나로 결정되지 않고,
리뷰 수, 긍정 리뷰율, 동시 접속자, 평균 플레이 시간이 함께 작용합니다.
""")
