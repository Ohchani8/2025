import streamlit as st
import random
import datetime

st.set_page_config(page_title="아이돌 궁합 테스트", page_icon="💕", layout="centered")

# -----------------------------
# CSS 스타일 (배경 + 폰트)
# -----------------------------
page_bg = """
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f0, #fdf4ff, #e0f7fa);
    background-attachment: fixed;
    font-family: "Comic Sans MS", "Arial Rounded MT Bold", sans-serif;
}
h1, h2, h3, h4 {
    font-family: "Comic Sans MS", "Arial Rounded MT Bold", sans-serif;
    color: #ff66b2;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -----------------------------
# 아이돌 데이터
# -----------------------------
idol_styles = {
    "정원 (ENHYPEN)": ("책임감 있는 리더", ["#리더", "#든든"]),
    "희승 (ENHYPEN)": ("차분한 현실주의자", ["#현실적", "#차분"]),
    "제이 (ENHYPEN)": ("재치 있는 아이디어 뱅크", ["#유머", "#센스"]),
    "제이크 (ENHYPEN)": ("성실한 노력파", ["#노력파", "#믿음직"]),
    "성훈 (ENHYPEN)": ("차분한 카리스마", ["#시크", "#냉철"]),
    "선우 (ENHYPEN)": ("장난꾸러기 무드메이커", ["#장난꾸러기", "#웃음"]),
    "니키 (ENHYPEN)": ("열정 가득한 댄서", ["#열정", "#댄서"]),
    "홍승한": ("따뜻한 감성형", ["#감성", "#따뜻"]),
    "해찬 (NCT)": ("에너지 넘치는 분위기 메이커", ["#에너지", "#비타민"]),
    "마크 (NCT)": ("다재다능 올라운더", ["#랩", "#춤", "#프로"]),
    "재현 (NCT)": ("따뜻한 공감러", ["#다정", "#공감"]),
    "차은우 (ASTRO)": ("비주얼 천재", ["#비주얼", "#완벽"]),
    "유우시 (NCT WISH)": ("밝고 긍정적인 매력", ["#긍정", "#밝음"]),
    "리쿠 (NCT WISH)": ("든든한 에너지형", ["#에너지", "#리더십"]),
    "오시온 (NCT WISH)": ("순수한 청량미", ["#청량", "#순수"]),
    "카리나 (aespa)": ("카리스마 리더", ["#걸크러시", "#리더"]),
    "윈터 (aespa)": ("청아한 보컬", ["#보컬", "#맑음"]),
    "닝닝 (aespa)": ("자유로운 영혼", ["#자유", "#솔직"]),
    "지젤 (aespa)": ("힙한 래퍼", ["#힙합", "#자신감"]),
}

user_styles = [
    "차분한 스타일",
    "에너지 넘치는 스타일",
    "리더형 스타일",
    "유머러스한 스타일",
    "예술적인 스타일",
    "따뜻한 스타일",
]

messages = [
    "찰떡궁합! 둘이 만나면 시너지 폭발 💖",
    "따뜻하고 편안한 관계 🌷",
    "티격태격하지만 즐거운 케미 🎶",
    "서로 배울 점이 많아요 ✨",
    "의외로 잘 맞는 조합이에요 ⚡",
    "환상의 팀워크를 보여줄 수 있어요 🌈",
]

# -----------------------------
# 유틸 함수
# -----------------------------
def get_score(user_choice, idol_style):
    random.seed(user_choice + idol_style)
    return random.randint(60, 100)

def get_relation(score):
    if score > 90:
        return "💕 완벽한 궁합!"
    elif score > 80:
        return "🌸 꽤 잘 맞는 편이에요!"
    else:
        return "🍀 서로 다른 매력이 있어요!"

def show_card(name, style, tags, score, highlight=False):
    bg_color = "#ffe6f0" if highlight else "#fdf4ff"
    border_color = "#ff99cc" if highlight else "#d8b4fe"
    relation = get_relation(score)
    tags_html = " ".join([f"<span style='color:#ff66a3; font-size:14px;'>{tag}</span>" for tag in tags])
    st.markdown(
        f"""
        <div style="padding:20px; margin:15px 0;
                    border-radius:25px; background-color:{bg_color};
                    border:3px solid {border_color};
                    box-shadow: 3px 3px 12px rgba(255,182,193,0.3); text-align:center;">
            <h4 style="margin:0; color:#ff3399;">💖 {name} 💖</h4>
            <p style="margin:6px 0 0 0; font-size:15px;">✨ 스타일: <b>{style}</b></p>
            <p style="margin:6px 0 0 0;">{tags_html}</p>
            <p style="margin:6px 0 0 0; font-size:14px;">👉 {random.choice(messages)}</p>
            <p style="font-weight:bold; font-size:16px; color:#ff3399;">궁합 점수: {score}% 🍭</p>
            <p style="font-size:12px; color:#999;">(높을수록 궁합이 좋아요!)</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.progress(score / 100)

# -----------------------------
# 메인 화면
# -----------------------------
st.title("💞 아이돌 궁합 테스트 💞")
st.write("👉 당신의 취향 스타일을 고르고, 최애와의 궁합을 확인해보세요!")

nickname = st.text_input("당신의 이름(닉네임)을 입력해주세요 ✨", "팬")
user_choice = st.selectbox("당신의 취향은?", user_styles)

if st.button("궁합 보기"):
    st.subheader(f"✨ {nickname}님의 아이돌 궁합 결과 ✨")

    # 특별 추천
    st.markdown("## 🌟 특별 추천 (ENHYPEN 전용) 🌟")
    for name, (style, tags) in idol_styles.items():
        if "ENHYPEN" in name or name == "홍승한":
            score = get_score(user_choice, style)
            show_card(name, style, tags, score, highlight=True)

    # 맞춤 추천
    st.markdown("## 🎀 당신에게 꼭 맞는 맞춤 추천 🎀")
    sorted_idols = sorted(idol_styles.items(), key=lambda x: get_score(user_choice, x[1][0]), reverse=True)
    name, (style, tags) = sorted_idols[0]
    score = get_score(user_choice, style)
    show_card(name, style, tags, score, highlight=True)

    # TOP 3 궁합
    st.markdown("## 🏆 궁합 TOP 3 🏆")
    scores = []
    for name, (style, tags) in idol_styles.items():
        score = get_score(user_choice, style)
        scores.append((score, name, style, tags))
    scores.sort(reverse=True)
    for score, name, style, tags in scores[:3]:
        show_card(name, style, tags, score)

    # 오늘의 아이돌
    st.markdown("## 🍀 오늘의 아이돌 운세 🍀")
    today = datetime.date.today().strftime("%Y-%m-%d")
    random.seed(today)
    lucky = random.choice(list(idol_styles.items()))
    name, (style, tags) = lucky
    score = get_score(user_choice, style)
    show_card(name, style, tags, score, highlight=True)
