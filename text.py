import streamlit as st
import random

st.set_page_config(page_title="아이돌 MBTI 궁합 테스트", page_icon="💕", layout="centered")

# 스타일 (폰트 + 색상)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Jua', sans-serif;
    }
    .title {
        color: #ff4b82;
        text-align: center;
        font-size: 36px;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #7a4bff;
        font-size: 18px;
        margin-bottom: 30px;
    }
    .card {
        padding: 15px;
        margin: 15px 0;
        border-radius: 15px;
        background: linear-gradient(135deg, #ffe6f0, #f3e5ff);
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .idol-info {
        flex: 1;
    }
    .idol-name {
        font-size: 20px;
        color: #ff4b82;
        margin-bottom: 5px;
    }
    .idol-text {
        font-size: 16px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# 아이돌 MBTI 데이터
idol_mbti = {
    "정국 (BTS)": "INTP",
    "뷔 (BTS)": "ENFP",
    "아이유": "INFJ",
    "태연 (소녀시대)": "ESFJ",
    "희승 (ENHYPEN)": "ISTP",
    "제이 (ENHYPEN)": "ENTP",
    "제이크 (ENHYPEN)": "ISTJ",
    "성훈 (ENHYPEN)": "ISTJ",
    "선우 (ENHYPEN)": "ENFP",
    "정원 (ENHYPEN)": "ESTJ",
    "니키 (ENHYPEN)": "ESFP",
    "RM (BTS)": "ENTJ",
    "홍승한": "INFP",
    "효연 (소녀시대)": "INTJ",
    "수호 (EXO)": "ISFJ",
    "진 (BTS)": "ISFP",
    "차은우 (ASTRO)": "ESTP",
    "재현 (NCT)": "ENFJ",
}

# 아이돌 이미지 URL
idol_images = {
    "정국 (BTS)": "https://i.namu.wiki/i/KB9eB1EoK7C0HhuGnTwDJQ.webp",
    "뷔 (BTS)": "https://i.namu.wiki/i/RodMmM2uFvVobHjS6OJj8Q.webp",
    "아이유": "https://i.namu.wiki/i/ArWc3ye9V67iPpiZxkFOSw.webp",
    "태연 (소녀시대)": "https://i.namu.wiki/i/9JZn9K8uW0SefB57V6rjLw.webp",
    "희승 (ENHYPEN)": "https://i.namu.wiki/i/Lbi6hZy3s3fwN3rLOfYf2A.webp",
    "제이 (ENHYPEN)": "https://i.namu.wiki/i/U9E0QjycM9aLCxqV8GfLPQ.webp",
    "제이크 (ENHYPEN)": "https://i.namu.wiki/i/IoK53B5vhT-9sRGRphhXXQ.webp",
    "성훈 (ENHYPEN)": "https://i.namu.wiki/i/MjWZMz6M1u0cWQt8uINnOA.webp",
    "선우 (ENHYPEN)": "https://i.namu.wiki/i/HC9B0jO8-bBhkgqE-xtWig.webp",
    "정원 (ENHYPEN)": "https://i.namu.wiki/i/dAsH-Nf8efl3oJm8i0VJDA.webp",
    "니키 (ENHYPEN)": "https://i.namu.wiki/i/jEYmjvBslfRNdDlS9t87-Q.webp",
    "RM (BTS)": "https://i.namu.wiki/i/KsY5aDgA_1ATxD8gRxm-fQ.webp",
    "홍승한": "https://i.namu.wiki/i/TU4hQ2cxAE4Z2aH3L6n8VA.webp",
    "효연 (소녀시대)": "https://i.namu.wiki/i/_h8xXgrvGJcDch9d0jvh9Q.webp",
    "수호 (EXO)": "https://i.namu.wiki/i/Gyy5zzdV3QpLdvfKXz5PAg.webp",
    "진 (BTS)": "https://i.namu.wiki/i/vgT9tJ19zN_3Jm4AwEJ-tQ.webp",
    "차은우 (ASTRO)": "https://i.namu.wiki/i/FaD20JZnau2Y6HTbD1pOZw.webp",
    "재현 (NCT)": "https://i.namu.wiki/i/Cpl4WlTfKzjcZEDnEhzZog.webp",
}

# 궁합 메시지
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

# 헤더
st.markdown("<div class='title'>💞 아이돌 MBTI 궁합 테스트 💞</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>👉 당신의 MBTI를 선택하면, 최애 아이돌과의 궁합을 확인할 수 있어요!</div>", unsafe_allow_html=True)

# 사용자 MBTI 입력
user_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    ["INTP","ENTP","INFJ","ENFP","ISTJ","ISFJ","ISTP","ISFP",
     "ESTP","ESFP","ESTJ","ESFJ","ENTJ","ENFJ","INTJ","INFP"]
)

if st.button("✨ 궁합 보기 ✨"):
    st.subheader(f"당신({user_mbti})과 아이돌 궁합 결과 💕")

    for name, mbti in idol_mbti.items():
        # 기본 메시지
        message = "평범한 조합이지만 노력 여하에 따라 좋은 관계가 될 수 있어요 😊"
        if (user_mbti, mbti) in compatibility:
            message = compatibility[(user_mbti, mbti)]
        elif (mbti, user_mbti) in compatibility:
            message = compatibility[(mbti, user_mbti)]

        # 랜덤 궁합 점수
        score = random.randint(70, 100)
        emoji = "💖" if score > 90 else "✨" if score > 80 else "😊"

        # 이미지 URL
        img_url = idol_images.get(name, "https://cdn-icons-png.flaticon.com/512/149/149071.png")

        # 카드 출력
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(img_url, width=120, caption=name)
        with col2:
            st.markdown(
                f"""
                <div class="card">
                    <div class="idol-info">
                        <div class="idol-name">{name} ({mbti})</div>
                        <div class="idol-text">👉 {message}</div>
                        <div class="idol-text">❤️ 궁합 점수: <b>{score}%</b> {emoji}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
