#!/usr/bin/python3

# z5206677

import pandas as pd
import numpy as np
import glob, os

data = dict()

print("Reading data")
os.chdir("../outdoor") # outdoor / indoor
fileSuffix = ".pcapng.csv"

# Read csv files
for file in glob.glob("*" + fileSuffix):
    point = int(file.replace(fileSuffix, ""))
    data[point] = pd.read_csv(file)
    print(point, data[point]["wlan_radio.signal_dbm"].count() )

# Order the data
data = [(i, data[i]) for i in sorted(data.keys())]

# Combine the data
combined = pd.concat([pd.DataFrame(dict(RSS=v["wlan_radio.signal_dbm"],Distance=[i]*v["wlan_radio.signal_dbm"].count())) for (i,v) in data], ignore_index=True)
print(combined["RSS"].count())

# Extract 10% of the data to be used as test data.
# The other 90% is to be used as training data.
testSample = combined.sample(frac=0.1)
trainingSample = combined.drop(testSample.index)

# Analyse
analysis = []
for i, frame in data:
  values = trainingSample.loc[trainingSample["Distance"] == i]
  average = values["RSS"].mean()
  analysis.append(dict(index=i, data=values, average=average))

print("Averages:", *(map(lambda v: round(v,2), [data["average"] for data in analysis])))

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
X = combined.iloc[:, 1].values.reshape(-1, 1)
Y = combined.iloc[:, 0].values.reshape(-1, 1) 

XYmodel = LinearRegression()  # create object for the class
XYmodel.fit(X, Y)  # perform linear regression
Y_pred = XYmodel.predict(X)  # make predictions
print("\nXY R^2 score:", XYmodel.score(X, Y))
print(f"XY: {round(XYmodel.coef_[0][0],3)}*distance + {XYmodel.intercept_[0]}")
print(f"Manual YX: (RSS+{-round(XYmodel.intercept_[0],3)})/{round(XYmodel.coef_[0][0],3)}")

'''
YXmodel = LinearRegression()
YXmodel.fit(Y, X)
print("\nYX R^2 score:", YXmodel.score(Y, X))
print(f"YX: {round(YXmodel.coef_[0][0],3)}*RSS + {YXmodel.intercept_[0]}")
print()

"""
Issues...
"""
def plot_YX_regression(values):
  X_pred = YXmodel.predict(values)
  plt.scatter(X_pred, values, color="green", marker="x")
  return X_pred
'''

def plot_XY_regression():
  plt.plot(X, Y_pred, color="red")

def plot_YX_manual(values):
  formula = lambda rss: (rss-XYmodel.intercept_[0])/XYmodel.coef_[0][0]
  x_values = [formula(v) for v in values]
  plt.scatter(x_values, values, color="green", marker="x")
  return x_values


def plot_average():
  indexes = []; averages = []
  for data in analysis:
    indexes.append(data["index"])
    averages.append(data["average"])
  plt.scatter(indexes, averages, color="red", marker="s")

# plt.scatter(combined["Distance"], combined["RSS"])

plt.scatter(X,Y) # Actual values
# plot_XY_regression()
plot_average()

print()
total = 0
hit = 0
for data in analysis:
  correctDistance = data["index"]
  samples = testSample.loc[testSample["Distance"] == correctDistance]["RSS"]
  x_values = plot_YX_manual(samples)
  count = sum(map(lambda v: (correctDistance-1 <= v <= correctDistance+1) and 1 or 0, x_values))
  
  hit += count
  total += len(x_values)
  print(f"Hit-rate for {correctDistance}m :: {count}/{len(x_values)} :: {round(count/len(x_values)*100,2)}%")

print(f"\nTotal hit-rate :: {hit}/{total} :: {round(hit/total*100,2)}%")

#plt.xscale('log')
plt.xlabel("Distance (m)")
plt.ylabel("RSS (dBm)")
plt.show()
