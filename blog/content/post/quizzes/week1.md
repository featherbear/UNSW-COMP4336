---
title: "Week 1 Quiz"
date: 2020-06-05T17:15:00+10:00

categories: ["Quiz"]
hiddenFromHomePage: false
postMetaInFooter: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

> Frequency hopping requires less bandwidth because it never uses the same channel for too long.

**False**

Whilst it uses a narrow bandwidth or transmission, as frequency hopping requires many different frequeny bands to hop to, the bandwidth is actually increased.

---

> What is the maximum data rate that can be supported on a 10 MHz noise-less channel if the channel uses eight-level digital signals?

**60 Mbps**

$ Capacity = 2 \times B \times log_2 (M) $  
$ Capacity = 2 \times (10 \times 10^6 ) \times log_2 (8) $  
$ Capacity = 60000000 bps = 60 Mbps $

---

> To achieve high security, a secret service agent is using a direct-sequence spread spectrum with a spreading factor of 1000 for all its transmissions. To transmit a message comprising of 10,000 bits, the transmitter will have to transmit.

**10 million bits**

$10000 \times 1000 $

---

> What is the channel coherence time for a wireless link between a car travelling at 36 km/hr and a stationary base station for a 3 GHz band?

**5 ms**

The coherence time is the period of the doppler spread, which is the period of twice the doppler shift.  

$ Doppler\ shift = \frac{v}{\lambda} = \frac{vf}{c} $  
$ Doppler\ spread = 2 \times shift = \frac{2vf}{c} $  
$ Coherence\ time = 1 / spread = \frac{c}{2vf} $

$ time = \frac{3 \times 10^8}{2 \times 36/3.6 \times (3 \times 10^9)} $

---

> To transmit 2-bit symbols, a transmitter uses the following 5-bit codewords (5-bit codewords are eventually transmitted instead of 2-bit symbols):  
&nbsp;  
Data    Codeword  
00  -->    00000  
01  -->    00111  
10  -->    11001  
11  -->    11110  
&nbsp;  
What is the minimum Hamming distance between any two codewords?

**3**

---

> What is the average Doppler frequency shift at 36 km/hr using 3 GHz band (average Doppler shift for a band is computed at the centre frequency of the band; for 3 GHz band, the centre frequency can be assumed as 3 GHz)?

**100 Hz**

$ Doppler\ shift = \frac{v}{\lambda} = \frac{vf}{c} $

$ shift = \frac{36/3.6 \times (3 \times 10^9)}{3 \times 10^8} $

---

> If a mobile error coding system uses a minimum Hamming distance of 3, which of the following statements is correct?  
&nbsp;  
* a. All single bit errors can be detected  
* b. All double bit errors can be corrected  
* c. All triple bit errors can be detected  
* d. All triple bit errors can be corrected  
* e. Bit errors can be detected, but they CANNOT be corrected  

**a. All single bit errors can be detected**

---

> What signal to noise ratio (in dB) is required to achieve 10 Mbps through a 5 MHz channel?

**S/N = 3 = 4.77 dB**

$ 10 \times 10^6 = (5 \times 10^6) \times log_2(1 + S/N) $  
$ 2 = log_2(1 + S/N) $  
$ 1 + S/N = 2^2 = 4 $  
$ S/N = 3 $  
$ 10log(S/N = 3) = 4.77 dB $

---

> What is the Doppler spread at 36 km/hr for 3 GHz band?

**200 Hz**

$ Doppler\ shift = \frac{v}{\lambda} = \frac{vf}{c} $  
$ Doppler\ spread = 2 \times shift = \frac{2vf}{c} $  

$ spread = \frac{2 \times 36/3.6 \times (3 \times 10^9)}{3 \times 10^8} $

---

> A telephone line is known to have a loss of 20 dB. The input signal power is measured at 1 Watt, and the output signal noise level is measured at 1 mW. What is the signal to noise ratio in dB?

**10 dB**

$ S/N = 1000/1 = 30 dB $  
$ S/N - loss = 30 dB - 20 dB = 10 dB $