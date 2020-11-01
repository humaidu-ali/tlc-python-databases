import numpy as np
import pandas as pd
import csv

# with open('AAPL.csv', newline='') as f:
#     reader = csv.DictReader(f)
#     data = np.empty((0,6))
#     for row in reader:
#         oneRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'],row['Adj Close'],row['Volume']]])
#         data = np.append(data,oneRow,axis=0)
#
# print(data)
# print(np.shape(data))
# print(data.ndim)
#

myDataFrame = pd.read_csv('AAPL.csv',usecols=['Date','Volume'])
print(myDataFrame)



