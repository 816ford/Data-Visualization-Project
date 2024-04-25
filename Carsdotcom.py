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
sns.scatterplot(x="Mileage", y="Price", data=df)