# Lecture 13 handout.pdf

Source: junk_drawer/Lecture 13 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 13: Feedback Control and Feedback Loop Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 13: Feedback Control and Feedback Loop

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

March 4, 2025

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

0 / 20

Recapture: Frequency response analysis

Frequency response: A.R. = Â/A = |G(iω)|, ϕ = ∠G(iω)
Bode diagram: A (log scale) v.s. ω (log scale), ϕ v.s. ω
K
0s
; Lead-lag system G(s) = 1+τ
First-order system G(s) = τ s+1
1+τ1 s ;
1−τ s
Non-minimum-phase element G(s) = 1+τ
s,

Higher-order systems in a general form:
(1 + τ̄1 s) . . . (1 + τ̄m s) −θs
G(s) = K
e (K > 0)
(1 + τ1 s) . . . (1 + τn s)

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

1 / 20

Use in Practice: Frequency-domain system identification
An accurate approach to identify the t.f. model of an unknown system

Guidelines
1

Obtain the Bode diagram
▶
▶

2
3

Choose many ω values, let u(t) = A sin ωt and measure y(t)
Determine A.R. = Â/A and ϕ from y(t) = Â sin(ωt + ϕ)

Check the asymptotic values/slopes on the Bode diagram
Choose factors to match the Bode diagram
1
Lag: 1+τ
slope 0 to −1, ϕ
value 0 to −π/2
s ... AR
Lead: 1 + τ s... AR
slope 0 to +1, ϕ
value 0 to +π/2
▶ NMP: 1−τ s ... AR = 1, ϕ
value
0
to
−π
1+τ s
▶ Delay: e−θs ... AR = 1, ϕ drops from 0 to −∞
▶ Integrator: 1 ... AR
slope −1, ϕ = −π/2
s
▶ Differentiator : s... AR
slope +1, ϕ = +π/2
K
▶ Underdamped 2nd -order:
slope 0 to −2, ϕ
τ 2 s2 +2τ ζs+1 : AR
value 0 to −π
▶

▶

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

2 / 20

Frequency-domain v.s. time-domain identification
Step-response data v.s. Frequency-response data
G(s) =

3
7s2 + 8s + 1

Identification from step response
▶

Likely a 2nd -order system, close to 1st -order, not sure if higher-order

Identification from frequency responses
▶

Two lags for sure!

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

3 / 20

An Example for frequency-domain system identification
** Frequency-domain system identification [Ex. 9.12, Kravaris]

Observation and analysis
▶
▶

A.R. slope: initially +1, then +2, then 0
ϕ values: initially 90◦ , then rises, but countered by a decrease to 0◦

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

4 / 20

Observation and analysis
▶

A.R. slope: initially +1, then +2, then 0 — ∴ 3 factors exist
1 first factor =
, with slope +1
2 second factor =
, with slope 0 → +1
3 third factor =
, with slope 0 → −2

▶

ϕ values: initially 90◦ , then rises, but countered by a decrease to 0◦
1 first factor = s, 90◦
2 second factor = 1 + τ s, 0◦ → 90◦
3 third factor = 2nd -order lag, 0◦ → −180◦

The t.f. should be
G(s) =

Wentao Tang (NCSU)

Ks(1 + τ̂ s)
τ 2 s2 + 2τ ζs + 1

Feedback Loop

.

March 4, 2025

5 / 20

Obtain the parameters – express A.R. and ϕ
√
Kω 1 + ω 2 τ̂ 2
|G(iω)| = p
(1 − ω 2 τ 2 )2 + 4ω 2 τ 2 ζ 2
π
∠G(iω) = + arctan ωτ̂ − ∠(1 − ω 2 τ 2 + 2iωτ ζ)
2
1

When ω ≪ 1: A.R. ≈ Kω
⋆

Check: ω = 10−1 , A.R. ≈ 10−2 ∴ K ≈ 1/10

2

When 1 ≤ ω ≤ 10: A.R. ≈ Kω 2 τ̂

3

When ω ≫ 10: A.R. ≈ K τ̂ /τ 2

⋆

⋆

4

Check: ω = 3, A.R. ≈ 1 ∴ τ̂ ≈ 10/9
√
Check: ω = 1000, A.R. ≈ 10 ∴ τ ≈ 1/ 90

When ω ≈ 10, ϕ ≈ π − ∠(1 − ω 2 τ 2 + 2iωτ ζ)
⋆
⋆

Check: ϕ = π/4 corresponds to ω = 15.
√
ϕ = π/4 means 1 − ω 2 τ 2 < 0 and 2ωτ ζ = ω 2 τ 2 − 1 ... ∴ ζ = 3/2 10

DONE!
G(s) =

Wentao Tang (NCSU)

1 2
1
9 s + 10 s
.
1 2
1
90 s + 10 s + 1

Feedback Loop

March 4, 2025

6 / 20

Learning objectives of this lecture

1

Explain schematically the role of feedback controllers

2

Recognize the time-domain and transfer-function forms of PID
controllers

3

Represent the closed-loop system in a block diagram

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

7 / 20

Recall: What is a feedback controller?
A device to adjust manipulated variables in a compensatory way
Typically, it uses a comparison of controlled variables to their
setpoints

