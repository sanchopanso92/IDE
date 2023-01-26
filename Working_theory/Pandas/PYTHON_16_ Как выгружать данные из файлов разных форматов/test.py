import json # Импортируем модуль json
from pprint import pprint # Импортируем функцию pprint()
with open('data/recipes.json') as f: # Открываем файл и связываем его с объектом "f"
    recipes = json.load(f) # Загружаем содержимое открытого файла в переменную recipes

cuisine=set()

for i in recipes:
    cuisine.add(i['cuisine'])




#dict_rec=dict(keys=cuisine, values=val)

d = {cuisine: 0}

#for i in recipes:
    #dict_rec[i['cuisine']]+=1

print(d )