# Homework Set 2 Solutions (1).pdf

Source: junk_drawer/Homework Set 2 Solutions (1).pdf

Category: [[academic-homework]]

## Summary
CHE 435/525 – Process Systems Analysis and Control Spring 2025 Homework Set 2. Laplace Transform and its Inverse, Transfer Function Model (Solutions) Question 1 (a) Let 𝑧1 = 𝑟1 𝑒 𝑖𝜃1 , 𝑎𝑛𝑑 𝑧2 = 𝑟2 𝑒 𝑖𝜃2 . • |𝑧1 𝑧2 | = |𝑧1 |. |𝑧2 |

## Full Content
CHE 435/525 – Process Systems Analysis and Control

Spring 2025

Homework Set 2. Laplace Transform and its Inverse, Transfer Function Model (Solutions)

Question 1
(a)
Let 𝑧1 = 𝑟1 𝑒 𝑖𝜃1 , 𝑎𝑛𝑑 𝑧2 = 𝑟2 𝑒 𝑖𝜃2 .
• |𝑧1 𝑧2 | = |𝑧1 |. |𝑧2 |
LHS:
|𝑧1 𝑧2 | = |𝑟1 𝑟2 𝑒 𝑖(𝜃1+𝜃2 ) | = 𝑟1 𝑟2 |𝑒 𝑖(𝜃1 +𝜃2) | = 𝑟1 𝑟2
RHS:

•

|𝑧1 |. |𝑧2 | = |𝑟1 𝑒 𝑖𝜃1 |. |𝑟2 𝑒 𝑖𝜃2 | = 𝑟1 |𝑒 𝑖𝜃1 | . 𝑟2 |𝑒 𝑖𝜃2 | = 𝑟1 𝑟2
𝐿𝐻𝑆 = 𝑅𝐻𝑆 (𝑃𝑟𝑜𝑣𝑒𝑑)
∡(𝑧1 𝑧2 ) = ∡𝑧1 + ∡𝑧2

LHS:
∡(𝑧1 𝑧2 ) = ∡(𝑟1 𝑟2 𝑒 𝒊(𝜽𝟏 +𝜽𝟐 ) ) = 𝜽𝟏 + 𝜽𝟐
RHS:
∡𝑧1 + ∡𝑧2 = ∡(𝑟1 𝑒 𝜃1 ) + ∡(𝑟2 𝑒 𝜃2 ) = 𝜃1 + 𝜃2
𝐿𝐻𝑆 = 𝑅𝐻𝑆
𝑧1
• |𝑧 | = |𝑧1 |/|𝑧2 | (whenever 𝑧2 is non-zero)

(𝑃𝑟𝑜𝑣𝑒𝑑)

2

LHS:

𝑧1
𝑟1
𝑟1
𝑟1
| | = | 𝑒 𝑖(𝜃1 −𝜃2 ) | = |𝑒 𝑖(𝜃1 −𝜃2) | =
𝑧2
𝑟2
𝑟2
𝑟2

RHS:
|𝑧1 |/|𝑧2 | = |𝑟1 𝑒 𝑖𝜃1 |/|𝑟2 𝑒 𝑖𝜃2 | = 𝑟1 |𝑒 𝑖𝜃1 | / 𝑟2 |𝑒 𝑖𝜃2 | =
𝐿𝐻𝑆 = 𝑅𝐻𝑆
•

𝑟1
𝑟2

(𝑃𝑟𝑜𝑣𝑒𝑑)

𝑧

∡ (𝑧1) = ∡𝑧1 − ∡𝑧2
2

LHS:
𝑧
𝑟
∡ (𝑧1) = ∡(𝑟1 𝑒 𝒊(𝜽𝟏 −𝜽𝟐 ) ) = 𝜽𝟏 − 𝜽𝟐
2

2

RHS:
∡𝑧1 − ∡𝑧2 = ∡(𝑟1 𝑒 𝜃1 ) − ∡(𝑟2 𝑒 𝜃2 ) = 𝜃1 − 𝜃2
𝐿𝐻𝑆 = 𝑅𝐻𝑆

(𝑃𝑟𝑜𝑣𝑒𝑑)

(b)
Let 𝑧1 = 𝑟1 𝑒 𝑖𝜃1 , 𝑎𝑛𝑑 𝑧2 = 𝑟2 𝑒 𝑖𝜃2 .

