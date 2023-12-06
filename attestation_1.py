import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Добавляем столбец для индекса
data['index'] = range(len(data))

# Создаем сводную таблицу
pivot_table = data.pivot_table(index='index', columns='whoAmI', aggfunc=len, fill_value=0)

# Объединяем с исходным DataFrame
data_one_hot = pd.concat([data, pivot_table], axis=1)

# Удаляем ненужные столбцы
data_one_hot = data_one_hot.drop(['whoAmI', 'index'], axis=1)

print(data_one_hot.head())
