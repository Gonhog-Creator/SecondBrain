# Lecture 20 handout.pdf

Source: junk_drawer/Lecture 20 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 20: Stability Margins and Robust Stability Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 20: Stability Margins and Robust Stability

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

April 3, 2025

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

0 / 14

Recapture: Bode stability criterion
Two characteristic frequencies for GOL
For the open-loop TF GOL (s), define
Gain crossover frequency ωg : where AR = |GOL (iωg )| = 1;
Critical frequency ωc (or phase crossover frequency ωp ): where
ϕ = ∠GOL (iωc ) = −π.

Bode stability criterion
Assume that GOL is proper and stable (i.e., the system is open-loop
stable), with unique ωg and ωc :
|GOL (iωg )| = 1, ∠GOL (iωc ) = −π.
Then the closed-loop system is stable if either one of the following holds:
ϕg = ∠GOL (iωg ) > −π,

Wentao Tang (NCSU)

ARc = |GOL (iωc )| < 1.

Robust Stability

April 3, 2025

1 / 14

Learning objectives of this lecture

1

Calculate phase margin and gain margin for given feedback loops

2

Explain the concept of robust stability, its difference from nominal
stability, and its relation to stability margins

3

Design controller parameters for stability margin specifications

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

2 / 14

Stability margins

Definitions
Assume that GOL is proper and stable (i.e., the system is open-loop
stable), with unique ωg and ωc :
ARg = |GOL (iωg )| = 1,

ϕc = ∠GOL (iωc ) = −π.

Phase margin PM = ∠GOL (iωg ) − (−π) = ϕg + π
Gain margin GM = 1/ARc = 1/|GOL (iωc )|
For closed-loop stability, we need PM > 0 and GM > 1 = 0 dB ... so
that GOL is different from −1 at all frequencies

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

3 / 14

Stability margins on the Bode diagram of GOL

Rule of thumb: A well-tuned controller should make
PM > π/6 = 30◦ and GM > 1.7 = 4.6 dB ... so that GOL is much
different from −1 at all frequencies
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

4 / 14

Stability margins: Example 1
Calculate GM
K

p
Given Gv = Gm = 1, Gp = s(τp s+1)
2 , Gc = Kc (P-controller), find GM.

1

K K

p c
GOL (s) = s(τp s+1)
2,

AR =
2

Find ωc :

Kp Kc
π
, ϕ = − − 2 arctan ωτp
2
2
ω(1 + ω τp )
2

π
− 2 arctan ωc τp = −π
2
⇒ ωc τp = tan(π/4) ⇒ ωc = 1/τp

ϕc = −π ⇒ −

3

Determine GM:
ARc =

Kp Kc
1
= Kp Kc τp ⇒ GM = 2/Kp Kc τp
ωc (1 + 1)
2

Add-on question: Design Kc to achieve GM ≥ 6 dB = 2.
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

5 / 14

Stability margins: Example 1
Design for a PM specification
K

p
Given Gv = Gm = 1, Gp = s(τp s+1)
2 , Gc = Kc (P-controller), design Kc
such that PM = 30◦ .

1

K K

p c
GOL (s) = s(τp s+1)
2,

Kp Kc
π
, ϕ = − − 2 arctan ωτp
2
2
ω(1 + ω τp )
2
2 Given PM = 30◦ , we know that ϕg = −150◦ :
AR =

−90◦ − 2 arctan ωg τp = −150◦ ⇒ ωg = tan 30◦ /τp
3

ARg must be equal to 1:

√
Kp Kc
3 3
4
=
Kp Kc τp = 1 ⇒ Kc = √
2
◦
◦
4
(tan 30 /τp )(1 + tan 30 )
3 3Kp τp

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

6 / 14

Stability margins: Example 2
Calculate PM
K

p
−θs , G = K (P-controller), determine
Given Gv = Gm = 1, Gp = (τp s+1)
c
c
2e
PM.

1

2

3

K K

p c
−θs ,
GOL (s) = (τp s+1)
2e

AR =

Kp Kc
, ϕ = −ωθ − 2 arctan ωτp
1 + ω 2 τp2

1=

Kp Kc
1p
⇒ ωg =
Kp Kc − 1
2
2
1 + ωg τp
τp

Find ωg :

Determine GM:
p
θp
ϕg = −
Kp Kc − 1 − 2 arctan Kp Kc − 1 ⇒ PM = ϕg + π
τp
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

7 / 14

Stability margins: Example 2
Design for a GM specification
K

