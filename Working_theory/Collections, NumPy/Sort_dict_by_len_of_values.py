from collections import defaultdict

a=[[1,2,3],[4,5,6]]
b=[[3,1]]
c=[[1,1,1,1],[2,2],[3,3,3]]

def prod(spisok):
    
    products=[]
    for i in spisok:
        products.extend(i)       
    return products

dic_prod=defaultdict()
dic_prod['a']=prod(a)
dic_prod['b']=prod(b)
dic_prod['c']=prod(c)
dic_prod1=sorted(dic_prod.items(), key=lambda x: len(x[1]), reverse=True)
       

print(dic_prod1[0][0])

#2ой пример сортировки с помощью функции
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

# Отсортируйте список ratings по убыванию рейтинга. Для кафе с одинаковым рейтингом отсортируйте кортежи по названию.

ratings.sort(key=lambda x: (-x[1], x[0]))

# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
from collections import OrderedDict
cafes = OrderedDict(ratings)