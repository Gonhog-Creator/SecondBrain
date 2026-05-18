# Lecture 09 handout (1).pdf

Source: junk_drawer/Lecture 09 handout (1).pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 9: Higher-Order Systems, Poles, Delays Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 9: Higher-Order Systems, Poles, Delays

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

February 6, 2025

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

0 / 11

Recapture: First-order systems and second-order systems
First-order system: G(s) = K/(τ s + 1)

Second-order system: G(s) = K/(τ 2 s2 + 2τ ζs + 1)

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

1 / 11

Learning objectives of this lecture

1

Use Matlab to simulate the step response of higher-order systems

2

Precisely describe the relation between poles and stability of T.F.s

3

Explain how time delay arises in process dynamics, and describe
response of delayed systems

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

2 / 11

Higher-order system

General form of an n-th order system
B(s)
bm sm + bm−1 sm−1 + · · · + b1 s + b0
G(s) =
=
A(s)
an sn + an−1 sn−1 + · · · + a1 s + a0
where an ̸= 0
For any physically realizable system, degree of denominator
n = deg A(s) ≥ m = deg B(s) degree of numerator
Imagine: What kind of processes can be n-th order?
A system that needs to be described by n simultaneous diff. eqs. (e.g.,
many tanks connected, multiple reactions, a distillation column with
many trays, etc.)
▶ Rule-of-thumb: Processes that involve reactions or phase equilibria are
usually high-order
▶

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

3 / 11

Step response of higher-order systems
Can be hard to calculate by hand (u(t) → U(s) → Y (s) → y(t))
Matlab: creating a transfer function G(s) = s2 3s+2
+4s+5
sys = tf([3, 2], [1, 4, 5]);
Matlab: simulating unit step response
[y, tOut] = step(sys);
▶

Only “step(sys)” will generate a plot without the data

Matlab: simulating unit impulse response
[y, tOut] = impulse(sys);
Matlab: simulating response to any given input (say, u(t) = 8 sin(πt))
t = 0:0.01:10; u = 8*sin(pi*t);
[y, tOut] = lsim(sys, u, t);

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

4 / 11

”PKZ” analysis of general TFs

”P” = poles, ”K” = static gain, ”Z” = zeros

Terminology
b sm +b

sm−1 s+···+b s+b

m
m−1
1
0
For a TF model G(s) = B(s)
A(s) = an sn +an−1 sn−1 +···+a1 s+a0 , poles refer to the
roots of A(s) (denominator), zeros refer to the roots of B(s) (numerator).

If p makes A(p) = 0, then |G(p)| → ∞... hence called a “pole”.
If z makes B(z) = 0, then |G(z)| → 0... hence called a “zero”.
τ0 s+1
, what are poles and zeros?
Example 1: For G(s) = (τ1 s+1)(τ
2 s+1)
2

−3s+2
, what are poles and zeros?
Example 2: For G(s) = ss2 +2s+2

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

5 / 11

Effect of poles on stability

Consider unit step input U(s) = 1/s ⇒ Y (s) = B(s)/sA(s)
If all roots of A(s) have negative real parts, then Y (s) ultimately
settles. (All remaining terms exponentially decay.)
▶ If any root of A(s) has a positive real parts, then Y (s) ultimately
explodes. (Some term exponentially grows.)
▶ What if A(s) has a zero root (e.g., G(s) = 1/s)?
▶ What if A(s) has a purely imaginary root (e.g., G(s) = 1/(s2 + 1))?
▶

What if A(s) has a purely imaginary root at iω, and u(t) = sin(ωt)
(for the exactly same ω)?

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

6 / 11

Effect of poles on stability and oscillations
Definition of stability: We say that a system is “stable” if any
bounded input signal gives a bounded output signal

“All poles are on LHP” is necessary for stability
The system G(s) is stable if and only if all poles are on the left half plane
(have negative real parts).
Poles also affect whether the output response is oscillatory

“All poles are real” gives non-oscillatory step response
The step response of G(s) is non-oscillatory if and only if all poles are real
(have zero imaginary parts).
Matlab: finding poles
p = poles(sys) % zeros(sys) for zeros
all(real(p) < 0) % if returns 1, then stable
all(imag(p) == 0) % if returns 1, then non-oscillatory
Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

7 / 11

Static gain
If the system is stable, then K = G(0) is its static gain.
Step response: When u(t) = MS(t), Y (s) = MG(s)/s,
lim y(t) = lim sY (s) = lim G(s) = G(0)M = KM.

t→∞

s→0

s→0

Matlab: finding static gain
K = g.Numerator{1}(end) / g.Denominator{1}(end)
or simply K = dcgain(g)
▶

“DC gain” = “direct current gain”

Finding poles, zeros, and gain [Seborg Ex.6.2]
G(s) =

Wentao Tang (NCSU)

4(s + 2)
(0.2s + 1)(2s + 1)

Poles & Delays

February 6, 2025

8 / 11

System with delay (deadtime)
In industrial practice, people often use low-order models with a delay
K
First-order “plus” time delay (FOPTD) G(s) = e−θs τ s+1
K
−θs
▶ Second-order “plus” time delay (FOPTD) G(s) = e
τ 2 s2 +2τ ζs+1
▶

Physical picture: Plug flow tube

c2 (t) = c1 (t − θ) ⇒
▶

C2 (s)
= e−θs
C1 (s)

Reason for time delay: lack of mixing makes the effect of input on the
output non-instantaneous

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

9 / 11

** Approximating higher-order systems as FOPTD
Skogestad’s half rule [Seborg Example 6.4]
G(s) =

K(1 − s)
e−s
(12s + 1)(3s + 1)(0.2s + 1)(0.05s + 1)

1

Factorize denominator. Keep the slowest term (τ = 12).

2

Split the second slowest term into two halves (3/2). One half adds to
τ → 12 + 1.5, the other half becomes a delay (e−1.5s ).

3
4

Approximate fast terms as delays (e−0.2s e−0.05s ).
For the numerator terms, approximate as delays/anti-delays
(1 + αs ≈ eαs , 1 − αs ≈ e−αs ) when α ≪ τ . [Otherwise not
approximable.]
K
e−3.75s .
G(s) ≈
13.5s + 1

Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

10 / 11

** Approximating e−θs as a rational TF
Padé approximation
e−θs ≈ R1,1 (s) =

1 − θ2 s

[1, 1]-approximation
1 + θ2 s
θ2 2
s
1 − θ2 s + 12
−θs
e
≈ R2,2 (s) =
[2, 2]-approximation
θ
θ2 2
1 + 2 s + 12 s
In general, Padé approximation Rm,n (s) can be found by letting
d i Rm,n
diG
=
, i = 0, 1, . . . , m + n
dsi s=0
dsi s=0
▶

0 +b1 s
and then determine these 3
For example, let R1,1 (s) = b1+a
1s
coefficients based on the above 3 equations.

These approximations are usually not necessary, although they are
often used just for simplicity. (Personal view: Simplification is
desirable only if there is a good reason.)
Wentao Tang (NCSU)

Poles & Delays

February 6, 2025

11 / 11



## Metadata
- Source file: junk_drawer/Lecture 09 handout (1).pdf
- Extracted: 2026-05-18
- Category: academic-lecture
