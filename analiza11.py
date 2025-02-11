import pandas as pd
import numpy as np

# Tworzenie przykładowego Dataframe z brakującymi danymi 

data = {
    'Imię': ['Jan', 'Anna', 'Piotr', 'Marek', 'Ewa'],
    'Wiek': [25, np.nan, 29, np.nan, 22]
}

df = pd.DataFrame(data)


#Zastępowanie NaN średnią wartością

średni_wiek = df['Wiek'].mean()
df['Wiek'].fillna(średni_wiek, inplace=True)
print(df)
