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
The human body did not make a large contribution to the loss of signal strength.  

The cooking pot however, did seem to cause a larger signal strength (and MCS Index) change.  
Even when brought nearer to the laptop, whilst the signal strength increased; the MCS Index did not return to its original value.
