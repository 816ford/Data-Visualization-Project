import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats


sns.set()
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


cols = ["Make", "Model", "Year", "Price", "Mileage"]
df = pd.read_excel("resources/Cars.comData.xlsx", usecols=cols)
#Dropping makes that have  >10 entries
dropped = ["Porsche", "Hummer", "Rivian", "Maserati", "Genesis", "Cadillac", "Alfa", "Volvo"]
for i in dropped:
    df = df.drop(df[df['Make'] == i].index)


df = df.drop_duplicates()
avg_price = {}

makes_list = df["Make"].unique()
for i in makes_list:
    avg_price[i] = df.loc[df['Make'] == i, 'Price'].mean()
print(avg_price)
df[np.abs(stats.zscore(df["Price"])) < 3]
df = df[df["Price"] < 100000]

df.insert(5, "Grouped Years", pd.cut(df["Year"], bins=[2013, 2016, 2019, 2022, 2025]))

print(df['Make'].value_counts())
f, ax = plt.subplots(figsize=(7, 7))
ax.set(xscale="log", yscale="log")
# sns.regplot(x="Mileage", y="Price",data=df, ax=ax, scatter_kws={"s": 100})

# sns.lineplot(x="Mileage", y="Price", hue="Make", data=df)
sns.lmplot(x="Mileage", y="Price",hue="Make", data=df,
           logx=True, ci=None, scatter_kws={"s": 100})

print(df['Make'].value_counts())
# sns.scatterplot(x="Mileage", y="Price", data=df)

plt.show()

