# Visco 2.pdf

Source: junk_drawer/Visco 2.pdf

Category: [[other]]

## Summary
Viscoelasticity • Mechanical behavior of polymers to applied stress or strain depends on rate or time period of loading • Elastic materials – at low strain-rate, obey Hooke’s law i.e. s = Ee

## Full Content
Viscoelasticity
•

Mechanical behavior of polymers to applied stress or strain depends on rate
or time period of loading

•

Elastic materials – at low strain-rate, obey Hooke’s law
i.e. s = Ee

•

Viscous liquids – at low strain-rate, obey Newton’s law
i.e. s =h de/dt

•

Most polymers are in between viscous liquids and elastic materials
(viscoelastic)

•

Viscoelasticity is highly dependent on temperature.
why (molecular level)?
1

Viscoelasticity
• What happens when weight is suspended on a polymer
filament?
• Strain increases over time due to stress-induced molecular
rearrangement in the solid. Upon release, the molecules
slowly recover to original state
• This is called creep – a manifestation of viscoelasticity.
• How then can we use polymers in engineering?
• Polymers do not creep indefinitely and they fully recover on
removing the stress
• Thus time is important in the use of polymer as an engineering
material.
2

Viscoelastic responses:
creep

3

Viscoelastic responses:
relaxation

4

Viscoelastic responses:
constant stress-rate

5

Viscoelastic responses:
constant stress-rate

6

How long does it take for 1 drop of
pitch to form & release?

GROUP ACTIVITY!

Extremes of viscoelasticity: pitch
• Pitch: extremely viscous (polymer)
• Produced through distillation of carbonaceous
materials
• Rosin: derive from plants (usually pine trees)
• Bitumen/asphalt: derive from petroleum

https://en.wikipedia.org/wiki/Pitch_drop_experiment
https://vimeo.com/event/4721898

8

Isostress

• Imagine parallel slabs of material

between platens that apply a load.

• Phase A has volume fraction V and
A

modulus EA; Phase B has volume
fraction VB and modulus EB.

Phase A

• What is the composite modulus, E ?
• We assume isostress because each
C

phase sees the same stress
(assuming same cross-sectional
area).

• The stress, σ = σ , is therefore the
C

field and the strain is the response
(and the compliance is the property).

Phase B

Isostrain

• Imagine parallel slabs of material between
platens that apply a load.

• Phase A has volume fraction V and
A

modulus EA; Phase B has volume fraction
VB and modulus EB.

• What is the composite modulus, E ?
• We assume isostrain because each phase
C

sees the same change in length.

• The strain, ε= ε , is therefore the field and
c

the stress is the response (and the
stiffness is the property).

Phase A
Phase B

Molecular basis stress relaxation
•

Chain Scission: breakage of polymeric
chains – reduces mechanical strength
but increases the elongation during
creep

•

Bond interchanges: chains exchange
bonds leading to chain re-organization
• Common in polysiloxanes and
polyesters

13

• Molecular relaxation: energy dissipation
through molecular vibrations (energy
dissipation)
• Thirion relaxation: entangled chains slip
reversibly over each other
• Specific to cross-linked polymers
• Viscous flow: polymer chains slip past
each other under flow.
• Permanent
• More prominent in linear polymers

But how can we model/understand relaxation and creep?
• Two approaches: stress relaxation or strain relaxation
14

Understanding stress relaxation & creep
Maxwell model (isostress)
•

Dashpot: a mechanical device that resists motion
through viscous friction e.g. used in hydraulic doors
• The mechanical behavior is described as;
𝝈=𝜼

•

𝒅𝜺
= 𝜼𝜺̇
𝒅𝒕

Spring: Elastic behavior follows Hooke’s law,
response to stress is;
𝝈 = 𝑬𝜺

•

Maxwell model places a spring and dashpot in series.
Stress is same across the assembly, but strain is
different, hence;
𝒅𝜺 𝒅𝜺 𝒅𝜺𝟏 𝟏 𝒅𝝈 𝝈
=
+
=
+
𝒅𝒕 𝒅𝒕
𝒅𝒕
𝑬 𝒅𝒕 𝜼

15

Understanding stress relaxation & creep
Maxwell model
•

