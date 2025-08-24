import streamlit as st
import random
import datetime

st.set_page_config(page_title="아이돌 궁합 테스트", page_icon="💕", layout="centered")

# -----------------------------
# CSS 스타일
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
# 아이돌 데이터 (이름: (그룹, 스타일, 태그))
# -----------------------------
idol_db = {
    "정원 (ENHYPEN)": ("ENHYPEN", "책임감 있는 리더", ["#리더", "#든든"]),
    "희승 (ENHYPEN)": ("ENHYPEN", "차분한 현실주의자", ["#현실적", "#차분"]),
    "제이 (ENHYPEN)": ("ENHYPEN", "재치 있는 아이디어 뱅크", ["#유머", "#센스"]),
    "제이크 (ENHYPEN)": ("ENHYPEN", "성실한 노력파", ["#노력파", "#믿음직"]),
    "성훈 (ENHYPEN)": ("ENHYPEN", "차분한 카리스마", ["#시크", "#냉철"]),
    "선우 (ENHYPEN)": ("ENHYPEN", "장난꾸러기 무드메이커", ["#장난꾸러기", "#웃음"]),
    "니키 (ENHYPEN)": ("ENHYPEN", "열정 가득한 댄서", ["#열정", "#댄서"]),
    "홍승한": ("Solo", "따뜻한 감성형", ["#감성", "#따뜻"]),
    "해찬 (NCT)": ("NCT", "에너지 넘치는 분위기 메이커", ["#에너지", "#비타민"]),
    "마크 (NCT)": ("NCT", "다재다능 올라운더", ["#랩", "#춤", "#프로"]),
    "재현 (NCT)": ("NCT", "따뜻한 공감러", ["#다정", "#공감"]),
    "차은우 (ASTRO)": ("ASTRO", "비주얼 천재", ["#비주얼", "#완벽"]),
    "유우시 (NCT WISH)": ("NCT WISH", "밝고 긍정적인 매력", ["#긍정", "#밝음"]),
    "리쿠 (NCT WISH)": ("NCT WISH", "든든한 에너지형", ["#에너지", "#리더십"]),
    "오시온 (NCT WISH)": ("NCT WISH", "순수한 청량미", ["#청량", "#순수"]),
    "카리나 (aespa)": ("aespa", "카리스마 리더", ["#걸크러시", "#리더"]),
    "윈터 (aespa)": ("aespa", "청아한 보컬", ["#보컬", "#맑음"]),
    "닝닝 (aespa)": ("aespa", "자유로운 영혼", ["#자유", "#솔직"]),
    "지젤 (aespa)": ("aespa", "힙한 래퍼", ["#힙합", "#자신감"]),
}

# 취향 옵션
user_styles = [
    "차분한 스타일",
    "에너지 넘치는 스타일",
    "리더형 스타일",
    "유머러스한 스타일",
    "예술적인 스타일",
    "따뜻한 스타일",
]

# 카드 문구
messages = [
    "찰떡궁합! 둘이 만나면 시너지 폭발 💖",
    "따뜻하고 편안한 관계 🌷",
    "티격태격하지만 즐거운 케미 🎶",
    "서로 배울 점이 많아요 ✨",
    "의외로 잘 맞는 조합이에요 ⚡",
    "환상의 팀워크를 보여줄 수 있어요 🌈",
]

# 오늘의 운세 요소
activities = ["춤 연습", "노래 감상", "팬 아트 만들기", "아이돌 영상 보기", "커버 영상 찍기", "응원봉 점검하기", "플리 업데이트"]
colors = ["핑크 💖", "하늘 💙", "노랑 💛", "보라 💜", "초록 💚", "민트 🩵", "코랄 🧡"]

# -----------------------------
# 사이드바 옵션 (그룹 필터 / 테마 / 결과 고정)
# -----------------------------
with st.sidebar:
    st.header("⚙️ 옵션")
    all_groups = sorted(set(g for g, _, _ in idol_db.values()))
    sel_groups = st.multiselect("그룹 필터", options=all_groups, default=all_groups)

    theme = st.selectbox("테마", ["하트 💖", "꽃 🌸", "별 ✨"])
    lock_today = st.toggle("결과 고정 (오늘 날짜 기준)", value=True, help="켜면 같은 취향/닉네임/날짜에서 결과가 고정돼요.")
    st.markdown("---")
    st.caption("팁: 그룹 필터로 보고 싶은 소속만 골라봐!")

