menu = []
menu.append(["egg", "spam", "beans"])
menu.append(["egg", "sausage", "bacom"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacom", "beans", "spam"])
menu.append(["spam", "egg", "spam", "beans", "spam", "sausage", "spam"])
menu.append(["spam", "egg", "sausage"])
menu.append(["rolls", "egg", "fish", "beans", "vegs", "sausage"])

# print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
