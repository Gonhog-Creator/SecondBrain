# Lecture 19 handout.pdf

Source: junk_drawer/Lecture 19 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 19: Loop Bode Diagram, Bode Stability Criterion Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 19: Loop Bode Diagram, Bode Stability Criterion

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

April 1, 2025

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

0 / 14

Recapture: Feedback controller synthesis

Gc Gv Gp Km
Y
=
Ysp
1 + Gc Gv Gp Gm
Feedback controller design Q = G̃f− , Gc = 1−QGQp Gv Gm
▶
▶

Ideally, synthesize by Q = 1/Gv Gp Km (targeting at Y /Ysp = 1)
Actually, subject to limitations in rel. deg., non-min.-phase, and delay

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

1 / 14

Recapture: Feedforward controller synthesis

Gd + Gf Gt Gv Gp
Y
=
D
1 + Gc Gv Gp Gm
Ideally, synthesize by Gf = −Gd /Gt Gv Gp (targeting at Y /D = 0)
Actually, subject to limitations in rel. deg., non-min.-phase, and delay
Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

2 / 14

Learning objectives of this lecture

1

Plot and sketch the Bode plot of the open-loop transfer function GOL

2

Explain the stability criterion in frequency domain – Bode criterion

3

Calculate phase margin and gain margin for given feedback loop

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

3 / 14

Controller design in frequency domain: Motivations

Objectives: Stability and performance in closed loop
The approach we used so far is a time-domain one ...
Stability: closed-loop poles (roots to 1 + GOL (s) = 0)
Performance: ISE/ISC from closed-loop TFs (Y /Ysp , Y /D, U/Ysp , U/D)
▶ Often reduce the problem to one-parameter tuning

▶

▶

An alternative but more systematic approach: frequency-domain
▶

Why?

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

4 / 14

Controller design in frequency-domain: Motivations

Every closed-loop t.f. H(s) = (·)/(1 + GOL (s)), GOL = Gc Gv Gp Gm
Frequency response (if there is a sinusoidal disturbance or setpoint):
Y /D = Gd (iω)/(1 + GOL (iω))
We can evaluate amplitude ratio AR and phase angle ϕ under any ω
Relevance to performance ... We hope that CV is not affected much
by a sinusoidal disturbance
Relevance to stability ... What if there is an ω with GOL (iω) = −1?
▶
▶

Then closed-loop stability would be lost (A.R. → ∞).
The frequency response of GOL is of importance to controller design

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

5 / 14

Bode diagram of the open-loop TF GOL (s)
Since GOL = Gc Gv Gp Gm ,
AROL = ARc × ARv × ARp × ARm
ϕOL = ϕc + ϕv + ϕp + ϕv
On AR-plot (log-scale) as well on ϕ-plot, add four plots together.

Bode diagram of GOL
1
1
2
Suppose that Gc = 3, Gm = s+1
, Gv = 2s+1
, Gp = 5s+1
e−1s . Plot (sketch)
the Bode diagram of GOL .

Answer:
AR = 3

1
2
6
1
e−1iω = p
2
2
iω + 1 2iω + 1 5iω + 1
(ω + 1)(4ω + 1)(25ω 2 + 1)
ϕ = − arctan ω − arctan 2ω − arctan 5ω − 1ω

Recall: How to sketch? – Shape of each term, and add up
Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

6 / 14

Shape of Gc

The Bode diagram of GOL (s) involves the Bode diagram of Gc (s) – to
be designed
▶
▶

P-controller: Gc = Kc . AR = Kc , ϕ = 0 (flat lines)
Is
PI-controller: Gc = Kc (1 + τ1I s ) = Kc 1+τ
τI s
ARc =

Kc

p

1 + ω 2 τI2
ωτI

ϕc = arctan ωτ −
▶

π
2

I τD s
PID-controller: Gc = Kc (1 + τ1I s + τD s) = Kc 1+τI s+τ
τI s

⋆

2

Not easy to sketch

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

7 / 14

Bode diagram of P, PI, PID controllers

I mode: At low frequencies,
raises AR by one slope and
costs π/2 from ϕ
D mode: At high frequencies,
raises AR by one slope and
gives π/2 to ϕ
▶

