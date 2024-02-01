import pandas as pd
titanic = pd.read_csv('Titanic-Dataset.csv')
tclass = titanic.groupby(['Pclass', 'survived']).size().unstack()

print(tclass)
