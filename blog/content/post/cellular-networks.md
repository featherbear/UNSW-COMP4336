---
title: "Cellular Networks"
date: 2020-07-22T09:24:25+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

* Adjacent cells that service the area
  * Frequencies are repeated between the cells

## Different Cell Sizes

* macro - sections of a city - > 1km
* micro - neighbourhoods - < 1km
* pico - busy public areas - 200m
* femto - inside a home - 10m

## Cell Geometry

All cells should have identical geometry such that their cells 'tessellate' - as to avoid any coverage gaps.

Equilateral triangle, square, hexagon.

* Hexagon is the best, as it has the widest coverage

## Clusters

* Cells can be grouped into **clusters**, where each cluster uses up the entire spectrum.
* **Co-channels** are cells which use the same channel frequency

* $D$ - minimum distance between co-channels
* $R$ - radius of a cell
* $d$ - distance between centers of adjacent cells
  * $ d = R \sqrt(3) $
  * $D < 2R $ due to overlapping cells
* $N$ - number of cells in cluster

* Frequency Reuse Factor = $1/N$
* Reuse Ratio = Distance / Radius = $D/R$ = $\sqrt{3N}$
* $D/d = \sqrt{N}$

<!-- $d \sqrt{N} = R \sqrt{3N}$ -->

## For hexagonal cells

> $N = I^2 + J^2 + (I \times J)$  

Where

* $I = 0, 1, 2, 3 ...$  
* $J = 0, 1, 2, 3 ...$  

### To locate co-channel cells

* Move `i` cells in any direction
* Turn 60 degrees counter clockwise
* Move `j` cells

---

> What would be the minimum distance between the centers of two cells with the same band of frequencies if cell radius is 1 km and the reuse factor is 1/12?

```
R = 1km
Reuse Factor is 1/12; N = 12

D/R = sqrt(3N)
D = R sqrt(3N)

D = 1km * sqrt(3 * 12)
D = 1km * sqrt(36)
D = 1km * 6
D = 6km
```

## Frequency Distribution

Assuming the spectrum is divided equally amongst cells.

* $T$ - Total Channels
* $N$ - Cluster size
* $K$ - Channels per cell

$K = T/N$  

Cells are usually then divided into **sectors**, which are grouped in a way to minimise interference/overlap.  
These sectors are directional (only devices in that direction will receive a signal from that sector)

## NSK Notation (Frequency Reuse)

$N \times S \times K$

* $N$ - Cluster size
* $S$ - Sectors per cell
* $K$ - Channels per cell

(Reminder, $K = T/N$)

e.g. `1 x 3 x 3`

Cluster size of 1, 3 sectors per cell, 3 channels per cell.

* NSK does not capture the frequency distribution among sectors

![](2020-07-24_01-11-18.png)

SS - Subscriber Station

## Fractional Frequency Reuse

Users close to a base station use all the frequencies.  
Users at the cell boundary use only a fraction of the available frequencies.  
Border frequencies are designed to avoid interference with adjacent cells

## Handoff

Changing base station when the signal strength (RSS) from another station is stronger than the connected station.

The new base station must have available channels to support the new client.  
The base station reserves some channels (known as **guard channels**) which are exclusively used to support handing off calls.  
Guard channels however, increase the probability of _new_ calls being blocked.  

The guard channel count is not standardised, and left up to the telco operator to optimise

---

![](2020-07-24_01-21-02.png)

### FDMA/FDD

* FDMA - Frequency Division Multiple Access
* FDD - Frequency Division Duplex

* Frequency range: 949-900 MHz -> 49 MHz
* 49 MHz / cluster size = 49 / 7 = 7 MHz per cell
* 7 MHz / 2 = 3.5 MHz uplink, 3.5 MHz downlink
* Supports 3.5 MHz * 1 bps/Hz = 3.5 Mbps
  * 3.5 Mbps / 10 kbps = 350 concurrent users
* Cell Area
  * 350 users / 100 users/km^2 = 3.5 km^2 cells
* Cell Radius
  * $\pi r^2 = 3.5$
  * $r = 1.056 km$

### TDMA

* Bandwidth: 3.5 MHz per cell  
* Channel bandwidth: 3.5 MHz / 35 = 100 KHz / channel
* Data Rate: 100 KHz * 1 bps/Hz = 100 kbps
* Time slots: 100 kbps / 10 kbps per user = 10 time slots
* Time per slot: 10ms / 10 = 1ms
* Bits per slot: 1ms * 100 kbps -> 10 kbps

---

# LTE

* Many different bands - 700,1500,1700,2100 (common),2600
* Flexible bandwidth - 1.4,3,510,15,20
* FDD
* TDD
* 4x4 MIMO
* Beamforming

## Structure

* Superframes (10ms)
  * Contains 10 subframes (1ms long)
    * Contains 2 slots (0.5ms long)
      * Each slot is 6 or 7 symbols long
      * 1 symbol = 66.7 us (1/15 kHz)

![](2020-07-24_01-46-20.png)

* Cyclic Prefix (the preamble (shaded part)) - 5.2 us for the first symbol, then 4.7 us
* Extended Cyclic Prefix - 16.7 us each

## Resource Allocation (OFDMA)

* Each time slot is 0.5 long
  * 6 or 7 OFDM symbols
* Subcarriers 15 kHZ wide
* Physical Resource Blocks (RB)
  * 12 subcarriers (180 kHz) over 1 time slot
* It is possible for at least 2 RBs to be transmitted per frame

---

> For normal cyclic prefix (CP), how many resource elements (REs) are there in 2 RBs?

Normal CP - 7 symbols per slot  
REs per RB = 12 * 7 = 84  
REs per 2 RBs = 168

---

## Transmission Bandwidth

(Multiply by 5.5555555)

![](2020-07-24_01-53-32.png)

---

> What is the transmission bandwidth for a resource allocation of 10 RBs?

Each RB = 180 kHz  
Transmission Bandwidth = 10 x 180 = 1.8 MHz

# Carrier Aggregation

Transmitting data through different bands.

Maximum of 5 component carriers -> 100 MHz.

Each component can be a different width (1.4,3,5,10,20 MHz)

`Number of components in DL > Number of components in UL`

# Coordinated Multipoint Operation (CoMP)

Base stations coordinate transmissions and receptions to devices at cell edges to improve performance

* Single Tx (DL) - Only one BS transmits in each frame
* Joint Tx (DL) - Multiple transmitters in the same subframe
* Joint Reception (UL) - Multiple BSs receive the signal from one UE and combine
* UE is informed about the different options

![](2020-07-24_01-59-56.png)

# 5G

* 20 Gbps peak rate
* 100 Mbps user experienced data rate
* 100 Mbps/m^2 area traffic capacity
* 3x spectrum efficiency
* 500 km/h mobility
* 1ms latency
* 10^6 devices/km^2 connection density
* 100x network energy efficiency

---

* Enhanced mobile broadband
* Ultra-reliable and low latency (Realtime and safety applications)
* IOT

# 6 GHz Considerations

* Huge loss at high frequencies.
* Difficult!

---

![](2020-07-24_02-05-54.png)

