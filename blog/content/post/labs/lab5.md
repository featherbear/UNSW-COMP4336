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

For all packets, the `wlan_radio.11n.short_gi` value was set to true, indicative that a guard interval of 400 ns was used.

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