𝑧1 𝑧2 = 𝑟1 𝑟2 𝑒 𝑖(𝜃1 +𝜃2)
𝑧1 𝑧2 = 𝑟1 𝑟2 [𝑐𝑜𝑠 (𝜃1 + 𝜃2 ) + 𝑖 𝑠𝑖𝑛 (𝜃1 + 𝜃2 ) ]

(1)

We can also write:
𝑧1 = 𝑟1 𝑐𝑜𝑠(𝜃1 ) + 𝑖 𝑟1 𝑠𝑖𝑛 (𝜃1 )
𝑧2 = 𝑟2 𝑐𝑜𝑠(𝜃2 ) + 𝑖 𝑟2 𝑠𝑖𝑛 (𝜃2 )

(2)
(3)

From (2) and (3), we have:
𝑧1 𝑧2 = 𝑟1 𝑟2 [𝑐𝑜𝑠 𝜃1 𝑐𝑜𝑠 𝜃2 − 𝑠𝑖𝑛 𝜃1 𝑠𝑖𝑛 𝜃2 + 𝑖(𝑐𝑜𝑠 𝜃1 𝑠𝑖𝑛 𝜃2 + 𝑠𝑖𝑛 𝜃1 𝑐𝑜𝑠 𝜃2 ) ]
Comparing (1), and (4), we have:
𝑐𝑜𝑠 (𝜃1 + 𝜃2 ) = 𝑐𝑜𝑠 𝜃1 𝑐𝑜𝑠 𝜃2 − 𝑠𝑖𝑛 𝜃1 𝑠𝑖𝑛 𝜃2 ,
𝑠𝑖𝑛 (𝜃1 + 𝜃2 ) = 𝑐𝑜𝑠 𝜃1 𝑠𝑖𝑛 𝜃2 + 𝑠𝑖𝑛 𝜃1 𝑐𝑜𝑠 𝜃2 ).

(4)

(c)
Let 𝑧1 = 𝑟1 𝑒 𝑖𝜃1 = 1 + 𝑖, 𝑎𝑛𝑑 𝑧2 = 𝑟2 𝑒 𝑖𝜃2 = √3 + 3𝑖;

𝜋
𝑟𝑎𝑑𝑖𝑎𝑛𝑠.
4
𝜋
𝑟2 = √12; 𝜃2 = 𝑡𝑎𝑛−1 (√3) = 𝑟𝑎𝑑𝑖𝑎𝑛𝑠.
3
1+𝑖
𝑧1 𝑟1 𝑖(𝜃 −𝜃 )
1 −𝑖( 𝜋 )
= = 𝑒 1 2 =
𝑒 12
√3 + 3𝑖 𝑧2 𝑟2
√6
𝑟1 = √2; 𝜃1 = 𝑡𝑎𝑛−1 (1) =

Question 2
(a)
With 𝑓(𝑡) = 5 + exp(−3𝑡) + 𝑡 exp(−4𝑡) = 5 𝑆(𝑡) + exp(−3𝑡) + 𝑡 exp(−4𝑡) for 𝑡 ≥ 0, where 𝑆(𝑡) is
the unit step function:
ℒ[𝑓(𝑡)] = ℒ[5 𝑆(𝑡) + exp(−3𝑡) + 𝑡 exp(−4𝑡)]
= 5ℒ[𝑆(𝑡)] + ℒ[exp(−3𝑡)] + ℒ[𝑡 exp(−4𝑡)]
= 5ℒ[𝑆(𝑡)] + ℒ[exp(−3𝑡)] + ℒ [
=

𝑡 2−1
exp(−4𝑡)]
(2 − 1)!

5
1
1
+
+
(using transforms 2, 5, and 7 from Table 3.1)
𝑠 𝑠 + 3 (𝑠 + 4)2

(b)
With 𝑓(𝑡) = (𝑡 − 1) cos(4(𝑡 − 1)) 𝑆(𝑡 − 1) + 𝑡 2 , then
ℒ[𝑓(𝑡)] = ℒ[(𝑡 − 1) cos(4(𝑡 − 1)) 𝑆(𝑡 − 1) + 𝑡 2 ]
= ℒ[(𝑡 − 1) cos(4(𝑡 − 1))] + ℒ[𝑡 2 ]
Let 𝑔(𝑡) = 𝑡 cos(4𝑡), then 𝑔(𝑡 − 𝜃) = (𝑡 − 𝜃) cos(4(𝑡 − 𝜃))
ℒ[𝑓(𝑡)] = ℒ[𝑔(𝑡 − 1)𝑆(𝑡 − 1)] + ℒ[𝑡 2 ]
= ℒ[𝑔(𝑡 − 1)𝑆(𝑡 − 1)] + ℒ[𝑡 3−1 ]

