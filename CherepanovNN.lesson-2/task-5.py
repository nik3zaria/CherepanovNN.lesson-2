price_list = [57.8, 46.51, 97, 32.9, 32, 87, 54.6, 1, 12.32, 1.1, 90]
i = 0
def adding_zeros(x):
    x = str(x)
    x = x.zfill(2)
    return x
while i < len(price_list):
    x = price_list[i]
    rub = int(x)
    kop = int(100 * (x - rub))
    rub = adding_zeros(rub)
    kop = adding_zeros(kop)
    price_list[i] = f'{rub} руб. {kop} коп.'
    i += 1
print(", ".join(price_list))

price_list = sorted(price_list)
print(", ".join(price_list))

reverse_price_list = price_list[:]
reverse_price_list = sorted(reverse_price_list, reverse = True)
print(", ".join(reverse_price_list))

max_price_list = reverse_price_list[:5]
print(", ".join(max_price_list))

max_price_list = sorted(max_price_list)
print(", ".join(max_price_list))
