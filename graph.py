import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats



plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

cars_columns = ["Make", "Model", "Year", "Price", "Mileage"]
car_details_columns = ["name", "year", "selling_price", "km_driven"]
vehicles_columns = ["drive", "make", "model", "year", "comb08", "displ", "cylinders", "trany"]

carAPI_cols = ["Make Name", "Model Name", "Trim Year", "Trim Msrp", "Engine Size", "Mileage Combined Mpg"]

cars_df = pd.read_csv("resources/cars_outliers_removed.csv", usecols=cars_columns)
vehicles_df = pd.read_csv("resources/vehicles.csv", usecols=vehicles_columns)
car_details_df = pd.read_csv("resources/CAR DETAILS FROM CAR DEKHO.csv", usecols=car_details_columns)
carAPI_df = pd.read_csv("resources/carapi-opendatafeed-sample.csv", usecols=carAPI_cols)

vehicles_df = vehicles_df.rename(columns={
    "make" : "Make",
    "model" : "Model",
    "year" : "Year",
    "drive" : "Drive",
    "displ" : "Disp",
    
})


# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Porsche", df)))
# sns.boxplot(x="Price", y="Make", hue="Year", data=years(2005,make("Honda", df)))

#plt.show()

merged_df = vehicles_df.merge(cars_df, how = "left", on = ["Make", "Year"])
# cleaned_df = merged_df.dropna(subset=["Price"])



Q1 = carAPI_df["Trim Msrp"].quantile(0.25)
Q3 = carAPI_df["Trim Msrp"].quantile(0.75)
IQR = Q3 - Q1

z = np.abs(stats.zscore(carAPI_df["Trim Msrp"]))

threshold = 2
upperLimit = Q1 - threshold * IQR
lowerLimit = Q3 + threshold * IQR

carAPI_df[carAPI_df["Trim Msrp"] > upperLimit]
carAPI_df[carAPI_df["Trim Msrp"] < lowerLimit]

trimmed_df = carAPI_df.loc[(carAPI_df["Trim Msrp"] > upperLimit) | (carAPI_df[carAPI_df["Trim Msrp"] < lowerLimit])]

sns.scatterplot(y="Trim Msrp", x="Mileage Combined Mpg", data=trimmed_df)
plt.show()