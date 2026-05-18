# 09_ChE312_MassTransferFundamentals.pdf

Source: junk_drawer/09_ChE312_MassTransferFundamentals.pdf

Category: [[academic-lecture]]

## Summary
ChE 312 – Transport Processes II III. Fundamentals of mass transfer. III.a. Basic concepts and equations: Diffusion, (bulk) Convection, Convective MT. • • • Mass transfer fundamentals. Flux vs flow. Fick’s Law.

## Full Content
ChE 312 – Transport Processes II
III. Fundamentals of mass transfer.
III.a. Basic concepts and equations: Diffusion, (bulk) Convection, Convective MT.
•
•
•

Mass transfer fundamentals.
Flux vs flow.
Fick’s Law.

III.b. Steady-state diffusion.
•
•

Equimolar counterdiffusion (“EMD”) vs. A through stagnant B (“UMD”, “unimolecular diffusion”).
Applications; HW08.

III.c. Diffusivities from data, correlation, and theory.
•
•
•
•

Diffusion coefficients ("diffusivities")
Transport properties from "Kinetic theory of gases" - T, P, & MW dependence.
How to measure diffusivities? And permeabilities?
Compare diffusivities and permeabilities.

© 2024, ChE 312-001 (PRW)

Fundamental definitions to remember !!!
• JA (diffusion flux) or vCA (convective flux) or NA (total flux), mass or moles /time per area
𝑑𝐶𝐴
𝑑𝑧

𝑞
𝑑𝑇
= −𝑘 ]
𝐴
𝑑𝑧

• Fick’s Law of Diffusion (1855):

𝐽𝐴 = −𝐷𝐴𝐵

• Bulk convection of species A:

𝑣𝐶𝐴

• Total flux 𝑁𝐴 :

𝑁𝐴 = 𝑣𝐶𝐴 + 𝐽𝐴

• [Convective MT to/from a surface:

𝑁𝐴,𝑐𝑜𝑛𝑣𝑒𝑐𝑡𝑖𝑣𝑒 = 𝑘 • 𝐶𝐴,𝑏𝑢𝑙𝑘 − 𝐶𝐴,𝑠𝑢𝑟𝑓𝑎𝑐𝑒 ]
z1

Fluid velocity v

© 2024, ChE 312-001 (PRW)

𝑏𝑖𝑛𝑎𝑟𝑦

=

𝑁𝐴 +𝑁𝐵
𝐶

𝐶𝐴 − 𝐷𝐴𝐵

𝑑𝐶𝐴
𝑑𝑧

z2

𝑁𝐴 = 𝑣𝐶𝐴 + 𝐽𝐴

Flux
area
CA1