Creep = constant stress:
𝜎 = 𝜎!
𝑑𝜎
=0
𝑑𝑡

Therefore

𝑑𝑒 𝜎!
=
𝑑𝑡
𝜂

16

Understanding stress relaxation & creep
Maxwell model
•

Stress relaxation = constant strain
𝑒 = 𝑒"
𝑑𝑒 1 𝑑𝜎 𝜎
=
+ =0
𝑑𝑡 𝐸 𝑑𝑡 𝜂

•

Then;

! #$
" #%

=−

$
&

=>

𝜎 = 𝜎" 𝑒

#$
$

"

= − 𝑑𝑡
&

# %$& '

17

Stress relaxation & creep: Maxwell model
•
•

Can we estimate the relaxation time?
Will the stress eventually dissipate and system relaxes back?

•

Relaxation time, t, is defined by;
𝜂
𝜏=
𝐸
Hence;

•

becomes

𝜎 = 𝜎" 𝑒

# %$& '
'

𝜎 = 𝜎" 𝑒 # $(

18

Stress relaxation & creep
Kelvin/Voigt Model (isostrain)
Creep
• Strain is the same on each element, but stress is
different
•

At constant load;

•

Hence;

•

Similarly, solving this equation gives us;
𝜀=

𝑑𝜀 𝜎 𝐸𝜀
= −
𝑑𝑡 𝜂
𝜂
𝑑𝜀 𝐸𝜀 𝜎)
+
=
𝑑𝑡
𝜂
𝜂

𝜎"
𝐸

1−𝑒

$%&#
'

=

𝜎"
𝐸

1−𝑒

