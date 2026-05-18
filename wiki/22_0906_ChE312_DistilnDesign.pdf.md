# 22_0906_ChE312_DistilnDesign.pdf

Source: junk_drawer/22_0906_ChE312_DistilnDesign.pdf

Category: [[academic-lecture]]

## Summary
ChE 312 – Transport Processes II I. Equilibrium separations: Distillation. I.d. Getting real: Practical aspects of distillation.. • What can we do with this understanding? Lots! • Explore effects of specification changes. • 𝑅 → ∞ (total reflux) and 𝑅𝑚𝑖𝑛 and their usefulness as bounds. • Optimal 𝑅 vs 𝑅𝑚𝑖𝑛 : Economic analysis of utility costs. • Overall and tray efficiencies. • Determining column height; determining diameter by flooding analysis.

## Full Content
ChE 312 – Transport Processes II
I. Equilibrium separations: Distillation.

I.d. Getting real: Practical aspects of distillation..
• What can we do with this understanding? Lots!
• Explore effects of specification changes.
• 𝑅 → ∞ (total reflux) and 𝑅𝑚𝑖𝑛 and their usefulness as bounds.
• Optimal 𝑅 vs 𝑅𝑚𝑖𝑛 : Economic analysis of utility costs.
• Overall and tray efficiencies.
• Determining column height; determining diameter by flooding analysis.
• Remark on enthalpy-concentration analysis for 𝐿/𝑉 changes.
• Consider column configuration variations.
1

© 2022, ChE 312-001 (PRW)

With R, solve for equilibrium, then the balance; then equilibrium, then balance, …

Let’s design a column: N, R, nfeed.
q line for sat’d-liquid feed

Here is an
equilibrium graph,
or use αAB=2.485.

R=1.78
R/(R+1)=0.64

Need feed and
product specs:
xF=0.50, saturated
liquid;
xD=0.97 (variable?);
xW≤0.020

Reflux ratio 1.78
(but R&q or R&N or
q&N could be
design variables)

xD=0.97

15 stages: 14 trays
xF=0.50 plus a partial reboiler;
dependent on R, q,
and on using optimal
feed stage position
xW≤0.020
2

© 2022, ChE 312-001 (PRW)

Use
graphical
method
OR
stepwise
calcs.

xD=x0 =
x1 equil

y1

x2

y2

balance

x3

y3

x4

y4

x5

y5

x6

y6

x7

y7

x8

y8

x9

y9

x10

y10

x11

y11

x12

y12

x13

y13

x14

y14
2

Three key factors to note:
• A vaporization with a condenser (one equilibrium stage) can do a lot of
separation if relative volatility is high, but ...
• Countercurrent contacting is crucial for purification.
– One stream gets higher in concentration, one gets lower; maximize the gradient.

• A lot of heat/cooling and heat transfer is required.
– Working against entropy costs money.
– Compute the required cooling for condensing the vapor flow V1.
– Compute heating for a boil-up rate VN in the reboiler, plus heating feed to the
desired q state.

3

© 2022, ChE 312-001 (PRW)

3

Could you do it more precisely or different ways?
•
•
•
•
•
•
•

Could you start from the bottom and solve upwards?
Could you use a more exact equilibrium calculation?
Could you start from the top and the bottom and work to the feed stage?
Could you include a side-stream draw?
Could you calculate changes in L and V (and L/V) as you go?
Could you solve for multicomponent mixtures?
Could you include reaction from having a catalyst on one stage?

4

© 2022, ChE 312-001 (PRW)

4

