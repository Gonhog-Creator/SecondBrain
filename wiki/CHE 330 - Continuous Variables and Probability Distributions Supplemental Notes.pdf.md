# CHE 330 - Continuous Variables and Probability Distributions Supplemental Notes.pdf

Source: junk_drawer/CHE 330 - Continuous Variables and Probability Distributions Supplemental Notes.pdf

Category: [[academic-lecture]]

## Summary
Department of Chemical & Biomolecular Engineering North Carolina State University CHE 330 Spring 2011 † Continuous Variables & Probability Distributions Continuous Variables

## Full Content
Department of Chemical & Biomolecular Engineering
North Carolina State University
CHE 330

Spring 2011
†

Continuous Variables & Probability Distributions

Continuous Variables
Continuous variables are variables that take on fractional values, examples include temperature,
pressure and pH readings, length, volume, weight and density measurements, mole number and
concentration, distance travelled, lifetime, etc. A continuous variable can theoretically carry as
many significant figures as one can imagine and, as such, no two continuous variables, even if
they are of the same kind, can ever take on exactly the same value. Thus, a temperature reading
of 25.0 oC is, in principle, different from a reading of 25.01 oC that is, in turn, different from
25.001 oC, even though the differences may be of little practical significance. Because a
continuous variable can take on an infinite number of possible values within any given interval
(by simply extending the number of significant figures beyond the decimal point), the probability
of the continuous variable taking on any specific value is one out of infinite possibilities or zero.
It follows that a continuous variable has a zero probability of taking on any specific value. A
non-zero probability can only be assigned to a continuous variable if an interval or a range of
values is specified for the continuous variable.
The probability distribution for a continuous variable x is given by the probability density
function f(x), which is defined as probability per unit interval of a possible range of x value. The
following relationships hold for a probability density function f(x) for a continuous variable x:
x2

P ( x1 < x < x2 ) ≡ Probability of x falling in the x1− x2 range = ∫ f ( x)dx
x1

∞

∫ f ( x)dx =1.0 for a normalized probability density function f (x )
E ( x) ≡ < x > = ∫ xf ( x)dx
E[ y ( x)] ≡ < y ( x) > = ∫ y ( x) f ( x)dx
σ ≡ variance of x ≡ E[( x − <x>) ] = ∫ ( x − <x>) f ( x)dx
σ ≡ standard deviation of x ≡ SQRT(σ ) = SQRT ⎡ ∫ ( x − <x>) f ( x )dx ⎤
⎢⎣
⎥⎦
−∞

∞

−∞

∞

−∞

2

2

∞

2

−∞

2

∞

−∞

2

(1)

(2)
(3)
(4)
(5)
(6)

Some Known Probability Density Functions for Continuous Variables
(A) Uniform Probability Density Function
A uniform probability density function can be represented generally by
⎧ 1
for a < x < b
⎪
(7)
f ( x) = ⎨ b − a
⎪⎩ 0 for x < a and x > b
where a and b are constants.
______________________________________________________________________________
†
P. K. Lim, Department of Chemical & Biomolecular Engineering, North Carolina State
University, Raleigh, NC 27695-7905, February 4, 2011.

The mean μ and variance σ2 of the continuous variable x with the uniform probability density
function given in Eqn (7) are given by:
b
∞
b
x
0.5
0.5 2
2
⎡
⎤
μ = ∫ x. f ( x)dx = ∫
dx =
=
(b − a 2 ) = 0.5(b + a)
x
−∞
a b−a
b−a ⎣
⎦a b − a
∞

b

−∞

a

σ 2 = ∫ ( x − μ )2 f ( x)dx = ∫ ( x − μ ) 2
b

⎤
1 ⎡x
1 ⎡ ⎛x
2
2 ⎤
2⎞
=
μ
μ
μ
μ
−
+
−
+
x
x
x
x
⎟⎥
⎥ b−a ⎢ ⎜
b−a ⎢ 3
3
3

σ2 =

σ2 =

2
2
b ( x − 2μ x + μ )
1
dx = ∫
dx
a
b−a
b−a

2

⎣

⎦

2

2

2

⎢⎣ ⎝

a

⎠ ⎥⎦

b

a

2

(b − a )
(b − a )
− μ (b − a ) + μ 2 =
− 0.5(b + a)(b − a) + 0.52 (b + a ) 2
3
3
(b + 5a )
⎡ (b − a ) (b − a ) (b + a ) ⎤
−
+
= (b + a )
⎥
2
4 ⎦
12
⎣ 3

σ 2 = (b + a ) ⎢

Example 1 A spinning dial shown below will come to rest with the pointer aligned randomly
with any of the degree markings in the range of 0−360 on the dial face. Determine the
probability that the dial will come to rest with the pointer aligned in 20−65o range.

Solution
The dial pointer reading R has a uniform probability density function given by
1
1
1
f ( R) =
=
=
o
360o
b − a (360 − 0)
65o

1
(65 − 20)o 45 1
dR
=
=
= = 0.125
20 360o
360o
360 8
65o

P(20o < R < 65o ) = ∫ o f ( R)dR = ∫ o
20

Example 2 The wait time t, in minutes, for a bus to arrive is uniformly distributed between 0 and
15 minutes. Determine (a) the probability density function of the wait time, (b) the average and
standard deviation of the wait time, (c) the probability that a person would wait less than 12.5
minutes.
Solution
(a) If the probability density function of the wait time t is uniformly distributed, it would be
⎧c for 0 min < t < 15 min
(2-1)
given by f (t ) = ⎨
⎩ 0 for t > 15 min
where c is a constant.

But 1 = ∫

∞

−∞

f (t ) dt = ∫

15min

0

[]

cdt = c t

15min
0

= c15 min

∴c =

1
15 min

Therefore, the probability density function of the wait time t is given by
⎧ 1
for 0 min < t < 15 min
⎪
f (t ) = ⎨15 min
⎪⎩ 0
for t > 15 min
∞

15min

−∞

0

(b) The average wait time is given by E (t ) = ∫ tf (t )dt = ∫
∞

15 min

−∞

0

σ 2 = ∫ (t − < t >)2 f (t )dt = ∫

σ2 =

t 2 − 2*7.5min t + 7.52 min 2
dt
15 min

⎡ 3

t
1
2
2
2 ⎤
−
+
7.5min
7.5
min
t
t⎥
15 min ⎢ 3
⎣

σ = 18.75 min
2

t
152
dt =
min = 7.5 min
15 min
30

⎦

15 min

⎛ 152
⎞
=⎜
− 7.5*15 + 7.52 ⎟ min 2
⎝ 3
⎠
0

∴σ = ±4.330 min

2

(c) P (t < 12.5 min) = ∫

12.5 min

0

1
12.5
dt =
= 0.8333
15 min
15

(B) Exponential Probability Density Function
The exponential probability density function for a random continuous variable x is given by
⎧λ exp(−λ x)
f ( x) = ⎨
0
⎩

for x ≥ 0
for x < 0

(8)

where λ is a positive constant known as the rate or decay parameter. The corresponding
cumulative probability distribution function is given by
x
⎧1 − exp(−λ x)
F ( x) ≡ ∫ f ( x)dx = ⎨
0
⎩
−∞

for x ≥ 0
for x < 0

(9)

The mean (or expected) value and variance of an exponentially distributed random variable X
with the rate parameter λ are given, respectively, by

∞

⎡
⎤
P
−λ x ⎥
E ( x) = ∫ xf ( x)dx = ∫ Ox λ exp(−λ x)dx = ⎢ x − exp
− ∫ ( − exp λ ) dx


O

⎢u 
⎥
v
⎣
⎦
1
1
⎡
⎤
⎡
⎤ or
E ( x) = − x exp(−λ x) − exp(−λ x) = − ( x − )exp(−λ x)
⎢⎣
⎥⎦
⎢⎣
⎥⎦
λ
λ
∞

∞

−∞

0

product
rule

u

dv

(

)

∞

− x

0

du

v

0

∞

∞

0

0

1 ⎤ 1
⎡
E ( x) = − ⎢ 0 − *1⎥ =
⎣ λ ⎦ λ

