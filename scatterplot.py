import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

#setting parameters and style
sns.set()
plt.rcParams["figure.figsize"] = [10.00, 3.50]
plt.rcParams["figure.autolayout"] = True

figure, axis = plt.subplots(1, 2)

#read csv
carAPI_cols = ["Make Name", "Model Name", "Trim Year", "Trim Msrp", "Engine Size", "Mileage Combined Mpg"]

#Set columns
carAPI_df = pd.read_csv("resources/carapi-opendatafeed-sample.csv", usecols=carAPI_cols)

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

#Dropping outliers from merged_df in trim msrp column
merged_df = merged_df.drop(outliers.index)

#plotting figures
sns.scatterplot(y="Engine Size", x="Mileage Combined Mpg", data=carAPI_df, ax=axis[0] )
sns.scatterplot(y="Trim Msrp", x="Mileage Combined Mpg", data=merged_df, ax=axis[1])


plt.show()




