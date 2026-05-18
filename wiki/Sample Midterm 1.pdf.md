# Sample Midterm 1.pdf

Source: junk_drawer/Sample Midterm 1.pdf

Category: [[academic-homework]]

## Summary
N ORTH C AROLINA S TATE U NIVERSITY D EPARTMENT OF C HEMICAL AND B IOMOLECULAR E NGINEERING CHE 435 / CHE 525 Process Systems Analysis and Control Sample Midterm Exam 1 with Study Guide Instructor: Prof. Wentao Tang February 19, 2025

## Full Content
N ORTH C AROLINA S TATE U NIVERSITY
D EPARTMENT OF C HEMICAL AND B IOMOLECULAR E NGINEERING
CHE 435 / CHE 525

Process Systems Analysis and Control

Sample Midterm Exam 1 with Study Guide
Instructor: Prof. Wentao Tang
February 19, 2025

Name (print legibly):

• Test is closed book, closed notes. You may use an unlimited pages of torpedo sheet and a nonprogrammable calculator.
• Turn off all cell phones and smart watches and put them away. We will display a clock.
• Sit with a seat between each person if possible. Remove all hats, caps, and hoods. Keep your
eyes on your own paper. To the extent you can, only display the page you are working on.
• If there is scrap work you don’t want to be graded, write on the back of the paper or clearly
cross it out. Only work in the boxed area will be graded.
• We will clarify wording, but we will not tell you how to do the problem or if your answer is
correct. If you have a question, come up front to ask the instructor/TA.
• You can have additional paper if needed — raise your hand. Any answers written on the back
of the pages cannot be scanned and hence will not graded.
• Only one person can leave the room at a time. Leave your test in the room when you leave. No
exits in the last 20 minutes of the test period.
• Before handing in the test, make sure the problems are in order and re-staple if necessary.
• Please do not discuss the exam within 48 hours, so as to keep the exam problems confidential
until everyone has taken the exam.

1

CHE 435 / CHE 525

Sample Midterm Exam 1 with Study Guide

February 19, 2025

1. Calculate the following.
(a) the modulus and argument of i/(1 + i ).
Solution:

|i |
1
i
=
=√ .
1+i
|1 + i |
2
∠

i
π π
π
= ∠i − ∠(1 + i ) = − = .
1+i
2
4
4

