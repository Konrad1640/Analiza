import pandas as pd
import numpy as np

df_klienci = pd.DataFrame({

    'ID_klienta': [1,2,3,4],
    'Imię': ['Jan', 'Anna', 'Piotr', 'Marek']
})

df_zamówienia = pd.DataFrame({
    'ID_zamówienia': [101, 102, 103, 104],
    'ID_klienta': [1,2,3,2],
    'Kwota': [150, 200, 250, 300]

})

merged_df = pd.merge(df_klienci, df_zamówienia, on='ID_klienta')
print(merged_df)