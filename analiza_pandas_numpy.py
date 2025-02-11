import pandas as pd

df = pd.read_csv("sprzedaz.csv")

print(df.describe())

top_sprzedawcy = df[df["Łączna wartość (PLN)"] > 30000]
print(top_sprzedawcy)