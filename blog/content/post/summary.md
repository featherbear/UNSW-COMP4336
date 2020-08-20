---
title: "Summary"
date: 2020-08-20T14:12:03+10:00

description: "Course recap summary"
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Physical Layer Fundamentals 

## Decibels

Decibels are a ratio of a signal strength

We use this unit for path loss / attenuation, signal-to-noise ratio, signal power

* dBm - reference to 1 milliwatt
* dBW - reference to 1 watt

**Ratio to dB**

$$ 10\ log_{10}\ (\frac{P_1}{P_2}) $$

_e.g Where $P_1 = 50$, $P_2 = 100$, ratio = $-3\ dB$_

**dB to Ratio**

$$ base^{\frac{dB}{10}} $$ 

_e.g. $17\ dB$ is $10^{1.7} = 50.12 $_

**dBW to dBm conversion**

Due to [logarithm laws](../physical-layer-fundamentals/#decibels), we can just add 30 to a dBW value.

$dBm = dBW + 30$

## Coding

* **Symbol** - the smallest detectable element of a signal
* **Baud Rate** - the rate at which symbols change - $ \frac{modulation\ rate}{symbol\ rate} $
* Data rate - bits per second
  * $ bps = bd \times log_2(M) $ for an M-ary signal
  * $ bps = bd $ for a binary signal

**Modulation**

* ASK - Amplitude Shift Keying
* FSK - Frequency Shift Keying
* PSK - Phase Shift Keying
  * DPSK - Differential Phase Shift Keying - Compare to previous wave
  * QPSK - Quadrature Phase Shift Keying - Look at new phase offset
* QAM - Quadrature Amplitude and Phase Modulation

[Read more](../physical-layer-fundamentals/#modulation)

**Hamming Distance**

The number of different bits, when two sequences are compared.
Increasing the hamming distance between codewords increases the correction rate.

Hamming distance of 3 can detect up to 2 bits of errors, but can only correct one bit errors.

## Channel Capacity

According the Nyquist Theorem, error-free transmission in a **noiseless channel** can only occur when

$ baud\\_rate \le 2 \times bandwidth $

[Read more](../physical-layer-fundamentals/#channel-capacity)

**Shannon's Theory**

The maximum data rate for error-free transmission in a **noisy channel** is $ bandwidth \times log_2(1+\frac{S}{N}) $.

<details><summary>Example: Get required SNR given data rate and bandwidth</summary>

$ 10 \times 10^6 = (5 \times 10^6) \times log_2(1 + S/N) $  
$ 2 = log_2(1 + S/N) $  
$ 1 + S/N = 2^2 = 4 $  

$ S/N = 3 $  

$ 10log(S/N = 3) = 4.77 dB $
</details>

## Multiple Access Methods

* TDMA - Time Division Multiple Access
* FDMA - Frequency Division Multiple Access
* CDMA - Code Division Multiple Access
  * FHSS - Frequency Hopping Spread Spectrum
  * DSSS - Direct Sequence Spread Spectrum
* [OFDMA](../physical-layer-fundamentals-2/#orthogonal-frequency-division-multiple-access---ofdma) - Orthogonal Frequency Division Multiple Access

[Read more](../physical-layer-fundamentals/#multiple-access-methods)

**Duplexing**

Bidirectional communication

* FDD - Frequency Division Duplexing (Full Duplex)
* TDD - Time Division Duplexing (Half Duplex)


## Doppler Shift

Moving radios will affect the frequency.

[Read more](../physical-layer-fundamentals/#doppler-shift)

**Doppler Spread**

Two rays will be received (due to reflections)

* $spread = 2 \times shift$
* coherence time - time which the channel response is constant
  * $ \frac{1}{doppler_spread} $

A symbol should be designed in such a way that it remains for the duration of the coherence time.  
High QAM needed for high data rate

## Antennas

Converts electrical energy into EM waves, as well as EM waves to electrical energy.

**Types of Antennas**

* Omni-directional - All directions
* Directional - Most power in the desired direction
* Isotropic - Radiate in all directions equally

**Antenna Gain**

* Power at a particular point / Power with an isotropic antenna
* Expressed in dBi (Decibel relative to isotropic)

**Antenna Length**

* Antennas are designed to transmit or receive a specific frequency band
* End-to-end antenna length = 1/2 wavelength
* For dipole (two rods), each rod is 1/4 wavelength

## Path Loss

Power lost due to transmission

$$ path\ loss = P_T - P_R $$

* **Small scale fading** - Phase changes due to receiving signals at different times due to multipath transmission
  * Affects amplitude
* **Large scale shadowing** - Sustained signal loss over large distances (i.e. blocked by a building)
  * Affects amplitude

---


**Path Loss Exponent**

Radio waves loss their signal strength exponentially, as modelled by the below 

$$ PL(dB) = 10\ log_{10} (d^n) + C = 10 \times n \times log_{10} (d) + C $$

Other models to exist, which better tune this model to specific variables

---

**Frii's Path Loss Model (Free space)**

* The higher the frequency, the greater the path loss at a given distance

_Linear_  
$$ P_R = P_T G_T G_R (\frac{\lambda}{4 \pi d})^2 = P_T G_T G_R (\frac{c}{4 \pi d f})^2 $$

_Logarithmic_  
$$ log(loss) = 20\ log (d) + 20\ log (f) - G_T\ dB - G_R\ dB - 147.55 $$

<details><summary>Logarithmic Derivation</summary>
$ log(loss) = 10\ log P_T - 10\ log P_R = 10\ log(\frac{P_T}{P_R}) $  
$ log(loss) = 10\ log(\frac{P_T}{P_T G_T G_R (\frac{c}{4 \pi d f})^2}) $  
$ log(loss) = 10\ log(\frac{(4 \pi d f)^2}{G_T G_R c^2}) $  
$ log(loss) = 10\ log (4 \pi d f)^2 - 10\ log (G_T G_R c^2) $  
$ log(loss) = 20\ log (4) + 20\ log (\pi) + 20\ log (d) + 20\ log (f) - G_T\ dB - G_R\ dB 20\ log (c) $  
$ log(loss) = 20\ log (d) + 20\ log (f) - G_T\ dB - G_R\ dB - 20\ log (c) + 20\ log (4) + 20\ log (\pi) $  
$ log(loss) = 20\ log (d) + 20\ log (f) - G_T\ dB - G_R\ dB - 147.55 $  
</details>

**2-Ray Path Loss Model**

* Model is independent of frequency
* Model requires $d > d_break = 4 h_T h_R / \lambda$ (far field distance)

_Linear_  
$$ P_R = P_T G_T G_R (\frac{h_T h_R}{d^2})^2 $$

_Logarithmic_  
$$ 40\ log_{10}(d) - 20\ log_{10}(h_T h_R) - G_T\ dB - G_R\ dB $$

## Signal Reception

**Receiver Sensitivity**

The received signal strength (RSS) has to be greater than a threshold in order to correctly decode information (with low error probability)

* Depends on channel bandwidth, receiver noise, and temperature
* Larger the bandwidth - larger the minimum power
* Larger the receiver noise - larger the minimum power

**Multipath**

Due to reflections, diffractions and scattering, multiple copies of the same signal may be received at different times.

The Line of Sight (LOS) signal reaches the receiver first, followed by the Non Line of Sight (NLOS) signals.

Multipath can be good, as it allows NLOS communication.
However, it can also be bad...  

**Inter-Symbol Interference (ISI)**

Due to the multipath effect, received signals may interfere with each other.
Multipath pulses will generally have less power, so even if some multipath artifacts occur, if their power is not sufficient enough, it won’t cause noticeable interference

**Delay Spread**

The duration that a signal is effectively received for (due to multipath effects).

Delay spread = time between the first LOS and last NLOS signal.

## MIMO

> Multiple Input, Multiple Output

* Multiple antennas for transmitter and receiver
* Allows for multiple paths which won’t interfere
* Improve signal quality and data rate
* Antennas are separated by a distance $ d > \lambda / 2 $
* **Single antenna devices can still benefit from MIMO units**

* Spatial Diversity - Improve reliability
  * Redundancy
  * $paths = n.transmit \times n.receive$
* Spatial Multiplexity - Improve data rate
  * $deg(freedom) = min(n.transmit, n.receive) $
* Beamforming - Increase coverage and signal strength in a particular direction
  * Phase shifts some signals to constructively interfere (increase SNR and range!)

[Read more](../physical-layer-fundamentals-2/#mimo---multiple-input-multiple-output)

## OFDM - Orthogonal Frequency Division Multiplexing

* The next frequency band begins to transmit when the previous transmission reaches its peak amplitude.

* Subcarrier spacing = frequency bandwidth / number of subcarriers
* Large number of carriers -> smaller data rate per carrier -> larger symbol symbol duration -> less inter-symbol interference
* Reduced subcarrier spacing -> Increased ICI due to doppler spread.

**Orthogonal Frequency Division Multiple Access - OFDMA**

2D Scheduling

* Each user uses a subset of subcarriers for a few time slots
* Users are given different frequencies at different times

# WiFi

## 2.4 GHz

There are **fourteen** 22 MHz channels.  
_Note: Channel 14 isn't always available_

A maximum of **three** non-overlapping channels can be used by using channels 1, 6 and 11

## 5 GHz

20 MHz channels.

There are general and DFS (radar) channels

**DFS/Radar Channels**

Certain frequencies in the 5 GHz spectrum is used for RADAR.  
Channels which occupy this frequency subset are known as radar channels.  
They are monitored for any detected RADAR signals, and if detected they will vacate clients.

---

**Taking Turns**

Collision detection is not possible as there may be hidden nodes.  
Only collision avoidance can be performed.

This is done through a four way handshake

* RTS (Request to Send)
* CTS (Clear to Send)
* Data
* ACK

[Read more](../wifi-1/#hidden-node-problems)

**Inter-Frame Spacing (IFS)**

Maths, maths, maths... Add things together and you'll be set.  

[Read more](../wifi-1/#inter-frame-spacing)

---

* Contention Free Period - polling - All devices are required not to transmit
* Contention Period - free for all - DCF access

**DCF Backoff**

* $ BO = random(0, CW) $  
* When transmission successful - $ CW = CW_{min} $  
* When transmission unsuccessful - $ CW = min({2CW+1, CW_max}) $

[Read More](../wifi-1/#80211-dcf-backoff)

---

|Type|Duration|
|:---:|:-----|
|RTS|RTS + SIF + CTS + SIF + Frame + ACK|
|CTS|CTS + SIF + Frame + ACK|
|Frame|Frame + SIF + ACK|
|ACK|ACK|

---

**802.11 Frame**

[Read More](../wifi-1/#80211-frame)

---

## Data Rates

**Error Coding**

* bit stream = original data bits + code bits
* original data bits = bit stream - code bits

We often use this ratio/rate representation `x/y` - `x` data bits for `y` coded bits.

* chip - Code bits in a symbol

**Calculation**

1) Find symbol interval (guard interval + data interval)  
2) Find symbol rate ($\frac{1}{symbol\ interval}$)  

3) Find coded bits per symbol - $log_2 M \times subcarriers$  
4) Find data bits per symbol - cording rate $\times$ coded bits per symbol  

5) **data rate = symbol rate * data bits per symbol**

_Note: `guard interval = 4 x multipath delay spread`_

**Alternate Calculation**

> data rate = coding rate * frequency * data rate / chip rate

<details><summary>Example Question 1</summary>

* 1/2 rate binary convolution encoding
* 2 bits/symbol
* 11 chips/symbol
* DQPSK

Coding Rate: 1/2  
Frequency: 22 MHz  
Data Rate: 2 data bits per symbol  
Chip Rate: 11 chips per symbol

Rate = 1/2 * 22 MHz * 2 / 11 = 2 megabits per second
</details>

<details><summary>Example Question 2</summary>

* Coding: 1/2 rate (1/2 chips per Hz)
* Chip Rate: 8 chips to code a symbol
* Modulation: 16 QAM
* Frequency bandwidth: 22 MHz

**What is the data rate?**

It will take 2 Hz to produce one chip.  
22 MHz * 1/2 = 22 MMz / 2 = 11 Mcps (Megachips per second)

11 / 8 = 1.375 - Chips per second / Chips per symbol

16 QAM -> $log_2 16 = 4$ bits  

1.375 * 4 = 5.5 Mbps

</details>

---
* Subcarriers = channel bandwidth / subcarrier spacing
  * Refer to tables and data for the data carriers

Remember: With $M$-ary modulation - $log_2 M$ data bits

[Read More](../wifi-2/#guard-interval)

![](../wifi-2/2020-06-26_01-32-48.png)

---

# 802.11af-2014 - White-Fi

Uses the free/whitespace of the 700 MHz spectrum for WiFi usage.

Software defined radio (SDR) to digitally reproduce different radio modes

* Data rate (single stream single channel) - 26.67 Mbps
* Max data rate (4 streams, 4 channels) - 26.67 * 4 * 4 = 426.7 Mbps

---

# 802.11ah-2017 - HaLow

* 900 MHz
* Low power consumption - good for IoT!

Like 802.11ac, but downclocked by 10x.  

Bunch of stuff to allow for low power consumption; shorter headers, null data packets, DTIM wakeup,intervals, deferral

[Read more](../802.11ah)

# 802.11ad-2012 - WiGig

* 60 GHz
* It's faaaaaaaaaaaaaaaast
* But it gets blocked very easily due to its high frequency
* Also is very directional - must be aligned to get a good signal

* Beamforming - Used to accurately pinpoint where to position antenna directions

[Read more](../802.11ad)

# 802.15 - Bluetooth

**Overview of Bluetooth**

* Battery powered (long battery life)
* Dynamic topologies (Short connections, sleep)
* No infrastructure (everything is ad-hoc)
* Avoids interference from other devices/technologies
* Simple and Interoperable
* Cheap!

---

* **Piconet** - a Bluetooth network
* One master device, up to 255 slave devices
  * Only 7 slave devices can be active at a time
  * Slave devices can _only_ communicate with the master device
* Master device in charge of orchestrating communication

* Parked - Devices that are "parked" are not active, but can become active in 2ms.

* **Scatternet** - Multiple networks with a common device
  * That device can only be active in one piconet at a time, but can be parked in the other piconets.

---

There are 79 1 MHz channels.

$$ f_c = (2402 + k )\ \text{where}\ k \in \{0..78\} $$

**Modulation and Data Rate**

* Basic Rate (BR)
* Enhance Data Rate (EDR)

**Packet Format and Headers**

... Ehh see the [actual post](../bluetooth-802.15.1/)

**Frequency Hopping**  

Channels are hopped switched to avoid collisions with other nearby BT communications.  
3200 Hz clock is used (312.5 us per tick).
2 ticks = 625 us.

* Time Division Duplexing (TDD) used to decide who communicates
  * Master uses even slots
  * Slave uses odd slots
* Packets can be other 1, 3 or 5 slots long - keeping the even/odd ordering

Channel hopping occurs after an entire packet has been transmitted / end of the slot group.

Minimum frequency hop rate (when all packets are 5 slots long) - 320 Hz
Maximum frequency hop rate (when all packets are 1 slot long) - 1600 Hz

Hopping algorithm is decided by a seed generated by the UAP and LAP of the master device, as well as the first 26 bits of the 28-bit clock.

**Adaptive Frequency Hopping (AFH)**  

As Bluetooth operates around the 2.4 GHz frequency spectrum, there may be interference with WiFi.  

The master device creates a channel map, containing a list of channels that are available, in used (by another piconet), or bad (clashing with another wireless protocol).

**Bluetooth States**

* Disconnected - Standby
* Connecting - Inquiry, Page
* Active - Transmit, Connected
* Low Power - Park, Sniff, Hold

**Bluetooth Low Energy (BLE)**

* Different physical layer to Bluetooth Classic.  
* 40 channels (2 MHz) wide
  * 0-36 - Data
  * 37, 38, 39 - Advertising channels

* BLE Hopping Algorithms (#1)
  * $f_{k+1} = (f_k + h) mod 37$
  * Adaptive frequency hopping - jumps to another channel if the attempted channel is bad
  * Refer to [lab](../labs/lab6/) for explanation

**Bluetooth 5**

* 2M Mode - decreased symbol duration (1ms to 500 ns)
  * 2x faster!
* Coded mode - Slower, but more error coding
  * 4x Range

---

# Cellular Networks

* Tessellated cells to avoid coverage gaps
* Clusters are a group of cells such that each cluster uses up the entire frequency spectrum
* Co-channels are cells that use the same channel frequency

* NSK Notation / Frequency Reuse

* Handoff
  * Devices change base station when the RSS from another base station is stronger

[Read more](../cellular-networks/)

---

# Mobile IP

## IP Mobility

A location server tracks the location (subnet) of a device, helps routers forward the packets correctly.  

* Mobile hosts have two IP addresses
  * Home address (permanent)
  * Care of address (temporary address)

* Home agent -> foreign agent -> mobile hosts

A router with multiple IP addresses can have a forward agent installed on it, where it assigns an address to each device. **DHCP not used!**

## Network Mobility

Entire moving subnet.

**NEMO**

* Onboard router
* Onboard fixed device
* Onboard user device (IP in IP in IP)

* Multihoming - multiple connections to the home agent over different links
  * Redundancy and load balancing

* IPv6 devices
  * Don't need DHCP - can use the MAC address to generate its IP address.
  * IPv6 Type 2 can include two IP address pairs, meaning that no IP-in-IP tunnelling is needed

## Proxy Mobile IP

> For campus / site networks

Software is installed on the network edge devices (i.e. access points) rather than the client devices.

* LMA - Local Mobility Anchor
  * The master device
* MAG - Mobile Access Gateway
  * The client devices

Data from the WAN first goes to the LMA.
The MAG stations see if the Mobile Host is attached to them, and notifies the LMA.
The LMA then forwards the packet to that specific MAG, which sens the packet to the Mobile Host.

---

# Wireless Power Transfer

**SWIPT** - Simultaneous Wireless Information and Power Transfer

Ambient and dedicated sources

* Out-of-band energy harvesting (EH) - separate frequencies and antennas.
* In-band energy harvesting - Same signal

**Methods of doing both energy harvesting and communication**

* Separate antennas
* Time switching
* Power splitting

---

# RF Sensing

* Activity Recognition
* Gesture Recognition
* Fall Detection

Can use metrics such as

* RSS - Received Signal Strength - Average signal amplitude
* CSI - Channel State Information - Detailed amplitude and phase
* TOF/TOA - Time of Flight/Arrival - Range
* Doppler Shift - Velocity
