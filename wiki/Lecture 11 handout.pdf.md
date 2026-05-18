# Lecture 11 handout.pdf

Source: junk_drawer/Lecture 11 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 11: Frequency Response and Bode diagram Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 11: Frequency Response and Bode diagram

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

February 18, 2025

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

0 / 14

Recapture (Lecture 7–10): Time-domain analysis

Step, impulse (, ramp) responses
Characteristics of first- and second-order systems
Poles, zeros, gain, time delay and their implications
Standard gain/time constant forms of transfer functions

Transfer function model (Lecture 6) from linearized ODEs
Qualitative behavior analysis (Lecture 5) based on L.T. (Lecture 4)

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

1 / 14

Learning objectives of this lecture

1

Explain the concepts of amplitude ratio and phase angle of G(s)

2

Make Bode diagrams to represent the frequency response

3

Calculate frequency response of first-order lag, lead-lag,
integrating, delayed systems

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

2 / 14

Frequency Response
Suppose that the input is sinusoidal: u(t) = A sin(ωt)
Radial frequency: ω [rad/min (or sec)]
Period: T = 2π/ω, frequency: f = 1/T = ω/2π [cycles/min(or sec)]
▶ Amplitude: A > 0
▶

▶

Frequency response: y(t) = Â sin(ωt + ϕ) will hold, when t is
sufficiently large
▶
▶

Output will also be sinusoidal, with the same period (frequency)
It is of interest to know Â/A (amplitude ratio) and ϕ (phase angle)

Why does this matter?
Process disturbances can be viewed as small oscillations
Frequency response will play an important role in control
▶ Applied in relevant engineering areas – communications, experimental
data processing, AI, etc.

▶
▶

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

3 / 14

**Testimony of ChatGPT
Dr. Tang asks: Some people believe that frequency response should not be taught to
undergraduates because it’s too hard. Do you agree?
I don’t agree that frequency response should be excluded from undergraduate curricula.
While it can be challenging, it offers valuable insights that are essential for a
comprehensive understanding of control systems. Here are a few reasons.
1 Fundamental Concept: Frequency response is foundational to control theory. It

connects theory with practical applications like filter design, communications, ...
2 Visualization of System Behavior: Tools like Bode plots and Nyquist diagrams

provide intuitive ways to understand system behavior, stability, and performance
without complex mathematics.
3 Industry Relevance: Frequency response techniques are widely used in industries

ranging from aerospace to automotive and electronics. Exposing students to these
concepts better prepares them for real-world challenges.
4 Supports Robust Design: Frequency response aids in designing systems that are

robust to disturbances and uncertainties, an essential skill in engineering practice.
5 Enhances Problem-Solving Skills: Learning challenging topics like frequency

response helps students develop critical thinking and problem-solving skills, which
are valuable beyond control theory.
Wentao Tang (NCSU)

Frequency Response

February 18, 2025

4 / 14

Simulation: First-order lag

1
Consider G(s) = s+1
, u(t) = sin(ωt)

t = 0:0.1:(30/omega); u = sin(omega*t);
y = lsim(tf(1, [1, 1]), u, t);

Observation: Â/A and ϕ depends on ω

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

5 / 14

Analysis: First-order lag
K
Consider G(s) = τ s+1
, u(t) = A sin(ωt) ⇒ U(s) = s2Aω
+ω 2
KAω
Y (s) = (τ s+1)(s
2 +ω 2 ) , do PFE and inverse L.T. to obtain

KAωτ −t/τ
KA
KAωτ
e
+
sin(ωt) −
cos(ωt)
2
2
2
2
1+ω τ
1+ω τ
1 + ω2 τ 2
KAωτ −t/τ
KA
=
e
+√
sin(ωt + ϕ)
2
2
1+ω τ
1 + ω2 τ 2
At sufficient large t, we have y(t) = Â sin(ωt + ϕ), where
KA
Â = √1+ω
and ϕ = − arctan(ωτ )
2τ 2
y(t) =

K
For first-order system G(s) = τ s+1
:

Amplitude Ratio =

Wentao Tang (NCSU)

K
Â
=√
, ϕ = − arctan(ωτ )
A
1 + ω2 τ 2

Frequency Response

February 18, 2025

6 / 14

Analysis: First-order lag

K
:
For first-order system G(s) = τ s+1

