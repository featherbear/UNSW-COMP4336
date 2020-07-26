---
title: "Lab 7"
date: 2020-07-22T16:39:25+10:00

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

# Task 1

|n=9|n=12|
|:---:|:---:|
|![](9.png)|![](12.png)|
|Figure 1|Figure 2|

![](9-tesselate.png)  
Figure 3 - Cluster size of 9, repeated

# Task 2

I was not able to get the Network Cell Info program running on my Android phone - it kept crashing every time I opened it; so I was unable to complete task 2.

In terms of the outcome, I believe that at different points in the house, there will be different reported Reference Signals Received Power values.

At lower heights, the RSRP will likely be weaker, as there is a greater distance to the cell tower.  
At higher heights, the RSRP will be stronger.

At different points around the house, there will be different readings from the current and neighbouring station. As the RSRP from the current station decreases, the RSRP from the neighbouring station should increase.  

When `RSRP(Neighbour) > RSRP(Current)` the phone _should_ switch to the neighbouring station.  
As a result, the once-current station will then become the neighbouring station.
