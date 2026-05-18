# Homework Set 03.pdf

Source: junk_drawer/Homework Set 03.pdf

Category: [[academic-homework]]

## Summary
CHE 435 (002) Process Systems Analysis and Control Spring 2025 Homework Set 3. First-Order, Second-Order, and Higher-Order Systems (Due on Friday, February 21, 2025) 1. (15 pt) Calculation with complex numbers.

## Full Content
CHE 435 (002) Process Systems Analysis and Control

Spring 2025

Homework Set 3. First-Order, Second-Order, and Higher-Order Systems
(Due on Friday, February 21, 2025)
1.

(15 pt) Calculation with complex numbers.

Recall the Cartesian representation of a complex number z = x+iy and the polar representation z = reiθ. You
already know that to convert polar to Cartesian representation, x = rcos θ and y = rsin θ.

(a) When converting z = x + yi to z = reiθ, obviously we have r = √x2 + y2. However, the simplistic
formula “θ = arctan(y/x)” is applicable only if x > 0, since “arctan” is valued in (–π/2, +π/2).

Therefore, please fill out the correct formula for –π ≤ θ < π:
arctan(y⁄x) , x > 0
? − arctan(y⁄|x| ) , x < 0, y > 0
θ = ? − arctan(y⁄|x| ) , x < 0, y ≤ 0
?, x = 0, y > 0
?, x = 0, y < 0
{
(b) Recall from the previous homework: |z1z2| = |z1|·|z2|, ∡(z1z2) = ∡z1 + ∡z2, and whenever z2 is
nonzero, |z1/z2| = |z1|/|z2|, ∡(z1/z2) = ∡z1 – ∡z2. In particular, |z2| = |z|2, ∡(z2) = 2∡z, |1/z| = 1/|z|,
∡(1/z) = –∡z. Please find the polar representations of the following numbers (where a, b, c are
positive real constants):
z1 =

(1 − bi)3
(1 − ai)(1 + bi) b−ci
1
1 − ai
, z2 =
,
z
=
(assuming |a|< 1), z4 =
e .
3
1 + ai
(1 + bi)(1 + ci) 2
(1 + ai) 2
1 − a2 + 2aci

For example, z1 = r1 exp(iθ1) where r1 = 1/√1 + a2 and θ1 = − arctan a.
2.

(15 pt) First-order system. [Seborg 5.2]
A heater for a semiconductor wafer has first-order dynamics, that is, the transfer function relating
changes in temperature T to changes in the heater input power level P is

1

T′ (s)
K
=
′
P (s) τs + 1
where K has units [°C/kW] and τ has units [min]. The process is at steady state when an engineer
changes the power input stepwise from 1 to 2 kW. She notes the following:
•

The process temperature initially is 100 °C.

•

4 minutes after changing the power input, the temperature is 400 °C.

•

30 minutes later the temperature is 500 °C.

(a) What are K and τ in the process transfer function?
(b) If at another time the engineer changes the power input linearly at a rate of 0.5 kW/min, what can
you say about the maximum rate of change of process temperature: When will it occur? How large
will it be?
3.

(15 pt) Overdamped second-order system, which can be considered as the parallel connection (sum)
of two first-order system. [Seborg 5.6, part of]:
Consider transfer function
G(s) =

Y(s)
10
=
.
U(s) (5s + 1)(3s + 1)

What is y(t → ∞) for the following inputs:
(a) Step input of height M?
(b) Unit impulse input δ(t)?
4.

(15 pt) Underdamped second-order system. [Seborg 5.14]

A step change from 15 to 31 psi in actual pressure results in the measured response from a pressureindicating element shown in the figure below.

(a) Assuming second-order dynamics, calculate all important parameters and write an approximate
transfer function in the form
R′ (s)
K
= 2 2
′
(s)
τ
s
+
2ζτs
+1
P
where R’ is the instrument output deviation (mm) and P’ is the actual pressure deviation (psi).
(b) Write an equivalent differential equation model in terms of actual (not deviation) variables .
5.

(20 pt) High-order dynamics due to connection of multiple simpler low-order models. [Seborg 6.7]

A pressure-measuring device has been analyzed and can be described by a model with the structure shown
in the left figure below. In other words, the device responds to pressure changes as if it were a first-order
process in parallel with a second-order process. Preliminary tests have shown that the gain of the first-

2

order process is −3 and the time constant equals 20 min. An additional test is made on the overall system.
The actual output Pm (not Pm’) resulting from a step change in P from 4 to 6 psi is plotted in the right figure
below.

(a) Determine Q’(s).
(b) Estimate the values of K, τ, and ζ.
(c) What is the overall transfer function for the measurement device Pm’(s)/P’(s)?
6.

(20 pt) Second-order dynamics due to recycle connections. [Seborg 6.19]

Consider the following connection of isothermal reactors. A first-order reaction A → B occurs in both
reactors, with reaction rate constant k. The volumes of liquid in the reactors, V, are constant and equal; the
flow rates F0, F1, F2 and R (recycle ratio) are constant. Assume constant physical properties and a negligible
time delay for the recycle line.

(a) Write a mathematical model for this process.
(b) Derive a transfer function model relating the output concentration of A, C2 to the inlet
concentration of A, C0.
(c) Verify that, in the limit of no recycle (R → 0), the transfer function derived in (b) is equivalent to
the transfer function of the two tanks connected in series.
(d) Show that when k = 0 and a very large recycle flow rate is used (i.e., the limit as R → ∞), the
transfer function derived in (b) becomes the transfer function of a single tank that has the volume
equal to 2V and a gain of 1.
Hint: Recognize that F1 = RF2 + F2 and F0 = F2.
7.

(Bonus: 10 pt) Process control in practice: Identifying a model from step test data. [Seborg 7.3]

In industrial practice, engineers often do not build models from first principles, but instead put a step signal
(or other designed signals) on the input and “identify” the model from the resulting output response data.
This procedure, called “system identification”, can be done either by engineer’s flesh-eye readings, rough
calculations, or statistical software. Matlab and Python have well established toolboxes for it. On the other

3

hand, since system identification is an extremely time-consuming (and hence expensive) task, it remains a
focus of today’s industrial control technology research and development.
To answer the following question, you may want to read Sections 7.1 and 7.2 of Seborg first.
A process consists of two stirred tanks with input q and outputs T1 and T2 (see figure below). To test the
hypothesis that the dynamics in each tank are basically first-order, a step change in q is made from 82 to 85
L/min, with output responses given in the table.

(a) Find the transfer functions T1’(s)/Q’(s) and T2’(s)/T1’(s). Assume that they are of the form Ki/(τis + 1).
(b) Calculate the model responses to the same step change in q and plot with the experimental data.
8.

(Bonus: 10 pt) Process control in depth: Lead-lag dynamics. [Seborg 6.4]

Consider a process model (for simplicity, you may assume K = 1):
Y(s)
K (τa s + 1)
(τ > τ2 )
=
U(s) (τ1 s + 1)(τ2 s + 1) 1
For a step input, prove that:
(a) y(t) can exhibit an extremum (maximum or minimum value) in the step response only if
1 − τa ⁄τ2
> 1.
1 − τa ⁄τ1
(b) Overshoot occurs only for τa / τ1 > 1.
(c) Inverse response occurs (namely an extreme of y(t) has a different sign from K) only for τa < 0.
(d) If an extremum in y exists, the time at which it occurs can be found analytically. What is it?

4



## Metadata
- Source file: junk_drawer/Homework Set 03.pdf
- Extracted: 2026-05-18
- Category: academic-homework
