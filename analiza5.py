import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "Data": pd.date_range(start='2023-01-01', periods=10, freq='D'),
    "Cena_Akcji": np.random.randint(100, 200, size=10),
}

df = pd.DataFrame(data)


df['Zmiana %'] = df["Cena_Akcji"].pct_change() * 100

print(df)