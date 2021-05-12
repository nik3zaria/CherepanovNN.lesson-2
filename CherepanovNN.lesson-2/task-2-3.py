def get_sign(x):
    if x[0] in '+-':
        return x[0]
string_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(string_list):
        sign = get_sign(string_list[i])
        if string_list[i].isdigit() or (sign and string_list[i][1:].isdigit()):
            if sign:
                string_list[i] = sign + string_list[i][1:].zfill(2)
            else:
                string_list[i] = string_list[i].zfill(2)
            string_list.insert(i, '"')
            string_list.insert(i + 2, '"')
            i += 1
        i += 1   
print(" ".join(string_list))
