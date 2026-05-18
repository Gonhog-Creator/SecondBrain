# Lecture 05 handout.pdf

Source: junk_drawer/Lecture 05 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 5: Further Properties of Laplace Transform Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 5: Further Properties of Laplace Transform

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

January 21, 2025

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

0 / 12

Discuss & Recapture

How do the Laplace transforms of step, impulse, exponential,
sinusoidal signals look like?

How to do partial fraction expansion for any given fractional function
of s?
How to use Laplace transform to solve ODEs?

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

1 / 12

Learning objectives of this lecture

1

Further properties of Laplace transform: Scaling of t, multiplication
by t, final and initial value

2

Use Laplace transform for process examples described by ODEs

3

Analyze the qualitative behaviors of a signal from its Laplace
transform

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

2 / 12

Laplace transform

Definition
Given a function (“signal”) f (t) on t ≥ 0, its Laplace transform is
Z ∞
f (t)e−st dt
F(s) = L[f (t)] =

(1)

0

comprehended as a function of a complex variable s.
Property 3: Scaling of t
Z ∞
Z ∞
1
1 s
−st
L[f (at)] =
f (at)e dt =
f (t̄)e−st̄/a d t̄ = F
.
a
a
a
0
0
Property 4: Multiplication by t
Z ∞
Z ∞

d 
−st
L[tf (t)] =
tf (t)e dt =
−
f (t)e−st dt = −F ′ (s).
ds
0
0

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

3 / 12

Practice problems

1
Exercise 1: L−1 [ (s+a)
2 ] =?
1
Exercise 2: L−1 [ τ s+1
] =?

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

4 / 12

Final and initial value theorems

Final value theorem: If limt→∞ y(t) exists, then
lim y(t) = lim sY (s).

t→∞
▶

s→0

The condition must not be violated! For y(t) = et , Y (s) = 1/(s − 1),
∞ = lim y(t) ̸= lim sY (s) = 0.
t→∞

s→0

Initial value theorem:
lim y(t) = lim sY (s).
t→0

Wentao Tang (NCSU)

s→∞

Laplace Transform Properties

January 21, 2025

5 / 12

SISO system modeled as ODE

The reason for doing L.T. is to deal with process dynamics, described
by linear or nonlinear ODEs.
If we have only one input (MV or DV) and only one output, the
system is called single-input-single-output (SISO).
In general, a linear SISO system can be expressed as
dny
d n−1 y
dy
+
a
+ · · · + a1 + a0 y =
n−1
n
n−1
dt
dt
dt
d m−1 u
du
dmu
+ bm−1 m−1 + · · · + b1 + b0 u
m
dt
dt
dt
where y(t) is the output and u(t) is the input.

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

(2)

6 / 12

SISO system modeled as transfer function
We are interested in how y(t) respond to u(t). Hence, we usually
assume initial conditions y(0) = 0, y′ (0) = 0, ..., y(n−1) (0) = 0.
Use Laplace transform
sn Y (s) + an−1 sn−1 Y (s) + · · · + a1 sY (s) + a0 Y (s) =
bm sm U(s) + bm−1 sm−1 U(s) + · · · + b1 sU(s) + b0 U(s).
We obtain
Y (s) =

bm sm + bm−1 sm−1 + · · · + b1 s + b0
U(s).
sn + an−1 sn−1 + · · · + a1 s + a0

Definition
The factor Y (s)/U(s) = G(s) is called the transfer function from the input
to the output
bm sm + bm−1 sm−1 + · · · + b1 s + b0
G(s) =
.
sn + an−1 sn−1 + · · · + a1 s + a0
Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

7 / 12

Calculating output response via Laplace transform
Seborg Ex.3.4(a)
Given the process model
dy
d2y
+ 6 + 8y = 3u(t),
2
dt
dt
where y(0) = 0, y′ (t) = 0, find y(t) for u(t) = be−2t .
1

By L.T., (s2 + 6s + 8)Y (s) = 3U(s), i.e., G(s) = 3/(s2 + 6s + 8).

2

U(s) = b/(s + 2). Thus,

3b
3b
=
.
(s + 2)(s2 + 6s + 8)
(s + 2)2 (s + 4)
3 Do partial fraction expansion:
a1
a2
a3
3b
=
+
+
,
Y (s) =
2
2
(s + 2) (s + 4)
s + 2 (s + 2)
s+4
Y (s) =

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

8 / 12

Calculating output response by Laplace transform
Seborg Ex.3.4(a)
Given the process model
d2y
dy
+ 6 + 8y = 3u(t),
2
dt
dt
where y(0) = 0, y′ (t) = 0, find y(t) for u(t) = be−2t .
6

Determine coefficients:
3b = a1 (s + 2)(s + 4) + a2 (s + 4) + a3 (s + 2)2
by 3b = 2a2 (by setting s = −2), 3b = 4a3 (by setting s = −4), and
a1 + a3 = 0.

7

3b/4
3b/2
Thus, Y (s) = −3b/4
s+2 + (s+2)2 + s+4 .

y(t) = L−1 [Y (s)] = −

Wentao Tang (NCSU)

3b −2t 3b −2t 3b −4t
e + te + e .
4
2
4

Laplace Transform Properties

January 21, 2025

9 / 12

Key observation
The values and multiplicities of the roots of denominator determine
what terms will appear after inverse L.T.
···
···
⇒ Y (s) = · · · +
Y (s) =
+ ···
· · · · (s − r)k · · · ·
(s − r)k
⇒ y(t) = · · · + const · t k−1 ert + · · ·
When r = a + bi, t k−1 ert = t k−1 eat (cos bt + i sin bt).
If a = Re r < 0 (r is on the left half plane), then the term decays
exponentially.
▶ If a = Re r > 0 (r is on the right half plane), then the term grows
exponentially.
▶ If a = Re r = 0 and k ≥ 2 (repeated root on the imaginary axis), then
the term grows polynomially (∝ t k−1 ).
▶ Whenever b = Im r ̸= 0 (r is not real), the term is oscillatory.
▶ If a = Re r = 0, b = Im r ̸= 0 and k = 1 (simple imaginary root), then
the term persistently oscillates.
▶ If a = Re r = 0, b = Im r = 0 and k = 1 (simple root at 0), then the
term is constant.
▶

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

10 / 12

Qualitative behavior analysis

Thus, given Y (s), we can know how y(t) behaves as t increases.
y(t) is dominated by the term(s) t k−1 ert whose r has the right-most
real part.
▶ Think about

▶

y(t) = −2e(1+3i)t + 5e2it − 4 − 7e−2−10i
When t is large enough, which term dominates?

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

11 / 12

Qualitative behavior analysis

Practice: Seborg Ex.3.9
Determine what functions of time will appear in y(t) in the following
cases. Which y(t) are oscillatory? Which have a constant value for large
values of t?
1

2
Y (s) = s2 (s+4)

2

2
Y (s) = s(s+1)(s+3)

3

2
Y (s) = s(s+2)
2

4

2
Y (s) = s(s2 +4s+8)

5

2(s+1)
Y (s) = s(s
2 +4)

Wentao Tang (NCSU)

Laplace Transform Properties

January 21, 2025

12 / 12



## Metadata
- Source file: junk_drawer/Lecture 05 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
