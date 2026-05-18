# Homework Set 04.pdf

Source: junk_drawer/Homework Set 04.pdf

Category: [[academic-homework]]

## Summary
CHE 435/525 – Process Systems Analysis and Control Spring 2025 Homework Set 4. Frequency Response and Bode Diagram (Due on Friday, March 7, 2025) 1. (15 pt) Process with a right-half-plane zero (inverse response). [Seborg 6.17] The dynamic behavior of a packed-bed reactor can be approximated by a transfer function model

## Full Content
CHE 435/525 – Process Systems Analysis and Control

Spring 2025

Homework Set 4. Frequency Response and Bode Diagram
(Due on Friday, March 7, 2025)
1.

(15 pt) Process with a right-half-plane zero (inverse response). [Seborg 6.17]
The dynamic behavior of a packed-bed reactor can be approximated by a transfer function model
T! (s)
3(2 − s)
=
!
Ti (s) (10s + 1)(5s + 1)
where Ti is the inlet temperature, T is the outlet temperature (°C), and the time constants are in hours.
The inlet temperature varies in a cyclic fashion due to the changes in ambient temperature from day to
night. As an approximation, assume that Ti’ varies sinusoidally with a period of 24 hours and
amplitude of 12 °C. What is the maximum variation in the outlet temperature, T?

2.

(15 pt) Frequency response of a first-order system. [Seborg 14.3]
A data acquisition system for environmental monitoring is used to record the temperature of an air
stream as measured by a thermocouple. It shows an essentially sinusoidal variation after about 15 s.
The maximum recorded temperature is 128 °F, and the minimum is 120 °F at 1.8 cycles per min. It is
estimated that the thermocouple has a time constant of 5 s. Estimate the actual maximum and minimum
air temperatures.

3.

(20 pt) Calculation of frequency response. [Kravaris 9.5]
The following are the transfer functions of first-, second- and third-order Butterworth filters, respectively:
1
1
1
G1 (s) =
, G2 (s) =
, G3 (s)=
.
2 s2 + τs + 1)
2
2
(τs
τs + 1
+
1)(τ
τ s + √2τs + 1
Calculate the amplitude ratio and the phase angle as a function of frequency and sketch the
corresponding the Bode diagrams. Validate your results using MATLAB. Are all of the above transfer
functions low-pass filters? What is the cut-off frequency in each case?

4.

(15 pt) Plotting the Bode diagram. You may need to use Matlab for accurate solutions. [Seborg 14.7]
Plot the Bode diagram (0.1 ≤ ω ≤ 100) of the third-order transfer function,
4
G(s) =
.
(10s + 1)(2s + 1)(s + 1)
Find both the value of ω that yields a −180° phase angle and the value of AR at that frequency.

5.

(15 pt) Frequency-domain error of transfer function approximation. You may use Matlab. [Seborg 14.8]
Using MATLAB, plot the Bode diagram of the following transfer function:
6(s + 1)e"2s
.
(4s + 1)(2s + 1)
Repeat for the situation where the time-delay term is replaced by a [1, 1]-Padé approximation, i.e., e–θs
G(s) =

≈ (1 – θs/2) / (1 + θs/2). Discuss how the accuracy of the Padé approximation varies with frequency.
6.

(20 pt) Identifying transfer function from frequence response. You may use Matlab. [Seborg 14.9]

1

Two thermocouples, one of them a known standard, are placed in an air stream whose temperature is
varying sinusoidally. The temperature responses of the two thermocouples are recorded at a number
of frequencies, with the phase angle between the two measured temperatures as shown below. The
standard is known to have first-order dynamics and a time constant of τ1 = 0.15 min when operating in
the air stream. From the data, show that the unknown thermocouple also is a first order and determine
its time constant.

7.

Frequency (cycles/min)

Phase difference (deg)

f = ω/2π

φ1 – φ2

0.05

4.5

0.1

8.7

0.2

16.0

0.4

24.5

0.8

26.5

1.0

25.0

2.0

16.7

4.0

9.2

(Bonus: 10 pt) Process control in practice: Safety Instrumented System (SIS). [Seborg 10.3]
The importance of process safety is evident. Safety instrumented system (SIS) plays the role of an
emergency backup when the basic process control system is operated beyond its proper capacity to
contain hazards. If you work as a process engineer, understanding the SIS based on analysis of the
process itself is necessary. You may want to read Sections 10.1 and 10.2 of Seborg first.
The two-phase feed stream for the gas-liquid separator (or flash drum) shown in the figure below
consists of a hydrocarbon mixture. Because the pressure in the vessel is significantly lower than the
feed pressure, part of the liquid feed flashes to form a gas phase. The hydrocarbons are flammable and
somewhat hazardous. Discuss the process safety issues and propose an alarm/SIS strategy.

8.

(Bonus: 10 pt) Process control in practice and also in depth: Identifying complicated transfer
functions from frequency responses. You may or may not need to use Matlab. [Kravaris 9.11]
If the transfer function of the process is unknown, instead of doing a step response, the engineer can
record the frequency response of the system under different frequencies to identify the model. This

2

technique is known as frequency-domain identification. It can be advantageous compared to the timedomain (step-response) approach, since it gives complete information over the frequency range, and
tends to be more accurate in estimating more complicated systems.
In Figure P9.11 the Bode plots of an unknown system are given.

Select a transfer function that can be used to best describe the given Bode diagrams among the
following ones, in which K, τ0, τ1, and τ2 are positive for all cases. For the transfer function selected,
estimate the values of parameters.
K
(τ1 s + 1)(τ2 s + 1)
K(τ0 s + 1)
G2 (s) =
(τ1 s + 1)(τ2 s + 1)
K(τ0 s + 1)
G3 (s) =
s(τ1 s + 1)
K
G4 (s) =
s(τ1 s + 1)(τ2 s + 1)
Ks
G5 (s) =
(τ1 s + 1)(τ2 s + 1)
G1 (s) =

3



## Metadata
- Source file: junk_drawer/Homework Set 04.pdf
- Extracted: 2026-05-18
- Category: academic-homework
