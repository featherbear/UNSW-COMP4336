---
title: "Lab 9"
date: 2020-08-07T17:50:26+10:00

categories: ["Labs"]
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

outputs: ["Report"]

---

# Hand Gestures

## Gesture 1

A hand is waved down and up in succession, in front of the wireless received

## Gesture 2

The wireless receiver is grasped momentarily by a hand

# Methodology

A laptop was connected to a wireless access point, which was running iPerf 3 to generate network activity.  
The wireless packet capture was started, and the gesture was repeated several times, with delays in between.

# Results

|Gesture 1|Gesture 2|
|:-------:|:-------:|
|![Figure 1.1](handupdown_wireshark.png)|![Figure 1.2](grabhold_wireshark.png)|
|![Figure 2.1](handupdown.png)|![Figure 2.2](grabhold.png)|

# Analysis

## Gesture 1

As seen in _[Figure 2.1]_, the RSS values dip during the gesture.  

However, they fall and rise more than the expected two times - likely due to environmental noise and RSS fluctuations.

## Gesture 2

As seen in _[Figure 2.2]_, the RSS values dip and sustain their low value until the end of the gesture.


