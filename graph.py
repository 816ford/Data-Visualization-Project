import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats


sns.set()
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
# plt.show()

#Finding z-score for trim msrp
trim_msrp_z = pd.DataFrame(np.abs(stats.zscore(carAPI_df["Trim Msrp"])))
trim_msrp_z = trim_msrp_z.rename(columns = {
    "Trim Msrp" : "Trim Msrp Z-Score"
})

#Joining new z-score column into new dataframe
merged_df = carAPI_df.join(trim_msrp_z, how = "left")

#Setting thresholds
upper_threshold = 3
lower_threshold = -3

#Finding all outliers
outliers = merged_df.loc[(merged_df["Trim Msrp Z-Score"] > upper_threshold) | 
                         (merged_df["Trim Msrp Z-Score"] < lower_threshold) 
                         ]

#Dropping outliers from merged_df
merged_df = merged_df.drop(outliers.index)


sns.scatterplot(y="Engine Size", x="Mileage Combined Mpg", data=carAPI_df)
#sns.scatterplot(y="Trim Msrp", x="Mileage Combined Mpg", data=merged_df)


plt.show()




