---
title: "Bluetooth 802.15"
date: 2020-07-15T15:14:40+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# WPANs (Wireless Personal Area Networks)

A personal network within a small area (~10 meters)

Considerations

* Battery powered (long battery life)
* Dynamic topologies (Short connections, sleep)
* No infrastructure (everything is ad-hoc)
* Avoids interference from other devices/technologies
* Simple and Interoperable
* Cheap!

# RN4020 BLE Microchip

* ISM Band: `2.402` - `2.480` GHz
* RX: -92.5 dBm (Requires a RSS greater than -92.5 dBm to pick up a signal)
* TX: -19 dBm (12 uW) to 7.5 dBm (5.6 mW)

# Bluetooth (IEEE 802.15.1)

* Bluetooth 1.1 (IEEE 805.15.1-2002)
* Bluetooth 1.2 (IEEE 805.15.1-2005) - Adaptive frequency hopping
* Bluetooth 2.0 (2004) - Enhanced data rate. 3 Mbps using DPSK. Reduced power due to reduced duty cycle
* Bluetooth 4.0 (2010) - Bluetooth Low Energy - Different PHY layer
* Bluetooth 5.0 (2006) - Better BLE

Note Bluetooth 2.0, 4.0 and 5.0 are NOT by the IEEE, but by SIG (Signal Interest Group)

# Bluetooth Classic

## Topology

### Piconet

In Bluetooth terminology, a network is called a `piconet`.  

There is one master device, and up to 255 slave devices (each with an 8-bit address).  
Of these 255 slave devices, only 7 slave devices can be active.  

They are polled by the master device when it is their turn to transmit.  

Slave devices can **only** communicate with the master device

_A parked device only needs around 2 ms to become active again_

### Scatternet

A device can be part of multiple piconets.  
In the even of this, the device will need to synchronise itself to the new master device.  

The device will be active in one piconet, and parked in the other networks.

## Channels

There are 79 `1-MHz` channels.  

$f_c = (2402 + k ) $ where $ k \in \{0..78\} $

## Modulation and Data Rate

### Basic Rate (BR)

* Binary Gaussian FSK (GFSK) - 1 bit/symbol
  * (Gaussian aka smooth ('sine' wave rather than a square wave))
* Symbol duration = 1 us = 1 Msps
* Data rate: 1 Mbps

### Enhanced Data Rate (EDR)

* Symbol duration = 1 us = 1 Msps
* u/4-DQPSK - 2 bits/symbol - 2 Mbps
* 8DQPSK - 3 bits/symbol - 3 Mbps

## Packet Format for Basic Rate

* Access Code - 68-72 Bits
* Header - 54 Bits
* BR Payload - 2745 Bits

* Max packet size is 72+54+2745 = 2871 us
  * 5 slots (5 * 625 us = 3125 us)
  * Packet size less than total possible, as some part of the slot is reserved for sync

* Access Code
  * Channel access code - Identify the piconet
  * Device access code - paging requests and response
  * Inquiry access code - discovery

* Header payload (18 bits)
  * 3 bits - member address
  * 4 bits - type code
  * 1 bit - flow control
  * 1 bit - ack/nack
  * 1 bit - sequence number
  * 8 bits - header error check
* Header uses 1/3 rate FEC (error coding), so results in 18*3 = 54 bits

* Time: 2871 us

> How many slots for a 400 bit payload?  
Each slot can carry 625 bits at most; inclusive of the 126 bit metadata

## Packet Format for Enhanced Data Rate (EDR)

* Access Code (72 bits)
* Header (54 bits)
* Guard Inteval (4.75 us to 5.25 us)
* Sync (30 bits)
* Payload Header (16 bits)
* EDR Payload (8168 bits compared to 2745 BR)
* Trailer (6 bits)

* GFSK is used for the Access Code, and Header
* DPSK is used for the Sync, Payload and Trailer

* Time: 2872.25 us
  * This packet still fits in a 5-slot time (3125 us)

* Start with GFSK, until the receiver knows that it is an EDR packet; then switch to DPSK

## Address Format

![](2020-07-16_19-43-42.png)

Unique 48-bit address contained in the access code

* The first 24 bits represent the OUI (Organisation Unique Identifier) / Company ID
* Purpose: Identification and authentication, pseudorandom seed

## Frequency Hopping (FHSS)

