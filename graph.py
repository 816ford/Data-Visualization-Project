import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from functions import make, years


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Make", "Model", "Year", "Price", "Mileage"]

cars_df = pd.read_csv("resources/cars_outliers_removed.csv", usecols=columns)
vehicles_df = pd.read_csv("resources/vehicles.csv")
car_details_df = pd.read_csv("resources/CAR DETAILS FROM CAR DEKHO.csv")

sns.scatterplot(x="Mileage", y="Price", data=years(2005,make("Toyota", cars_df)))
# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Porsche", df)))
# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Honda", df)))

plt.show()