$&#
(

19

Stress relaxation & creep
Kelvin/Voigt Model (isostrain)
Stress relaxation
• Strain is the same on each element, but stress is
different
•

At constant strain:
𝑑𝑒
=0
𝑑𝑡

•

Hence;

𝜎 𝐸𝑒"
=
𝜂
𝜂
and
𝜎 = 𝐸𝑒"
20

Comments
Neither the Maxwell or Kelvin-Voigt
models work perfectly.
One works for creep and one for
stress relaxation.
More complex models can be
constructed based on various
combinations of springs and dashpots.

a 4-element model

This is a standard way of building
accurate models of viscoelasticity.

22

Stress relaxation & creep
Burgers Model
• Four element models –combination of Maxwell and Kelvin models
• At t = 0, 𝜀 = 𝜎/𝐸* - deforms right away and is first element to relax.
,
Δ𝑡 – this is non-recoverable strain
&!

•

Also, 𝜀+ = ̇𝜀Δ𝑡 =

•
•

Strain on the Kelvin elements is; 𝜀- = 𝜀 − (𝜀* + 𝜀+ )
Hence, overall strain can be expressed as;
𝜀=

𝜎
𝜎
𝜎
'
+
1 − 𝑒 # $(" + 𝑡
𝐸* 𝐸𝜂+

24

Example 1: Velveeta® cheese

Examinable

Researchers made measurements on Velveeta®
cheese:
• 15 cm block with dimensions 4x6 cm
• compressive load of 4.9 N for 2 hours
• height of block measured every 5 minutes
• a second experiment used a load of 6.85 N
• the data are the symbols:

from Chang et al., J. Chem Ed. 63, 1077 (1986).

25

Example 1: Velveeta® cheese

•

at long times,

•

the slope at long times yields the viscosity η3

•

at t=0,

Examinable

yielding E1

26

from Chang et al., J. Chem Ed. 63, 1077 (1986).

Example 1: Velveeta® cheese

•

they measured the total strain, and can
determine the strain of the spring with modulus
E1 from

•

the strain of the bottom dashpot is

•

the strain for the Voigt structure is

•

E2 and

•

thus, have all the parameters

Examinable

can be found by curve fitting

27

from Chang et al., J. Chem Ed. 63, 1077 (1986).

Example 1: Velveeta® cheese

Examinable

lines are fit to data with the model

28

from Chang et al., J. Chem Ed. 63, 1077 (1986).

Viscoelasticity
•
•

If a constant shear stress, s1, is applied to a
viscoelastic material over time, t, strain, e1,
evolves as shown in (a)
Hence at an arbitrary time, t, the strains at
the two stresses are e1(t) and e2(t), then;
ε1(t) ε2(t)
=
𝜎*
𝜎-

Constant stressing rate

Constant straining rate

30

Viscoelasticity
•
•

If a constant shear stress, s1 or s2, is applied
to a viscoelastic material over time, t, strain,
e1 (i.e. g1) evolves as shown in (a)
Hence at an arbitrary time, t, the strains at
the two stresses are e1(t) and e2(t), then;
ε1(t) ε2(t)
=
𝜎*
𝜎-

•

Strain in the two experiments are
proportional to imposed stress. Hence creep
compliance at time t can be defined as;
. (t)
. (t)
𝐽 𝑡 = 1 = 2
,#

in general,

𝐽 𝑡 =

,"

. (t)
,

31

Chpt 20

Boltzmann Superposition Principle

•

Helps determine state of stress or strain in viscoelastic materials from
knowledge of the materials deformation history

•

For varying stress, overall deformation is related to the sum of strains due
to each stress step.

32

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
𝐽 𝑡 = /(')⁄,,
which is only a function of time
then for each loading,
𝜀 𝑡 = ∆𝜎𝐽(𝑡 − 𝜏)

•

With further stressing we get;
𝜀 𝑡 = 𝜀* 𝑡 + 𝜀- 𝑡 + 𝜀+ 𝑡 +. .
= ∆𝜎* 𝐽 𝑡 − 𝜏* + ∆𝜎- 𝐽 𝑡 − 𝜏- +. .
2

= @ 𝐽 𝑡 − 𝜏 ∆𝜎2
23"

33

Boltzmann Superposition Principle
•

We have seen that overall deformation (strain) is given by;
2

𝜀 𝑡 = @ 𝐽 𝑡 − 𝜏 ∆𝜎2
23"

•

Which can be represented as an integral (-∞ to t =all deformation history);
'

𝜀 𝑡 = B 𝐽 𝑡 − 𝜏 𝑑𝜎(𝑡)
#4

•

This equation can be express in terms of relaxation time, t;
'

𝑑𝜎(𝜏)
𝜀 𝑡 = B 𝐽(𝑡 − 𝜏)
𝑑𝜏
𝑑𝜏
•

#4

Predicts overall strain
After stressing the sample

35

Stress relaxation & creep
Kelvin Model
• At constant load;
𝑑𝜀 𝜎 𝐸𝜀
= −
𝑑𝑡 𝜂
𝜂
•

But if the load is then removed (s = 0) after
straining the system, then;
𝑑𝜀 𝐸𝜀
𝑑𝜀 𝐸
=
⇒
= 𝑑𝑡
𝑑𝑡
𝜂
𝜀
𝜂

•

Therefore;

%'$
&

𝜀 = 𝜀) 𝑒 #
•

Since 𝜏 = 𝜂/𝐸 ; then;
#𝒕
𝜺 = 𝜺𝒐𝒆 $𝝉

•

Therefore, this model only explains strain
relaxation and is useful in explaining creep (strain
relaxation)

36

Chpt 20

Boltzmann Superposition Principle:
Recovery
𝑒* = 𝜎" 𝐽(𝑡)
𝑒- = −𝜎" 𝐽 𝑡 − 𝑡*
𝑒 𝑡 = 𝜎" 𝑡 − 𝜎" 𝑡 − 𝑡*

𝑒 8 𝑡 − 𝑡* = 𝜎" 𝐽 𝑡 − 𝑡*

37

Boltzmann Superposition Principle
•

We can also consider stress relaxation the same way:
𝜎 𝑡
𝐺 𝑡 =
𝜀

•

If we consider the stress relaxation modulus, then;
𝜎 𝑡 = 𝐺 𝑡 𝜀 = ∆𝜀* 𝐺 𝑡 − 𝜏* + ∆𝜀- 𝐺 𝑡 − 𝜏- +. .

•

This is analogous to what we saw above, hence;
'

𝑑𝜀(𝜏)
𝜎 𝑡 = B 𝐺(𝑡 − 𝜏)
𝑑𝜏
𝑑𝜏

Predicts overall stress
After straining the sample

#4

38



## Metadata
- Source file: junk_drawer/Visco 2.pdf
- Extracted: 2026-05-18
- Category: other
