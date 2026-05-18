# Visco 3.pdf

Source: junk_drawer/Visco 3.pdf

Category: [[other]]

## Summary
Muddiest points: Feb 17 • For viscoelasticity how are stress and strains equal to each other for two separate systems? 1 Muddiest points: Feb 17 • What do the variables in the following equations correspond to?

## Full Content
Muddiest points: Feb 17
• For viscoelasticity how are stress and strains equal to
each other for two separate systems?

1

Muddiest points: Feb 17
• What do the variables in the following equations
correspond to?

2

Muddiest points: Feb 17
• Constitutive equations for Maxwell, Kelvin/Voigt,
Burgers models?

3

Spring model

4

Dashpot model

5

Maxwell model

6

Kelvin/Voigt model

7

Burgers model

8

Muddiest points: Feb 17
• Can different models be used together, how do they
actually combine?

9

Viscoelasticity
•

If a constant stress, s1 or s2, is applied to a
viscoelastic material over time, t, strain, e1
evolves as shown in (a)

•

Hence at an arbitrary time, t, the strains at
the two stresses are e1(t) and e2(t), then;
ε1(t) ε2(t)
=
𝜎!
𝜎"

10

Viscoelasticity
•

If a constant stress, s1 or s2, is applied to a
viscoelastic material over time, t, strain, e1
evolves as shown in (a)

•

Hence at an arbitrary time, t, the strains at
the two stresses are e1(t) and e2(t), then;
ε1(t) ε2(t)
=
𝜎!
𝜎"

•

Strain in the two experiments are
proportional to imposed stress. Hence creep
compliance at time t can be defined as;
# (t)
# (t)
𝐽 𝑡 = 1 = 2
$!

in general,

𝐽 𝑡 =

$"

# (t)
$
11

Chpt 20

Boltzmann Superposition Principle

•

Helps determine state of stress or strain in viscoelastic materials from
knowledge of the materials deformation history

•

For varying stress, overall deformation is related to the sum of strains due
to each stress step.

12

Chpt 20

Boltzmann Superposition Principle

•

Helps determine state of stress or strain in viscoelastic materials from
knowledge of the materials deformation history

•

For varying stress, overall deformation is related to the sum of strains due
to each stress step.

•

