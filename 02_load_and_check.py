import pandas as pd

df = pd.read_csv("news_sample_plus.csv", encoding="utf-8-sig")

print(df.head(5))
print(df.dtypes)
print(df.shape)