Wentao Tang (NCSU)

Bode Stability Criterion

Actually may have to be
filtered... AR will plateau, ϕ
will return

April 1, 2025

8 / 14

Controller design in frequency domain
Recall: Any closed-loop t.f. = 1+G···OL (s) !
Key observation: For closed-loop stability, GOL (iω) must keep away
from “−1” at all frequencies
▶

Design Gc so that GOL = Gc Gp Gv Gm is away from −1

If there was an ω such that GOL (iω) = −1, then at this frequency, AR
= 1 and ϕ = −π

Definition
For the open-loop TF GOL (s), define
Gain crossover frequency ωg : where AR = |GOL (iωg )| = 1;
Critical frequency ωc (or phase crossover frequency, ωp ): where
ϕ = ∠GOL (iωc ) = −π.

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

9 / 14

Bode stability criterion
Bode stability criterion
Assume that GOL is proper and stable (i.e., the system is open-loop
stable), with unique ωg and ωc :
|GOL (iωg )| = 1, ∠GOL (iωc ) = −π.
Then the closed-loop system is stable if either one of the following holds:
∠GOL (iωg ) > −π,

|GOL (iωc )| < 1.

The proof will need Complex Analysis (MA 513)... let’s avoid this.
Why do we need another stability criterion (in addition to “all roots
of 1 + GOL (s) = 0 are on the LHP”)?
They must be equivalent... indeed, they are.
Bode criterion is more convenient (especially with time delays).
▶ Bode criterion gives useful robustness concepts (next lecture).
▶
▶

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

10 / 14

Bode stability criterion: FOPTD Example
P controller for a FOPTD [cf. Seborg Example 14.7]
K

p
Suppose that Gv = Gm = 1, Gp = τp s+1
e−θs , with P controller Gc = Kc .
Determine the range of Kc to ensure closed-loop stability.

K K

1 + GOL = 1 + τp cs+1p e−θs ... the roots can’t be explicitly related to Kc !
K K
1+ω τp

Bode criterion: GOL (iω) = √ c p2 2 , ∠GOL (iω) = −ωθ − arctan ωτp .
1

By definition |GOL (iωg )| = 1, we get
1q 2 2
ωg =
Kc Kp − 1.
τp

2

To ensure ∠GOL (iωg ) > −π, we need
−ωg θ − arctan ωg τp > −π
q
q
θ
Kc2 Kp2 − 1 + arctan Kc2 Kp2 − 1 < π
τp

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

11 / 14

Bode stability criterion: FOPTD Example

3

q
Kc2 Kp2 − 1 < π2 , i.e.,
r
 πτ 2
1
p
Kc <
.
1+
Kp
2θ
Further simplify ... it suffices that
1 πτp
Kc <
Kp 2θ
** Simplify: It suffices that τθp

A rule about process control with delay
Process delay (vis-à-vis process time constant) requires that the
controller gain should not be too high
2 Upper bound on the controller gain Kcu ∝ (θ/τp )−1
1

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

12 / 14

Bode stability criterion: FOPTD Example

Looking at the Bode plots
(Kp = 1, τp = 1, θ = 1/2)
with different Kc ...
How does the choice of Kc
affect the Bode plot?
Why should Kc be kept under
an upper bound?

Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

13 / 14

Bode stability criterion: Third-order process example
P controller for a FOPTD [cf. Seborg Example 14.4]
K

p
Suppose Gv = Gm = 1, Gp = (τp s+1)
3 , with P controller Gc = Kc .
Determine the range of Kc to ensure closed-loop stability.

K K

Bode criterion: GOL (iω) = (1+ωc2 τ p2 )3/2 , ∠GOL (iω) = −3 arctan ωτp .
p

1

By definition ∠GOL (iωc ) = −π, we get
√
ωc = tan(π/3)/τp =

2

3/τp

To ensure |GOL (iωc )| < 1, we need
Kc Kp
Kc Kp
Kc Kp
=
=
<1
2
2
3/2
3/2
8
(1 + ωc τp )
(1 + 3)
Kc < 8/Kp

A rule about control in third- or higher-order: Kc can’t be too large
Wentao Tang (NCSU)

Bode Stability Criterion

April 1, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 19 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
