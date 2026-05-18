# 04_ChE312_DistillationEquations.pdf

Source: junk_drawer/04_ChE312_DistillationEquations.pdf

Category: [[academic-lecture]]

## Summary
ChE 312 – Transport Processes II Distillation: Co-solving equilibrium relations with mass balances. Review PS03: Txy, Pxy, Semibatch distillation. Analysis and design of Continuous stagewise distillation. Overall balances. Coupling stagewise balances in the rectifying stages, feed stage, and stripping stages. McCabe-Thiele and “constant molar overflow.” •Use the McCabe-Thiele algorithm to find number of stages N and optimal feed-stage location. •Discuss how to calculate simple cases with spreads

## Full Content
ChE 312 – Transport Processes II
Distillation: Co-solving equilibrium relations with mass balances.
Review PS03: Txy, Pxy, Semibatch distillation.
Analysis and design of Continuous stagewise distillation.
Overall balances.
Coupling stagewise balances in the rectifying stages, feed stage, and stripping stages.
McCabe-Thiele and “constant molar overflow.”
•Use the McCabe-Thiele algorithm to find number of stages N and optimal feed-stage location.
•Discuss how to calculate simple cases with spreadsheets and a worked example.
•Illustrate with binary graphs.

© 2024, ChE 312-001 (PRW)

“Reflux ratio”=Reflux/D

Continuous
distillation is a
workhorse for
separations.

What steps to develop a
model for analysis or design?

How
Supply
heato
thru
feed
and reboiler;
analyze?
Supply coolant at
top to condense and
return part of the
liquid; Thus
countercurrent V-L
contacting.

(1)Overall material balance
(2)Component balance.
(3)Then single equilibrium stage.
(4)Then the stages together.
(5)Possibly energy balances.
“Boil-up rate” is set by
reboiler heating rate

View https://www.youtube.com/watch?v=I70jgRpf80o
© 2024, ChE 312-001 (PRW)

2
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

2

First step is to
calculate overall
balances.
Initially, only some
information is given,
such as feed rate &
composition and a
product specification
(purity or % recovery
of desired species)

© 2024, ChE 312-001 (PRW)

First balance: Total flows
𝐹 =𝐷+𝐵
2nd: Higher volatility species
𝑧𝐹 = 𝑥𝐷 𝐷 + 𝑥𝐵 𝐵
𝑧 is feed mole fraction.
𝑥𝐷 may be specified product;
If a “total condenser”, same as
the vapor from the top!
3
Fig. 1.16; Seader, Henley, and Roper, Separation Process Principles, 3rd Ed.

3

Then stagewise balances: Sketch a stage; label; write balances.

Stage n

© 2024, ChE 312-001 (PRW)

4

Then stagewise balances: Sketch a stage; label; write balances.
𝑉𝑛 , 𝑦𝑛
Stage n
𝐿𝑛 , 𝑥𝑛

• Standard convention: Streams leaving stage n have subscripts n.
• Key assumption: Streams Ln and Vn have reached equilibrium (“equilibrated).
• Number other streams from top or from bottom.
• We have to find the stage equilibrium compositions for all species, plus T and P.
• A classic approach is McCabe-Thiele analysis (like Theel’-ee).
© 2024, ChE 312-001 (PRW)

5

Then stagewise balances: Sketch a stage; label; write balances.
If numbering starts from 1 at the top:
𝐿𝑛−1 , 𝑥𝑛−1

𝑉𝑛 , 𝑦𝑛
Stage n
𝑉𝑛+1 , 𝑦𝑛+1

𝐿𝑛 , 𝑥𝑛

• Standard convention: Streams leaving stage n have subscripts n.
• Key assumption: Streams Ln and Vn have reached equilibrium (“equilibrated”).
• Number other streams from top or from bottom.
• We have to find the stage equilibrium compositions for all species, plus T and P.
• A classic approach is McCabe-Thiele analysis (like Theel’-ee).
© 2024, ChE 312-001 (PRW)

6

