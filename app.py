import streamlit as st
import pandas as pd
import numpy as np
from time import sleep

# 페이지 기본 설정
st.set_page_config(

    page_icon = "🎬",
    page_title = "배포",
    layout = "wide",
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("영화 추천 시스템")
st.subheader("영화 추천 시스템")

# 사용자 입력 섹션
st.sidebar.header("사용자 입력")
user_name = st.sidebar.text_input("이름을 입력하세요")
favorite_genre = st.sidebar.selectbox("좋아하는 장르를 선택하세요", ["액션", "코미디", "드라마", "공포", "SF"])
rating_threshold = st.sidebar.slider("최소 평점", 0.0, 10.0, 7.0, 0.1)

# 더미 영화 데이터
movies_data = pd.DataFrame({
    "제목": ["인셉션", "매트릭스", "인터스텔라", "어벤져스", "겨울왕국"],
    "장르": ["SF", "SF", "SF", "액션", "애니메이션"],
    "평점": [8.8, 8.7, 8.6, 8.4, 7.4]
})

# 영화 추천 로직 (간단한 예시)
recommended_movies = movies_data[(movies_data["장르"] == favorite_genre) & (movies_data["평점"] >= rating_threshold)]

# 결과 표시
st.subheader(f"{user_name}님을 위한 영화 추천")
if not recommended_movies.empty:
    st.table(recommended_movies)
else:
    st.write("조건에 맞는 영화가 없습니다. 다른 장르나 낮은 평점을 선택해보세요.")

# 데이터 시각화
st.subheader("장르별 평균 평점")
genre_ratings = movies_data.groupby("장르")["평점"].mean().reset_index()
st.bar_chart(genre_ratings.set_index("장르"))

# 인터랙티브 요소
if st.button("랜덤 영화 추천"):
    random_movie = movies_data.sample(1)
    st.write(f"오늘의 추천 영화: {random_movie['제목'].values[0]} (평점: {random_movie['평점'].values[0]})")

# 고급 차트 예시 (plotly 사용)
import plotly.express as px

fig = px.scatter(movies_data, x="제목", y="평점", size="평점", color="장르", hover_name="제목")
st.plotly_chart(fig)