import streamlit as st

# 메인 환경 설정 (가장 먼저 실행되어야 함)
st.set_page_config(
    page_title="SteamScope Analytics",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils import apply_custom_style, draw_sidebar_footer, load_and_preprocess_data

# 디자인 스타일 시트 적용
apply_custom_style()

# 데이터 사전 로드 (캐싱 및 속도 최적화 확인용)
with st.spinner("Steam 대용량 데이터 분석 인프라 초기화 중..."):
    df = load_and_preprocess_data()

st.title("🎮 SteamScope Analytics")
st.subheader("데이터로 증명하는 Steam 게임 시장 분석 플랫폼")

st.markdown("""
---
### 📈 본 웹 애플리케이션의 탐구 방향성
본 프로젝트는 글로벌 PC 게임 플랫폼인 **Steam**의 대규모 마켓 플레이스 데이터를 다각도로 정량화하여, 시장에서 성공하는 게임의 규칙을 데이터로 도출하는 것을 목적으로 합니다. 

좌측 사이드바의 **Navigation 메뉴**를 활용하여 각 탐구 질문별 데이터 인사이트와 통계적 시각화를 자유롭게 탐색할 수 있습니다.

### 🔬 6대 핵심 탐구 과제 (Research Questions)
1. **🏆 Sales Analysis:** 어떤 장르 및 타이틀의 게임이 시장을 지배하는가?
2. **💰 Price Analysis:** 게임의 가격은 유저의 구매 전환율(판매량)을 위축시키는가?
3. **⭐ Rating Analysis:** 유저 평점과 긍정 리뷰 비율은 흥행의 절대적인 척도인가?
4. **👥 Player Analysis:** 롱런하는 게임(플레이 시간, 동시 접속자)이 마켓에서도 성공하는가?
5. **🎁 Discount Analysis:** 할인은 판매 프로모션으로서 유의미한 상관관계를 가지는가?
6. **🔍 Game Explorer:** 탐구에 사용된 로우 데이터를 조건별로 필터링하여 검증하는 검색 엔진.
""")

st.info("💡 사이드바의 각 분석 메뉴를 클릭하시면 본격적인 데이터 시각화 리포트가 시작됩니다.")

# 사이드바 하단 정보 출력
draw_sidebar_footer()
