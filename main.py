import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
job_recommendations = {
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "소프트웨어 아키텍트"],
    "ENTP": ["창업가", "광고 기획자", "기술 혁신가"],
    "INFJ": ["작가", "상담사", "인권 변호사"],
    "ESFP": ["이벤트 플래너", "배우", "마케팅 전문가"],
    # 필요한 MBTI 타입 계속 추가
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼")

st.title("💼 MBTI 기반 직업 추천 앱")

# MBTI 선택
mbti_list = list(job_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 추천 직업 표시
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 타입 추천 직업")
    for job in job_recommendations[selected_mbti]:
        st.write(f"- {job}")

# 추가 기능: 검색
search_job = st.text_input("관심 있는 직업 키워드로 검색해 보세요:")

if search_job:
    matched = [j for jobs in job_recommendations.values() for j in jobs if search_job in j]
    if matched:
        st.success(f"🔍 검색 결과: {', '.join(matched)}")
    else:
        st.warning("검색 결과가 없습니다.")

