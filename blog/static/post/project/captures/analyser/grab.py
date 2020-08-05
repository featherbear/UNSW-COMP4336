#!/usr/bin/python3

# z5206677

from scipy.optimize import curve_fit
import math
import pandas as pd
import numpy as np
import glob
import os
from pykalman import KalmanFilter
import matplotlib.pyplot as plt

data = dict()

print("Reading data")
fileSuffix = ".pcapng.csv"

oldCWD = os.getcwd()
os.chdir("../outdoor")

# Read csv files
t = 0
for file in glob.glob("*" + fileSuffix):
    point = int(file.replace(fileSuffix, ""))
    data[point] = pd.read_csv(file)

    # print(point, data[point]["wlan_radio.signal_dbm"].count())
# Order the data
data = [(i, data[i]) for i in sorted(data.keys())]

# Combine the data
combined = pd.concat(
  [pd.DataFrame(dict(
      RSS=v["wlan_radio.signal_dbm"],
      Distance=[i]*v["wlan_radio.signal_dbm"].count()
   )) for (i, v) in data
  ],
  ignore_index=True
)

X = combined.iloc[:, 1].values.reshape(-1, 1)
Y = combined.iloc[:, 0].values.reshape(-1, 1)

# Extract 10% of the data to be used as test data.
# The other 90% is to be used as training data.
testSample = combined.sample(frac=0.1)
trainingSample = combined.drop(testSample.index)

"""
Analyse data and perform Kalman Filtering
"""

os.chdir(oldCWD)
os.chdir("../../report/kalman_filter")

# Analyse
analysis = []
for i, frame in data:
    values = trainingSample.loc[trainingSample["Distance"] == i]

    average = values["RSS"].mean()
    minimum = values["RSS"].min()
    maximum = values["RSS"].max()
    val_range = maximum - minimum

    # Perform Kalman Filter algorithm
    kf = KalmanFilter()
    kalman_vals = kf.smooth(values["RSS"])[0]

    # Generate Kalman filter overlay on top of raw values
    assert(len(values["RSS"]) == len(kalman_vals))
    plt.clf()
    plt.title(f"RSS distribution at {i}m")
    plt.xlabel('Samples')
    plt.ylabel('RSS (dBm)')
    plt.plot(range(len(kalman_vals)), values["RSS"], label="raw")
    plt.plot(range(len(kalman_vals)), kalman_vals, label="filtered", alpha=0.9)
    plt.legend()
    plt.savefig(f"./{i}.png", dpi=300)
    plt.clf()

    analysis.append(dict(
        index=i,
        data=values,
        average=average,
        range=val_range,
        kalman=dict(
            avg=(kalman_vals[-1][-1]+kalman_vals[-2][-1])/2,
            data=kalman_vals,
            range=kalman_vals.max() - kalman_vals.min()
        )
    ))


"""
Compare unfiltered vs kalman filter values
"""
print("Averages:", *(map(lambda v: round(v, 2), [data["average"] for data in analysis])))
print("Kalman Averages:", *(map(lambda v: round(v, 2), [data["kalman"]["avg"] for data in analysis])))

print("RSS Range:", *(map(lambda v: round(v, 2), [data["range"] for data in analysis])))
print("RSS Range (Kalman):", *(map(lambda v: round(v, 2), [data["kalman"]["range"] for data in analysis])))

plt.clf()
plt.title("Average Value vs Kalman Filter")
plt.xlabel('Distance (m)')
plt.ylabel('RSS (dBm)')
xdata = np.array([data["index"] for data in analysis])
plt.scatter(xdata, [data["average"] for data in analysis], label="average value")
plt.scatter(xdata, [data["kalman"]["avg"] for data in analysis], label="kalman weighted value")
plt.legend()
plt.savefig("./average_vs_kalman_linear.png", dpi=300)
plt.xscale('log')
plt.xlim(right=15)
plt.savefig("./average_vs_kalman_logarithmic.png", dpi=300)
plt.clf()

"""
Data set removal
"""

os.chdir(oldCWD)
os.chdir("../../report/set_removal")

# Ignore distance 3 (outlier)
strippedData = [*filter(lambda d: d["index"] != 3, analysis)]
plt.clf()
plt.title("Average Value vs Kalman Filter | 3m Redacted")
plt.xlabel('Distance (m)')
plt.ylabel('RSS (dBm)')
xdata = indexData = np.array([data["index"] for data in strippedData])
plt.scatter(xdata, [data["average"] for data in strippedData], label="average value")
plt.scatter(xdata, [data["kalman"]["avg"] for data in strippedData], label="kalman weighted value")
plt.legend()
plt.savefig("./average_vs_kalman_no3_linear.png", dpi=300)
plt.xscale('log')
plt.xlim(right=15)
plt.savefig("./average_vs_kalman_no3_logarithmic.png", dpi=300)
plt.clf()

"""
Analyse other values
"""

os.chdir(oldCWD)
os.chdir("../../report")