(b) the Laplace transform of the following “pulse” signal:
(
1/a, 0 ≤ t < a
f (t) =
0,
t≥a
where a > 0 is a constant. (Hint: To verify your answer, you may check that F (s) → 1 as a → 0.)
Solution:
F (s) =

Z ∞

f (t)e

−st

0

=

Z a
0

1 −st
1 − e−as
e dt =
.
a
as

Alternatively, note that f (t) = 1a (1 − S(t − a)). For the delayed unit step S(t − a), we have
L[S(t − a)] = 1s e−as . Therefore,
1
F (s) =
a



1 1 −as
− e
s
s



=

1 − e−as
.
as

Indeed, as a → 0 (the pulse approaches a unit impulse), F (s) → 1. This is due to the limit
−x
limx→0 1−xe = 1.
(c) the inverse Laplace transform of 1/(s2 + 4).
Solution: We know that L[sin 2t] = s2 2+4 . Therefore,

L −1




1
1
= sin 2t.
s2 + 4
2

Skills required:
• Use Euler’s formula to perform calculations on modulus and argument of complex numbers, or
convert between forms of eiθ and cos θ + i sin θ.
• Perform Laplace transform based on definition or common properties – linearity, multiplication
by e−at , multiplication by t, delayed signal, etc.
• Perform inverse Laplace transform based on the common properties, by memorization, derivation, and/or using a Laplace transform table.

Page 2 of 6

CHE 435 / CHE 525

Sample Midterm Exam 1 with Study Guide

February 19, 2025

2. Suppose that a process is described by the following ODE:
d2 y ( t )
dy(t)
−2
+ y(t) = 3u(t).
2
dt
dt
(a) What is the static gain of the system?
Solution: The transfer function is
Y (s)
3
= 2
.
U (s)
s − 2s + 1
Since the system is unstable (has poles not on the left half plane), there does not exist a static
gain.
(b) Calculate and plot its unit impulse response.
Solution: For the unit impulse input, U (s) = 1 and hence Y (s) = (s−31)2 . By inverse Laplace
transform,
y(t) = 3tet .
(The plot is omitted.)
Skills required:
• Convert between an ODE and a transfer function model.
• Calculate impulse and step responses of a transfer function, by Laplace transform and its inverse.
• Indicate the poles, zeros, and static gain (but first whether they exist) of a transfer function.
Skills required:
• Convert between an ODE and a transfer function model.
• Calculate impulse and step responses of a transfer function, by Laplace transform and its inverse.
• Indicate the poles, zeros, and static gain (but first whether they exist) of a transfer function.

Page 3 of 6

CHE 435 / CHE 525

Sample Midterm Exam 1 with Study Guide

February 19, 2025

3. The unit step response of an unknown process is plotted below. The engineer John Doe suspects that
it has a second-order transfer function
G (s) =

K
τ 2 s2 + 2τζs + 1

.

(a) If John is correct, when should the second peak occur?
Solution: The peak time t p = 2 min, and hence the period is 2t p = 4 min. The second peak
occurs at 6 min.
(b) Determine the static gain K.
Solution: We use the relation that decay ratio = overshoot2 . That is,
0.8 − K
=
1−K



1−K
K

2

⇒ 0.8K2 − K3 = (1 − K )3
⇒ 2.2K2 − 3K + 1 = 0

⇒ 0.8K2 − K3 = 1 − 3K + 3K2 − K3
⇒ K = 0.7834

Hint: For a second-order system, time to first peak t p = √πτ 2 , period = 2πτ/

1− ζ
overshoot (as a ratio) = exp(− √πζ 2 ), decay ratio = exp(− √2πζ 2 ) = overshoot2 .
1− ζ
1− ζ

p

1 − ζ 2 = 2t p ,

Disclaimer: Ruler measurements on the paper may not represent the actual relations.
Skills required:
• For first- and underdamped second-order systems, find the characteristic quantities of the step
response from the parameters (K, τ, ζ).
• For first- and underdamped second-order systems, find the system parameters from the data on
the step response curve.
• For second-order systems, discriminate overdamped, critically damped, and underdamped systems, and explain the difference of their qualitative behaviors.

Page 4 of 6

CHE 435 / CHE 525

Sample Midterm Exam 1 with Study Guide

February 19, 2025

4. A system of two liquid storage tanks in series is shown in the figure below.

(a) Assume that the volumetric flow rate of the
p outgoing stream from each
p tank is proportional to the
square root of liquid height (Fout,1 = C1 h1 (t) and Fout,2 (t) = C2 h2 (t)). Use material balance
equations to derive a dynamic model for the system of tanks.
Solution: The model should be
F (t) − C1
dh1
= in
dt
A1

p

h1 ( t )

,

C
dh2
= 1
dt

p

h1 (t) − C2
A2

p

h2 ( t )

.

(b) At a steady state, the inlet volumetric flow rate is F̄in . Express the liquid heights in the two tanks,
h̄1 and h̄2 , in terms of F̄in , and then linearize the dynamic model at this steady state.
Solution: At the steady state, dh1 /dt = 0 and dh2 /dt = 0. Hence,
q
p
p
F̄in − C1 h̄1 = 0, C1 h̄1 − C2 h̄2 = 0.
That is,
h̄1 = ( F̄in /C1 )2 ,

h̄2 = (C1 /C2 )2 h̄1 = ( F̄in /C2 )2 .

Given the partial derivatives:
√ !
C12
steady state
∂
Fin − C1 h1
C1
C1
√
=−
=−
−→ −
∂h1
A1
2A1 ( F̄in /C1 )
2A1 F̄in
2A1 h1
!
√
∂
1 steady state 1
Fin − C1 h1
=
−→
∂Fin
A1
A1
A1
√
√ !
C12
steady state
C1 h1 − C2 h2
C1
∂
C1
√
=
−→
=
∂h1
A2
2A2 ( F̄in /C1 )
2A2 F̄in
2A2 h1
!
√
√
steady state
C22
∂
C1 h1 − C2 h2
C2
C2
√
=−
−→ −
=−
∂h2
A2
2A2 ( F̄in /C2 )
2A2 F̄in
2A2 h2
the linearized model is
C12
dh1′
1 ′
=
Fin (t) −
h ′ ( t ),
dt
A1
2A1 F̄in 1

C12
C22
dh2′
=
h1′ (t) −
h ′ ( t ).
dt
2A2 F̄in
2A2 F̄in 2

Page 5 of 6

CHE 435 / CHE 525

Sample Midterm Exam 1 with Study Guide

February 19, 2025

′ ( t ) = V δ ( t )), how will
(c) If a volume V0 of liquid is suddenly pushed into the first tank (i.e., Fin
0
h2 (t) respond?

Solution: By Laplace transform, we find the following transfer functions of the two tanks,
respectively:

= 2A F̄

2A1 F̄in

C12

2 F̄in
C12

1

H1′ (s)
A1
=
′
C2
Fin (s)
s+ 1

1 in

C12

s+1

H2′ (s)
2A2 F̄in
=
′
C2
H1 (s)
s+ 2

,

= 2A F̄

C12
C22

2 in

C22

2A2 F̄in

s+1

.

Connecting the two tanks (i.e., multiplying the two transfer functions), we obtain
C12
C22

C22

H2′ (s)
2A2 F̄in
′ (s) =
C2
Fin
s+ 2

2A2 F̄in

=

2A1 F̄in
s+1
C12



2A2 F̄in
s+1
C22

.

This is a second-order system with K = C12 /C22 .
• If A1 /C12 = A2 /C12 , denote τ = 2A1 F̄in /C12 . The system is critically damped: G (s) =
′ ( s ) = V , we have H ′ ( s ) = KV / ( τs + 1)2 . By inverse
K/(τs + 1)2 . Given that Fin
0
0
2
Laplace transform, we have
KV0 t −t/τ
e
.
h2′ (t) =
τ2
• If A1 /C12 ̸= A2 /C12 , denote τ1 = 2A1 F̄in /C12 and τ2 = 2A2 F̄in /C22 . The system is overdamped: G (s) = K/(τ1 s + 1)(τ2 s + 1). We have
!
KV
KV
1
KV
1
1
1
1
0
0
0
H2′ (s) =
=
=
−
.
(τ1 s + 1)(τ2 s + 1)
τ1 τ2 s + τ1 s + τ1
τ1 τ2 τ1 − τ1 s + τ1
s + τ12
2
2
1
1
1
By inverse Laplace transform,
h2′ (t) =


KV0  −t/τ1
− e−t/τ2 .
e
τ1 − τ2

Skills required:
• Use material and energy balance to build the model of a plant.
• Indicate the inputs (cause) and outputs (outcome) based on the process description and engineering common sense.
• Explain the meaning of a steady state (d/dt of every variable is 0), and determine the inputoutput relation at the steady state.
• Linearize the process model around the steady state through partial differentiation.
• Determine the transfer function in the presence of parallel or series connections of transfer functions.
• Perform calculations in symbols.

Page 6 of 6



## Metadata
- Source file: junk_drawer/Sample Midterm 1.pdf
- Extracted: 2026-05-18
- Category: academic-homework
