import streamlit as st
import random
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="아이돌 궁합 테스트",
    page_icon="💕",
    layout="centered"
)

# -----------------------------
# CSS 꾸미기
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f0, #fdf4ff, #e0f7fa);
    font-family: "Comic Sans MS", "Arial Rounded MT Bold", sans-serif;
}
h1, h2, h3, h4 {
    color: #ff66b2;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 아이돌 데이터
# -----------------------------
idol_styles = {
    "정원 (ENHYPEN)": "책임감 있는 리더",
    "희승 (ENHYPEN)": "차분한 현실주의자",
    "제이 (ENHYPEN)": "재치 있는 아이디어 뱅크",
    "제이크 (ENHYPEN)": "성실한 노력파",
    "성훈 (ENHYPEN)": "차분한 카리스마",
    "선우 (ENHYPEN)": "장난꾸러기 무드메이커",
    "니키 (ENHYPEN)": "열정 가득한 댄서",
    "홍승한": "따뜻한 감성형",
    "해찬 (NCT)": "에너지 넘치는 분위기 메이커",
    "마크 (NCT)": "다재다능 올라운더",
    "재현 (NCT)": "따뜻한 공감러",
    "차은우 (ASTRO)": "비주얼 천재",
    "유우시 (NCT WISH)": "밝고 긍정적인 매력",
    "리쿠 (NCT WISH)": "든든한 에너지형",
    "오시온 (NCT WISH)": "순수한 청량미",
    "카리나 (aespa)": "카리스마 리더",
    "윈터 (aespa)": "청아한 보컬",
    "닝닝 (aespa)": "자유로운 영혼",
    "지젤 (aespa)": "힙한 래퍼",
}

user_styles = [
    "차분한 스타일", "에너지 넘치는 스타일", "리더형 스타일",
    "유머러스한 스타일", "예술적인 스타일", "따뜻한 스타일"
]

messages = [
    "찰떡궁합! 시너지 폭발 💖",
    "따뜻하고 편안한 관계 🌷",
    "티격태격하지만 즐거운 케미 🎶",
    "서로 배울 점이 많아요 ✨",
    "의외로 잘 맞는 조합이에요 ⚡",
    "환상의 팀워크를 보여줄 수 있어요 🌈",
]

# -----------------------------
# 함수 정의
# -----------------------------
def get_score(user_choice, idol_name):
    random.seed(user_choice + idol_name)
    return random.randint(60, 100)

def show_card(name, style, score):
    st.markdown(f"""
    <div style="padding:20px; margin:10px 0;
                border-radius:20px; background-color:#fdf4ff;
                border:2px dashed #d8b4fe;
                box-shadow: 2px 2px 8px rgba(255,182,193,0.3);
                text-align:center;">
        <h4 style="color:#ff3399;">💖 {name} 💖</h4>
        <p>스타일: <b>{style}</b></p>
        <p>궁합 점수: <b>{score}%</b> 🍭</p>
        <p>{random.choice(messages)}</p>
    </div>
    """, unsafe_allow_html=True)
    st.progress(score / 100)

# -----------------------------
# 메인 화면
# -----------------------------
st.title("💞 아이돌 궁합 테스트 💞")
st.write("당신의 취향 스타일을 선택하고, 최애 아이돌과의 궁합을 확인해보세요!")

nickname = st.text_input("당신의 이름(닉네임)을 입력해주세요 ✨", "팬")
user_choice = st.selectbox("당신의 취향은?", user_styles)

if st.button("궁합 보기"):
    st.subheader(f"✨ {nickname}님의 아이돌 궁합 결과 ✨")

    # 궁합 카드
    scores = []
    for name, style in idol_styles.items():
        score = get_score(user_choice, name)
        scores.append((score, name, style))
        show_card(name, style, score)

    # TOP5 궁합 그래프
    st.markdown("## 🏆 TOP 5 궁합 아이돌 🌈")
    scores.sort(reverse=True)
    top5 = scores[:5]
    names = [n for s,n,_ in top5]
    values = [s for s,_,_ in top5]
    emojis = ["💖","🌸","🍭","🐰","✨"]

    fig, ax = plt.subplots(figsize=(6,4))
    ax.barh(names[::-1], values[::-1], color="#ffb6c1")
    ax.set_xlim(60,100)
    ax.set_xlabel("궁합 점수 (%)")
    ax.set_title("TOP 5 아이돌 궁합 🌈")

    for i,(v,e) in enumerate(zip(values[::-1], emojis)):
        ax.text(v + 0.5, i, f"{v}% {e}", va='center', fontsize=12)

    fig.patch.set_facecolor('#fff0f5')
    ax.set_facecolor('#fdf4ff')
    st.pyplot(fig, clear_figure=True)
    plt.close(fig)

    # 오늘의 행운 아이템
    st.markdown("## 🍀 오늘의 행운 아이템 🍀")
    items = ["🍭 사탕", "🎧 이어폰", "📸 카메라", "🐰 인형", "🌸 꽃"]
    st.write(f"오늘의 아이템은 **{random.choice(items)}** 이에요!")
