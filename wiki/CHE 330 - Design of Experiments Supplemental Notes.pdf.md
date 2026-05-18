# CHE 330 - Design of Experiments Supplemental Notes.pdf

Source: junk_drawer/CHE 330 - Design of Experiments Supplemental Notes.pdf

Category: [[academic-lecture]]

## Summary
Department of Chemical & Biomolecular Engineering North Carolina State University CHE 330 Design of Experiment† Fall 2010 Design of experiment or experimental design is a structured approach that could be used to establish causality relationship between factors (along with their possible interaction effects) and

## Full Content
Department of Chemical & Biomolecular Engineering
North Carolina State University
CHE 330

Design of Experiment†

Fall 2010

Design of experiment or experimental design is a structured approach that could be used to
establish causality relationship between factors (along with their possible interaction effects) and
the outcome of an experiment. The approach is general with broad applications in engineering,
natural science, social science, and finance.

The schematic of experimental design is shown in Fig. 1 above. Experimental design is useful in
interpreting the outcome of an experiment. It provides an efficient identification of key variables
that affect the outcome of the experiment, including interaction effects that are often not
immediately obvious among the factors under study. It makes possible an efficient establishment
of causality relationship between the factors and their interaction effects and the outcome of the
experiment. One could attempt to determine the effects of various factors on the outcome of the
experiment by varying the factors one at a time with the misguided notion that the interpretation
of the experimental outcome would be simpler, but such an approach would be inefficient and it
could lead to erroneous conclusions because it overlooks possible interaction effects among the
various factors that could be important. A case in point will be shown shortly.
The benefits of experimental design have been convincingly demonstrated in the following case
studies using the simplest application of experimental design: (1) using a 2-level, 4-factor (2 x 4)
experimental design, the Tool Products Company, Plymouth, was able to pinpoint the cause of
______________________________________________________________________________
†
P. K. Lim, Department of Chemical Engineering, North Carolina State University, Raleigh, NC
27695-7905, March 25, 2010.

defects in the manufacturing of die-cast aluminum housings for computer disk drives
(specifically, metal temperature and final die pressure acting together) and thereby reduce the
incidence of defects from 15% to essentially zero1; (2) with the aid of a 2-level, 6-factor (2 x 6)
experimental design, engineers at Eastman Kodak were able to retool an existing metal-forming
machine with the net results of a higher production rate of camera film clip that it produced with
a greater reliability and a 10-fold scrap reduction2; and (3) with the help of a 2-level, 3-factor (2
x 3) experimental design, the design engineers of SKF (a Swedish company) were able to
optimize the design of the ball bearing it produced and thereby successfully met the competition
from a Japanese rival3.
The last case study is presented in details below to illustrate generally the analysis of a 2-level, nfactor (2 x n) experimental design. A two-level factorial design experiment means that each of
the factors under study is varied to take on two assigned values (denoted by the plus- and minusvalues). A three-level experiment means three assigned values (denoted by plus-, mid- and
minus-values) for each of the variables being studied. Performance experience suggested that
three factors affected the effective lifetime of a ball bearing, specifically, (i) outer ring osculation
(see the figure below), (ii) heat treatment of the inner ring (see Fig 2 below), and (iii) material of
construction for the bearing cage.

In the 2 x 3 factorial design study performed by SKF engineers, the osculation ratio was varied
between a standard value and a modified value, the heat treatment of the inner ring was varied
between standard treatment and an enhanced treatment, and the material of construction was
varied between (cheaper) polymer and steel. A total of 23 or 8 runs were performed to measure
the effective lifetime of the ball bearing (presumably under accelerated test conditions) for the
different parametric combinations, and the test results are presented in Table 1 on the next page.
The test results revealed two unexpected findings. First, unusually strong interaction effects
were found among the test factors, especially between the outer ring osculation and the inner ring

heat treatment. Second, the material of construction for the bearing cage had only modest effect
on the bearing life, suggesting the possibility of a major cost saving with the use of polymer
material with only minor impact on the bearing’s service life. These findings are supported by
the following analysis.
Table 1. Effective lifetime of ball bearing under various test conditions.
Run
# Osculation Ratio (A)
1
Standard (A–)
2
Modified (A+)
3
Standard (A–)
4
Modified (A+)
5
Standard(A–)
6
Modified (A+)
7
Standard (A–)
8
Modified (A+)

Inner Ring Heat Treatment (B)

Cage Material (C)

Measured
Lifetime Y, h

Standard (B–)
Standard (B–)
Enhanced (B+)
Enhanced (B+)
Standard (B–)
Standard (B–)
Enhanced (B+)
Enhanced (B+)

Polymer (C–)
Polymer (C–)
Polymer (C–)
Polymer (C–)
Steel (C+)
Steel (C+)
Steel (C+)
Steel (C+)

17
25
26
85
19
21
16
128

Test Parameters

A+

B+

C+

Overall Mean <YA,B,C>. = ∑ ∑ ∑ YA, B ,C = [(17+25+26+85+19+21+16+128)/8] h = 42.125 h
A= A− B = B − C =C −

