import pandas as pd
import numpy as np

df = pd.DataFrame({'name': ['Маша', 'Саша', 'Рудольф'],
'surname':['Петрова', 'Сидоров', 'Кац'],
                   'age': [-5, 2, 4]})

df.to_csv('peoples.csv')
print(df)
