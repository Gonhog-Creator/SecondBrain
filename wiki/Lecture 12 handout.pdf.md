# Lecture 12 handout.pdf

Source: junk_drawer/Lecture 12 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 12: Frequency-Domain Dynamical Analysis Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 12: Frequency-Domain Dynamical Analysis

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

February 25, 2025

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

0 / 14

Recapture: Frequency response

Frequency response: u(t) = A sin(ωt) → y(t) = Â sin(ωt + ϕ)
A.R. = Â/A = |G(iω)|, ϕ = ∠G(iω)
Bode diagram: A (log scale) v.s. ω (log scale), ϕ v.s. ω
K
First-order system G(s) = τ s+1
: a low-pass filter and a lag
0s
Lead-lag system G(s) = 1+τ
1+τ1 s : A.R. monotonic and has limits at two
ends, phase angle has a max/min

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

1 / 14

Learning objectives of this lecture
1

Calculate and explain the features of the frequency response of
non-minimum-phase and second-order systems

2

Calculate the frequency response of higher-order t.f. through the
factorization approach

3

Sketch Bode diagram by asymptotes

Hendrik W. Bode (1905–1982)

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

2 / 14

Example 5: Non-minimum-phase (NMP) systems

Consider t.f. (with static gain 1, denominator and numerator are
conjugates)
1 − iωτ
1 − τs
s=iω
(τ > 0)
⇒ G(iω) =
G(s) =
1 + τs
1 + iωτ
Exercise: Show that A.R.= 1, ϕ = −2 arctan(ωτ )
It does not “filter” any sinusoidal wave, but only causes the phase to
lag

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

3 / 14

NMP system and its minimum-phase counterpart

s
Any system with a RHP zero can factorize such an element 1−τ
1+τ s ...

(1 − τ s)(· · · )
1 − τ s (1 + τ s)(· · · )
1 − τs
=
·
=
G− (s)
(· · · )
1 + τs
(· · · )
1 + τs
In G− (s), RHP zero is “reflected” from +1/τ to −1/τ
G(s) =

G− (s) has the same A.R. but less phase lag
|G(iω)| = |G− (iω)|
∠G(iω) = ∠G− (iω) − 2 arctan(ωτ )
A system with RHP zeros G(s) is a non-minimum-phase system, and
G− (s) is its minimum-phase counterpart without RHP zeros

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

4 / 14

G(s) =

Wentao Tang (NCSU)

1−s
1+s
, G− (s) =
1 + 3s
1 + 3s

Frequency Domain Analysis

February 25, 2025

5 / 14

Example 6: Overdamped second-order systems

G(s) =

K
(K > 0, τ1 > τ2 > 0)
(1 + τ1 s)(1 + τ2 s)

s=iω

⇒ G(iω) = · · ·

Evaluate modulus and angle:
K
q
A.R. = |G(iω)| = q
1 + ω 2 τ12 1 + ω 2 τ22
ϕ = ∠G(iω) = − arctan(ωτ1 ) − arctan(ωτ2 )
When ω ≪ 1/τ1 : A.R.→ 1, ϕ → 0
When ω ≫ 1/τ2 : A.R.∝ ω −2 , ϕ → −π
If τ1 ≫ τ2 (time-scale separation), when 1/τ1 ≪ ω ≪ 1/τ2 ,
A.R.∝ ω −1 , ϕ ≈ −π/2

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

6 / 14

Example 7: Underdamped second-order systems

G(s) =
=

K
τ 2 s2 + 2τ ζs + 1

(K > 0, 0 < ζ < 1)

K
p
p
2
(τ s + ζ + i 1 − ζ )(τ s + ζ − i 1 − ζ 2 )

Evaluate modulus and angle:
K
p
p
|ζ + i(ωτ + 1 − ζ 2 )| · |ζ + i(ωτ − 1 − ζ 2 )|
K
= ··· = p
4
4
ω τp
+ (4ζ 2 − 2)ω 2 τ 2 + 1 p
ωτ + 1 − ζ 2
ωτ − 1 − ζ 2
ϕ = − arctan
− arctan
ζ
ζ

A.R. =

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

7 / 14

√
When ζ < √12 , at ωr =

1−2ζ 2
, A.R.= √K 2 reaches max.
τ
2ζ 1−ζ

Such a phenomenon is called resonance

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

8 / 14

Higher-order systems: Calculating frequency response
Guideline: Convert into a fractional T.F. and then factorize the
numerator and denominator
You should end up with a standard gain/time-constant form

Example 8: ”Filtered PID controller”
3
G(s) =
0.5s + 1



1
2
1+
+ s
3s 3



.
1

3
3s+1+2s
Adding the fractions: G(s) = 0.5s+1
3s

2

Factorize the terms: G(s) = (2s+1)(s+1)
s(0.5s+1)

3

2

Evaluate frequency response (term-wise)
√
√
1 + 4ω 2 1 + ω 2
π
√
A.R. =
, ϕ = arctan 2ω+arctan ω− −arctan 0.5ω
2
2
ω 1 + 0.25ω
Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

9 / 14

Higher-order systems: Sketching the Bode plot
G(s) = K
.

(1 + τ̄1 s) . . . (1 + τ̄m s) −θs
e (K > 0)
(1 + τ1 s) . . . (1 + τn s)

If RHP zeros exist, first extract (1 − τ s)/(1 + τ s) and plot for it
(A.R.= 1, ϕ = −2 arctan(ωτ ))
2 Plot for every lead (in numerator) and lag (in denominator)
1

Plot for gain (A.R.= K, ϕ = 0) and delay (A.R.= 1, ϕ = −ωθ)
4 Add these curves together
3

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

10 / 14

Example 9: NMP, two lead, double lag
G(s) = 0.5
1

(1 − s)(1 + 0.1s)
(1 + 10s)2

Factorize!

G1 (s)G2 (s)
1 − s (1 + s)(1 + 0.1s)
= KG0 (s)
1 + s (1 + 10s)(1 + 10s)
G3 (s)G4 (s)
2 Let’s plot for each of them
G(s) = 0.5

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

11 / 14

Higher-order systems: Sketching the Bode plot
Let’s plot for each of them

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

12 / 14

Higher-order systems: Sketching the Bode plot
Let’s add them together

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

13 / 14

Higher-order systems: Sketching the Bode plot
The actual Bode plot

Wentao Tang (NCSU)

Frequency Domain Analysis

February 25, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 12 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
