---
title: "Lab 3"
date: 2020-06-17T14:06:04+10:00

categories: ["Labs"]
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Objectives

1. To observe path loss phenomenon under LoS condition by analysing RSS at different distances
2. To estimate path loss exponent for indoor and outdoor under LoS

# Measurements

Measurements were taken over a 5 metre distance, with ten 0.5 metre intervals.  
A 5m measuring tape was used to mark out the distances between the laptop and wireless access point.  

For all measurements, packets were captured for a minute, with the laptop and AP maintaining an unobstructed line of sight throughout.

## Indoor Measurement

![](indoor.png)

_Note: The data point for 2.5m was removed as it looked like an outlier in the dataset_

## Outdoor Measurement

![](outdoor.png)

# Analysis

|Location|Slope Gradient|$R^2$|
|:-------|:------------:|:---:|
|Indoor|-8.0781|0.6732|
|Outdoor|-8.3350|0.6271|
|Indoor (with 2.5m data point)|-8.0781|0.6121|

When comparing the $R^2$ values, the indoor measurement has a better fit to its slope equation - as its data points fit closer to the line of best fit.  

> I found this interesting as I had originally thought that inside the house, there would be more interference (I had conducted the experiment near the kitchen, where an active microwave oven was in use) - yet the data points were more closely related than the data points recorded outside 

The outdoor measurement has a steeper slope gradient, and therefore a greater path loss exponent - meaning that the signal strength decreased faster when outdoors than when indoors.  

This could be attributed to the environment and atmosphere of the recording locations, such as extra reflections, reflection surface material, temperature, weather (it was raining when I recorded outside).
