---
title: "Lab 2"
date: 2020-06-10T13:00:11+10:00

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

1. To learn WiFi tracing, filtering, and data export using Wireshark
2. To observe some fundamental properties of wireless signal strength and noise through capturing and analysing real WiFi trace

# Useful

> Lab Task: [lab2-task.pdf](./lab2-task.pdf)

To show Antenna Strength - find the `wlan_radio.signal_dbm` field in the header, then right-click and press **Apply as Column**

---

# Task 1

> Capture: [lab2.pcapng](./lab2.pcapng)  

![](2020-06-05_21-45-03.png)

|Type|Graph|
|:---:|:---:|
|Signal Strength|![](task1-signalstrength.png)|
|Signal Noise|![](task1-signalnoise.png)|
|SNR|![](task1-signalnoiseratio.png)|

**Analysis**

Signal strength decreased when the mobile phone was brought away from the laptop. When the laptop was brought closer, the signal strength increased again.  
The closer the mobile phone was to the laptop, the stronger the amplitude of radio waves were, hence the stronger the signal strength.

Signal noise remained fairly consistent at around -86dBm throughout the packet capture. Noise is as a result of atmospheric and environmental influences, which are unlike to change too drastically. The laptop was most likely also stationary, so there should not be too much of a change in signal noise.

The signal to noise ratio closely follows the shape of the signal strength graph - decreasing when the phone is moved away from the laptop, and increasing when the phone is brought nearer. This is as expected as the signal noise is considered to be quite constant, hence the changes in SNR is as a result of a change in signal strength.

---

# Task 2

> _Capture was taken over a period of 50 seconds, moving the phone away for 25 seconds, then bringing it closer for the next 25 seconds._  
> &nbsp;  
> Capture: [task2_packets.pcapng](./task2_packets.pcapng)  
> CSV: [task2_packets.csv](./task2_packets.csv)

_Note: I was only able to capture the signal strength, as no signal noise data nor SNR data was captured in Wireshark_

![](2020-06-10_14-06-10.png)

![](task2-signalstrength.png)

**Analysis**

Like what was seen in task 1, increasing the distance between the phone and laptop lowered the signal strength. When bringing the two devices closer together, the signal strength would increase.

There is noticeably much more variance in the signal strength as compared to the graphs in task 1.  
This is most likely as a result of atmospheric and environmental factors (Brick walls, plasterboard walls, metals, other devices in the house).

As no signal noise was able to be recorded, it is difficult to justify whether signal noise had changed during this investigation. As a result, the SNR is unknown.