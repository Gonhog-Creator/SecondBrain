# Lecture 10 handout.pdf

Source: junk_drawer/Lecture 10 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 10: Zeros, Inverse Response, and Non-Invertibility Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 10: Zeros, Inverse Response, and Non-Invertibility

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

February 13, 2025

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

0 / 11

Recapture: Delayed systems and higher-order systems

K
First-order plus time delay: G(s) = τ s+1
e−θs
▶
▶

How does time delay arise in a process? Lack of mixing (plug flow)
How does its step response look like?

Higher-order system:
bm sm + bm−1 sm−1 s + · · · + b1 s + b0
B(s)
=
G(s) =
A(s)
an sn + an−1 sn−1 + · · · + a1 s + a0
▶
▶

Stable if all poles are on LHP
If stable, G(0) = K is the gain

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

1 / 11

Learning objectives of this lecture

1

Explain the implications of right-half-plane zeros

2

Convert transfer functions into gain/time constant form

3

Recognize the form of transfer function based on step response plot

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

2 / 11

Zeros

Recall: Poles are roots to denominator A(s). Their locations on the
complex plane determine stability.
Question: Zeros are roots to numerator B(s). What do their
locations imply?
To best investigate this, let’s always treat the TF with a factorization!
B(s)
bm (s − z1 ) . . . (s − zm )
G(s) =
=
A(s)
an (s − p1 ) · · · (s − pn )
The poles and zeros have units [1/time]
Denote “denominator time constants” τ1 = −1/p1 , · · · , τn = −1/pn ,
then (s − p1 ) · · · (s − pn ) = const · (τ1 s + 1) . . . (τn s + 1).
▶ Denote “numerator time constants” τ̄ = −1/z , · · · , τ̄ = −1/z ,
1
1
m
m
then (s − z1 ) · · · (s − zm ) = const · (τ̄1 s + 1) . . . (τ̄m s + 1).
▶

▶

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

3 / 11

Gain/time constant form

Thus, the TF can be converted to a standard gain/time constant form
(τ̄1 s + 1) . . . (τ̄m s + 1)
G(s) = K
(τ1 s + 1) . . . (τn s + 1)
K = G(0) is the gain
τj = −1/pj . If all τj are on RHP, then the system is stable.
▶ τ̄ = −1/z . Question: What do the locations of numerator time
j
j
constants imply?

▶

▶

s+4
Practice: Convert G(s) = s2 +6s+5
into gain/time constant form

Practice: Convert G(s) = s−4s+0.5
2 +6s+5 into gain/time constant form

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

4 / 11

Inverse response
When a numerator time constant is negative, namely when there
exists a right-half-plane zero, there can be inverse response –
“sign-flipping”
K(τa s + 1)
: τ1 = 4, τ2 = 1
G(s) =
(τ1 s + 1)(τ2 s + 1)

Distinguish inverse response / overshoot / oscillations!
Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

5 / 11

Inverse response: Interpretation

Two first-order dynamics in competition (for simplicity, K = 1):
1
τa − τ2
1
k1
k2
τ1 − τa
·
+
·
=
+
G(s) =
τ1 − τ2 τ1 s + 1 τ1 − τ2 τ2 s + 1
τ1 s + 1 τ2 s + 1
The first dynamics is slow (τ1 ); the second dynamics is fast (τ2 )
When τa < 0, we have k1 > 1, −1 < k2 < 0. The first gain is larger in
absolute value and ultimately dominates, but the second dynamics
exhibits itself transiently
′′
▶ y′ (0) = lim
s→∞ G(s) = 0, y (0) = lims→∞ sG(s) = Kτa /τ1 τ2 < 0
▶
▶

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

6 / 11

RHP zeros: Non-invertibility
Imagine: Given the plant G(s) with inverse response, you want to
design connect the plant to an extra device Q(s), so that G(s)Q(s)
has no inverse response.

▶

If so, you manipulate r(t) (the input to Q(s)), so that the output of
Q(s) will “automatically” manipulate the plant. The overall system
r → y has no inverse response. [Useful later in process control.]

When G(s) has a RHP zero, to cancel this RHP zero, Q(s) must have
a corresponding RHP pole (i.e., Q(s) is unstable)
In reality, you can’t exactly “assign” a pole. The resulting G(s)Q(s)
will contain both a RHP pole and a RHP zero ... even worse!
Conclusion: RHP zeros are non-invertible / irremovable.
The same holds for time delay e−θs .
Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

7 / 11

Summary: Time-domain analysis

Step, impulse (,ramp) responses
Characteristics of the step response of first- and second-order
systems
Poles, zeros, gain, time delay and their implications
Standard forms of transfer functions and their conversions

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

8 / 11

Exercise: Recognizing the form of a TF model

Step response of a complicated process
The engineer used a unit step input and got the following step response.
Determine the structure of G(s) (not its parameters).

Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

9 / 11

Exercise: Recognizing the form of a TF model

Start with the standard gain/time constant form.
(τ̄1 s + 1) . . . (τ̄m s + 1) −θs
G(s) = K
e
(τ1 s + 1) . . . (τn s + 1)
1 Poles: Is it stable? Is it oscillatory?
2 Gain & Delay: What is the ultimate output/input ratio? Deadtime
before response?
3 Zeros: Is there inverse response or overshoot? How many RHP zeros?
Wentao Tang (NCSU)

Zeros, State-Space Models

February 13, 2025

10 / 11

Exercise: Recognizing the form of a TF model

1

Poles: Negative real (stable system, non-oscillatory).
▶

2
3

Gain: K ≈ 0.33; Delay: θ ≈ 2.5
Zeros: Two on RHP (inverse response occurs twice, no overshoot).
▶

4

Denominator: (τ1 s + 1) · · · (τn s + 1), all τi > 0.

Numerator: (τ̄1 s + 1)(τ̄2 s + 1), both τ¯i on LHP. Also, n ≥ 3 since
m = 2.

Actual TF:
G(s) =
Wentao Tang (NCSU)

1 2
1
2s − s + 1
·
e−2.5s .
3 (s + 1)( 21 s + 1)( 31 s + 1)
Zeros, State-Space Models

February 13, 2025

11 / 11



## Metadata
- Source file: junk_drawer/Lecture 10 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
