import streamlit as st
from utils import apply_custom_style, load_and_preprocess_data, draw_sidebar_footer

st.set_page_config(page_title="Game Explorer - SteamScope", page_icon="🔍", layout="wide")
apply_custom_style()

df = load_and_preprocess_data()

st.title("🔍 다차원 게임 검색 및 데이터 익스플로러")
st.markdown("프로젝트 탐구 타당성 검증을 위해 본 분석에 활용된 데이터를 다양한 조건의 다중 복합 필터링 기능을 통해 직접 탐색할 수 있습니다.")

# 사이드바 혹은 메인 상단 배치용 필터 UI 설계
st.markdown("### 🎛️ 필터 제어 패널")
f_col1, f_col2, f_col3 = st.columns(3)
f_col4, f_col5, f_col6, f_col7 = st.columns(4)

with f_col1:
    search_keyword = st.text_input("🎯 게임명 검색 (키워드)", "")
with f_col2:
    # 결측치 처리된 고유값 정렬 리스트 구축
    dev_list = ["전체"] + sorted(df['developer'].dropna().unique().tolist())
    selected_dev = st.selectbox("🛠️ 개발사(Developer) 필터", dev_list)
with f_col3:
    pub_list = ["전체"] + sorted(df['publisher'].dropna().unique().tolist())
    selected_pub = st.selectbox("🏢 퍼블리셔(Publisher) 필터", pub_list)

with f_col4:
    min_p, max_p = int(df['price_krw'].min()), int(df['price_krw'].max())
    price_range = st.slider("💰 원화 가격 범위 설정", min_p, max_p, (min_p, max_p))
with f_col5:
    rating_range = st.slider("⭐ 유저 평점 범위 (%)", 0, 100, (0, 100))
with f_col6:
    discount_range = st.slider("🎁 프로모션 할인율 범위 (%)", 0, 100, (0, 100))
with f_col7:
    min_o, max_o = float(df['owners_low'].min()), float(df['owners_low'].max())
    owners_range = st.slider("🏆 최소 판매량 필터", min_o, max_o, (min_o, max_o))

# --- 동적 조건 필터링 알고리즘 전개 ---
filtered = df.copy()

if search_keyword:
    filtered = filtered[filtered['name'].str.contains(search_keyword, case=False, na=False)]

if selected_dev != "전체":
    filtered = filtered[filtered['developer'] == selected_dev]

if selected_pub != "전체":
    filtered = filtered[filtered['publisher'] == selected_pub]

filtered = filtered[
    (filtered['price_krw'] >= price_range[0]) & (filtered['price_krw'] <= price_range[1]) &
    (filtered['rating_percent'] >= rating_range[0]) & (filtered['rating_percent'] <= rating_range[1]) &
    (filtered['discount'] >= discount_range[0]) & (filtered['discount'] <= discount_range[1]) &
    (filtered['owners_low'] >= owners_range[0]) & (filtered['owners_low'] <= owners_range[1])
]

st.markdown("---")
st.subheader(f"📊 검색 및 필터 매칭 결과 (총 {len(filtered):,}개 타이틀 조회됨)")

# 컬럼 가독성 최적화를 위한 뷰포트 컬럼 선택 및 리네이밍
view_cols = {
    'appid': 'App ID',
    'name': '게임 타이틀명',
    'developer': '개발사',
    'publisher': '퍼블리셔',
    'owners': '기존 추정 범위',
    'owners_low': '최소 판매수량',
    'price_krw': '실제 판매가(₩)',
    'rating_percent': '긍정 평점(%)',
    'discount': '할인율(%)',
    'ccu': '동시접속자(CCU)'
}

output_df = filtered[list(view_cols.keys())].rename(columns=view_cols)

# 대용량 데이터프레임 오버헤드 방지를 위한 상위 최대 300개 출력 규칙 준수
st.dataframe(output_df.head(300), use_container_width=True)

st.caption("⚠️ 대용량 브라우저 렌더링 최적화 규칙에 의거하여 필터 매칭 데이터 중 상위 최대 300개 행(Row)만 가시화됩니다.")

draw_sidebar_footer()