How to proceed?
Solve all stages at once?
• Instead, start from an end where you
know the flowrate and mole fraction.
• Given the purity 𝑥𝐷 of distillate, what is
the composition of reflux?
– They are the same!

• For a total condenser, what is the
composition 𝑦1 , the overhead vapor?
– The same as 𝑥𝐷 !

• Given a distillate product rate 𝐷 and reflux
ratio “𝐿0 ”/𝐷, what is 𝐿0 ? It’s 𝐷 ∙ 𝐿0 /𝐷
• And what is 𝑥1 ? Equilibrium with 𝑦1 !
• Then sequentially solve from the top...
7

© 2024, ChE 312-001 (PRW)

7

Key to the algorithm: Start with the top stage.
D , xD=x0

If you know xD ,
then you know y1 and x0.

V1 , y1

L0 , x0
Stage 1

V2 , y2

L1 , x1
Stage 2

V3 , y3

L2 , x2

Vn , yn

then you know x1 from 𝜙𝑖 𝑦𝑖 𝑃 =
𝛾𝑖 𝑥𝑖 𝑃𝑣𝑎𝑝,𝑖 .

Ln-1 , xn-1

If you compose balances from the
column end (D , xD) to the stage exit
AND you know D and L1 (or L1 / V2),

Ln , xn

then you know y2 from a mass balance.

Stage n

Vn+1 , yn+1

If you know y1 ,and the top stage
is equilibrated,

8

© 2024, ChE 312-001 (PRW)

8

Analyze a balance above the top stage.
D , xD=x0

V1 , y1

L0 , x0
Stage 1

V2 , y2

L1 , x1
Stage 2

V3 , y3

L2 , x2

Vn , yn

Ln-1 , xn-1

𝑉1 = 𝐿0 + 𝐷
𝑉1 𝐿0
=
+1=𝑅+1
𝐷
𝐷
𝐷
1
𝐷 /𝐿0
1/𝑅
=
=
=
𝑉1 𝑅 + 1 𝑉1 /𝐿0 𝑉1 /𝐿0

𝐿0
𝑅
=
𝑉1 𝑅 + 1

Stage n

Vn+1 , yn+1

Ln , xn
9

© 2024, ChE 312-001 (PRW)

9

Analyze balances from the top thru stage n of the enriching section:
D , xD=x0
V1 , y1

L0 , x0

𝑉𝑛+1 𝑦𝑛+1 = 𝐿𝑛 𝑥𝑛 + 𝐷𝑥𝐷
Divide by 𝑉𝑛+1 to get an almost linear eqn:

Stage 1

V2 , y2

L1 , x1

𝐿

If 𝑉 𝑛 is constant (“equimolar overflow”), then
𝑛+1

Stage 2

V3 , y3

𝐿𝑛
𝐷𝑥𝐷
𝑥𝑛 +
𝑉𝑛+1
𝑉𝑛+1

𝑦𝑛+1 =

L2 , x2

𝒚𝒏+𝟏 =

𝑳
𝑽

𝒙𝒏 +

𝑫𝒙𝑫
𝑽

is linear!!!!

This balance =“enriching-section operating line.”
Vn , yn

Ln-1 , xn-1
Stage n

Vn+1 , yn+1

Ln , xn

Because 𝑅 = 𝐿0 /𝐷 and
𝒚𝒏+𝟏 =

𝐿
𝐿
𝑅
= 0=
:
𝑉
𝑉1
𝑅+1

𝑹
𝒙𝑫
𝒙𝒏 +
𝑹+𝟏
𝑹+𝟏
10

© 2024, ChE 312-001 (PRW)

10

Now analyze the enriching section stepwise:
D , xD=x0
V1 , y1

L0 , x0
Stage 1

V2 , y2

You have 𝑦1 , so now get 𝑥1 from equilibrium!
If a binary, graph the 𝑦 𝑣𝑠 𝑥 data and read 𝑥1 ;
𝑦𝑛
Use 𝑥𝑛 =
if it is valid.
𝛼+ 1−𝛼 𝑦𝑛

