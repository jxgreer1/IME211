#imports
import pandas
import pandas as pd
import statistics
#read csv
pandas_dataframe = pd.read_csv("data.csv")
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



