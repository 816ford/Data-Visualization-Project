import pandas as pd
from matplotlib import pyplot as plt
from functions import make, years
import seaborn as sns
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Make", "Model", "Year", "MSRP", "city mpg", "Popularity", "Engine HP"]
df = pd.read_csv("data.csv", usecols=columns)


sns.boxplot(x="MSRP", y="Make", hue="Year", data=years(2005,make("Porsche", df)))

sns.boxplot(x="MSRP", y="Make", hue="Year", data=years(2005,make("Honda", df)))
plt.show()