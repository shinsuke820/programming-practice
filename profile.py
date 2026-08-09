name = input("名前を入力してください：")
age = int(input("年齢を入力してください："))

next_age = age + 1

print(f"こんにちは、{name}さん！")
print(f"来年は{next_age}歳ですね。")
if age >= 20:
    print("あなたは成人です。")
else:
    print("あなたは未成年です。")
    