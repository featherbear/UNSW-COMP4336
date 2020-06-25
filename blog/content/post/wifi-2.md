---
title: "WiFi 2"
date: 2020-06-24T09:30:42+10:00

description: "802.11 technologies"
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

Highest data rate isn't always the best.
Have to consider the SNR.

* `Data rate = Symbol rate * Data bits per symbol`
* Chip - Code bits in a symbol


## IEEE 802.11b - 1999

* Uses the Direct Sequence Spread Spectrum
* 1 bit/symbol
* 10 chips/symbol

# 802.11-1997

* 1/2 rate binary convolution encoding
* 2 bits/symbol
* 11 chips/symbol
* DQPSK

`Data Rate = Encoding rate * Frequency * Data rate / chip rate`  
DQPSK = 1/2 * 22 MHz / 11 chips per symbol * 2 data bits per symbol = 2 megabits per second

## 802.11b-1999

1/2 rate binary convolution encoder at 8 bits/symbol, 8 chips/symbol  
Complementary Code Keying (CCK)

`Data Rate = Encoding rate * Frequency * Data rate / chip rate`  
CCK = 1/2 * 22 * 8/8 = 11 Mbps

## Example Question

1/2 rate (1/2 chips per Hz)  
8 chips to code a symbol  
16 QAM  
22 MHz  

It will take 2 Hz to produce one chip.

22 Mhz / 2 = 11 Mcps (Megachips per second)  
11/8 = 1.375 - Chips per second / Chips per symbol  
log2 16 = 4  
1.375 * 4 = 5.5 Mbps  

---

# OFDM

Bits per symbol depends on the modulation order and subcarrier structure.  
Total number of subcarriers = channel bandwidth / subcarrier spacing.

There are three categories of subcarriers  

* Data - Data
* Pilot - Known symbols to check synchronisation
* Guard - Sort of like dummy channels

Each OFDM is carried over all data subscribers in parallel.

* $M$-ary modulation - $ log_2 {M} $ bits per data subcarrier
  * i.e. 16QAM is $ log_2 16 = 4 $ bits per data subcarrier

Number of raw coded bits = $ log_2 {M} $ * number of data subcarriers

## Impacts of Error Coding on Data Bits Per Symbol

`Coded bit stream = original data bits + code bits`  
So, `data bits = coded bits - code bits`  

We often use this as ratio/rate - `x/y` - x data bits for y coded bits.

Data bits per symbol = coding rate * log_2 M * number of data subcarriers

---

# Parameters affecting WiFi data rate

* Modulation - affects number of bits per second
* Coding - affects error correction overhead
* Guard interval - affects symbol rate
* Channel width - affects number of data subcarriers
* MIMO streams - overall throughput

# IEEE802.11a-1999

* 5GHz
* Uses OFDM
* 20 MHz channel width
* 64 subcarriers
  * 6 guard subcarriers at each side
  * 4 pilot subcarriers
  * 48 data subcarriers to use
* Symbol interval of 4 microseconds
  * 0.25 million symbols per second
  * 3200ns (data) + 800ns (guard)
* Supports BPSK, QPSK, 16QAM, 64QAM
* Supports 1/2, 2/3, 3/4 coding rate
* Supports 8 (as opposed to 4x3=12) different data rates, 6 Mbps up to 54 Mbps - depending on the **modulation and coding scheme (MCS)**

![](2020-06-26_01-30-16.png)

---

# IEEE802.11g-2003

* Achieved 54Mbps on 2.4GHz using OFDM

# IEEE802.11n-2009

* First spec to use MIMO
* Frame aggregation - multiple frames in one
* Reduced IFS (SIFS is 2 us instead of 10 us)
* Greenfield Mode - Can disable support for a/b/g (shorter and higher rate preamble)
* Dual Band - 2.4 and 5 GHz
* Lower FEC overhead - 5/6 instead of 3/4
* Channel Bonding - Can combine two 20 MHz channels to form a 40 MHz channel
* Shorter Guard Interval - 400ns instead of 800ns
* More OFDM subcarriers - Shorter GI in time domain, less guard carriers needed
  * 4 guard carriers (per side) instead of 6 (per side)
  * 52 instead of 48 data carriers (20 MHz channels)
  * 108 (52 * 2 + 4) data carriers in 40 MHz channels (no guard channels needed between)

