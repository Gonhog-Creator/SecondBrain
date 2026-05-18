# Homework Set 02 (1).pdf

Source: junk_drawer/Homework Set 02 (1).pdf

Category: [[academic-homework]]

## Summary
CHE 435/525 – Process Systems Analysis and Control Spring 2025 Homework Set 2. Laplace Transform and its Inverse, Transfer Function Model (Due on Friday, January 31, 2025) 1. (15 pt) Calculation with complex numbers

## Full Content
CHE 435/525 – Process Systems Analysis and Control

Spring 2025

Homework Set 2. Laplace Transform and its Inverse, Transfer Function Model
(Due on Friday, January 31, 2025)
1.

(15 pt) Calculation with complex numbers

Based on Euler’s formula, you should have reached at the following picture. That is, any complex number
can be expressed as z = x + yi (x = Re z, y = Im z) as well as z = reiθ (r = |z|, θ = ∡z). We can refer to (x, y) as
the Cartesian coordinate of z and (r, θ) as the polar coordinate of z. If you are not yet sure about this, please
review Problem 1 in the last homework.

(a) Using the polar coordinates, prove that
|z1z2| = |z1|·|z2|, ∡(z1z2) = ∡z1 + ∡z2,
and whenever z2 is nonzero,
|z1/z2| = |z1|/|z2|, ∡(z1/z2) = ∡z1 – ∡z2.
Note: In particular, |z | = |z| , ∡(z2) = 2∡z, |1/z| = 1/|z|, ∡(1/z) = –∡z.
2

2

(b) Using the relation x = r cos θ and y = r sin θ between the polar and Cartesian coordinates, prove
the following trigonometric formulas:
cos(θ1 + θ2) = cos θ1 cos θ2 – sin θ1 sin θ2,
sin(θ1 + θ2) = sin θ1 cos θ2 + cos θ1 sin θ2.
(c) Calculate (1 + i)/(√3 + 3i) in polar coordinate. You may need to be familiar with the trigonometric
function values of commonly used angles. Angles should be in radians (instead of degrees).
(d) Testify that you are fine with the above required calculations by writing “I understand and can use
the formulas for the moduli and arguments of products and quotients of complex numbers.”
2.

(20 pt) Laplace transform. [Seborg 3.1, 3.5, part of]

Find the Laplace transforms of the following functions. You may use Table 3.1 of Seborg.
(a) f(t) = 5 + exp(–3t) + t exp(–4t);
(b) f(t) = (t – 1)cos(4(t – 1))S(t – 1) + t2 (here S refers to the step function);
(c) The temperature profile T(t) below.

1

Hint: Consider T(t) as the sum (or difference) of a normal function in Table 3.1 and a function with a
delay (e.g., f(t − θ)).
3.

(20 pt) Inverse Laplace transform. [Seborg 3.6, part of]

Using PFE where required, found x(t) for:
s(s + 1)

(a) X(s) = (s

+ 2)(s + 3)(s + 4)
s+2

(b) X(s) = (s

(c) X(s) = 2

+ 1)2
1

s +s+1

4.

(15 pt) Qualitative behavior. [Seborg 3.10]

Which solutions of the following equations will exhibit convergent behavior (to zero or a nonzero
constant)? Which are oscillatory? Assume zero initial conditions for y and its derivatives.
(a)

d3 x
dt3
2

(b)
(c)

d x
dt2
d3 x
dt3

+2

d2 x
dt2

+2

dx
dt

+x=3

− x = 2et
+ x = sin t

2

(d)
5.

d x
dt2

+x=4

(10 pt) Transfer function of a measuring device. [Seborg 4.3]

The dynamic behavior of a pressure sensor/transmitter can be expressed as a first-order transfer function
(in deviation variables) that relates the measured value Pm to the actual pressure, P:
P′m (s)
1
=
.
′
P (s) 30s + 1
Both Pm and P have units of psi and the time constant has units of seconds. Suppose that an alarm will
̅m = P
̅ = 35 psi), and then P suddenly
sound if Pm exceeds 45 psi. If the process is initially at steady state (P
changes from 35 to 50 psi at 1:30 PM, at what time will the alarm sound?
6.

(20 pt) Linearization of a nonlinear process. [Seborg 4.13]

A horizontal cylindrical tank (shown in the left subfigure below) is used to slow the propagation of liquid
flow surges in a processing line. An end view of the tank is shown in the right subfigure below. wt is the
width of the liquid surface (note: the typo “wi” in the figure should actually be “wt”), which is a function of
its height, both of which can vary with time. Develop a model for the height of liquid h in the tank at any

2

time with the inlet and outlet volumetric flow rates as model inputs. Linearize the model assuming that the
process initially is at steady state and that the liquid density ρ is constant.

Hint: With geometry, you can verify that the volume holdup in the tank, V, is dependent on h via
h
V = [R2 arccos (1 − ) − (R − h)√R2 − (R − h)2 ] L.
R
Recall from calculus that
d
1
(arccos x) = −
.
dx
√1 − x2
7.

(Bonus: 10 pt) Process control in practice: Final control elements (FCEs).

List the main types of rotary valves. How are their mechanisms different? How are different types of rotary
valves suitable for different applications? You may want to read Section 9.2 of Seborg and/or look for resources
on the Internet. You should summarize your points, rather than copying a large volume of text.
8.

(Bonus: 10 pt) Process control in depth: Transfer function model of PDE systems.

In a tubular reactor where an elementary reaction A → B takes place, the concentration of A, x(z, t), depends
on the spatial coordinate z as well as time. The reactor is described by a PDE with boundary conditions:
∂x ∂2 x
=
− βx
∂t ∂z2
∂x
(z = 1, t) = 0.
∂z
To describe how the inlet concentration u(t) affects the outlet concentration y(t) = x(z = 1, t), we aim to find
x(z = 0, t) = u(t),

x(z = 1, t) +

the transfer function G(s) = Y(s)/U(s).
(a) By applying Laplace transform on the time variable (from x(z, t) to X(z, s)), show that X(z, s) (as a
function of z) satisfies the following ODE
d2 X
(z, s) = (s + β)X(z, s),
dz2
and also convert the boundary conditions on X(z, s).
(b) Show that the transfer function is
G(s)=

√s + β
sinh √s + β + √s + β cosh √s + β

where sinh a = (ea – e–a)/2 and cosh a = (ea + e–a)/2 are the hyperbolic sine and cosine, respectively.

3



## Metadata
- Source file: junk_drawer/Homework Set 02 (1).pdf
- Extracted: 2026-05-18
- Category: academic-homework
