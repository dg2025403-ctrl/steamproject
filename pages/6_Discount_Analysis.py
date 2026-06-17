import streamlit as st
import matplotlib.pyplot as plt
from utils import apply_custom_style, load_and_preprocess_data, draw_sidebar_footer, set_matplotlib_style

st.set_page_config(page_title="Discount Analysis - SteamScope", page_icon="🎁", layout="wide")
apply_custom_style()
set_matplotlib_style()

df = load_and_preprocess_data()

st.title("🎁 탐구 Q5. 할인은 판매량에 영향을 줄까?")
st.markdown("Steam 마케팅의 정수인 '할인율 프로모션' 전략이 실제로 유저들을 자극하여 대량 판매로 전환시키는지 검증합니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎁 적용 프로모션 할인율분포")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df['discount'], bins=15, color='#FFD369', edgecolor='#0E1117')
    ax.set_xlabel("현재 할인율 (%)")
    ax.set_ylabel("등록 건수")
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("📈 프로모션 할인율 vs 추정 판매량 상관관계")
    sample = df.sample(min(5000, len(df)), random_state=42)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(sample['discount'], sample['owners_low'] / 10000, alpha=0.4, color='#00ADB5', edgecolors='none')
    ax.set_xlabel("할인율 (%)")
    ax.set_ylabel("추정 판매량 (만 단위)")
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")
st.subheader("📊 할인율 구간 범주별 평균 누적 판매 격차 비교")

def label_discount_group(d):
    if d == 0: return '❌ 할인 없음'
    elif d <= 30: return '🔍 라이트 할인 (1~30%)'
    elif d <= 60: return '🔥 미디엄 세일 (31~60%)'
    else: return '🚀 울트라 폭탄세일 (61%+)'

df['discount_group'] = df['discount'].apply(label_discount_group)
discount_analysis = df.groupby('discount_group')['owners_low'].mean().reindex([
    '❌ 할인 없음', '🔍 라이트 할인 (1~30%)', '🔥 미디엄 세일 (31~60%)', '🚀 울트라 폭탄세일 (61%+)'
]).reset_index()

fig, ax = plt.subplots(figsize=(7, 3))
ax.bar(discount_analysis['discount_group'], discount_analysis['owners_low'] / 10000, color='#10ac84')
ax.set_ylabel("평균 판매량 (만 단위)")
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
> **🔬 데이터 분석 결론:**
> 데이터 가공 결과, **할인율이 극대화되는 구간(61% 이상 폭탄 세일 위주)에서 평균 판매량이 점진적으로 팽창함**을 파악할 수 있었습니다. 
> 반면, 어설픈 라이트 세일(30% 미만) 구간은 세일을 전혀 진행하지 않는 프리미엄 브랜드 타이틀 집단보다 평균 판매 지표가 저조한 역설이 증명되므로, 스팀 플랫폼 내부 마케팅 기획 시에는 확실하고 과감한 대형 디스카운트 정책 투입이 효과적임을 증명합니다.
""")

draw_sidebar_footer()