With 𝑥1 , 𝒚𝟐 = 𝒚𝒏+𝟏 =

L1 , x1

y1
y2

Stage 2

V3 , y3

𝑹
𝒙
𝒙𝒏 + 𝑫
𝑹+𝟏
𝑹+𝟏

y3

L2 , x2

Each step
to a new
𝑦𝑛 counts
as a
stage.

Phase
eq.

yn
Vn , yn

, and …

Ln-1 , xn-1
Stage n

Vn+1 , yn+1
© 2024, ChE 312-001 (PRW)

Ln , xn

x3

x11n

x2

x1 x0
11

At the feed stage, three balance equations must be satisfied.
• Three relations must intersect:
– Enriching-section mole balance (“OL”) 𝑉𝑦 = 𝐿𝑥 + 𝐷𝑥𝐷 ;
ത = 𝐿ത 𝑥 − 𝐵𝑥𝐵
– Stripping-section mole balance (“OL”) 𝑉𝑦
(where 𝐿ത = 𝐿 + 𝐿𝐹 and 𝑉ത = 𝑉 − 𝑉𝐹 are stripping-section flowrates);
– And the feed’s energy balance: its “q line”: 𝑦𝑞 =

© 2024, ChE 312-001 (PRW)

𝑞
1
𝑥−
𝑥
𝑞−1
𝑞−1 𝐹

𝑉𝑓 , 𝑦𝑓

𝐹, 𝑧𝐹
𝑉ത𝑓+1 , 𝑦𝑓+1

(𝑉, 𝐿)

𝐿𝑓−1 , 𝑥𝑓−1

Stage n

