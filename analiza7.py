import pandas as pd
import numpy as np

np.random.seed(10)
data = {
    "ID": np.arange(1,11),
    "Wiek": np.random.randint(18, 65, size=10),
    "Zarobki": np.random.randint(3000, 15000, size=10),
}

df = pd.DataFrame(data)
print(df)