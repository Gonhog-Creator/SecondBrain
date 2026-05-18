# Lecture 02 Handout (1).pdf

Source: junk_drawer/Lecture 02 Handout (1).pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 2: Dynamic Modeling Principles & Simple Examples Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 2: Dynamic Modeling Principles & Simple Examples

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

January 9, 2025

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

0 / 14

Discuss & Recapture
What is feedforward and feedback control?
What is a controlled/manipulated/disturbance variable
(CV/MV/DV)?
How do you state a control objective?
Growth mindset v.s. fixed mindset

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

1 / 14

Learning objectives of this lecture

1

Apply the general principles of building a dynamic process model

2

Model typical tank systems: one-component/multi-component,
adiabatic/heated

3

Perform degree-of-freedom (DoF) analysis on dynamic models

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

2 / 14

Principle 1: Conservation Laws

Accumulation rate = In − Out + Generation − Consumption
Mass balances:
▶
▶

Total balance and component balances
Generation/consumption terms in reactions: Use reaction rate laws

Energy balance:
▶

Recall from thermodynamics
X
dU tot
wj Ĥ j + Q̇ + Ẇshaft .
=
dt
j:streams

▶

wj : mass/molar flow rate, Ĥj : specific/molar enthalpy, U: internal
energy

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

3 / 14

Example 1: Liquid storage tank (isothermal)

(qi and q: volumetric flow rates)

Mass balance:
dm
dh
qi − q
= ρqi − ρq ⇒
=
.
dt
dt
A
qi : a constant, or a DV, or an MV (depending on the actual setting)
q: either an MV (if a valve is installed to manipulate), or related to h:
√
q = h/Rv or q = Cv h
Which one is more accurate? You may do an experiment.
Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

4 / 14

Example 1 (cont.): Liquid storage tank (isothermal)

Assumptions:
1
2
3

qi is a constant;
Cv (valve
√ constant) and ρ (density) are constant parameters;
q = Cv h: the out-flow from the bottom is naturally pressed by the
liquid in the tank.

Model:

▶
▶

√
qi − C v h
dh
=
.
dt
A

An ODE describing how the liquid level changes with time
Can be solved under given initial condition h(0) = h0

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

5 / 14

Example 2: Blending tank with variable holdup

(w1 , w2 , w: mass flow rates)

Mass balances:

Wentao Tang (NCSU)

d(ρV )
= w1 + w2 − w
dt
d(ρVx)
= w1 x1 + w2 x2 − wx
dt

Modeling Principles

January 9, 2025

6 / 14

Example 2 (cont.): Blending tank with variable holdup
Assumptions:
1
2
3
4

w1 and x2 are constants;
x1 is a DV;
w2 and w are MVs;
ρ is a constant, not affected by x (How do you like it?)

Model:

dV
1
= (w1 + w2 − w)
dt
ρ
d(Vx)
1
= (w1 x1 + w2 x2 − wx)
dt
ρ

Simplification of the second equation:
d(Vx)/dt = V · dx/dt + x · dV /dt
dx
w1
w2
=
(x1 − x) +
(x2 − x).
dt
ρV
ρV
Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

7 / 14

Principle 2: Constitutive equations

Use thermodynamics, transport, reaction kinetics to relate variables
When heat effect exists:
▶
▶

Relate Û, Ĥ to (T , P, x)
Use heat capacity and mixture models (ideal mixture or fugacity
equations)

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

8 / 14

Example 3: Heating Tank

Assumptions:
1
2
3

wi is a DV, w an MV
Ti is a DV, Q an MV
CP = const., ρ = const.

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

9 / 14

Example 3 (cont.): Heating Tank
Mass balance:

dV
wi − w
=
dt
ρ

Energy balance:
dUtot
= wi Ĥi − wĤ + Q
dt
▶
▶

Ĥi = CP Ti , Ĥ = CP T (assuming no phase change)
Utot = ρV Û ≈ ρV Ĥ = ρVCP T (assuming Ĥ ≈ Û for liquid)

Simplification of energy balance:


dV
dT
ρ CP T
+ VCP
= wi CP Ti − wCP T + Q
dt
dt
dT
= CP (wi Ti − wT ) + Q
⇒ CP T (wi − w) + ρVCP
dt
dT
wi
Q
⇒
=
(Ti − T ) +
dt
ρV
ρVCP
Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

10 / 14

Once you have a model, confirm with DoF Analysis!

List known quantities / parameters as constants.
2 Determine # equations (NE ) and # process variables (NV ).
1

▶

Time t is not considered as a process variable.

3

Calculate NF = NV − NE as # DoFs.

4

Identify NE output variables to be solved from ODEs.

5

There must be exactly NF input variables (DVs/MVs). Identify them.

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

11 / 14

DoF for the Heating Tank Example

Model:

dV
wi − w
=
dt
ρ
⇒

dT
wi
Q
=
(Ti − T ) +
dt
ρV
ρVCP

Constants: ρ, CP
NE = 2 and NV = 6 (V , T , wi , w, Ti , Q)
NF = 4 DoFs.
2 outputs: V , T . They are dependent on ...
4 inputs: 2 MVs (w, Q), 2 DVs (wi , Ti )

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

12 / 14

Example 4: Jacket-heated tank [Seborg Ex.2.8]

Assumptions:
Tank holdup V and jacket holdup VJ are constants
Heat loss from the vessel is negligible
Tank contents and jacket contents have significant thermal
capacitances
4 Tank wall and jacket wall have negligible thermal capacitances
5 Heat transfer coefficient [Btu/h/ft2 /degF] U = KqJ0.8 (K = const.)
1
2
3

Model: “Two-tank”
Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

13 / 14

Example 4 (cont.): Jacket-heated tank

Energy balance for the tank
dT
q
Q
= (TF − T ) +
dt
V
ρVCP
where Q = UA(TJ − T ) = KqJ0.8 A(TJ − T )
Energy balance for the jacket
dTJ
qJ
Q
= (Ti − TJ ) −
dt
V
ρJ VJ CPJ
Engineers’ insight: How can you model fluently?
1
2
3

Understand the meaning of each term.
Verify dimensions (units).
Use analogy.

Wentao Tang (NCSU)

Modeling Principles

January 9, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 02 Handout (1).pdf
- Extracted: 2026-05-18
- Category: academic-lecture