(10)
∞

⎡
⎤
P ⎢
1 2
1
1
−λ x ⎥
σ = ∫ ( x − ) λexp(−λ x)dx = ( x − ) − exp
− ∫ ( − exp λ ) 2( x − )dx

⎢
⎥
 λ
 λ
λ 

⎢⎣ u
⎥⎦
v
⎡
⎤
1 2
⎢
2
−λ x ⎥
σ = ( x − ) − exp
+ ∫ 2 x exp( −λ x) dx − ∫ exp(−λ x)dx
(11)
λ
⎢
⎥
λ 
⎢⎣  u
⎥⎦
v
product
rule

∞

2

(

2

0

dv

u

)

∞

− x

0

v

du

0

∞

(

2

)

∞

∞

0

0

0

∞

But ∫ 2 x exp(−λ x)dx =
0

2

2

2

∞

2⎛1⎞

2

and
xλ exp(−λ x)dx = E ( x) = ⎜ ⎟ =
λ∫
λ
λ⎝λ⎠ λ
2

0

2

exp(−λ x) dx = − exp(−λ x )
λ∫
λ
2

∞

1 2
⎡
⎤
2 ⎡ 2
−λ x ⎤
∴σ = ( x − ) − exp
+
+
−
λ
x
exp(
)
⎢⎣
⎥⎦ λ ⎢⎣ λ 2
⎥⎦
λ
2

(

)

∞

2

0

1
2
1
⎡
⎤ 2
∴σ 2 = ⎢0 − 2 (−1) ⎥ + 2 + (0 − 2 ) = 2
λ
λ
⎣ λ
⎦ λ

0

(12)

The exponential probability distribution function is used extensively used in the service,
consumer product, and travel industries in connection with customer queue time analysis,
reliability analysis, and traffic accident analysis. It is often used to determine the time until some
specific event occurs. For example, the projected service life of a device (like battery), the time
required for a fractional decay of a radio-active substance, the spending on a supermarket trip
may all be estimated using the exponential probability distribution function.

Example 3 Plutonium 239 decays continuously at a rate of 0.00284% per year. It follows that if
X is the time (in year) at which a randomly chosen plutonium atom will decay, the normalized
probability density function for the plutonium atom decaying in the time X will be given by
0.0000284
f ( X ) = a *exp[−
X ] , where a is a constant to be determined. (a) Show that
yr
0.0000284
a=
, and (b) determine the probability that a plutonium atom will decay between 100
yr
and 500 years from now.
Solution
(a) For a normalized probability density function,

⎛ −0.0000284 ⎞ ⎤
⎛ −0.0000284 ⎞
yr
X ⎟ dX =
aexp
1.0 = ∫ f ( X ) dX = ∫ a exp ⎜
X ⎟⎥
⎜
yr
−0.0000284
⎝
⎠
−∞
0
yr
∞

⎝

or 1.0 =

∞

∞

⎠⎦

0

yr
yr
0.0000284
a ( 0 − 1) =
a or a =
−0.0000284
0.0000284
yr

500 yr

(b) P(100 yr < X < 500 yr) =

500 yr

⎛ 0.0000284 ⎞
0.0000284
exp ⎜ −
X ⎟ dX
yr
yr
⎝
⎠
100 yr

∫ f ( X )dX = ∫

100 yr

P (100 yr < X < 500 yr ) = −exp

⎛ 0.0000284 ⎞
X⎟
⎜−
yr
⎝
⎠

500 yr

100 yr

= − exp ( −0.0000284*500 ) + exp ( −0.0000284*100 )

P (100 yr < X < 500 yr ) = −0.9859 + 0.9972 = 0.0113
Thus, there is a 1.13% chance a plutonium atom will decay between 100 and 500 years from
now.
Example 4 The amount of time t a postal clerk spends with a customer is known to be
exponentially distributed with a mean t value of 4.0 minutes. Determine (a) the exponential
probability density function, and (b) the probability that a clerk will spend four to five minutes
with a randomly selected customer.
Solution
(a) Recall that for the exponential probability density function of a continuous random variable t,
1
f (t ) = λ exp(−λt ) , the expectation value of t is given by Eqn (10) or E (t ) = . For a mean t
λ

1
. It follows that the
λ
4 min
−t
1
exponential probability density function is given by f (t ) =
exp(
)
4 min
4 min

value of 4.0 minutes, E (t ) =

1

= 4.0 min . Therefore, λ =

⎡
−t ⎤
1
−t
exp(
)dt = − exp(
)
4 min 4 min
⎢
4 min
4 min ⎥

(b) P(4 min < t < 5 min) = ∫

5 min

5 min

⎣

⎦

4 min

⎡
−5 min
−4 min ⎤
P(4 min < t < 5 min) = − ⎢ exp(
) − exp(
) ⎥ = −(e−1.25 − e −1 ) = 0.0814
4 min
4 min ⎦
⎣

Example 5
The service life t of a computer part is exponentially distributed with a mean value of
10 years. Determine (a) the probability that the computer part lasts more than 7 years,
and (b) the 80th percentile of the service life of the computer part (or the maximum
service life of 80% of the computer part).
Solution
For the exponential probability density function of service life t, f (t ) = λ exp(−λt ) , the
expectation value of t is given by Eqn (10) or E (t ) =

λ

. For a mean t value of 10

1
. It follows that the exponential
λ
10 yr
1
−t
probability density function is given by f (t ) =
exp(
).
10 yr
10 yr

years, E (t ) =

1

1

= 10 yr . Therefore, λ =

⎡
−0.1t ⎤
0.1
−0.1t
exp(
)dt = 1 − − exp(
(a) P(t > 7 yr) = 1 − P(t < 7 yr) = 1 − ∫
)⎥
⎢
yr
yr
yr
⎣
⎦

7 yr

7 yr

0

P (t > 7 yr) = 1 − P(t < 7 yr) = 1 + (e

−0.7

0

− 1) = 0.4966

(b) Let the 80th percentile of the service life of the computer part be denoted by t0.80.
The 80th percentile of the service life of the computer part is given by
P (t < t0.80 ) = 0.80 = ∫

t0.80

0

⎡
−t ⎤
1
−t
exp(
)dt = − exp(
)
⎢
10 yr
10 yr
10 yr ⎥
⎣

−t
−t0.80
exp( 0.80 ) = 1 − 0.80 = 0.20 or
= ln(0.20) = −1.6094
10 yr
10 yr

⎦

t0.80

⎡
⎤
−t
= − ⎢ exp( 0.80 ) − 1⎥
10 yr
⎣
⎦
0

∴ t0.80 = 16.094 yr

(C) Normal (or Gaussian) Probability Density Function
The normal (or Gaussian) probability density function is a two-parameter function given by

⎡ −1 ⎛ x − μ ⎞2 ⎤
1
f ( x) =
exp ⎢ ⎜
⎟ ⎥
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦

(13)

where μ is the mean value for the continuous random variable x and σ is the standard deviation
for x. As shown below, the function is represented by the well-known, symmetrical bell-shaped
curve centered at x = μ. The spread of the curve is determined by σ.

The normal distribution function has the following properties:

∫

∞

−∞

⎡ −1 ⎛ x − μ ⎞2 ⎤
1
exp ⎢ ⎜
⎟ ⎥dx = 1.0
−∞
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦

f ( x)dx = ∫

∞

∞

∞

−∞

−∞

E ( x) = ∫ xf ( x)dx = ∫ x

∞

∞

−∞

−∞

⎡ −1 ⎛ x − μ ⎞ 2 ⎤
1
exp ⎢ ⎜
⎟ ⎥dx = μ
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦

E[( x − μ ) 2 ] = ∫ ( x − μ ) 2 f ( x)dx = ∫ ( x − μ ) 2


⎡ −1 ⎛ x − μ ⎞ 2 ⎤
1
2
exp ⎢ ⎜
⎟ ⎥dx = σ
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦

(14)

(15)

(16)

The probability that x is less than a is equal to the area under the normal curve bounded
by a and minus infinity (as indicated by the shaded area in the figure below).






