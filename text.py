import streamlit as st
import random
import datetime

st.set_page_config(page_title="아이돌 궁합 테스트", page_icon="💕", layout="centered")

# 아이돌 스타일 데이터 + 해시태그
idol_styles = {
    "정원 (ENHYPEN)": ("책임감 있는 리더", ["#리더", "#책임감"]),
    "희승 (ENHYPEN)": ("차분한 현실주의자", ["#차분", "#현실적"]),
    "제이 (ENHYPEN)": ("재치 있는 아이디어 뱅크", ["#유머", "#아이디어"]),
    "제이크 (ENHYPEN)": ("성실한 노력파", ["#노력", "#성실"]),
    "성훈 (ENHYPEN)": ("차분한 카리스마", ["#카리스마", "#차분"]),
    "선우 (ENHYPEN)": ("장난꾸러기 무드메이커", ["#장난꾸러기", "#무드메이커"]),
    "니키 (ENHYPEN)": ("열정 가득한 댄서", ["#댄서", "#열정"]),
    "RM (BTS)": ("지적인 리더", ["#지적", "#리더"]),
    "해찬 (NCT)": ("에너지 넘치는 분위기 메이커", ["#에너지", "#분위기메이커"]),
    "재현 (NCT)": ("따뜻한 공감러", ["#따뜻함", "#공감"]),
    "마크 (NCT)": ("열정 만렙 올라운더", ["#올라운더", "#열정"]),
    "유우시 (NCT WISH)": ("밝은 에너지 소년", ["#밝음", "#에너지"]),
    "리쿠 (NCT WISH)": ("따뜻한 미소 천사", ["#미소", "#따뜻함"]),
    "시온 (NCT WISH)": ("열정적인 무대 장인", ["#무대", "#열정"]),
    "차은우 (ASTRO)": ("비주얼 천재", ["#비주얼", "#천재"]),
    "카리나 (aespa)": ("카리스마 리더", ["#카리스마", "#리더"]),
    "윈터 (aespa)": ("청순한 보컬 요정", ["#청순", "#보컬"]),
    "닝닝 (aespa)": ("자유로운 영혼", ["#자유", "#영혼"]),
    "지젤 (aespa)": ("쿨한 매력녀", ["#쿨함", "#매력"]),
    "홍승한": ("따뜻한 감성형", ["#감성", "#따뜻함"]),
}

# 사용자 취향 선택지
user_styles = [
    "차분한 스타일",
    "에너지 넘치는 스타일",
    "리더형 스타일",
    "유머러스한 스타일",
    "예술적인 스타일",
    "따뜻한 스타일",
]

# 궁합 점수 생성
def get_score(user_choice, idol_style):
    random.seed(user_choice + idol_style)
    return random.randint(60, 100)

# 점수에 따른 궁합 유형
def get_relation(score):
    if score >= 90:
        return "찰떡궁합! 연애 케미 최고 💕"
    elif score >= 80:
        return "팀워크도 굿! 🤝"
    elif score >= 70:
        return "친구처럼 편안한 사이 🌷"
    else:
        return "서로 배울 점이 많아요 ✨"

# 카드 출력 함수
def show_card(name, style, tags, score, highlight=False):
    bg_color = "#fff0f6" if highlight else "#fef9ff"
    border_color = "#d63384" if highlight else "#f3c4fb"
    relation = get_relation(score)
    tags_html = " ".join([f"<span style='color:#555'>{tag}</span>" for tag in tags])
    st.markdown(
        f"""
        <div style="padding:15px; margin:12px 0;
                    border-radius:15px; background-color:{bg_color};
                    border:2px solid {border_color};
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.1); text-align:center;">
            <h4 style="margin:0;">{name}</h4>
            <p style="margin:4px 0 0 0;">🌟 스타일: {style}</p>
            <p style="margin:4px 0 0 0;">{tags_html}</p>
            <p style="margin:4px 0 0 0;">👉 {relation}</p>
            <p style="font-weight:bold; color:#d63384;">궁합 점수: {score}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.progress(score / 100)

# 특별 추천 로직
style_match = {
    "차분한 스타일": "희승 (ENHYPEN)",
    "에너지 넘치는 스타일": "해찬 (NCT)",
    "리더형 스타일": "RM (BTS)",
    "유머러스한 스타일": "제이 (ENHYPEN)",
    "예술적인 스타일": "닝닝 (aespa)",
    "따뜻한 스타일": "재현 (NCT)",
}

# UI
st.title("💞 아이돌 궁합 테스트 💞")
st.write("👉 당신의 취향 스타일을 고르고, 아이돌과의 궁합을 확인해보세요!")

user_name = st.text_input("닉네임을 입력하세요 ✍️", "익명")
user_choice = st.selectbox("당신의 취향은?", user_styles)

if st.button("궁합 보기"):
    st.subheader("🌟 특별 추천 멤버 (ENHYPEN) 🌟")

    special_members = [name for name in idol_styles.keys() if "(ENHYPEN)" in name]
    for name in special_members:
        style, tags = idol_styles[name]
        score = get_score(user_choice, style)
        show_card(name, style, tags, score, highlight=True)

    st.subheader("✨ 당신의 취향에 맞는 특별 추천 ✨")
    if user_choice in style_match:
        match_idol = style_match[user_choice]
        style, tags = idol_styles[match_idol]
        score = get_score(user_choice, style)
        show_card(f"{match_idol} (맞춤 추천)", style, tags, score, highlight=True)

    st.subheader(f"🔥 {user_name}님의 TOP 3 궁합 아이돌 🔥")
    all_scores = []
    for name, (style, tags) in idol_styles.items():
        score = get_score(user_choice, style)
        all_scores.append((name, style, tags, score))
    top3 = sorted(all_scores, key=lambda x: x[3], reverse=True)[:3]
    for name, style, tags, score in top3:
        show_card(name, style, tags, score, highlight=True)

    st.subheader("🔮 오늘의 아이돌 운세 🔮")
    today = datetime.date.today().strftime("%Y-%m-%d")
    random.seed(today)
    today_idol = random.choice(list(idol_styles.keys()))
    st.success(f"✨ 오늘 {user_name}님과 최고의 케미를 보여줄 아이돌은 **{today_idol}** ✨")