ത 𝐿ത )
(𝑉,

𝐿ത𝑓 , 𝑥𝑓

At the feed stage, three balance equations must be satisfied.
• Three relations must intersect:
– Enriching-section mole balance (“OL”) 𝑉𝑦 = 𝐿𝑥 + 𝐷𝑥𝐷 ;
ത = 𝐿ത 𝑥 − 𝐵𝑥𝐵
– Stripping-section mole balance (“OL”) 𝑉𝑦
(where 𝐿ത = 𝐿 + 𝐿𝐹 and 𝑉ത = 𝑉 − 𝑉𝐹 are stripping-section flowrates);
– And the feed’s energy balance: its “q line”: 𝑦𝑞 =

𝑞
1
𝑥−
𝑥
𝑞−1
𝑞−1 𝐹

• The q line is obtained by co-solving the OL equations with
– A feed-stage mole balance 𝐹 + 𝑉ത + 𝐿 = 𝑉 + 𝐿ത
– An overall mole balance 𝐹𝑧𝐹 = 𝐷𝑥𝐷 + 𝐵𝑥𝐵
– And defining “feed quality” 𝑞:
increase in molar liq rate across the feed stage 𝐿ത − 𝐿
𝑉 − 𝑉ത
𝑞≡
=
=1+
total molar feed rate
𝐹
𝐹

• It is equivalent by an enthalpy balance to:
𝑞=

ℎ𝑒𝑎𝑡 𝑡𝑜 𝑡𝑢𝑟𝑛 𝑓𝑒𝑒𝑑 𝑖𝑛𝑡𝑜 𝑠𝑎𝑡’𝑑 𝑣𝑎𝑝𝑜𝑟 𝐻𝑉 − 𝐻𝐹
=
ℎ𝑒𝑎𝑡 𝑡𝑜 𝑡𝑢𝑟𝑛 𝑠𝑎𝑡’𝑑 𝑙𝑖𝑞 −> 𝑠𝑎𝑡’𝑑 𝑣𝑎𝑝 𝐻𝑉 − 𝐻𝐿

© 2024, ChE 312-001 (PRW)

𝑉𝑓 , 𝑦𝑓

𝐹, 𝑧𝐹
𝑉ത𝑓+1 , 𝑦𝑓+1

(𝑉, 𝐿)

𝐿𝑓−1 , 𝑥𝑓−1

Stage n

ത 𝐿ത )
(𝑉,

𝐿ത𝑓 , 𝑥𝑓

At the feed stage, three balance equations must be satisfied.
• Three relations must intersect:
– Enriching-section mole balance (“OL”) 𝑉𝑦 = 𝐿𝑥 + 𝐷𝑥𝐷 ;
ത = 𝐿ത 𝑥 − 𝐵𝑥𝐵
– Stripping-section mole balance (“OL”) 𝑉𝑦
(where 𝐿ത = 𝐿 + 𝐿𝐹 and 𝑉ത = 𝑉 − 𝑉𝐹 are stripping-section flowrates);
– And the “q line”: 𝑦𝑞 =

𝑞
1
𝑥−
𝑥
𝑞−1
𝑞−1 𝐹

𝑉𝑓 , 𝑦𝑓

𝐹, 𝑧𝐹

– A feed-stage mole balance 𝐹 + 𝑉ത + 𝐿 = 𝑉 + 𝐿ത
– An overall mole balance 𝐹𝑧𝐹 = 𝐷𝑥𝐷 + 𝐵𝑥𝐵
– And defining “feed quality” 𝑞:
increase in molar liq rate across the feed stage 𝐿ത − 𝐿
𝑉 − 𝑉ത
𝑞≡
=
=1+
total molar feed rate
𝐹
𝐹

𝐿𝑓−1 , 𝑥𝑓−1

Stage n

𝑉ത𝑓+1 , 𝑦𝑓+1
y1
y2

• The q line is obtained by co-solving the OL equations with

(𝑉, 𝐿)

y3

ത 𝐿ത )
(𝑉,

𝐿ത𝑓 , 𝑥𝑓

𝑞 =0.5

yn

• It is equivalent by an enthalpy balance to:
𝑞=

ℎ𝑒𝑎𝑡 𝑡𝑜 𝑡𝑢𝑟𝑛 𝑓𝑒𝑒𝑑 𝑖𝑛𝑡𝑜 𝑠𝑎𝑡’𝑑 𝑣𝑎𝑝𝑜𝑟 𝐻𝑉 − 𝐻𝐹
=
ℎ𝑒𝑎𝑡 𝑡𝑜 𝑡𝑢𝑟𝑛 𝑠𝑎𝑡’𝑑 𝑙𝑖𝑞 −> 𝑠𝑎𝑡’𝑑 𝑣𝑎𝑝 𝐻𝑉 − 𝐻𝐿

xF

xn
© 2024, ChE 312-001 (PRW)

x2

x1 x0

At the feed stage, three balance equations must be satisfied.
• Must satisfy:
– Enriching-section OL equation;
– Stripping-section OL equation;
– A feed-stage energy balance.

Vf , yf
F, xF

𝑞=

y1
y2
y3

𝐿ത − 𝐿
𝑉 − 𝑉ത
=1+
𝐹
𝐹

(where 𝐿ത and 𝑉ത are stripping-section flowrates)
= relative heat to turn feed into saturated vapor
𝑞=

yn

xF

𝑞
1
𝑦𝑞 =
𝑥−
𝑥
𝑞−1
𝑞−1 𝐹
15

© 2024, ChE 312-001 (PRW)

(V,L)

Lf , xf

𝑞 =0.5

𝐻𝑉 − 𝐻𝐹
𝐻𝑉 − 𝐻𝐿

• Balance gives “q-line”:

Lf-1 , xf-1

Stage n

Vf+1 ,yf+1

• Define “feed quality” 𝑞 as
(increase in molar liquid rate across the feed stage)
(molar feed rate)

(V,L)

xn

x2

x1 x0

Similarly to ER, solve balances for the stripping-section OL eqn.
Balance 𝐿ത 𝑛 𝑥𝑛 = 𝑉ത𝑛+1 𝑦𝑛+1 + 𝑊𝑥𝑊
ഥ
𝑉

Vn , yn

Ln-1 , xn-1
Stage n (Stripping)

Vn+1 , yn+1

Ln , xn

Define boil-up ratio 𝑠 = 𝑁 , so:
𝑊
ത𝑳𝒏
𝑾𝒙𝑾 𝒔 + 𝟏
𝒙𝑾
𝒚𝒏+𝟏 =
𝒙 −
=
𝒙𝒏 −
ഥ 𝒏+𝟏 𝒏 𝑽
ഥ 𝒏+𝟏
𝒔
𝒔
𝑽
y1
y2
y3

VN , yN

LN-1 , xN-1
N (partial reboiler)

LN =W, xN=xW

y4

y5
zF
xW x4

© 2024, ChE 312-001 (PRW)

x3

x2

x1 x0

Summary of McCabe-Thiele equations
𝑳

• Enriching-section OL equation: 𝒚𝒏+𝟏 = 𝑽 𝒙𝒏 +
the reflux ratio = (reflux rate) / (distillate rate)

• Feed-stage “q-line”: 𝑦 =

𝑞
1
𝑥−
𝑥
𝑞−1
𝑞−1 𝐹

𝑫𝒙𝑫
𝑽

𝑹

= 𝑹+𝟏 𝒙𝒏 +

𝒙𝑫
𝑹+𝟏

where 𝑹 is

where 𝑞 is the heat needed to raise feed to

a saturated vapor relative to the latent heat needed to raise saturated liquid to
saturated vapor.
𝑳ത
𝑽𝒏+𝟏

𝑾𝒙
𝑽𝒏+𝟏

• Stripping-section OL equation: 𝒚𝒏+𝟏 = ഥ 𝒏 𝒙𝒏 − ഥ 𝑾 =
boil-up ratio = (boil-up rate) / (bottoms rate)
• Solve with equilibrium 𝑦 vs 𝑥 from data or (e.g.) yA =

𝒔+𝟏
𝒙
𝒙𝒏 − 𝑾 where 𝒔 is the
𝒔
𝒔

a AB x A
1+ (a AB -1)x A
yA =

yA
yA + a AB (1- yA )

ax A
+ bx A (1- x A )
1+ (a -1)x A
17

© 2024, ChE 312-001 (PRW)

xA =

End of slides for class 4, Thu Jan 18

© 2024, ChE 312-001 (PRW)

“Constant molar overflow” (CMO) is an approximation.
• We’re assuming:
– L & V within the enriching section don’t change from stage to stage;
ഥ (or L´ & V´) within the stripping section don’t change from stage to stage.
– 𝑳ത & 𝑽

• That requires the rates of molecules evaporating and condensing must be identical
on each stage (“equimolar overflow”).
• That is if heats of vaporization of the components are the same.
– More subtly, there can’t be any nonideal heats of vaporization of the mixture.

• CMO is often a pretty good assumption.
ഥ for more detailed energy-balance
– If not, we can calculate the changes in L & V and ത𝑳 & 𝑽
calculations.

© 2024, ChE 312-001 (PRW)

Classically illustrate McCabe-Thiele with graphs,
but it’s really the equations & algorithm.
Here is an
equilibrium
graph; or use
αAB=2.485.
Q: What else
do you need
to design a
column?

© 2024, ChE 312-001 (PRW)

Let’s design a column: N, R, nfeed.
Here is an
equilibrium
graph; or use
αAB=2.485.
Need feed
and product
specs, e.g.:
xF=0.50 as
saturated
liquid;
xD=0.97;
xW≤0.020
© 2024, ChE 312-001 (PRW)

Q: Use
graphical
method
OR
stepwise
calcs
to
determine
N stages, R
reflux
ratio, and
optimal
feed stage
location.

Design column (N, R, nfeed ) based on “Minimum Reflux Ratio.”
Here is an
equilibrium
graph; or use
αAB=2.485.
Need feed
and product
specs, e.g.:
xF=0.50 as
saturated
liquid;
xD=0.97;
xW≤0.020
© 2024, ChE 312-001 (PRW)

Use
graphical
method
OR
stepwise
calcs.
xD=0.97

xF=0.50

xW≤0.020

New aspect for
designing: What is the
best R to use?
Base it on Rmin , found
from the enrichingsection OL slope that
touches the
equilibrium curve at
or before the q line.

Need to find minimum reflux ratio Rmin to estimate optimum R.

Design column (N, R, nfeed ) based on “Minimum Reflux Ratio.”
q line for sat’d-liquid feed

Here is an
equilibrium
graph; or use
αAB=2.485.
Need feed
and product
specs, e.g.:
xF=0.50 as
saturated
liquid;
xD=0.97;
xW≤0.020
© 2024, ChE 312-001 (PRW)

Use
graphical
method
OR
stepwise
calcs.

Slope Rmin/(Rmin+1)
=(0.97-0.715)/(0.97-0.50)
=0.54 => Rmin=1.19
R=1.5Rmin=1.79
=>R/(R+1)=0.64
xD=0.97

xF=0.50

xW≤0.020

Q: What steps to follow?
• Use q line equation and (xD,xD) to get Rmin.
• Rmin => R => eqn for enriching-section operating line =>
eqn for stripping-section operating line.
• Solve equilibrium, then mass balance, then equilibrium,
then mass balance, … stepping over the feed stage and
past the bottoms spec.
• Number of complete steps = total number of
equilibrium stages = N trays + reboiler.

© 2024, ChE 312-001 (PRW)

Q: What equations?
• q line:

æ q ö æ xF ö
H - HF
y =ç
÷x -ç
÷ where q º V
HV - H L
è q -1 ø è q -1 ø

• Enriching-section operating line (Constant molar overflow!):
æ Ln ö
æ DxD ö
æ R ö
æ xD ö
yn+1 = ç
÷ xn + ç
÷ = ç
÷ xn + ç
÷
è
ø
è
ø
V
V
R
+1
R
+1
è n+1 ø
è n+1 ø

• Stripping-section operating line (Constant molar overflow!):
æ Lm ö
æ WxW ö
ym+1 = ç
÷ xn + ç
÷
V
V
è m+1 ø
è m+1 ø

© 2024, ChE 312-001 (PRW)

With R, solve for equilibrium, then the balance; then equilibrium, then balance, …

Let’s design a column: N, R, nfeed.
q line for sat’d-liquid feed

Here is an
equilibrium
graph; or use
αAB=2.485.
Need feed
and product
specs:
xF=0.50,
saturated
liquid;
xD=0.97;
xW≤0.020
© 2024, ChE 312-001 (PRW)

R/(R+1)=0.64

Use
graphical
method
OR
stepwise
calcs.

xD=0.97

xW≤0.020

15 stages: 14 trays
plus a partial
xF=0.50 reboiler;
dependent on R, q,
and on feed stage
position

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

• Ideal equilibrium: Data or
– Or empirical fit (non-ideal):

• q line:

yA =

a AB x A
1+ (a AB -1)x A
yA =

xA =

yA
yA + a AB (1- yA )

ax A
+ bx A (1- x A )
1+ (a -1)x A

æ q ö æ xF ö
HV - H F
y =ç
x
where
q
º
÷ ç
÷
HV - H L
è q -1 ø è q -1 ø

• Enriching-section operating line (Constant molar overflow):
æL ö
æ Dx ö
æ x ö
æ R ö
n
yn+1 = çç
x
+
÷÷ xn + çç D ÷÷ = ç
÷ n ç D ÷
è R +1ø
è R +1ø
èVn+1 ø
è Vn+1 ø

• Stripping-section operating line (Constant molar overflow):
æL ö
æ Wx ö
æx ö
æ s +1ö
Boil-up rate or VN +1
ym+1 = çç m ÷÷ xm - çç W ÷÷ = ç
÷ xm - ç W ÷ where s =
W
è s ø
è s ø
èVm+1 ø
è Vm+1 ø

© 2024, ChE 312-001 (PRW)

27



## Metadata
- Source file: junk_drawer/04_ChE312_DistillationEquations.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