plt.clf()
plt.title("Signal Strength over Distance")
plt.xlabel('Distance (m)')
plt.ylabel('RSS (dBm)')
plt.scatter(indexData, [data["kalman"]["avg"] for data in strippedData], label="kalman weighted value", color="#FF7900")
plt.legend()
plt.savefig("./kalman_no3_linear.png", dpi=300)
plt.xscale('log')
plt.xlim(right=15)
plt.savefig("./kalman_no3_logarithmic.png", dpi=300)

plt.clf()
plt.title("RSS to Distance Distribution")
plt.xlabel('RSS (dBm)')
plt.ylabel('Distance (m)')
plt.scatter(Y, X, label="recorded values")
plt.scatter([data["kalman"]["avg"] for data in strippedData], indexData, label="kalman weighted value")
plt.legend()
plt.gca().invert_xaxis()
plt.savefig("./dist_linear.png", dpi=300)
plt.yscale('log')
plt.ylim(top=15)
plt.savefig("./dist_logarithmic.png", dpi=300)
plt.clf()

# Get RSS value at distance = 1m
rss_1 = [data["kalman"]["avg"] for data in strippedData if data["index"] == 1][0]

"""
Calculate distance model parameters

# RSS = loss at 1m - n10log(d) + chi
# log(d) = (loss at 1m + chi (+) RSS)/10n
# d = exp((loss at 1m + chi (+) RSS)/10n)

:: Model: distance = exp( (rss_1 + RSS + chi) / 10n )
"""
def formula(x, n, chi):
    val = rss_1 - x
    val /= 10 * n
    val = math.exp(val)
    return val

# Multi-function
def fit_func(x, n, chi):
    return [formula(X, n, chi) for X in x]


xdata = [data["kalman"]["avg"] for data in strippedData]
ydata = indexData
(n, chi), pcov = curve_fit(fit_func, xdata, ydata)

# https://stackoverflow.com/questions/19189362/getting-the-r-squared-value-using-curve-fit
residuals = ydata - fit_func(xdata, n, chi)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((ydata-np.mean(ydata))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"distance = exp( ({round(rss_1, 2)} + RSS + {round(chi,2)}) / (10*{round(n,2)}) )")
print(f"R^2 = {round(r_squared, 2)}")

"""
Display model fit
"""
plt.clf()
plt.title("RSS to Distance Distribution")
plt.xlabel('RSS (dBm)')
plt.ylabel('Distance (m)')
plt.scatter(Y, X, label="recorded values")
xdata = [data["kalman"]["avg"] for data in analysis]
ydata = [data["index"] for data in analysis]
plt.scatter(xdata, ydata, label="kalman weighted value")
xdata = [*range(-80, 0)]
ydata = [formula(i, n, chi) for i in range(-80, 0)]
plt.plot(xdata, ydata, label=f"line (n: {round(n,2)}, $\chi$: {round(chi,2)})", color="green")
plt.legend()
plt.gca().invert_xaxis()
plt.ylim(top=15)
plt.savefig("./fit_linear.png", dpi=300)
plt.yscale('log')
plt.autoscale()
plt.xlim(left=rss_1 // 4 * 3)
plt.ylim(bottom=0.5, top=15)
plt.savefig("./fit_logarithmic.png", dpi=300)
plt.clf()

"""
Check model accuracy
"""

print()
plt.clf()
plt.title("RSS to Distance Test")
plt.xlabel('RSS (dBm)')
plt.ylabel('Distance (m)')
plt.gca().invert_xaxis()

plt.scatter([], [], label="hit", color="green")
plt.scatter([], [], label="near", color="lightgreen")
plt.scatter([], [], label="miss", color="grey")
plt.legend()

total_hit = 0
total_near = 0
total = 0

for data in analysis:
  correctDistance = data["index"]
  samples = testSample.loc[testSample["Distance"] == correctDistance]["RSS"]
  
  approximations = fit_func(samples, n, chi)
  
  tolerance = 1
  nearTolerance = 1.5

  hit   = []
  near  = []
  miss  = []
  
  for i in range(len(approximations)):
    if correctDistance - tolerance <= approximations[i] <= correctDistance + tolerance:
      hit.append(samples.iloc[i])
    elif correctDistance - tolerance - nearTolerance <= approximations[i] <= correctDistance + tolerance + nearTolerance:
      near.append(samples.iloc[i])
    else:
      miss.append(samples.iloc[i])
  
  total_hit += len(hit)
  total_near += len(near)
  total += len(approximations)

  plt.scatter(hit, [correctDistance] * len(hit), label="hit", color="green")
  plt.scatter(near, [correctDistance] * len(near), label="near", color="lightgreen")
  plt.scatter(miss, [correctDistance] * len(miss), label="miss", color="grey")

  print(f"Hit-rate for {correctDistance}m :: {len(hit)+len(near)}/{len(approximations)} :: {round((len(hit)+len(near))/len(approximations)*100,2)}%")

print(f"\nTotal hit-rate :: {total_hit+total_near}/{total} :: {round((total_hit+total_near)/total*100,2)}%")

plt.savefig(f"./fit_test.png", dpi=300)
plt.show()