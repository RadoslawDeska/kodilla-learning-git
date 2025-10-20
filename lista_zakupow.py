shopping_list = {
    "Piekarnia": ["chleb", "bułki", "pączek"],
    "Warzywniak": ["marchew", "seler", "rukola"],
}

cnt = 0

print("Lista zakupów:")
for store in shopping_list:
    store_list = [p.capitalize() for p in shopping_list[store]]
    print(f"Idę do {store} i kupuję tam: {store_list}.")
    cnt += len(shopping_list[store])
print(f"W sumie kupuję {cnt} produktów.")

# koniec pliku