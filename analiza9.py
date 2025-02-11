import pandas as pd
import numpy as np

data = {
    'Miasto': ['Warszawa', 'Kraków', 'Gdansk', 'Wrocław', 'Poznań'],
    'Sprzedaż': [15000, 20000, 18000, 22000, 30000]
}

df = pd.DataFrame(data)

#Obliczanie średniej sprzedaży

average_sales = df['Sprzedaż'].mean()
print(f"Średnia sprzedaż: {average_sales}")