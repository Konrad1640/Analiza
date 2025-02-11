import pandas as pd
import numpy as np 

data = {
    'Imię': ['Jan', 'Anna', 'Piotr', 'Marek', 'Ewa'],
    'Wiek': [25, 35, 29, 45, 22],
    'Zarobki': [4000, 6000, 3000, 8000, 4500]
}

df = pd.DataFrame(data)

# Filtrowanie danych: zarobki > 5000 i wiek < 40

filtered_df = df[(df['Zarobki'] > 4000) & (df['Wiek'] < 40)]
print(filtered_df)