Â
K
=√
, ϕ = − arctan(ωτ )
A
1 + ω2 τ 2
K
Amplitude ratio ↓ as ω ↑: G(s) = τ s+1
is a “low-pass filter”
Amplitude Ratio =

When ω ≪ 1/τ , A.R. ≈ K
When ω ≫ 1/τ , A.R. ≈ K/ωτ ∝ ω −1
√
▶ When ω = 1/τ (called the cutoff frequency) A.R. = K/ 2
▶

▶

K
ϕ ↓ from 0 to −π/2 as ω ↑ from 0 to ∞: G(s) = τ s+1
is a “lag”
▶

When ω = 1/τ , ϕ = −π/4(= −45◦ ).

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

7 / 14

Example: First-order lag
√
Exercise: G(s) = 2/( 3s + 1), u(t) = 5 sin t, then at sufficiently large
t, y(t) =?
▶

√
√
K = 2, τ = √
3, ω = 1. Hence A.R.= 2/ 1 + 3 = 1,
ϕ = − arctan 3 = −π/3, y(t) = 5 sin(t − π/3).

You can verify with a simulation.

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

8 / 14

Bode diagram
Plot A.R. (in log scale) and ϕ (in linear scale) against ω (in log scale)
Matlab: [AR, phi] = bode(sys, omega) or bode(sys)

Decibels (dB)?? A.R. [in dB] = 20 log10 A.R. [actual]
√

√
10 = 10 dB, 2 ≈ 6 dB, 2 ≈ 3 dB, 1 = 0 dB, 0.5 ≈ -6 dB...
▶ The cutoff frequency is where the A.R. has dropped by 3 dB

▶

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

9 / 14

General conclusion about frequency response
G(s) at s = iω determines frequency response!!
If G(s) is a stable system, then G(iω) in polar coordinate satisfies:
G(iω) = (A.R.)eiϕ .
In other words, at radial frequency ω,
A.R. = |G(iω)|, ϕ = ∠G(iω)
K
Example 1: First-order lag G(s) = τ s+1
(K > 0):
K
G(iω) =
1 + iωτ
|K|
K
|G(iω)| =
=√
= A.R. ✓
|1 + iωτ |
1 + ω2 τ 2

∠G(iω) = ∠K − ∠(1 + iωτ ) = − arctan(ωτ ) = ϕ ✓

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

10 / 14

Example 2: Lead-lag

G(s) =

1 + τ0 s
1 + τ1 s

s=iω

⇒ G(iω) =

1 + iωτ0
1 + iωτ1

Evaluate modulus and angle:
q
1 + ω 2 τ02
|1 + iωτ0 |
A.R. = |G(iω)| =
=q
|1 + iωτ1 |
1 + ω 2 τ12
ϕ = ∠G(iω) = ∠(1+iωτ0 )−∠(1+iωτ1 ) = arctan(ωτ0 )−arctan(ωτ1 )
When ω → 0: A.R.→ 1, ϕ → 0
When ω → ∞: A.R.→ τ0 /τ1 , ϕ → 0
If τ0 > τ1 (lead dominates), A.R.↑, ϕ ≥ 0 and has a max.
If τ0 < τ1 (lag dominates), A.R.↓, ϕ ≤ 0 and has a min.
Wentao Tang (NCSU)

Frequency Response

February 18, 2025

11 / 14

Example 2: Lead-lag
s+1
Bode plot for G(s) = 2s+1

Bode plot for G(s) = 2s+1
s+1

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

12 / 14

Example 3: Integrating system
G(s) =

K
(K > 0)
s

s=iω

⇒ G(iω) =

K
iω

Evaluate modulus and angle:
K
|K|
=
A.R. = |G(iω)| =
|i| · |ω|
ω
ϕ = ∠G(iω) = ∠(K/ω) − ∠i = −π/2
A.R. ∝ ω −1 . The first plot of Bode is a
line with slope −1 (in log-log)
ϕ = −π/2 for an integrator. The
second plot of Bode is a constant

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

13 / 14

Example 4: Time delay
G(s) = e−θs (θ > 0)

s=iω

⇒ G(iω) = e−iωθ

Evaluate modulus and angle:
A.R. = |G(iω)| = |e−iωθ | = 1
ϕ = ∠G(iω) = ∠e−iωθ = −ωθ
A.R. is a constant 1 (naturally!)
ϕ is endlessly decreasing

Wentao Tang (NCSU)

Frequency Response

February 18, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 11 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
