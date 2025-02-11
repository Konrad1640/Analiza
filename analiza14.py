import pandas as pd
import numpy as np

#Tworzenie przykładowego DataFrame

data = {
    'Produkt': ['Laptop', 'Smartfon', 'Tablet', 'Monitor'],
    'Cena': [3000, 1500, 1200, 2500]
}

df = pd.DataFrame(data)

df['Cena_po_rabacie'] = df['Cena'] * 0.9
print(df)
