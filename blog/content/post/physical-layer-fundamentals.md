---
title: "Physical Layer Fundamentals"
date: 2020-06-03T10:19:06+10:00

hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

# Frequency, Period, Phase

* Frequency - $ f $
* Period - $ T = 1/f $
* Phase - $ \phi $
* Amplitude - $ A $
* Wave - $ A \sin(2 \pi ft + \phi) $

# I-Q Graph

The I-Q graph is a 2D representation of the phase and amplitude.

In-phase component $ I $ + Quadrature component $ Q $

> $ \sin(2 \pi f t + \frac{\pi}{4} ) $  
= $ \sin(2 \pi f t) \cos( \frac{\pi}{4}) + \cos(2 \pi f t) \sin (\frac{\pi}{4}) $  
= $ \frac{1}{\sqrt{2}} \sin(2 \pi f t) + \frac{1}{\sqrt{2}} \sin (2 \pi f t) $

# Wavelength

The distance occupied by one cycle of a wave

$ \lambda = vT $  
$ \lambda f = v $

$ c = 3 \times 10^8 m/s $

$ \lambda = c/f $

e.g 2.5 Ghz to Wavelength  
$ \lambda = \frac{300 m/\mu s}{2.5 \times 10^9} = 12 cm $

e.g 5mm to Frequency  
$ f = \frac{300 m/\mu s}{0.005} = 60 GHz$

# Time and Frequency Domain

* Time Domain
* Frequency Domain

# Wireless Spectrum Allocation

* Maximise utilisation
* Adapt to market needs
* Fair licensing
* Promote competition
* Ensure spectrum availability
* Licensing

# Decibels

The unit to measure power, loss, signal-to-noise ratio (SNR)

When measuring power, we have a very large scale (i.e. pico watts to kilo watts)

$ dB = 10 \log_{10}(\frac{P_1}{P_2}) $  

* Path Loss / Attenuation
  * $ P_1 $ - Transmit
  * $ P_2 $ - Receive
* SNR
  * $ P_1 $ - Signal
  * $ P_2 $ - Noise
* Signal Power
  * $ P_1 $ - Signal
  * $ P_2 $ - Reference

$ dBm $ - reference to 1 milliwatt  
$ dBW $ - reference to 1 watt  


> **$ dBm = dBW + 30 $**  
When converting dBW to dBm, as 1 W = 1000 mW...  
When multiplying the ratio by 1000, we can use the logarithm law $log(a \times b) = log(a) + log(b) $.  
This allows us to split the ratio $log(1000 \times \frac{a}{b}) = log(1000) + log(\frac{a}{b}) $  
When evaluated, $ log_{10}(1000) = 30 $

# Coding

* Symbol - the smallest element of a signal that can be detected
* Baud rate (modulation rate / symbol rate) - the rate at which a symbol can change = $ \frac{1}{symbol\ duration} $
* Data rate - Bits per second
  * $ bps = Bd \times \log_2 (M) $ for an M-ary signal
  * For a **bi**nary signal, $ Bps = Bd $

## Modulation

The digital version of modulation is called keying

* ASK - Amplitude Shift Keying
* FSK - Frequency Shift Keying
* PSK - Phase Shift Keying
  * DPSK - Differential Phase Shift Keying - Compare to previous wave
    * `0` - No difference
    * `1` - Difference
  * QPSK - Quadrature Phase Shift Keying - Look at new phase offset
    * `11` - 45 degrees
    * `10` - 135 degrees
    * `00` - 225 degrees
    * `01` - 315 degrees
  * Note: We can visualise this with a constellation diagram (I-Q graph)  
  ![](Snipaste_2020-06-03_11-27-49.png)
* QAM - **Q**uadrature **A**mplitude and **P**hase Modulation
  ![](Snipaste_2020-06-03_11-28-00.png)
  * 4-QAM - 2 bits per symbol
  * 16-QAM - 4 bits per symbol
  * n bits per symbol -> 2^n QAM

## Channel Capacity

* Capacity - Maximum data rate (bps) for a channel
* Nyquist Theorem - In noiseless channel, error-free transmission can occur when the $ baud\  rate \le 2 \times bandwidth$
  * $ Capacity = 2 \times bandwidth \times log_2(M) $
  * M - number of levels

### Shannon&apos;s Theory

When noise is present, the maximum data rate for error free communication, is $ B\ log_2 (1 + S/N) $

## Hamming Distance

The number of different bits, when two sequences are compared.  
Increasing the hamming distance between codewords increases the correction rate.  

# Multiple Access Methods

* TDMA - Time Division Multiple Access
  * Clients are allocated a portion of time to communicate
  * Only one client at a time
* FDMA - Frequency Division Multiple Access
  * Clients are allocated to different frequency groups
  * Using FFT, etc... we can extract data from certain frequencies
* CDMA - Code Division Multiple Access
  * FHSS - Frequency Hopping Spread Spectrum
    * Frequently change to different frequencies
    * Transmitter and Receiver share a pseudo-random seed (code) which produces the next frequency to hop to.
    * Hard to intercept
    * Requires more bandwidth
    * Requires time and frequency synchronisation
  * DSSS - Direct Sequence Spread Spectrum
    * Data XOR code

# Doppler Shift

Moving radios will affect the frequency.  

* Moving towards - frequency increase
* Moving away - frequency decrease
* Frequency difference = velocity / wavelength = $ \frac{v}{\lambda} $ = $ \frac{vf}{c} $

## Doppler Spread

Two rays will be received (due to reflections)

* Doppler Spread = $ \frac{2vf}{c} $ = 2 $ \times $ doppler shift
  * Spread will either add or cancel out as the receiver moves
* Coherence time - time during which the channel response is constant
  * $ 1 / doppler\ spread $ = $ \frac{c}{2cf} $ = $ \frac{\lambda}{2v} $

Symbol should be designed to remain for the duration of the coherence time.  
High QAM needed for high data rate.

# Duplexing

Bidirectional communication.

* FDD - Frequency Division Duplexing (Full Duplex)
  * Allocate different frequency ranges for Tx and Rx
* TDD - Time Division Duplexing (Half Duplex)
  * Use the same frequency for Tx and Rx
  * Synchronise time allocation