The probability that x is greater than a is equal to the area under the normal curve
bounded by a and plus infinity (as indicated by the non-shaded area in the figure above).
About 68% of the area under the curve falls within 1 standard deviation of the mean.
About 95% of the area under the curve falls within 2 standard deviations of the mean.
About 99.7% of the area under the curve falls within 3 standard deviations of the mean.

The normal distribution function (particularly its standard counterpart, the standard normal
distribution function--see the next section) is the most widely known and used of all probability
density functions for continuous variables. It, for example, describes the distribution patterns

found in many natural and engineering phenomena. The height, blood pressure, and
IQ of a population are normally distributed, as well as measurement errors, and length
of an object produced by a machine.
Example 6 The service life X (in days) of a light bulb manufactured by a company is a normal
variate with a mean μ of 300 days and a standard deviation σ of 50 days. Determine the
probability that a randomly-selected light bulb made by the company will have a service life of
(a) at most 365 days, (b) at least 365 days.
Solution
(a) P ( X < 365 days) = ∫

365

0

f ( X )dX = ∫

365

0

⎡ −1 ⎛ X − μ ⎞ 2 ⎤
1
exp ⎢ ⎜
⎟ ⎥dX
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦

Using the VBA numerical integration program (NumInteg.xls), P ( X < 365 days) = 0.9032
⎡ −1 ⎛ X − μ ⎞ 2 ⎤
⎡ −1 ⎛ X − μ ⎞ 2 ⎤
365
1
1
(b) P ( X > 365 days) = ∫
exp ⎢ ⎜
exp ⎢ ⎜
⎟ ⎥dX = 1 − ∫0
⎟ ⎥dX
365
σ 2π
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦
∞

P ( X > 365 days) = 1 − P ( X > 365 days) = 1 − 0.9032 = 0.0968

Example 7 The scores on an IQ test administered to a large group of students are normally
distributed with a mean μ of 100 and a standard deviation σ of 10. Determine the probability that
a student will have an IQ score between 90 and 110.
Solution
P(90 < X < 110) = ∫

110

90

⎡ −1 ⎛ X − μ ⎞ ⎤
1
f ( X )dX = ∫
exp ⎢ ⎜
⎟ ⎥dX
90
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦
110

2

Using the VBA numerical integration program (NumInteg.xls), P (90 < X < 110) = 0.6827

Example 8 The percentage of impurities in a product is a normally distributed variable X with a
mean μX = 1.8% and a standard deviation σX = 0.40%. For a randomly selected product,
determine (a) the 95% confidence interval for X, (b) the probability that X will fall outside the
(1.8 ± 0.1)% interval, (c) the probability that X will exceed 2.0%, and (d) the probability that X

will fall within the 1:00-2:00% range.
Solution
(a) The 95% confidence interval for X is defined by

X = μ X ± c0.95 such that P( μ X − c0.95 < X < μ X + c0.95 ) = 0.95 or

1

μ X + c0.95

∫μ

X − c0.95

σX

⎡ −1 ⎛ X − μ ⎞2 ⎤
⎡ −1 ⎛ X − 1.8% ⎞ 2 ⎤
1.8% + c0.95
1
X
exp ⎢ ⎜
exp ⎢ ⎜
⎟ ⎥dX = ∫1.8% − c0.95
⎟ ⎥dX = 0.95
2π
0.40% 2π
⎢⎣ 2 ⎝ σ X ⎠ ⎥⎦
⎢⎣ 2 ⎝ 0.40% ⎠ ⎥⎦

Using the VBA numerical integration program (NumInteg.xls) in conjunction with a trial and
error on c0.95, c0.95 = 0.7841. Therefore, the 95% confidence interval for X is given by

X = μ X ± c0.95 = (1.8 ± 0.7841) % or 1.016 % < X < 2.584 %
(b) The probability that X will fall outside the (1.8 ± 0.1)% interval is given by
P(X < 1.7 % or X > 1.9 %) = 1 – P(1.7 % < X < 1.9 %)
⎡ −1 ⎛ X − 1.8% ⎞2 ⎤
1
exp ⎢ ⎜
⎟ ⎥dX
1.7%
0.40% 2π
⎢⎣ 2 ⎝ 0.40 ⎠ ⎥⎦

P(1.7 % < X < 1.9 %) = ∫

using
NumInteg
program

1.9%

P
=

0.1974

Therefore, the probability that X will fall outside the (1.8 ± 0.1)% interval = 1 – 0.1974
= 0.8026
(c) The probability that X will exceed 2.0 % is given by
⎡ −1 ⎛ X − 1.8% ⎞ 2 ⎤
1
exp ⎢ ⎜
⎟ ⎥dX
0%
0.40% 2π
⎢⎣ 2 ⎝ 0.40% ⎠ ⎥⎦

P ( X > 2.0%) = 1 − P( X < 2.0%) = 1 − ∫

2%

Using the VBA numerical integration program (NumInteg.xls),
P ( X > 2 %) = 1 − 0.6914 = 0.3086
(d) The probability that X will fall within the 1:00-2:00% range is given by
⎡ −1 ⎛ X − 1.8% ⎞ 2 ⎤
1
P(1.0 % < X < 2.0 %) = ∫
exp ⎢ ⎜
⎟ ⎥dX
1%
0.40% 2π
⎢⎣ 2 ⎝ 0.40% ⎠ ⎥⎦
2%

using the
NumInteg
program

P
=

0.6687

(D) Standard Normal Probability Density Function or the Z-Distribution Function
If one does not have the benefit of a calculator program such as NumInteg.xls that can
⎡ −1 ⎛ X − μ ⎞ 2 ⎤
X
1
numerically evaluate the cumulative probability, P ( X ) = ∫
exp ⎢ ⎜
⎟ ⎥dX ,
0
σ 2π
⎢⎣ 2 ⎝ σ ⎠ ⎥⎦
one would have to refer to tables of cumulative normal probability in performing statistical
analyses. Because the normal distribution function has two parameters, μ and σ, there is
theoretically an infinite number of different possible combinations of μ and σ, and it is
impractical to list the tables of cumulative probability values for all the different combinations of
μ and σ in a handbook of mathematics or statistics. Fortunately, the problem is resolved by an
X − μX
ingenious definition of the Z -variable, Z ( X ) ≡
(17)
σX
With this definition or transform, all the different distribution curves collapse into a single
universal curve, all the different cumulative distribution tables consolidate into a single table and
⎡ − Z ( X )2 ⎤
1
Eqn (13) simplifies to f [ Z ( X )] =
exp ⎢
(18)
⎥
2
2π
⎣
⎦
Eqn (18) defines the standard normal probability density function or simply the Z-distribution
function. The Z-distribution function has the following properties:
∞
∞
⎡ −Z 2 ⎤
1
f
(
Z
)
dZ
exp
=
(19)
∫−∞
∫−∞ 2π ⎢⎣ 2 ⎥⎦dZ = 1.0
∞

E (Z ) ≡ μZ = ∫ Z
−∞

∞

E[( Z − μZ )2 ] ≡ σ Z 2 = ∫ Z 2
−∞

⎡ −Z 2 ⎤
1
exp ⎢
⎥dZ = 0
2π
⎣ 2 ⎦

⎡ −Z 2 ⎤
1
exp ⎢
⎥dZ = 1.0 or σ Z = ± 1.0
2π
⎣ 2 ⎦

(20)

(21)

The standard normal distribution is thus a special case of the normal distribution with a mean
of zero and a standard deviation of one. The function is symmetrical about the mean Z of zero.
It follows that the function corresponding to negative Z-values is a mirror image of the function
corresponding to positive Z-values, viz., f(−Z) = f(Z), and P(−Z) = P(Z).
Table 1 presents the Z-table which lists the cumulative probability as a function of the Z-score.
⎡ −Z 2 ⎤
1
The cumulative probability corresponds to the area under the f ( Z ) =
exp ⎢
⎥ vs Z -curve
2π
⎣ 2 ⎦
2
Table
P1
1.96
1 − Z2
between Z = 0 & Z = Z . Thus, P ( Z = 1.96) = ∫
e dZ = Area shaded blue = 0.4750.
0
2π

