# CHE 330 - Error Propagation Analysis Supplemental Notes (1).pdf

Source: junk_drawer/CHE 330 - Error Propagation Analysis Supplemental Notes (1).pdf

Category: [[academic-lecture]]

## Summary
Department of Chemical & Biomolecular Engineering North Carolina State University CHE 330 Propagation of Error Analysis† Summer I 2011 Introduction Every measurement that is made in an experiment entails some measurement uncertainty (or

## Full Content
Department of Chemical & Biomolecular Engineering
North Carolina State University
CHE 330

Propagation of Error Analysis†

Summer I 2011

Introduction
Every measurement that is made in an experiment entails some measurement uncertainty (or
standard deviation), which may be small or significant, depending on the measurement method,
precision of the measurement instrument, the care or haste with which the measurement is made,
skill of the experimentalist, and the number of repeat measurements, if any. The uncertainty may
arise from a precision limitation of the measurement instrument, i.e., a reading between the
smallest markings on the instrument may have to be estimated, or it may result from an
oscillating measurement parameter that does not settle. In any case, each measurement
uncertainty will introduce an uncertainty in the result of the experiment.
Why is it important to account for measurement uncertainties in an experiment? The following
example illustrates how one may arrive at different conclusions depending on whether the
measurement uncertainties are taken into account. The example involves the catalytic hydrolysis
k
of aqueous ethylacetate, CH3COOC2H5 + H2O ⎯
⎯→
CH3COOH + C2H5OH, over a packed bed
of catalyst resin in a plug-flow reactor at a known reaction temperature. Aqueous ethylacetate of
a known concentration is fed to the reactor, and the conversion of the ethylacetate is determined
as function of the volumetric flow rate of the reactor feed. Figure 1 presents the results of four
runs at different flow rates.

If measurement uncertainties are not taken into account, the results would be defined by the four
dark circle points alone (i.e., without the error bars), and a linear regression analysis would
produce a least-square line that has a positive slope, as shown by the solid line. The latter would
lead one to conclude that the reaction rate constant k increases with the volumetric flow rate vo
and that the reaction is affected by mass transfer.
†

By P.K. Lim, Department of Chemical & Biomolecular Engineering, North Carolina State
University, Raleigh, NC 27695-7905 on August 16, 2005. Revised and updated on May 23,
2011.

On the other hand, if measurement uncertainties are taken into account, the results would then be
defined by the data points with the error bars. The error bars indicate that, with the measurement
uncertainties, the results are not definitive because all the results within the error bar range are
plausible, including a horizontal trend that is marked by the dash line in the figure above. The
latter would lead one to conclude that the reaction rate constant is independent of the volumetric
feed rate and that the reaction would not be affected by mass transfer. One would have to rely on
additional data, such as temperature-variation data, to make a definitive finding. It turns out that
additional data support the horizontal trend. Thus, an uncertainties analysis can save us from
making an over-reaching conclusion that is embarrassing at least or at worst, costly or disastrous!
At other times, an uncertainties analysis may improve the chances of validating a theory or guide
us in determining the correct data trend. Figure 2 presents the experimental results of two series
of runs. If measurement uncertainties are not taken into account, one would arrive at the linear
regression trends represented by the solid lines, which would indicate different slopes that are
contrary to a theory that one is trying to validate. The theory leads one to expect a common
slope for the two data series. If measurement uncertainties are taken into account, the data points
have error bars that make it possible to draw parallel plots for the two data series, as represented
by the dashed lines, thus validating the theory.

The two examples presented above illustrate that experimental results and conclusions could be
affected significantly by an uncertainties analysis and that a failure to account for measurement
uncertainties could lead to erroneous conclusions.
How Are Measurement Uncertainties Propagated Into an Experimental Result?
Measurement uncertainties are propagated into an experimental result through its functional
dependence on the measurement parameters. Let’s denote the experimental result or the
dependent variable by y and the measurement variables (also known as the independent
variables) by xi, where i = 1, 2, 3, …. It may be shown that for a general function y that is
dependent on independent variables x1, x2, x3, …, xi, i.e., y = f(x1, x2, x3, …, xi), the uncertainty

(or standard deviation) of y is related to the uncertainties (or standard deviations) of independent
variables x1, x2, x3, …, xi by Eqn (1)
2

2

⎡⎛ ∂y ⎞ ⎤
n ⎡
⎛ ∂y ⎞ ⎤
2
2
2
⎢
⎥
⎢
Δy = σ y = ∑ ⎜
σ xi = ∑ ⎜ ⎟ ⎥ Δxi 2
⎟
i =1 ⎢⎝ ∂xi ⎠ x ⎥
i =1 ⎢⎝ ∂xi ⎠ x ⎥
j ≠i ⎦
j ≠i ⎦
⎣
⎣
n

(1)

Two most common functional dependences of y on xi are (1) a linear combination relationship,
and (2) a power law relationship. It may be shown that, for these two common cases, Equation 1
leads to the following y uncertainty expressions, provided that the independent variables, xi (x1,
x2, …), are not correlated. The importance of the last qualification will be illustrated in two later
examples.
(1) Linear Combination Relationship
For y(xi) = ao + a1x1 + a2x2 + …, where ao, a1, a2, … are constants that may be positive or
negative or zero, and provided that x1, x2, … are NOT correlated,
n

(∆y)2 = a12(∆x1)2 + a22(∆x2)2 + a32(∆x3)2 + …. = ∑ ai 2 (Δxi ) 2

(2)

i =1

(2) Power Law Relationship
For y ( xi ) = ao x1a1 x2 a2 x3a3 ...., where ao, a1, a2, … are constants that may be positive or negative or
zero, and provided that x1, x2, … are NOT correlated,
2
2
2
2
n
(Δy ) 2
2 Δx1
2 Δx2
2 Δx3
2 Δxi
....
a
a
a
a
(3)
=
+
+
+
=
∑
1
2
3
i
y2
x12
x2 2
x32
xi 2
i =1
Example 1 The unknown density ρL of an organic liquid is determined by a buoyancy method.
A solid sphere of a known radius R is weighed in the air and then weighed again while
submerged in the organic liquid. The following set of data has been obtained: Win air = 5.2360 ±
0.0005 g, Win liq = 1.9478 ± 0.0005 g, R = 1.00 ± 0.01 cm. Determine ρL and its uncertainty from
the data.
Solution
The weight of the solid submerged in the liquid is related to the weight of the solid in air (more
rigorously in vacuum) and the buoyancy force B by Win liq = Win air − B. But the buoyancy force
4
is given by the weight of the liquid displaced, i.e., B = πR 3 ρ L .
3
4 3
4
Win air = πR ρ S where ρS is the density of the solid.
Win liq = πR 3 ( ρ S − ρ L )
3
3
Win liq Win air − Win liq (5.2360 − 1.9478) g
ρL = ρS −
=
=
= 0.7850 g / cm 3
4 3
4 3
4
πR
πR
π (1.0) 3 cm 3
3
3
3

Win air − Win liq (ΔW ) R −3
, it follows from Equation 3
=
4 3
4
πR
π
3
3
2
2
2
Δρ L
[Δ(ΔW )]2
0.01 2
2 [ Δ ( ΔW )]
2 ΔR
(4)
that
=
(
1
)
+
(
−
3
)
=
+ 9(
)
2
2
2
2
1.00
(ΔW )
3.2882 g
R
ρL
Using the power law relationship, ρ L =

but ΔW = Win air − Win liq , which is a linear combination relationship, it follows from Equation 2
that [∆(∆W)]2 = ∆Win air2 + ∆Win liq2 = (0.00052 + 0.00052) g2
Equation 4 =>

Δρ L

2

ρL2

=

[Δ(ΔW )]2
0.01 2 0.0005 2 (2)
+
9
(
) =
+ 0.0009 = 0.00090005
1.00
3.2882 2 g 2
3.2882 2

Therefore, ∆ρL = ±(0.00090005)½ρL = ±(0.0300008)(0.7850) g/cm3 = ±0.0236 g/cm3. The
density of the organic liquid should then be reported as ρL = (0.7850 ±0.0236) g/cm3.
The above analysis shows that the uncertainty of the density determination is largely dependent
on the uncertainty of the radius measurement and the contribution of the uncertainty of mass
measurement to the density uncertainty is essentially negligible. If an increased precision of the
density determination is desired, the analysis indicates that the incremental effort and resource
should be directed at getting a more precise radius measurement rather than mass measurement.
In general, an analysis of the propagation of measurement uncertainties is essential for an
efficient allocation of resource and effort in seeking an experimental improvement.
Example 2 The following data have been collected on a hot water stream in a heat exchanger
experiment: mass flow rate = 5.0 ± 0.2 kg/min, inlet temperature = 60.0 ± 0.05 oC, outlet
temperature = 45.5 ± 0.05 oC. Given that the specific heat of water is 1.0 kcal/(kg.oC),
determine (a) the heat transfer rate from the hot water stream, and (b) the uncertainty in the heat
transfer rate due to measurement uncertainties.
Solution



Q = − m hCP (Thout − Thin ) ≡ −m hCP ΔTh

(5)


kg
kcal
kcal
*1.0 o *(45.5 − 60.0)o C = 72.5
(a) Q = − m hCP (Thout − Thin ) = −5.0
min
kg. C
min

(b) First Solution that starts with a power law relation, Q = −m C ΔT
h

P

h

2
2
2
⎛ ΔQ ⎞ ⎛ Δm h ⎞ ⎛ ΔΔTh ⎞
⎟ +⎜
⎟
⎜  ⎟ =⎜
⎝ Q ⎠ ⎝ m h ⎠ ⎝ ΔTh ⎠

(5)
(6)

But ΔTh = Thout − Thin for which the linear combination rule applies, Δ ( ΔTh ) = ΔThout 2 + ΔThin 2
2

(

2
2
2
2
ΔThout 2 + ΔThin 2
⎛ ΔQ ⎞ ⎛ Δm h ⎞ ⎛ ΔΔTh ⎞ ⎛ Δm h ⎞
⎟ +⎜
⎟ =⎜
⎟ +
⎜  ⎟ =⎜
2
⎝ Q ⎠ ⎝ m h ⎠ ⎝ ΔTh ⎠ ⎝ m h ⎠
Th out − Thin

(

)

)

(6’)

(

)

(

)

2
2
2
ΔThout 2 + ΔThin 2
0.052 + 0.052
⎛ ΔQ ⎞ ⎛ Δm h ⎞
⎛ 0.2 ⎞
=⎜
= 0.001624
⎟ +
⎜  ⎟ =⎜
⎟ +
2
2
⎝ 5.0 ⎠
( 45.5 − 60.0 )
⎝ Q ⎠ ⎝ m h ⎠
Th out − Thin

(

)

kcal
kcal
ΔQ = ±Q 0.001624 = ±72.5
*0.0403 = ±2.92
min
min

(7)

Second (Erroneous) Solution that starts with the linear combination rule,

Q = −CP (m hThout − m hThin )

(5”)

would give
2
2
2
2




ΔQ 2 = CP 2 ⎡ Δ − 
mThout ⎤ + CP 2 ⎡ Δ 
mThin ⎤ = CP 2 ⎡ Δ 
mThout ⎤ + CP 2 ⎡ Δ 
mThin ⎤
⎣
⎦
⎣
⎦
⎣
⎦
⎣
⎦

(

(

)

)

(

(

2

)

)

(

)

(

)

(8)

2

But ⎡ Δ 
mThout ⎤ & ⎡ Δ 
mThin ⎤ are given by the power law relation, i.e.,
⎣
⎦
⎣
⎦

(

)

2

2
2
⎡Δ 
2
mThout ⎤
2
2 ⎡ Δm
 2 ΔThout ⎤
⎣
⎦ = Δm + ΔThout => ⎡ Δ 
mThout ⎤ = 
mThout ⎢ 2 +
⎥ or
2
⎣
⎦
m 2
Thout 2
Thout 2 ⎥⎦
⎢⎣ m

mThout

(

)

(

(

)

)

(

)

2

⎡Δ 
mThout ⎤ = ⎡⎣Thout 2 Δm 2 + m 2 ΔThout 2 ⎤⎦
⎣
⎦

(

)

(9)

2

2
2
⎡Δ 
2
mThin ⎤
2
2 ⎡ Δm
 2 ΔThin ⎤
⎣
⎦ = Δm + ΔThin => ⎡ Δ 
mThin ⎤ = 
mThin ⎢ 2 +
⎥ or
2
⎣
⎦
m 2
Thin 2
Thin 2 ⎥⎦
⎢⎣ m

mThin

(

)

(

(

)

)

(

)

2

⎡Δ 
mThin ⎤ = ⎡⎣Thin 2 Δm 2 + m 2 ΔThin 2 ⎤⎦
(10)
⎣
⎦

(11)
Eqn (7), (8) & (9) => ΔQ 2 = CP 2 ⎡ Thout 2 + Thin 2 Δm 2 + m 2 ΔThout 2 + ΔThin 2 ⎤
⎣
⎦
1

2
2
2
2
2
2 ⎤2

⎡


ΔQ = ±CP Thout + Thin Δm + m ΔThout + ΔThin
⎣
⎦
1
kcal
kg ⎞
kcal
⎛
(12)
ΔQ = ±1.0 o ⎡⎣(602 + 45.52 )0.22 + 5.02 (0.052 + 0.052 ) ⎤⎦ 2 ⎜ o C
⎟ = ± 15.06
kg. C
min ⎠
min
⎝

(

(

)

)

(

(

)

)

The two results given by Equations 7 & 12 are in sharp disagreement. It turns out that the
Second Solution is based on an assumption−which turns out to be faulty in this example−that is
implicit in the use of the linear combination rule, namely, that the independent variables (xi’s)
are independent of and not correlated or related to one another. However, in this problem, the
two variables upon which the linear combination rule was erroneously applied, 
mThout and 
mThin ,
are, in fact, not independent but are related by m . Being based on a faulty assumption, the
Second Solution is actually not valid.
Example 3 In a study of the head loss coefficient of an expansion valve, the following set of set
of data has been collected:

Inlet valve diameter = 0.0225 m, Outlet valve diameter = 0.0296 m

Volumeric flow rate of water through the valve = (4.10 ± 0.10)*10–4 m3/s
Manometer readings: at valve inlet = 231 ± 2 mm H2O, at valve outlet = 249 ± 2 mm H2O
Given that the mechanical energy balance across the expansion valve is given by
2
2
2
P2 − P1 (v 2 − v1 )
v1
+
= −K d
, where P is the fluid pressure, v is the fluid velocity, ρ is the
2
2
ρ
fluid density (= 1.0 g/cm3), Kd is the head loss coefficient, and subscripts 1 and 2 denote inlet and
outlet conditions, respectively, determine (a) the head loss coefficient of the expansion valve and
(b) its uncertainty.
Solution
2 ( P2 − P1 ) (v2 2 − v12 ) 2 ( P2 − P1 ) v2 2
−Kd =
+
=
+ 2 −1
v12
v1
ρ v12
ρ v12
4v
4vo
, P = ρ gh1 , and P2 = ρ gh2
But v1 = o2 , v2 =
π d1
π d22 1
π 2 d14 g ( h2 − h1 ) d14
2 ( P2 − P1 ) v2 2
1
∴− K d =
+
−
=
+ 4 −1
v12
vo 2
d2
8
ρ v12

(13)

(13’)

π 2 d14 g ( h2 − h1 )

d14
m ( 0.249 − 0.231) m ⎛ 0.0225 ⎞
π 2 0.02254 m 4
1
9.81 2
(a) − K d =
+
−
=
+⎜
⎟ −1
6
2
4
2 m
8
8
0.0296 ⎠
vo
d2
s
⎝
–4
4.10*10
s2
− K d = 0.3321 + 0.3339 − 1 = −0.3340 or K d = 0.3340
4

(

)

(b) Assuming that d1 and d2 have no uncertainties, the uncertainty in Kd would then be given by
2

⎛ ΔK d ⎞ ⎛ Δ ( Δh ) ⎞
2 ⎛ Δvo ⎞
the power law relation, ⎜
⎟ + ( −2 ) ⎜
⎟ =⎜
⎟
⎝ K d ⎠ ⎝ Δh ⎠
⎝ vo ⎠
2

2

(14)

But [Δ ( Δh )]2 is given by the linear combination rule, i.e., [Δ ( Δh )]2 = ( Δh1 ) + ( Δh2 )
2

(

2

)

2
2
2
2
2
22 + 22 mm 2
⎛ ΔK d ⎞ ⎛ ( Δh1 ) + ( Δh2 ) ⎞
2 ⎛ Δvo ⎞
⎛ 0.10 ⎞
⎟ + ( −2 ) ⎜
∴⎜
+ 4⎜
⎟ =⎜
⎟ =
⎟ = 0.02707
2
⎟
vo ⎠
(249 − 231) 2 mm 2
4.10 ⎠
⎝
⎝ K d ⎠ ⎜⎝ (h2 − h1 )
⎝
⎠

or ΔK d = ± 0.02707 K d = ± 0.02707 *0.3340 = ±0.0550
2

2

⎛d ⎞
⎛d ⎞
Note that v1 and v2 are related by volumetric flow rate vo = π ⎜ 1 ⎟ v1 = π ⎜ 2 ⎟ v2
⎝2⎠
⎝ 2 ⎠
Therefore, they should NOT BOTH be treated as independent variables. If v1 and v2 were both
treated as independent variables, a different and erroneous result would be obtained (after a
somewhat tedious analysis).
π 2 d14 g ( h2 − h1 ) d14
π 2 d14 g ( h2 − h1 ) d14
+
−
and
−
=
+ 4 − 1 are
1
K
Note that while − K d =
d
8
8
vo 2
d24
vo * vo
d2
mathematically equivalent, the two expressions would yield different ΔK d results if the power

law relation is applied to the second expression without a consideration of the independency of
the parameters. It can be shown that the erroneous approach would yield
2

2

⎛ Δ ( Δh ) ⎞
⎛ ΔK d ⎞ ⎛ Δ ( Δh ) ⎞
⎛ Δvo ⎞
2 ⎛ Δvo ⎞
(15)
⎟ + 2* ( −1) ⎜
⎟ + 2⎜
⎜
⎟ =⎜
⎟ =⎜
⎟
⎝ K d ⎠ ⎝ Δh ⎠
⎝ vo ⎠ ⎝ Δh ⎠
⎝ vo ⎠
2
2
22 + 22 )
(
⎛ ΔK d ⎞
⎛ 0.10 ⎞
+ 2⎜
⎜
⎟ =
⎟ = 0.02588 or ΔK d = ± 0.02588 *0.3340 = ±0.0537 ,
(249 − 231) 2
⎝ 4.10 ⎠
⎝ Kd ⎠
which would be incorrect.
2

2

2

Table 1 summarizes the formulae which are appropriate for the analysis of the propagation of
measurement uncertainties for the various functional dependence of the variable y on the
independent variables xi. In addition to the linear combination and power-law relationships
covered by Equations 2 and 3 that are most commonly used, Table 1 lists other formulae that are
less commonly used.
Table 1. Formulae (derived from Equation 1) for the propagation of measurement uncertainties
for the various fundamental dependence of y on xi.
Function y = y(x1, x2, ..)

Uncertainty of y, Δy
2

2 2
1 1

2

2

n

y = ao + a1x1 + a2x2 + …

Δy = a x + a2 x2 + ...

y = ao + a1x1 – a2x2 + …

Δy 2 = a12 x12 + ( −a2 ) x2 2 + ...

y = ao x1a1 x2 a2 ...

⎛ Δy ⎞
2 ⎛ Δx1 ⎞
2 ⎛ Δx2 ⎞
⎟ + a2 ⎜
⎟ + ...
⎜ ⎟ = a1 ⎜
⎝ y ⎠
⎝ x1 ⎠
⎝ x2 ⎠

2

2

2

Z = ao

x1a1 a2
x2 ... = ao x1a1 x2 − a2 ...
x2 a2

y = ao ln ( a1 * x1 )
= ao ln a1 + ao ln x1

2

2

⎛ Δx ⎞
Δy = ao ⎜ 1 ⎟
⎝ x1 ⎠
2

2

2

⎛ Δy ⎞
2
2
⎜ ⎟ = a1 Δx1
y
⎝ ⎠
2

y = ao

( a1 x1 )

i =1

2

2

⎛ Δy ⎞
2 ⎛ Δx2 ⎞
2 ⎛ Δx1 ⎞
⎟ + ( −a2 ) ⎜
⎟ + ...
⎜ ⎟ = a1 ⎜
⎝ y ⎠
⎝ x1 ⎠
⎝ x2 ⎠

2

y = ao exp ( a1 x1 )

Δy 2 = a12 x12 + a2 2 x2 2 + ... =∑ ai 2 (Δxi ) 2

⎛ Δy ⎞
2
2
2
⎜ ⎟ = a1 Δx1 [ ln(ao ) ]
⎝ y ⎠

2

n
⎛ Δy ⎞
2 ⎛ Δxi ⎞
=
⎟
⎜ ⎟ ∑ ai ⎜
i =1
⎝ y ⎠
⎝ xi ⎠

2



## Metadata
- Source file: junk_drawer/CHE 330 - Error Propagation Analysis Supplemental Notes (1).pdf
- Extracted: 2026-05-18
- Category: academic-lecture
