import pandas as pd

data = {
    "Zawodnik": ["Lewandowski", "Mbappe", "Messi", "Haaland"],
    "Gole": [30, 28, 40, 35],
    "Asysty": [10, 12, 15, 8],
}

df = pd.DataFrame(data)

# Ranking zawodników wedlug goli + asyst

df["Punkty"] = df["Gole"] + df["Asysty"]
df = df.sort_values(by="Punkty", ascending=False)

print(df)