Table 1. Z-table listing the value of cumulative probability as a function of the Z-score.
Z(X )
⎡ −Z 2 ⎤
1
P[ Z ( X )] = ∫
exp ⎢
⎥dZ = Area under the f ( Z ) vs Z curve between Z = 0 and Z = Z .
0
2
2π
⎣
⎦

Z
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
1.2
1.3
1.4
1.5
1.6
1.7
1.8
1.9
2.0
2.1
2.2
2.3
2.4
2.5
2.6
2.7
2.8
2.9
3.0
3.1
3.2
3.3
3.4

0.00
0.0000
0.0398
0.0793
0.1179
0.1554
0.1915
0.2257
0.2580
0.2881
0.3159
0.3413
0.3643
0.3849
0.4032
0.4192
0.4332
0.4452
0.4554
0.4641
0.4713
0.4772
0.4821
0.4861
0.4893
0.4918
0.4938
0.4953
0.4965
0.4974
0.4981
0.4987
0.4990
0.4993
0.4995
0.4997

0.01
0.0040
0.0438
0.0832
0.1217
0.1591
0.1950
0.2291
0.2611
0.2910
0.3186
0.3438
0.3665
0.3869
0.4049
0.4207
0.4345
0.4463
0.4564
0.4649
0.4719
0.4778
0.4826
0.4864
0.4896
0.4920
0.4940
0.4955
0.4966
0.4975
0.4982
0.4987
0.4991
0.4993
0.4995
0.4997

0.02
0.0080
0.0478
0.0871
0.1255
0.1628
0.1985
0.2324
0.2642
0.2939
0.3212
0.3461
0.3686
0.3888
0.4066
0.4222
0.4357
0.4474
0.4573
0.4656
0.4726
0.4783
0.4830
0.4868
0.4898
0.4922
0.4941
0.4956
0.4967
0.4976
0.4982
0.4987
0.4991
0.4994
0.4995
0.4997

0.03
0.0120
0.0517
0.0910
0.1293
0.1664
0.2019
0.2357
0.2673
0.2967
0.3238
0.3485
0.3708
0.3907
0.4082
0.4236
0.4370
0.4484
0.4582
0.4664
0.4732
0.4788
0.4834
0.4871
0.4901
0.4925
0.4943
0.4957
0.4968
0.4977
0.4983
0.4988
0.4991
0.4994
0.4996
0.4997

0.04
0.0160
0.0557
0.0948
0.1331
0.1700
0.2054
0.2389
0.2704
0.2995
0.3264
0.3508
0.3729
0.3925
0.4099
0.4251
0.4382
0.4495
0.4591
0.4671
0.4738
0.4793
0.4838
0.4875
0.4904
0.4927
0.4945
0.4959
0.4969
0.4977
0.4984
0.4988
0.4992
0.4994
0.4996
0.4997

0.05
0.0199
0.0596
0.0987
0.1368
0.1736
0.2088
0.2422
0.2734
0.3023
0.3289
0.3531
0.3749
0.3944
0.4115
0.4265
0.4394
0.4505
0.4599
0.4678
0.4744
0.4798
0.4842
0.4878
0.4906
0.4929
0.4946
0.4960
0.4970
0.4978
0.4984
0.4989
0.4992
0.4994
0.4996
0.4997

0.06
0.0239
0.0636
0.1026
0.1406
0.1772
0.2123
0.2454
0.2764
0.3051
0.3315
0.3554
0.3770
0.3962
0.4131
0.4279
0.4406
0.4515
0.4608
0.4686
0.4750
0.4803
0.4846
0.4881
0.4909
0.4931
0.4948
0.4961
0.4971
0.4979
0.4985
0.4989
0.4992
0.4994
0.4996
0.4997

0.07
0.0279
0.0675
0.1064
0.1443
0.1808
0.2157
0.2486
0.2794
0.3078
0.3340
0.3577
0.3790
0.3980
0.4147
0.4292
0.4418
0.4525
0.4616
0.4693
0.4756
0.4808
0.4850
0.4884
0.4911
0.4932
0.4949
0.4962
0.4972
0.4979
0.4985
0.4989
0.4992
0.4995
0.4996
0.4997

0.08
0.0319
0.0714
0.1103
0.1480
0.1844
0.2190
0.2517
0.2823
0.3106
0.3365
0.3599
0.3810
0.3997
0.4162
0.4306
0.4429
0.4535
0.4625
0.4699
0.4761
0.4812
0.4854
0.4887
0.4913
0.4934
0.4951
0.4963
0.4973
0.4980
0.4986
0.4990
0.4993
0.4995
0.4996
0.4997

0.09
0.0359
0.0753
0.1141
0.1517
0.1879
0.2224
0.2549
0.2852
0.3133
0.3389
0.3621
0.3830
0.4015
0.4177
0.4319
0.4441
0.4545
0.4633
0.4706
0.4767
0.4817
0.4857
0.4890
0.4916
0.4936
0.4952
0.4964
0.4974
0.4981
0.4986
0.4990
0.4993
0.4995
0.4997
0.4998

To make use of the Z-table in a statistical analysis of a normally-distributed variable X, it is
necessary to relate X to Z by means of Eqn (17) and then work in terms of Z. The approach is
illustrated by re-analyzing Examples 6, 7, and 8 using the Z-statistics approach.
Example 6 The service life X (in days) of a light bulb manufactured by a company is a normal
variate with a mean μ of 300 days and a standard deviation σ of 50 days. Determine the
probability that a randomly-selected light bulb made by the company will have a service life of
(a) at most 365 days, (b) at least 365 days.
Alternate Solution
(a) For X = 365 days, Z =

X − μX

σX

=

365 − 300
= 1.3
50
0.50 by symmetry property

Table 1
 
 
P ( X < 365 days) = P (−∞ < Z < 1.3) = P (−∞ < Z < 0) + P (0 < Z < 1.3) = 0.50 + 0.4032 = 0.9032

P ( Z =1.30), Table 1
 


(b) P ( X > 365 days) = P (1.30 < Z < ∞ ) = P (0 < Z < ∞ ) − P (0 < Z < 1.30) = 0.50 − 0.4032 = 0.0968
0.50 by symmetry property

Example 7 The scores on an IQ test administered to a large group of students are normally
distributed with a mean μ of 100 and a standard deviation σ of 10. Determine the probability that
a student will have an IQ score between 90 and 110.
Alternate Solution
90 − 100
110 − 100
= −1 and Z =
=1
10
10
P ( Z =−1) = P ( Z 1), symmetry
P ( Z =1)
Table 1
 
 

P (90 < X < 110) = P ( −1 < Z < 1) = P (−1 < Z < 0) + P (0 < Z < 1) = 2 P ( Z = 1) = 2*0.3413 = 0.6826

For X = 90 and X = 110, Z =

Example 8 The percentage of impurities in a product is a normally distributed variable X with a
mean μX = 1.8% and a standard deviation σX = 0.40%. For a randomly selected product,
determine (a) the 95% confidence interval for X, (b) the probability that X will fall outside the
(1.8 ± 0.1)% interval, (c) the probability that X will exceed 2.0%, and (d) the probability that X

will fall within the 1:00-2:00% range.
Alternate Solution
(a) The 95% confidence interval for X is defined by

X = μ X ± c0.95 such that P( μ X − c0.95 < X < μ X + c0.95 ) = 0.95 or
P ( Z =−Δz ) = P ( Z =Δz ), symmetry

Z = μZ ± Δz = 0 ± Δz such that 0.95 = P(−Δz < Z < Δz ) =



P (−Δz < Z < 0)

P ( Z =Δz )

 
+ P(0 < Z < Δz )

2 P ( Z = Δz ) = 0.95 or P ( Z = Δz ) = 0.475

From Table 1, P ( Z ) = 0.475 corresponds to Z = 1.960 or more precisely, Z = ± 1.960
Z = ± 1.960, the corresponding X values are given by X = μ X + Zσ X = 1.8% ± 1.96*0.4%
Therefore, the 95% confidence interval for X is given by
X = 1.8 % ± 0.784 % or 1.016 % < X < 2.584 %
(b) For X = (1.8 ± 0.1)%, Z =

