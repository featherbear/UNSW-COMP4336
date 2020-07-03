---
title: "Week 3 Quiz"
date: 2020-06-19T01:20:53+10:00

categories: ["Quizzes"]

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> Which of the following protocol mechanism helps achieve collision avoidance in WLAN?

a) Carrier Sensing  
**b) RTS/CTS**  
c) MIMO  
d) Virtual Carrier Sensing  
e) DCF  

---

> What is the slot-time for 5 GHz WLANs?

a) 9ms  
**b) 9μs**  
c) 12ms  
d) 12μs  
e) 12ns  

---

> Although a total of fourteen 22-MHz channels are defined for 2.4 GHz DSSS WLANs, the 14th channel is not always available. The first 13 channels follow the 5 MHz channel spacing for the centre frequency (starting from 2412) with 11 MHz assigned on both sides of the centre frequency. If we consider the first 13 channels, a maximum of three non-overlapping channels exist. (1, 6, 11) is an example of a set of three non-overlapping channels. Can you identify another set of three non-overlapping channels among the first 13 channels?

**2, 7, 12**

---

> How many successive unsuccessful transmission attempts are required for the Congestion Window (CW) variable to reach its maximum value in an 802.11n WLAN operating in the 5 GHz band?

**6**

_For 5 GHz 802.11n, CWmin=15 and CWmax=1023. After nthunsuccessful attempt, CW = (2n x CWmin + 2n -1, CWmax) For n=6, 2n x CWmin + 2n -1 = 1023.Therefore, after 6 successive unsuccessful transmission attempts, CW will reach its maximum value._

---

> Consider an 802.11a WLAN. A station estimates the transmission times of RTS, CTS, and ACK as 16 μs, 16 μs, and 25 μs, respectively. After receiving the RTS, the AP generates a CTS. What would be the value of the Duration field in the CTS header if the station wanted to send a 250 μs long data frame?

**323 us**

802.11a has SIFS = 16 μs.  
Duration field in CTS = CTS_time + ACK_time + data_time + 2xSIFS  
= 16+25+250+2x16 = 323 μs

---

> An WiFi frame has the following contents in its first three address fields, ADR1 to ADR3:Destination Address,BSSID, and Source Address. Which of the following is a likely transmission event for this frame?

**a) Server to mobile client**  
b) Client to mobile server  
c) Mobile to Mobile direct communication without any access point (adhoc WiFi)  
d) Mobile from one Distribution System to a mobile in another Distribution System connected via two WiFi access points (wireless bridge)  
e) None of these  

---

> Which of the following bits are used for power saving in WiFi?

a) Power management and Retry bits  
b) Power management and Order bits  
c) Power management and ToDS bits  
d) Power management and FromDS bits  
**e) Power management and More Data bit**  

---

> Dynamic Frequency Selection (DFS) is required for 5GHz WiFi irrespective of the choice of channel.

**False**

_A set of channels are always available, no DFS required (not shared by RADAR)._

---

> It is always wise to combine two channels into a wider channel of larger bandwidth.

**False**

Wider channel means more chances of interference from adjacent WLAN. This is particularly problematic in dense deployment (typical urban living)and for 2.4GHz WiFi (40MHz channel would occupy a large fraction of the 2.4GHz band and finding non-overlapping channel would be problematic)_

---

> What would be the channel width if two 5GHz channels are combined into a single one?

**40 MHz**

_5GHz WiFi uses 20 MHz-wide channels. So 20+20=40MHz_