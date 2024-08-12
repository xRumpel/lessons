import pandas as pd

df = pd.read_csv('dz.csv')
#print(df.head())
#print(df.tail())
#print(df.info())
#print(df.describe())
#print(df['Name'])
#print(df[['Name', 'City']])
#print(df.loc[3])
#print(df.loc[2, 'Name'])

#print(df.[df['Salary', 'City'] > 0.7])
average_salaries = df.groupby('City')['Salary'].mean()
print(average_salaries)




