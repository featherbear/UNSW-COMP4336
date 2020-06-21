---
title: "Week 2 Quiz"
date: 2020-06-12T17:15:35+10:00

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

> Q1. What is the received signal power (approx.) observed by a user equipment (UE) at 4m
and at a distance of 500 m from a 14 m high base station? The transmitter and receiver
antenna gains are 10 dBi and 5 dBi, respectively. Base station transmission frequency is
2GHz and transmission power is 30 dBm.

30 dBm  
-30 dBm  
30 W  
30 mW  
30 dBW  

D break = 4(14*4*2*10 9 /3*10 8 ) = 1493.33m; thus at 500m, the UE is NOT at far field and
hence we CANNOT use the 2-ray model. One option would be to use the Free-space
model, but that could be grossly incorrect for the practical scenario explained in the
question (not clearly a free-space scenario). Also, none of the options of the multiple
choice are for the free-space model. This question is therefore abandoned and all students
who attempted this question was given the full mark.

---

> Q2. With a subcarrier spacing of 10 kHz, how many subcarriers will be used in an OFDM
system with 8 MHz channel bandwidth?

8  
80  
**800**  
8000  
None of these  

Number of Subcarriers = (8×10 6 )/(10×10 3 ) = 800

---

> Q3. Let us consider an OFDM system that uses the same carrier spacing irrespective of the
channel bandwidth used. It employs 1024 subcarriers for 10 MHz channel. How many
subcarriers will be used if the channel was 1.25 MHz wide?

1000  
1024  
1280  
**128**  
900  

Inter carrier spacing = 10MHz/1024 = 9.7656 kHz  
Now, for a 1.25 MHz channel: 1.25x10 3 /9.7656 = 128 subcarriers.  

---

> Q4. You have bought a 2.4 GHz WiFi router with two dipole antennas claiming effective
antenna gain of 6 dB. Your laptop has a single dipole with 0 dB gain and it claims a receiver
sensitivity of -64 dBm. What is the maximum distance from the router your laptop can
receive data if the router always use a transmit power of 20 dB?

10m  
20m  
115m  
215m  
**315m**  

We can tolerate a maximum pathloss of 90 dB (20+6+64 = 90). 2.4 GHz will lose 90
dB at 315 m. Beyond 315 m from the router, the laptop will receive signal strength
below its sensitivity level and hence will not be able to decode information.

---

> Q5. You have bought a 2.4 GHz WiFi router with antenna gain of 6 dB and default
transmission power of 100 mW. Your laptop has a 0 dB antenna gain and claims a receiver
sensitivity of -60 dBm. Can you connect your laptop to the router from a distance of 150 m?

**a) YES**  
b) NO  

There is 83.56 dB path loss at 150 m. Therefore, the laptop will receive a signal
strength of 20+6-83.56 = -57.56 dBm, which is higher than its receiver sensitivity.
Therefore the laptop can connect to the router.

---

> Q6. An omni-directional antenna radiates power in ALL directions equally.

a) True  
**b) False**

Only the isotropic antenna radiates power in all directions EQUALLY.

---

> Q7. A lamp post would cause scattering for a 300 GHz transmission.

a) True  
**b) False**  

A 300 GHz signal has a wavelength of only 1mm. Lamp posts are usually much wider objects
having diameters on the order of centimeters, hence are unlikely to serve as effective scatters
for such high-frequency signals.

---

> Q8. In the presence of multipath, symbols get wider at the receiver.
**a) True**  
b) False  

With multipaths, reflections from different paths keep coming to the receiver for some time,
effectively widening the symbol interval.

---

> Q9. Symbols must be wider than the delay spread to avoid inter-symbol interference.

**a) True**  
b) False

If symbols are shorter than delay spread then signals with significant power from
previous symbol will interfere with signals from the next symbol.

---

> Q10. MIMO is only useful with the presence of multipath and scattering.

a) True  
**b) False**

Even for LoS-only scenarios, the separation of multiple antennas in MIMO leads to
uncorrelated LoS paths, thus providing spatial diversity benefits.
End of Quiz-2