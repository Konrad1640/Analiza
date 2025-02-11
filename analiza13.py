import pandas as pd
import numpy as np

wynagrodzenia = np.array([3500, 4200, 5000, 3700, 4800])

odchylenie_standardowe = np.std(wynagrodzenia)
print(f"Odchylenie standardowe: {odchylenie_standardowe}")


#Standaryzowanie danych (średnia = 0, odchylenie = 1)
wynagrodzenia_znormalizowane = (wynagrodzenia - np.mean(wynagrodzenia)) / np.std(wynagrodzenia)
print(f"Znormalizowane wynagrodzenia: {wynagrodzenia_znormalizowane}")