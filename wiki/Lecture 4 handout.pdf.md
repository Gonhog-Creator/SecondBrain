# Lecture 4 handout.pdf

Source: junk_drawer/Lecture 4 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 4: Laplace Transform and Its Use in ODEs Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 4: Laplace Transform and Its Use in ODEs

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

January 21, 2025

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

0 / 14

Discuss & Recapture

What complicates the modeling when the system involves reactions?

How do we account for multiple reactions?
** What behaviors can a nonlinear system have?

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

1 / 14

Learning objectives of this lecture

1

Calculate Laplace transform of common functions of time

2

Calculate inverse Laplace transforms through partial fraction
expansion

3

Analytically calculate the output response to input signals

A quote from Laplace
Ce que nous connaissons est peu de chose, ce que nous ignorons est
immense. (What we know is not much. What we do not know is
immense.)
Pierre-Simon, Marquis de Laplace (1749–1827)

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

2 / 14

Laplace transform
Definition
Given function (“signal”) f (t) on t ≥ 0, its Laplace transform is
Z ∞
F(s) = L[f (t)] =
f (t)e−st dt

(1)

0

comprehended as a function of a complex variable s.
Property 0: Laplace transform is linear:
L[af (t) + bg(t)] = aL[f (t)] + bL[g(t)]
Example 0: Step function
(
0, t < 0
S(t) =
1, t ≥ 0
For a step of magnitude a:

Z ∞
⇒ L[S(t)] =
0

1
1e−st dt = .
s

L[aS(t)] = a/s

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

3 / 14

Exponential and sinusoidal functions

Property 1: Exponential term
Z ∞
f (t)eat−st dt = F(s − a).
L[f (t)eat ] =
0

Example 1: Exponential function
L[eat ] =

1
.
s−a

Sine and cosine: 




eiat + e−iat
1
1
1
s
L[cos at] = L
=
+
= 2
.
2 s − ia s + ia  s + a2
 iat 2 −iat 
e −e
1
1
1
a
L[sin at] = L
=
−
= 2
.
2i
2i s − ia s + ia
s + a2

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

4 / 14

Differentiating/Integrating over time

Property 2: If f is differentiable,


L f ′ (t) = sF(s) − f (0)
If f (0) = 0, L[f ′ ] = sF(s) (d/dt ⇒ multiplication by s)
▶ More generally,

▶

L[f (n) ] = sn F(s) − sn−1 f (0) − sn−2 f ′ (0) − · · · − sf (n−2) (0) − f (n−1) (0).

Hence, if g(t) =

Rt

′
0 f (τ )dτ , then g (t) = f (t) and g(0) = 0, implying

G(s) = F(s)/s.
Rt

( 0 ⇒ division by s)

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

5 / 14

Ramp and impulse
By integrating over t on L[S(t)] = 1/s,
L[t] = 1/s2 (ramp), L[t 2 /2] = 1/s3 , . . . L[t n /n!] = 1/sn+1
By differentiating over t on L[S(t)] = 1/s,
L[S ′ (t)] = 1
... What is the derivative of a step?
Dirac’s δ function (impulse): δ(t) = S ′ (t)

δ(t) = 0 when t ̸= 0; δ(t) = +∞ when t = 0;
Wentao Tang (NCSU)

Laplace Transform

R∞
0

δ(t)dt = 1.
January 21, 2025

6 / 14

Practice problems

Exercise 1: L[sin(ωt + ϕ)] =?
Exercise 2: L[t n e−at ] =?
Exercise 3: If L[f ] = F(s), then L[f (t − θ)S(t − θ)] =?
▶
▶

Answer: e−θs F(s)
Delay by θ ⇒ Multiplication by a factor of e−θs

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

7 / 14

Solving ODE by Laplace transform

Solve ODE [Seborg Ex.3.16]
Determine solution y(t) for ODE
dy
d2y
+ 6 + 9y = cos t
2
dt
dt
with initial condition y(0) = 1, y′ (0) = 2.
Laplace transform on both sides:
[s2 Y (s) − sy(0) − y′ (0)] + 6[sY (s) − y(0)] + 9Y (s) =
(s2 +6s+9)Y (s)−s−8 =

s
s2 + 1

⇒

Y (s) =

s

.

s2 + 1
s + (s + 8)(s2 + 1)

(s2 + 6s + 9)(s2 + 1)

Only have to find whose Laplace transform this is.

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

8 / 14

Partial Fraction Expansion
Goal: Invert the Laplace transform for any fractional function of s

Case 1: Denominator has simple roots
Question: Find L−1

h

2s+7
s2 +6s+8

i
.

1

Find the roots: s2 + 6s + 8 = (s + 2)(s + 4) (roots are −2, −4)

2

Let

2s + 7
s2 + 6s + 8

=

c1
c2
+
s+2 s+4

Determine c1 and c2 (by multiplying both sides by the denominator):
(
(
c1 + c2 = 2
c1 = 1.5
2s+7 = c1 (s+4)+c2 (s+2) ⇒
⇒
4c1 + 2c2 = 7
c2 = 0.5
h
i
i
h
2s+7
1.5
0.5
4 Hence, L−1 2
= L−1 s+2
+ s+4
= 1.5e−2t + 0.5e−4t .
s +6s+8
3

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

9 / 14

Partial Fraction Expansion
Case 2: Denominator has repeated roots
Question: Find L−1

h

2s+7
s2 +6s+9

i
.

1

Find roots: s2 + 6s + 9 = (s + 3)2 (roots are −3 with multiplicity 2)

2

Let

3

Determine c1 and c2 :

2s + 7
c1
c2
=
+
s2 + 6s + 9
s + 3 (s + 3)2

(
c1 = 2
2s + 7 = c1 (s + 3) + c2 ⇒
c2 = 1
h
i
h
i
2s+7
2
1
4 Hence, L−1 2
= L−1 s+3
+ (s+3)
= 2e−3t + te−3t .
2
s +6s+9

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

10 / 14

Partial Fraction Expansion
Case 3: Denominator has complex roots – Do it as usual.
Question: Find L−1

h

2s+7
s2 +6s+13

i
.

1

Find the roots: s2 + 6s + 13 = (s + 3 + 2i)(s + 3 − 2i)

2

Let

2s + 7
s2 + 6s + 13

=

c1
c2
+
s + 3 + 2i s + 3 − 2i

Determine c1 and c2 by 2s + 7 = c1 (s + 3 − 2i) + c2 (s + 3 + 2i) ⇒
(
(
c1 + c2 = 2
c1 = 1 + 0.25i
⇒
(3 − 2i)c1 + (3 + 2i)c2 = 7
c2 = 1 − 0.25i
h
i
2s+7
4 Hence, L−1 2
= (1 + 0.25i)e−3t−2it + (1 − 0.25i)e−3t+2it .
s +6s+13
3

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

11 / 14

Partial Fraction Expansion

Case 3: Denominator has complex roots – Do it as usual.
i
h
2s+7
.
Question: Find L−1 s2 +6s+13
h
i
2s+7
5 Hence, L−1 2
= (1 + 0.25i)e−3t−2it + (1 − 0.25i)e−3t+2it .
s +6s+13
6

In view of Euler’s formula
e2it + e−2it = 2 cos 2t, e2it − e−2it = 2i sin 2t,
we have
−1

L

Wentao Tang (NCSU)




2s + 7
= e−3t [2 cos 2t − 0.5 sin 2t] .
s2 + 6s + 13

Laplace Transform

January 21, 2025

12 / 14

Solving ODE by Laplace transform
Solve ODE [Seborg Ex.3.16]
2

Determine solution y(t) for ODE ddt 2y + 6 dy
dt + 9y = cos t with initial
condition y(0) = 1, y′ (0) = 2.
From Laplace transform,
s + (s + 8)(s2 + 1)
s3 + 8s2 + 2s + 8
Y (s) = 2
=
(s + 6s + 9)(s2 + 1)
(s + 3)2 (s + i)(s − i)
Now do PFE. Let
s3 + 8s2 + 2s + 8
c1
c2
c3
c4
=
+
+
+
2
2
(s + 3) (s + i)(s − i)
s + 3 (s + 3)
s+i s−i
s3 + 8s2 + 2s + 8 =c1 (s + 3)(s + i)(s − i) + c2 (s + i)(s − i)
+ c3 (s + 3)2 (s − i) + c4 (s + 3)2 (s + i)

Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

13 / 14

Solving ODE by Laplace transform
Usual approach: Expand R.H.S. and match the coefficients
** Tricky approach: Match by plugging in the roots
s3 + 8s2 + 2s + 8 =c1 (s + 3)(s + i)(s − i) + c2 (s + i)(s − i)
+ c3 (s + 3)2 (s − i) + c4 (s + 3)2 (s + i)
Examine s = −3: 47 = c2 (−3 + i)(−3 − i) ... c2 = 4.7
Examine s = −i: −i = c3 (−i + 3)2 (−2i) ... c3 = 0.04 + 0.03i
▶ Examine s = −i: i = c (i + 3)2 (2i) ... c = 0.04 − 0.03i
4
4
▶ Need another eq.: 1 = c1 + c3 + c4 for the coeff. of s3 ... c1 = 0.92
▶
▶

Finally,
−1



y(t) =L

0.92
4.7
0.04 + 0.03i 0.04 − 0.03i
+
+
+
2
s + 3 (s + 3)
s+i
s−i



= 0.92e−3t + 4.7te−3t + (0.04 + 0.03i)e−it + (0.04 − 0.03i)eit
= 0.92e−3t + 4.7te−3t + 0.08 cos t + 0.06 sin t
Wentao Tang (NCSU)

Laplace Transform

January 21, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 4 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