AT: analyzer transmittor (composition sensor), AC: controller
p: electric current signal, I/P: current-to-pressure transducer
Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

8 / 20

Block representation

Generally, the controller can be any algorithm, as long as the
controller output p depends on the past ym and ysp
Less generally, the controller can be designed as a linear system
P′ (s) = G1 (s)Ysp (s) + G2 Ym (s)
Even less generally, P′ (s) = Gc (s)E(s), where E(s) = Ysp (s) − Ym (s)
(i.e., e(t) = ysp (s) − ym (s)) is the error signal
▶

Controller is a t.f. Gc (s)

How to design the form of Gc (s)? (What kind of t.f. can it be?)
Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

9 / 20

“Natural” design of controller: Three control modes

Controller output p: Force on the brake
Error e: Speed of the car & Distance to the stop line
1

Proportional (P) control
p(t) = p̄ + Kc e(t)
▶
▶

p̄: steady state value, i.e., the value of p(t) when e(t) = 0
Kc : controller gain

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

10 / 20

“Natural” design of controller: Three control modes

Is your controller really that simple? ... Likely it contains more.
2

Integral (I) mode
Z t
p(t) = KI

e(t ∗ )dt ∗

0

KI : integration coefficient
Rt
Proportional-integral controller (PI): p(t) = p̄ + Kc e(t) + KI 0 e(t ∗ )dt ∗
▶ By writing K = K /τ , we have
I
c I


Z
1 t ∗ ∗
p(t) = p̄ + Kc e(t) +
e(t )dt
τI 0
▶
▶

where τI is called integral time (constant)
Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

11 / 20

Offset

Why use I-mode?
As long as the error remains, keep changing p(t) ... until error totally
vanishes
▶ This (hopefully) eliminates the error between y and y
m
sp ultimately

▶

⋆
⋆

Offset – steady-state value of y(t) − ysp (t), often in percentages
I-mode achieves offset-free control (to be proved later)

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

12 / 20

“Natural” design of controller: Three control modes

What if there is a rapidly decelerating car ahead of you?
3

Derivative (D) mode
p(t) = KD
▶
▶

de(t)
dt

Write KD = Kc τD , where τD is called derivative time
Proportional-derivative controller (PD):


de(t)
p(t) = p̄ + Kc e(t) + τD
dt
or proportional-integral-derivative controller (PID):


Z
1 t ∗ ∗
de(t)
p(t) = p̄ + Kc e(t) +
e(t )dt + τD
τI 0
dt

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

13 / 20

TF of PID controller



Z t

de(t)
p(t) = p̄ + Kc
e(t )dt + τD
dt
0


P′ (s)
1
= Gc (s) = Kc 1 +
+ τD s
E(s)
τI s
1
e(t) +
τI

∗

∗



Gc (s) is the TF of the controller.

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

14 / 20

Derivative filter

Wait... There is no ”process” that can appear like KD s
For any physically realizable t.f., degree of denominator ≥ degree of
numerator! (But 0 ≥ 1 does not hold.)
▶ From a frequency-response point-of-view, such a controller would
respond drastically to high-frequency noises.
▶

Filtered PID controller:
▶

▶

“Parallel with
h derivative filter”:
i
s
(α ≪ 1)
Gc (s) = Kc 1 + τ1I s + αττDDs+1
h
i
τD s+1
“Series with derivative filter”: Gc (s) = Kc 1 + τ1I s ατ
(α ≪ 1)
D s+1

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

15 / 20

Be aware!

After all, PID is just a specific form of controllers
PID is usually not optimal, and may even fail to work or work badly.
There even exist processes that cannot be controlled with PID.
▶ In general, controllers can be any t.f. or even any algorithm. There is
no sound reason to restrict to PID unless you have to.
▶ Engineers need to know the process models first, and then design a
suitable controller (instead of being igorant of the process and
expecting a magical “tuning rule”)!
▶

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

16 / 20

Towards closed-loop system analysis

Now the central problem of process control is how to design the
controller
... based on the analysis of how the controller design affects
regulation and tracking
... i.e., the effect of ysp on y, and the effect of d (disturbances) on y,
under control
So, we need to put together everything in the loop

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

17 / 20

Components of a feedback control system

Process (plant): x (controlled) affected by w2 (manipulated) and x1
(disturbance)
K1
K2
X ′ (s) =
X1′ (s) +
W ′ (s)
τ1 s + 1
τ2 s + 1 2
2 Sensor: approximately a first-order system
Km
Xm′ (s)/X(s) = G(s) =
X(s)
τm s + 1
1

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

18 / 20

Components of a feedback control system

Controller: a PI for example


P′ (s)
1
= Kc 1 +
, E(s) = Ỹsp (s) − Ym (s) = Km Ysp (s) − Ym (s)
E(s)
τI s
4 Current-to-pressure transducer: Pt′ (s) = KIP P′ (s)
3

5

Control valve: W2′ (s)/Pt′ (s) = Kv /(τv s + 1)
Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

19 / 20

Block diagram of the feedback control system

Wentao Tang (NCSU)

Feedback Loop

March 4, 2025

20 / 20



## Metadata
- Source file: junk_drawer/Lecture 13 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
