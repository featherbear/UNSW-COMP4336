---
title: "Project"
date: 2020-06-17T09:26:54+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Distance Estimation using Wireless Signal Strength

This project aims to investigate the relationship between distance and wireless signal strength; in hopes to accurately estimate the distance between objects given a wireless signal strength reading.

## Data Collection

### Procedure

11 markers were placed in a straight unobstructed line, each 1 meter apart from the next marker. An access point (mobile phone) was placed at one end of the line. For each marker (including the marker where the phone was positioned), a laptop was positioned - such that its USB WiFi adapter was in direct line of sight with the access point. Beacon frames were captured at each marker for one minute (60 seconds).

This capturing procedure was completed twice - once in an indoor environment and once in an outdoor environment.

### Results

|Indoor Environment|Outdoor Environment|
|:---:|:---:|
|![](part1/indoor/signal_linear_all.png)|![](part1/outdoor/signal_linear_all.png)|

#### Indoor Environment

|Linear Average|Logarithmic Average|
|:---:|:---:|
|![](part1/indoor/signal_linear_average.png)|![](part1/indoor/signal_log_average.png)|

|Distance (m)|Average RSS (dBm)|# Data Points|
|:----------:|:---------------:|:-----------:|
|0|-16.85|530|
|1|-50.01|515|
|2|-61.51|631|
|3|-67.62|561|
|4|-63.11|544|
|5|-59.89|505|
|6|-63.25|603|
|7|-64.67|609|
|8|-64.17|487|
|9|-71.35|496|
|10|-62.64|548|

#### Outdoor Environment

|Linear Average|Logarithmic Average|
|:---:|:---:|
|![](part1/outdoor/signal_linear_average.png)|![](part1/outdoor/signal_log_average.png)|

|Distance (m)|Average RSS (dBm)|# Data Points|
|:----------:|:---------------:|:-----------:|
|0|-21.32|584|
|1|-40.47|631|
|2|-55.18|670|
|3|-47.71|711|
|4|-62.47|692|
|5|-55.78|678|
|6|-57.84|668|
|7|-63.09|691|
|8|-64.46|655|
|9|-67.92|662|
|10|-62.67|540|

## Data Fit

> To model the data and to verify the distance estimation, 90% of the data was used to train the model, whilst the other 10% of the data was used as sample test data.

**Indoor**

|![](part1/indoor/graph_mini.png)|![](part1/indoor/script_output.png)|
|:---:|:---:|

**Outdoor**  

|![](part1/outdoor/graph_mini.png)|![](part1/outdoor/script_output.png)|
|:---:|:---:|

> **Legend**
> * Blue - Recorded data points
> * Red - Average data points
> * Green - Estimated distances

### Naive Distance Estimation

For both indoor and outdoor environments; a linear regression fit was calculated from their sample data.  
This linear regression fitted distance (X) to estimated RSS (Y). The formula for RSS to estimated distance was derived by re-ordering the linear regression curve formula.

* Indoor Estimation - $ d_{indoor}(rss) = -(rss+44.936) / 2.797 $
* Outdoor Estimation - $ d_{outdoor}(rss) = -(rss+38.521) / 3.303 $

### Accuracy

> Hit-rate has been defined as the percentage of data points in a distance class, whose distance estimation matches the recorded distance.

As shown by the hit-rates on both graphs, it is evident that the distance estimation formula is sub-optimal, and is not accurate over a wide range of RSS values. For both indoor and outdoor environments, the normalised mean square error was quite low.

The $R^2$ score for the indoor environment was only $0.38$, indicating a very poor fit.  
As a result, many of the test RSS values for each distance class did not return the correct distance; the majority of distance classes had only (at most) 1 correctly estimated distance.
This can be attributed due to RF interference within the house (i.e. microwaves and other wireless devices) - which had largely increased the variance of RSS values of each class.

The $R^2$ score for the outdoor environment was $0.62$, which indicated a slightly better fit - with many more distance classes being accurate to at least 10% of their test samples. It is however, still not a good fit for all values