We define creep compliance as
𝐽 𝑡 = %(')⁄$,
which is only a function of time
then for each loading,
𝜀 𝑡 = ∆𝜎𝐽(𝑡 − 𝜏)

•

With further stressing we get;
𝜀 𝑡 = 𝜀! 𝑡 + 𝜀" 𝑡 + 𝜀) 𝑡 +. .
= ∆𝜎! 𝐽 𝑡 − 𝜏! + ∆𝜎" 𝐽 𝑡 − 𝜏" +. .
*

= 0 𝐽 𝑡 − 𝜏 ∆𝜎*
*+,

13

Chpt 20

Boltzmann Superposition Principle

•

Helps determine state of stress or strain in viscoelastic materials from
knowledge of the materials deformation history

•

For varying stress, overall deformation is related to the sum of strains due
to each stress step.

•

Provided there is a linear relationship between stress and strain and
their time derivatives, then the strain produced by any set of applied
stresses is the sum of the strains produced by the individuals of the
set when acting alone.

14

Boltzmann Superposition Principle
•

We have seen that overall deformation (strain) is given by;
*

𝜀 𝑡 = 0 𝐽 𝑡 − 𝜏 ∆𝜎*
*+,

•

Which can be represented as an integral (-∞ to t =all deformation history);
'

𝜀 𝑡 = 2 𝐽 𝑡 − 𝜏 𝑑𝜎(𝑡)
-.

•

This equation can be express in terms of relaxation time, t;
'

𝑑𝜎(𝜏)
𝜀 𝑡 = 2 𝐽(𝑡 − 𝜏)
𝑑𝜏
𝑑𝜏
-.

Predicts overall strain
After stressing the sample

17

Chpt 20

Boltzmann Superposition Principle:
Recovery
𝑒! = 𝜎, 𝐽(𝑡)
𝑒" = −𝜎, 𝐽 𝑡 − 𝑡!
𝑒 𝑡 = 𝜎, 𝑡 − 𝜎, 𝑡 − 𝑡!

𝑒 / 𝑡 − 𝑡! = 𝜎, 𝐽 𝑡 − 𝑡!

19

Boltzmann Superposition Principle
•

We can also consider stress relaxation the same way:
𝜎 𝑡
𝐺 𝑡 =
𝜀

•

If we consider the stress relaxation modulus, then;
𝜎 𝑡 = 𝐺 𝑡 𝜀 = ∆𝜀! 𝐺 𝑡 − 𝜏! + ∆𝜀" 𝐺 𝑡 − 𝜏" +. .

•

This is analogous to what we saw above, hence;
'

𝑑𝜀(𝜏)
𝜎 𝑡 = 2 𝐺(𝑡 − 𝜏)
𝑑𝜏
𝑑𝜏

Predicts overall stress
After straining the sample

-.

20

Recall:
Maxwell-Reuss (isostress)

Elasticity (chpt. 19)
Kelvin-Voigt (isostrain)

Other Model
• Three-element (zener) model – overall strain can be expressed as;
𝜎
𝜎
𝜎
'
𝜀=
+
1 − 𝑒 % &(! + 𝑡
𝐸# 𝐸$
𝜂)

25

Revisiting Creep Compliance
•

•

•

A better way to represent creep is to normalize strain with a constant
applied load (i.e. creep compliance);
ε (t)
𝐽 𝑡 =
𝜎,
But from Kelvin/Voigt model;
𝜎0
𝜀(𝑡) 1
-'
'
𝜀=
1 − 𝑒 12 ⇒
=
1 − 𝑒 - 12
𝐸
𝜎,
𝐸
A better way to represent this is in log form, hence plot log (J) vs ln(t)

•
T3
T2

Since relaxation time is dependent
on temperature, we see different
curves at different T.

T1
28

…But, properties depends on temperature too

•
•

What is the basis for this thermal-driven change in mechanical properties?
How do we predict thermal response of a material under stress?

•

First look at T-driven change in stress at constant elongation.
29

Creep compliance scaling
Creep compliance curves can
be scaled onto a single “master
curve” by

T>Tg

•

shifting each curve by an
amount that depends on T

Tg • the ln(t) values shifted by a
temperature dependent
parameter of the form log(at):
now plot vs. log(t/at)

T↑

31

T<Tg

•

for T<Tg, curves shifted to
left

•

for T>Tg, curves shifted to
right

Time-Temperature Superposition
Williams-Landel-Ferry (WLF) Equation (time-temperature superposition)
• Its possible to interrelate time & temperature dependence of viscoelasticity
• Flow, a molecular relaxation effect, requires free volume, but in polymers this is limited
by neighboring polymer chains
• Doolittle’s theory of viscosity relates viscosity to occupied volume and free volume;
𝑣0 − 𝑣3
ln 𝜂 = 𝐵
+ ln 𝐴
𝑣3
A & B are constants
The WLF compares time dependent behavior of a polymer at two different
temperatures
𝐵@
af = expansion coefficient of the
𝑓0 𝑇 − 𝑇0
ln 𝑎 4 = −
free volume
𝑓0
@𝛼3 + 𝑇 − 𝑇0
f0 = fractional free volume at Tg
or other point of interest
• But 5@3* and 3*@6+ are constants, therefore;
𝑐! 𝑇 − 𝑇0
ln 𝑎 4 = −
𝑐" + 𝑇 − 𝑇0
To is the reference temperature
32
•

Williams-Landel-Ferry (WLF) equation

empirically:

Ts is a reference temperature and
c1 and c2 are constants.
With Ts=Tg, c1 = 17.5 and c2 =
52 C.
t is the time it takes to reach a
given stress level

“master curve” in an ideal case

Constructing a master curve
modified (rubber toughened) epoxy adhesive

Creep compliance (D instead of J here)

Polyisobutylene

Constructing a master curve

Example 2
Suppose we have data on a stress relaxation modulus vs. time for an amorphous
polymer (like chewing gum). Suppose that the polymer has a glass transition
temperate of Tg=100 °C. We measure a creep modulus of 150 GPa of 1 hour at 95 °C.
How much time would it take to achieve the same creep modulus at 90 °C?

With Ts=Tg, c1 = 17.5 and c2 = 52 C.
NOTE temperature
measured in °C

Example 2
Suppose we have data on a stress relaxation modulus vs. time for an
amorphous polymer (like chewing gum). Suppose that the polymer has a glass
transition temperate of Tg=100 °C. We measure a creep modulus of 150 GPa
of 1 hour at 95 °C. How much time would it take to achieve the same creep
modulus at 90 °C?

With Ts=Tg, c1 = 17.5 and c2 = 52 C.

For our problem:

…But, properties depends on temperature too

Boltzmann's principle of superposition states that, provided there is a linear
relationship between stress and strain and their time derivatives, then the strain
produced by any set of applied stresses is the sum of the strains produced by the
individuals of the set when acting alone.
38



## Metadata
- Source file: junk_drawer/Visco 3.pdf
- Extracted: 2026-05-18
- Category: other