# 테마별 스타일
def theme_style(theme_name: str):
    if "하트" in theme_name:
        return {"accent": "#ff3399", "bg_hi": "#ffe6f0", "bg": "#fdf4ff", "border_hi": "#ff99cc", "border": "#d8b4fe", "emoji": "💖"}
    if "꽃" in theme_name:
        return {"accent": "#ff6fb1", "bg_hi": "#fff0f6", "bg": "#fff7fb", "border_hi": "#ffc2e5", "border": "#ffd6ec", "emoji": "🌸"}
    return {"accent": "#8a5cff", "bg_hi": "#f1ecff", "bg": "#f7f4ff", "border_hi": "#b7a1ff", "border": "#d3c8ff", "emoji": "✨"}

TS = theme_style(theme)

# -----------------------------
# 유틸 함수
# -----------------------------
def seed_for(user_choice: str, idol_style: str, nickname: str, lock_today: bool):
    base = user_choice + "|" + idol_style + "|" + nickname
    if lock_today:
        base += "|" + datetime.date.today().strftime("%Y-%m-%d")
    random.seed(base)

def get_score(user_choice, idol_style, nickname, lock_today):
    seed_for(user_choice, idol_style, nickname, lock_today)
    return random.randint(60, 100)

def score_meaning(score):
    if score >= 91:
        return "완벽한 궁합"
    elif score >= 81:
        return "꽤 잘 맞는 편"
    elif score >= 71:
        return "괜찮은 케미"
    else:
        return "서로 다른 매력"

