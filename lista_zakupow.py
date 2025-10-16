shopping_list = {
    "Piekarnia": ["chleb", "bułki", "pączek"],
    "Warzywniak": ["marchew", "seler", "rukola"],
}

cnt = 0

print("Lista zakupów:")
for store in shopping_list:
    print(f"Idę do {store} i kupuję tam: {shopping_list[store]}.")
    cnt += len(shopping_list[store])
print(f"W sumie kupuję {cnt} produktów.")