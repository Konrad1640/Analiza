import numpy as np
import pandas as pd

data = {
    "Data": pd.date_range(start="2023-01-01", periods=12, freq='M'),
    "Sprzedaż": np.random.randint(5000, 15000, size=12),
}

df = pd.DataFrame(data)

df["Średnia_3M"] = df["Sprzedaż"].rolling(window=3).mean()

print(df)