X − μX

σX

=

± 0.1
= ± 0.25
0.4

The probability that X will fall outside the (1.8 ± 0.1)% interval is given by
P(X < 1.7 % or X > 1.9 %) = P(Z< −0.25 or Z > 0.25) = P(Z< −0.25) + P(Z > 0.25)
symmetry property
P
P( X < 1.7 % or X > 1.9 % )
=
2 P( Z > 0.25)
Table
P1
P( X < 1.7 % or X > 1.9 % ) = 2[0.50 − P(0 < Z < 0.25)] = 2(0.50 − 0.0987) = 0.8026

(c) For X = 2.0%, Z =

X − μX

σX

=

2 − 1.8 1
=
0.40
2

The probability that X will exceed 2.0 % is given by
P ( Z = 0.5)
  Table 1


1
1 P
P( X > 2.0%) = P ( Z > ) = P (0 < Z < ∞) − P (0 < Z < ) = 0.50 − 0.1915 = 0.3085
2
2
0.50

X − μX

1 − 1.8
2.0 − 1.8 1
= −2 and
=
σX
0.40
0.40
2
The probability that X will fall within the 1:00-2:00% range is given by
P (1.0 % < X < 2.0 %) = P(−2.0 < Z < 0.50) = P(−2.0 < Z < 0) + P(0 < Z < 0.50)

(d) For X = 1.0 % and 2.0 %, Z =

symmetry
property

=

P
= P(0 < Z < 2.0) + P(0 < Z < 0.50) = P( Z = 2.0) + P( Z = 0.50)
Table
P1
P (1.0 % < X < 2.0 %) = 0.4772 + 0.1915 = 0.6687

P (1.0 % < X < 2.0 %)

Central Limit Theorem

The Central Limit Theorem is used extensively in statistical analyses. It may be explained as
follows. Given a distribution of a variable X–not necessarily a normal distribution–that has a
mean μX and a variance σX², a second distribution, which is known as the distribution of the
sample mean, may be created by repeatedly taking n samples each time and determining the
sample mean X each time. The Central Limit Theorem states that the distribution of the sample
mean X has a mean μ X , a variance σ X ² , and a standard deviation σ X that are related to μX ,
σX², and σX of the original distribution as follows
μX = μX
(22)

σX ² =
σX =

σX2
n

σX

n

(23)
(24)

The figure below summarizes the relationship given in Eqn (22)−24. Notice that the distribution
for the sample mean is narrower than the population distribution as a consequence of σ X < σ X .

Moreover, the distribution of the sample mean X approaches a normal distribution as the sample
size n increases, even if the original distribution of X is other than a normal distribution!
The Central Limit Theorem may be illustrated by the following computer simulation example
based on a random sampling of a large population of n distinct groups of balls present in equal
proportions, i.e., balls in each group have a 1/5 or 20% chances of being picked. Balls in the five
distinct groups are labeled 1, 2, 3, 4, and 5, respectively. Let X denote the number label of a ball
being picked.
For the uniform distribution of X,

it may be shown that the mean μX and variance σX2 of X are given, respectively, by
5

1
5

μ X = ∑ Pi X i = (1 + 2 + 3 + 4 + 5) = 3.0
i =1
5

1
5

σ X 2 = ∑ Pi ( X i − μ X ) 2 = (4 + 1 + 0 + 1 + 4) = 2.0
i =1

(25)
(26)

Suppose n balls are randomly picked by the computer program for N successive times, each time
the average of the n number labels is computed. The sample mean X and its variance s X 2 would
be given, respectively, by

1 5
∑ Xi
n i =1
1 n
sX 2 =
( X i − X )2
∑
n − 1 i =1
X=

(27)
(28)

For sample size n = 5 and N = 6 successive averaging trials, the results shown in Figure 1 may be
obtained. The red bar denotes the drawn label X and the blue bar denotes the sample mean X in
each trial. The distribution of the sample mean X in the N = 6 trials is given in Figure 2.

The sample means of the six samples are not the same (see Figure 1) and Figure 2 shows that the
distribution of the sample means clusters in a narrow range that suggests a bell-shaped
distribution characteristic of a normal distribution. As the number of averaging trials N is
increased from 6, the distribution of sample mean X becomes "smoother" and more closely
resembles a normal distribution. For example, when the sample size is increased from 6 to 25,
the distribution of sample mean X shown in Table 1 is obtained.
Table 1. Frequency distribution of sample mean X for N = 25 averaging trials.
Sample Mean X
Frequency

1.40
1

2.60
3

2.80
6

3.00
1

3.20
4

3.40
4

3.60
1

3.80
3

4.00
1

4.20
1

As shown in Figures 3 and 3’, the distribution of the sample mean X becomes progressively
more normal-like as the number N of samples (or averaging trials) is increased. In the limit of N
→ ∞ (or ~1000 for most practical purposes), the distribution becomes normal. Note that as N →
∞, the mean value μ X and standard deviation σ X of X are as predicted by Eqn (22) and (24).

The foregoing computer simulation example illustrates an important result of general validity,
namely that, the distribution of the sample mean X drawn from a population with any kind of
distribution can be approximated by the normal distribution when the sample size n is
sufficiently large (n ≥ 30) or when the number N of averaging trials is sufficiently large (N ~
100–1000). The larger the sample size n in each of the averaging trials or the larger the number
of the averaging trials (N), the better is the approximation of the sample mean distribution to the
normal distribution. Moreover, the mean value and standard deviation of the sample mean X are
given by Eqn (22) and (24), respectively, where n is the sample size in each averaging trial.
Example 9 A grain company markets rice in 25-lb sacks. Data collected over many years
indicate that the weight W of rice shipped in each sack is a normally distributed variable with a
mean value μW = 25.0 lb and a standard deviation σW = 0.25 lb. Determine the probability that a
sack will contain (a) less than 25.25 lb of rice, and (b) between 24.50 and 25.25 lb of rice.

If a delivery truck ships 9 sacks of rice, what is the probability that the average of the shipment
contains less than 25.25 lb per sack?
Solution

Use the Z-distribution function and the definition of Z to relate Z to W, Z =

W − μW

σW

25.25 − 25.0
= 1.0
0.25
P(W < 25.25 lb) = P(Z < 1.0) = P(−∞ < Z < 0) + P(0 < Z < 1.0)

(a) For W = 25.25 lb, Z =

But symmetry property gives P(−∞ < Z < 0) = P(0 < Z < ∞) = ½ = 0.50 and
P(0 < Z < 1.0) = A(Z = 1.0) = 0.3413.
Therefore, P(W < 25.25 lb) = P(−∞ < Z < 0) + P(0 < Z < 1.0)
= 0.50 + 0.3413
= 0.8413

.

(b) For W = 25.25 lb, Z = 1.0 from part a above.
24.50 − 25.0 − 0.50
For W = 24.50 lb, Z =
=
= − 2 .0
0.25
0.25
P(24.50 lb < W < 25.25 lb) = P(−2.0 < Z < 1.0)
But P(−2.0 < Z < 1.0) = P(−2.0 < Z < 0) + P(0 < Z < 1.0)
= P(0 < Z < 2.0) + P(0 < Z < 1.0)
= A(Z = 2.0) + A(Z = 1.0)
= 0.4772 + 0.3413
= 0.8185
Therefore, P(24.50 lb < W < 25.25 lb) = 0.8185
(c) According to the Central Limit Theorem, the average of the normally distributed W of 9
sacks, W , is also a normally distributed variable with a mean μW that is the same as W
(μW) but with a standard σ W that is different from that (σW) of W. Specifically,
Eqn (20) => μW = μW = 25.0 lb
σ
0.25 lb
= 0.0833 lb
Eqn (22) => σ W = W =
n
9
W − μW 25.25 − 25.0
0.25
For W = 25.25lb, Z =
=
=
= 3.0
σW
0.0.0833
0.0833
Therefore, P( W < 25.25 lb) = P(Z < 3.0) = P(−∞ < Z < 0) + P(0 < Z < 3.0)
P( W < 25.25 lb) = 0.50 + A(Z=3.0)
= 0.50 + 0.4987
= 0.9987
Example 10 Based on data collected from the National Health Survey, the weight for adult
males in the United States follows a normal distribution with a mean of 173 lb and a standard
deviation of 30 lb. (a) If one U.S. adult male is randomly selected, what is the probability that his
weight will be greater than 180 lb? (b) If 36 different U.S. adult males are randomly selected,
what is the probability that their sample mean weight will be greater than 180 lb?
Solution

