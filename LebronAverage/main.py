import pandas as pd
import numpy as np
import statistics

# Read CSV files
"""
pandas_minutes = pd.read_csv("minutes.csv")
pandas_points = pd.read_csv("points.csv")

# Turn Colum into series
pandas_seriesM = pandas_minutes["Minutes"]
pandas_seriesP = pandas_points["Points"]

print(pandas_seriesM)
"""
#read csv
pandas_dataframe = pd.read_csv("minutes.csv")
pandas_series = pandas_dataframe["Lengths"]
data_list = pandas_series.tolist()
#sort data into find mean and standard deviation
data_mean = statistics.mean(data_list)
data_stdev = statistics.stdev(data_list)
#print the mean and stdev
print(data_mean)
print(data_stdev)
#user import USL and LSL
USL_str = input("Enter the upper spec limit")
LSL_str = input("Enter the lower spec limit")

USL = float(USL_str)
LSL = float(LSL_str)

cp1 = (USL-data_mean) / (3 * data_stdev)
cp2 = (data_mean - LSL) / (3 * data_stdev)

cpk=min(cp1,cp2)

print("cpk value", cpk)



