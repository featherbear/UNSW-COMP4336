---
title: "Lab 6"
date: 2020-07-17T14:49:07+10:00

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

* To observe and analyse BLE (Bluetooth 4) Frequency Hopping (Algorithm #1)

---

BLE Frequency Hopping Algorithm #1 functions as per the [block diagram](https://inst.eecs.berkeley.edu/~ee290c/sp18/note/BLE_Vol6.pdf) (Page 2644)

![](2020-07-17_15-16-48.png)

* $f_{k+1} = (f_k + h)\ mod\ 37$
  * $h = 5$ in this simulation

---

![](Snipaste_2020-07-17_14-09-43.png)

Following the BLE frequency hopping algorithm ...  
Channels follow the pattern: 5, 10, 15, 20, 25, 30, 35, 3, 8, 13, 18, 23, 28, ...

---

* If the next unmapped channel is a good channel, the algorithm selects that channel to be used.

* If the next unmapped channel is a bad channel, a different channel is used, as per the remapping algorithm $remappingIndex = unmappedChannel\ mod\ numUsedChannels$. This allows for a previously used good channel to be reused.

---

|Settings|View|
|:---:|:---:|
|![](Snipaste_2020-07-17_14-22-38.png)|![](Snipaste_2020-07-17_14-22-21.png)|

- WiFi Channel 1 occupies the 2401–2423 MHz range
- BLE Channel 0 occupies the 2403-2405 MHz range
- BLE Channel 9 occupies the 2421-2423 MHz range

* WiFi channel 1 interferes with BLE channels 0-9, therefore BLE channels 0-9 are marked as "Bad"
* Hop increment of $h = 5$

Channel Selection Flow
---

> Used Channels: `[10, ..., 36]` (length 27)

* Try channel 0+5%37=5
  * Channel 5 is a bad channel
  * Use remapping index 5%27 -> Channel 15
* Try channel 5+5%37=10
  * Channel 10 is a good channel
  * Use channel 10
* Try channel 15+5%37=20
  * Channel 20 is a good channel
  * Use channel 20
* Try channel 20+5%37=25
  * Channel 25 is a good channel
  * Use channel 25
* Try channel 25+5%37=30
  * Channel 30 is a good channel
  * Use channel 30
* Try channel 30+5%37=35
  * Channel 35 is a good channel
  * Use channel 35
* Try channel 35+5%37=3
  * Channel 3 is a bad channel
  * Use remapping index 3%27 -> Channel 13
* Try channel 3+5%37=8
  * Channel 8 is a bad channel
  * Use remapping index 8%27 -> Channel 18
* Try channel 8+5%37=13
  * Channel 13 is a good channel
  * Use channel 13

Explanation
---

The algorithm starts of with the old channel as 0.  
The next calculated channel is $(old+h)%37$.  
If that calculated channel does not exist in the used channel list, a modulo (size of the used channel list) is performed against calculated channel, and the result is used as the index of the used channel list.

As a result, the simulation (using $h=5$) attempts to use channel, however it is considered bad - and so it is remapped to channel 15.  
The channels then increase by 5 mod 37, until it reaches channel 3 which is considered bad. Channel 3 is remapped to channel 13.  
The next channel, channel 8 - is also considered bad, and so is remapped to channel 18.  
Following that, the next channel - channel 13 is considered good, so channel 13 is used.
