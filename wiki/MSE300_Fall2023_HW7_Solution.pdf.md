# MSE300_Fall2023_HW7_Solution.pdf

Source: junk_drawer/MSE300_Fall2023_HW7_Solution.pdf

Category: [[academic-homework]]

## Summary
MSE300 Homework 7 - Solution Q1) Structure factor and intensity calculations (30 pts) (a) Calculate the structure factor of a cubic F crystal with a single atom basis and identify its systematic absences. Solution: There are four lattice points per unit cell in a cubic F: (0,0,0), (1/2,1/2,0), (0,1/2,1/2), (1/2,0,1/2). These four sites are occupied by four atoms (N=4) of the

## Full Content
MSE300

Homework 7 - Solution

Q1) Structure factor and intensity calculations (30 pts)
(a) Calculate the structure factor of a cubic F crystal with a single atom basis
and identify its systematic absences.
Solution:
There are four lattice points per unit cell in a cubic F: (0,0,0), (1/2,1/2,0),
(0,1/2,1/2), (1/2,0,1/2). These four sites are occupied by four atoms (N=4) of the
same kind, with fi = f.
𝑁

𝑆ℎ𝑘𝑙 = ∑ 𝑓𝑖 𝑒 −2𝜋𝑖(ℎ𝑥+𝑘𝑦+𝑙𝑧) = 𝑓(1 + 𝑒 −𝜋𝑖(ℎ+𝑘) + 𝑒 −𝜋𝑖(𝑘+𝑙) + 𝑒 −𝜋𝑖(ℎ+𝑙) )
𝑗=1

If h, k, l are all odd, then 𝑆ℎ𝑘𝑙 = 4𝑓. Similarly, if h, k, l are all even, then 𝑆ℎ𝑘𝑙 = 4𝑓.
Indices that are mixed even, odd yield 𝑆ℎ𝑘𝑙 = 0.
(b) Derive the relationship for the interplanar spacing of the cubic F unit cell,
with lattice parameter, a.
Solution:

Show that 𝑑ℎ𝑘𝑙 =

𝑎
√ℎ2 +𝑘 2 +𝑙2

(c) Using Bragg’s law and assuming =1.54 Å and a = 5.64 Å, calculate the ten
lowest Miller index interplanar spacings and diffraction angles.
Solution:
Bragg’s law: 2dhklsinhkl=; 𝑑ℎ𝑘𝑙 =
𝜆

𝑎
√ℎ2 +𝑘 2 +𝑙2

𝜆

= 2 sin 𝜃 ;
ℎ𝑘𝑙

𝜆

𝜃ℎ𝑘𝑙 = sin−1 (2𝑎 √ℎ2 + 𝑘 2 + 𝑙 2 ) = sin−1 (2𝑑

ℎ𝑘𝑙

)

Prepare a table; note that diffraction angle is 2hkl. ID of diffraction peaks present is
optional.

1

MSE300

Hkl
100
110
111
200
210
211
220
221
300
301

Homework 7 - Solution

h2 + k2 + l2
1
2
3
4
5
6
8
9
9
10

dhkl (Å)
5.64
3.99
3.256
2.82
2.52
2.30
1.99
1.88
1.88
1.78

2hkl ()
15.69
22.26
27.36
31.69
35.55
39.07
45.43
48.36
48.36
51.15

Present?
N
N
Y
Y
N
N
Y
N
N
N

(d) Calculate the structure factor of NaCl and compute the intensity, Ihkl.
Solution:

The NaCl structure is composed of two cubic F sublattices.
Na: (000) (

11
1 1
11
0) ( 0 ) (0 )
22
2 2
22

1
1
1 111
Cl: (0 0) ( 00) (00 ) (
)
2
2
2 222
𝑁

𝑆ℎ𝑘𝑙 = ∑ 𝑓𝑖 𝑒 −2𝜋𝑖(ℎ𝑥+𝑘𝑦+𝑙𝑧)
𝑗=1

= 𝑓𝑁𝑎 (1 + 𝑒 −𝜋𝑖(ℎ+𝑘) + 𝑒 −𝜋𝑖(ℎ+𝑙) + 𝑒 −𝜋𝑖(𝑘+𝑙) )
+ 𝑓𝐶𝑙 (𝑒 −𝜋𝑖𝑘 + 𝑒 −𝜋𝑖ℎ + 𝑒 −𝜋𝑖𝑙 + 𝑒 −𝜋𝑖(ℎ+𝑘+𝑙) )
(e) Identify the systematic absences of NaCl. How do they differ from those of
the cubic F lattice?

2

MSE300

Homework 7 - Solution

Solution:
If h, k, l are all odd, then Shkl = 4fA - 4fB. When h, k, l are all even, then Shkl = 4fA + 4fB.
The systematic absences are the same as cubic F, but the intensity of the peaks
is modulated by the even vs odd hkl indices.
In complicated cases such as this, it helps to use test indices:
hkl
100
110
111
200
210
211
220

Shkl
0
0
4fA - 4fB
4fA + 4fB
0
0
4fA + 4fB

(f) Using (a) and (d), compare the intensity of the first five diffractions present
in the cases of cubic F and NaCl.
Solution:
hkl
100
110
111
200
210
211
220
221
300
310
311
222

Cubic F
|Shkl|2
0
0
16f 2
16f 2
0
0
16f 2
0
0
0
16f 2
16f 2

NaCl
|Shkl|2
0
0
16(fA - fB)2
16(fA + fB)2
0
0
16(fA + fB)2
0
0
0
16(fA - fB)2
16(fA + fB)2

