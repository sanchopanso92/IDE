import pandas as pd
diabetes = pd.read_csv('diabetes_data.csv')
diabetes.head()

duplicates = diabetes[diabetes.duplicated()]
print('Число дубликтов: {}'.format(duplicates.shape[0]))
diabetes = diabetes.drop_duplicates()
print('Результирующее число записей: {}'.format(diabetes.shape[0]))

list_stat=[]
for i in diabetes.columns:
    dupl=diabetes.i.value_counts(normalize=True)
    list_stat.append(dupl)
print(dupl)