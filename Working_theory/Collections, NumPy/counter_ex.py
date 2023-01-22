from collections import Counter

Moscow=['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow=Counter(Moscow)
counter_spb=Counter(spb)

counter_spb_msc=counter_moscow+counter_spb
counter_dif=counter_moscow-counter_spb
most_common_car=counter_moscow.most_common(1)

print(*counter_spb.elements()) #вывод всех элементов 
print(list(counter_spb)) #список элементов 
print(dict(counter_spb)) #преобразование в словарь
print(counter_spb_msc) #суммарное кол-во машин в 2х городах
print(counter_dif) #расчет разницы при помощи знака "-"
counter_moscow.subtract(counter_spb) #объект модифицирован
print(counter_moscow) #расчет разницы при помощи ф-и subtract
print(most_common_car[0][0]) #выводим наиболее часто встречаемый цвет в Москве