(a) Using the Z-statistics approach, relate Z to W, Z =

W − μW

σW

.

180 − 173
= 0.233
30
P(W > 180 lb) = P(Z > 0.233) = 0.50 – P(Z < 0.233) = 0.50 – A(Z = 0.233)

For W = 180 lb, Z =

From Z-table, A(Z = 0.233) = 0.0923.
Therefore, P(W > 180 lb) = 0.50 – 0.0923 = 0.4077

(b) Using the Central Limit theorem, Eqn (20) => μ X = μ X = 173 lb
σ
30 lb
= 5 lb
Eqn (23) => σ X = X =
n
36
W − μW 180 − 173
For W = 180 lb, Z =
=
= 1.40
5
σW
P( W > 180 lb) = P(Z > 1.40) = 0.50 – P(Z < 1.40) = 0.50 – A(Z = 1.40)
From Z-table, A(Z = 1.40) = 0.4192.
Therefore, P( W > 180 lb) = 0.50 – 0.4192 = 0.0808
Example 11 Measurements on 120 random trucks on a highway give a mean speed of 62

mph. Given that the truck population on the highway has a mean of 60 mph and a
standard deviation of 12.5 mph, find the probability that the average speed of 120
trucks will exceed 62 mph.
Solution
Using the Z-statistics approach, Z =

u − μu

σu

=

u − μu
62 − 60
2
=
=
= 1.753
σ u / n 12.5 / 120 1.141

P (u > 62 mph) = P ( Z > 1.753) = P (0 < Z < ∞ ) − P ( Z < 1.753) = 0.50 − A( Z = 1.753)

From the Z-table, A(Z = 1.753) = 0.4602. Therefore, P ( u > 6 2 m p h ) = 0 .5 0 − 0 .4 6 0 2 = 0 .0 3 8 2
Example 12 A sardine packaging company claims that its cans of sardine have a normal weight
distribution with a mean of 6.05 oz and a standard deviation of 0.18 oz. An independent check
by a consumer group found that a random case of 36 cans of sardine gives an average weight of
5.97 oz. What is the probability of the observation of the test result if the company’s claim is
valid, i.e., determine P(X ≤ 5.97 oz). What conclusion may be drawn by the consumer group?
Solution

According to the Central Limit Theorem, μ X = μ X = 6.05 oz and σ X =
Use the Z-statistics approach. Z =

X − μX

σX

=

σX
n

=

0.18 oz
= 0.03 oz
36

5.97 − 6.05
= −2.667
0.03

P
=

symmetry

P ( X ≤ 5.97 oz) = P ( Z ≤ −2.667)

P ( Z ≥ 2.667) = P (0 < Z < ∞) − P ( Z ≤ 2.667)
P
P ( X ≤ 5.97 oz) = 0.50 − A( Z = 2.667) = 0.5000 − 0.4962 = 0.0038
Table 1

Since the calculated probability for the observation of the result is 0.38%, which is very low, the
consumer group may be justified to conclude that the company’s claim is false.

(E) Student’s t-Probability Density Function

In order to use the normal or Z- distribution function in a statistical analysis, it is necessary that
the standard deviation σX of the population of the random continuous X-variable be known or the
sample size n upon which the sample mean X is based is sufficiently large (n > 30). If neither of
these two conditions is met, the use of normal or Z- statistic is not justified. One must instead
use the Student’s t-distribution function or, simply, the t-distribution, which has the probability
⎛ν +1 ⎞
−1
Γ⎜
⎟ ⎛ t 2 ⎞ 2 (ν +1)
2
⎠ 1+
density function defined by f (t ) = ⎝
,
(29)
⎜
⎟
ν
⎛ ⎞⎝ ν ⎠
νπ Γ ⎜ ⎟
⎝2⎠
where ν is the number of degrees of freedom and Γ is the Gamma function.

For ν even,

⎛ν +1 ⎞
Γ⎜
⎟
⎝ 2 ⎠ = (ν − 1)(ν − 3)...5*3
⎛ν ⎞
νπ Γ ⎜ ⎟ 2 ν (ν − 2)(ν − 4)...4* 2
⎝2⎠

(30)

For ν odd,

⎛ν + 1 ⎞
Γ⎜
⎟
⎝ 2 ⎠ = (ν − 1)(ν − 3)...4* 2
⎛ν ⎞
νπ Γ ⎜ ⎟ 2 ν (ν − 2)(ν − 4)...5*3
⎝2⎠

(31)

Figures 4 and 4’ present representative plots of the probability density function f(t) and the

t

cumulative probability P (t ) = ∫ f (t )dt of t−distribution with the degree of freedom ν as a
−∞

parameter. The degree of freedom ν is given by ν = N data pts − N indept variables

(32)

