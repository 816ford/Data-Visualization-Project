import pandas as pd
import numpy as np
from scipy import stats

#Create a sample DataFrame of student heights
df = pd.DataFrame({'Height': [170, 160, 130, 190, 180, 150, 140, 200, 175, 165]})

# Calculate the z-score for each student's height
z = np.abs(stats.zscore(df['Height']))

# Identify outliers as students with a z-score greater than 3
threshold = 3
outliers = df[z > threshold]

# Print the outliers
print(outliers)