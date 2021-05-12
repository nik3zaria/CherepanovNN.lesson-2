staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
def employee_name(name):
    getting_a_name = name.split()
    name_staff = getting_a_name[-1]
    name_staff = name_staff.capitalize()
    return name_staff
i = 0
while i < len(staff):
    name_for_output = employee_name(staff[i])
    print(f'Привет, {name_for_output}!')
    i += 1