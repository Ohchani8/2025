import streamlit as st
import random

st.set_page_config(page_title="아이돌 MBTI 궁합 테스트", page_icon="💕", layout="centered")

# 아이돌 MBTI 데이터 (정원, 홍승한 먼저)
idol_mbti = {
    "정원 (ENHYPEN)": "ESTJ",
    "홍승한": "INFP",
    "정국 (BTS)": "INTP",
    "뷔 (BTS)": "ENFP",
    "아이유": "INFJ",
    "태연 (소녀시대)": "ESFJ",
    "희승 (ENHYPEN)": "ISTP",
    "제이 (ENHYPEN)": "ENTP",
    "제이크 (ENHYPEN)": "ISTJ",
    "성훈 (ENHYPEN)": "ISTJ",
    "선우 (ENHYPEN)": "ENFP",
    "니키 (ENHYPEN)": "ESFP",
    "RM (BTS)": "ENTJ",
    "효연 (소녀시대)": "INTJ",
    "수호 (EXO)": "ISFJ",
    "진 (BTS)": "ISFP",
    "차은우 (ASTRO)": "ESTP",
    "재현 (NCT)": "ENFJ",
}

# 아이돌 이미지 URL (정원, 홍승한 우선)
idol_images = {
    "정원 (ENHYPEN)": "https://i.namu.wiki/i/dAsH-Nf8efl3oJm8i0VJDA.webp",
    "홍승한": "https://i.namu.wiki/i/TU4hQ2cxAE4Z2aH3L6n8VA.webp",
    "정국 (BTS)": "https://i.namu.wiki/i/KB9eB1EoK7C0HhuGnTwDJQ.webp",
    "뷔 (BTS)": "https://i.namu.wiki/i/RodMmM2uFvVobHjS6OJj8Q.webp",
    "아이유": "https://i.namu.wiki/i/ArWc3ye9V67iPpiZxkFOSw.webp",
    "태연 (소녀시대)": "https://i.namu.wiki/i/9JZn9K8uW0SefB57V6rjLw.webp",
    "희승 (ENHYPEN)": "https://i.namu.wiki/i/Lbi6hZy3s3fwN3rLOfYf2A.webp",
    "제이 (ENHYPEN)": "https://i.namu.wiki/i/U9E0QjycM9aLCxqV8GfLPQ.webp",
    "제이크 (ENHYPEN)": "https://i.namu.wiki/i/IoK53B5vhT-9sRGRphhXXQ.webp",
    "성훈 (ENHYPEN)": "https://i.namu.wiki/i/MjWZMz6M1u0cWQt8uINnOA.webp",
    "선우 (ENHYPEN)": "https://i.namu.wiki/i/HC9B0jO8-bBhkgqE-xtWig.webp",
    "니키 (ENHYPEN)": "https://i.namu.wiki/i/jEYmjvBslfRNdDlS9t87-Q.webp",
    "RM (BTS)": "https://i.namu.wiki/i/KsY5aDgA_1ATxD8gRxm-fQ.webp",
    "효연 (소녀시대)": "https://i.namu.wiki/i/_h8xXgrvGJcDch9d0jvh9Q.webp",
    "수호 (EXO)": "https://i.namu.wiki/i/Gyy5zzdV3QpLdvfKXz5PAg.webp",
    "진 (BTS)": "https://i.namu.wiki/i/vgT9tJ19zN_3Jm4AwEJ-tQ.webp",
    "차은우 (ASTRO)": "https://i.namu.wiki/i/FaD20JZnau2Y6HTbD1pOZw.webp",
    "재현 (NCT)": "https://i.namu.wiki/i/Cpl4WlTfKzjcZEDnEhzZog.webp",
}

# 궁합 설명
compatibility = {
    ("INTP", "ENFP"): "찰떡궁합! 서로 부족한 부분을 잘 채워줍니다 💖",
    ("ENFP", "INFJ"): "운명적인 조합! 서로 깊이 이해합니다 🌌",
    ("ISTJ", "ESFP"): "서로 정반대라 끌리기도, 힘들기도 해요 ⚖️",
    ("ISTP", "ENFP"): "자유로운 영혼끼리 즐겁게 지낼 수 있어요 🎶",
    ("ESFJ", "INFP"): "따뜻한 관계를 만들 수 있습니다 🌷",
    ("ENTP", "INFJ"): "아이디어 뱅크와 깊은 영혼의 만남 ✨",
    ("ESTJ", "ISFP"): "현실적이고 따뜻한 조합 🏡",
    ("ENTJ", "INTP"): "리더와 전략가의 완벽한 케미 💎",
    ("ENFJ", "INFP"): "이상과 공감을 함께 나눌 수 있어요 🌈",
}

# 궁합 점수 랜덤 생성
def get_score(user_mbti, idol_mbti):
    random.seed(user_mbti + idol_mbti)
    return random.randint(60, 100)

# UI
st.title("💞 아이돌 MBTI 궁합 테스트 💞")
st.write("👉 당신의 MBTI를 선택하면, 아이돌과의 궁합을 확인할 수 있어요!")

user_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    ["INTP","ENTP","INFJ","ENFP","ISTJ","ISFJ","ISTP","ISFP",
     "ESTP","ESFP","ESTJ","ESFJ","ENTJ","ENFJ","INTJ","INFP"]
)

if st.button("궁합 보기"):
    st.subheader(f"✨ 당신({user_mbti})과 아이돌의 궁합 ✨")

    for name, mbti in idol_mbti.items():
        # 궁합 메시지
        message = "평범한 조합이지만 노력 여하에 따라 좋은 관계가 될 수 있어요 😊"
        if (user_mbti, mbti) in compatibility:
            message = compatibility[(user_mbti, mbti)]
        elif (mbti, user_mbti) in compatibility:
            message = compatibility[(mbti, user_mbti)]

        # 궁합 점수
        score = get_score(user_mbti, mbti)

        # 출력 (카드 스타일)
        st.markdown(
            f"""
            <div style="padding:15px; margin:12px 0;
                        border-radius:15px; background-color:#fef9ff;
                        border:2px solid #f3c4fb;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                <img src="{idol_images.get(name, 'https://cdn-icons-png.flaticon.com/512/149/149071.png')}" 
                     width="120" style="border-radius:15px; margin-bottom:10px;" />
                <h4 style="margin:0;">{name} ({mbti})</h4>
                <p style="margin:4px 0 0 0;">👉 {message}</p>
                <p style="font-weight:bold; color:#d63384;">궁합 점수: {score}%</p>
            </div>
            """,
            unsafe_allow_html=True
        )