[Like Fourier’s Law,

mol•s-1m-2
CA2

2

Where does 𝑁𝐴 = 𝐽𝐴 +

𝑁𝐴 +𝑁𝐵 +⋯ 𝐶𝐴
come from?
𝐶

• Total flux 𝑁𝐴 = Diffusion flux 𝐽𝐴 + Convective flux 𝑣𝐶𝐴
𝑁

𝑃

• Total concentration is 𝐶: density in mass/vol or mol/volume, like 𝐶 = 𝑉 = 𝑅𝑇
• Alternative form: First recognize 𝑁𝑡𝑜𝑡𝑎𝑙 = σ 𝑁𝑖 = σ 𝑣𝐶𝑖 = 𝑣 σ 𝐶𝑖 = 𝑣𝐶
– Then 𝑣 =

σ 𝑁𝑖
𝐶

so…

– Convective flux of A is 𝑣𝐶𝐴 =

– So 𝑁𝐴 = 𝐽𝐴 +

© 2024, ChE 312-001 (PRW)

σ 𝑁𝑖
𝐶

𝐶𝐴

𝑁𝐴 +𝑁𝐵 +⋯ 𝐶𝐴
𝐶

3

We will construct and use related forms of two reference cases.
Apply this idea: If 𝑁𝐴 and 𝑁𝐵 are related, integrate 𝑁𝐴 = 𝐽𝐴 +

𝑁𝐴 +𝑁𝐵
𝐶

1. Equimolar counterdiffusion: If 𝑁𝐵 = −𝑁𝐴 , then 𝑁𝐴 = 𝐽𝐴 +

𝐶𝐴 by simplifying
𝑁𝐴 +𝑁𝐵
𝐶

𝑁𝐴 +𝑁𝐵
.
𝐶

𝜕𝐶

𝐶𝐴 = −𝐷𝐴𝐵 𝜕𝑧𝐴

– How can that happen physically? e.g., If V↔L in distillation, or fast reaction A➔B at a surface.
[Note: If 2A➔B at a surface, then 𝑁𝐵 = −2𝑁𝐴 and then σ 𝑁𝐴 + 𝑁𝑏 = −𝑁𝐴 ]

– If 1D, constant 𝐷𝐴𝐵 , & steady-state, then integrate 𝑁𝐴 ‫ = 𝑧𝑑 ׬‬−𝐷𝐴𝐵 ‫ 𝐴𝐶𝑑 ׬‬and 𝑁𝐴 ∆𝑧 = −𝐷𝐴𝐵 ∆𝐶𝐴
– If 𝐶𝐴𝑜 at 𝑧1 and 𝐶𝐴2 at 𝑧2 , then 𝑁𝐴 𝑧2 − 𝑧1 = +𝐷𝐴𝐵 𝐶𝐴1 − 𝐶𝐴2
– Using ∆𝑥𝐴 = 𝐶 𝑥𝐴1 − 𝑥2 , then

𝑁𝐴 =

𝑫𝑨𝑩𝑪
∆𝒙𝑨
∆𝒛

2. Diffusion of A through stagnant B: If 𝑁𝐵 = 0, then 𝑁𝐴 = 𝐽𝐴 + 𝑁𝐴 𝐶𝐴 /𝐶
𝑑𝐶𝐴
𝑁 𝐶
𝑑𝑥
𝑑𝑥
+ 𝐴 𝐴 = −𝐷𝐴𝐵 𝐶 𝐴 + 𝑁𝐴 𝑥𝐴 or 1 − 𝑥𝐴 𝑁𝐴 = −𝐷𝐴𝐵 𝐶 𝐴
𝑑𝑧
𝐶
𝑑𝑧
𝑑𝑧
−𝑑𝑥𝐴
– Integrate 𝑁𝐴 𝑑𝑧 = 𝐷𝐴𝐵 𝐶
= 𝐷𝐴𝐵𝐶 ∙ d ln 1 − 𝑥𝐴 with
1−𝑥𝐴

– Then 𝑁𝐴 = −𝐷𝐴𝐵

– From 𝑁𝐴 =

𝐷𝐴𝐵𝐶
1−𝑥𝐴2
∙ ln
𝑧1 −𝑧2
1−𝑥𝐴1

© 2024, ChE 312-001 (PRW)

, we can get the usefully analogous form

𝑁𝐴 =

𝑫𝑨𝑩𝑪
∆𝒛∙ 𝒙𝑩 𝒍𝒐𝒈 𝒎𝒆𝒂𝒏

∆𝒙𝑨
4

Manipulate to get

∆𝒙𝑨
𝒙𝑩 𝒍𝒐𝒈 𝒎𝒆𝒂𝒏

for diffusion of A through non-diffusing B.

• Recap:

∙

• Use log-mean definition:

𝒙𝑨𝟐 − 𝒙𝑨𝟏
=
𝑥𝐴2 − 𝑥𝐴1

𝑓log 𝑚𝑒𝑎𝑛 ≡

𝐷𝐴𝐵 𝐶 ln 1 − 𝑥𝐴2 / 1 − 𝑥𝐴1
∙
𝑧2 − 𝑧1
1 − 𝑥𝐴2 − 1 − 𝑥𝐴1

𝒙𝑨𝟐 − 𝒙𝑨𝟏

𝑓2 − 𝑓1
𝑓2 − 𝑓1
=
ln 𝑓2 − ln 𝑓1 ln 𝑓2 /𝑓1

• To get correction term:

(1) Same form as 𝑁𝐴 = 𝑘𝑥 𝑥𝐴2 − 𝑥𝐴1
(2) Can use other variables like pi or CA etc.
© 2024, ChE 312-001 (PRW)

5

You can do useful things with these relations.
• Suppose you have a vulcanized rubber in a tire where diffusivities at 303K
are DO2,membrane=2.1E-8 m2/s and DN2,membrane=1.5E-8 m2/s
• You’re told that putting N2 in your tires will be better than O2. Is it because
there is less diffusive loss?
• 𝑁𝐴 =

𝐷𝐴𝐵
𝐷
1
∆𝐶𝐴 = 𝐴𝐵
∆𝑧
∆𝑧 𝑅𝑇

𝑃𝑖𝑛 𝑦𝑖𝑛 − 𝑃𝑜𝑢𝑡 𝑦𝑜𝑢𝑡

𝐷𝑁2,𝑚 50𝑝𝑠𝑖𝑎 1.00 − 15𝑝𝑠𝑖𝑎 0.79
𝑁𝑁2
=
𝐷𝑁2,𝑚 50 0.79 − 15 0.79 +𝐷𝑂2,𝑚 50 0.21 − 15 0.21
𝑁2 +𝑁𝑂2
𝟓𝟕.𝟐𝟐𝟓
𝟓𝟕.𝟐𝟐𝟓
=
= 𝟏. 𝟎𝟎𝟔
𝟒𝟏.𝟒𝟕𝟓+𝟏𝟓.𝟒𝟑𝟓
𝟓𝟔.𝟗𝟏𝟎

• Relative loss is 𝑁

=

• No loss-rate difference at 303 K; Different 𝐷 at high T? Oxidation by O2?
6

© 2024, ChE 312-001 (PRW)

6

Theory helps us correlate.
• How does diffusivity change:
– With T and P?
– With molecular weight?
– With phase: gas, liquid, solid?
• We have a good qualitative intuition.
• But gas correlation is based on theory (see book):
1.8583×10-7 T 3/2 æ 1
1 ö
DAB m 2 /s =
+
ç
÷
2
P × s AB
× WD,AB (T ) çè M A M B ÷ø

(

1/2

)

• Extended by correlation (vA & vB “specific volumes”; see book)
DAB ( m /s) =
2

© 2024, ChE 312-001 (PRW)

P

((

1.00 ×10-7 T 1.75

åu A

) (
1/3

+ åu B

) )

1/3 1/2

7



## Metadata
- Source file: junk_drawer/09_ChE312_MassTransferFundamentals.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
