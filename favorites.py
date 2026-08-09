foods = ["ラーメン", "寿司", "焼肉"]

print("好きな食べ物一覧")

for number, food in enumerate(foods, start=1):
    print(f"{number}. {food}")