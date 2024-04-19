import pandas as pd
from matplotlib import pyplot as plt
from functions import make, years, price
import seaborn as sns
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Make", "Model", "Year", "Price", "Mileage"]
df = pd.read_csv("resources/cars_outliers_removed.csv", usecols=columns)

sns.scatterplot(x="Mileage", y="Price", data=years(2005,make("Toyota", df)))
# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Porsche", df)))

# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Honda", df)))
plt.show()
