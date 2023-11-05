week_days = ["Monday", "Thuesday", "Wednesday", "Thursday", "Frieday", "Satureday", "Sunday"]
first_dict = {i + 1 : day for i, day in enumerate(week_days)}
print(first_dict)
second_dict = {day : i + 1 for i, day in enumerate(week_days)}
print(second_dict)