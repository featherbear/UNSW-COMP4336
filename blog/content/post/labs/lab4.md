---
title: "Lab 4"
date: 2020-06-24T13:20:39+10:00

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

* To observe wireless signal path loss in WiFi frequencies due to different types of obstacles

# Useful

> Lab Task: [lab4-task.pdf](./lab4-task.pdf)

Data was extracted from the PCAP files with

`tshark -r FILE -T fields -e frame.number -e frame.time -e wlan_radio.signal_dbm -E header=y -E separator=, -E quote=d -E occurrence=f`

---

# Experiment

## Procedure

The access point (phone) and laptop were placed 5 meters apart in a hallway, with a clear Line of Sight.

For each scenario, measurements were recorded on 2.4 GHz only (as my laptop does not support 5 GHz communication) for one minute.

I had decided to take measurements of the following

* Unobstructed (Control variable)
* Wooden Sliding Door - directly beside the laptop
* Plastic Chair - 2.5m away from both devices
* Mattress - 2.5m away from both devices
* Mattress + Door
* Aluminium Foil - Placed over the access point
* Aluminium Foil - Wrapped over the access point, but not as to block all communications

Note: The aluminium foil was not originally part of the intended experiment, but was used to check that the recordings were valid. _(Aluminium foil wrapped around a device creates a Faraday cage which will block all EM radiation)_

## Data and Results

> All graphs were created with a binning size of 4 dB.

### Aggregate Data

|Scenario|Data Points|Average (dBm)|Range (dBm)|Graph|
|:-------|:---------:|:-----------:|:---------:|:---:|
|Control |473        |-63.51       |20|![](captures/5m%20unobstructed.png)|
|Door    |490        |-63.76       |20|![](captures/5m%20wooden%20door.png)|
|Mattress|501        |-63.97       |16|![](captures/5m%20mattress.png)|
|Mattress + Door|497|-64.24|12|![](captures/5m%20mattress%20door.png)|
|Foil    |508|-64.69|16|![](captures/5m%20foil.png)|
|Plastic Chair   |486        |-64.73       |26|![](captures/5m%20chair.png)|
|Foil (Wrapped)|348|-75.94|16|![](captures/5m%20foil%20wrap.png)|

### Binning Coverage (estimate)

|Scenario|Average Value Coverage|
|:------:|:--------:|
|Control|53%|
|Door|89.80%|
|Mattress|71.86%|
|Mattress + Door|40.24%|
|Foil|88.58%|
|Chair|46.30%|
|Foil (Wrapped)|61.78%|

### Signal Loss

|Scenario|Loss (dBm)|
|:------:|:--------:|
|Control|-|
|Door|0.25|
|Mattress|0.46|
|Mattress + Door|0.73|
|Foil|1.18|
|Chair|1.22|
|Foil (Wrapped)|12.43|

## Analysis

### Signal Loss

Interestingly, despite placing different objects in-between the AP and Laptop - not much of a signal loss was recorded.  

For most recordings, the signal loss was less than 1 dBm.  
This is likely due to my choice in objects as the object and density of its material is a large factor. I had however expected the mattress to have a greater signal loss

### Relative Signal Loss

When comparing the signal loss between the different scenarios, the relative losses did seem to make sense.  

* The wooden sliding door was very thin in nature, and so logically it would not impede the strength of the signal too greatly.
* The mattress is denser, and so it would greater impede the signal strength
* When combining the mattress and wooden door, there should be an even greater signal loss
  * This is logically confirmed as `0.25 dBm + 0.46 dBm = 0.71 dBm ~= 0.73 dBm`
* A sheet of aluminium foil placed on top of the access point would have interfered with the path that a EM wave would have to travel
* A sheet of aluminium foil _wrapped_ around the access point would greatly interfere with the signal strength
  * This is also suggested through the low number of captured beacon frames / packets (348) during the recording

### Signal Strength Variation

Most data sets and results were logical, _except_ the chair.  
Being made out of plastic, but also being relatively small in size - I would have assumed that the chair would not have a signal loss greater than the other objects.  

This could possibly be attributed to some external radio interference during measurement, as the range of recorded signal strengths is 26 dBm - noticeably higher than the ranges of the other scenarios. Consequently, only 46.30% of the recorded signal strengths were within the same binning segment as the average value.

It seems that the Door had the most stable average coverage, as the signal strength of least ~90% of the captured packets were within the average bin (-68 to -64 dBm range).