import matplotlib.pyplot as plt

# scores = [(점수, 이름, 스타일, 태그), ...] # 이미 계산된 리스트
top5 = scores[:5]

idols = [n for _, n, _, _ in top5]
values = [s for s, _, _, _ in top5]
emojis = ["💖", "🌸", "🍭", "🐰", "✨"]  # 상위 5위에 붙일 이모지

fig, ax = plt.subplots(figsize=(6,4))
bars = ax.barh(idols[::-1], values[::-1], color="#ffb6c1")  # 파스텔 핑크
ax.set_xlim(60, 100)
ax.set_xlabel("궁합 점수 (%)")
ax.set_title("TOP 5 아이돌 궁합 🌈")

# 바 위에 점수 + 이모지
for i, (v, e) in enumerate(zip(values[::-1], emojis)):
    ax.text(v + 0.5, i, f"{v}% {e}", va='center', fontsize=12)

# 배경 색 파스텔 유지
fig.patch.set_facecolor('#fff0f5')
ax.set_facecolor('#fdf4ff')

st.pyplot(fig)
