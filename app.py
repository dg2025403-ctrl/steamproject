import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(
    page_title="Steam 흥행 요인 분석",
    page_icon="🎮",
    layout="wide"
)

df = load_data()

# -----------------------------
# 디자인 CSS
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #1e3a8a 0%, #0f172a 35%, #020617 100%);
    color: white;
}

.hero {
    padding: 38px 34px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(59,130,246,0.28), rgba(147,51,234,0.22));
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 0 35px rgba(59,130,246,0.25);
    margin-bottom: 25px;
}

.hero-title {
    font-size: 46px;
    font-weight: 900;
    line-height: 1.15;
    color: #ffffff;
    margin-bottom: 12px;
}

.hero-sub {
    font-size: 18px;
    color: #cbd5e1;
    line-height: 1.7;
}

.badge {
    display: inline-block;
    padding: 8px 14px;
    margin-right: 8px;
    margin-bottom: 10px;
    border-radius: 999px;
    background: rgba(14,165,233,0.18);
    border: 1px solid rgba(125,211,252,0.25);
    color: #e0f2fe;
    font-size: 14px;
    font-weight: 700;
}

.card {
    padding: 22px;
    border-radius: 22px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 24px rgba(124,58,237,0.18);
    height: 100%;
}

.card-title {
    font-size: 21px;
    font-weight: 800;
    color: #e0e7ff;
    margin-bottom: 8px;
}

.card-text {
    font-size: 15px;
    color: #cbd5e1;
    line-height: 1.6;
}

.section-title {
    font-size: 28px;
    font-weight: 900;
    color: #ffffff;
    margin-top: 34px;
    margin-bottom: 14px;
}

.small-text {
    color: #94a3b8;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 히어로 영역
# -----------------------------
st.markdown("""
<div class="hero">
    <div>
        <span class="badge">Steam Big Data</span>
        <span class="badge">Game Success Analysis</span>
        <span class="badge">Data Visualization</span>
    </div>
    <div class="hero-title">
        🎮 Steam 게임 흥행 요인 분석 대시보드
    </div>
    <div class="hero-sub">
        글로벌 PC 게임 플랫폼 Steam 데이터를 바탕으로, 게임의 흥행에 영향을 미치는
        가격, 리뷰, 할인율, 동시 접속자, 평균 플레이 시간의 관계를 분석합니다.
        단순 인기 순위가 아니라, 흥행에 영향을 주는 핵심 요인을 데이터로 추정하고 검증하는 프로젝트입니다.
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 핵심 지표
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("전체 게임 수", f"{len(df):,}개")

with col2:
    st.metric("평균 긍정 리뷰율", f"{df['positive_rate'].mean():.1f}%")

with col3:
    st.metric("평균 가격", f"${df['price_won'].mean():.2f}")

with col4:
    st.metric("최고 동시 접속자", f"{int(df['ccu'].max()):,}명")

# -----------------------------
# 분석 질문 카드
# -----------------------------
st.markdown('<div class="section-title">🧪 핵심 탐구 질문</div>', unsafe_allow_html=True)

q1, q2 = st.columns(2)

with q1:
    st.markdown("""
    <div class="card">
        <div class="card-title">💰 가격의 역설</div>
        <div class="card-text">
        게임이 비싸면 정말 덜 팔릴까?<br>
        가격대별 흥행점수와 추정 보유자 수를 비교하여,
        적정 가격대가 흥행에 어떤 영향을 주는지 분석합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with q2:
    st.markdown("""
    <div class="card">
        <div class="card-title">⭐ 리뷰의 가치</div>
        <div class="card-text">
        평점이 높으면 무조건 대박 게임이 될까?<br>
        긍정 리뷰율과 흥행점수의 상관관계를 확인하여,
        사용자 평가가 시장 성과와 어떤 관계를 갖는지 분석합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

q3, q4 = st.columns(2)

with q3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎮 유저 잔존율</div>
        <div class="card-text">
        오래 플레이되는 게임이 실제로 더 성공할까?<br>
        평균 플레이 시간과 동시 접속자 수를 통해
        게임의 지속성과 흥행 사이의 관계를 분석합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

with q4:
    st.markdown("""
    <div class="card">
        <div class="card-title">🏷️ 마케팅 효과</div>
        <div class="card-text">
        할인을 많이 하면 실제로 판매량이 폭발할까?<br>
        할인율 구간별 흥행점수를 비교하여
        할인 전략의 효과를 데이터로 검증합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# 흥행점수 설명
# -----------------------------
st.markdown('<div class="section-title">🧮 새롭게 만든 데이터: 흥행점수</div>', unsafe_allow_html=True)

left, right = st.columns([1.1, 1])

with left:
    st.markdown("""
    <div class="card">
        <div class="card-title">흥행점수란?</div>
        <div class="card-text">
        기존 Steam 데이터에 존재하는 추정 보유자 수, 전체 리뷰 수, 긍정 리뷰율,
        동시 접속자 수, 평균 플레이 시간을 조합하여 새롭게 만든 지표입니다.
        단일 수치만 보는 것이 아니라 여러 흥행 요인을 함께 반영합니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.code("""
긍정 리뷰율 = positive / (positive + negative) × 100

흥행점수 =
log(추정 보유자 수) × 35
+ log(전체 리뷰 수) × 25
+ 긍정 리뷰율 × 0.3
+ log(동시 접속자 수) × 20
+ log(평균 플레이 시간) × 10
""")

with right:
    top_games = df.sort_values("흥행점수", ascending=False).head(8)

    fig = px.bar(
        top_games,
        x="흥행점수",
        y="name",
        orientation="h",
        title="현재 데이터 기준 흥행점수 TOP 8",
        template="plotly_dark"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=430,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 안내
# -----------------------------
st.markdown('<div class="section-title">📌 페이지 안내</div>', unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.info("📄 데이터 보기\n\nSteam 원본 데이터를 필터링하며 확인")

with p2:
    st.success("💰 가격 분석\n\n가격대별 흥행 경향 분석")

with p3:
    st.warning("⭐ 리뷰 분석\n\n긍정 리뷰율과 흥행 관계 분석")

with p4:
    st.error("🚀 흥행요인 분석\n\n할인율, 동접자, 플레이 시간 종합 분석")