def show_card(name, style, tags, score, highlight=False):
    bg_color = TS["bg_hi"] if highlight else TS["bg"]
    border_color = TS["border_hi"] if highlight else TS["border"]
    emoji = TS["emoji"]
    tags_html = " ".join([f"<span style='color:{TS['accent']}; font-size:14px;'>{tag}</span>" for tag in tags])
    st.markdown(
        f"""
        <div style="padding:20px; margin:15px 0;
                    border-radius:25px; background-color:{bg_color};
                    border:3px solid {border_color};
                    box-shadow: 3px 3px 12px rgba(0,0,0,0.05); text-align:center;">
            <h4 style="margin:0; color:{TS['accent']};">{emoji} {name} {emoji}</h4>
            <p style="margin:6px 0 0 0; font-size:15px;">✨ 스타일: <b>{style}</b></p>
            <p style="margin:6px 0 0 0;">{tags_html}</p>
            <p style="margin:6px 0 0 0; font-size:14px;">👉 {random.choice(messages)}</p>
            <p style="font-weight:bold; font-size:16px; color:{TS['accent']};">궁합 점수: {score}% 🍭</p>
            <p style="font-size:12px; color:#777;">({score_meaning(score)})</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.progress(score / 100)

# -----------------------------
# 메인 화면
# -----------------------------
st.title("💞 아이돌 궁합 테스트 (업그레이드) 💞")
st.write("👉 취향을 고르고, 그룹 필터/테마를 설정한 뒤 결과를 확인해보세요!")

nickname = st.text_input("당신의 이름(닉네임)을 입력해주세요 ✨", "팬")
user_choice = st.selectbox("당신의 취향은?", user_styles)

# 필터링된 아이돌 목록
filtered = {n: v for n, v in idol_db.items() if v[0] in sel_groups}

if st.button("궁합 보기"):
    if not filtered:
        st.error("선택된 그룹에 아이돌이 없어요. 사이드바에서 그룹을 선택해주세요!")
        st.stop()

    st.subheader(f"✨ {nickname}님의 아이돌 궁합 결과 ✨")

    # 점수 계산
    scored = []
    for name, (group, style, tags) in filtered.items():
        s = get_score(user_choice, style, nickname, lock_today)
        scored.append((s, name, group, style, tags))
    scored.sort(reverse=True)  # 점수 높은 순

    # 맞춤 추천 (상위 3 중 랜덤)
    st.markdown("## 🎀 당신에게 꼭 맞는 맞춤 추천")
    top3_candidates = scored[:3] if len(scored) >= 3 else scored
    seed_for(user_choice, "match_pick", nickname, lock_today)
    pick = random.choice(top3_candidates)
    s, n, g, stl, tg = pick
    show_card(n, stl, tg, s, highlight=True)

    # TOP 3 카드
    st.markdown("## 🏆 궁합 TOP 3")
    for s, n, g, stl, tg in scored[:3]:
        show_card(n, stl, tg, s)

    # 오늘의 아이돌 + 운세
    st.markdown("## 🍀 오늘의 아이돌 운세")
    # 오늘자 고정 랜덤
    seed_for(user_choice, "today_lucky", nickname, True)  # 운세는 날짜 고정
    lucky = random.choice(list(filtered.items()))
    lucky_name, (lg_group, lg_style, lg_tags) = lucky
    lucky_score = get_score(user_choice, lg_style, nickname, True)
    show_card(lucky_name, lg_style, lg_tags, lucky_score, highlight=True)

    # 오늘의 추천 활동 + 색상
    seed_for(user_choice, "today_activity", nickname, True)
    today_activity = random.choice(activities)
    seed_for(user_choice, "today_color", nickname, True)
    today_color = random.choice(colors)
    st.markdown(
        f"<p style='text-align:center; font-size:16px;'>오늘의 추천 활동: <b>{today_activity}</b></p>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='text-align:center; font-size:16px;'>오늘의 행운 색상: <b>{today_color}</b></p>",
        unsafe_allow_html=True
    )

    # 결과 다운로드 (텍스트)
    result_lines = []
    result_lines.append(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] 아이돌 궁합 테스트 결과")
    result_lines.append(f"닉네임: {nickname}")
    result_lines.append(f"취향: {user_choice}")
    result_lines.append(f"테마: {theme}")
    result_lines.append(f"그룹 필터: {', '.join(sel_groups)}")
    result_lines.append("")
    result_lines.append("🎀 맞춤 추천")
    result_lines.append(f"- {n} / 점수: {s}% ({score_meaning(s)}) / 스타일: {stl} / 태그: {' '.join(tg)}")
    result_lines.append("")
    result_lines.append("🏆 TOP 3")
    for i, (ss, nn, gg, stl2, tg2) in enumerate(scored[:3], start=1):
        result_lines.append(f"{i}. {nn} / 점수: {ss}% ({score_meaning(ss)}) / 스타일: {stl2} / 태그: {' '.join(tg2)}")
    result_lines.append("")
    result_lines.append("🍀 오늘의 아이돌 운세")
    result_lines.append(f"- {lucky_name} / 점수: {lucky_score}% ({score_meaning(lucky_score)})")
    result_lines.append(f"- 추천 활동: {today_activity}")
    result_lines.append(f"- 행운 색상: {today_color}")

    result_text = "\n".join(result_lines)
    st.download_button("📥 결과 저장 (텍스트)", data=result_text.encode("utf-8"),
                       file_name="아이돌_궁합_결과.txt", mime="text/plain")

    # 작은 미니 미션 (클릭 시 랜덤 미션 새로 뽑기)
    with st.expander("🎲 오늘의 미니 미션 뽑기"):
        if st.button("미션 뽑기"):
            seed_for(user_choice, "mini_mission", nickname, not lock_today)  # 고정 끄면 매번 달라짐
            missions = [
                "최애 직캠 3개 보기",
                "최애에게 편지 쓰기(메모 OK)",
                "최애 노래로 10분 워밍업",
                "랜덤 셀카 포즈 따라 하기",
                "최애 입덕 영상 친구에게 추천"
            ]
            st.success(f"오늘의 미션: {random.choice(missions)}")

# 푸터
st.markdown("<p style='text-align:center; color:#888;'>© 아이돌 궁합 테스트 · 즐거운 덕질 되세요! ✨</p>", unsafe_allow_html=True)
