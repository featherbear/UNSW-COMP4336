---
title: "Wireless Power Transfer and Sensing"
date: 2020-08-07T07:30:42+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Uses of RF

* Can be used for wireless communication
* Can be used for wireless power transfer
* Can be used for sensing - remote sensing of humans and other phenomena

# SWIPT

> Simultaneous Wireless Information and Power Transfer

Can transfer power wirelessly (remotely powered toy helicopter!)

* Ambient source - TV, Radio, Cellular towers
* Dedicated - Static RF sources, Mobile sources, Hybrid sources

_Example devices: Powercast - 915 MHz TX91501_

Energy harvesting (EH) often requires -10 dBm sensitivity, whilst information decoding is possible even at -60 dBm.

![](2020-08-07_08-31-39.png)

## Out of Band EH

* Separate frequencies are used for energy and communication
* Requires separate antennas

## In-Band EH

* Same RF signal used for both energy and communication

However, we **can only perform one operation at a time** on the signal.  

* separate antennas
* time switching - switch between energy and communication use
* power splitting - split the signal into two weaker signals

### Separate Antenna

Device will be larger due to having two antennas, and also the distance from the placement of the antennas.  
Will also be more costly.

* Entire signal power available for energy harvesting
  * $ P_H = P_R \times \eta $
  * $\eta$ is the RF-DC conversion efficiency (ratio)
* No additional noise for information processing
  * $C = Wlog(1+P_R/P_N)$
  * $P_N$ is the thermal/antenna noise

### Time Switching

Device will switch between energy harvesting and information decoding.  
Consequently, operation will only be able to use half of the total available time 

* Entire signal power available for energy harvesting
  * $ P_H = P_R \times \eta $
  * $\eta$ is the RF-DC conversion efficiency (ratio)
* No additional noise for information processing
  * $C = Wlog(1+P_R/P_N)$
  * $P_N$ is the thermal/antenna noise

### Power Splitting

Both EH and ID can occur at the sime time, but energy is lost.

* Entire signal power available for energy harvesting
  * $ P_H = P_R \times \theta \times \eta $
  * $\theta$ is the fraction of received signal used for EH
  * $\eta$ is the RF-DC conversion efficiency (ratio)
* Additional signal processing noise
  * $C = Wlog(1+P_R\frac{1-\theta}{P_N+P_{SP}})$
  * $P_SP$ is the power of signal processing noise
  * $P_N$ is the thermal/antenna noise

## Power to Energy

Power is the _rate of energy_ (joules per second).  

$$ E_H = P_H \times T $$

However, $P_H$ may vary over time - interference, distance, etc

$$ E_H = \sum_i P_{H_i} \times T_i $$

---

Depending on the $\eta$ value (RF-DC conversion efficiency), we will actually have less usable power than that!

i.e at $-60\ dBm$, $\eta = 0.5$ ... We only have $500\ pW$ of usage power.  
$10^{-6} \times 0.5 = 500\ pW$

---

### Can a WiFi AP be used as an ambient source?

![](2020-08-07_09-23-01.png)

---

# RF Sensing

* Activity Recognition
* Gesture Recognition
* Fall Detection

![](2020-08-07_12-39-57.png)

## Metrics

* RSS - Received Signal Strength - **Average** signal amplitude
* CSI - Channel State Information - Detailed amplitude and phase
* TOF/TOA - Time of Flight/Arrival - Range
* Doppler Shift - Velocity

### Channel State Information

$$ y = h(x) + n $$

CSI estimation involves estimating $h$.

$$ Ae^{j\theta} $$

* $\theta$ - phase
* $j$ = $\sqrt{-1}$

$$ a+jb $$

* amplitude = $\sqrt{a^2 + b^2}$
* phase = $tan^{-1} \frac{a}{b} $


Can be used for **Human sensing**, with a CSI time series

CSI is used in the PHY layer, to help wireless devices switch the best channel and data rates.
Software like [`nexmon`](https://github.com/seemoo-lab/nexmon) can be used to extract the CSI values

### Time of Flight / Time of Arrival

Range = TOF x Speed of Light

#### RADAR application - FMCW

> Frequency Modulated Continuous Wave

A radio wave is emitted with a linear chirp.

Linear Chirp - frequency increase at a known constant rate.  

The transmitter and receiver are both located on the same hardware.  
By detecting the received frequency and time taken to receive the signal, we can calculate the distance.  

We can even detect multiple signals - allowing us to detect multiple objects.

### Doppler Effect

> Doppler Effect - frequency changes depending on velocity

Radial velocity of different body parts can be obtained from the doppler shift.

$$ v = \frac{\Delta f \times c}{f} $$

* Using FFT, we can estimate the doppler and velocity from FMCW range data, and CSI (less accurate)
