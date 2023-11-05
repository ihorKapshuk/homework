stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0
sum_dict = {}

for element in stock:
    element_price = stock[element] * prices[element]
    total_price += element_price
    sum_dict[element] = element_price
print("Загальна сума товарів на складі : ", total_price)
print("Словник із товарами та вартістю їх кількості на складі : ", sum_dict)