= ℒ[𝑔(𝑡 − 1)𝑆(𝑡 − 1)] +
= 𝑒 −𝑠 𝐺(𝑠) +

(3 − 1)!
(using transforms 4 and 26 from Table 3.1)
𝑠3

2
𝑠3
∞

Where 𝐺(𝑠) = ℒ[𝑔(𝑡)] = ℒ[𝑡 cos(4𝑡)] = ∫0 𝑡 cos(4𝑡) 𝑒 −𝑠𝑡 𝑑𝑡. Using an integral table, or integration by
parts, we arrive at the following:
𝐺(𝑠) =

𝑠 2 − 16
𝑠 4 + 32𝑠 2 + 256

Thus,
𝑠 2 − 16
2
ℒ[𝑓(𝑡)] = 𝑒 −𝑠 ( 4
)+ 3
2
𝑠 + 32𝑠 + 256
𝑠

(c)
Using the figure, we can find the define a piecewise function of Temperature with time as follows:
𝑇(𝑡) = {

75 − 20
𝑡 + 20 0 ≤ 𝑡 < 30
30
75
𝑡 ≥ 30
11
= { 6 𝑡 + 20 0 ≤ 𝑡 < 30
75
𝑡 ≥ 30

This piecewise function can be expanded into a single-line
equation using time-delayed step function:
𝑇(𝑡) =

11
11
𝑡 + 20 + {− ( 𝑡 + 20) + 75} 𝑆(𝑡 − 30)
6
6
11
11
𝑇(𝑡) =
𝑡 + 20 + {− 𝑡 + 55} 𝑆(𝑡 − 30)
6
6
11
11
11
=
𝑡 + 20 + {− (𝑡 − 30) − (30) + 55} 𝑆(𝑡 − 30)
6
6
6
11
11
=
𝑡 + 20 − (𝑡 − 30)𝑆(𝑡 − 30)
6
6

Since 𝑡 ≥ 0,
𝑇(𝑡) =

11
11
𝑡 + 20 𝑆(𝑡) − (𝑡 − 30)𝑆(𝑡 − 30)
6
6

Then,
11
11
𝑡 + 20 𝑆(𝑡) − (𝑡 − 30)𝑆(𝑡 − 30)]
6
6
11
11
=
ℒ[𝑡] + 20ℒ[𝑆(𝑡)] − ℒ[(𝑡 − 30)𝑆(𝑡 − 30)]
6
6

ℒ[𝑇(𝑡)] = ℒ [

Question 3

(a)

(b)

=

11 1
1
11 𝑒 −30𝑠
( 2 ) + 20 ( ) − ( 2 ) (using transforms 2, 3, and 26 from Table 3.1)
6 𝑠
𝑠
6
𝑠

=

11 1 − 𝑒 −30𝑠
20
(
)+
2
6
𝑠
𝑠

(c)

Question 4
The initial conditions:

𝑑2 𝑥
𝑑𝑥
(0) = 0, (0) = 0, 𝑥(0) = 0
𝑑𝑡 2
𝑑𝑡

(a)
𝑑3 𝑥
𝑑2 𝑥
𝑑𝑥
+
2
+2
+𝑥 =3
3
2
𝑑𝑡
𝑑𝑡
𝑑𝑡
Do Laplace transform:
𝑑𝑥
𝑑2 𝑥
𝑑𝑥
(0) − 2 (0)] + 2 [𝑠 2 ∙ 𝑋(𝑠) − 𝑠 ∙ 𝑥(0) −
(0)]
𝑑𝑡
𝑑𝑡
𝑑𝑡
3
+2[𝑠 ∙ 𝑋(𝑠) − 𝑥(0)] + 𝑋(𝑠) =
𝑠
𝑠 3 ∙ 𝑋(𝑠) + 2𝑠 2 ∙ 𝑋(𝑠) + 2𝑠 ∙ 𝑋(𝑠) + 𝑋(𝑠)
3
3
𝑋(𝑠) =
=
3
2
𝑠(𝑠 + 2𝑠 + 2𝑠 + 1)
1 √3
1 √3
𝑠(𝑠 + 1)(𝑠 + +
𝑖)(𝑠 + −
𝑖)
2
2
2
2
3
𝐴
𝑋(𝑠) =
= + {𝑜𝑡ℎ𝑒𝑟 𝑡𝑒𝑟𝑚𝑠}
𝑠
1 √3
1 √3
𝑠(𝑠 + 1)(𝑠 + 2 + 2 𝑖)(𝑠 + 2 − 2 𝑖)

[𝑠 3 ∙ 𝑋(𝑠) − 𝑠 2 ∙ 𝑥(0) − 𝑠 ∙

The pole at s=0 indicates a constant term in the time domain suggesting that the system has a steady-state
component that does not decay over time. The other poles are on the LHP as they all have negative real
parts, indicating exponential decay to zero in the time domain. Hence x(t) converges (to a non-zero
constant).

(b)
𝑑2 𝑥
− 𝑥 = 2𝑒 𝑡
𝑑𝑡 2
The Laplace transform:

𝑑𝑥
2
(0)] − 𝑋(𝑠) =
𝑑𝑡
𝑠−1
2
𝑠 2 ∙ 𝑋(𝑠) − 𝑋(𝑠) =
𝑠−1
2
2
𝑋(𝑠) =
=
2
(𝑠 − 1)(𝑠 − 1) (𝑠 − 1)2 (𝑠 + 1)
The denominator does not have complex roots, so function x(t) is not oscillatory.
The system has a pole at s=1 in the right half-plane. Hence, x(t) diverges.
[𝑠 2 ∙ 𝑋(𝑠) − 𝑠 ∙ 𝑥(0) −

(c)
𝑑3 𝑥
+ 𝑥 = sin (𝑡)
𝑑𝑡 3
The Laplace transform:
𝑑𝑥
𝑑2 𝑥
1
(0) − 2 (0)] + 𝑋(𝑠) = 2
𝑑𝑡
𝑑𝑡
𝑠 +1
1
𝑠 3 ∙ 𝑋(𝑠) + 𝑋(𝑠) = 2
𝑠 +1
1
1
𝑋(𝑠) = 2
=
(𝑠 + 1)(𝑠 3 + 1)
1 √3
1 √3
(𝑠 + 𝑖)(𝑠 − 𝑖)(𝑠 + 1)(𝑠 − 2 + 2 𝑖)(𝑠 − 2 − 2 𝑖)
[𝑠 3 ∙ 𝑋(𝑠) − 𝑠 2 ∙ 𝑥(0) − 𝑠 ∙

The denominator has complex roots, so x(t) is oscillatory.
1
2

The system has poles at s = ±

√3
𝑖
2

(in the right half-plane). Hence, x(t) diverges.

(d)
𝑑2 𝑥
+𝑥 =4
𝑑𝑡 2
The Laplace transform:
𝑑𝑥
4
(0)] + 𝑋(𝑠) =
𝑑𝑡
𝑠
4
𝑠 2 ∙ 𝑋(𝑠) + 𝑋(𝑠) =
𝑠
4
4
𝑋(𝑠) =
=
𝑠(𝑠 2 + 1) 𝑠(𝑠 + 𝑖)(𝑠 − 𝑖)

[𝑠 2 ∙ 𝑋(𝑠) − 𝑠 ∙ 𝑥(0) −

The denominator has complex roots, leading to persistent oscillations in x(t). The pole at s=0 introduces a
constant term in the time domain, while the purely imaginary poles cause undamped oscillations. Hence,
x(t) does not converge and remains oscillatory.
[x(t)=4-4cos(t)]

Question 5

The transfer function for the pressure transmitter is given by,
Pm' ( s)
1
=
'
P ( s) (30s + 1)

And P’(s)=15/s for the step change from 35 to 50 psi.
Pm' ( s)
1
15
=
.
'
P ( s) (30s + 1) s
The step response after taking the Laplace inverse is given by−

t
30

P (t ) = 15(1 − e )
Let 𝑡𝑎 be the time that the alarm sounds. Then,
𝑃𝑚′ (𝑡𝑎 ) = 45-35 = 10 psi.
'
m

−

t

10 = 15(1 − e 30 )
ta= 32.98 s
The alarm will sound 32.98 s after 1:30 PM.

Question 6
Setting Up Balance Equation with Mass Balance
{accumulation} = {in} − {out}
𝑑𝑚
= 𝑚̇in − 𝑚̇out
𝑑𝑡
𝑑(𝜌𝑉)
= 𝜌𝑖 𝑞𝑖 − 𝜌𝑞
𝑑𝑡
Assuming constant density, 𝜌(𝑡) = 𝜌 = 𝜌𝑖
𝑑𝑉
= 𝑞𝑖 − 𝑞
𝑑𝑡
Since the volume of the water accumulated in the tank at a given height is given by: 𝑉 =
h

[R2 arccos (1 − R) − (R − h)√R2 − (R − h)2 ] L, then,
h
𝑑 ([R2 arccos (1 − R) − (R − h)√R2 − (R − h)2 ] L)
𝑑𝑡
2

= 𝑞𝑖 − 𝑞

𝑑 ((R − h)√R − (R − h) )
h
𝑑 (R arccos (1 − ))
R
𝐿
−
𝑑𝑡
𝑑𝑡
2

(
h
𝑑 (arccos (1 − R))

2

= 𝑞𝑖 − 𝑞
)

𝑑 (√R2 − (R − h)2 )

𝑑((R − h)) 𝑞𝑖 − 𝑞
=
𝑑𝑡
𝑑𝑡
𝑑𝑡
𝐿
h
𝑑𝑢
−1 𝑑ℎ
𝑑𝑣
𝑑ℎ
2
2
(R
Let 𝑢 = 1 − R and 𝑣 = R −
− h) where 𝑑𝑡 = 𝑅 𝑑𝑡 and 𝑑𝑡 = 2(𝑅 − ℎ) 𝑑𝑡 , then
𝑅2

− (R − h)

− √R2 − (R − h)2

𝑑(arccos(u)) 𝑑𝑢
𝑑(√𝑣) 𝑑𝑣
𝑑ℎ 𝑞𝑖 − 𝑞
− (R − h)
+ √R2 − (R − h)2
=
𝑑𝑡
𝑑𝑡
𝑑𝑡 𝑑𝑡
𝑑𝑡
𝐿
−1
−1
𝑑ℎ
1
𝑑ℎ
𝑑ℎ
𝑞𝑖 − 𝑞
𝑅2 (
)(
) − (R − h) (
) (2(𝑅 − ℎ) ) + √R2 − (R − h)2
=
𝑅 𝑑𝑡
𝑑𝑡
𝑑𝑡
𝐿
2√𝑣
√1 − 𝑢2
𝑅2

1

𝑅
(

(

2
√1 − (1 − h )
R

𝑑ℎ
)−
𝑑𝑡

(𝑅 − ℎ)2

(

2
√ 2
( R − (R − h) )

𝑑ℎ
𝑑ℎ
𝑞𝑖 − 𝑞
) + √R2 − (R − h)2 ( ) =
𝑑𝑡
𝑑𝑡
𝐿

)

𝑅2

𝑑ℎ
(
)( ) −
√𝑅 2 − (𝑅 − ℎ)2 𝑑𝑡

(𝑅 − ℎ)2

(

𝑑ℎ
𝑑ℎ
𝑞𝑖 − 𝑞
) + √R2 − (R − h)2 ( ) =
𝑑𝑡
𝑑𝑡
𝐿

2
√ 2
( R − (R − h) )
𝑅 2 − (𝑅 − ℎ)2
𝑑ℎ
𝑞𝑖 − 𝑞
2(
)( ) =
𝐿
√𝑅 2 − (𝑅 − ℎ)2 𝑑𝑡
𝑑ℎ
𝑞𝑖 − 𝑞
√𝑅 2 − (𝑅 − ℎ)2 ( ) =
𝑑𝑡
𝐿
𝑑ℎ
𝑞𝑖 (𝑡) − 𝑞(𝑡)
1
=(
)(
)
𝑑𝑡
2𝐿
√𝑅 2 − (𝑅 − ℎ(𝑡))2

Find Steady-State Condition
Let ℎ̅, 𝑞̅𝑖 , and 𝑞̅ represent the steady state conditions of height, inlet flowrate, and exit flowrate,
respectively. Steady state is found by setting the time derivative to zero:
𝑞̅𝑖 − 𝑞̅
1
0=(
)(
)
2
2𝐿
√𝑅 − (𝑅 − ℎ̅)2
Or
𝑞̅𝑖 = 𝑞̅
Tank is at steady state when the inlet and outlet flowrates are equal. Notice the steady-state condition is
independent of height; thus, this steady-state condition is applicable to any height. Since we are stating
that the tank is initially at steady-state condition, the steady-state height is its initial height.
Model in Deviation Variable Form
Let ℎ′ = ℎ − ℎ̅, 𝑞𝑖′ = 𝑞𝑖 − 𝑞̅𝑖 , and 𝑞 ′ = 𝑞 − 𝑞̅ , then
𝑑(ℎ′ + ℎ̅)
𝑞𝑖′ + 𝑞̅𝑖 − 𝑞′ − 𝑞̅
1
=(
)(
)
𝑑𝑡
2𝐿
√𝑅2 − (𝑅 − ℎ′ − ℎ̅)2
Since 𝑞̅𝑖 = 𝑞̅
𝑑(ℎ′ )
𝑞𝑖′ − 𝑞′
1
=(
)(
)
2
𝑑𝑡
2𝐿
√𝑅 − (𝑅 − ℎ′ − ℎ̅)2
Linearizing the Model using Taylor Series Expansion
𝑑ℎ ′

The model is in the form 𝑑𝑡 = 𝑓(ℎ′ , 𝑞𝑖′ , 𝑞’), and it can be linearized as

𝑑ℎ ′
𝜕𝑓
𝜕𝑓
≈ 𝜕ℎ′ | ℎ′ + 𝜕𝑞′ |
𝑑𝑡
𝑠
𝑖

𝜕𝑓
| 𝑞’ where 𝑠 denotes that the partial derivative is evaluated at the steady-state condition:
𝜕𝑞’ 𝑠
(ℎ′ = 0, 𝑞𝑖′ = 0, 𝑞’ = 0)

𝑠

𝑞𝑖′ +

𝑑(ℎ′ )
𝑞𝑖′ − 𝑞’ 𝜕
≈(
) ′
𝑑𝑡
2𝐿
𝜕ℎ

1

|| ℎ′ +

′
̅ 2
√ 2
{ 𝑅 − (𝑅 − ℎ − ℎ) } 𝑠

1

+

′
̅ 2
√ 2
(2𝐿 𝑅 − (𝑅 − ℎ − ℎ) )

𝑑(ℎ′ )
0− 0 𝜕
≈(
)
𝑑𝑡
2𝐿 𝜕ℎ′

𝑠

𝑠

|| ℎ′ +

′
̅ 2
√ 2
{ 𝑅 − (𝑅 − ℎ − ℎ) } 𝑠

1
2

′
̅ 2
√ 2
(2𝐿 𝑅 − (𝑅 − ℎ − ℎ) )

𝜕
{𝑞′ − 𝑞’}|| 𝑞𝑖′
𝜕𝑞𝑖′ 𝑖

𝜕
{𝑞′ − 𝑞’}|| 𝑞’
𝜕𝑞’ 𝑖

1

+

1

̅
√ 2
(2𝐿 𝑅 − (𝑅 − 0 − ℎ) )

1
̅ 2
√ 2
(2𝐿 𝑅 − (𝑅 − 0 − ℎ) )

𝜕
{𝑞 ′ − 𝑞’}|| 𝑞𝑖′
𝜕𝑞𝑖′ 𝑖
𝑠

𝜕
{𝑞 ′ − 𝑞’}|| 𝑞’
𝜕𝑞’ 𝑖
𝑠

The first term on the right-hand side goes to zero.
𝑑(ℎ′ )
≈
𝑑𝑡

1
(

2
2𝐿√𝑅 2 − (𝑅 − ℎ̅)

1

𝑞𝑖′ −
)

(

2
2𝐿√𝑅 2 − (𝑅 − ℎ̅)

𝑞’
)

Question 7
1. Ball Valves:
• Mechanism: Operates with a spherical ball that has a bore through its center. The valve opens
when this bore aligns with the flow and closes with a 90-degree rotation, effectively obstructing
the flow.
•

Applications: Favored for its reliable sealing in high pressure and temperature settings, typically
used in water, natural gas, and oil processing for secure and tight shutoff.

2. Butterfly Valves:
• Mechanism: Features a thin disc mounted on a rod that rotates to either block or open the flow
path.
•

Applications: Ideal for HVAC systems and large volume water services due to their quick
operation and ability to effectively throttle flow.

3. Plug Valves:
• Mechanism: Uses a cone-shaped or cylindrical plug that rotates within the valve body, with
passageways that line up with inlets and outlets to regulate flow.

•

Applications: Common in settings requiring frequent operation, such as slurry handling, where
minimal flow resistance and prevention of clogging are critical.

4. Rotary Globe Valves:
• Mechanism: Utilizes a rotating disk or rotor inside the valve body to finely control fluid passage.
•

Applications: Suitable for precise flow regulation in dosing, mixing, and filling operations,
especially in the pharmaceutical and chemical industries where manageable pressure drops are
necessary.

Question 8

(a)
∂x ∂2 x
= 2 − βx
∂t
∂z
Applying the Laplace transform with respect to time t, we have:
d2 X

𝑠𝑋(𝑧, 𝑠) − 𝑥(𝑧, 0) = dz2 (z, s) − β𝑋 (𝑧, 𝑠).
Assuming the initial condition, 𝑥(𝑧, 0) = 0, we obtain:
d2 X
(z, s) = (s + β)X(z, s)
dz2
Converting the boundary conditions on X(z, s):
• x(z = 0, t) = u(t) becomes:
•

X(z = 0, s) = U(s).
x(z = 1, t) + ∂z (z = 1, t) = 0 becomes:

(1)

(2)

∂x

X( 1, s) +

dX
(1,s) = 0
dz

(3)

(b)
The solution to (1) is given by:
X(z, s) = 𝐴 𝑐𝑜𝑠ℎ(√𝑠 + β 𝑧) + 𝐵 𝑠𝑖𝑛ℎ(√𝑠 + β 𝑧),
(4)
where A and B are to be determined.
Using the boundary condition given in (2),
X(0, s) = Acosh(0) + Bsinh(0) = A = U(s)
(5)
Using the boundary condition given in (3),
𝐴 𝑐𝑜𝑠ℎ(√𝑠 + β ) + 𝐵 𝑠𝑖𝑛ℎ(√𝑠 + β ) + 𝐴 √𝑠 + β 𝑠𝑖𝑛ℎ(√𝑠 + β ) + 𝐵 √𝑠 + β 𝑐𝑜𝑠ℎ(√𝑠 + β )
= 0. (6)
From (5) and (6), we have:
𝑐𝑜𝑠ℎ(√𝑠 + β ) + √𝑠 + β 𝑠𝑖𝑛ℎ(√𝑠 + β )
𝐵 = −𝑈(𝑠)
(7)
𝑠𝑖𝑛ℎ(√𝑠 + β ) + √𝑠 + β 𝑐𝑜𝑠ℎ(√𝑠 + β )
With A and B obtained in (5) and (7), we now have the full expression for the solution in (4).

•

Obtaining the transfer function:
𝐺(𝑠) =

𝑌(𝑠) 𝑋(1, 𝑠)
=
𝑈(𝑠)
𝑈(𝑠)

(8)

Obtain 𝑋(1, 𝑠) using (4)
X(1, s) = 𝐴 𝑐𝑜𝑠ℎ(√𝑠 + β ) + 𝐵 𝑠𝑖𝑛ℎ(√𝑠 + β )
Using (5) and (6), we have:
X(1, s) = 𝑈(𝑠) [𝑐𝑜𝑠ℎ(√𝑠 + β )
𝑐𝑜𝑠ℎ(√𝑠 + β ) + √𝑠 + β 𝑠𝑖𝑛ℎ(√𝑠 + β )

𝑠𝑖𝑛ℎ(√𝑠 + β ) ] (9)
𝑠𝑖𝑛ℎ(√𝑠 + β ) + √𝑠 + β 𝑐𝑜𝑠ℎ(√𝑠 + β )
Simplifying (9), while noting that 𝑐𝑜𝑠ℎ2 (√𝑠 + β ) − 𝑠𝑖𝑛ℎ2 (√𝑠 + β ) = 1, we have:
√𝑠 + β
X(1, s) = 𝑈(𝑠) [
] (10)
𝑠𝑖𝑛ℎ(√𝑠 + β ) + √𝑠 + β 𝑐𝑜𝑠ℎ(√𝑠 + β )
Plugging (10) into (8), we finally obtain:
√s + β
G(s) =
.
sinh(√s + β ) + √s + β cosh(√s + β )
−



## Metadata
- Source file: junk_drawer/Homework Set 2 Solutions (1).pdf
- Extracted: 2026-05-18
- Category: academic-homework