(g) Discuss how the intensities in (f) may be used to distinguish an elemental
cubic F from a binary cubic F, such as NaCl.
Solution:
While systematic absences are identical, the difference lies in the intensity
distribution of all-odd and all-even indices, with the latter (all-even indices)
exhibiting systematically higher intensity (and equal to cubic F) than the (all-odd
indices).

3

MSE300

Homework 7 - Solution

Q2) Designing an XRD experiment to detect phase transition (10 pts)
BaTiO3 has a structure that is completely analogous to SrTiO3, except that it is
tetragonal. Assume that SrTiO3 and BaTiO3 form solid solutions, (Sr,Ba)TiO3, but
at an undetermined concentration of Ba, the solid solution takes on a tetragonal
structure. Outline a powder diffraction experiment that could be used to determine
the concentration of Ba at which the material transforms from cubic to tetragonal.
Be sure to explain the signature that the transformation would have on the
diffraction experiment.
Solution:
The cubic and tetragonal phases of the same compound will have unit cells such
that a=b=c in the cubic case and a=bc in the tetragonal case. In a cubic case,
(n00) and (00n) have the same d-spacing and same diffraction angle. However, in
a tetragonal case (n00) and (00n) have different d-spacings and diffraction angles,
leading to formation of new diffraction peaks.
As soon as the phase transforms to tetragonal, there is appearance of new
diffraction peaks, which we can compute by considering the interplanar spacing
as well as Bragg’s law:

𝑑ℎ𝑘𝑙 =

𝑎

√ℎ2 + 𝑘 2 + 𝑙2

2dhklsinhkl=; 𝜃ℎ𝑘𝑙 = sin−1 (2𝑑𝜆 )
ℎ𝑘𝑙

Q3) Compound identification (20 pts)
Consider the reaction of Al powder and Fe powder to form FeAl. The structural
data for these materials are given in the table below.

4

MSE300

Homework 7 - Solution

One of the schematic diffraction patterns shown below is of the combined,
unreacted powders of Al and Fe, and the other is of the intermetallic phase, FeAl.
Distinguish between the two. All computations and reasoning on which you base
your decision must be included with your answer. Assume that the X-ray
wavelength is 1.54 Å and the experimental resolution is limited to ± 0.5° in 2𝜃.

Solution:
Fe, Al and FeAl are cubic with I, F, and P lattices, respectively. The three
compounds therefore exhibit different systematic absences.

5

MSE300

Homework 7 - Solution

Using Bragg’s law, we can compute the dhkl and hkl values for the three
compounds using trial indices and noting systematic absences.

𝑑ℎ𝑘𝑙 =

𝑎

√ℎ2 + 𝑘 2 + 𝑙2

2dhklsinhkl=; 𝜃ℎ𝑘𝑙 = sin−1 (2𝑑𝜆 )
ℎ𝑘𝑙

Fe: cubic I (a=2.87A)
hkl

h2+k2+l2

100
110
111
200
210
211
220

1
2
3
4
5
6
8

dhkl
2.03
1.44
1.17
1.01

2

Obs

N
44.58 Y
N
64.65 Y
N
82.31 Y
Y

Al: cubic F
(a=4.08A)
dhkl
2

2.36
2.04
1.44

FeAl: cubic P
(a=3.01A)
Obs dhkl 2
?
3.01 29.6 Y
2.13 42.4 Y
38.1 Y
1.74 52.5 Y
44.4 Y
Y
Y
Y
64.7 Y
Y

Based on the above table, the diffraction in (b) matches Al as all three peaks 111,
200 and 220 are a match. The first three diffractions of FeAl match those of the
diffraction pattern in (a).

6

MSE300

Homework 7 - Solution

Q4) Diffraction pattern (30 pts)
Using the reciprocal lattice pattern, draw the hk0, h0l, and 0kl sections of the
diffraction patterns of the following space groups considering all systematic
absences; explain your answer:

a) I41/a
I: Reflectons present when h+k+l=2n; even.
41: Reflections present when l=4n, involved in 00l
a: Reflections present when h=2n; even, involved in hk0
hk0: h has to be even from glide, k has to be even from I center since h is
even
h0l: l=4n along 00l direction from screw. h+l has to be even aside from 00l
due to I center
0kl: l=4n along 00l direction from screw. k+l has to be even aside from 00l
due to I center

7

MSE300

Homework 7 - Solution

b) Cmc21
C: Reflections present when h+k=2n; even
c: Reflections present when l=2n; even, involved in h0l
21: Reflections present when h, k, or l=2n; even, involved in 00l
hk0: h+k has to be even from C center
h0l: l has to be even along 00l direction from screw and in general from
glide, h has to be even from C center
0kl: l has to be even along 00l direction from screw, h has to be even from
C center

c) Aba2
A: Reflections present when k+l=2n; even
b: Reflections present when k=2n; even, involved in 0kl
a: Reflections present when h=2n; even, involved in h0l
hk0: k has to be even from A center
h0l: h has to be even from glide and l has to be even from A center
0kl: k has to be even from glide and l has to be even from A center

8

MSE300

Homework 7 - Solution

Q5) Diffraction Intensity (10 pts)
List all the factors that can influence the intensity of a diffraction intensity.

9



## Metadata
- Source file: junk_drawer/MSE300_Fall2023_HW7_Solution.pdf
- Extracted: 2026-05-18
- Category: academic-homework
