---
title: "Lab 5"
date: 2020-07-05T15:26:42+10:00

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

_Choice of modulation and coding affects the transmission data rates in wireless networks. There are many combinations of modulation and coding implemented in consumer WiFi chipsets. These combinations, known as modulation and coding schemes (MCSs), are standardized by IEEE 802.11. WiFi networks monitor the channel all the time and switch to an appropriate MCS depending on the channel condition, which also affect the instantaneous data rate of the wireless communication. In this lab, you will use simple tools, such as laptops, phones, and WiFi packet capture tools (e.g., Wireshark), to observe such dynamic variation of data rates and identify the MCSs being used by the WiFi network._

---

_Note: I am using the provided packet captures, as my wireless card was not able to capture the MCS Index data values._

---

## Task 1 - Channel variation due to change of Tx-Rx separation

> Distance affects signal strength (RSS) and hence SNR. Weaker SNR makes it difficult to detect symbols from complex MCS, and vice versa. As such, WiFi chipsets are expected to switch to simpler MCS when Tx-Rx separation is increased, and vice versa.

Start WiFi data transmissions between a phone and a laptop and then move the phone away from the laptop and then bring it closer again, slowly. Keep capturing WiFi packet in Wireshark during this time. Analyse RSS, MCS as well as the data rates from the Wireshark traces and try to explain how change in distance affects MCS/data-rate.

* [Wireshark Capture](task1/task1.pcapng)
* [CSV](task1/task1.csv)

`tshark -r "task1.pcapng" -T fields -e frame.number -e frame.time -e wlan_radio.signal_dbm -e wlan_radio.11n.mcs_index -e wlan_radio.data_rate -e wlan_radio.11n.greenfield -E header=y -E separator=, -E quote=d -E occurrence=f > task1.csv`

|Graphs|
|:----:|
|![](task1/wlan_radio.11n.mcs_index.png)|
|![](task1/wlan_radio.data_rate.png)|
|![](task1/wlan_radio.signal_dbm.png)|
|![](task1/wlan_radio.11n.greenfield.png)|

### Analysis

* The `wlan_radio.11n.greenfield` value did not seem to have an apparent effect on the MCS Indices, Data Rate nor the RSS.
* For all packets, the `wlan_radio.11n.short_gi` value was set to true, indicative that a guard interval of 400 ns was used.  
* The signal was weakest at around the 50 second mark; where the separation distance was at its maximum.

The graphs for the MCS value and data rates are virtually identical in shape, which indicate a very strong if not 1-1 correlation between MCS and Data Rate values.

|MCS Index|Data Rate (Mbps)|
|:-------:|:--------------:|
|4|43.33|
|7|72.22|
|12|86.67|
|13|115.56|
|14|130|
|15|144.44|

In comparing the MCS/Data Rate against the RSS values - it is evident that the Rate Rate drops as device separation increases, and increases when the two devices are drawn closer. Likewise, the MCS Index decreases when separated, and increases when brought together.

### Comment

When sorting the data points by RSS or MCS Index, the graphs indicate that there is a relationship between the MCS Index / Data Rate and Received Signal Strength. Sorting by RSS best produces this observation, as seen by the trend of increasing MCS Index values.

|Sort by MCS|Sort by RSS|
|:---------:|:---------:|
|![](task1/sort.by.mcs/wlan_radio.11n.mcs_index.png)|![](task1/sort.by.rss/wlan_radio.11n.mcs_index.png)|
|![](task1/sort.by.mcs/wlan_radio.signal_dbm.png)|![](task1/sort.by.rss/wlan_radio.signal_dbm.png)|

## Task 2 - Channel variation due to obstacles

> Obstacles between Tx-Rx affects signal strength (RSS) and hence SNR. As such, WiFi chipsets are expected to switch to simpler MCS when Tx-Rx path is obstructed, and vice versa.

Start WiFi data transmissions between a phone and a laptop and then bring an obstacle, such as a sofa between them and then remove it again, slowly. Keep capturing WiFi packets in Wireshark during this time. Analyse RSS, MCS as well as the data rates from the Wireshark traces and try to explain how change in obstacle affects MCS/data-rate.

* [Wireshark Capture](task2/task2.pcapng)
* [CSV](task2/task2.csv)

_A sofa, door, human body and cooking pot (cumulatively added) was used to capture the results._

`tshark -r "task2.pcapng" -T fields -e frame.number -e frame.time -e wlan_radio.signal_dbm -e wlan_radio.11n.mcs_index -e wlan_radio.data_rate -E header=y -E separator=, -E quote=d -E occurrence=f > task2.csv`