Effect of A ≡ Mean YA+,B,C – Mean YA–,B,C
= [(25+85+21+128)/4 – (17+26+19+16)/4] h
= 45.25 h
Effect of B ≡ Mean YA,B+,C – Mean YA,B–,C
= [(26+85+16+128)/4 – (17+25+19+21)/4] h
= 43.25 h
Effect of C ≡ Mean YA,B,C+ – Mean YA,B,C–
= [(19+21+16+128)/4 – (17+25+26+85)/4] h
= 7.75 h
Effect of AB Interaction
= Half difference between A effect when B is B+ and the A effect when B is B–
= Half difference between B effect when A is A+ and the B effect when A is A–
= [(Mean YA+B+C − Mean YA−B+C) − (Mean YA+B−C − Mean YA−B−C)]/2
= {[(YA+B+C+ + YA+B+C−) − (YA−B+C+ + YA−B+C−)] − [(YA+B−C+ + YA+B−C−) − (YA−B−C+ + YA−B−C−)]}/4
= {[(128 + 85) – (16+26)] – [(21+25) – (19+17)]}h/4
= {171 – 10}h/4
= 40.25 h
Effect of AC Interaction
= Half difference between A effect when C is C+ and the A effect when C is C–
= Half difference between C effect when A is A+ and the C effect when A is A–
= [(Mean YA+BC+ − Mean YA−BC+) − (Mean YA+BC− − Mean YA−BC−)]/2

= {[(YA+B+C+ + YA+B−C+) − (YA−B+C+ + YA−B−C+)] − [(YA+B+C− + YA+B−C−) − (YA−B+C− + YA−B−C−)]}/4
= {[(128+21) – (16+19)] – [(85+25) – (26+17)]}h/4
= {114 – 67}h/4
= 11.75 h
Effect of BC Interaction
= Half difference between B effect when C is C+ and the B effect when C is C–
= Half difference between C effect when B is B+ and the C effect when B is B–
= [(Mean YAB+C+ − Mean YAB−C+) − (Mean YAB+C− − Mean YAB−C−)]/2
= {[(YA+B+C+ + YA−B+C+) − (YA+B−C+ + YA−B−C+)] − [(YA+B+C− + YA−B+C−) − (YA+B−C− + YA−B−C−)]}/4
= {[(128+16) – (21+19)] – [(85+26) – (25+17)]}h/4
= {104 – 69}h/4
= 8.75 h
Effect of ABC Interaction
= Half difference between the AB interactions when C is C+ and C is C–
= {[(YA+B+C+ − YA−B+C+) − (YA+B−C+ − YA−B−C+)]/2 − [(YA+B+C− − YA−B+C−) − (YA+B−C− − YA−B−C−)]/2}/2
= [YA+B+C+ + YA–B–C+ + YA–B+C– + YA+B–C–]/4 − [YA–B+C+ + YA+B–C+ + YA+B+C– + YA–B–C–]/4
= {[128 + 19 + 26 + 25] – [16 + 21 + 85 + 17]}h/4
= 14.75 h
It is seen that factors A (outer ring osculation) and B (inner ring heat treatment) and their
interaction (AB) have much larger effects than factor C (material of cage construction).
The 2-level factorial design provides a model equation that not only summarizes the test results
but also predict model results that could be tested for different parameter settings within the
ranges tested. For the above example, the model equation predicting the bearing lifetime of is
given by Ymodel = βo + β1A + β2B + β3C + β4A*B + β5A*C + β6B*C + β7A*B*C

(1)

where βo = overall mean lifetime = 42.125 h,
β1 = A Effect/(A+ – A–) = 45.25 h/2 = 22.625 h, if A+ = +1 and A– = –1,
β2 = B Effect/(B+ – B–) = 43.25 h/2 = 21.625 h, if B+ = +1 and B– = –1,
β3 = C Effect/(C+ – C–) = 7.75 h/2 = 3.875 h, if C+ = +1 and C– = –1,
β4 = AB Effect/2 = 40.25 h/2 = 20.125 h,
β5 = AC Effect/2 = 11.75 h/2 = 5.875 h,
β6 = BC Effect/2 = 8.75 h/2 = 4.375 h, and
β7 = ABC Effect/2 = 14.75 h/2 = 7.375 h
It follows that Eqn (1) =>
Ymodel = [42.125 + 22.625A + 21.625B + 3.875C + 20.125AB + 5.875AC + 4.375BC + 7.375ABC] h (1’)

The following table may be constructed using Eqn (1’).

Measured
Run
Test Parameters
Lifetime
Y, h
A
B
C
#
1
A– = –1
B– = –1
C– = –1
17
2
A+ = 1
B– = –1
C– = –1
25
3
A– = –1
B+ = 1
C– = –1
26
4
A+ = 1
B+ = 1
C– = –1
85
5
A– = –1
B– = –1
C+ = 1
19
6
A+ = 1
B– = –1
C+ = 1
21
7
A– = –1
B+ = 1
C+ = 1
16
8
A+ = 1
B+ = 1
C+ = 1
128
9
–0.5
0
–1
10
0.75
–0.5
1
Red entries are model predictions that could be tested.

Model Lifetime
Ymodel, h

17
25
26
85
19
21
16
128
29.9
44.06

References
1. “Diecaster achieves zero-defect parts,” Quality in Manufacturing (March/April, 1994).
2. Peter Runke, “Design of Experiments Software Saves Kodak Thousands,” MetalForming
OnLine, \DesignExpt\Design of Experiments Software Saves Kodak Thousands.mht.
3. C. Hellstrand, A. D. Oosterhoom, D. J. Sherwin and M. Gerson, “The Necessity of Modern
Quality Improvement and Some Experience with its Implementation in the Manufacture of
Rolling Bearings,” Phil Trans, Royal Soc. London A 327, 529-537 (1989).



## Metadata
- Source file: junk_drawer/CHE 330 - Design of Experiments Supplemental Notes.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