p
−θs , G = K (P-controller), design K
Given Gv = Gm = 1, Gp = (τp s+1)
c
c
c
2e
such that GM = 2.

1

K K

p c
−θs ,
GOL (s) = (τp s+1)
2e

Kp Kc
, ϕ = −ωθ − 2 arctan ωτp
1 + ω 2 τp2
2 Given GM = 2, we know that ARc = 1/2:
Kp Kc
1
1p
=
⇒ ωc =
2Kp Kc − 1
2
2
1 + ωc τp
2
τp
3 ϕc must be equal to −180◦ :
p
p
−(θ/τp ) 2Kp Kc − 1 − 2 arctan 2Kp Kc − 1 = −π
p
4 Numerical solution is needed for x =
2Kp Kc − 1 first:
AR =

(θ/τp )x + 2 arctan x = π
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

8 / 14

Numerical evaluation of stability margins

Well... We don’t always have closed-form expressions for margins.
Matlab: [GM, PM, omega c, omega g] = margin(G OL);
Python: GM, PM, omega c, omega g = control.margin(G OL)
2
−s
Example: GOL = (s+1)
2e
▶
▶

Verify that ωg = 1, PM = (π/2 − 1) rad = 32.72◦
Verify that ωc (= 1.3065) satisfies ωc + 2 arctan ωc = π,
GM = (1 + ωc2 )/2 = 1.3535

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

9 / 14

Model uncertainties
The need for margins arises from model uncertainties

Dude got this data from step response ...
Kp
Maybe the process is Gp = τp s+1
e−θp s with Kp = 1, τp = 0.5, and
θp = 1... Are we sure about these values?
Gc that achieves closed-loop stability with the “model” may not be
good with the “actual plant”
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

10 / 14

Implications of stability margins
Phase margin
▶

Suppose that the actual
system has an extra
unknown delay ∆θ than the
model

Gain margin
▶

GOL = G̃OL e−(∆θ)s
▶

GOL = K ′ G̃OL

GOL & G̃OL always have
equal AR, so ... ωg doesn’t
change, but

▶

ϕg = ϕ̃g − ωg ∆θ
▶

GOL & G̃OL always have
equal ϕ, so ... ωc doesn’t
change, but
fc
ARc = K ′ AR

In order that ϕg > π,
ωg ∆θ < PM... Maximum
allowed unmodeled delay

▶

Maximum allowed unmodeled
gain
′
Kmax
= GM

∆θmax = PM/ωg
Wentao Tang (NCSU)

Suppose that the actual
system has an extra
unknown gain than the
model

Robust Stability

April 3, 2025

11 / 14

Robust stability

PM and GM – Capability to tolerate model uncertainty or
plant-model mismatch
Nominal stability: Stable based on a “nominal model” of the plant
▶

PM > 0 & GM > 0 dB

Robust stability: Stable against possible model uncertainty
▶

PM quite large, GM quite large

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

12 / 14

** More generic description of robust stability

Plant-model mismatch: GOL (s) = (1 + ∆(s))G̃OL (s)
∆(s): Relative (multiplicative) mismatch
Assume that |∆(iω)| ≤ ℓ(ω): Percentage uncertainty on frequency
response at ω
▶ Total upper bound of uncertainty:

▶

▶

|GOL (iω) − G̃OL (iω)| ≤ ℓ(ω)|G̃OL (iω)|

Robust stability: At all ω, G̃OL (iω) must keep away from −1 with a
distance at least ℓ(ω)|G̃OL (iω)|
▶

|G̃OL (iω) − (−1)| ≥ ℓ(ω)|G̃OL (iω)|

Wentao Tang (NCSU)

Robust Stability

April 3, 2025

13 / 14

** More generic description of robust stability
Doyle-Stein Theorem (1980)
Suppose the open-loop t.f. is inaccurately modeled, with relative
mismatch bounded in frequency domain:
GOL (s) = (1 + ∆(s))G̃OL (s), |∆(iω)| ≤ ℓ(ω).
(In other words, the mismatch is uncertain but a bound on its A.R. is
known.) Then a sufficient condition for robust stability is
GOL
(iω) < 1 for all ω.
ℓ(ω)
1 + GOL
GOL
If Gm = Km , 1+G
= T = QGp Gv Gm is the t.f. from Ysp to Y !
OL

Often we can overestimate ℓ(ω) by the A.R. of another t.f. WT (s):
ℓ(ω) ≤ |WT (iω)|.
Then the robust stability can be guaranteed, as long as
|(WT T )(iω)| < 1 for all ω.
Wentao Tang (NCSU)

Robust Stability

April 3, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 20 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