|Graphs|
|:----:|
|![](task2/wlan_radio.11n.mcs_index.png)|
|![](task2/wlan_radio.data_rate.png)|
|![](task2/wlan_radio.signal_dbm.png)|

### Analysis

|MCS Index|Data Rate (Mbps)|
|:-------:|:--------------:|
|3|28.89|
|4|43.33|
|7|72.22|
|12|86.67|
|13|115.56|
|14|130|
|15|144.44|

* Before any obstructions were placed in the way, the measured signal had an RSS of -55 dBm, a data rate of 144.44 Mbps, and an MCS index of 15.
* When the sofa was added in-between the AP and the laptop (~15 seconds since start); the signal strength dropped marginally by about 3 dBm.
* The closed door (~25s) caused the signal strength to drop by another ~3 dBm - but had also cause the MCS Index to change from 15 to 14.
* Adding in the human body had not caused much of a change in strength.  
* When the cooking pot was added in (~50s), the signal strength had decreased to about -73 dBm (~16 dBm loss from the previous RSS values); and the MCS Index had changed to 11.
* When walking back towards the laptop; the signal strength and MCS Index increased
  * However the MCS Index did not return to an MCS of 15, but topped out at 12.

As more obstacles were added, the signal strength decreased; which had lowered the MCS Index and subsequently the Data Rate.  
The human body did not make a large contribution to the loss of signal strength. The cooking pot however, did seem to cause a larger signal strength (and MCS Index) change. Even when brought nearer to the laptop, whilst the signal strength increased; the MCS Index did not return to its original value.

## Task 3 - Channel variation due to interference

> Interference from other wireless transmissions affects signal-to-noise-and-interference-ratio (SNIR). As such, WiFi chipsets are expected to switch to simpler MCS when there is severe interference, and vice versa.

Start WiFi data transmissions between a phone and a laptop and keep capturing WiFi packets in Wireshark during this time. Also, turn on a smart TV and watch a video from the Internet. Now turn on a microwave oven nearby, which uses 2.4GHz (all microwave ovens do). You may find that the video stall in your smart TV due to severe interference in the WiFi network arising from the high-power use of 2.4GHz in the microwave. The microwave should also affect the WiFi transmission between the phone and the laptop. Analyse RSS, MCS as well as the data rates from the Wireshark traces and try to explain how the microwave operation affects MCS/data-rate.

* [Wireshark Capture](task3/task3.pcapng)
* [CSV](task3/task3.csv)

A tablet, phone and laptop were all loaded with the same video stream to be played concurrently for roughly three minutes; whilst a microwave was turned on.

`tshark -r "task3.pcapng" -T fields -e frame.number -e frame.time -e wlan_radio.signal_dbm -e wlan_radio.11n.mcs_index -e wlan_radio.data_rate -e wlan_radio.noise_dbm -e wlan_radio.snr -E header=y -E separator=, -E quote=d -E occurrence=f > task3.csv`

### Analysis

![](task3/packet_frequency_histogram.png)

The frequency histogram has been split into 10 bins, each class accounting for 18 seconds of the capture.  

* At the 90 second mark, there were considerably many more packets recorded (about 10x more).  
* At the 144 second mark, there were 3x even more packets.

|Graphs|
|:----:|
|![](task3/wlan_radio.11n.mcs_index.png)|
|![](task3/wlan_radio.data_rate.png)|
|![](task3/wlan_radio.signal_dbm.png)|
|![](task3/wlan_radio.noise_dbm.png)|
|![](task3/wlan_radio.snr.png)|

It is somewhat difficult to detect the impact of the microwave, as the MCS Index, Data Rate and RSS were constantly fluctuating. Throughout the 3 minute capture period; the MCS Index constantly fluctuated from 15 to 13.  
As expected, a change in data rate followed, changing from 144.44 Mbps to 115.56 Mbps.

At times, the MCS Index would drop to 12, and the Data Rate would decrease to 68.67 Mbps - suggestive that high RF activity had cause interference, which made active data connections stall.

This can be seen most clearly at around 150 seconds; when the noise floor increased from -88 dBm to -84 dBm and stayed consistently at -84 dBm. When analysing the change in MCS Index and Data Rate, there were many more occasions where the MCS Index and Data Rate had dropped to MCS 12 - 86.67 Mbps. Consequently, the SNR decreased.  
This is indicative of continuous RF interference from a source like a microwave.  

We can infer from this observation that microwave usage causes RF interference - which makes the MCS Index and Data Rates of connections fluctuate consistently. It also causes devices to stall/drop out.