## Guard Interval

Generally, `guard interval = 4 x multipath delay spread`

If agreed, a guard interval of 400ns can be used.  
(3200ns + 400ns GI)

---

![](2020-06-26_01-32-42.png)  
![](2020-06-26_01-32-48.png)

* Single Stream Data Rate - https://www.cablefree.net/wirelesstechnology/wireless-lan/data-rates-in-802-11n

![](2020-06-26_01-32-00.png)

* Multi Stream Data Rate - https://www.cablefree.net/wirelesstechnology/wireless-lan/data-rates-in-802-11n

![](2020-06-26_01-32-08.png)

## Frame aggregation

Each layer has Service Data Units (SDUs) as inputs.  
Each layer makes Protocol Data Units (PDUs) as outputs to communicate with the corresponding layer at the other end.  
_Note: PDUs create overhead from their headers._  

Frame Aggregation: Multiple SDUs in one PDUs.  
All SDUs must have the same transmitter and receiver address

## Channel State Information (CSI)

High Throughput Control field in the wireless packet to exchange CSI data.  
Receivers can derive the CSI from the pilots, but the transmitter cannot derive - and needs to be notified.

# IEEE 802.11ac

* 5 GHz only
* 20, 40, 80, 160 MHz channels
* 52+4, 108+6, 234+8, 468+16 data subcarriers - `data+pilot`
* Up to 256QAM
* Up to 8 MIMO streams

![](2020-06-26_01-35-03.png)

![](2020-06-26_01-35-11.png)

![](2020-06-26_01-36-26.png)

* Data Rate - https://www.cablefree.net/wirelesstechnology/wireless-lan/data-rates-802-11ac/

![](2020-06-26_01-35-21.png)

## Multi-User MIMO

MIMO - Uncorrelated spatial beams, separated by \lambda/4 or \lambda/2  

MU-MIMO - Two single antennas users can act as one multi-antenna device. The users are unaware of this configuration

Beamforming can be used to direct the different streams.

802.11ac improves over 802.11n in three dimensions

* Higher channel bandwidth
* More spatial streams
* More data bits per subcarrier


# IEEE 802.11ax

Previous evolutions focused on increasing the speed - however it is hard to attain that actual throughput due to congestion, collisions and interference.  
802.11ax instead aims on attaining **high efficiency** - Works efficiently in dense deployments.

* Supports 2.4 GHz and 5 GHz
* Max coding rate: 5/6 (no change)
* Max channel width: 40 MHz @ 2.4 GHz; 160 MHz at 5 GHz (no change)
* Max MIMO streams: 8 (no change)
* Max modulation rate: 1024QAM (10 bits)
* Increased symbol interval - to address longer delay spread in challenging environments
  * Symbol data interval increased to 12.8 us
  * Guard interval increased to 0.8 us, 1.6 us or 3.2 us
* OFDM subcarrier spacing reduced to 78.125 kHz
  * _Total subcarriers = data + pilot + guard + DC + null_
  * 20 MHz - 256 subcarriers, 234 data subcarriers
  * 40 MHz - 512 subcarriers, 468 data subcarriers
  * 80 MHz - 1024 subcarriers, 980 data subcarriers
  * 160 MHz - 2014 subcarriers, 1960 data subcarriers

![](2020-06-26_01-38-14.png)

![](2020-06-26_01-37-10.png)

![](2020-06-26_01-37-02.png)

## OFDMA - Orthogonal Frequency Division Multiple Access

* 2D frequency and time allocation
* Split into Resource Units (RU)
* Subcarriers of 78.125 kHz
* Subcarriers are grouped into RUs called tones
* 26, 54, 106, 242, 484 or 996 tones per station.
* Each tone consists of a single subcarrier of 78.125 kHz
  * Smallest resource allocation / tone is 26 * 78.125 kHz = 2031.25 kHz ~= 2 MHz
  * Largest resource allocation / tone - 996 * 78.125 kHz = 77812.5 kHz ~= 80 MHz
* A station can have a maximum of two 996 tones

![](2020-06-26_01-38-29.png)

![](2020-06-26_01-38-40.png)

![](2020-06-26_01-37-56.png)

![](2020-06-26_01-37-42.png)