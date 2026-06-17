import streamlit as st
import matplotlib.pyplot as plt
from utils import apply_custom_style, load_and_preprocess_data, draw_sidebar_footer, set_matplotlib_style

st.set_page_config(page_title="Price Analysis - SteamScope", page_icon="💰", layout="wide")
apply_custom_style()
set_matplotlib_style()

df = load_and_preprocess_data()

st.title("💰 탐구 Q2. 게임 가격은 판매량에 영향을 줄까?")
st.markdown("가격 장벽이 유저들의 실질적인 구매 욕구 저하로 이어지는지 다변량 상관관계 분석을 수행합니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📉 가격(KRW) vs 판매량 상관관계 산점도")
    # 산점도 최적화 규칙 적용 (최대 5,000개 샘플링링)
    sample = df.sample(min(5000, len(df)), random_state=42)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(sample['price_krw'], sample['owners_low'] / 10000, alpha=0.5, color='#00ADB5', edgecolors='none')
    ax.set_xlabel("출시 가격 (원)")
    ax.set_ylabel("추정 판매량 (만 단위)")
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("📊 가격 그룹 파티션별 평균 판매량")
    # 가격 그룹 인덱싱 연산
    def label_price_group(p):
        if p == 0: return '01. 무료(F2P)'
        elif p <= 10000: return '02. 1만원 이하'
        elif p <= 30000: return '03. 1만~3만원'
        elif p <= 60000: return '04. 3만~6만원'
        else: return '05. 6만원 초과(AAA)'
        
    df['price_group'] = df['price_krw'].apply(label_price_group)
    price_group_analysis = df.groupby('price_group')['owners_low'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(price_group_analysis['price_group'], price_group_analysis['owners_low'] / 10000, color='#FFD369')
    ax.set_ylabel("평균 판매량 (만 단위)")
    plt.xticks(rotation=20)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown("---")
st.subheader("🆓 무료 게임(0원) 정밀 서브 스케일 분석")
free_games = df[df['price_krw'] == 0]
st.write(f"현재 등록된 총 무료 게임 수: **{len(free_games):,}** 개")

fig, ax = plt.subplots(figsize=(8, 2.5))
ax.boxplot(free_games['owners_low'] / 10000, vert=False, patch_artist=True,
           boxprops=dict(facecolor='#00ADB5', color='#00ADB5'),
           medianprops=dict(color='#FFD369'))
ax.set_xlabel("무료 게임 판매량 분포 외상치 (만 단위)")
plt.tight_layout()
st.pyplot(fig)

st.markdown("""
> **🔬 데이터 분석 결론:**
> 가격과 판매량 산점도 분석 결과 일반적인 수요-공급 원리와 달리 **'비쌀수록 안 팔린다'는 가설은 성립하지 않았습니다.**
> 오히려 3만~6만 원 혹은 6만 원 이상의 AAA급 프리미엄 게임들의 평균 판매량이 1만 원 이하의 저가 인디 게임들보다 월등히 높은 경향을 보입니다. 유저들은 가격보다는 게임의 퀄리티와 IP 가치에 기반한 가치 소비를 지향함을 증명합니다.
""")

draw_sidebar_footer()
