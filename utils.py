import streamlit as st
import pandas as pd
import numpy as np

# 글로벌 스타일 및 카드 디자인 폰트 CSS 정의
def apply_custom_style():
    st.markdown("""
        <style>
        /* 기본 배경 및 글자색 정의 */
        .stApp {
            background-color: #0E1117;
            color: #FFFFFF;
        }
        /* 사이드바 스타일링 */
        [data-testid="stSidebar"] {
            background-color: #1E1E2F;
        }
        /* 메트릭 카드 컨테이너 디자인 */
        .metric-card {
            background-color: #1E1E2F;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            border-left: 5px solid #00ADB5;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 15px;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0, 173, 181, 0.4);
        }
        .metric-title {
            font-size: 0.9rem;
            color: #8B949E;
            margin-bottom: 5px;
            font-weight: 600;
        }
        .metric-value {
            font-size: 1.6rem;
            color: #FFD369;
            font-weight: bold;
        }
        /* 푸터 스타일 */
        .footer {
            text-align: center;
            padding: 30px 10px 10px 10px;
            font-size: 0.85rem;
            color: #6E7681;
            border-top: 1px solid #1E1E2F;
            margin-top: 50px;
        }
        /* 상단 여백 조절 */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def draw_metric_card(title, value):
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

# Matplotlib 전역 스타일 설정 함수
def set_matplotlib_style():
    import matplotlib.pyplot as plt
    plt.rcParams['figure.facecolor'] = '#0E1117'
    plt.rcParams['axes.facecolor'] = '#1E1E2F'
    plt.rcParams['text.color'] = '#FFFFFF'
    plt.rcParams['axes.labelcolor'] = '#FFFFFF'
    plt.rcParams['xtick.color'] = '#FFFFFF'
    plt.rcParams['ytick.color'] = '#FFFFFF'
    plt.rcParams['grid.color'] = '#2E2E3F'
    plt.rcParams['axes.edgecolor'] = '#2E2E3F'

@st.cache_data(show_spinner=False)
def load_and_preprocess_data():
    # 대용량 데이터 최적화를 위한 필수 컬럼 및 데이터 타입 정의
    cols = [
        'appid', 'name', 'developer', 'publisher', 'positive', 'negative', 
        'userscore', 'owners', 'average_forever', 'average_2weeks', 
        'median_forever', 'median_2weeks', 'price', 'initialprice', 'discount', 'ccu'
    ]
    
    dtypes = {
        'appid': 'int32',
        'name': 'string',
        'developer': 'string',
        'publisher': 'string',
        'positive': 'float64',
        'negative': 'float64',
        'userscore': 'float64',
        'owners': 'string',
        'average_forever': 'float64',
        'average_2weeks': 'float64',
        'median_forever': 'float64',
        'median_2weeks': 'float64',
        'price': 'float64',
        'initialprice': 'float64',
        'discount': 'float64',
        'ccu': 'float64'
    }
    
    # 1. 데이터 로드 (low_memory 및 usecols 최적화)
    try:
        df = pd.read_csv("all_data.csv", usecols=cols, dtype=dtypes, low_memory=False)
    except Exception:
        # 데이터가 없을 때를 대비한 모크 데이터 빌더 (안전성 확보)
        np.random.seed(42)
        n = 10000
        mock_owners = ['0 .. 20,000', '20,000 .. 50,000', '1,000,000 .. 2,000,000', '10,000,000 .. 20,000,000']
        df = pd.DataFrame({
            'appid': np.arange(1, n+1),
            'name': [f"Game {i}" for i in range(1, n+1)],
            'developer': [f"Developer {i%50}" for i in range(1, n+1)],
            'publisher': [f"Publisher {i%30}" for i in range(1, n+1)],
            'positive': np.random.randint(0, 50000, size=n).astype(float),
            'negative': np.random.randint(0, 10000, size=n).astype(float),
            'userscore': np.random.randint(0, 100, size=n).astype(float),
            'owners': np.random.choice(mock_owners, size=n),
            'average_forever': np.random.randint(0, 5000, size=n).astype(float),
            'average_2weeks': np.random.randint(0, 500, size=n).astype(float),
            'median_forever': np.random.randint(0, 3000, size=n).astype(float),
            'median_2weeks': np.random.randint(0, 200, size=n).astype(float),
            'price': np.random.choice(
