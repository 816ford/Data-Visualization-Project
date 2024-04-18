def make(make, df):
    make = df[df["Make"].str.contains(make)]
    return make

def years(year, df):
    year = df[df["Year"] >= year]
    return year
