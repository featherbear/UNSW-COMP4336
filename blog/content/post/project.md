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

## Data Collection

### Procedure

11 markers were placed in a straight unobstructed line, each one meter apart from the next marker. An access point (mobile phone) was placed at one end of the line. For each marker (including the marker where the phone was positioned), a laptop was positioned - such that its USB WiFi adapter was in direct line of sight with the access point. Beacon frames were captured at each marker for one minute (60 seconds).

This set of packet captures were completed twice. Once in an indoor environment and once in an outdoor environment.

### Results

|Indoor Environment|Outdoor Environment|
|:---:|:---:|
|![](part1/indoor/signal_linear_all.png)|![](part1/outdoor/signal_linear_all.png)|

## Analysis

#### Indoor Environment

|Linear Average|Logarithmic Average|
|:---:|:---:|
|![](part1/indoor/signal_linear_average.png)|![](part1/indoor/signal_log_average.png)|

|Distance (m)|RSS (dBm)|
|:----------:|:-------:|
|0|-16.85|
|1|-50.01|
|2|-61.51|
|3|-67.62|
|4|-63.11|
|5|-59.89|
|6|-63.25|
|7|-64.67|
|8|-64.17|
|9|-71.35|
|10|-62.64|

#### Outdoor Environment

|Linear Average|Logarithmic Average|
|:---:|:---:|
|![](part1/outdoor/signal_linear_average.png)|![](part1/outdoor/signal_log_average.png)|

|Distance (m)|RSS (dBm)|
|:----------:|:-------:|
|0|-21.32|
|1|-40.47|
|2|-55.18|
|3|-47.71|
|4|-62.47|
|5|-55.78|
|6|-57.84|
|7|-63.09|
|8|-64.46|
|9|-67.92|
|10|-62.67|

## Data Fit

> To model the data and to verify the distance estimation, 90% of the data was used to train the model, whilst the other 10% of the data was used as sample test data.

**Indoor**

|![](part1/indoor/graph_mini.png)|![](part1/indoor/script_output.png)|
|:---:|:---:|

**Outdoor**  

|![](part1/outdoor/graph_mini.png)|![](part1/outdoor/script_output.png)|
|:---:|:---:|

* Blue - Recorded data points
* Red - Average data points
* Green - Estimated distances

### Naive Distance Estimation

* Indoor Estimation - $ d_{indoor}(rss) = -(rss+44.936) / 2.797 $
* Outdoor Estimation - $ d_{outdoor}(rss) = -(rss+38.521) / 3.303 $

### Accuracy

> Hit-rate has been defined as the percentage of data points in a distance class, whose distance estimation matches the recorded distance.

As shown by the hit-rates on both graphs, it is evident that the distance estimation formula is sub-optimal, and is not accurate over a wide range of RSS values.

For both indoor and outdoor environments, the normalised mean square error was quite low.  
The $R^2$ score for the indoor environment was only $0.38$, indicating a poor fit.  
The $R^2$ score for the outdoor environment was $0.62$, which indicated a slightly better fit.

