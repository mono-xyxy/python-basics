import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, np.nan, 30, 35, np.nan],
    "salary": [50000, 60000, np.nan, 80000, 90000],
    "city": ["NY", "LA", "SF", None, "NY"]
}
df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe())
print(df.head(2))
print(df.tail(2))
print(df.sample(2))
print(df.isnull().sum())
print(df.isnull().mean()*100)
print(df.notnull().sum())