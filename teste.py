import pandas as pd


file = pd.read_csv("C:\\Users\\manoel.torres\\OneDrive - Kumulus\\Documents\\GitHub\\Python\\ex1\\crimes.csv")
df = pd.DataFrame(file)

print(df[(df['Rolling year total number of offences'] > 10) & (df['Region'] == 'East') & (df['12 months ending']) & (df['PFA'])])