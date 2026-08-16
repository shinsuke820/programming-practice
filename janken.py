import tkinter as tk
import random

root = tk.Tk()
root.title("じゃんけんゲーム")
root.geometry("400x480")
root.configure(bg="#f2f2f2")


# タイトル
title_label = tk.Label(
    root,
    text="じゃんけんゲーム",
    font=("Arial", 22, "bold"),
    bg="#f2f2f2"
)
title_label.pack(pady=15)


# -------------------------
# キャラクター画像
# -------------------------

# 元の画像を読み込む
character_original = tk.PhotoImage(file="character.png")

# 表示したい最大サイズ
max_width = 140
max_height = 140

# 元画像のサイズを取得
image_width = character_original.width()
image_height = character_original.height()

# 何分の1に縮小するか計算
width_scale = (image_width + max_width - 1) // max_width
height_scale = (image_height + max_height - 1) // max_height

scale = max(width_scale, height_scale, 1)

# 画像を縮小
character_image = character_original.subsample(scale, scale)

# 画像を表示
character_label = tk.Label(
    root,
    image=character_image,
    bg="#f2f2f2"
)
character_label.pack(pady=5)


# -------------------------
# 結果を表示するカード
# -------------------------

result_label = tk.Label(
    root,
    text="手を選んでね\n頑張ってね！",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="black",
    width=26,
    height=4,
    padx=15,
    pady=10,
    relief="solid",
    bd=2,
    justify="center"
)
result_label.pack(pady=15)


# -------------------------
# じゃんけんの処理
# -------------------------

def choose(hand):
    hands = ["グー", "チョキ", "パー"]
    computer = random.choice(hands)

    if hand == computer:
        result = "あいこ"
        text_color = "#555555"
        bg_color = "#eeeeee"

    elif (
        (hand == "グー" and computer == "チョキ")
        or (hand == "チョキ" and computer == "パー")
        or (hand == "パー" and computer == "グー")
    ):
        result = "勝ち"
        text_color = "#228B22"
        bg_color = "#e6ffe6"

    else:
        result = "負け"
        text_color = "#cc0000"
        bg_color = "#ffe6e6"

    result_label.config(
        text=f"あなた：{hand}\nコンピューター：{computer}\n結果：{result}",
        fg=text_color,
        bg=bg_color
    )


# -------------------------
# ボタン
# -------------------------

button_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)
button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="グー",
    font=("Arial", 12),
    width=8,
    height=2,
    command=lambda: choose("グー")
).pack(side="left", padx=5)


tk.Button(
    button_frame,
    text="チョキ",
    font=("Arial", 12),
    width=8,
    height=2,
    command=lambda: choose("チョキ")
).pack(side="left", padx=5)


tk.Button(
    button_frame,
    text="パー",
    font=("Arial", 12),
    width=8,
    height=2,
    command=lambda: choose("パー")
).pack(side="left", padx=5)

root.mainloop()