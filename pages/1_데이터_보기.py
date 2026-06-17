import streamlit as st
from utils import load_data

st.set_page_config(page_title="데이터 보기", page_icon="📄", layout="wide")

df = load_data()

st.title("📄 Steam 데이터 보기")

st.markdown("""
Steam 게임 데이터를 확인하고, 가격대나 할인율에 따라 게임을 탐색할 수 있습니다.
""")

price_filter = st.multiselect(
    "💰 가격대 선택",
    options=list(df["가격대"].dropna().unique()),
    default=list(df["가격대"].dropna().unique())
)

discount_filter = st.multiselect(
    "🏷️ 할인율 구간 선택",
    options=list(df["할인율구간"].dropna().unique()),
    default=list(df["할인율구간"].dropna().unique())
)

filtered = df[
    df["가격대"].isin(price_filter)
    & df["할인율구간"].isin(discount_filter)
]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("선택된 게임 수", f"{len(filtered):,}개")

with col2:
    st.metric("평균 긍정 리뷰율", f"{filtered['positive_rate'].mean():.1f}%")

with col3:
    st.metric("평균 흥행점수", f"{filtered['흥행점수'].mean():.1f}")

show = filtered.rename(columns={
    "name": "게임명",
    "developer": "개발사",
    "publisher": "배급사",
    "positive": "긍정 리뷰",
    "negative": "부정 리뷰",
    "owners": "추정 보유자 수",
    "price_won": "가격($)",
    "discount": "할인율(%)",
    "ccu": "동시 접속자",
    "average_forever": "평균 플레이 시간",
    "positive_rate": "긍정 리뷰율",
    "흥행점수": "흥행점수"
})

columns = [
    "게임명",
    "개발사",
    "배급사",
    "추정 보유자 수",
    "가격($)",
    "할인율(%)",
    "긍정 리뷰율",
    "동시 접속자",
    "평균 플레이 시간",
    "흥행점수"
]

st.dataframe(show[columns], use_container_width=True, height=600)