1982 Eastman
Chemical Co.
patent by
Victor H.
Agreda (NCSU
BS '75, MS '77,
PhD '79)

© 2022, ChE 312-001 (PRW)

5

You can design multi-stage absorption/stripping.
•

A liquid stream and a gas stream with a third
component.

•

Suppose you have PFAS in a air stream and
want to trap it in a liquid solvent.
• Use yi,n and Vn for PFAS in the gas stream (feed).
• Use xi,n and Ln for PFAS in the solvent stream.

•

As before, apply the stage n subscript to the
streams leaving each stage, presumably in
equilibrium (maybe Henry’s Law yi,n = m xi,n).

•

Then, just as before: Successively apply
equilibrium relation, material balance,
equilibrium relation, material balance...

•

What is different? Not thermally driven!
6

© 2022, ChE 312-001 (PRW)

6

You can design multi-stage absorption/stripping.
•

A liquid stream and a gas stream with a third
component.

•

Suppose you have PFAS in a air stream and
want to trap it in a liquid solvent.
• Use yi,n and Vn for PFAS in the gas stream (feed).
• Use xi,n and Ln for PFAS in the solvent stream.

•

As before, apply the stage n subscript to the
streams leaving the stage, presumably in
equilibrium (maybe Henry’s Law yi,n = m xi,n).

•

Then, just as before: Successively apply
equilibrium relation, material balance,
equilibrium relation, material balance...

•

What is different? Not thermally driven!

PFAS Oxidizer and Scrubber,
Chemours Fayetteville Works

Usually not staged but continuous countercontacting, rate-limited by mass transfer.
7

© 2022, ChE 312-001 (PRW)

7

Could you design multi-stage extraction of an amino acid?

• Two liquid streams with a amino acid transferring from one phase to another:
•
•

Use “yi,n” and “Vn” for the solvent-rich “extract” stream (here, right to left).
Use xi,n and Ln for the feed-to-”raffinate” stream (here, left to right).

• As before, apply the stage n subscript to the streams leaving the stage, presumably in
equilibrium (γyAyA,n=γxAxA,n).
• Then, just as before: Successively apply equilibrium relation, material balance,
equilibrium relation, material balance...
• What is different?
8

© 2022, ChE 312-001 (PRW)

8

We can examine design sensitivities.
• Tighten or loosen
distillate and/or
bottoms specification.
• Change quality of feed
(𝑞) or its composition.

9

© 2022, ChE 312-001 (PRW)

9

We can examine design sensitivities.
• Dial reflux ratio up and down:
– “Total reflux” or 𝑅 → ∞ gives a lower bound for number of stages (minimum
number of stages).
– “Pinch point” determines 𝑅𝑚𝑖𝑛 (infinite number of stages required), determines
𝑅 (optimal number of stages, ~1.5 𝑅𝑚𝑖𝑛 )….>
“tangent pinch”

10

© 2022, ChE 312-001 (PRW)

10

We have
𝑳/𝑽 but
need actual
flowrates
to
determine
utilities
and
column
diameter.

How to get reflux
rate, L0?
Reflux Ratio*D
How to get
overhead vapor
rate, V1?
L0+D
How to get boil-up
rate, VN+1?
If R and q are set,
it must conform to
the Stripping
Section Operating
Line (the balance).

© 2022, ChE 312-001 (PRW)

W

11
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

11

How to get reflux
rate, L0?
Reflux Ratio*D
How to get
overhead vapor
rate, V1?
L0+D
How to get boil-up
rate, VN+1?
If R and q are set,
it must conform to
the Stripping
Section Operating
Line (the balance).
© 2022, ChE 312-001 (PRW)

W

12
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

12

How to get reflux
rate, L0?
Reflux Ratio*D
How to get
overhead vapor
rate, V1?
L0+D
How to get boil-up
rate, VN+1?
If R and q are set,
it must conform to
the Stripping
Section Operating
Line (the balance).
© 2022, ChE 312-001 (PRW)

W

13
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

13

How to get reflux
rate, L0?
Reflux Ratio*D
How to get
overhead vapor
rate, V1?
L0+D
How to get boil-up
rate, VN+1?
If R and q are set,
VN+1 must conform
to the Stripping
Section Operating
Line (the balance).
© 2022, ChE 312-001 (PRW)

W

14
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

14

Expensive capital (CAPEX), but utilities are expensive, too.

Here is
one case:

How to calculate
utilities costs?

15

© 2022, ChE 312-001 (PRW)

15

Utilities are the most expensive operating cost (OPEX).
Heat required for boil-up is
𝑉𝑁 ∙ 𝜆𝑊 = 𝑚ሶ 𝑠𝑡𝑒𝑎𝑚 𝜆𝑠𝑡𝑒𝑎𝑚 ,
and heat for heating the feed is
𝑞𝐹 ∙ 𝜆𝐹 = 𝑚ሶ 𝑠𝑡 𝜆𝑠𝑡𝑒𝑎𝑚
Cooling req’d for the condenser is
𝑉1 ∙ 𝜆1 = 𝐷 𝑅 + 1 𝜆1 =
𝑚ሶ 𝑐𝑤 𝐶𝑝,𝑐𝑤 𝑇𝑜 − 𝑇𝑖𝑛
Note:
1. If feed is sat’d liquid,
𝑄𝑟𝑒𝑏𝑜𝑖𝑙𝑒𝑟 ≅ 𝑄𝑐𝑜𝑛𝑑𝑒𝑛𝑠𝑒𝑟
2. For ideal solution,
𝜆𝑚𝑖𝑥 = 𝑥𝐴 𝜆𝐴 + 𝑥𝐵 𝜆𝐵
Here, optimal 𝑅 ≅ 1.25, divided
by 𝑅𝑚𝑖𝑛 ≅ 1.13, is 1.1
16

© 2022, ChE 312-001 (PRW)

16

Consider the numbers for C3H6/C3H8.
1.

Find the flow rate of vapor going through the distillate (𝑉1) and the flow rate of boil-up
(𝑉𝑁+1 ).
a.

𝑉1=2293+159 kmol/hr of ~propene (99%); ∆𝐻𝑣𝑎𝑝𝑛 ≅ 18.9 kJ/mol at 320 K (NIST Webbook )

b.

𝑉𝑁+1 =2575 kmol/hr of ~propane (95%); ∆𝐻𝑣𝑎𝑝𝑛 ≅ 18.7 kJ/mol at 330 K

Determine the enthalpy removed from the distillate and added to the reboiler, ሶ
𝑚𝜆.

2.
a.

3.

46•106 kJ/hr CW and 48•106 kJ/hr steam

Find the cooling water and steam required to complete the energy balance.
a.

𝑄𝑐𝑤 = 𝑚ሶ 𝑐 𝐶𝑝 ∆𝑇 so 𝑚ሶ 𝑐 =

b.

𝑄𝑠𝑡 = 𝑚ሶ 𝑠𝑡 𝜆𝐻2𝑂 so 𝑚ሶ 𝑠𝑡 =

4.

𝑄𝑐𝑤
𝐶𝑝 ∆𝑇
𝑄𝑠𝑡

𝜆𝐻2𝑂

=

=

46𝐸6 𝑘𝐽/ℎ
𝑘𝐽
𝑘𝑔•𝐾

4.2

50−20°𝐶

48𝐸6 𝑘𝐽/ℎ
2257

𝑘𝐽
𝑘𝑔

= 3.7𝐸5 𝑘𝑔/ℎ

= 21𝐸3 𝑘𝑔 𝑠𝑡𝑒𝑎𝑚/ℎ

Plug into a cost equation and find the cost required to run.
a.
b.

Estimate $3/1000 gal CW=$0.0008/kg so $290/h or $2.6 million/yr CW
Estimate $14/GJ steam “loaded cost” (fuel + generation) so $670/h or $6 million/yr steam
17

© 2022, ChE 312-001 (PRW)

17

Detailed designs show that 𝑅 (optimal number of stages) ≅ 1.5𝑅𝑚𝑖𝑛

18

© 2022, ChE 312-001 (PRW)

18

Fenske equation for stages: Useful and dangerous.
• Requires constant relative volatility; may be very wrong if nonideal mixtures.
• Requires total condenser and assumes optional feed location.

𝑋
1 − 𝑋𝑤
log 1 −𝐷𝑋
𝑋𝑤
𝐷
𝑁𝑚𝑖𝑛,𝐹𝑒𝑛𝑠𝑘𝑒 =
log 𝛼𝑎𝑣𝑒
where 𝛼𝑎𝑣𝑒 =

𝛼𝑡𝑜𝑝 𝛼𝑏𝑜𝑡𝑡𝑜𝑚𝑠

• In this class, assume you have to determine stages from balance equations
unless I tell you to use Fenske – or if you’re checking yourself.
19

© 2022, ChE 312-001 (PRW)

19



## Metadata
- Source file: junk_drawer/22_0906_ChE312_DistilnDesign.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
