import pandas as pd
import numpy as np

data = {
    'Sklep': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Miesiąc': ['Styczeń', 'Styczeń', 'Luty', 'Luty', 'Marzec', 'Marzec'],
    'Sprzedaż': [5000, 7000, 8000, 6000, 9000, 7500]
}

df = pd.DataFrame(data)

#Grupowanie danych wedlug sklepu i obliczanie sumy i średniej sprzedaży
grupa = df.groupby('Sklep').agg({'Sprzedaż': ['sum', 'mean']})
print(grupa)