* Bluetooth communication continually switches channels (in the same connection) to avoid collisions with other nearby Bluetooth communications
* Bluetooth uses a 3200 Hz clock (312.5 us per tick)
  * 2 ticks = 625 us
* Time Division Duplex is used to decide who communicates
  * Master uses even slots
  * Slaves use odd slots
* Packets can be 1 slot, 3 slots or 5 slots long
  * Odd numbering allows the master/slave to be the next
* Frequency hopping is performed at slot boundaries, and never hopped during a packet
* Minimum frequency hop rate (when all packets are 5 slots long) - 320 Hz
* Maximum frequency hop rate (when all packets are 1 slot long) - 1600 Hz

---

* Channels change in a pseudorandom fashion - seeded by the UAP and LAP address of the master device, as well as bits 1-26 of the 28-bit Bluetooth clock

## Adaptive Frequency Hopping (AFH)

> 2.4 GHz Bluetooth co-existence with WiFi

Interfering channels are marked as bad channels - which are not hopped to.  
The minimum number of good channels is 20 (59 bad channels), before BT breaks

The master creates a channel map, which contains a list of which channels are available, used (by another piconet), or bad.

## Bluetooth States

There are 8 distinct states which belong to 4 categories  

Disconnected - Standby  
Connecting - Inquiry, Page  
Active - Transmit, Connected  
Low Power - Park, Sniff, Hold  

\[Inquiry] - Broadcasted by the Master device.  
Slave devices scan for the inquiry, and respond with their address and clock after a random delay (CSMA/CA)

\[Page] - Master sends a page (info about its address and clock) to slave devices, to join its piconet.  
Slave devices enter page response state and respond to the master

\[Connected] - A 3 bit address (member address in the control header) is assigned to the slave)

\[Hold] - Go inactive for a short period of time  
\[Sniff] - Listen periodically after an interval
\[Park] - Gives up its 3-bit active member address, and receives an 8-bit parked member address. Wakes up periodically to listen to beacons.

### Flow

![](2020-07-17_00-11-04.png)

![](2020-07-17_00-13-03.png)

# Bluetooth Low Energy (BLE) / Bluetooth Smart / Bluetooth 4

* 1-50% of BT Classic power consumption
  * Battery life in years
* For short broadcasts
* Lower cost
* Star topology
* Uses a different PHY layer (based on Nokia's WiBree technology)
  * Does not work with BT Classic

* Only has 40 channels (2 MHz wide)
  * 3 channels (37, 38, 39) - advertising
  * 37 channels (0-36) - data

## Modulation and Data Rate

* Binary GFSK
* The wider channel widths (2 MHz) allow for longer range communication with lower power
* 1 Mbps

## Advertising Channels

ONLY three advertising channels (37, 38, 39)!  

Can be used to have connection-less broadcasts of 'advertising beacons'.  
Chosen specifically to not interfere with the popular WiFi channels (1, 6, 11)

31 byte advertising payloads

## Connection Flow

As opposed to BT Classic, where frequency hopping occurs after every slot, BLE frequency hopping occurs every 'connection interval' (7.5ms to 4s)

## Bluetooth GATT

Devices as Gateway - small signal from the BLE device connects to a phone, which then makes a URL request, etc

### Hopping Algorithm #1

Fixed hopping algorithm

$f_{k+1} = (f_k + h) mod 37$

Where $h$ is a fixed value negotiated during connection setup.

Note: There are 37 data channels (0-36)

* Adaptive FH: If the hop lands on a bad channel, it is remapped

# Bluetooth 5

* 2x Faster than BLE
* 4x Longer range than BLE

* Contains two new PHY modes

## 2M Mode (2x Speed)

2x Faster Speed by decreasing the symbol duration to 500 ns.  

This will however lead to inter-symbol interference.  
To mitigate this, we can increase the frequency deviation (increase the distance between the frequency for `1` and the frequency for `0`)

## Coded Mode (4x Range)

4x Longer range by implementing a code

* FEC (Forward Error Control) by 1/4
* 250 Kbps -> 4x range increase

Note: BLE and BT Classic do not employ any FEC

## Advertising Extension: Channel Offload

Only the header is transmitted over the advertising channel.  
The payload is offloaded to a data channel, which devices can tune into to listen to.

255 byte advertisement payloads

Multiple 255 byte packets can be chained together!

## Hopping Algorithm #2

Pseudorandom frequency hopping

