# Lecture 03 handout.pdf

Source: junk_drawer/Lecture 03 handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 3: Reactor Models, Dynamic Simulation, and Their Nonlinear Behaviors Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 3: Reactor Models, Dynamic Simulation,
and Their Nonlinear Behaviors

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

January 14, 2025

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

0 / 14

Discuss & Recapture

How does a process model usually look like?

What assumptions do we typically make?
How to write out the model quickly and accurately?

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

1 / 14

Learning objectives of this lecture

1

Model tanks (CSTRs) involving chemical reactions
▶

Challenge: Deal with thermodynamics of a mixture

2

Simulate the reactor model with Matlab

3

See the complexity in the behaviors of a nonlinear system

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

2 / 14

Example 5: CSTR (non-isothermal)

Reaction: A → B
Assumptions
1
2

Constant volume holdup (qin = qout = q)
Constant ρ and CP (independent of cA ): A and B have equal ρ and CP
and form an ideal mixture

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

3 / 14

Mass balance

Molar balance for A:
d(VcA )
= qcAi − qcA − rV
dt
Reaction kinetics:
▶
▶

⇒

Rate law: r = kcA
Arrhenius law: k = k0 e−E/RT (k0 , E, R: constants)

dcA
q
= (cAi − cA ) − k0 e−E/RT cA
dt
V
Why don’t we need to do a mass balance for B?
What if this is a multi-reaction system?

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

4 / 14

Energy balance
Assuming U = H for liquid:
dH
= Ḣin − Ḣout + Q
dt
▶
▶

H: total enthalpy, Ḣin , Ḣout : enthalpy flow rate
Heat exchange: Q = −UA(T − Tc ) (U, A: constants)

Enthalpy-temperature relation: Not so easy!
We can’t simply use Ĥ = CP T . The molar enthalpy of A and B can’t
be both zero at the reference temperature.
▶ We may set Ĥ = C T . Then Ĥ = C T + ∆Ĥ ◦ (standard molar
A
P
B
P
r
enthalpy change of reaction)


H = VcA ĤA + VcB ĤB = V cA CP T + cB (∆Ĥr◦ + CP T )
▶

▶

Then,


dH
dcA
dcB
dT
◦
=V
CP T +
(∆Ĥr + CP T ) + (cA + cB )CP
dt
dt
dt
dt

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

5 / 14

Energy balance (cont.)

Note: cA + cB = cAi , dcA = −dcB .


dcA
dT
◦
V
(−∆Ĥr ) + cAi CP
= Ḣin − Ḣout − UA(T − Tc )
dt
dt
How about Ḣin, out ?


Ḣin = qcAi CP Ti , Ḣout = q cA CP T + cB (∆Ĥr◦ + CP T )


Ḣin − Ḣout = q cAi CP (Ti − T ) − (cAi − cA )∆Ĥr◦
Plug in mass balance: dcdtA = Vq (cAi − cA ) − k0 e−E/RT cA ⇒
dT
VcAi CP
= qcAi CP (Ti − T ) + Vk0 e−E/RT cA (−∆Ĥr◦ ) − UA(T − Tc )
dt

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

6 / 14

Energy balance ... Finally!

q
dcA
= (cAi − cA ) − k0 e−E/RT cA
dt
V
dT
q
k0 e−E/RT cA (−∆Ĥr◦ ) UA(T − Tc )
= (Ti − T ) +
−
dt
V
CP cAi
VcAi CP
How to make sense of this model?
V /q: residence time, (q/V )(in − out): effect of inlet
k0 e−E/RT cA : reaction rate [=] mol/m3 /s
▶ (−∆Ĥ ◦ ): heat released from reaction [=] J/mol
r
▶ UA(T − T ): cooling rate [=] J/s
c
▶ VC c : total heat capacity [=] J/K
P Ai
▶

▶

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

7 / 14

Example 6: Isothermal CSTR with multiple reactions)

Setting (Gray-Scott model):
1
2

qi = q = const., V = const.
k
k
Reactions: A+2B →1 3B, B →2 C, both are elementary reactions

Mass balances:

dcA
= qcAi − qcA − I?
dt
dcB
= qcBi − qcB + II?
V
dt
V

I = Vk1 cA cB2 , II = V ((3 − 2)k1 cA cB2 − k2 cB )

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

8 / 14

Summary on process modeling

1

Start with mass and energy balances
▶
▶

2

Relate variables to T , P, compositions, and mass/moles
▶
▶

3

Based on the description, include all relevant terms [CHE 205/225]
Transport phenomena are handled in a simplified way here. (In a real
setting, use PDEs or more accurate correlations.) [CHE 311/312]
Thermo: enthalpy, chemical potential (fugacity), etc. [CHE 315/316]
Reaction: rate law [CHE 446]

Simplify... Just be patient!
▶

Interpret the model, verify the units, check DoF

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

9 / 14

Simulating the CSTR with Matlab

Consider the isothermal reactor
dcA
= (q/V )(cAi − cA ) − k1 cA cB2
dt
dcB
= (q/V )(cBi − cB ) + k1 cA cB2 − k2 cB
dt
where q/V = 0.15 min−1 , cAi = 1 mol/L, cBi = 0.0667 mol/L,
k1 = 40 L2 · mol−2 · min−1 , k2 = 1 min−1
Chemical processes are almost always nonlinear systems!
▶
▶

No analytical solution should be expected
The behavior may be complicated ... let’s see how

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

10 / 14

Codes: Mind the syntax
Suppose cA (0) = 0.2, cB (0) = 0.1

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

11 / 14

** Limit cycle behavior
Simulate for 250 minutes... The system is attracted to
(non-sinusoidal) periodic oscillations – called a limit cycle

We did not force the system to oscillate, but only replenish reactants
Think about biological clocks, cell mitosis, etc.
Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

12 / 14

** Bifurcation
Increase q/V to 0.3 (a smaller tank) or decrease to 0.1 (a larger tank)

The reactor can exhibit high-conversion steady-state, cyclic,
low-conversion steady-state behaviors, sensitive to parameters
(operating conditions) (in this case: residence time)
Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

13 / 14

Nonlinear Systems v.s. Linear Systems

Generally speaking, nonlinear ODEs can have highly complex traits
▶

An intriguing area of scientific research

This course shall focus on linear systems (from next lecture)
Reason: Linear systems are easier to study, while nonlinear systems
require much more mathematics
▶ Justification for this laziness: Nonlinear systems are approximately
linear, if operated near a steady state
▶ Tools: Laplace transform and transfer function
▶

Wentao Tang (NCSU)

Reactor Models & Simulation

January 14, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 03 handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
