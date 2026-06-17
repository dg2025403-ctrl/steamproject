# 🎮 SteamScope Analytics
> **데이터로 증명하는 Steam 게임 시장 분석 플랫폼**

Kaggle의 Steam 빅데이터를 활용하여 게임 시장의 다양한 상관관계를 분석하고 시각화하는 데이터 탐구 중심의 Web Dashboard 프로젝트입니다. 학교 수행평가 제출 및 Streamlit Cloud 배포를 목적으로 최적화되었습니다.

---

## 📌 1. 프로젝트 소개 & 목표
본 프로젝트는 단순한 게임 소개나 순위 나열을 넘어, 실제 Steam 마켓의 데이터를 기반으로 가격, 평점, 할인율, 플레이 타임 등이 실제 게임의 '흥행(판매량)'에 어떤 영향을 미치는지 통계적으로 분석합니다. Netflix와 Steam의 다크 모드 감성을 결합한 UI 디자인과 대용량 데이터 처리 기법을 적용했습니다.

## ❓ 2. 핵심 탐구 질문
* **Q1.** 어떤 게임이 시장에서 가장 많이 팔릴까?
* **Q2.** 게임 가격은 판매량에 영향을 줄까? (비쌀수록 안 팔릴까?)
* **Q3.** 평점(리뷰 긍정 비율)이 높을수록 더 많이 팔릴까?
* **Q4.** 오래 플레이되는 게임이 동시 접속자 수나 흥행과 어떤 관계가 있을까?
* **Q5.** 할인은 판매량에 실질적인 영향을 줄까?
* **Q6.** 동시 접속자 수(CCU)는 판매량과 어떤 정량적 관계가 있을까?

## ✨ 3. 주요 기능
* **통합 대시보드:** 핵심 KPI 지표(총 게임 수, 평균 가격, 평균 평점 등) 및 Top 10 차트 시각화
* **다차원 데이터 분석:** 판매량, 가격, 평점, 플레이어, 할인율 별 상세 다변량 분석 및 시각화 제공
* **고급 게임 익스플로러:** 복합 필터링(개발사, 퍼블리셔, 가격, 평점, 할인율 등) 기반 동적 데이터 검색 (최대 300개 제한 최적화)
* **고성능 최적화:** `@st.cache_data`, `usecols`, `dtype` 고정, 5,000개 데이터 샘플링 산점도를 통한 성능 극대화

## 🛠 4. 기술 스택
* **Language:** Python 3.10+
* **Framework:** Streamlit
* **Data Science:** Pandas
* **Visualization:** Matplotlib

## 📂 5. 프로젝트 구조
```text
steamproject/
├── app.py
├── utils.py
├── all_data.csv (데이터 파일)
├── requirements.txt
├── README.md
└── pages/
    ├── 1_🏠_Dashboard.py
    ├── 2_🏆_Sales_Analysis.py
    ├── 3_💰_Price_Analysis.py
    ├── 4_⭐_Rating_Analysis.py
    ├── 5_👥_Player_Analysis.py
    ├── 6_🎁_Discount_Analysis.py
    └── 7_🔍_Game_Explorer.py

    자료 출처 - https://www.kaggle.com/datasets/fmpugliese/steam-all-games-data