where N data pts ≡ ( # data points/measurements ) and N indept variables ≡ (# independent variables) .

The overall shape of the probability density function of the t-distribution resembles the bell
shape of a normally distributed variable with mean 0 and variance 1, except that the shape of the
t-distribution is flatter than that of the normal distribution, and the t-distribution has greater area
under the tails. Figure 5 shows a comparison of the t-distribution with Z-distribution. The Zscores defining a 95% confidence interval are ±1.960 and the tail areas above Z = 1.960 and
below Z = –1.960 each has an area of 0.025. The confidence interval (or area under the curve)
bounded by the t = ±1.960 scores is 92.76% (< 95%) for ν = 3 and the tail areas above t = 1.960
and below t = –1.960 each has an area of 0.0362 (> 0.025). The fact that the t-distribution has
higher tail areas than the Z-distribution means that critical t-values must be set higher than the
corresponding critical Z-values in statistical analyses. As ν increases above 3, the t-distribution
approaches the Z-distribution, and the difference in the tail areas corresponding to the same
critical t- and Z-scores narrows progressively. Thus, for ν = 30, the critical t-scores of ±1.960
give tail areas of 0.0297 (closer to 0.0250). For most practical purposes, the t-distribution may
be substituted by the Z-distribution for ν ≥ 30.
The t-distribution has the following properties:
• the mean of the distribution (μt) is equal to 0 and the distribution is centered at t = 0 and
symmetric about t = 0, i.e., f(–t) = f(t)
• the variance is equal to v / ( v - 2 ), where v is the degrees of freedom and v > 2
• the variance is always greater than 1, although it is close to 1 when there are many
degrees of freedom
• the total area under the f(t)-vs-t curve is 1.0 and each half of the curve above and below
t = 0 has an area of ½.
The symbol tα is used to represent the t-value for which the area to the right is α.
Table 2 presents the t-distribution table with the values of tν,α as a function of the degree of
freedom ν and one-sided or two-sided cumulative probability. The symbol tν,α is used to denote
the t-value for which the area (under f(t)-vs-t curve) to the right is α for a specified degree of
freedom ν. Thus, tν=10,α=0.025 = 2.228 means that the tail area to the right of t = 2.228 is 0.025 for
ν = 10. A t-distribution calculator is available on the web site, http://stattrek.com/Tables/T.aspx,
which allows a determination of the value of the third parameter if any two of the parameters, ν,
cumulative probability P ≡ (1 – α), and t-value are specified. Thus, if ν and (1 – α) are specified
as ν = 10 and P = (1 – α) = 0.975, the calculator program will return a value of 2.228 for the
t-value. Likewise, if ν and t-value are specified as ν = 10 and t-value = 2.228, the program will
determine P = (1 – α) = 0.975 or α = 0.025.
Example 13 A survey of 31 students reveals that the average one-way travel to a college is 19.4
min with a standard deviation of 9.6 min. Determine the 95% confidence for the average oneway travel time to the college.
Solution
The 95% confidence interval for the average one-way travel time to the college centers about the

Table 2. t-Table: Values of tν,α as a function of the degree of freedom ν and one-sided or twosided cumulative probability, e.g., tν=10,α=0.025 = 2.228.
α
0.30 0.25 0.20 0.15 0.10 0.05 0.025 0.010 0.005 0.0025 0.001 0.0005
One Sided 70% 75% 80% 85% 90% 95% 97.5% 99% 99.5% 99.75% 99.9% 99.95%
Two Sided 35% 50% 60% 70% 80% 90% 95% 98% 99% 99.5% 99.8% 99.9%
0.727 1.000 1.376 1.963 3.078 6.314 12.71 31.82 63.66 127.3 318.3 636.6
1
0.617 0.816 1.061 1.386 1.886 2.920 4.303 6.965 9.925 14.09 22.33 31.60
2
0.584 0.765 0.978 1.250 1.638 2.353 3.182 4.541 5.841 7.453 10.21 12.92
3
0.569 0.741 0.941 1.190 1.533 2.132 2.776 3.747 4.604 5.598 7.173 8.610
4
0.559 0.727 0.920 1.156 1.476 2.015 2.571 3.365 4.032 4.773 5.893 6.869
5
0.553 0.718 0.906 1.134 1.440 1.943 2.447 3.143 3.707 4.317 5.208 5.959
6
0.549 0.711 0.896 1.119 1.415 1.895 2.365 2.998 3.499 4.029 4.785 5.408
7
0.546 0.706 0.889 1.108 1.397 1.860 2.306 2.896 3.355 3.833 4.501 5.041
8
0.543 0.703 0.883 1.100 1.383 1.833 2.262 2.821 3.250 3.690 4.297 4.781
9
0.542 0.700 0.879 1.093 1.372 1.812 2.228 2.764 3.169 3.581 4.144 4.587
10
0.540 0.697 0.876 1.088 1.363 1.796 2.201 2.718 3.106 3.497 4.025 4.437
11
0.539 0.695 0.873 1.083 1.356 1.782 2.179 2.681 3.055 3.428 3.930 4.318
12
0.538 0.694 0.870 1.079 1.350 1.771 2.160 2.650 3.012 3.372 3.852 4.221
13
0.537 0.692 0.868 1.076 1.345 1.761 2.145 2.624 2.977 3.326 3.787 4.140
14
0.536 0.691 0.866 1.074 1.341 1.753 2.131 2.602 2.947 3.286 3.733 4.073
15
0.535 0.690 0.865 1.071 1.337 1.746 2.120 2.583 2.921 3.252 3.686 4.015
16
0.534 0.689 0.863 1.069 1.333 1.740 2.110 2.567 2.898 3.222 3.646 3.965
17
0.534 0.688 0.862 1.067 1.330 1.734 2.101 2.552 2.878 3.197 3.610 3.922
18
0.533 0.688 0.861 1.066 1.328 1.729 2.093 2.539 2.861 3.174 3.579 3.883
19
0.533 0.687 0.860 1.064 1.325 1.725 2.086 2.528 2.845 3.153 3.552 3.850
20
0.532 0.686 0.859 1.063 1.323 1.721 2.080 2.518 2.831 3.135 3.527 3.819
21
0.532 0.686 0.858 1.061 1.321 1.717 2.074 2.508 2.819 3.119 3.505 3.792
22
0.532 0.685 0.858 1.060 1.319 1.714 2.069 2.500 2.807 3.104 3.485 3.767
23
0.531 0.685 0.857 1.059 1.318 1.711 2.064 2.492 2.797 3.091 3.467 3.745
24
0.531 0.684 0.856 1.058 1.316 1.708 2.060 2.485 2.787 3.078 3.450 3.725
25
0.531 0.684 0.856 1.058 1.315 1.706 2.056 2.479 2.779 3.067 3.435 3.707
26
0.531 0.684 0.855 1.057 1.314 1.703 2.052 2.473 2.771 3.057 3.421 3.690
27
0.530 0.683 0.855 1.056 1.313 1.701 2.048 2.467 2.763 3.047 3.408 3.674
28
0.530 0.683 0.854 1.055 1.311 1.699 2.045 2.462 2.756 3.038 3.396 3.659
29
0.530 0.683 0.854 1.055 1.310 1.697 2.042 2.457 2.750 3.030 3.385 3.646
30
0.529 0.681 0.851 1.050 1.303 1.684 2.021 2.423 2.704 2.971 3.307 3.551
40
0.528 0.679 0.849 1.047 1.299 1.676 2.009 2.403 2.678 2.937 3.261 3.496
50
0.527 0.679 0.848 1.045 1.296 1.671 2.000 2.390 2.660 2.915 3.232 3.460
60
0.526 0.678 0.846 1.043 1.292 1.664 1.990 2.374 2.639 2.887 3.195 3.416
80
0.526 0.677 0.845 1.042 1.290 1.660 1.984 2.364 2.626 2.871 3.174 3.390
100
0.526 0.677 0.845 1.041 1.289 1.658 1.980 2.358 2.617 2.860 3.160 3.373
120
0.524 0.674 0.842 1.036 1.282 1.645 1.960 2.326 2.576 2.807 3.090 3.291

P
=

95% confidence interval

1 − 0.95
= 0.025
2
X − <X > X − <X > X − 19.4 min X − 19.4 min
tν ,α =
=
=
=
sX
1.724 min
s X / 31
9.6 min/ 31
ν = 31 − 1 = 30,
α = 0.025
From the t-table (Table 2), tν =30,α =0.025 = ±2.042
mean with two tails. Therefore, α

∴ X = <X > ± tν ,α sX = (19.4 ± 2.042*1.724 ) min = (19.4 ± 3.517 ) min
Therefore, the 95% confidence interval of the mean one-way travel time to the college is given
by 15.883 min < X < 22.917 min
Example 14 The saturated vapor pressure Psat of a newly synthesized compound has been measured
five times at 40oC with the following results: 125.0, 124.2, 124.7, 126.0, and 125.3 mm Hg.
Determine (a) the sample mean, <Psat>, and its standard deviation, sP, and (b) the 95% and 99%
confidence intervals for Psat.
Solution
(a) <Psat> = (125.0 + 124.2 + 124.7 + 126.0 + 125.3)/5 mm Hg = 125.04 mm Hg
n =5
1
Variance sP2 = ∑
( P sat i − <P sat >) 2
i =1 n − 1
= ¼[(125.0 − 125.04)2 + (124.2 − 125.04)2 + (124.7 − 125.04)2
+ (126.0 − 125.04)2 + (125.3 − 125.04)2] (mm Hg)2
= 0.4530 (mm Hg)2

Standard deviation sP = sP 2 = 0.673 mm Hg
Central Limit
P Theorem P sat − <P sat > P sat − 125.04 mm Hg P sat − 125.04 mm Hg
P sat − <P sat >
=
=
=
(b) tν ,α =
0.301 mm Hg
sP sat
sP sat / 5
0.673 / 5 mm Hg

(

)

For ν = 5 − 1 = 4 and a 95% confidence interval (with 2 tails), α = (1 − 0.95)/2 = 0.025.
From the t-table, tν = 4,α =0.025 = ±2.776
Therefore, the 95% confidence interval for the mean P sat is given by
P sat = <P sat > + tν ,α sPsat = (125.04 ± 2.776*0.301) mm Hg = (125.04 ± 0.836 ) mm Hg
or

P Lsat= 124.20 mm Hg < P sat < PUsat = 125.88 mm Hg

Likewise, for the 99% confidence interval, α = ½(1 − 0.99) = 0.005
From the t-table, tν = 4,α =0.025 = ±4.604
Therefore, the 99% confidence interval for the mean P sat is given by
P sat = <P sat > + tν ,α sPsat = (125.04 ± 4.604*0.301) mm Hg = (125.04 ± 1.386 ) mm Hg
or

P Lsat= 123.65 mm Hg < P sat < PUsat = 126.43 mm Hg

Example 15 A newly manufactured product contains an impurity X whose true mean (μX) and true
standard deviation (σX) in concentration level are unknown. Suppose an analysis of five random

samples yields a sample mean (<X>) of 1.8% and a sample standard deviation (sX) of 0.40% in the
concentration level. Assuming that the impurity concentration level conforms to the t-distribution,
determine the following:
(a) the 95% confidence interval for X ,
(b) the probability that X will fall outside the (1.8 ± 0.1)% range,
(c) the probability that X will exceed 2.0%, and
(d) the probability that X will fall within the 1:00-2:00% range.
Solution
Use the t-distribution function and the definition of t to relate t to X ,
X − <X > X − <X > X − 1.8% X − 1.8%
tν ,α =
=
=
=
.
sX
0.179%
sX / n
0.40%/ 5
(a) For a 95% confidence interval, the tail area α = (1 − 0.95)/2 = 0.025. For the degrees
of freedom ν = 5 − 1 = 4, and with α = 0.025, the t-table gives tν=4,α=0.025 = ±2.776.
X − 1.8%
or the 95% confidence interval for X is given by
Therefore, ±2.776 = tν =4,α =0.025 =
0.179%
X = 1.8% ± 2.776*0.179% = (1.8 ± 0.497)% or X L = 1.303% < X < X U = 2.296%.

(b) The t- interval corresponding to the X = (1.8 ± 0.1)% interval is given by
X − <X > (1.8 ± 0.1)% − 1.8%
tν ,α =
=
= ±0.559
0.179%
sX / n
Using the t-distribution calculator program on http://stattrek.com/Tables/T.aspx, for ν = 4 and
t = ± 0.559, α = 1 – 0.6970 = 0.3030.
Thus, P(1.7% < X < 1.9%) = P(−0.559 < t < 0.559)
= 2*(0.500 − 0.3030)
= 2*0.1970
= 0.3940
Therefore, P( X is outside the 1.8 ± 0.1 % range) = P( X < 1.7% or X > 1.9%)
= 1 − Prob(1.7% < X < 1.9%)
= 1 − 0.3940
= 0.6060
X − <X > 2.0% − 1.8%
(c) For X > 2.0% or t >
=
= 1.118 ,
0.179%
sX / n
∞

P( X >2%) = P(tν=4>1.118) = ∫ f (t )dt = α
1.118

Using the t-distribution calculator program on http://stattrek.com/Tables/T.aspx, for ν = 4,
and t = 1.118, α = 1 – 0.8369 = 0.1631 Therefore, P( X >2%) = 0.1631.
(d) For X = 1.0%, t =

X − <X > 1.0% − 1.8%
=
= −4.472
0.179%
sX / n

For X = 2.0%, tν=4 = 1.118 from part c.

P(1.0% < X < 2.0%) = P(−4.472 < tν=4 < 1.118)
However, P(−4.472 < tν=4 < 1.118) = P(−4.472 < tν=4 < 0) + P(0 < tν=4 < 1.118)
symmetry
P
= P ( 0 < tν = 4 < 4.472 ) + P ( 0 < tν = 4 < 1.118 )
=∫

4.472

0

f (t ,ν = 4)dt + ∫

1.118

0

f (t ,ν = 4)dt

P
= (0.9945 − 0.5000) + (0.8369 − 0.5000)
= 0.8314
Alternatively, P ( −4.472 < tν = 4 < 1.118 ) = 1 − (αν = 4,t =−4.472 + αν = 4,t =1.118 )
t-calculator

symmetry

t − calculator
P
P
αν = 4,t =−4.472 = αν =4,t =4.472 = 1 − 0.9945 = 0.0055
t − calculator
P
αν = 4,t =1.118 = 1 − 0.8369 = 0.1631

∴ P ( −4.472 < tν =4< 1.118) = 1 − ( 0.0055 + 0.1631) = 0.8314 same as above.
Alternatively, using Table 2 and linear interpolation,
P ( −4.472 < tν = 4 < 1.118 ) = 1 − (αν = 4,t =−4.472 + αν = 4,t =1.118 )
symmetry

linear interpolation using Table 2
P
P
4.472 − 3.747
=
0.010 +
(0.005 − 0.010)
αν = 4,t =−4.472 = αν = 4,t = 4.472
4.604 − 3.747
αν = 4,t =−4.472 = 0.00577
linear interpolation using Table 2

P
=

1.118 − 0.941
(0.15 − 0.20) = 0.1645
1.190 − 0.941
P ( −4.472 < tν =4< 1.118 ) = 1 − ( 0.00577 + 0.1645 ) = 0.8298

αν = 4,t =1.118

0.20 +

The result based on linear interpolation of Table 2 is slightly different from that using the
t-calculator program.
Example 16 The concentration of sulfur dioxide in the air around a coal-fired power plant has been
measured six times with the following results: 320, 295, 306, 284, 315, 290 ppm. Determine (a) the
sample mean and sample standard deviation, and (b) the 95% confidence interval for the average
sulfur dioxide concentration. (c) Repeat part (b) if, instead of six measurements, only three
measurements were made with the same sample mean and sample standard deviation as in part (a).
(d) What conclusion may be made based on the result in part (c)?
Solution
(a) Sample mean SO2 concentration is given by
1 n
1
< CSO2 >= ∑ CSO2 = ( 320 + 295 + 306 + 284 + 315 + 290 ) ppm = 301.7 ppm
n i =1
6
i
Sample variance of C SO2 is given by

(

)

sCSO

2

2

1 n
=
∑ CSO2 − < CSO2 > i
n − 1 i =1

(

)

2

1 ⎡( 320 − 301.7 ) + ( 295 − 301.7 ) + ( 306 − 301.7 ) ⎤
⎥ ppm 2
sCSO = ⎢
2
2
2
2
5 ⎢ + ( 284 − 301.7 ) + ( 315 − 301.7 ) + ( 290 − 301.7 ) ⎥
⎣
⎦
2
2
sCSO = 205.1 ppm
2
2
= SQRT( sCSO ) = ± 14.32 ppm
Sample standard deviation of C is given by s
2

2

2

2

2

CSO2

SO2

(b) Use t-statistics to determine the 95% confidence interval for the average sulfur dioxide
concentration CSO2 .
For the six measurements, degrees of freedom ν = 6 – 1 = 5.
For a 95% confidence interval, α = (1 – 0.95)/2 = 0.025.
From the t-table, for ν = 5 and α = 0.025, tν =5,α =0.025 = ± 2.571

tν =5,α =0.025 = 2.571 =

CSO2 − < CSO2 >
sCSO

=

CSO2 − < CSO2 >

2

sCSO / n

=

2

CSO2 − 301.7 ppm
14.32 ppm/ 6

Therefore, the 95% confidence interval for CSO2 is given by
14.32 ⎞
⎛
CSO2 = < CSO2 > ± 2.571* sCSO = ⎜ 301.7 ± 2.571*
⎟ ppm = ( 301.7 ± 15.03) ppm
2
6 ⎠
⎝
or 286.7 ppm < CSO2 < 316.7 ppm
(c) If n = 3 instead of 6 and if the sample mean and sample standard deviation remain the same as
in part (a), then tν = 2,α =0.025 =

CSO 2 − < CSO2 >
sCSO

2

=

CSO 2 − < CSO2 >
sCSO / n

= 4.303

2

The 95% confidence interval for CSO2 would then be given by
14.32 ⎞
⎛
CSO2 = ⎜ 301.7 ± 4.303*
⎟ ppm = ( 301.7 ± 35.58 ) ppm
3 ⎠
⎝
or 266.1 ppm < CSO2 < 337.3 ppm
(d) It is seen that the 95% confidence interval for CSO2 based on a sample size of 3 is broader
than that based on a sample size of 6, reflecting a greater uncertainty associated with a
smaller sample size. The result reflects a general observation, namely, a price to pay for a
smaller sample size is a broader confidence interval and a greater uncertainty in the result.



## Metadata
- Source file: junk_drawer/CHE 330 - Continuous Variables and Probability Distributions Supplemental Notes.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
