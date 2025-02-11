import pandas as pd

data = {
    "Miasto": ["Warszawa", "Kraków", "Gdańsk", "Wrocław"],
    "Temp_Styczeń": [-2, -3, 0, -1],
    "Temp_Lipiec": [25, 27, 23, 26],
}

df = pd.DataFrame(data)

df["Amplituda"] = df["Temp_Lipiec"] - df["Temp_Styczeń"]

print(df)