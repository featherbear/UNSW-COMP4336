---
title: "WiFi - 1"
date: 2020-06-17T09:54:46+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# IEEE 802.11 Basics

* `IEEE 802.11` is the name of the standard
* `WiFi` - "Wireless Fidelity" TM
* Fidelity: Compatibility between wireless equipment from different manufacturers

* IEEE 802.11 uses letters to name their versions
* WiFi Alliance uses numbers to simplify
  * WiFi 4 - 802.11n
  * WiFi 5 - 802.11ac
  * WiFi 6 - 802.11ax
  * WiFi 7 - 802.11be

# IEEE 802.11 Features

* The original legacy IEEE 802.11 operated at 1 Mbps (over IR) and 2 Mbps (over 2.4 GHz)
  * New versions were 11 Mbps (802.11b over 2.4 GHz), 54 Mbps (802.11a OFDM over 5 GHz, 802.11g OFDM over 2.4 GHz), 108 Mbps, 1.2 Gbps
* All versions used the unlicensed RF spectrum (Free!)
* Different technologies
  * Old versions - Spread spectrum ([FHSS](../physical-layer-fundamentals/#multiple-access-methods), [DSSS](../physical-layer-fundamentals/#multiple-access-methods))
  * New version (802.11n and above) - OFDM
* Priority of wireless traffic (i.e VOIP)
* Power management - longer battery life

# WLAN Bands

|Standard|Band|
|:-------|:---|
|802.11 b/g/n|2.4 GHz|
|802.11 a/n/ac/ax|5 GHz|
|802.11p|5.9 GHz (licensed)|
|802.11ah|900 MHz|
|802.11af|700 MHz (unused TV channels)|
|802.11 ad/ay|60 GHz|

# WiFi Channels

The entire band is divided into several smaller channels (22 MHz @ 2.4 GHz, 20 MHz @ 5 GHz).  
An AP operates over a single channel at any given time.  
Different APs will use different channels - avoiding congestion and interference

Newer versions of WiFi can combine two or more channels to get a wider channel.

## Channel Overlap

Try to avoid channel overlap, but this is practically impossible in a household setting as other nearby homes will also have wireless APs.

For 2.4 GHz - A maximum of three non-overlapping channels can be used by using channels 1, 6 and 11.
For 5 GHz - There are many more available channels

# 5 GHz Band

There are two types of 5 GHz channels - General channels and DFS (Radar-possible) channels.

Dynamic Frequency Selection (DFS) - WiFi APs monitor radar channels and vacate them if a radar is detected - this may cause temporary connection drops.  
DFS channels are hardcoded (to their country)

# Hidden Node Problems

CSMA/CD (Collision Detection) is not possible as there are hidden nodes.  
Only CSMA/CA (Collision Avoidance) can be performed - through a 4-way handshake.

1) RTS (Request to Send)
2) **CTS** (Clear to Send)
3) Data
4) ACK

* The **RTS** packet contains the destination address and the duration (time from RTS to ACK) of the message
* The **CTS** packet is broadcasted, so all devices will be able to see it.
  * Other devices set their "network allocation vector" (NAV) and wait for that duration
* As collision cannot be detected, each packet must be ACK'd
* Retransmission occurs in the MAC level if packets are not ACK'd

The _Network Allocation Vector_ stores the duration for which a device should wait for.

# Inter-Frame Spacing

> If all devices waited for the exact same time when the network is busy; there will be collision!

802.11 has different priorities for control, data and time-critical packets.  
This can be achieved by using different IFS times.  
_(high priority packets will be the first to try to request the RTS packet, lower priority packets will see this and stay away from transmitting)_

SIFS - High priority (i.e. ACKs) - Short IFS - Shortest wait duration
PIFS - Medium priority - **P**oint-**C**oordination-**F**unction IFS - Medium wait duration
DIFS - Asynchronous - **D**istributed-**C**oordination-**F**unction IFS - Longest wait duration

PIFS = SIFS + 1 slot time 
DIFS = PIFS + 1 slot time = SIFS + 2 slot times  

Devices also wait for an extra 'random backoff' time.

![](Snipaste_2020-06-17_11-30-47.png)

# Time Critical Services

Contention Free Period - PCF Access (using polling) - The AP will tell you when you can transmit  
Contention Period - DCF Access (free-for-all)

## 802.11 DCF Backoff

MAC works on a FIFO Queue.

* 3 variables
  * Contention Window (CW) (units of slot time)
  * Backoff Count (BO)
  * Network Allocation Vector (NAV)

* If a frame (RTS, CTS, Data, ACK) is heard - NAV is set to the duration in the frame (waits for that duration).  
* If the network is idle for DIFS, and the backoff (BO) is not already active, the station devices chooses a random BO
* If the network is busy during backoff, a new NAV is set.

$ BO = random(0, CW) $  
When transmission successful - $ CW = CW_{min} $  
When transmission unsuccessful - $ CW = min({2CW+1, CW_max}) $

The higher $ CW $ is, the larger the backoff count ( $ BO $ ) can become.

---

# Virtual Carrier Sense

To reduce power usage, instead of continually monitoring for a busy network, timers are used.

Every frame has a duration ID, which indicates how long the medium will be busy for

|Type|Duration|
|:---:|:-----|
|RTS|RTS + SIF + CTS + SIF + Frame + ACK|
|CTS|CTS + SIF + Frame + ACK|
|Frame|Frame + SIF + ACK|
|ACK|ACK|

# Operation

By waiting for the `DIFS` time (the longest delay), we will be able to sense if any other communication has begun.  
This allows nodes to correctly determine if the channel is idle or not during the 4-way handshake

![](Snipaste_2020-06-17_11-34-29.png)

# IEEE 802.11 Architecture

## Basic Service Set (BSS)

The set of stations connected to an Access Point.
BSSID - 48-bit MAC address of the AP  
IBSSID - Randomly generated address - 2 bits are fixed, other 46 randomly generated

FF:FF:FF:FF:FF:FF is for broadcast

## Independent Basic Service Set (IBSS)

Adhoc

---

# 802.11 Frame

![](Snipaste_2020-06-17_11-55-02.png)

## Duration/Connect ID

When used as a duration field, it indicates the time (in microseconds) the channel will be allocated for successful transmission.  

When used in control frames, it contains association or connection identifiers.

## Sequence Control

* 4-bit fragment number subfield - for fragmentation and reassembly
* 12-bit sequence number
* number of frames between given transmitter and receiver

![](Snipaste_2020-06-17_12-00-27.png)

Two bits (toDS and fromDS) are used to control the roles of ADR1-4

# Power Saving

If a device does not need to receive (i.e. channel is busy) - it can save power by sleeping.

* If an AP receives a frame from a device with the power management bit set to `1`, the AP will hold the frames for you until you wake up
* A Traffic Indication Map (TIM) is kept and broadcasted (beacon) by the AP
* When a device wakes up
  * Wait for the beacon
  * Check the TIM to see if the AP has any data
  * If there is data, sends a PS-POLL message to the AP
  * The AP will send the data to device
  * If there is more data, the "More" bit is set
