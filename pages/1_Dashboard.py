import streamlit as st
import matplotlib.pyplot as plt
from utils import apply_custom_style, load_and_preprocess_data, draw_metric_card, draw_sidebar_footer, set_matplotlib_style

st.set_page_config(page_title="Dashboard - SteamScope", page_icon="🎮", layout="wide")
apply_custom_style()
set_matplotlib_style()

df = load_and_preprocess_data()

st.title("🏠 통합 대시보드 (Dashboard)")
st.markdown("Steam 마켓의 전체적인 현황을 한눈에 파악할 수 있는 고수준 메트릭 지표와 분포 현황입니다.")

# 1. 상단 핵심 KPI 메트릭 배치 (주문 제작 카드 디자인)
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    draw_metric_card("🎮 전체 분석 게임 수", f"{len(df):,} 개")
with col2:
    draw_metric_card("💰 평균 게임 가격", f"{int(df['price_krw'].mean()):,} 원")
with col3:
    draw_metric_card("⭐ 평균 유저 평점", f"{df['rating_percent'].mean():.1f} / 100 점")
with col4:
    top_game = df.loc[df['owners_low'].idxmax(), 'name']
    draw_metric_card("🏆 최고 판매 추정 게임", str(top_game))
with col5:
    top_ccu = df.loc[df['ccu'].idxmax(), 'name']
    draw_metric_card("👥 최고 동시 접속 게임", str(top_ccu))
with col6:
    draw_metric_card("🎁 평균 프로모션 할인율", f"{df['discount'].mean():.1f} %")

st.markdown("---")

# 2. 메인 시각화 차트 배치 (미리 Groupby 연산 처리 적용)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📈 누적 판매량 TOP 10 게임")
    top10_sales = df.nlargest(10, 'owners_low')
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(top10_sales['name'], top10_sales['owners_low'] / 1_000_000, color='#00ADB5')
    ax.set_xlabel("추정 판매량 (백만 단위)")
    ax.invert_yaxis()
    plt.tight_layout()
    st.pyplot(fig)

with chart_col2:
    st.subheader("🎮 최다 출시 개발사 TOP 10")
    top10_dev = df['developer'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(top10_dev.index, top10_dev.values, color='#FFD369')
    ax.set_ylabel("출시 게임 수")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("🏢 대형 퍼블리셔 TOP 10")
    top10_pub = df['publisher'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(top10_pub.index, top10_pub.values, color='#A3CB38')
    ax.set_ylabel("퍼블리셔 등록 게임 수")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

with chart_col4:
    st.subheader("📊 Steam 게임 할인율 분포")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df['discount'], bins=20, color='#EA2027', edgecolor='#0E1117')
    ax.set_xlabel("할인율 (%)")
    ax.set_ylabel("게임 수")
    plt.tight_layout()
    st.pyplot(fig)

draw_sidebar_footer()
