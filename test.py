import pandas as pd

df = pd.read_csv("data/company_master.csv")

print(df.shape)

print(df.columns.tolist())

print(df.head())