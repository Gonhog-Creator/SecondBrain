# John Smallwood dissertation (FINAL).pdf

Source: junk_drawer/John Smallwood dissertation (FINAL).pdf

Category: [[academic-homework]]

## Summary
THERMAL AND STRUCTURAL CHARACTERIZATION OF A ROTATING DETONATION ROCKET ENGINE by John Smallwood A Dissertation Submitted to the Faculty of Purdue University In Partial Fulfillment of the Requirements for the degree of Doctor of Philosophy

## Full Content
THERMAL AND STRUCTURAL CHARACTERIZATION OF A
ROTATING DETONATION ROCKET ENGINE
by
John Smallwood

A Dissertation
Submitted to the Faculty of Purdue University
In Partial Fulfillment of the Requirements for the degree of

Doctor of Philosophy

School of Aeronautics and Astronautics
West Lafayette, Indiana
August 2024

THE PURDUE UNIVERSITY GRADUATE SCHOOL
STATEMENT OF COMMITTEE APPROVAL

Dr. Stephen D. Heister, Chair
School of Aeronautics and Astronautics
Dr. Michael D. Sangid
School of Aeronautics and Astronautics
Dr. Carson D. Slabaugh
School of Aeronautics and Astronautics
Dr. Joseph D. Sims
Quadrus Corporation

Approved by:
Dr. Gregory A. Blaisdell

2

This work is dedicated to my wife and children: Emily Smallwood, Elena Smallwood, Lydia
Smallwood, and John “Clark” Smallwood.

Emily - Without your love, support, and motivation, none of this would have been
possible. You are an incredible wife and mother, all while balancing a demanding career in the
space industry. During this journey, we moved our family from Northern Virginia to Indiana and
then back to Virginia. We gave birth to our son Clark, and watched our beautiful daughters grow
from infants to toddlers and preschoolers. We met new families and friends, explored new
places, and made family memories that we will cherish for the rest of our lives. You are an
inspiration to me and our children. As our journey continues, I look forward to what our future
holds and am excited to explore it with you by my side.
Elena, Lydia, and Clark – You make me a proud father. Your excitement, curiosity, and
eagerness to explore motivates me to cherish each day. This journey was full of once in a lifetime
events, such as learning to talk, learning to walk, first day of school, and even learning to ride a
bike. We shared every moment together as a family. It is my hope that you find your mother and
my passion for family and adventure as an inspiration to try new things, explore the world
together, and live life to its fullest. I look forward to what your future holds and the things you
will accomplish.

I would also like to thank Leah Warren. As Emily and I both work, this would not have been
possible without your amazing childcare for 3 years. You gave our children experiences they will
never forget. We will always consider you as family and are grateful our children have you in
their life.

3

ACKNOWLEDGMENTS

I would like to thank everyone who helped me throughout my PhD work. Firstly, I would
like to thank my advisor, Professor Stephen Heister. Thank you for providing this opportunity and
guiding my research. Your passion for rocket propulsion and aerospace engineering is a motivation
to me along with many other current and aspiring aerospace professionals. Additionally, your
research and rocket propulsion course has inspired many of today’s propulsion designers who have
helped to revolutionize the launch market and make space more accessible. I would also like to
thank my committee members including Professor Carson Slabaugh, Professor Michael Sangid,
and Dr. Joseph Sims. Your guidance and feedback on this work is greatly appreciated. I would
like to thank Dr. Joseph Sims and Thomas Teasley for their guidance and support throughout the
design and additive manufacturing process.
This work was possible due to the staff at Zucrow Laboratory. I would like to thank Scott
Meyer for his guidance and feedback throughout the hardware development and test setup process.
I would like to thank Rob McGuire whose support through the design process and attention to
detail during the post machining process made this work come together. I would like to thank the
research group for their feedback, support, and recommendations. This group includes Dr. Kevin
Dille, Brendan Reese, Dr. Ariana Martinez, Dr. Alexis Harroun, and Dr. Nathan Ballintyn. I would
like to thank Joseph Prom and Wesley Gibson for their test setup support. I would also like to
thank Dr. Kevin Dille, Brendan Reese, and Drake Fish for the test operations support.

4

TABLE OF CONTENTS

LIST OF TABLES .......................................................................................................................... 7
LIST OF FIGURES ...................................................................................................................... 10
ABSTRACT.................................................................................................................................. 17
INTRODUCTION .................................................................................................................... 19
TEST ARTICLE AND FACILITY SETUP ............................................................................. 23
2.1

Traditionally Manufactured Approach ......................................................................... 24

2.2

Combined Traditional/Additive Manufactured Approach ............................................ 34

2.3

Entirely Additive Manufacturing Approach ................................................................. 38

2.4

Combustor Sizing.......................................................................................................... 48

2.5

Ignition System ............................................................................................................. 51

2.6

Material Selection ......................................................................................................... 55

2.7

Heat Sink Combustor .................................................................................................... 55

2.8

Post Processing ............................................................................................................. 55

2.9

Water Flow Results ....................................................................................................... 56

2.10

Manufacturing Approach Trade Study Conclusion ...................................................... 59

2.11

Design Changes and Hardware Configuration Summary ............................................. 60

2.12

Test Facility .................................................................................................................. 64

THERMAL EVALUATION .................................................................................................... 69
3.1

Calorimetry Thermal Model Methodology ................................................................... 69

3.2

Predictive Thermal Model Methodology ...................................................................... 79

TEST CAMPAIGN 1.0 RESULTS .......................................................................................... 83
4.1

Heat Sink Testing .......................................................................................................... 83

4.2

Water Cooled Testing ................................................................................................... 87

5

TEST CAMPAIGN 2.0 RESULTS ........................................................................................ 103
5.1

Heat Sink Testing ........................................................................................................ 103

5.2

Water Cooled Testing ................................................................................................. 107

5.2.1

Heat Flux Characterization Testing and Calorimetry Uncertainty Assessment .... 110

5.2.2

Endurance Testing ................................................................................................. 130

5.2.3

Pulsed Short Duration Testing .............................................................................. 140

STRUCTURAL EVALUATION ........................................................................................... 164
6.1

Material Properties ...................................................................................................... 167

6.2

Problem Description ................................................................................................... 181

6.3

Low Cycle Fatigue Assessment .................................................................................. 183

6.4

Combined Low Cycle and High Cycle Fatigue Assessment ...................................... 198

CONCLUSIONS..................................................................................................................... 215
REFERENCES ........................................................................................................................... 218
APPENDIX A. HARDWARE CONFIGURATION SUMMARY ............................................ 222
APPENDIX B. PLUMBING AND INSTRUMENTATION DIAGRAMS ............................... 225

6

LIST OF TABLES

Table 2.1. TSRDE Injector Element Design Values (Used in All Hardware Configurations) ..... 44
Table 2.2. Cooling Passage Design (Water Cooled 1.0 Design) .................................................. 46
Table 2.3. RDRC Minimum Sizing Constraint Using Bykovskii Criteria ................................... 50
Table 2.4. RDRC Size and Part Quantity Conclusion Per Manufacturing Approach .................. 60
Table 2.5. Water Cooled 2.0/2.1 Outerbody Cooling Passage Design ......................................... 64
Table 2.6. Autosequence Example for ~0.25 sec Duration Test (No Active Cooling) ................ 66
Table 4.1. Test Campaign 1.0, HS 1.0, Hot Fire Testing Summary ............................................. 83
Table 4.2. Test Campaign 1.0, Water Cooled 1.0, Hot Fire Testing Summary ............................ 87
Table 5.1. Test Campaign 2.0, HS 1.1, Hot Fire Testing Summary ........................................... 104
Table 5.2. Test Campaign 2.0, WC 2.0, Long Duration Hot Fire Testing Summary ................. 108
Table 5.3. Test Campaign 2.0, WC 2.0, Cumulative Thermal Cycles and Total Test Duration 109
Table 5.4. Test Campaign 2.0, Outerbody Thermal Loading Performance Metric Summary ... 118
Table 5.5. Test Campaign 2.0, Injector Thermal Loading Performance Metric Summary ........ 118
Table 5.6. Test 59, Heat Flux Variation with Operation Conditions .......................................... 135
Table 6.1. Structural Evaluation Parameter List and Description .............................................. 166
Table 6.2. Cycle Stress Strain Data Constants Derived for Ramberg Osgood Fit, Extruded GRCop84 at 673 K; R-Ratio = -1 ........................................................................................................... 175
Table 6.3. Basquin Coffin Manson Coefficients for Extruded GRCop-84 at 673 K; R-Ratio = -1
..................................................................................................................................................... 179
Table 6.4. Cooling System Design Used for the Fatigue Assessments ...................................... 181
Table 6.5. Equation 6-12 - Equation 6-14 Assumptions ............................................................. 185
Table 6.6. Operating Conditions Used for LCF Assessment ...................................................... 186
Table 6.7. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Nominal Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties .................................................................................................................................... 193

7

Table 6.8. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Nominal Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties .................................................................................................................................... 194
Table 6.9. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Upper Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties .................................................................................................................................... 195
Table 6.10. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Upper Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson Properties
..................................................................................................................................................... 195
Table 6.11. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Lower Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties .................................................................................................................................... 196
Table 6.12. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Lower Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson Properties
..................................................................................................................................................... 197
Table 6.13. Equation 6-27 Assumptions ..................................................................................... 201
Table 6.14. Pressure Stress Summary, Channel Width (CW) = 0.030 in / 0.762 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8 ...................................... 202
Table 6.15. Pressure Stress Summary, Channel Width (CW) = 0.065 in / 1.651 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8 ...................................... 203
Table 6.16. Pressure Stress Summary, Channel Width (CW) = 0.100 in / 2.540 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8 ...................................... 203
Table 6.17. Smith Watson Topper Results for Thermal Loading, Heat Flux = 5 kW/cm^2, Hot
Wall Temperature = 673 K; Nominal Ramberg Osgood Material Properties,
Nominal/Upper/Lower Basquin Coffin Manson Material Properties ......................................... 209
Table 6.18. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation
Wave, Detonation Pressure Ratio = 8; Nominal Ramberg Osgood Material Properties; Nominal
Basquin Coffin Manson Material Properties .............................................................................. 209
Table 6.19. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation
Wave, Detonation Pressure Ratio = 8; Nominal Ramberg Osgood Material Properties; Lower
Bound Basquin Coffin Manson Material Properties ................................................................... 210
Table 6.20. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation
Wave, Detonation Pressure Ratio = 8; Nominal Ramberg Osgood Material Properties; Upper
Bound Basquin Coffin Manson Material Properties ................................................................... 210

8

Table 6.21. Linear Damage Assessment Results for Chamber Pressure of 3.10 MPa and 8.62 MPa;
Nominal Ramberg Osgood Material Properties; Nominal/Upper/Lower Bound Basquin Coffin
Manson Material Properties; Wave Pass Frequency = 13 kHz to Calculate Run Time from Cycles
..................................................................................................................................................... 211
Table 6.22. Linear Damage Assessment Results for Chamber Pressure of 15.5 MPa and 22.4 MPa;
Nominal Ramberg Osgood Material Properties; Nominal/Upper/Lower Bound Basquin Coffin
Manson Material Properties; Wave Pass Frequency = 13 kHz to Calculate Run Time from Cycles
..................................................................................................................................................... 212

9

LIST OF FIGURES

Figure 1.1. (a) RDE Operating Configuration [1] (b) Unwrapped Visualization of RDE Operating
Principles [33] ............................................................................................................................... 20
Figure 1.2. (a) Center Body Damage During Liquid Bi-Propellant RDRE Testing at Purdue
University [35] (b) Fuel Injector Damage During GOx/Kerosene RDRE Testing at Purdue
University [36] .............................................................................................................................. 21
Figure 2.1. Traditionally Manufactured RDRC Cross Section ..................................................... 24
Figure 2.2. Traditionally Manufactured RDRC Outerbody Design ............................................. 26
Figure 2.3. Outerbody Cooling Liner Buckling Evaluation ......................................................... 27
Figure 2.4. Traditionally Manufactured RDRC Outerbody Cooling Liner Design ...................... 29
Figure 2.5. Traditionally Manufactured RDRC Innerbody and Injector Cooling Flow Paths ..... 31
Figure 2.6. Traditionally Manufactured RDRC Innerbody Cooling Liner Design....................... 32
Figure 2.7. Traditionally Manufactured RDRC Injector Cooling Design .................................... 33
Figure 2.8. Combined Manufactured RDRC Cross Section ......................................................... 35
Figure 2.9. Combined Manufactured RDRC Cross Section ......................................................... 36
Figure 2.10. Combined Manufactured RDRC Components and Flow Paths ............................... 38
Figure 2.11. Additively Manufactured RDRC Cross Section (Water Cooled 1.0 Design) .......... 39
Figure 2.12. Additively Manufactured RDRC Propellant Flow Schematic (Water Cooled 1.0
Design) .......................................................................................................................................... 42
Figure 2.13. Additively Manufactured RDRC Coolant Flow Schematic (Water Cooled 1.0 Design)
....................................................................................................................................................... 45
Figure 2.14. Innerbody and Outerbody Cooling System Passages (Used in All Hardware
Configurations) ............................................................................................................................. 47
Figure 2.15. Pressure and Temperature Measurements (Water Cooled 1.0 Design) .................... 48
Figure 2.16. Detonation Cell Width of Various Mixtures [12]..................................................... 49
Figure 2.17. Chamber pressure vs Propellant Flowrate ................................................................ 50
Figure 2.18. Pre-Detonation System [7] ....................................................................................... 52

10

Figure 2.19. Pre-Detonation Ignition System Passage to Combustion Chamber (Used in All
Hardware Designs)........................................................................................................................ 53
Figure 2.20. Cooling Jacket Accommodation of Pre-Detonation Ignition System Passage (Used in
All Hardware Designs) ................................................................................................................. 54
Figure 2.21. Innerbody Cooling System Water Flow Results (Water Cooled 1.0 Design) .......... 57
Figure 2.22. Outerbody Cooling System Water Flow Results (Water Cooled 1.0 Design) ......... 58
Figure 2.23. Oxidizer Injector Water Flow Results (Water Cooled 1.0 Design).......................... 58
Figure 2.24. Fuel Injector Water Flow Results (Water Cooled 1.0 Design) ................................ 59
Figure 2.25. Water Cooled 2.0 and 2.1 Dimension Summary ...................................................... 62
Figure 2.26. Water Cooled 2.0 Hardware, Outerbody Coolant Outlet Temperature Measurement
....................................................................................................................................................... 63
Figure 2.27. Water Cooled 2.0 Hardware, Accelerometer Placement Overview ......................... 67
Figure 2.28. Water Cooled 2.0 Hardware, Accelerometer Placement Cross Section ................... 68
Figure 3.1. WC 1.0 Outerbody Coolant Exit Thermocouple Placement ...................................... 71
Figure 3.2. Cooling Channel Arrangement and Definition........................................................... 74
Figure 3.3. Hot Gas Temperature Comparison, Stoichiometric Mixture Ratio, Frozen Combustion
Product Conditions........................................................................................................................ 77
Figure 3.4. Hypersonic Local Heat Flux Scaling [30] .................................................................. 78
Figure 3.5. Temperature Profiles in Copper Combustion Chamber Wall From Transient Heat Flux
[8] .................................................................................................................................................. 80
Figure 4.1. CTAP Measurement Location on HS 1.0 ................................................................... 85
Figure 4.2. Test 21 High Speed Video Screen Captures Showing Single Wave in Different
Quadrants ...................................................................................................................................... 85
Figure 4.3. Stechmann Performance Model Comparison with Experimental Dataset [3,8]......... 86
Figure 4.4. Test 39; Cooling System Mass Flowrates .................................................................. 88
Figure 4.5. Test 43; Outerbody Calorimetry Results; Indication of Thermocouple Protrusion Error
and Invalid Calorimetry Results From TC-208 ............................................................................ 89
Figure 4.6. Test 44; Outerbody Calorimetry Results; TC-208 Adjustment Resulting in Acceptable
Correlation with TC-210 ............................................................................................................... 91

11

Figure 4.7. Test 44; Injector Calorimetry Results......................................................................... 92
Figure 4.8. Test 45; Propellant System Flowrates ........................................................................ 93
Figure 4.9. Test 45; Outerbody Calorimetry Results .................................................................... 94
Figure 4.10. Test 45; Injector Calorimetry Results....................................................................... 95
Figure 4.11. Test 45; Outerbody Coolant System Temperatures.................................................. 95
Figure 4.12. Test 46; Fuel Manifold High Frequency Pressure FFT ............................................ 97
Figure 4.13. Test 47; Outerbody Calorimetry Results .................................................................. 98
Figure 4.14. Test 47; Injector Calorimetry Results....................................................................... 99
Figure 4.15. WC 1.0 Outerbody Heat Flux Summary; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2 ..................................................................... 100
Figure 4.16. WC 1.0 Outerbody Heat Flux Ratio; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2 ..................................................................... 101
Figure 4.17. WC 1.0 Injector Heat Flux Summary; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2 ..................................................................... 102
Figure 4.18. WC 1.0 Injector Heat Flux Ratio; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2 ..................................................................... 102
Figure 5.1. Test 21 High Speed Video Screen Captures For Tests 48-50 .................................. 105
Figure 5.2. CTAP Measurement Location Comparison Between HS1.0 and HS1.1 ................. 106
Figure 5.3. Test 52; Investigation of Outerbody Coolant Temperature Differences .................. 111
Figure 5.4. Outerbody Coolant Outlet Temperature Measurement, WC 2.0 Hardware ............. 112
Figure 5.5. Test 53; Investigation of Outerbody Coolant Temperature Differences .................. 113
Figure 5.6. Test 54; Investigation of Outerbody Coolant Temperature Differences .................. 114
Figure 5.7. Scanning Electron Microscope Image of WC 2.0 Hardware; Cooling Channel;
Unobstructed Backpressure Feature ........................................................................................... 115
Figure 5.8. Scanning Electron Microscope Image of WC 2.0 Hardware; Cooling Channel,
Obstructed Backpressure Feature ............................................................................................... 116
Figure 5.9. Test 52; Outerbody Calorimetry Results .................................................................. 119
Figure 5.10. Test 52; Injector Calorimetry Results..................................................................... 119

12

Figure 5.11. WC 2.0, Accelerometer Placement ........................................................................ 120
Figure 5.12. Test 52, Power Spectral Density of Radial Acceleration ....................................... 121
Figure 5.13. Test 52, Power Spectral Density of Axial Acceleration ......................................... 122
Figure 5.14. Test 52, Power Spectral Density of Fuel Manifold Pressure.................................. 123
Figure 5.15. Test 53; Outerbody Calorimetry Results ................................................................ 124
Figure 5.16. Test 53; Injector Calorimetry Results..................................................................... 125
Figure 5.17. Test 54; Outerbody Calorimetry Results ................................................................ 125
Figure 5.18. Test 54; Injector Calorimetry Results..................................................................... 126
Figure 5.19. WC 1.0 and 2.0 Outerbody Heat Flux Summary from Test Campaign 1.0 and 2.0;
Constant Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2 127
Figure 5.20. WC 1.0 and 2.0 Outerbody Heat Flux Ratio from Test Campaign 1.0 and 2.0; Constant
Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2 .............. 128
Figure 5.21. WC 1.0 and 2.0 Injector Heat Flux Summary from Test Campaign 1.0 and 2.0;
Constant Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2 129
Figure 5.22. WC 1.0 and 2.0 Injector Heat Flux Ratio from Test Campaign 1.0 and 2.0; Constant
Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2 .............. 129
Figure 5.23. Test 59, Outerbody Calorimetry Results from Endurance Testing ........................ 131
Figure 5.24. Test 59, Injector Calorimetry Results from Endurance Testing ............................. 132
Figure 5.25. Test 59, Power Spectral Density of Radial Acceleration ....................................... 133
Figure 5.26. Test 59, Propellant Manifold Pressure ................................................................... 134
Figure 5.27. Test 59, Outerbody Hot Wall Temperature and Heat Flux .................................... 135
Figure 5.28. Test 64, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 136
Figure 5.29. Test 64, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 137
Figure 5.30. Test 65, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 138
Figure 5.31. Test 65, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 139
Figure 5.32. Test 65, Power Spectral Density of Radial Accelerometer .................................... 140
Figure 5.33. Test 55, Description of a Thermal Cycle................................................................ 142

13

Figure 5.34. Test 56, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 144
Figure 5.35. Test 56, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 145
Figure 5.36. Test 56, Power Spectral Density of Radial Acceleration ....................................... 146
Figure 5.37. Test 56, Outerbody Calorimetry Results for First Thermal Cycle ......................... 147
Figure 5.38. Test 57, Temperature in Pre-Det Supply Line that Supplies the Combustion Chamber
Ignition Port ................................................................................................................................ 148
Figure 5.39. Test 57, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 149
Figure 5.40. Test 57, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 150
Figure 5.41. Test 57, Outerbody Calorimetry Results for First Thermal Cycle ......................... 151
Figure 5.42. Test 58, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 152
Figure 5.43. Test 58, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 153
Figure 5.44. Test 61, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 154
Figure 5.45. Test 61, Propellant Manifold Pressures .................................................................. 155
Figure 5.46. Test 61, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 156
Figure 5.47. Test 62, Propellant Manifold Pressures .................................................................. 157
Figure 5.48. Test 62, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 159
Figure 5.49. Test 62, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 160
Figure 5.50. Test 61 and Test 62, Power Spectral Density of Radial Accelerometer ................ 161
Figure 5.51. Test 63, Outerbody Calorimetry Results from Pulsed Short Duration Testing ...... 162
Figure 5.52. Test 63, Injector Calorimetry Results from Pulsed Short Duration Testing .......... 163
Figure 6.1. Yield Strength vs Temperature for High Strength Copper Alloys Commonly Used in
Rocket Combustors [41] ............................................................................................................. 168
Figure 6.2. (Left) Monotonic Stress vs Strain for High Strength Copper Alloys Commonly Used
in Rocket Combustors [41]; (Right) Monotonic Stress vs Strain for Extruded GRCop-84 at Various
Temperatures, Zoomed in to Low Strain Region........................................................................ 169
Figure 6.3. Cyclic Stress Range vs Plastic Strain Range for Extruded GRCop-84 at Rocket
Relevant Temperatures; R-Ratio = -1 [36] ................................................................................. 170

14

Figure 6.4. Cyclic Stress Range vs Plastic Strain Range for Extruded GRCop-84 at 673 K;
Generated Using Cyclic Stress vs Strain Data from [36]; R-Ratio = -1; Lerch et al Curve Fit
Represents data From NASA Reusable Launch Vehicle Program and is Considered the Nominal
Material Property for this Study ................................................................................................. 171
Figure 6.5. Cyclic Stress Amplitude vs Plastic Strain Amplitude for Extruded GRCop-84 at 673K;
Generated Using Cyclic Stress vs Strain Data from [36]; R-Ratio = -1; Lerch et al Curve Fit
Represents data From NASA Reusable Launch Vehicle Program and is Considered the Nominal
Material Property for this Study ................................................................................................. 172
Figure 6.6. Young’s Modulus vs Temperature for Pure Copper at Rocket Relevant Temperatures
[5] ................................................................................................................................................ 174
Figure 6.7. Cyclic Stress Amplitude vs Total Strain Amplitude at 673 K Using the Ramberg
Osgood Coefficients in Table 6.2; Cyclic Stress vs Total Strain Data from Reference [36];
Monotonic Stress vs Total Strain Data from Reference [41] ...................................................... 175
Figure 6.8. Total Strain Life Data for Extruded GRCop-84 at Rocket Relevant Temperatures; RRatio = -1 [36]............................................................................................................................. 176
Figure 6.9. Total Strain Life for Extruded GRCop-84 at 673 K; Generated Using Total Strain Life
Data from [36]; R-Ratio = -1 ...................................................................................................... 177
Figure 6.10. Basquin Coffin Manson Relationship for Extruded GRCop-84 at 673 K; Generated
Using Strain Life Data from [36]; R-Ratio = -1 ......................................................................... 179
Figure 6.11. Total Strain Life Using Basquin Coffin Manson Coefficients in Table 6.3 for Extruded
GRCop-84 at 673 K; Total Strain Life Data Points from Reference [36]; R-Ratio = -1; Upper and
Lower Bounds Represent +/- 68.27% ......................................................................................... 180
Figure 6.12. Structural Arrangement and Loading Summary..................................................... 181
Figure 6.13. Hot Wall Stress from Loading Conditions Present in Rotating Detonation Engine
..................................................................................................................................................... 182
Figure 6.14. Hot Wall Loading Condition Assumptions Used for the Low Cycle Fatigue
Assessment .................................................................................................................................. 185
Figure 6.15. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Nominal Ramberg Osgood Material Properties from Table 6.2 ............. 188
Figure 6.16. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Nominal Ramberg Osgood Material Properties from Table 6.2 .................... 188

15

Figure 6.17. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Upper Bound Ramberg Osgood Material Properties from Table 6.2 ..... 189
Figure 6.18. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Upper Bound Ramberg Osgood Material Properties from Table 6.2 ............ 190
Figure 6.19. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Lower Bound Ramberg Osgood Material Properties from Table 6.2 ..... 190
Figure 6.20. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Lower Bound Ramberg Osgood Material Properties from Table 6.2 ............ 191
Figure 6.21. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Nominal
Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin Coffin
Manson Material Properties ........................................................................................................ 194
Figure 6.22. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Upper
Bound Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin
Coffin Manson Material Properties ............................................................................................ 196
Figure 6.23. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Lower
Bound Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin
Coffin Manson Material Properties ............................................................................................ 197
Figure 6.24. Pressure Loads Experienced by Hot Wall; Assumed Coolant Pressure to be 2x the
Average Chamber Pressure; Assumed Peak Detonation Pressure to be 8x the Average Chamber
Pressure ....................................................................................................................................... 200
Figure 6.25. Pressure Loads Experienced by Hot Wall; Assumed Coolant Pressure to be 2x the
Average Chamber Pressure; Assumed Peak Detonation Pressure to be 8x the Average Chamber
Pressure ....................................................................................................................................... 204
Figure 6.26. Summary of Maximum and Minimum Combined Tangential Stress Calculations 206
Figure 6.27. Summary of Combined Loading Assessment; Nominal Ramberg Osgood Material
Properties; Nominal Basquin Coffin Manson Material Properties; Detonation Pressure Ratio = 8;
Wave Pass Frequency = 13 kHz to Determine Run Time from Cycles ..................................... 213
Figure 6.28. Summary of Combined Loading Assessment; Nominal Ramberg Osgood Material
Properties; Lower Basquin Coffin Manson Properties; Detonation Pressure Ratio = 8; Wave Pass
Frequency = 13 kHz to Determine Run Duration from Cycles .................................................. 214

16

ABSTRACT

Improving launch vehicle and satellite propulsion system performance directly correlates
to the delivery of more mass (or quantity) on orbit from launch vehicles, longer duration satellite
missions, and longer ranges for missiles/interceptors. Alternative propulsion devices such as
rotating detonation engines (RDEs) offer the potential for significant performance gains but their
operability has only been demonstrated on “battle hardened” laboratory devices for rocket
applications. The objective of this research was to demonstrate cooling and structural approaches
that mature rotating detonation rocket engines (RDREs) to flight like maturation levels.
Multiple 1.6”/4.1 cm diameter RDE combustors were designed, fabricated, and tested. The
RDE tested the most accumulated 309 seconds of hot fire testing and 118 starts/shutdowns. Long
duration testing was completed to characterize heat flux and high cycle fatigue (HCF) loading.
Large quantities of short duration tests were completed to evaluate thermal cycling impacts to the
combustor structure and evaluate low cycle fatigue (LCF) loading. The hardware experienced 118
LCF loadings on the combustor cooling passages, equivalent to the amount of thermal cycle starts
and shutdowns. An endurance test was completed at 60 seconds in duration, demonstrating
operation well beyond thermal steady state. Additionally, ~3.7 million HCF loadings were placed
on the combustor cooling passages, equivalent to the approximate amount of detonation wave
passes present for all of the WC 2.0 testing.
Predicted operating pressures ranged from 5 to 15 atm. The highest-pressure conditions
resulted in hot gas wall temperatures exceeding 1000°F on the outerbody of the combustor and
injector face temperatures peaking at 350°F. Water calorimetry was used to compute heat fluxes,
which were then compared to traditional rocket engine throat level heat fluxes calculated using
Bartz equations under average operating conditions. The outerbody heat fluxes reached up to 3.7
kW/cm², while injector face heat fluxes reached a maximum of 1.6 kW/cm². When compared to
Bartz throat level values, the outer-body heat fluxes varied from 0.9 to 1.6 times the throat level
values, and injector heat fluxes ranged from 0.3 to 0.5 times the throat level values.
A combined thermal and pressure loading fatigue assessment was completed that took into
consideration mean stresses and cumulative damage from the spectrum of loading events.
Traditional rocket combustor life is typically limited by the thermal cycles that can be placed on
the cooling channel hot wall. The fatigue analysis results highlight the reduction in available low
17

cycle fatigue life as RDE's experience larger thermal loads when compared to traditional rocket
combustors. Low cycle fatigue life will become especially challenging in higher chamber pressure
combustors where thermal environments are more extreme, and the ability keep hot wall
temperatures within acceptable levels is more challenging.
The study also highlights that the passing detonation wave provides a high cycle fatigue
(HCF) failure mechanism that is not present in traditional rocket combustors. This failure
mechanism is the result of the pressure pulse provided by the passing detonation wave causing a
variable load on the hot wall. This variable load is applied at frequencies commonly in the 10's of
kHz, resulting in large quantities of loading cycles when operated at rocket like durations (>60
sec). This HCF failure mechanism is most impactful at larger chamber pressures where the
detonation pressure ratio causes peak pressures to be elevated, resulting in larger cyclic stresses
and strains in the hot wall. The results indicate that high chamber pressure combustors may
experience HCF life exceedances within seconds of operation.

18

INTRODUCTION

The world is becoming increasingly reliant on space assets. Whether it is a commercial
satellite providing communication services or a national security spacecraft collecting vital
intelligence, a propulsion system is required to reach the desired orbit or complete the mission.
The department of defense and the intelligence community are highly dependent on space
operations to assist in war time activities and assure the security of the Unites States. Improving
launch vehicle and satellite propulsion system performance directly correlates to more mass (or
quantity) on orbit for commercial and national security satellites, longer duration missions, and
longer ranges for missiles/interceptors.
Alternative propulsion devices such as rotating detonation engines (RDEs) offer the
potential for significant performance gains but their operability has only been demonstrated on
“battle hardened” laboratory devices for rocket applications. Global competition is increasingly
evident in this nascent technology and the U.S. trails Russia in critical aspects therefore justifying
accelerated development efforts. The objective of this research is to demonstrate cooling and
structural approaches that mature rotating detonation rocket engines (RDREs) to flight like
maturation levels. To accomplish this objective, operational environments unique to RDREs will
need to be characterized to permit a successful design solution. Furthermore, this research will
evaluate additive manufacturing (AM) techniques to determine if printed hardware can be reliably
and cost-effectively implemented in an RDRE.
Modern conventional rocket engines operate with deflagrative combustors and combustion
efficiencies greater than 99%. Advancements to constant pressure devices offers only marginal
efficiency gains and little to no performance gain realizable when evaluated at the propulsion
system level. Alternatively, RDE’s are pressure gain based combustion devices with one or more
detonation waves traversing an annular chamber in the azimuthal direction as depicted in Figure
1a. The detonation wave(s) continuously rotate around the combustion chamber annulus,
combusting fresh reactants that provide the energy necessary to propagate the supersonic flame
front as depicted in the “unwrapped RDE” schematic shown in Figure 1b. The pressure gain
realizable from an RDE can be attributed to the thermodynamic gains available from the Humphry
cycle compared to the Brayton cycle used to model constant pressure devices [34]. When operated

19

at rocket conditions, studies have shown these thermodynamic benefits can result in specific
impulse gains up to 10% [10].

Figure 1.1. (a) RDE Operating Configuration [1] (b) Unwrapped Visualization of RDE Operating
Principles [33]
At Purdue and most other institutions evaluating RDRE’s, heat sink cooled copper
hardware with large factors of safety have been employed for short duration testing. Though the
air breathing propulsion community has begun to evaluate flight weight RDE combustion
chambers, they operate at much lower chamber pressures and detonation pressure ratios than
RDREs. The severity of the environments that need to be maintained in the RDRE are evident in
hardware damage sustained across multiple hot fire test campaigns at Purdue University. Figure
2a shows a damaged center body of a triglyme/hydrogen peroxide propellant RDRE at Purdue
after 2 hot fires, each 1 second in duration [35]. The damage indicates that chamber pressures
mechanically extruded the copper center body. Figure 2b represents a damaged copper fuel injector
ring operated in a gaseous oxygen/kerosene RDRE also at Purdue [36]. Researchers concluded
that the pitted damage notable on the fuel injector was due to softening of the copper material at
high temperatures and high pressures heavily deforming the material at the free surfaces, especially
at regions of high stress concentration [36]. The damaged hardware from both test cases indicate
that detonation peak pressures are exceeding the 2,500 psi yield strength of the ¼ work hardened,
oxygen free high conductivity (OFHC), copper hardware, operating at combustor-like wall
temperatures of 1,000 deg F [43].

20

Figure 1.2. (a) Center Body Damage During Liquid Bi-Propellant RDRE Testing at Purdue
University [35] (b) Fuel Injector Damage During GOx/Kerosene RDRE Testing at Purdue
University [36]
Flight weight RDREs will not only need to withstand the peak detonation pressures
described above but also the cyclic thermomechanical stresses from the continuous rotation of the
detonation wave. Detonation wave front speeds are known to exceed 6,500 ft/sec in rocket
applications resulting in wave arrival frequencies commonly exceeding 10 kHz [36]. Boost phase
propulsion systems typically operate in excess of 200 seconds which would result in over
2,000,000 cycles on an RDRE chamber for a single mission. Likely the most fatigue sensitive
feature on the RDRE will be regenerative cooling jackets necessary to maintain acceptable wall
temperatures in the combustor. Even in constant pressure combustors, the thin structures between
adjacent cooling jackets experience high stresses and are prone to cracking and failure [37]. RDRE
regenerative jacket designs will need to be strengthened to withstand elevated peak stresses and
high cycle fatigue loading. Furthermore, with detonation wave speeds approaching sound speeds
in typical wall materials, resonance frequencies within the regenerative jacket webs may need to
be isolated from wave pass frequencies to avoid exciting a structural mode.
Typically rocket combustor life estimates are based on low cycle fatigue (LCF) induced by
the thermal expansion and resultant stresses in the hot wall as the combustor reaches steady state
temperature. In traditional rocket combustors, thermal stresses typically surpass mechanical loads,
especially when operating at high pressures. Consequently, the lifespan of many combustors is
dictated by the quantity of start/shutdown cycles. This is the case for the Space Shuttle Main
Engine (SSME) which is estimated to have a life of ~400 start/shutdown cycles [41]. Other, more
conservative estimates estimate standard combustor lives can be as low as 60 start/shutdown cycles
[42]. Currently, there exists no publicly available data on high cycle fatigue (HCF) or low cycle
fatigue (LCF) for RDE combustors, which serves as a major impetus for this study. It is expected
21

these results will be exacerbated by the larger thermal loads and mechanical loads driven from the
passing detonation waves in RDEs.
Additive manufacturing (AM), specifically selective laser melting (SLM), offers a
potentially affordable manufacturing solution for an RDRE injector assembly and regenerative
cooled chamber with the recent and rapid advancements in build size capabilities, surface finishes,
and printable feature sizes. The advancement in SLMs usability in rocket applications is evident
by its use in firms like Aerojet Rocketdyne, SpaceX, and Blue Origin for injector designs [37].
NASA’s Marshall Space Flight Center has used AM techniques to build and hot fire test hardware
in sizes ranging from 100 lbf to 35,000 lbf. One goal of this research will be to explore SLM
techniques and vendors to assess their ability to manufacture high performance metals such as
copper alloys that can be applied to RDREs.

22

TEST ARTICLE AND FACILITY SETUP

To facilitate an understanding of the thermal and structural characteristics in a an RDRC,
a combustor was required that provided the capability to complete long duration testing. A list of
design objectives were developed to guide the development process and are listed below:
•

A small scall combustor able to achieve modest rocket like combustion conditions (~150
psia) was required to reduce manuacturing cost and the commodities consumed each test

•

An active cooling system is required to support long duration testing (~100 sec) so that
thermal and structural performance can be evaluated

•

Temperature of the coolant inlet and outlet is required to be collected so that a calorimetry
assessment can be completed

•

A proven injector design and simple propellant combination with previous test experience
was required to reduce the facility complexity and focus the study on cooling and structural
concerns rather than performance
With these overall design objectives in mind, multiple approaches were evaluated. The

first design was a traditionally manufactured combustor with modular cooling liners aimed at
evaluating different cooling channel geometries. The second design was a combined
manufacturing approach (traditional and additive components) aimed at reducing the quantity of
parts and eliminating sealing challenges encountered with with the traditionally manfuctured
design. The third design was an entirely additively manfuctured approach aimed at reducing
complexity and the time required to manufacture. Each design was matured to a critical design
review (CDR) level and a trade study was completed to determine which approach to utlize for
this study. Ultimately the entirely additively manufactured combustor was selected as the test
hardware. A summary of each design, the down select trade study, and the test hardware is
provided below.

23

2.1

Traditionally Manufactured Approach

The traditionally manufactured hardware was designed with modularity as the key
objective. The original design objectives envisioned a replaceable cooling liner that could be used
to evaluate different cooling channel aspect ratios their associated cooling and structural
performance. In reality, the modularity approach in an actively cooled RDRC drove significant
complexity and cost into the design and opened risks with potential impacts to the study objectives.
An overview of this design can be found in Figure 2.1 and Figure 2.2. This design resulted in ten
major components, most having critical clearances and sealing surfaces required for successful
operation. Twenty fluid connections were required to provide fuel, oxidizer, and coolant to the
injector face, outerbody, and innerbody.

Figure 2.1. Traditionally Manufactured RDRC Cross Section
The original outerbody diameter was desired to be around 1 in but was driven outboard to
accommodate cooling supply passages to the innerbody, seal glands between the
injector/outerbody/innerbody, and traditional machining/tooling approaches. The impact to design

24

size based on seal size cannot be overstated and may be best described in the following example.
A common non-cryogenic seal choice of Viton with cross sectional thicknesses of 3/32 in. or larger
are recommended in propulsion devices to provide enough sealing material to accommodate
coefficient of thermal expansion mismatches between components. Recommended face seal gland
sizes for this size seal results in the following minimum dimensions: .070 in. depth and .120 in.
width (1). Three face seals were required to isolate hot combustion gases from the cooling system,
supply coolant to the innerbody, and return coolant from the innerbody. Simply accounting for
gland width limits the combustion chamber inner diameter to nearly 0.75 inches. Including a
reasonable wall thickness of 0.05 in. between ports/glands and port sizes of 0.15 in. increases this
diameter another 0.75 in., resulting in a minimum innerbody diameter of 1.5 in. Accommodating
fastening hardware will further increase this diameter. These items considered may pose a
considerable challenge to the combustor designer considering traditionally manufactured
approaches for RDRC in-space propulsion systems or attitude/reaction control system propulsion
systems.
The outerbody of a traditionally machined actively cooled RDRC is the most flexible area
of the combustor in terms of design choices. The outerbody offers numerous locations to
accommodate manifolds and is not restricted in outboard size other than weight and port/fitting
needs. In a laboratory setting weight is not a concern and ports and fittings can easily be
accommodated. The outerbody design is shown in Figure 2.2 and Figure 2.4 below. The manifold
were designed to accommodate both axial coolant channels (coolant moving from injector face to
combustor exit) and circumferential coolant channels (coolant flowing around the circumference
of the RDRC body). The clamshells were placed between the manifold and coolant liner to support
multiple passage dimensions and aspect ratios. The clamshells were designed to be easy to
manufacture and would be machined to fit for different liner designs. Circumferential cooling
channels offer the ability to calorimetry assessment at multiple axial locations on the chamber and
characterize the heat flux distribution. This same methodology can be used on axial cooling
channel designs, but thermocouples would need to be placed within the coolant flow at axial
stations along the channel presenting flow disturbance and sealing challenges.

25

Figure 2.2. Traditionally Manufactured RDRC Outerbody Design
The cooling channel liner shown in Figure 2.4 was the primary component under
evaluation for the study. This liner represents the axial cooling configuration. The part would be
formed to size on a lathe and then cooling passages would be milled into the liner at the desired
aspect ratio and rib size determined from the cooling analysis. To accommodate the combustor
heat load, this part would likely be manufactured from oxygen free high conductivity (OFHC)
copper or a higher strength copper alloy. Material selection is discussed in greater detail in
Chapter2.6. The supply and exit passages were built into the clamshells and accommodated
through the manifold. Leakage from supply to exit was blocked by two piston seals that seated
between the clamshell and manifold. Leak paths existed from passage to passage as they were not
closed out but rather clearance fitted with the clamshell. Other options exist such as brazing or
electron beam welding a closeout material overtop the cooling passages. Closeouts can also be
accommodated through electroplating a high strength alloy overtop the cooling passages. These
options were not considered due to added cost, complexity, and the need for a risk reduction
qualification program to prove out the manufacturing process. Additionally, these options do not
allow the part to be disassembled and reconfigured to support the modular design approach. The
design quickly became overly complex to accommodate multiple cooling configurations.

26

Multiple operational risks existed with this complex outerbody design. Buckling was a
concern due to the high-pressure coolant causing large stresses on the mid span of the liner due to
the closeout approach not structurally attaching to the ribs. A detailed structural finite element
analysis (FEA) was not completed for this study. Estimates for buckling were completed using the
approach outlined in NASA SP-8007, Buckling of Thin-Walled Circular Cylinders [14]. These
results can be seen in Figure 2.3 with 1000 psia coolant highlighted in blue and no factors of safety
applied to the data. Typical hot wall thicknesses range from 0.025 in. to 0.040 in. in rocket
combustors with the results indicating that structural challenges exist in this range. Passage to
passage leakage was also a concern due to the passage not being closed out. Coolant pressure could
cause the liner to flex off its clearance fit at the mid span causing the flow area to increase and
coolant velocity to decrease. Decreased coolant velocity results in considerably lower critical heat
flux and increases the risk to boiling and hot wall burn through. Attaching the liner and sealing it
through piston and face seals presented multiple failure prone seal locations and a sandwich
approach.

Figure 2.3. Outerbody Cooling Liner Buckling Evaluation

27

As shown in Figure 2.2, the cooling liner was constrained from transmitting axially by the
closeout plate. The closeout plate sandwiched the cooling liner into place with fasteners that pass
through the outerbody manifold and thread into the injector head. The copper cooling liner, having
an approximate CTE of 9.7x10^-6 (in/deg F), could lengthen nearly 0.010 in. at combustor
operational temperatures. With the clamshell, manifold, fasteners, and closeout plate were to be
manufactured from a steel alloy for strength margin. With the steel components remaining at
considerably lower temperatures due to their location and possessing orders of magnitude lower
CTE’s, the liner thermal expansion alone could induce enough stress to flex at the midspan and
reduce coolant flow area.
Pressure measurement in the small RDRE chamber volumes with highly convective
environments has proven to be very challenging.

Flush-mounted high frequency pressure

transducers have been immediately consumed and the larger cooled high frequency devices present
substantial blemishes in the chamber contour thus altering wave character [8]. Helium purged
high frequency transducers have survived, though the helium alters the local sound speed [8]. For
these reasons, the community has had to rely on capillary tube average pressure (CTAP)
measurements where transducers are stood off from the chamber by a length of tubing that gets
charged to the average pressure produced in the combustor.
Heat sink RDRC designs in the laboratory setting typically collect CTAP measurements
through the outerbody wall. Though achievable, installing passages through the innerbody and
injector face presents accessibility, sealing, and porting challenges. This challenge becomes even
greater when dealing with an actively cooled injector face or innerbody due to the amount of
manifolds required to distribute coolant. Collecting CTAP measurements, even through the
outerbody, presents risks in an actively cooled RDRC. Firstly, a hole in the outerbody wall presents
a hot gas stagnation point and localized increase in hot wall temperatures. With no active purge
through this port, acceptable hot wall temperatures may exceed allowable limits when employed
in long-duration firings. Adding an active purge presents additional operational complexity and
uncertainty to the pressure measurement. Secondly, porting into the hot wall is required through a
cooling rib. For example, the space shuttle main engine (SSME) cooling rib thickness is .04 in and
the rib thickness in Figure 2.4 is 0.05 in [2]. Porting through this rib with a reasonable hole size,
let alone accommodating a seal cannot be accommodated with any known seal/seal gland
combination. Wrapping cooling channel passages chamber pressure port is possible but causes

28

significant complexity on machining operations (likely going from manual milling operations to
computer numerical control [CNC] operations) and causes a coolant flow disturbance that impacts
pressure drop.

Figure 2.4. Traditionally Manufactured RDRC Outerbody Cooling Liner Design
Traditional actively cooled rocket engine combustor designs recess the cooling passages
behind the injector face or provide film cooling around the injector head. In the RDRE application,
film cooling has not been employed (to the authors knowledge) for fear of parasitic deflagration
of the fuel inhibiting detonative behavior. Implementing film cooling into this study would limit
the accuracy of the calorimetry data due to the extra cooling provided by film cooling.
Additionally, gaseous propellants were desired for facility simplicity and they offer limited film
cooling capacity. Recessing the cooling passages behind the injector face allows the coolant to be
at the design velocity as it reaches high heat flux zones within the combustion chamber.

29

Accommodating recessed passages on a traditionally machined RDRC was found to be unfeasible
without a special seal design. Depending on injector configuration, these passages will likely need
to taper outboard to accommodate injector elements. Accommodating a seal on this tapered surface
was determined to high of a risk to pursue, especially when this sealing surface would see hot gas.
Even without a complex seal glad, a seal in this location would be at risk of failure due to hot gas
exposure. Operational rocket engine programs go to great lengths to avoid sealing hot gas
locations, and if it is unavoidable, it is often bathed in coolant or custom manufactured from a high
temperature insulative material. Bathing a seal in coolant was considered too complex for this
study and pursuing a custom high temperature seal was too costly and lead times were unknown.
These items considered, a recessed passage was not pursued face seals were baselined as the hot
gas seals with an attempt to place as far from hot gas location as possible.
The innerbody and injector of a traditionally machined actively cooled RDRC are
considerably more challenging than designing the outerbody. The coolant flow paths for the
innerbody and injector designs for the traditionally machined approach can be seen in Figure 2.5.
Along with the challenges experienced on the outerbody, the addition of how to provide and return
coolant to the innerbody even further complicates the design. Coolant can only enter and exit
through to the center of the innerbody as all other locations on the innerbody experience hot gas
or are located on the exhaust side of the combustor. As a rule of thumb, coolant manifolds are
recommended to be 1.5 times the flow area of the total flow area for the passages be being supplied.
Accommodating a manifold of this size without a welded closeout was found to be
unfeasible in this design. Employing a welded innerbody assembly doubled the cost of the part
and required weld samples to achieve as only electron beam (EB) welding can be used on OFHC
copper and maintain its structural properties at an appropriate level (Meyer Tool, Personal
Communication, Dec, 2020). Additionally, the welded assembly would need to be pressurized with
water to assess for leaks prior to assembly. As show in Figure 2.6, welded joints for the closeout
plates were required to be close to the hot wall to adequately feed the cooling passages from the
assembled manifold. This left limited surface area between the two metals being joined and opened
risk that the EB weld would be successful.
Design of a sealing mechanism for the innerbody proved to be challenging. The supply and
exit ports for the innerbody cooling system would each need face seals. A face seal would also be
needed to isolate hot gas from the combustion chamber migrating between the innerbody and its

30

seat on the injector face. Seal glands could not be placed on the innerbody because of the depth
required to accommodate the seal’s cross section. This depth directly correlated to how thick the
supply closeout plate was which in turn impacted how close to the injector face the cooling passage
could start. Considering these items, seals glands were placed on the injector face side. It was
desired to place the hot gas seal as far inboard as possible, increasing its change to survive long
duration test conditions. How far this seal could be moved inboard was limited because of the area
required to accommodate supply and exit port face seals.

Figure 2.5. Traditionally Manufactured RDRC Innerbody and Injector Cooling Flow Paths
Innerbody cooling passages could only be produced via electron discharge machining
(EDM) or standard drilling operation. EDM offered the ability to for the traditional square passage,
making the hot wall thickness between the cooling passage and hot wall a more uniform thickness.
Additionally, EDM offered a more uniform hot wall thickness axially because the EDM head is
less likely to “wander” as it plunges through the material. Drilling operations are much more prone

31

to “wander” as the length over diameter ratio of the bit increases. With a .030” passage at a
minimum length of 1 in., it was very likely the bit would have deviated from the desired path
during the process. Non-uniformity in hot wall thickness opened risk for localized regions of
excess temperature and would increase the uncertainty of the calorimetry data.

Figure 2.6. Traditionally Manufactured RDRC Innerbody Cooling Liner Design
Traditional rocket combustors experience less heat flux into the injector face when
compared to the hot wall of the combustion chamber. This it attributed to the active propellant
flow out of the injectors, convectively cooling this location and maintaining the flame front away
from the injector face. Though hot gas recirculation does occur, it typically can be managed by

32

bathing the backside of the injector face in coolant. This is convenient for a liquid propellant rocket
engine as liquid coolants are in the vicinity of the injector face to reach their injector elements.
The heat load into the injector face is largely unknown in RDRCs and whether its
magnitude is larger or less than that experienced in the innerbody/outerbody hot walls has also yet
to be determined. Though propellant is supplied in similar manners as standard liquid propellant
rocket engines, it is unclear where the detonation wave is located axially in the chamber. Further
towards the injector face will most likely increase the heat load into the injector face and not offer
the same reduction in magnitude that a traditional rocket combustor experiences. Additionally, the
RDRC for this study utilizes gaseous propellants with no major benefit being using the propellant
to bathe the back side of the injector face. For a water cooled RDRC this requires fuel, oxidizer,
and water to be brought in close proximity at the injector face within the gap distance (typically
between 0.10 in. and 0.25 in. for current laboratory RDRE designs). To manufacture the injector,
the elements would be EDM’d and a slot for a cooling passage would need milled or turned into
the injector face. As shown in Figure 2.7, this passage would need closed out through an EB weld
process. For the chamber gap of 0.15 in., an oxidizer element of 0.040 in., a fuel element of 0.020
in., and a cooling passage of 0.030 in. width, only 0.060 in remained to complete the EB weld.
Initial discussions with EB weld vendors indicated that that the heat affected zone could distort
the injector elements or cause localized melting of element edges.

Figure 2.7. Traditionally Manufactured RDRC Injector Cooling Design
33

2.2

Combined Traditional/Additive Manufactured Approach

Because of the complexity, cost, and operational risk described in Chapter 2.1, a combined
manufacturing approach was then considered. A combined approach is one that has traditionally
machined components and additively manufactured components. Additive manufacturing offers
far more flexible design options and improved lead time. Furthermore, high strength copper alloys
such as the NASA developed GRCop-84 and GRCop-42 offer great combustion chamber
manufacturing materials due to their high thermal conductivity, high strength with respect to pure
copper, and good low cycle fatigue performance [16]. More detail on these materials are provided
in Chapter 2.6.
As shown in Figure 2.8, the additional design flexibility reduced size of the combustor and
the number of components. The primary reduction in size occurred in the outerbody diameter,
reducing from 2.6 in. to 1.2 in. This was solely driven by the elimination of seals which also
improved the reliability of the combustor and ease of assembly. The injector, innerbody, and
outerbody became one integral component (here forth called the integral combustor) which
eliminated the need for hot gas seals critical to the combustor’s operation. This integral component
could either have the fuel and oxidizer elements printed during the DMLS process or they could
be adding during the post machining process through EDM. EDM offers an improved surface
roughness within the injector element so a better discharge coefficient can be expected.
Additionally, tighter tolerances on element alignment, spacing, and location can be achieved
through the EDM process.

34

Figure 2.8. Combined Manufactured RDRC Cross Section
Axial cooling passages for the outerbody and innerbody would be printed into the integral
combustor. To simplify the design, the coolant would exit the aft end of the combustor and not be
manifolded and collected. Collecting the exit coolant into a manifold was considered but it reduces
the capability for powder to be removed and was therefore not pursued. To collect calorimetry, a
thermocouple would be plunged into the coolant stream exiting the combustor. One major
advantage of this design was the ability to recess the passages behind the injector face. This was
completed by angling the outerbody passages outboard at the same angle as the injector element
and angling the outerbody passages inboard at the same angle as the injector element. This recess
ensures the coolant is at the design velocity when it reaches the high heat flux zone of the
combustion chamber. The innerbody cooling manifold was designed into the printed component
with powder removal capable through the exits of the cooling passages themselves as well as the
port that supplies coolant to the manifold.

35

Figure 2.9. Combined Manufactured RDRC Cross Section
A cooling passage was also placed behind the injector face to collect calorimetry on the
injector face heat loads. This passage was horizontal to the print bed and could not be printed with
a standard square passage due to print overhang concerns. To accommodate this, multiple passage
cross sections are printable, including a diamond, upside down triangle, and tear drop shaped
passage. An upside-down triangle or diamond are printable and can match the angles of the
injectors and keep a constant wall thickness for structural concerns. Coolant incoming to this
passage would split and flow circumferentially around the backside of the injector face. The
coolant would then collect into a single port and exit the top side of the combustor. Placing a seal
around the supply and exit ports could not be accommodated with the seals already required
between fuel and oxidizer manifolds. That being said, the fuel and oxidizer face seals were used
to stop coolant from leaking overboard though a leak path did exist between supply and exit. This
was a risk, as the size of this leak path would be challenging to measure and control. To mitigate,
excessive coolant flow would have been used to accommodate any leakage from the sealing
challenge.

36

One challenge with the additive manufacturing process chosen, direct metal laser sintering
(DMLS), is removing powder following the printing process. Due to this concern, manifolds are
commonly added after printing to allow for access to internal passages for powder removal.
Manifolds can either be welded or brazed onto the printed component or the printed component
can be post machined to provide or accept a sealing surface. For laboratory settings, the sealed
approach allows the hardware to be disassembled and inspected through a flight solution would
likely have a welded manifold closeout. Two traditionally machined components were built into
the design to provide manifolding and manifold closeouts. The first, located on the top of the
combustor, provided manifolds for the fuel and oxidizer, along with the supply port for the
innerbody coolant. Seal glands were placed in this component to reduce the post processing
required on the printed hardware. The printing process results in a surface roughness of ~200-300
micro-in. depending on the vendor. The recommended surface roughness for sealing surfaces is
16 to 32 micro-in. (depending on seal design and fluid) so some post machining/polishing of the
printed component was still required to improve the surface finish of all sealed surfaces. The
second component, located around the outerbody of the integral combustor, was the outerbody
coolant manifold closeout. The manifold itself would be printed into combustor along with the
face seal required to seal the manifold from leaking. This face seal gland would be post machined
to improve surface roughness for sealing.

37

Figure 2.10. Combined Manufactured RDRC Components and Flow Paths

2.3

Entirely Additive Manufacturing Approach

The combined manufacturing approach offered a promising hardware solution for the study
due to reduced complexity and cheaper cost. The primary drivers for the combined approach were
to incorporate the capability for EDM of the injector elements, powder removal from manifolds,
and powder removal from cooling passages. With a majority of the combustor being additively
manufactured and only manifolds accommodated through traditionally machined approaches, a
study was completed to determine if the hardware could be entirely additively manufactured. In
the end, the entirely additive manufactured approach was selected as the study baseline and the
design is shown in Figure 2.11. As this study progressed, design alterations were completed to the
baseline design. The baseline design discussed in this section is referred to as Water Cooled 1.0
(WC 1.0). Other hardware configurations are summarized in Section 2.11 The primary drivers for
this decision were further reduction in the quantity of seals required for long duration operation
and the ability to print in adequate features for powder removal. Additionally, precision aligned

38

injector elements for RDRC’s may be less critical than traditional rocket combustors due to
detonation wave induced mixing. This reduces the need for precise EDM RDRC approach.

Figure 2.11. Additively Manufactured RDRC Cross Section (Water Cooled 1.0 Design)
Below is a list of additive manufacturing design rules of thumb that can be used as quick
reference. These rules of thumb represent recommendations learned through numerous discussions
and design reviews with additive manufacturing vendors in 2022. The additive manufacturing
community is rapidly advancing printer technology and these rules will change as the technology
advances. They are not applicable to any one vendor and should be reviewed with the vendor prior
to implementing. Additionally, these rules apply to GRCop-84 and GRCop-42 copper alloys and
may vary for different alloys such as Inconel.
•

Minimum printable hole diameters
o 0.045 in. prints reliably with most additive manufacturing vendors
o 0.025 in. prints reliably with limited additive manufacturing vendors
o 0.010 in. has been demonstrated with an additive manufacturing vendor

39

•

Minimum distance between holes before porosity becomes an issue
o 0.020 in. prints reliably with most additive manufacturing vendors
o 0.010 in. to 0.015 in. prints reliably with limited additive manufacturing vendors
o Anything smaller than 0.010 in. increases risk of porosity issues between holes

•

Minimum distance between a hole and a wall
o 0.020 in. prints reliably with most additive manufacturing vendors
o 0.010 in. to 0.015” prints reliably with limited additive manufacturing vendors
o Anything smaller than 0.010 in. increases risk of defected transition between hole
and wall

•

Maximum overhang angle for internal passages
o 30 deg from vertical prints reliably with most additive manufacturing vendors
o 45 deg from vertical prints reliably with limited additive manufacturing vendors
o Overhangs that are not internal features can be accommodated through a support
structure that can be post machined

•

Surface Roughness of surfaces that cannot be post processed
o Standard surface roughness within a straight passage is 150-200 micro-in.
o Flow passages that include overhangs (such as manifolds or canted passages)
expect increased surface roughness of approximately 300 micro-in.

•

Powder removal
o Larger passages with less turns result in easier powder removal
o Best approach is to print without manifolds so powder can be easily removed
o Manifolds can be welded or brazed on during post processing
o Manifolds can be accommodated through a sealed closeout though the sealing
surface of the printed part will need post processed to improve surface roughness

40

o Printing closed out manifolds introduces challenges for inspection and powder
removal; If decided to print manifold, have adequate holes/access to remove
powder
o Jammed powder can be removed with thin wire or in some instances a vibration
table
o If verification of powder removal is critical, a computerized tomography (CT) scan
is recommended as non-destructive test to visually confirm no powder remains
•

Passages horizontal to print bed
o Passages horizontal to print bed must be one of the following shapes to adhere to
the overhand rule: upside down triangle, diamond, or tear drop
o Large holes can be printed with support structures that can be removed with post
processing; The post processing machinist may prefer the whole to not be printed
so the drill bit does not attempt to follow the holes printed path, potentially breaking
the drill bit.

•

Post Processing
o If straight thread o-ring sealed ports (AS5202) are desired after printing, make sure
enough clearance exists in the design to accommodate the fitting depth and width
after porting
o A standard AS5202 porting tool is longer than is required to accommodate common
straight thread fittings; This tool can be shortened by a machinist to complete a
minimum depth port
o A purge plate/adapter can be used to put positive pressure on foreign object debris
(FOD) sensitive areas during post processing machining; This plate needs to be
considered during the design phase because it will need to seal in some location on
the combustor
o For combustors being used in the laboratory setting where high/low cycle fatigue
is not a concern, hot isostatic pressing (HIP) can be skipped; HIPing improves
ductility and fatigue response but also reduces the strength of the component

41

Additively manufacturing the injector elements in an RDRC approaches the limits in
printable hole sizes, porosity between the close proximity injector elements, and hole to wall
transitions. Traditional rocket combustors have nearly the entire circular chamber cross sectional
area to place injectors leaving room to vary injection angles and increasing distance between
injectors to lengthen or shorten the impingement point. RDRCs have a limited annular gap to place
the injector elements within as will be outlined in an example below. A doublet injector design
was chosen for this study as shown in Figure 2.11. Doublet injectors in RDRC’s have been widely
used in other designs with proven detonation combustion [3,4].

Figure 2.12. Additively Manufactured RDRC Propellant Flow Schematic (Water Cooled 1.0
Design)
For traditional rocket combustors, injector element angles are chosen to place the
impingement point in a location far enough away from the injector face that it remains cool but
close enough for adequate mixing. Injector element angles are also chosen to balance propellant

42

momentum such that the resulting fan is angled axially and not toward the combustor wall.
RDRC’s operate off the “design condition” for large portions of the detonation cycle. For example,
peak pressures within the chamber are experienced as the detonation wave passes the injector and
likely halts the flow of propellant into the chamber, assuming the injector feed pressure is not
adequate to overcome the detonation wave pressure. Following that pressure peak, the pressure
decays until the next wave pass and the element recovers to flowing propellant again. Balancing
momentum for the entire detonation cycle would be challenging, requiring varying feed pressures
on an operational timescale of kilohertz. For this study, a design pressure was chosen as the average
pressure within the combustion chamber and the injector elements were sized to support that
pressure. The approach outlined below is recommended to design doublet injector elements for an
additively manufactured RDRC with a reliable vendor. These guidelines were used to produce the
injector elements for this study with results outlined in Table 2.1.
• With propellants and desired performance chosen, set the injector diameter for the lower
flowrate propellant to a reliable print diameter of 0.025 in.
• Determine the number of elements required to support the desired injector stiffness
(manifold pressure/average chamber pressure)
• At the required number of elements, verify the spacing between each like element is greater
than 0.015 in to reduce the risk of porosity between elements
• Determine the largest hole diameter achievable for the other propellants injector element by
taking the RDRC gap length, subtracting the injector diameter chosen above, and
subtracting 3X the 0.015 in (accounts for reliably printed distance between holes with no
porosity and reliably printed hole to wall transition distance)
• At the number of elements chosen above, determine the injector stiffness required to support
this hole diameter
• If this stiffness is too low, reduce the hole diameter until injector stiffness is acceptable
• If this stiffness is too large, further discussion is required with the additive manufacturing
vendor to determine if the 0.015 in. value used between the element hole and wall as well
as from hole to hole can be relaxed.

43

Table 2.1. TSRDE Injector Element Design Values (Used in All Hardware Configurations)
Parameter

Value

Average Chamber Pressure (psia)

150

Fuel Diameter (in)

.025

Fuel Angle (deg)

30

Fuel Stiffness

(575 psia /150 psia) = 3.8

Oxidizer Diameter (in)

.041

Oxidizer Angle (deg)

30

Oxidizer Stiffness

(540 psia /150 psia) = 3.6

Element Quantity

22

Discharge Coefficients

0.60

The manifolds for the injectors are necessarily triangularly shaped as they are subject to
printing overhang constraints. The hardware is printed with the injector side facing the print bed
(aft end of combustor facing up). The triangular manifolds adhere to the 30 deg from vertical
reliable print overhang rule. The larger manifold was placed inboard so that porting to that
manifold would not be restricted by the smaller manifold located outboard. A rule of thumb for
propellant manifold sizing is to ensure the dynamic pressure divided by the total pressure within
the manifold is less than 1%. This requirement was strived for but not met within the fuel circuit
(1.2%) or the oxidizer circuit (2.6%). Each manifold included three ports: propellant supply, low
speed pressure transducer sense port, high speed pressure transducer sense port. These ports were
adequate to remove powder from the printing process.
The cooling system is illustrated in Figure 2.13 and Figure 2.14 with details on the passage
dimensions found in Table 2.2. The analysis used to select the passage sizes and determine the
required flowrate can be found in Section 3.2. These passage dimensions were chosen because
they provided adequate cooling results and could be printed reliably. In a flight-like RDRC design
with regenerative cooling, coolant (in this case fuel or oxidizer) will need to be collected after
cooling the chamber and routed to the injector. Collecting the coolant from the innerbody will
prove to be challenging as little room exists for return ports and manifolds. Exit manifolds for the
innerbody and outerbody likely need to be added after the printing process through a sealed or
welded/brazed approach. This adds additional cost and complexity to the design. To simplify this
44

study, no attempt was made to manifold the coolant exits for the innerbody and outerbody. Instead,
coolant was discharged out the aft end of the combustor. This simplifies powder removal from the
passages after the print process and provides a means to visually inspection of the passages to
verify coolant is flowing without blockage. Surface roughness for the injector cooling passage is
larger than the innerbody and outerbody cooling passages due to its orientation to the print bed
and internal overhang.

Figure 2.13. Additively Manufactured RDRC Coolant Flow Schematic (Water Cooled 1.0 Design)
The innerbody and outerbody cooling passages were not manifolded and exited the aft end
of the combustor to atmosphere. Additionally, each individual passage was restricted at the end to
backpressure the cooling system and increase the critical heat flux (CHF) of the coolant. This
approach required more supply pressure to achieve the desired coolant flowrate but facility supply
pressure was adequate to accommodate. Metering individual coolant passage exit streams greatly
simplified manufacturability of this test hardware, it also presented challenges that are discussed

45

extensively in Section 5. Collecting coolant exit temperature in a manifold permits measurement
of the average coolant exit temperature of all the coolant passages that flow into the manifold. If
variations in passage dimensions exist which impact the coolant flow in each passage individually,
the local coolant exit temperature may vary from passage to passage.
The innerbody and outerbody cooling passages are perpendicular to the build plate except
for the portions of the cooling passages that recess behind the injector face. In this location, the
passages are angled 30 degrees of the vertical axis both inboard and outboard for the innerbody
and outerbody, respectively. The outerbody passage manifolds are triangular to support the 30
degree of vertical printing concern. In the outerbody cooling system, two ports for coolant supply
and one port for a supply pressure measurement exist in this manifold to support powder removal.
In the innerbody cooling system, a single port exists for powder removal. With combustors of this
size, little room exists for ports to the innerbody. Providing additional ports to the innerbody for
pressure measurements, additional supply, or coolant return is challenging with the limited space
to accommodate. A rule of thumb for manifold sizing is that the cross-sectional flow area within
the manifold equals 1.5 times the total cross-sectional area of the cooling passages (T. Teasley,
Personal Communication, April, 06, 2021). This rule of thumb is to ensure that the manifold
completely fills and distributes coolant evenly to every coolant passage. Both the innerbody and
outerbody manifolds meet this criterion.

Table 2.2. Cooling Passage Design (Water Cooled 1.0 Design)
Parameter

Innerbody

Outerbody

Injector

Passage Dimensions
# of Passages

Square 0.030 in x
0.030 in
49

Square 0.030 in x
0.030 in
67

Triangular, Base = 0.073
in., Height = 0.060 in.
1

# of Passes

1

1

½ Circumference

Hot Wall Thickness
(in)
Rib Thickness (in)

0.040

0.040

0.050

.05

.05

N/A

Channel Roughness

200 micro-in

200 micro-in

300 micro-in

The injector face cooling system is comprised of a single passage located in between the
doublet injectors. Coolant incoming to this passage is provided from a single port and then split to

46

flow circumferentially around the backside of the injector face. The coolant would then collect
into a single port and exit the top side of the combustor. Supply and exit ports were printed into
the design eliminating the sealing challenges and leak paths discussed in Section 2.2. Like the
combined manufacturing approach defined in Section 2.2, this passage is parallel to the print bed
and cannot be the traditional square square/rectangular passage due to additive manufacturing
overhang challenges. The passage was printed as a triangle as shown in Figure 2.13 to support
printing overhang requirements. Even though additive manufacturing greatly improved the ability
to locate this passage, the designer is still limited in how close it can be placed to the injector face
in a doublet-oriented injector arrangement. This is primarily driven by the injector hole size and
spacing which are both limited by the additive manufacturing capabilities and the gap width chosen
on the engine. If heat fluxes on the RDRC injector face are determined to be larger than a traditional
deflagrative rocket engine, challenges will exist on where cooling passages are placed which will
need to be traded with the injector concept chosen.

Figure 2.14. Innerbody and Outerbody Cooling System Passages (Used in All Hardware
Configurations)

47

As show in Figure 2.15, an attempt was made to print instrumentation ports. These ports
included a chamber pressure passage through the cooling passage land and two passages into the
cooling channel to collect coolant temperature and pressure. All three ports failed to print as the
hole size was below the recommended minimum and horizontal to the additive manufacturing
build plate. Holes that are horizontal to the build plate are subject to overhang angle limitations.
No attempt was made to post process the printed holes to avoid damaging the cooling passages or
cooling ribs.

Figure 2.15. Pressure and Temperature Measurements (Water Cooled 1.0 Design)

2.4

Combustor Sizing

The intent of this study was not to develop the smallest RDRC but rather keep the size small
to reduce manufacturing costs and commodity consumption. That being said, the author did not
want to reduce the size below designs that had been tested, adding risk to the operability of the
study. The primary concern in reducing combustor size was introducing operational instablity due
to the amount of curvature the detonation wave must go around [12]. Another size limiting factor

48

includes detonation cell size which varies by propellant and initial mixture pressures, as shown in
Figure 2.16 [12]. The sizing guidelines published by Bykovskii et al. were primarily driven by this
consideration [9]. Though these guidelines offer sizing estimates, they were derived from
operational pressures lower than rocket like conditions and not expected to drive design size at the
chamber pressures expected during this study. Figure 2.16. highlights this, with few-millimeter
cell sizes expected at operational pressures expected during this study and even smaller cell sizes
at high chamber pressures [12]. Nonetheless, the Bykovski sizing criteria at 1/3 the planned
chamber pressure and propellants under consideration were used to develop a minimum design
size constraint as outlined in Table 2.3. This was considered a conservative approach to verify
operational limitations would not exist for this study.

Figure 2.16. Detonation Cell Width of Various Mixtures [12]

Though the results in Table 2.3 indicate an outer diameter of 0.98 in is feasible, the
minimum diameter experimentally operated by Bykovskii was 40 mm (1.57 in). To the authors
knowledge, the smallest diameter RDRC operated was by Fiorno et al. at 28 mm (1.1 in) in outer
diameter [11]. The combustor operated on Ethylene-Nitrous Oxide with a chamber gap of 2 mm
(0.079 in) and achieved stable one wave modes at multiple operating conditions [11]. Though

49

differences exist in the propellant choice, injection scheme, and chamber design, the diameter
operated by Fiorno et al. was considered as the minimum limitations for this study as they
experimentally verified sustained detonation. With minimum design size bounds, the performance
model by Stechmann et al. was used to determine commodity flowrates vs. chamber pressure [10].
The results from the selected configuration for this study are presented in Figure 2.17 below.

Table 2.3. RDRC Minimum Sizing Constraint Using Bykovskii Criteria
Parameter

Value

Propellant

Gaseous Oxygen/Gaseous Methane

Average Chamber Pressure (psia)

50 psia (1/3 of the planned 150 psia)

Minimum Length

17 mm (0.67 in)

Annulus Gap

1.68 mm (.067 in)

Outer Diameter

25 mm (0.98 in)

Figure 2.17. Chamber pressure vs Propellant Flowrate

50

2.5

Ignition System

With most of the RDRC community focused on short duration heat sink testing, ignition
systems are often an afterthought in the design process. The heat sink community uses multiple
methods to ignite RDRC’s including variations of augmented spark igniters and pre-detonation
ignition systems [5,6]. Hypergolic ignition systems are not commonly used in a university setting
due to the challenges working with hazardous chemicals. For each of the variations, the igniter is
typically placed through the sidewall of the combustor or back lite from the aft side of the
combustor. Ignition from the backside of the combustion chamber is convenient because it can be
accomplished without holes or alterations to the combustor design. This is preferable, as alterations
to the igniter to support different schemes can be supported with minor modifications to the RDRC
hardware. Ignition through the outerbody sidewall occurs through a hole in the heat sink chamber
wall. This is also easy to accommodate as the heat sink chamber wall is typically made from easily
machinable copper and multiple axial locations down the chamber can be accommodated.
Placing the igniter, through the side wall of an actively cooled combustor is challenging
due to the cooling channel configuration. Cooling channels will need to cover the entire surface
area of the RDRC hot wall, whether that is accommodated through axial, circumferential or helical
channels. In either case, the distance between cooling channels is typically small, on the order of
0.05 in. This small section is called the rib which provides structural support to the chamber and
helps to cool the combustion chamber through finning. Bringing an igniter through the outerbody
sidewall of an RDRC would likely require it to port through a cooling channel rib. Because the
ribs size is small, this would require the port diameter to be even smaller and limit the capability
of the igniter. Additionally, this port may also be in a high heat flux zone, putting the hole thermally
at risk.
For both the conventionally manufactured RDRC discussed in Section 2.1 and the
combined manufactured RDRC discussed in Section 2.2, the ignition system would have been
placed at the aft end of the chamber. This would have been chosen to reduce the complexity of
how the cooling system would accommodate an ignition system through the side wall. To date,
the author has not discovered an RDRC ignition system that penetrates the injector face. Bringing
an ignition system through the injector face of an RDRC is challenging due to the limited space
available. The space is driven by the annulus gap, the injector configuration, the injector spacing,
and the injector diameters. Aside from limited space, a traditionally machined RDRC also has

51

porting challenges with this configuration. Often located directly behind the injector face are
propellant manifolds and numerous seals to accommodate the manifolds. Placing an igniter
through this area is challenging and sealing the port that feeds the igniter flame/hot gas presents
even more challenges.
Additive manufacturing offers many more ignition configurations than a conventionally
machined approach, especially when considering ignition through the injector face. The entirely
additively manufactured RDRC chosen for this study utilized an ignition system through the
injector face. A pre-detonation system similar to the one used by Lim [7] was used as the ignition
source. The pre-detonation system shown in Figure 2.18, was spark ignited after being filed with
a timed charge of hydrogen and oxygen. The pre-detonation system was located outside of the
RDRC, and the exhaust products were delivered to the RDRC combustion chamber with a ¼ inch
stainless steel tube.

Figure 2.18. Pre-Detonation System [7]
The fitting that supplied the backside of the injector face was tapped to accommodate
threads to form a Shchelkin spiral for deflagration to detonation transition. This detonation wave,
along with hot exhaust products, then initiated the combustion process in the RDRC. This method
was preferred over an augmented spark igniter due to simplicity of operation and its successful use
52

on other RDRCs [6]. The passage that supplies the pre-detonation charge to the RDRC chamber
is shown in Figure 2.19. This passage was placed between two pairs of injector elements and had
to be accommodated by the injector face cooling passage. The cooling passage was wrapped
around the igniter supply passage as shown in Figure 2.20. Despite having a cooling passage
wrapped around the supply port, concern remained that the igniter port would back fill with hot
combustion gas and potentially cause a localized failure. To mitigate this, a flowrate metered purge
is supplied to this port after the ignition charge is supplied. This purge was sized to remain choked
and remains active during the entire portion of the test. The flowrate typically results in 5% of the
total propellant flowrate.

Figure 2.19. Pre-Detonation Ignition System Passage to Combustion Chamber (Used in All
Hardware Designs)
One concern was whether a detonation wave would exist by the time it reaches the
combustion chamber after being initiated in the pre-detonation system. As shown in Figure 2.16,

53

a hydrogen-oxygen mixture at 100 psia (6.8 atm) results in a detonation cell width on the order of
0.010 in (0.25 mm) [8]. This initial gas pressure was targeted for the test campaign. This cell width
is well below the ¼ in. diameter tube between the pre-detonation system and combustor indicating
that a detonation wave has the capability to exist. Additional concern existed in the length of tubing
and bends required to connect the pre-detonation system to the combustor. The tubing length was
~1.5 feet, with 4 bends of approximately 30 deg. Other pre-detonation systems operated at Zucrow
Laboratory have used tubing lengths on the order of 6 feet and still achieved ignition. Hence, the
overall L/D of the flow-path for the detonation wave is likely on the order of 1/576. In conclusion,
it is unclear whether a detonation wave is igniting the mixture within the chamber or hot gases
from a detonation process. Nonetheless, as discussed in Chapter 4 and Chapter 5, repeatable
ignition was achieved.

Figure 2.20. Cooling Jacket Accommodation of Pre-Detonation Ignition System Passage (Used in
All Hardware Designs)

54

2.6

Material Selection

GRCop-84 was used to additively manufacture the hardware tested for this research. This
includes HS 1.0, HS 1.1, WC 1.0, and WC 2.0. GRCop-42 was used to manufacture WC 2.1 but
was not hot fire tested. GRCop-84 and 42 were selected as the manufacturing materials at the time
of this research as they were the most common and commercially available material for additively
manufacturing rocket combustors. Both materials were developed by NASA for high heat flux
applications and key attributes include high thermal conductivity and mechanical strength. These
attributes make them great choices for rocket combustors where efficient dissipation of heat is
required along with structural integrity. A detailed discussion of both alloys along with their
thermal and mechanical properties can be found in Chapter 6.

2.7

Heat Sink Combustor

Because of the complexity with operating a cooling system, a heat sink RDRC was also
utilized during the test campaign. This combustor was used to develop start sequences, shutdown
sequences, measure chamber pressure, and to image the detonation wave through the aft end of the
combustor not obscured by water flow exiting coolant channels. This combustor was the exact
same design as the additively manufactured combustor discussed in Section 2.3, but the cooling
system was removed from the design. This combustor is referred to as Heat Sink 1.0 (HS 1.0). As
discussed in Section 2.3, the chamber pressure port failed to print in the actively cooled hardware
and no attempt was made to conventionally machine in a passage. Additionally, the actively cooled
combustor ejected water out of the aft end of the combustor. This water impinged on the mirror
system used to capture high speed footage of the detonation wave and did not allow footage to be
captured. The heat sink combustor served as a platform to characterize performance through high
speed imaging capability, chamber pressure measurements, and high frequency manifold pressure.
As discussed in Chapter 4 and Chapter 5, these performance correlations were used to justify the
performance of the actively cooled hardware during long duration testing.

2.8

Post Processing

Post processing of the combustor included straight thread porting, high frequency pressure
transducer porting, and sanding of the combustion chamber hot wall to reduce surface roughness.

55

Straight thread ports were post machined to accept AS5202-2 fittings. A custom straight thread
tool was used with a minimum depth to accommodate close proximity port to manifold depths.
Straight thread fittings were used in the fuel manifold, oxidizer manifold, coolant manifold, and
ignition system. PCB 102-B pressure transducers were used and their metallic sealing interface
were also post processed into the hardware. The high frequency pressure transducers were
accommodated in the fuel and oxidizer manifolds.
Porting introduces the potential for introduction of chips/debris into the combustor filled
with tiny features and this operation was conducted with utmost care from a skilled technician. To
prevent machining foreign object debris (FOD) ingress during post processing, a sealed purge plate
was designed to attach to the aft end of the combustor and provide positive pressure to all
manifolds. Accommodating post processing with critical internal passages in an additively
manufactured part is one major down side to the printing process.
Careful machining is required, and care must be taken not to let FOD ingress into internal
passages. Following machining it is recommended to reverse flow all critical passages towards
their manifolds and out of their supply ports. This is an attempt to remove any FOD deposited
during the machining process. Surface roughness from the additive manufacturing process can
range from 150-350 micro-in. depending on the build feature and the vendor. Excessive surface
roughness on the hot wall can increase the heat load into the cooling system. That being said, 1000
grit sand-paper wrapped around a dowel rod was used to smooth the hot wall surface. Due to
limited ability to access the hot wall a quantitative evaluation of the surface finish could not be
completed.

2.9

Water Flow Results

Following the additive manufacturing process, all passages were water flowed to verify
powder was adequately removed. Figure 2.21, Figure 2.22, Figure 2.23, and Figure 2.24 show the
water flow results for the innerbody cooling system, the outerbody cooling system, the oxidizer
injector, and the fuel injector respectively. This evaluation was qualitative, simply to verify water
was flowing, with no attempt to measure any flow characteristics. A clogged cooling passage on
the outerbody was identified as circled in Figure 2.22. This clogged passage was remediated
through additional powder removal attempts by the vendor. Additionally, the fuel injector elements
in Figure 2.23 appeared to have a more dispersed flow pattern than the oxidizer injector elements
56

in Figure 2.24. The fuel injector elements were printed at a hole diameter of 0.025 in. while the
oxidizer elements were printed at a hold diameter of 0.041 in. Both elements were printed at the
same 30 deg angle from vertical. It is unclear whether an actual issue existed with the hole size
due to limited inspection capability or if the water flow results were construed because of the
reduced flowrate in the fuel circuit. As discussed in Section 2.3, impinging element alignment is
critical for traditional rocket combustors but may be less crucial for RDRC’s due to detonation
wave induced mixing. As this study was not focused on RDRC performance, no attempt was made
to correct this issue and successful detonation operation was achieved.

Figure 2.21. Innerbody Cooling System Water Flow Results (Water Cooled 1.0 Design)

57

Figure 2.22. Outerbody Cooling System Water Flow Results (Water Cooled 1.0 Design)

Figure 2.23. Oxidizer Injector Water Flow Results (Water Cooled 1.0 Design)

58

Figure 2.24. Fuel Injector Water Flow Results (Water Cooled 1.0 Design)
2.10 Manufacturing Approach Trade Study Conclusion
A summary of the trade study findings can be found in Table 2.4 below. The most notable
finding was the reduction in cost for the fully additively manufactured combustor, approaching
nearly 1/5th the cost of a traditionally machined combustor. In a laboratory setting, low cost is an
important feature as exploring test conditions often push the operational limits of hardware. In a
flight like design, reliability is often a key priority. The fully additively manufactured combustor
also offers substantial benefits over the traditionally manufactured combustor in this regards due
to the reduction of required seals and close tolerance assemblies. One major drawback of the fully
additively manufactured combustor is powder removal. In a laboratory setting, this can be
accomplished by water flowing the hardware but flight hardware this typically requires a CT scan
to verify powder is fully removed. Flow passage surface roughness less than 50 micro-inches can
be accommodated when traditionally machined. Printed surface passages are typically between
150-350 micro-in. depending on the build feature and the vendor. These values greatly impact
pressure budget and will be heavily considered in flight builds. This study was completed in a

59

laboratory setting with more than adequate pressure budget on all commodities. That being said,
surface finish was not a primary trade study driver.
The combined manufacturing approach offers many benefits for powder removal, with
propellant and coolant manifolds closed out after the printing process. The combined
manufacturing approach also offers the capability to EDM injector elements. EDM offers
improved hole diameter tolerances at .001 in. and hole true diameter locations at .005 in (Meyer
Tool, Personal Communication, Dec, 2020). As seen in Table 2.4, a significant reduction in size
is possible using a combined or fully additively manufactured approach. In conclusion, the fully
additively manufactured approach was selected as the study hardware. This selection was primarily
driven by its reduced complexity and cheap cost. The final size of the fully additively manufactured
combustor allowed it to be printed on small print beds or on the same print bed as other larger
hardware. This improved the lead time that combustors could be designed and printed.

Table 2.4. RDRC Size and Part Quantity Conclusion Per Manufacturing Approach
Approach/Parameter
Outer Mold Line
Length (in)
Outer Mold Line
Diameter (in)
Combustion
Chamber Outer
Diameter (in)
Part Count*

Traditionally
Manufactured

Combined
Manufactured

Additively
Manufactured

3.1

1.8

2.3

4.6

3.2

3.3

2.6

1.2

1.6

15

3

1

Cost (Referenced to
>4X
>1.5X
Baseline
Baseline)
*Part count excludes seals, commodity fittings, fasteners, and facility support hardware
**Cost includes post machining additively manufactured components but does not include hot
isostatic pressing
2.11 Design Changes and Hardware Configuration Summary
Design modifications were completed on the HS 1.0 and WC 1.0 following Test Campaign
1.0. HS 1.0 was altered to move the CTAP pressure port closer to the injector face to gather more
accurate CTAP measurements. This combustor is referred to as Heat Sink 1.1 (HS 1.1) and was
tested during Test Campaign 2.0. Two major changes to the WC 1.0 hardware were incorporated

60

following Test Campaign 1.0. These changes resulted in two new combustors, Water Cooled 2.0
(WC 2.0) and Water Cooled 2.1 (WC 2.1). WC 2.0 and WC 2.1 were both successfully additively
manufactured but only WC 2.0 was hot fire tested. A summary table and figures of each
configuration can be found in Appendix A. A description of the design changes resulting in the
WC 2.0 and WC 2.1 designs is presented below. A detailed discussion of test results from HS 1.1
and WC 2.0 can be found in Section 5.
Following testing of WC 1.0 there was concern that hot combustion gas was impinging on
the outerbody coolant outlet thermocouple and impacting the thermal assessment. To mitigate this
concern, the coolant outlet thermocouple was shrouded. The thermocouple shroud was formed
conical nozzle with passages to place the thermocouple in the outerbody coolant outlet stream.
Additionally, the outerbody cooling system dimensions were varied in an attempt to induce
structural failure. The updated design, called Water Cooled 2.0 (WC 2.0), was used during Test
Campaign 2.0 and is shown in Figure 2.25. All other major combustor functions and dimensions
were kept that same. This included the propellant feed system and injector design, innerbody
cooling system, injector cooling system, and pre-det ignition system.

61

Figure 2.25. Water Cooled 2.0 and 2.1 Dimension Summary
The conical nozzle and thermocouple shroud can be seen in Figure 2.26. The 15 degree
conical nozzle was designed to expand to atmospheric pressure. Two thermocouple passages, 180
degrees apart, were placed behind the nozzle wall. When placed in these passages, the
thermocouples would be shielded from the combustion hot gases exiting the combustor. Similar
to the WC 1.0 hardware, the thermocouples would be bathed by coolant exiting the outerbody
cooling system offering the ability to complete a calorimetry assessment. Additional discussion on
the challenges and results from this design modification can be found in Chapter 5.
The other major design change included varying the outerbody cooling channel
dimensions. As shown in Chapter 6, wider cooling channels experience larger stresses. Larger
stresses result in lower low cycle and high cycle fatigue life. Wider cooling channels are typically
referred to as low aspect ratio designs as they are wider than they are in height. Low aspect ratio
cooling channel designs also result in reduced cooling performance due to the reduced finning
effect and therefore aren’t common in traditional rocket engine designs. Along with the thermal

62

performance degradation from low aspect ratio cooling system designs, RDRC’s are expected to
be more prone to high cycle fatigue failure due to the increased stresses in the hot wall as the
detonation wave passes.

Figure 2.26. Water Cooled 2.0 Hardware, Outerbody Coolant Outlet Temperature Measurement
In an attempt to induce larger stresses in the hot wall, a low aspect ratio design was
employed in the WC 2.0. The cooling channel dimensions for the WC 2.0 hardware can be found
in Table 2.5. An additional combustor was manufactured with the WC 2.0 design but using the
original WC 1.0 outerbody cooling channel dimensions. This hardware is referred to as WC 2.1
and was not hot fire tested during for this research. The structural performance predictions for the
designs can be found in Section 6.

63

Table 2.5. Water Cooled 2.0/2.1 Outerbody Cooling Passage Design
Outerbody Parameter

WC 2.0

WC 1.0

Passage Dimensions

Low Aspect Ratio 0.100 in
x 0.030 in

Square 0.030 in x 0.030 in

# of Passages

67

67

# of Passes

1

1

Hot Wall Thickness (in)

0.040

0.040

Rib Thickness (in)

.05

.05

Channel Roughness

200 micro-in

200 micro-in

2.12 Test Facility
Both the heat sink combustor and the actively cooled combustor were tested at Zucrow
Laboratories, Rocket Test Cell C. The propellant and instrumentation diagram (P&ID) can be
found in 0 along with the coolant and instrumentation diagram (C&ID). Fuel and oxidizer were
fed from separate manifolds, each capable of accepting a quantity of twelve, 300 series gaseous
cylinders. Gaseous methane bottles are filled to 2400 psia while gaseous oxidizer bottles are filled
to 2600 psia. This resulted in ~90 lbm of gaseous methane and ~160 lbm of gaseous oxygen
available for each test. These mass values take into consideration the pressure required upstream
of the regulator to supply the propellant at the RDRC design condition of 150 psia chamber
pressure. With this mass of propellant, a 700 sec test was feasible with oxidizer as the limitation.
Propellant flowrates were measured with sonic venturis with the fuel venturi throat diameter being
0.100 in and the oxidizer venturi throat diameter being 0.053 in. The desired propellant supply
pressure was achieved with electronically adjustable pressure regulators. Propellant temperature
could not be controlled and was typically the ambient temperature on the test day.
All valving other than the pre-detonation run valves were pneumatically operated from
regulated facility nitrogen. High pressure nitrogen purges were used for test preparation and
shutdown on the fuel and oxidizer circuits. The pre-detonation system was fed from the
aforementioned test cell oxygen system and high-pressure hydrogen routed to the test cell. Both
circuits were manually regulated to the desired setpoint of ~100 psia for each test. A purge was
flowed through the pre-detonation ignition system into the RDRC to thermally manage the ignition
port. The purge gas was regulated nitrogen and the flowrate was measured through sonic venturi.

64

The cooling system was supplied by a 100-gallon deionized (DI) water tank capable of
supply pressures up to 5000 psia. The water tank is pressurized through a high-pressure nitrogen
ullage system and can maintain a desired set pressure for the duration of a test. The 100-gallon
water tank provided ~200 seconds of available run time. Water temperature could not be controlled
and was typically the facility internal temperature on the day of test. A custom manifold was
designed and build to distribute the coolant to the innerbody, outerbody, and injector. A filter was
placed 10-micron filter was placed upstream of this manifold to capture any FOD ingress into the
critical passages within the hardware. Each circuit’s flowrate was individually measured through
cavitating venturis downstream of the manifold. The outerbody venturi throat diameter was 0.136
in, the innerbody venturi throat diameter was 0.115 in, and the injector venturi throat diameter was
0.030 in.
The run valve open and close time was metered so that water hammer did not occur on the
hardware during coolant startup or the upstream supply lines during coolant shutdown.
Temperature measurements of the coolant were taken at the injector cooling circuit and outerbody
cooling circuits supply and exit so that calorimetry could be completed. Exit temperature of the
innerbody could not be taken due to the location of the innerbody exit and its proximity to hot
exhaust gas. DI water was used so dissolved solids would not precipitate and clog cooling passages
during hot fire testing. Without DI water, blocked channels can occur through iron sulfate deposits
and calcium carbonate formation.
A National Instruments data acquisition system was used for low speed data acquisition at
a maximum sample rate of 1 kHz. An additional National Instruments data acquisition system was
used for high-speed data acquisition at a maximum sample rate of 2 MHz. Standard K-type
thermocouples were used for low-speed temperature measurements. Unik 5000 pressure
transducers were used for low-speed pressure measurements. Two high frequency pressure
transducers (PCB-102B) were used to collect high frequency manifold pressure data. A high-speed
camera (Vision Research, Phantom V2512) was used with a 200 mm lens to provide high speed
imaging of the detonation wave during heat sink RDRC operation. A labview code developed for
use at Zucrow Laboratory was used to operate the facility, read and record telemetry, and set
redlines for abort monitoring.
An example of a heat sink ~0.25 sec duration test can be found in Table 2.6 below.
Determination of valve opening times were derived from purge and propellant cold flow data. An

65

oxidizer leading start sequence was used along with an active purge through igniter passage to
verify hot gas did not back flow into the ignition system. For actively cooled tests, coolant was
flowed through the hardware for 15 seconds prior to ignition. This 15 second period was to prime
the cooling system and verify adequate coolant flowrates through automated redline aborts on
venturi upstream pressures. The cooling system remained active at the end of the test to remove
any residual heat from the combustor following shutdown.

Table 2.6. Autosequence Example for ~0.25 sec Duration Test (No Active Cooling)
Name
PV-PDOX-084
PV-PDFU-059
PV-N2-077
PV-N2-043
PV-N2-068
PV-N2-068
PV-N2-043
PV-N2-077
SV-PDOX-088
SV-PDFU-060
PV-OX-019
PV-FU-007
PV-N2-068
SV-PDOX-088
SV-PDFU-060
PV-PDOX-084
PV-PDFU-059
Spark
Spark
PV-FU-007
PV-N2-077
PV-N2-043
PV-OX-019

Value
open
open
open
open
open
close
close
close
open
open
open
open
open
close
close
close
close
open
close
close
open
open
close

Time (s)
1
1
1
2
2
4
4
5
6
6
7.76
7.81
7.92
8
8
8
8
8.003
8.008
8.21
8.21
8.21
8.25

Description
Oxygen Pre-Det Prime Valve
Fuel Pre-Det Prime Valve
Nitrogen Oxygen Purge Valve
Nitrogen Fuel Purge Valve
Nitrogen Pre-Det Purge Valve
Nitrogen Pre-Det Purge Valve
Nitrogen Fuel Purge Valve
Nitrogen Oxygen Purge Valve
Oxygen Pre-Det Run Valve
Fuel Pre-Det Run Valve
Oxygen Run Valve
Fuel Run Valve
Nitrogen Pre-Det Purge Valve
Oxygen Pre-Det Run Valve
Fuel Pre-Det Run Valve
Oxygen Pre-Det Prime Valve
Fuel Pre-Det Prime Valve
Spark Coil Trigger
Spark Coil Trigger
Fuel Run Valve
Nitrogen Oxygen Purge Valve
Nitrogen Fuel Purge Valve
Oxygen Run Valve

High frequency accelerometers were used to characterize structural accelerations during
Test Campaign 2.0. Two accelerometers were used, each clocked 180 degrees apart as shown in
Figure 2.27 and Figure 2.28. The accelerometer placed on the aft face of the combustor was
66

oriented to capture axial accelerations. The accelerometer placed on the circumferential face of the
combustor was oriented to capture radial accelerations. As shown in Section 5, both accelerometers
proved useful at identifying wave pass frequency. The accelerometers used were PCB Piezotronic
Model 621C40.

Figure 2.27. Water Cooled 2.0 Hardware, Accelerometer Placement Overview

67

Figure 2.28. Water Cooled 2.0 Hardware, Accelerometer Placement Cross Section

68

THERMAL EVALUATION

No matter the cooling system approach, accurately predicting thrust chamber heat loads is
critical to any rocket engine development program. Models are well developed for the
conventional rocket engine designer for trade studies, including commercially available options
such as Rocket Thermal Environment and Rocket Propulsion Analysis [28, 29]. These models
likely make use of proven convective coefficient correlations for the coolant (Hines, Seider-Tate,
and Dittus-Boelter) and hot combustion products (McAdams, Bartz, Ambroks) [37]. Literature is
scarce for RDE cooling systems and approaches. Along with the minimal research completed,
correlations do not exist for the designer to make accurate predictions to support trade studies.
Along with these challenges, little is known about the hot gas convective environment and its
boundary layer with the combustion chamber wall. The structure of the passing detonation front is
presumably closely tied to the injector design and operating conditions. The detonation wave
certainly thins, if not removes, boundary layers which vastly increases heat transfer.
Two thermal analyses were completed for this study to give future RDE designers insight
into the thermal environments they face with their cooling system designs. These analyses are
described in detail within the following sections. Firstly, a calorimetry model was developed and
used to reduce the cooling system data obtained during RDRC hot firing. This model is used to
predict operational wall temperatures, heat flux, and hot gas coefficients. Secondly, a predictive
thermal model was developed that could be scaled to the experimental test data. This model can
be used by the RDE designer to complete trade studies by predicting cooling system performance
at different operating conditions and design configurations, based on the results from the
experimental test data.

3.1

Calorimetry Thermal Model Methodology

The calorimetry model utilizes coolant temperature data at the inlet and outlet of the
cooling system to determine the thermal conditions experienced by the hardware during the test.
These thermal conditions include hot wall temperatures, cold wall temperatures, heat fluxes, and
hot gas coefficients. Because coolant temperature was only collected at the inlet and outlet of the
coolant system, the thermal conditions predicted by this model are considered average across the

69

cooling channel they are calculated for. Thermal data was collected on the outerbody cooling
system and injector cooling system for this study. As discussed in Section 0, coolant outlet
temperature on the innerbody was not collected because a thermocouple could not be placed in the
coolant exit flow.
Coolant inlet temperature was measured in a manifold upstream of the combustor and used
as the inlet temperature for both the injector and outerbody coolant system. For the outerbody,
coolant outlet temperature was measured at the exit of the cooling passage on the aft end of the
combustor. For WC 1.0, thermocouples were plunged into the coolant flow exiting the combustor
with care taken not to expose the thermocouples to the convective hot gas environment. The WC
1.0 configuration can be seen in Figure 3.1 with only one thermocouple shown. For WC 2.0, the
thermocouples were also plunged into the coolant flow but shrouded behind a nozzle. The WC 2.0
configuration can be seen in Figure 2.26. Two thermocouples were used in the outerbody exit
stream 180 degrees apart to determine if temperature variations existed in separate passages. The
injector coolant flow entered and exited through fittings on the top side of the combustor as shown
in Figure 2.13. The exit flow was routed through a line and then dumped outside of the test facility.
Near the exit fitting of the combustor, a t-fitting was used to plunge a thermocouple in the exiting
fluid which served as the injector cooling system outlet temperature.
With the coolant mass flowrate and its inlet and outlet temperature, the total heat transfer
rate can be found. The total heat rate (𝑄̇ ) to the coolant is determined by Equation 3-1 below,
where 𝑚̇ is the coolant mass flowrate, 𝑇𝑐𝑜 is the coolant outlet temperature, 𝑇𝑐𝑖 is the coolant inlet
temperature, and 𝑐𝑝 is the specific heat capacity of the coolant. The average specific heat capacity
from coolant inlet temperature and outlet temperature was used for this model.
𝑄̇ = 𝑚̇𝑐𝑝 (𝑇𝑐𝑜 − 𝑇𝑐𝑖 )

Equation 3-1

During actual hot fire testing, discrepancies existed in coolant outlet temperatures
measured from different channels. It was determined that the temperature difference was likely
attributed to variations in channel dimensions, resulting in varying cooling velocities. This
evaluation is discussed extensively in Section 5. Because the coolant outlet was not manifolded
and measured as a bulk temperature for this experiment, the variation in temperature between the
two channels had to be considered in the calorimetry assessment. Making the assumption that each

70

channel experienced the same average specific heat capacity and the average flowrate between the
two channels represents the total average flowrate, a relationship was developed for the coolant
temperature change as shown in Equation 3-2. 𝑇𝑐𝑜,𝑎 and 𝑇𝑐𝑜,𝑏 represent the coolant outlet
temperature measured at the two different locations.

𝑇𝑐𝑜 − 𝑇𝑐𝑖 =

2

Equation 3-2

1
1
𝑇𝑐𝑜,𝑎 − 𝑇𝑐𝑖 + 𝑇𝑐𝑜,𝑏 − 𝑇𝑐𝑖

Figure 3.1. WC 1.0 Outerbody Coolant Exit Thermocouple Placement
With the total heat rate known and wall area subject to heat conduction, the heat flux can
be calculated. Figure 3.2 defines a standard cooling passage arrangement, with coolant flowing
through passages into and out of the page. Once the heat load passes through the combustor hot
wall, it either passes into the cooling rib through conduction or into the coolant itself through
convection. The heat load that passes into the rib then convectively passes into the coolant in the

71

+/- Z direction. This process of transmitting the heat load from the rib to the coolant is called
finning. The calorimetry model takes the finning heat load into account when determining the heat
flux from the combustion environment. The heat flux (𝑞̇ ) to the coolant is then determined by
Equation 3-3 below, where 𝐴𝑐𝑤 is the cold wall area defined in the x-z plane, 𝐴𝑓𝑖𝑛 is the finning
area defined in the y-z plane, and 𝜂𝑓𝑖𝑛 is the fin efficiency.
𝑞̇ = 𝑄̇ /(𝐴𝑐𝑤 + 𝐴𝑓𝑖𝑛 𝜂𝑓𝑖𝑛 )

Equation 3-3

The fin efficiency 𝜂𝑓𝑖𝑛 can be calculated using Equation 3-4, where m is the fin parameter
and 𝐶𝐻 is the channel height [18]. The fin parameter can be calculated using Equation 3-5, where
ℎ𝑐 is the coolant convective coefficient, 𝐶𝑊 is the channel width, 𝐶𝐿 is the channel length, and 𝐾𝑤
is the chamber material thermal conductivity [18]. Many correlations exist for the coolant
convective coefficient and are commonly used in rocket combustor cooling system analyses. The
commonly used include the Hines correlation, the Seider-Tate correlation, and the Dittus-Boelter
correlation [37]. Each of these correlations were developed with smooth pipe assumptions which
is not applicable to the surface roughness produced in additively manufactured cooling passages.
Another correlation, developed by Petukhov, does take surface roughness into
consideration, and was used for this study [29]. As discussed in Section 2, the surface roughness
of internal passages for additively manufactured parts is ~200-300 micro-in. depending on the
vendor. This surface roughness invalidates the smooth pipe assumptions for other common
correlations and is the motivation for using the Petukhov correlation in this study. The Petukhov
correlation is shown in Equation 3-6 below, where Re is the Reynolds Number, Pr is the Prandtl
number, 𝜇𝑏 is the dynamic viscosity at the coolants bulk temperature, 𝜇𝑤 is the dynamic viscosity
of the coolant at the cold wall temperature, and 𝑓 is the friction factor. The Petukhov correlation
was developed for Reynolds Numbers between 104 < 𝑅𝑒 < 106 . For the combustor and coolant
conditions experienced in this study, the Reynolds Number was on the order of 104 .

𝜂𝑓𝑖𝑛 =

tanh (𝑚𝐶𝐻 )
𝑚𝐶𝐻

Equation 3-4

72

𝑚=√

ℎ𝑐 𝐷
=
𝑘𝑐

2ℎ𝑐 (𝐶𝑊 + 𝐶𝐿 )
𝐾𝑤 𝐶𝑊 𝐶𝐿

Equation 3-5

0.25
𝑓
𝜇
( ⁄8) 𝑅𝑒 Pr ( 𝑏⁄𝜇𝑤 )
0.5

(𝐾1 + 𝐾2) (𝑓⁄8)

(𝑃𝑟 0.67 − 1)
Equation 3-6

𝐾1 = 1.0 + 3.4 𝑓
𝐾2 = 11.7 +

1.8
𝑃𝑟 0.33

The friction factor was calculated using the Colebrook equation as shown in Equation 3-7
below with 𝜀 being the relative surface roughness of the cooling passage. For this study, the
relative surface roughness was not measured but was approximated based on recommendations
from the vendor. The approximated values are summarized in Table 2.2. The Colebrook equation
is accurate over all ranges of Reynolds Number that would be experienced in a rocket combustor
cooling passage but is implicit and must be solved iteratively. All coolant properties required for
these equations were found using REFPROP using the measured temperature and pressure in the
cooling system [21].
1

2.51
𝜀
= −2𝑙𝑜𝑔 (
+
)
𝑅𝑒√𝑓 3.7
√𝑓

Equation 3-7

73

Figure 3.2. Cooling Channel Arrangement and Definition
With the heat flux approximated, the cold wall temperature (𝑇𝑐𝑤 ) can then be estimated by
solving the convective heat transfer in Equation 3-8, where 𝑇𝑐𝑎 is the coolant average temperature.
As mentioned earlier in this Chapter, coolant temperature was only measured at the inlet and outlet
of the cooling systems. Equation 3-8 requires a coolant temperature to estimate the cold wall
temperature but is relatively insensitive to the temperature selected for this study. For example,
coolant temperature rises in this study were typically supplied at ambient conditions and rose on
the order of 20-30 deg F. Using coolant average temperature, inlet temperature, or outlet
temperature in Equation 3-8 only impacts the approximated cold wall temperature by +/- 20-30
deg F for a cold wall operating in the range of roughly 300-500 deg F. Mechanical properties for
the materials used in this study are largely unaffected by this minor variation and can be considered
negligible for this study. With the cold wall temperature known, the combustion chamber hot gas
wall temperature (𝑇ℎ𝑤 ) can then be solved using the conductive heat transfer in Equation 3-9,
74

where 𝑘𝑤 is the thermal conductivity of the chamber wall material, and 𝑡𝑤 is the hot wall
thickness.
𝑞̇ = ℎ𝑐 (𝑇𝑐𝑤 − 𝑇𝑐𝑎 )+ ℎ𝑐 𝜂𝑓𝑖𝑛 (𝑇𝑐𝑤 − 𝑇𝑐𝑎 )

𝑞̇ =

Equation 3-8

𝑘𝑤
(𝑇 − 𝑇𝑐𝑤 )
𝑡𝑤 ℎ𝑤

Equation 3-9

To calibrate predictive thermal models, it is essential to make accurate predictions of the
hot combustion gas convective heat transfer coefficient. This coefficient is understood and well
characterized for conventional rocket engines using correlations such as McAdams, Bartz, or
Ambroks, with the Bartz correlation the most used [37]. These correlations are commonly used in
industry and were developed with large experimental datasets that currently do not exist in the
RDC literature or are not shared outside of the organizations that developed them. The airbreathing
RDE community has begun to evaluate the hot gas coefficients utilizing direct heat flux
measurements and calorimeter outfitted hardware [22, 23, 24]. This information is useful, but was
obtained at chamber pressures at least an order of magnitude lower than those that will be
experienced in RDRC’s. With the hot wall temperature estimated, the hot gas convective
coefficient (ℎ𝑔 ) can be solved by using the convective heat transfer in Equation 3-10 below, where
𝑇𝑟 is the recovery temperature of the hot combustion gases.
𝑞 ′′ = ℎ𝑔 (𝑇𝑟 − 𝑇ℎ𝑤 )

Equation 3-10

Selection of the recovery temperature represents the largest assumption involved in the
calorimetry assessment. For conventional rocket chambers, the temperature of the gas driving the
convective heat transfer process into the hot wall is lower than the stagnation temperature of the
hot combustion gases. The boundary layer between the free stream combustion products and the
hot wall is compressible and subject to viscous dissipation [37]. This viscous dissipation reduces
the kinetic energy of the fluid resulting in a lower temperature driving the convective process
called the recovery temperature [37]. The recovery temperature is calculated with Equation 3-11
below, where r is the recovery factor, 𝛾 is the ratio of specific heats for the combustion products,
𝑇∞ is the combustion gas free stream temperature, and 𝑀∞ is the combustion gas free stream mach

75

number. The recovery factor is boundary layer dependent and can be approximated as a turbulent,
free boundary layer through the Prandtl number correlation shown in Equation 3-12 [37].

𝑇𝑟 = 𝑇∞ (1 +

𝛾−1
2
)
𝑟𝑀∞
2

Equation 3-11

1

Equation 3-12

𝑟 = 𝑃𝑟 ⁄3

The airbreathing community commonly replaces the recovery temperature with the
Chapman-Jouguet (CJ) free stream temperature as an upper limit in the detonating flow,
acknowledging that the true temperature is likely a few hundred degrees kelvin lower [22]. If
temperature used to calculate the hot gas coefficient is larger than the actual operational
temperature, the calculated hot gas coefficient using Equation 3-10 will artificially be lower than
the actual value. Figure 3.3 below represents the range of temperatures that could be driving the
convective process over a range of operating chamber pressures. The largest estimated
temperatures in Figure 3.3 is the CJ recovery temperature. The CJ recovery temperature is the free
stream temperature corrected to a recovery value using Equation 3-11. This temperature was
calculated assuming combustion products from NASA’s CEA Chapman Jouguet Detonation
feature [27]. Additionally, the combustion products were assumed to be choked as demonstrated
in RDE numerical computations [26]. This methodology likely represents the peak convective
driving temperature within the combustion chamber as the combustion products expand during the
blowdown process that follows the detonation wave passing.

76

4500
4300
4100
CJ, Recovery

Temperature (K)

3900
3700

RDE Cycle Avg, Recovery
3500
3300

Conventional Combustion
Chamber, Recovery

3100

Conventional Throat,
Recovery

2900
2700
2500
0

100

200

300

400

500

Chamber Pressure (psia)

Figure 3.3. Hot Gas Temperature Comparison, Stoichiometric Mixture Ratio, Frozen Combustion
Product Conditions
The lowest temperatures in Figure 3.3 are the RDE cycle averaged temperatures, developed
using Stechmann’s RDE performance model [10]. This free stream temperature was also corrected
to the recovery temperature using the same methodology above to correct the CJ free stream
temperature. In comparison to the CJ approach, this methodology likely represents an average
convective driving temperature within the combustion chamber as the products expand during the
blowdown process. The values located between the maximum and minimum represent recovery
temperatures from a conventional deflagrative rocket combustor operating at the same conditions.
The values presented represent combustion chamber and throat level recovery temperatures.
The recovery temperature calculations in Figure 3.3 were completed using recovery factors
commonly used for conventional rocket combustor calculations. As indicated above, the recovery
factor accounts for the reduction in the driving temperature across the boundary layer between the
combustion products and the hot wall. As pointed out by Stechmann, local regions of the RDRC
combustor wall will experience direct shock impingement from the passing detonation wave which
will significantly disrupt the boundary layer [8]. In RDRC’s this will undoubtedly result in an
increase in the recovery factor, driving the temperature of the convective environment closer to
the stagnation temperature of the combustion products with the boundary layer disruption.

77

Stechmann also points out that the outer skins of hypersonic vehicles can experience periods of
direct shock impingement, causing an increase in local heat flux [8]. This local increase in heat
flux was characterized by Anderson as shown in Figure 3.4. Using Figure 3.4, Stechmann
estimates that instantaneous heat fluxes could be on the order to 6 to 23 times larger than average
heat fluxes at expected operating conditions of RDRC’s [37].

Figure 3.4. Hypersonic Local Heat Flux Scaling [30]
Along with the challenges of estimating the recovery factor due to boundary layer
degradation, the hot gas environment in an RDE is highly transient with fluctuations in temperature
and pressure well above that experienced in a conventional rocket engine. These fluctuations are
occurring on the kHz timescale and are challenging to capture experimentally due to the response
time of commonly used instrumentation. With these uncertainties, the author proceeded using

78

conventional rocket combustor throat level combustion product properties to determine the
recovery temperature using Equation 3-11. These properties were calculated using the industry
standard NASA Chemical Equilibrium Application (CEA) for conventional rocket conditions at
the same RDRC operating condition. Though this does not represent the true RDRC combustion
environment, it offers a common means of comparison and scaling to cooling system analyses
completed on traditional rocket combustors. Once calorimetry heat flux and hot gas coefficients
are calculated from RDRC test data, a predictive analysis for a traditional rocket combustor can
be completed for throat level heat flux and results can be compared. Adopting this methodology
allows the RDRC combustion designer to utilize proven cooling system analysis methods and scale
environments for trade studies and design selections.

3.2

Predictive Thermal Model Methodology
The predictive thermal model is a quasi-steady, one-dimensional thermal analysis [37]. It

is an iterative analysis approach that uses simplifying assumptions to reduce computational
intensity. This approach has shown good correlation to higher fidelity models and experimental
data [31]. The two major simplifying assumptions are: 1.) Regen jacket closeout wall heat transfer
is negligible and 2.) Steady state thermal condition has been achieved [37]. With typical closeout
wall temperatures between ambient and 150 deg F, assumption #1 induces a negligible error.
Understanding the instantaneous heat transfer environment is beyond the scope of this study. The
instantaneous heat transfer environment is not expected to create large temperature fluctuations in
the chamber material because of the timescale the detonation is occurring on.
As shown in Figure 3.5, Stechmann analytically concluded for a 200 atm chamber pressure
case that hot wall temperatures remain within 15 deg K of the mean wall temperature over the
detonation cycle [8]. Stechmann also concluded that the temperature excursions from mean scale
with chamber pressure and that lower chamber pressures result in lower excursions [8].
Furthermore, these excursions decrease with penetration depth into the hot wall [8]. Based on these
results, assumption #2 simplifies the thermal analysis, and offers the RDRC combustion designer
a means of estimating hot wall temperatures that is not computationally intensive. Though this
study is not investigating the temperature fluctuations throughout the detonation cycle, the author
recommends this be investigated in future studies. The thermal variations induced by this
temperature fluctuation could result in un-expected stresses within the chamber material due to
79

unmatched thermal expansion between materials or coatings. In high heat flux combustion
chamber environments, these variations could impact the bond strength of thermal barrier coatings
used to maintain acceptable hot wall temperatures.

Figure 3.5. Temperature Profiles in Copper Combustion Chamber Wall From Transient Heat Flux
[8]
Calculation of the hot gas convective coefficient is required for this assessment and
represents the largest assumption in the predictive thermal model. Commonly used correlations
for traditional rocket combustors include those developed by McAdams, Bartz, and Ambrok [37].
Arguably, the most used correlation was developed by Bartz and is calculated using Equation 3-13
below. The inputs to Equation 3-13 represent the conditions of the combustion products where 𝜌
is the density, 𝐶𝑝 is the specific heat capacity, 𝜇𝑏 is the dynamic viscosity, 𝑉 is the velocity, and
𝐷 is the diameter of the combustion chamber. For an RDRC, 𝐷 represents the hydraulic diameter
of the combustion chamber annulus. The subscripts in Equation 3-13 represent different
conditions, where “0” conditions are determined at the stagnation temperature, “∞” conditions are
determined at the free stream temperature, and “am” represents the arithmetic mean between the
free stream temperature and the hot wall temperature.

80

0.026 𝜇00.2 𝐶𝑝0
𝜌𝑎𝑚 0.8 𝜇𝑎𝑚 0.2
0.8
(𝜌
)
(
) (
)
ℎ𝑔 =
(
)
𝑉
∞
∞
𝐷0.2
𝜌∞
𝜇0
𝑃𝑟00.6

Equation 3-13

The Bartz correlation is commonly used in industry and was developed with large
experimental datasets that currently do not exist in the RDC literature or are not shared outside of
the organizations that developed them. As mentioned in Section 3.1, the airbreathing RDE
community has begun to evaluate the hot gas coefficients utilizing direct heat flux measurements
and calorimeter outfitted hardware [22, 23, 24]. This information is useful, but was obtained at
chamber pressures orders of magnitude lower than those that will be experienced in RDRC’s.
To calculate the hot gas coefficient for the RDRC predictive model, the author proceeded
using conventional rocket combustor throat level combustion product properties to determine the
inputs for Equation 3-13. These properties were calculated using the industry standard NASA
Chemical Equilibrium Application (CEA) for conventional rocket conditions at the same RDRC
operating condition. Though this does not represent the true RDRC combustion environment, it
offers a common means of comparison and scaling to cooling system analyses completed on
traditional rocket combustors.
To complete the quasi-steady, one-dimensional analysis, the chamber geometry and engine
operating conditions must be known. The chamber geometry and cooling system are broken into
stations where each station is solved using a steady state heat transfer assessment [37]. The results
from the previous station are used as inlet conditions to the next station and the steady state
assessment is completed again until the entire chamber is analyzed [37]. The steps below are
repeated at each station within the model, increasing the coolant temperature with the heat obtained
from the previous station and reducing the coolant pressure by the predicted losses within the
cooling channel [37]:
1. The iterative variable in the analysis is the hot wall temperature (𝑇ℎ𝑤 ). To start the analysis,
𝑇ℎ𝑤 is guessed and the analysis is iterated until the heat flux from the combustion products
to the hot wall balances with the heat flux from the cold wall to the coolant.
2. Calculate the hot gas coefficient as discussed above using Equation 3-12.
3. Calculate the heat flux (𝑞 ′′ ) from the combustion products to the hot wall with Equation
3-10. Details on the recovery temperature approach can be found in Section 3.1 and
calculated with Equation 3-11 and Equation 3-12.
81

4. Calculate the cold wall temperature with Equation 3-9 using the 𝑇ℎ𝑤 guess from Step 1.
5. Calculate the coolant convective coefficient using Equation 3-6.
6. Calculate the heat flux (𝑞 ′′ ) from the cold wall to the coolant using Equation 3-15 below.
Equation 3-15 takes into consideration the finning characteristics of the channel geometry
as described in Section 3.1 where 𝜂𝑓𝑖𝑛 can be calculated with Equation 3-4 and Equation
3-5.
"
"
"
"
𝑞 ′′ = 𝑞ℎ𝑤
+ 𝑞𝑟𝑖𝑏
= 𝑞ℎ𝑤
+ 𝑞ℎ𝑤
𝜂𝑓𝑖𝑛

Equation 3-14

𝑞 ′′ = ℎ𝑐 (𝑇𝑐𝑤 − 𝑇𝑐𝑎 ) + ℎ𝑐 (𝑇𝑐𝑤 − 𝑇𝑐𝑎 )𝜂𝑓𝑖𝑛

Equation 3-15

7. The convergence criteria of this model is that the heat flux calculated in Step 6 equals the
heat flux calculated in Step 3. If the heat fluxes are not equal, a new hot wall temperature
should be guessed in Step 1 and the process repeated until convergence occurs.
8. With model convergence, the predicted heat flux is known. The temperature rise of the
coolant through the segment under evaluation can be calculated using Equation 3-16 below.
It should be noted that the channel length (𝐶𝐿 ) is the length of the channel segment under
evaluation, not the entire length of the cooling channel. The temperature increase of the
coolant is driven by the heat flux through the hot wall and the heat flux finned from the
cooling channel rib.

𝑇𝑐(𝑖+1) = 𝑇𝑐(𝑖) +

1
𝑚̇𝑐ℎ𝑎𝑛𝑛𝑒𝑙 𝐶𝑝

"
"
(𝑞ℎ𝑤
𝐶𝑊 𝐶𝐿 + 𝑞𝑟𝑖𝑏
𝐶𝐻 𝐶𝐿 )

Equation 3-16

9. The pressure drop of the coolant through the segment under evaluation can be calculated
using Equation 3-17 below, where the friction factor (𝑓) can be found using the Colebrook
correlation in Equation 3-7.

𝑃𝑐(𝑖+1) = 𝑃𝑐(𝑖) − 2𝑓𝜌𝑉 2

𝐶𝐿
𝑑

Equation 3-17

82

TEST CAMPAIGN 1.0 RESULTS

Test campaign 1.0 was comprised of 47 tests used to prepare the facility, verify the
operability of the additively manufactured RDRC design, and complete a long duration RDRC hot
fire. Testing included propellant cold flows, water system cold flows, and hot fire testing. Two
RDRC’s were hot fired during the 1.0 campaign. The hardware versions tested included a heat
sink combustor (HS 1.0) and a water-cooled combustor (WC 1.0). A hardware configuration
summary for HS 1.0 and WC 1.0 is provided in Table A.1 and described in detail in Chapter 2. Of
the 47 tests, 3 hot fires were completed on HS 1.0 and 8 hot fires were completed on WC 1.0.

4.1

Heat Sink Testing

HS 1.0 hot fire testing is summarized in Table 4.1 below. Heat sink testing was to validate
the ignition concept and confirm rotating detonation behavior existed before adding the additional
facility complexity required to operate the water-cooled combustor. Coolant from WC 1.0 exits
the aft end of the combustor thereby making high speed imaging through the aft end of the chamber
impractical. High speed video footage was captured during HS 1.0 testing to be used for correlation
to WC 1.0 testing. High frequency manifold pressure data was not collected as the high frequency
data acquisition system was not operational. Additionally, chamber pressure measurements on the
WC 1.0 hardware could not be accommodated. As discussed in Section 2.3, an attempt was made
to accommodate this measurement, but the features failed to print successfully in the additive
manufacturing process. Thus, HS 1.0 hardware was used to correlate chamber pressure with
throttle setting for heat load correlations.

Table 4.1. Test Campaign 1.0, HS 1.0, Hot Fire Testing Summary

19

Total
Propellant
Flowrate
(lbm/s)
0.077

20
21

0.074
0.072

Test
#

Mixture
Ratio
(O/F)

Predicted
CTAP
(psia)

Measured
CTAP
(psia)

Test
Duration
(sec)

Wave Pass
Frequency
(kHz)

3.8

53

20

0.50

N/A

3.4
3.5

52
50

19
19

0.50
0.75

12.5
12.7

83

Throttle settings were intentionally kept low for initial testing of HS 1.0 to avoid hardware
damage. For the three tests completed on HS 1.0, predicted chamber pressures based on
performance modeling described in Section 2.4 were expected to be ~50 psia while measured
chamber pressures were ~20 psia. High speed video footage was captured on test 20 and 21. Both
tests operated with a single wave mode, rotating counterclockwise (as viewed from aft end of the
combustor) with the wave pass frequencies defined in Table 4.1. Screen captures images from the
high-speed video footage of Test 21 can be seen in Figure 4.2. Due to the test cell configuration,
capturing quality high speed video footage was challenging. The light from the combustion process
had to be reflected off two polished stainless-steel plates angled at 45 degrees and then viewed
through the optics of the high-speed camera. Additionally, the mirrors were placed ~15 feet from
the small combustor which was 1.6 in in outer diameter with a 0.14 in annulus gap.
Detonation wave speeds were ~1500 m/s for Test 20 and 21, resulting in ~65% of Chapman
Jouguet predicted speeds. Measured chamber pressures were expected to be lower than predicted
due to the location of the pressure measurement as shown in Figure 4.1 and the associated pressure
drop of the combustion products. As shown, the pressure measurement location was biased
towards the aft end of the combustor. This location was chosen to keep the measurement location
identical to WC 1.0 so performance measurements could be correlated. In the WC 1.0 hardware,
coolant supply passages take up available landscape for a chamber pressure measurement to be
located closer to the injector face. As discussed in Section 2.3, the chamber pressure measurement
features of WC 1.0 failed to print successfully in the additive manufacturing process and the
measurement was not pursued.

84

Figure 4.1. CTAP Measurement Location on HS 1.0

Figure 4.2. Test 21 High Speed Video Screen Captures Showing Single Wave in Different
Quadrants
Experimental data from other comparable injector and hardware configurations exhibited
this expected chamber pressure drop along the axial length of the combustor. Smith et al. placed

85

three CTAP measurements spaced axially, with the first being near the detonation zone [4]. For
the test conditions presented in their literature, they experienced an approximate 50% reduction in
CTAP from the pressure measurement located near the injector face and the measurement located
near the combustor exit [4]. Bennewitz et al. also presented data from CTAP measurements axially
along the combustion chamber [3]. The results highlighted the reduction in pressure with axial
length [3]. Bennewitz et al. also provided CTAP data for varying throttle settings for similar
injector configurations, propellants, and run conditions to those tested with the HS 1.0 hardware
[3]. The data presented was for the CTAP measurement located nearest the detonation zone [3].
This data set was analytically recreated with the model described in Section 2.4 and is presented
in Figure 4.3. Though the experimental data was limited in the range of conditions presented,
analytical predictions were deemed satisfactory and CTAP in the detonation zone for HS 1.0 was
assumed to be as predicted by the Stechmann model for this study [10].

Figure 4.3. Stechmann Performance Model Comparison with Experimental Dataset [3,8]
Heat flux scales with chamber pressure and the RDRC designer will undoubtedly need
predicted levels based on the operating conditions. The ideal experimental configuration would
collect calorimetry and chamber pressure at numerous axial locations along the combustor. This
would allow the designer to better understand the heat load distribution, especially the heat flux in
86

the detonation zone. This approach was not accommodated in the WC 1.0 as the hardware size
was small and it was considered a risk to incorporate. The calorimetry data collected on the WC
1.0 hardware represents the average heat load and should be treated as such. Designers should use
this average heat flux data with caution as the peak flux within the detonation zone could be
substantially larger. This peak heat flux will result in larger magnitude hot wall temperatures and
could possibly approach or exceed critical heat flux levels.

4.2

Water Cooled Testing

WC 1.0 hot fire testing is summarized in Table 4.2 below. Tests 37 and 38 were low throttle
setting (50 psia and 75 psia predicted CTAP, respectively) and short duration (0.25 sec) tests to
validate the operability of the water-cooled combustor. Calorimetry data were collected but did
not reach steady state for the outerbody or injector with the low throttle setting and short run
duration. Test duration was increased to 0.75 sec for Test 39 but calorimetry data still did not reach
steady state due to the low throttle setting (75 psia predicted CTAP). During post test inspections
it was identified that the thermocouple collecting coolant outlet temperature on the outerbody was
protruding through the coolant exit stream. This indicated that the outerbody coolant outlet
temperatures were being overpredicted because the thermocouple was experiencing hot gas
interaction with the exiting combustion products.

Table 4.2. Test Campaign 1.0, Water Cooled 1.0, Hot Fire Testing Summary
Total
Fuel/Ox
Wave
Mixture Predicted Measured
Test
Test Propellant Manifold
Pass
Ratio
CTAP
CTAP
Duration
#
Flowrate
Pressure
Frequency
(O/F)
(psia)
(psia)
(sec)
(lbm/s)
(psia)
(kHz)
37*
.0923
171/99
3.55
50.0
N/A
0.25
N/A
38*
0.139
235/202
4.00
77.0
N/A
0.75
N/A
39*
0.130
220/193
4.03
72.1
N/A
0.75
N/A
43
0.179
293/266
4.11
99.6
N/A
0.75
N/A
44
0.225
360/325
4.11
126
N/A
0.75
N/A
45
0.140
235/202
4.00
77.3
N/A
3
N/A
46
0.131
220/193
4.04
72.1
N/A
10
N/A
47
0.177
297/259
4.06
98.4
N/A
10
N/A
*Outerbody calorimetry measurement error identified resulting in invalid data. Injector
calorimetry did not reach steady state

87

As shown in Figure 4.4 for Test 39, the cooling system flowrates were steady, indicating
that the ullage pressure system described in Section 2.12 performed nominally. For reference,
ignition was commanded at T+13.00 sec and engine shutdown was commanded at T+13.75
seconds. The cooling system was started well before the engine start transient to allow flowrates
to achieve steady state. Abort monitoring was also completed prior to commanding ignition to
verify the correct flowrates were being achieved and that the system was performing nominally.
The abort redlines continued for the duration of the test, including the addition of a coolant
temperature exceedance redline aimed at avoiding hot wall overheating. Prior to testing, the system
was primed at low pressures to verify coolant flow was steady and confirm bubbles did not ingress
into the system. The cooling system was left operational following the test until a nominal
shutdown was confirmed and is then manually commanded to shutdown.

Figure 4.4. Test 39; Cooling System Mass Flowrates
This protruding thermocouple on the outerbody coolant exit was left untouched following
Test 39, and an additional thermocouple was added to a cooling channel clocked 180 degrees away.
Care was taken to place the tip of the new thermocouple no further than the midplane of the exiting
water. This careful placement was to ensure the thermocouple remained bathed in the exiting

88

coolant and did experience hot gas interaction with the exiting combustion products. Test 43 was
the next hot fire completed in the test series and it confirmed that the protruding thermocouple on
the outerbody was producing invalid calorimetry data for Tests 37-39. As shown in Figure 4.5,
heat flux measurements from the protruding thermocouple (TC-208), produced outerbody heat
flux results ~60% in excess of the correctly placed thermocouple (TC-210). This resulted in
outerbody hot wall temperatures being overpredicted by ~253 deg F. Figure 4.5 also indicates that
outerbody thermocouple temperatures had not reached steady state at the time of engine shutdown.
It is expected that this can be attributed to slow response time that is characteristic of
thermocouples rather than the wall temperature continuing to rise during the 0.75 sec test duration.

Figure 4.5. Test 43; Outerbody Calorimetry Results; Indication of Thermocouple Protrusion Error
and Invalid Calorimetry Results From TC-208

89

Following Test 43, TC-208 was adjusted to the midplane of the outerbody coolant exit. As
shown in Figure 4.6, TC-208 showed good correlation to TC-210 following the adjustment. It
should be noted that TC-210 appears to have a slower response time than TC-208 but the steady
state results track closely. The predicted chamber pressure for Test 44 was 125 psia and represents
the highest throttle setting achieved for Test Campaign 1.0. Outerbody hot wall temperatures were
approaching 750 deg F which is well within the capability of GR-Cop84. GRCop-84 combustors
are commonly operated in excess of 1000 deg F but rule of thumb is to remain below 1200 deg F
if the strength margin of the material remains within acceptable limits for the specific design.
Additionally, margin to surpassing critical heat flux was in excess of 50% indicating the system
was overcooled and future increases in throttle setting could be achievable. With additional testing
required, including testing in excess of 5 seconds, the Test 44 throttle setting was not passed. Test
Campaign 2.0 included larger throttle settings and is discussed in Chapter 5 below. Injector
calorimetry results are shown in Figure 4.7 below. Heat flux values and corresponding hot wall
temperatures are less than half of those experienced on the outerbody. More discussion will occur
on these observations and their comparison to predictions later in this chapter.

90

Figure 4.6. Test 44; Outerbody Calorimetry Results; TC-208 Adjustment Resulting in Acceptable
Correlation with TC-210

91

Figure 4.7. Test 44; Injector Calorimetry Results
The next series of tests were aimed at longer duration run times to verify the cooling system
temperatures were reaching steady state. These tests were also completed to confirm the facility
performed as expected for test durations beyond those typically operated in a laboratory setting on
heat sink hardware (typically < 2 sec). The throttle setting was reduced for Test 45 to a predicted
chamber pressure of 77 psia to reduce the risk of hardware damage for the first test in excess of 1
second on the WC 1.0 hardware. The cooling system was operated in excess of 30 seconds to
verify longer duration operability and the ullage supply system maintained steady flowrates. As
shown in Figure 4.8, the test duration was increased to 3 seconds and the pressure regulated
propellant supply system maintained the commanded setpoints for the duration of the test.

92

Figure 4.8. Test 45; Propellant System Flowrates
The outerbody calorimetry results are shown in Figure 4.9 and the injector calorimetry
results are shown in Figure 4.10. Thermal steady state is reached shortly after 1 second of run
duration on the outerbody cooling system and prior to 1 second on the injector cooling system. It
is expected that this duration is driven by the lag in the thermocouple rise time rather than the hot
wall reaching a steady state temperature. Outerbody thermocouples remained in good correlation
with TC-210 taking slightly longer to reach steady state. A slight decay (~20 deg F) in outerbody
hot wall temperature and injector hot wall temperature is experienced over the duration of test.
Because of the cooling system configuration, the coolant inlet temperature varies over the run
duration.
As shown in Figure 4.11, the coolant temperature is rising during this particular test. The
coolant bulk storage and pressurization tank are located inside a thermally conditioned room
whereas the run line travels outside (75 ft of run line) and then back into a thermally conditioned
test cell. Furthermore, the coolant inlet temperature is taken ~ 8 ft in run line length upstream of
the test article. This results in a lag within the calorimetry temperature delta on the order of 1
second using approximate coolant velocities through the feed system. This decay in hot wall
93

temperature can likely be attributed to the increase in coolant supply temperature resulting in an
increase in the thermal conductivity of the coolant over the test duration. This will be discussed in
more detail for Test 47 below.

Figure 4.9. Test 45; Outerbody Calorimetry Results

94

Figure 4.10. Test 45; Injector Calorimetry Results

Figure 4.11. Test 45; Outerbody Coolant System Temperatures
95

The remaining two tests in Test Campaign 1.0 were completed at 10 second run time
durations. As noted on Test 45, thermal steady state was achieved in less than 1.5 seconds and wall
temperatures were stabilizing at acceptable levels to proceed with longer duration tests. The test
duration was increased to 10 seconds for Test 46 and Test 47. The high speed data acquisition
system was brought into operation starting with Test 41, resulting in the availability of high speed
manifold pressure data. Typically high speed manifold pressure data is correlated and validated
with high speed video imagery. As discussed earlier in this section, the high speed data acquisition
system was not available when the high speed camera was used on HS 1.0. Additionally, the high
speed camera was not used during WC 1.0 testing because water exited the aft end of the combustor
resulting in the inability to collect high speed video.
High speed video was captured on the HS 1.0 hardware for Test 20 and 21 at predicted
CTAP pressures of ~50 psia. Wave pass frequencies determined by high- speed video footage on
Test 20 and Test 21 were 12.5 kHz and 12.7 kHz, respectively. A power level at this low of
magnitude was not tested on the WC 1.0 hardware when high speed data was collected. Test 46
was the lowest throttle setting tested, resulting in a predicted CTAP pressure of ~72 psia. With
similar throttle settings, an attempt was made to correlate the wave pass frequency imaged on Test
20 and 21 with the high frequency manifold pressure response on Test 46. High frequency
manifold pressure data was collected during steady state combustor operation on Test 46. A
cabling issue was identified on the oxidizer high frequency pressure transducer for both tests and
was fixed for Test Campaign 2.0.
As shown in Figure 4.12, 13.6 kHz frequency content was evident in an FFT of the high
frequency fuel pressure data. Additionally, larger magnitude frequency content was visible at 26.6
kHz. The 13.6 kHz content is expected to be the wave pass frequency as it is notably comparable
to the wave pass frequencies captured during Test 20 and 21. Additionally, the speculated wave
pass frequency of 13.6 kHz fundamental frequency has a strong first harmonic at 26.6 kHz,
strengthening the argument that this is likely the wave pass frequency. The FFT of the high
frequency pressure data in the oxygen manifold was saturated with noise in this bandwidth and
was therefore unusable to make conclusions. Calorimetry data collected on Test 46 exhibited
similar behavior to that of Test 47 though heat fluxes were lower in magnitude due to the lower
throttle setting.

96

Figure 4.12. Test 46; Fuel Manifold High Frequency Pressure FFT
Test 47 was the last test in Test Campaign 1.0. The throttle setting was increased to a
predicted CTAP pressure of 98 psia. As shown in Figure 4.13 and Figure 4.14, outerbody and
injector hot wall temperatures remained well below the acceptable hot wall temperatures of 1200
deg F. The measured heat flux also remained well below the critical heat flux with over 50%
margin. The variations in heat flux are expected to be driven from variations in coolant inlet
temperature. As stated previously, the coolant supply line was subject to variations in temperature
prior to the test due to its length and sections of the line being in different parts of the facility at
different temperatures. The coolant inlet temperature was taken upstream of the test article which
results in a lag within the calorimetry temperature delta on the order of 1 second using approximate
coolant velocities through the feed system. Additionally, the thermal conductivity of the coolant
decreases with temperature over the range of coolant temperatures experienced during this testing.
This temperature delta lag along with the coolants thermal conductivity change are the driving
factors for the heat flux fluctuation. This heat flux variation was eliminated for Test Campaign 2.0
by flowing the coolant until a steady inlet temperature was achieved, then followed by combustor
ignition.

97

Figure 4.13. Test 47; Outerbody Calorimetry Results

98

Figure 4.14. Test 47; Injector Calorimetry Results
A summary of outerbody and injector heat fluxes from the WC 1.0 testing in Test
Campaign 1.0 are shown in Figure 4.15, Figure 4.16, Figure 4.17, and Figure 4.18. Each figure
contains the measured heat flux from the test and a predicted heat flux for the same operating
condition. The methodology for the predicted heat fluxes can be found in Section 3.2. For each
prediction analysis, the combustor performance and coolant inlet conditions were modeled. As
discussed in detail within Section 3.2 the predicted heat flux represents a constant pressure engine
throat level value. As evident in in Figure 4.15, the measured outerbody heat fluxes were larger
than the predicted throat level heat fluxes for most operating conditions. Though limited data exists
from Test Campaign 1.0, early evidence suggests that lower power levels result in near throat level
heat fluxes. With only a limited range of operating conditions tested in Test Campaign 1.0, it is
challenging to model a trendline that allows heat flux predictions at higher chamber pressures.
99

That being said, it is evident that RDRC operation produces heat fluxes in excess of throat level
constant pressure predictions. It should also be noted that these heat fluxes represent an average
value along the axial length of the combustor. It is expected that peak heat fluxes occur near the
detonation zone which will drive local wall temperatures to larger values than those shown for
Test Campaign 1.0. The values from Test Campaign 1.0 should be treated as average values.

Figure 4.15. WC 1.0 Outerbody Heat Flux Summary; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2

100

Figure 4.16. WC 1.0 Outerbody Heat Flux Ratio; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2
Similar to the outerbody prediction methodology, predicted heat fluxes in Figure 4.17
represent a constant pressure engine throat level value. As evident in the figure, measured heat
fluxes on the injector face remain at or below 50% of the predicted throat level heat fluxes. Though
limited data exists at high power levels, evidence suggests that injector heat flux is not as sensitive
to power level increases as the outerbody and could be conservatively predicted with a degraded
value of throat level heat flux. In conventional combustors, the injector face thermal environment
is dominated by recirculation of combustion products and reactant gas mixtures. Often times,
injector face heat loads can be predicted through the radiative environment alone. In an RDRE the
injector face is expected to also see a highly convective environment with shock-induced heating.
This study used an unlike doublet impinging injector arrangement and reactants that are upstream
of the impingement point are presumed to be pushed back against the injector face upon wave
passage. If present, this phenomenon would have a cooling effect but subsequent reaction in this
region would lead to heating. In addition, the injector is cooled somewhat by the flow of cold gases
through the orifices in the face. This balancing effect of reactant cooling and product heating may

101

offer insight into the steady heat load on the injector face. Further investigation into RDRE injector
face heat loads is recommended as future work.

Figure 4.17. WC 1.0 Injector Heat Flux Summary; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2

Figure 4.18. WC 1.0 Injector Heat Flux Ratio; Constant Pressure Throat Heat Fluxes were
Calculated Using the Methodology in Section 3.2

102

TEST CAMPAIGN 2.0 RESULTS

Test Campaign 2.0 included 309 seconds of hot fire testing and 121 starts/shutdowns. The
hardware versions tested included a heat sink combustor (HS 1.1) and a newly
designed/manufactured water-cooled combustor (WC 2.0). A summary of the hardware
configuration for HS 1.1 and WC 2.0 can be found in Table A.1 and described in detail in Chapter
2. HS 1.1 testing is summarized in Table 5.1. The WC 2.0 testing included long duration testing
and pulsed short duration testing. Long duration testing was completed to characterize heat flux
and high cycle fatigue (HCF) loading. Pulsed short duration testing was completed to evaluate
thermal cycling impacts to the combustor structure and evaluate low cycle fatigue (LCF) loading.
A summary of test conditions and results can be found in Table 5.2. Of the 309 seconds of total
test time, pulsed short duration testing comprising 197 seconds and long duration testing
comprising 112 seconds. The hardware experienced 118 LCF loadings on the combustor cooling
passages, equivalent to the amount of thermal cycle starts and shutdowns. An endurance test was
completed at 60 seconds in duration, demonstrating operation well beyond thermal steady state.
Additionally, ~3.7 million HCF loadings were placed on the combustor cooling passages,
equivalent to the approximate amount of detonation wave passes present for all of the WC 2.0
testing.

5.1

Heat Sink Testing

HS 1.1 hot fire testing is summarized in Table 5.1 below. Heat sink testing was completed
during Test Campaign 2.0 to collect high speed imaging data at higher power levels than pursued
during Test Campaign 1.0. This testing was used to validate the ignition concept and confirm
rotating detonation behavior existed at higher power levels than pursued during Test Campaign
1.0 before adding the additional facility complexity required to operate the water-cooled
combustor. Similar to Test Campaign 1.0, coolant from WC 2.0 exits the aft end of the combustor
thereby making high speed imaging through the aft end of the chamber impractical. High speed
video footage was captured during HS 1.1 testing to be used for correlation to WC 2.0 testing. Due
to the issues attempting to accommodate chamber pressure measurements on the WC 1.0 hardware,
chamber pressure measurements on the WC 2.0 hardware were not pursued. As in Test Campaign

103

1.0, HS 1.1 hardware was used to correlate chamber pressure with throttle setting for heat load
correlations.

Table 5.1. Test Campaign 2.0, HS 1.1, Hot Fire Testing Summary
Test
#

Total
Propellant
Flowrate
(lbm/s)

Mixture
Ratio
(O/F)

Predicted
CTAP
(psia)

48

0.147

3.9

103

43

0.75

13.1 (1 Wave, CW)

49

0.202

3.7

144

61

0.75

13.9 (1 Wave, CCW)

50

0.294*

4.1*

206*

95

0.75

15.6 (**)

Measured
Test
CTAP
Duration
(psia)
(sec)

Wave Pass
Frequency (kHz)

*Fuel mass flowrate estimated as fuel venturi did not choke during test
**Varying wave modes primarily between 1 wave CCW, 2 co-rotating waves CCW, and 4
waves (2 co-rotating waves CCW and 2 co-rotating waves CW); Wave pass frequency
determined during 2 wave mode

Test 50 resulted in the largest power level pursued during Test Campaign 2.0. The
flowrates required to achieve this power level were the maximum that could be provided by the
facility with the backpressures experienced in the combustor and the propellant feed system
downstream of the venturis used for flowrate measurement. High speed video footage was
captured on tests 48-50. Test 48 operated with a single wave mode, rotating clockwise (as viewed
from aft end of the combustor) with the wave pass frequency defined in Table 5.1. Test 49 also
operated with a single wave mode but the wave rotation was counterclockwise. Test 50 resulted in
varying wave modes throughout the 0.75 sec test. The primary wave mode was 2 co-rotating
waves, rotating counterclockwise. Other portions of the test included 1 wave rotating
counterclockwise and 4 waves comprised of 2 sets of counter-rotating waves. Images from the
high-speed video footage of each test can be seen in Figure 5.1. Due to issues with the
configuration file for the data acquisition, the high frequency pressure measurement data from the
oxygen and fuel manifolds were invalid and not used for video comparison on HS1.1. The clarity
of the images and complexity of capturing high speed video footage in this facility is described in
Section 4.

104

Figure 5.1. Test 21 High Speed Video Screen Captures For Tests 48-50
Detonation wave speeds were between 1500 m/s and 1800 m/s for Tests 48-50, resulting
in ~65% of Chapman Jouguet predicted speeds. As shown in Figure 4.1, chamber pressure
measurements were taken 0.68 in from the injector face for HS 1.0 during Test Campaign 1.0.
Measured chamber pressures were ~40% of predictions for Test Campaign 1.0 and this was
expected to be driven by the location of the pressure measurement and the associated pressure drop
of the combustion products. Additionally, the impinging element injectors were additively
manufactured in all hardware used for this study and the expectation is that they have poor
tolerances and surface roughness when compared to traditional EDM manufacturing. This would
presumably reduce the combustor performance and likely contribute to the lower than predicted
measured chamber pressures. No correlation was observed between wave characteristics and
measured CTAP measurements which is consistent with observations from prior studies [10].
The chamber pressure measurement location in HS 1.1 was moved coincident with the
impingement point of the propellants, 0.10 in from the injector face as shown in Figure 5.2. The
purpose of the adjustment to the chamber pressure measurement location was to capture the
chamber pressure closer to the injector face, prior to the pressure drop of the combustion products
as they approach the exit of the combustor. Measured chamber pressures remained ~40% of the
predictions for Test Campaign 2.0, despite the move of the chamber pressure measurement
location closer to the injector face.
The axial location of the detonation wave and the wave’s axial length during combustor
operation may provide insight into this observation. The fill height of the combustor can be
estimated by determining how far the propellant travels axially before the next detonation wave
arrives to consume the propellant. For this combustor design, oxygen injection velocities were
105

lower than fuel and were used to drive the fill height calculation. The results take into consideration
the impingement angle and indicate the fill height was roughly equal to length of the combustion
chamber (~1 in). With fresh propellant available the entire length of the chamber for each wave
pass during operation, it can be assumed that the detonation wavelength extended from the
impingement point to the exit plane of the combustor. This observation correlates with the
measured chamber pressure being 40% of the predicted chamber pressure despite the differences
in chamber pressure measurement between HS 1.0 and HS 1.1.

Figure 5.2. CTAP Measurement Location Comparison Between HS1.0 and HS1.1
One of the primary objectives of this research is to provide the RDE combustor designer
with a preliminary set of tools to complete trade studies that aid the design process. The correlation
of heat flux to chamber pressure is of critical importance to the designer as it greatly affects the
cooling system approach and design. Achieving a fundamental chamber pressure measurement in
an RDE is challenging. As described by Lim, the widely used CTAP approach represents a static
measurement and should not be directly compared to the stagnation pressures represented in
constant pressure combustors [38]. Lim highlights that axial placement of the CTAP location can

106

expose the measurement to varying degrees of dynamic pressure [38]. Additionally, the CTAP
measurement approach (ex. line length from measurement port to pressure transducer interface)
varies depending on research facility, inducing differences in attenuation to the measurement
source. These challenges introduce variability into the tools used by the designer. Because of the
measurement uncertainty, predicted chamber pressures were used in this work for correlations to
heat loading data. For reference, the performance assessment approach used to predict chamber
pressure is described in Section 2.4 and should be used by the designer when using heat loading
data in this document for design purposes. Linking the design process to a prediction approach
allows the designer to adopt their cooling system design to a standard performance assessment
which reduces induced uncertainties from measurement approaches.

5.2

Water Cooled Testing

WC 2.0 hot fire testing included long duration testing and pulsed short duration testing.
Long duration testing was completed to characterize heat flux and high cycle fatigue loading.
Pulsed short duration testing was completed to evaluate thermal cycling impacts to the combustor
structure and evaluate if low cycle fatigue (LCF) loading was present. A summary of the testing is
shown in Table 5.2. The WC 2.0 hardware experienced 307 seconds of total test time with pulsed
short duration testing comprising 195 seconds and long duration testing comprising 112 seconds.
Additionally, the hardware experienced 117 starts and shutdowns. Tests 52, 53, 54, and 64 were
used to characterize heat flux data at higher power levels than operated during Test Campaign 1.0.
Tests 59 and 65 were endurance tests operated at longer durations to evaluate long duration thermal
operation and high cycle fatigue (HCF) structural loading. Tests 55-58 and 61-63 were pulsed
short duration tests completed to evaluate thermal cycling impacts on the combustor. Table 5.3
provides the cumulative thermal cycles and cumulative test time placed on WC 2.0 throughout
Test Campaign 2.0. Further insight into each test can be found below.

107

Table 5.2. Test Campaign 2.0, WC 2.0, Long Duration Hot Fire Testing Summary
Hot Wall
Temp
(deg
F)^^
52
0.190
3.87
106
1
5
12.9
64.5
2.44
747
53
0.264
3.48
148
1
5
13.0
65.0
3.25
953
54
0.380
3.75
215
1
5
12.7
63.5
3.69
1061
55
0.188
3.95
105
1
2
13.1
26.2
2.44
760
56
0.190
4.00
106
10
20
12.9
258
2.45
761
57
0.188
3.95
105
19
33
12.9
429
2.49
763
58
0.190
3.87
106
20
35
13.0
455
2.50
766
59*
0.255
2.95
135
1
30
11.0
330
2.77
834
60*
0.152
3.00
84
1
2
11.5
40.3
1.65
560
61*
0.156
2.72
87
20
35
11.0
385
1.25
410
62*
0.156
2.72
87
20
35
10.7
375
1.01
350
63*^
0.157
2.74
87
20
35
10.7
375
1.25
410
64*
0.284
2.79
160
1
5
12.7
63.5
2.95
887
65*
0.206
2.88
115
1
60
12.3
738
2.30
716
*Leak downstream of oxygen feed system venturi resulted in suppressed O/F ratios. Oxygen system flowrates were estimated by correlating manifold pressure
data to previous test results
**Wave pass frequency determined through assessment of high frequency instrumentation
^High frequency data system failed to activate during test. Test at similar operating conditions used to estimate wave pass frequency.
^^Average values from outerbody calorimetry
Test
#

Total Prop
Flowrate
(lbm/s)

MR
(O/F)

Predicted
CTAP (psia)

Start /
Shutdown
Cycles

Total Test
Duration (sec)

Wave Pass
Freq (kHz)**

Total Wave
Passes
(x1000)

Heat Flux
(kW/cm^2)^^

108

Table 5.3. Test Campaign 2.0, WC 2.0, Cumulative Thermal Cycles and Total Test Duration
Test #

Start / Shutdown
Cycles

52

1

Cumulative
Thermal
Cycles
1

53

1

54

Total Test
Duration (sec)

Cumulative Test
Duration (sec)

5

5

2

5

10

1

3

5

15

55

1

4

2

17

56

10

14

20

37

57

19

33

33

70

58

20

53

35

105

59

1

54

30

135

60

1

55

2

137

61

20

75

35

172

62

20

95

35

207

63

20

115

35

242

64

1

116

5

247

65

1

117

60

307

For Test Campaign 2.0, the same cooling system upstream of the combustor was used with
different cavitating venturis to achieve the desired cooling flowrates. For each test the flowrate to
the outerbody was ~3.7 lbm/s, the flowrate to the innerbody was 1.90 lbm/s, and the flowrate to
the injector was 0.13 lbm/s. Manifold pressure was collected upstream of the outerbody cooling
circuit, allowing verification of the friction factor assumed for the thermal analysis. The outerbody
manifold pressure required to achieve the desired coolant flowrate was 30% larger than predicted.
A detailed discussion is provided below that highlights some of the cooling passages were likely
partially blocked due to the backpressure restrictions being a challenge to accommodate with
additive manufacturing. Not knowing the total cross section area or true surface roughness in the
channel makes it challenging to determine the larger magnitude supply pressure required. Surface
roughness values recommended by the vendor are listed in Table 2.2. If these values are correct,
the results indicate that the cross-sectional flow area may have been ~10% smaller than designed,
causing the larger supply pressure experienced. Assuming cross sectional area was as designed
(highly expected not to be the case as described in the detailed discussion below), surface

109

roughness values would have been 4 times larger than those in Table 2.2 to have caused the larger
supply pressure. Scanning electron microscope images in Figure 5.7 and Figure 5.8 provide
evidence that some cooling channels had a reduced cross sectional area. It is not known whether
that reduction in cross sectional area was present in a small quantity of cooling channels at a larger
magnitude or in a large number of cooling channels at a smaller magnitude. Not knowing the true
reduction in cross sectional area of the coolant exit, the surface roughness values recommended
by the manufacturer in Table 2.2 were used for this assessment.
The cooling system was started well before the combustor start transient to allow coolant
flowrates to achieve steady state. Automated abort monitoring was completed on cooling circuit
sensors prior to commanding ignition to verify the correct flowrates were being achieved and that
the system was performing nominally. The abort redlines continued for the duration of the test.
Prior to testing, the system was primed at low pressures to verify coolant flow was steady and
confirm bubbles did not ingress into the flow path. The cooling system was left operational
following the test until a nominal shutdown was confirmed and then was manually commanded to
shut down.

5.2.1 Heat Flux Characterization Testing and Calorimetry Uncertainty Assessment
Test 52 was 5 seconds in duration and used to characterize heat flux at a predicted chamber
pressure of 106 psi. Two thermocouples (TC-208 and TC-210) were used to measure coolant outlet
temperature. The difference in outlet temperature measured by both thermocouples during steady
state operation varied by ~9 deg F. These measurements are used directly in the calorimetry
analysis, as detailed in Section 3.1. As shown in Figure 5.3, this resulted in hot wall temperatures
varying by ~300 deg F and heat flux difference of ~1.1 kW/cm^2. Both thermocouples were
measuring coolant that passed through the same passage design and presumably driven by the
same hot gas convective environment and coolant conditions. The results indicate that flowrate
discrepancies between channels may have existed with further consideration provided below.

110

Figure 5.3. Test 52; Investigation of Outerbody Coolant Temperature Differences
The differences in outerbody coolant outlet temperature measurements are likely not driven
by the measurement accuracy of the type-k thermocouples used for testing. Using the KlineMcClintock methodology proposed by Walters et al., type-k thermocouple uncertainty should be
within approximately +/- 2 deg F at the temperatures under consideration [44]. As described in
Section 2.11 and shown below in Figure 5.4, the outerbody coolant outlet temperature
measurements were shrouded behind the nozzle wall to mitigate concerns from Test Campaign 1.0
that hot combustion products were impinging on the thermocouple and artificially elevating
measured coolant outlet temperatures. Installing these thermocouples for testing was more
challenging than expected during the design process. Due to the small part size and associated port
sizes, poor visibility existed in the coolant outlet port to verify proper placement of the

111

thermocouple. Challenges included making sure the thermocouple was plunged adequately enough
into the coolant stream but not far enough such that it touched the cold wall surface. To place the
thermocouple, the length from desired thermocouple tip placement to the fitting attachment point
were measured in CAD and then used when installing the thermocouple in the fitting. Predicted
outerbody cold wall temperatures for this testing varied between 500 deg F to 900 deg F depending
on operating conditions. Though the thermocouples would be bathed by coolant, it is expected that
if a thermocouple was touching the hot wall, much larger temperature excursions would have been
measured.

Figure 5.4. Outerbody Coolant Outlet Temperature Measurement, WC 2.0 Hardware
Both thermocouples used to measure outerbody coolant outlet temperature were replaced
for the following test to remove uncertainty that a defective sensor was causing the difference in
readings. Test 53 was then completed at 5 seconds in duration and used to characterize heat flux
at a predicted chamber pressure of 148 psi. A similar discrepancy between outerbody coolant outlet
temperature readings existed. The difference in outlet temperature measured by both
thermocouples during steady state operation varied at peak by ~10 deg F and on average by ~6
deg F. As shown in Figure 5.5, this resulted in hot wall temperatures varying at peak by ~350 deg

112

F and on average by ~235 deg F. Also shown in Figure 5.5, this resulted in heat flux prediction
predictions varying at peak by ~1.4 kW/cm^2 and on average by ~1.0 kW/cm^2.

Figure 5.5. Test 53; Investigation of Outerbody Coolant Temperature Differences
Test 54 was then completed at 5 seconds in duration and used to characterize heat flux at a
predicted chamber pressure of 215 psi. A similar discrepancy between outerbody coolant outlet
temperature readings existed. The difference in outlet temperature measured by both
thermocouples during steady state operation varied at peak by ~11 deg F on average. As shown in
Figure 5.6, this resulted in hot wall temperatures varying at peak by ~340 deg F on average. Also
shown in Figure 5.6, this resulted in heat flux predictions varying at peak by ~1.5 kW/cm^2 on
average.

113

Figure 5.6. Test 54; Investigation of Outerbody Coolant Temperature Differences

It is believed that the driving factor for this discrepancy is variation in coolant flow between
individual cooling passages in the combustor. The primary evidence for this hypothesis are results
from scanning electron microscope (SEM) images of the combustor following the test campaign.
Figure 5.7 is a SEM image of the innerbody, near the combustion chamber exit/transition to the
nozzle exit. The features highlighted in this image are nearly identical to the outerbody’s
construction. Because limited images of this region were taken, this figure is used for reference to
describe the outerbody because its highlights what a non-obstructed cooling passage should look
like.

114

Coolant flows from left to right through the cooling passage. The flow area dimensions are
set by the channel height of 0.030” (vertical axis in Figure 5.7) and the channel width of 0.100”
(visualized into/out of page in Figure 5.7). A flow restriction feature was placed near the exit of
the cooling channel to backpressure the coolant. Increasing the pressure in the cooling channel
reduced the possibility of critical heat flux being exceeded. With excessive facility coolant
pressure budget to achieve desired flowrate, this feature was included to mitigate risk of larger
than expected heat fluxes during detonative operation. The backpressure feature reduced the exit
flow area. The exit flow area dimensions are set by the exit height of 0.015” (vertical axis in Figure
5.7) and the exit width of 0.075” (visualized into/out of page in Figure 5.7). After exiting the
backpressure feature, coolant flowed into a thermocouple shroud before exhausting to ambient
conditions. The flow area of the thermocouple shroud was designed to accommodate a
thermocouple, not to provide specific flow conditions. The SEM image in Figure 5.7 represents a
clear cooling passage with no identified obstructions.

Figure 5.7. Scanning Electron Microscope Image of WC 2.0 Hardware; Cooling Channel;
Unobstructed Backpressure Feature
115

The SEM image in Figure 5.8 represents an obstructed cooling passage. The level of
obstruction is unknown as the image represents a slice of the hardware and flow area could exist
in the radial direction (into/out of the page). Though it is unclear how much of the flow area was
obstructed, it is clear that the passage in the image was operating with an off-design condition and
therefore resulted in an off-nominal flowrate through the passage. A limited quantity of SEM
images were taken so it is also unclear how many passages were obstructed and/or if passages
were completely obstructed and not permitting any flowrate. No discoloration was observed in the
hot wall indicating that combustion chamber was cooled adequately. Analyzing whether the
hardware could survive operation with a fully obstructed cooling passage is beyond the scope of
this work.

Figure 5.8. Scanning Electron Microscope Image of WC 2.0 Hardware; Cooling Channel,
Obstructed Backpressure Feature

116

To accommodate the variations in passage flow area, an exit temperature averaging
approach was adopted. The methodology for this approach is described in Section 3.1. Metering
individual coolant passage exit streams greatly simplified manufacturability of this test hardware
but also presented challenges that should be taken into consideration for future studies. Collecting
coolant exit temperature in a manifold represents the average coolant exit temperature of all the
coolant passages that flow into the manifold. If variations in passage dimensions exist which
impact the coolant flow in each passage individually, the local coolant exit temperature may vary
from passage to passage. A path forward for future studies is recommended in Section 7.
Using the predictive thermal model discussed in Section 3.2, a rough estimate of the
velocity degradation of the coolant through an obstructed passage can be approximated. The
average heat flux measured during Test 54 was ~3.69 kW/cm^2. Artificially prescribing this heat
flux in the predictive model and then varying the coolant velocity until the measured coolant outlet
temperatures are achieved provides a rough estimate of passage variations. Using this
methodology, results indicate that the obstruction could have limited the coolant velocity to half
of its target value. As critical heat flux is primarily driven by coolant velocity, passage to passage
variations due to manufacturing methods or unintentional obstructions should be monitored
closely. Additionally, testing should be approached with significant cooling margin to avoid
hardware damage.
Using the heat flux averaging approach described in Section 3.1, Tests 52-54 were
evaluated further to determine the heat loading relationship to power level. A summary of these
performance metrics can be found in Table 5.4 and Table 5.5. Predicted hot wall temperature and
margin to critical heat flux exceedance were monitored as performance metrics to determine how
close the combustor was to exceeding thermal limits. The hot wall temperature performance metric
was evaluated with respect to a 1200 deg F limit where yield strength is appreciably degraded. The
heat flux performance metric was evaluated with respect to the critical heat flux for each test. If
critical heat flux is exceeded, localized boiling can be expected and risk to hot wall burn through
increases significantly. As margin to these performance metrics decrease, the combustor can be
considered as operating closer to predicted thermal failure.

117

Table 5.4. Test Campaign 2.0, Outerbody Thermal Loading Performance Metric Summary
Test #

52
53
54

Predicted
Chamber
Pressure
(psia)
106
148
215

Heat Flux
(kW/cm^2)

Critical
Heat Flux
Margin

Hot Wall
Hot Wall
Temperature Temperature
(deg F)
Margin

2.44
3.25
3.69

90%
40%
13%

747
953
1061

37%
21%
11%

Table 5.5. Test Campaign 2.0, Injector Thermal Loading Performance Metric Summary
Test #

52
53
54

Predicted
Chamber
Pressure
(psia)
106
148
215

Heat Flux
(kW/cm^2)

Critical
Heat Flux
Margin

Hot Wall
Hot Wall
Temperature Temperature
(deg F)
Margin

0.78
0.85
0.85

>100%
>100%
>100%

305
322
322

>100%
>100%
>100%

The outerbody cooling calorimetry results from Test 52 can be found in Figure 5.9 below
and was operated at a predicted chamber pressure of 106 psi. Due to the calorimetry averaging
approach, these values fall between the two calorimetry results presented in Figure 5.3 which
treated each outerbody coolant temperature measurement individually. The injector cooling
calorimetry results from Test 52 can be found in Figure 5.10.

118

Figure 5.9. Test 52; Outerbody Calorimetry Results

Figure 5.10. Test 52; Injector Calorimetry Results
119

As shown in Figure 5.11, the WC 2.0 combustor included an accelerometer mounted on
the outer circumference to measure radial acceleration and mounted on the aft face to measure
axial acceleration. Additionally, high speed pressure transducers were ported into the fuel manifold
and oxygen manifold. Data from these high-speed measurements were processed into power
spectral density (PSD) plots. PSD plots provide insight into the relative strength of various
frequency components within a given signal. Figure 5.12 is a PSD of the circumferentially
mounted accelerometer measuring radial acceleration. As shown in the figure, the signal strength
of this measurement was most prominent at 12.9 kHz. This was identified to be the wave pass
frequency as it was shown to correlate well with the wave pass frequency identified on Test 48
(reference Table 5.1) running at a similar operating condition and identified through high-speed
video footage. In addition to the wave pass frequency, the first harmonic (2x wave pass frequency)
and 2nd harmonic (3x wave pass frequency) are observed.

Figure 5.11. WC 2.0, Accelerometer Placement

120

Figure 5.12. Test 52, Power Spectral Density of Radial Acceleration
Figure 5.12 is a PSD of the aft face mounted accelerometer measuring axial acceleration.
Figure 5.14. is a PSD of the high frequency fuel manifold pressure. High frequency oxidizer
manifold pressure was determined to be erroneous and excluded from evaluation. The wave pass
frequency, first harmonic, and second harmonic were all observed to occur at the same frequencies
across the operational high-speed instrumentation for Test 52. This general trend continued for
Tests 52-54 as chamber pressure was increased from 106 psi to 215 psi though in some cases the
wave pass frequency and harmonics were less prominent. A trend between wave pass frequency
and chamber pressure was not observed. Additionally, a trend between PSD magnitude and
pressure was not observed. To avoid repetitiveness, high speed instrumentation PSD plots are not
presented for Test 53 and 54, instead the wave pass frequencies were identified and captured in
Table 5.2.
One of the primary purposes of this study was to gain insight into the high cycle fatigue
and low cycle fatigue characteristics of RDE operation. The focus area of this assessment was the
combustion chamber hot wall as it was expected to experience the cyclic pressure loading from
the passing detonation wave and the largest thermal gradient. It is important to note that data from

121

the radial and axial accelerometer measurements are useful to inform a global assessment of
combustor vibration rather than a microscopic view of combustion chamber hot wall.
Instrumenting the hot wall with an accelerometer or strain gauge presented challenges. The hot
wall itself cannot be instrumented as the combustion environment produces temperatures that
exceed the operational capability of all applicable instrumentation. The cold wall is the next best
alternative but it is limited in space (0.030 in width) and bathed in high pressure coolant flowing
at velocities approaching 100 ft/s. Even if instrumentation could be placed in this environment it
would be challenging to seal the coolant flow passage and the instrumentation would likely disrupt
the cooling capacity of the fluid as it would take up surface area on the cold wall.

Figure 5.13. Test 52, Power Spectral Density of Axial Acceleration
Realizing these instrumentation placement restrictions, the author placed the
accelerometers on the outer surface of the hardware. Both accelerometers were over 0.80 in from
the hot wall. It is expected that the vibration environment measured at this location was primarily
driven by the detonation event propagating through the combustor material. As the detonation
event traverses the annulus of the combustion chamber, a pressure wave from the detonation event
122

propagates through the material similar to how a sound wave propagates through air. The global
structural vibration of the combustor is also expected to be present in the accelerometer readings,
but the frequency content of these vibrations is well below that of wave pass frequency. For
example, the natural frequency of the combustor outer body in the radial and axial direction are
both expected to be less than 2 kHz when estimating the structure as a cylinder fixed rigidly on
one end and representative material properties.

Figure 5.14. Test 52, Power Spectral Density of Fuel Manifold Pressure
The outerbody cooling calorimetry results from Test 53 can be found in Figure 5.15 below
and for reference was operated at a predicted chamber pressure of 148 psi. The injector cooling
calorimetry results from Test 53 can be found in Figure 5.15. The outerbody cooling calorimetry
results from Test 54 can be found in Figure 5.17 below and for reference was operated at a
predicted chamber pressure of 215 psi. This test represented the highest power level achieved on
the WC 2.0 hardware. Increasing power level beyond this was limited by the facility pressure
budget. The injector cooling calorimetry results from Test 54 can be found in Figure 5.18. As
highlighted in Table 5.4 and Table 5.5, the larger thermal load was present on the outerbody when
123

compared to the injector. Calorimetry data was not collected on the innerbody and therefore could
not be evaluated. The performance metrics highlight that hot wall temperature margin would have
likely been the limiting thermal loading factor if higher power levels would have been pursued.

Figure 5.15. Test 53; Outerbody Calorimetry Results

124

Figure 5.16. Test 53; Injector Calorimetry Results

Figure 5.17. Test 54; Outerbody Calorimetry Results

125

Figure 5.18. Test 54; Injector Calorimetry Results
Test 54 concluded the data collected from Test Campaign 2.0 aimed at developing a
relationship between power level and heat loading. A global assessment of the trends are presented
here, including data from Test Campaign 1.0 to draw conclusions. Test 55-65 included endurance
tests and pulsed short duration testing to evaluate structural characteristics. Calorimetry was also
collected for test 55-65 and will be discussed following the global heat loading trend assessment
presented here. A summary of outerbody and injector heat fluxes from Test Campaign 1.0 and 2.0
are shown in Figure 5.19, Figure 5.20, Figure 5.21, and Figure 5.22. Similar to the Test Campaign
1.0 conclusions, each figure contains the measured heat flux from the test and a predicted heat flux
for the same operating condition. The methodology for the predicted heat fluxes can be found in
Section 3.2. For each prediction analysis, the combustor performance and coolant inlet conditions
were modeled. As discussed in detail within Section 3.2 the predicted heat flux represents a
constant pressure engine throat level value.

126

As evident in in Figure 5.19 and Figure 5.20, the measured outerbody heat fluxes were
larger than the predicted throat level heat fluxes for most operating conditions. At lower power
levels it is evident that RDRC operation produces heat fluxes near throat level constant pressure
predictions. At higher power levels it is evident that RDRC operation produces heat fluxes in
excess of throat level constant pressure predictions. It should also be noted that the thermal
methodology in Chapter 5 used to complete this assessment assumes the ideal chamber pressure
and all of the propellant in the combustor is burned. Fill heights were calculated to exceed the
chamber length of the WC 2.0 hardware and propellant is assumed to have been exiting without
being combusted. These factors would even further amplify the ratios shown in Figure 5.20. Due
to facility limitations, a limited range of operating conditions could be tested throughout Test
Campaign 1.0 and Test Campaign 2.0. These limitations make it challenging to model a trendline
that allows heat flux predictions at higher chamber pressures.

Outerbody Heat Flux
Measured

Constant Pressure Throat

4

Heat Flux (kW/cm^2)

3.5
3
2.5
2
1.5
1
0.5
70

90

110

130

150

170

190

210

230

Predicted Chamber Pressure (psia)

Figure 5.19. WC 1.0 and 2.0 Outerbody Heat Flux Summary from Test Campaign 1.0 and 2.0;
Constant Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2

127

Measured Heat Flux/CP Throat Heat Flux

Ratio of Measured Outerbody Heat Flux to Constant
Pressure Throat Level Predictions
1.7

1.5
1.3
1.1
0.9
0.7
0.5
70

90

110

130

150

170

190

210

230

Predicted Chamber Pressure (psia)

Figure 5.20. WC 1.0 and 2.0 Outerbody Heat Flux Ratio from Test Campaign 1.0 and 2.0; Constant
Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2
Similar to the outerbody prediction methodology, the predicted heat fluxes in Figure 5.21
and Figure 5.22 represent a constant pressure engine throat level value. As evident in the figures,
measured heat fluxes on the injector face remain at or below 50% of the predicted throat level heat
fluxes, even at higher power levels. Though limited data exists at high power levels, evidence
suggests that injector heat flux is not as sensitive to power level increases as the outerbody and
could be conservatively predicted with a degraded value of throat level heat flux. In conventional
combustors, the injector face thermal environment is dominated by recirculation of combustion
products and reactant gas mixtures. Often times, injector face heat loads can be predicted through
the radiative environment alone. In an RDRE the injector face is expected to also see a highly
convective environment with shock-induced heating. This study used an unlike doublet impinging
injector arrangement and reactants that are upstream of the impingement point are presumed to be
pushed back against the injector face upon wave passage. If present, this phenomenon would have
a cooling effect but subsequent reaction in this region would lead to heating. In addition, the
injector is cooled somewhat by the flow of cold gases through the orifices in the face. This
balancing effect of reactant cooling and product heating may offer insight into the steady heat load

128

on the injector face. Further investigation into RDRE injector face heat loads is recommended as
future work.

Injector Heat Flux
Measured

Constant Pressure Throat

3.5

Heat Flux (kW/cm^2)

3
2.5
2
1.5
1
0.5
0
70

90

110

130

150

170

190

210

230

Predicted Chamber Pressure (psia)

Measured Heat Flux/CP Throat Heat Flux

Figure 5.21. WC 1.0 and 2.0 Injector Heat Flux Summary from Test Campaign 1.0 and 2.0;
Constant Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2

Ratio of Measured Injector Heat Flux to Constant
Pressure Throat Level Predictions
0.6
0.5

0.4
0.3
0.2
0.1
0
70

90

110

130

150

170

190

210

230

Predicted Chamber Pressure (psia)

Figure 5.22. WC 1.0 and 2.0 Injector Heat Flux Ratio from Test Campaign 1.0 and 2.0; Constant
Pressure Throat Heat Fluxes were Calculated Using the Methodology in Section 3.2

129

5.2.2 Endurance Testing
Prior to the first endurance test, there were a series of pulsed short duration tests that will
be discussed in Section 5.2.3. Tests 59 and 65 were endurance tests operated at extended durations
to evaluate long duration thermal operation and HCF structural loading. Test 64 was originally
planned to be a heat flux characterization test but a leak impacted the test results and it adds most
value to discuss its results with the other endurance test results. Test 59 was the first endurance
test. It was 30 seconds in duration and targeted to operate at a predicted chamber pressure of 200
psia. During post test analysis of Test Campaign 2.0, it was found that an oxygen leak existed
downstream of the run valve venturi used to measure flowrate. Between tests, operating conditions
were verified by validating that the targeted flowrate was achieved.
As the leak was downstream of the venturi used to measure flowrate, the oxygen leak was
present but not noticeable in the flowrate data. The leak was discovered by evaluating manifold
pressure data. To determine the actual flowrate achieved during the remainder of testing, the
manifold pressure in the oxygen circuit was correlated to the previous test data that included
accurate flowrate results. During tests with the leak, the flowrate was then approximated using the
achieved manifold pressures as the leak was expected to be upstream of the manifold. Tests
operating with this leak experienced a reduction in achieved power level and suppression of
mixture ratio. For Test 59, the average predicted chamber pressure for the duration of the test was
~145 psia with an average mixture ratio of 2.5.
Outerbody and injector calorimetry results for Test 59 are shown in Figure 5.23 and Figure
5.24, respectively. The outerbody hot wall temperature operated at ~834 deg F on average while
the heat flux operated at ~2.77 kW/cm^2 on average throughout the test. The injector hot wall
temperature operated at ~310 deg F on average while the heat flux operated at ~0.79 kW/cm^2 on
average throughout the test. Though these values are average, some fluctuation in predicted hot
wall temperature was observed early in the test followed by a small but steady climb until
shutdown. A description for why this climb in thermal loading occurred can be found below. As
shown in Figure 5.25, the wave pass frequency of ~11.0 kHz and its first harmonic are visible in
the high frequency radial accelerometer data.

130

Figure 5.23. Test 59, Outerbody Calorimetry Results from Endurance Testing

131

Figure 5.24. Test 59, Injector Calorimetry Results from Endurance Testing

132

Figure 5.25. Test 59, Power Spectral Density of Radial Acceleration
As shown in Figure 5.26, fuel manifold pressure varied throughout the test. At point A the
fuel regulator overshot causing an increase in fuel flowrate. At point B the fuel regulator had
corrected and achieved the set pressure but the available fuel mass for the test was overpredicted.
This overprediction resulted in bulk fuel supply pressures steadily declining below the target
pressure from point B to C. As shown in Table 5.6, these variations in fuel supply pressure resulted
in a varying mixture ratio and power level throughout the test. Note, the data provided in Table
5.6 includes the corrected oxygen mass flowrate to accommodate the propellant leak. The
variations in mixture ratio correlate with the variations in heat flux and hot wall temperature shown
in Figure 5.23 and Figure 5.24.
At point A, the combustor was operating at the highest power level but experienced the
lowest heat flux and hot wall temperature throughout the test. Point A also correlated with the
lowest mixture ratio. The results are expected, as combustion temperatures are expected to decay
as the mixture ratio varies away from the stoichiometric mixture ratio of 4 for this propellant
combination. At point B, the combustor was operating at nearly the same power level but with an

133

increased mixture ratio. The corresponding heat flux at this point was ~15% higher than at point
A. As the test continued, fuel manifold pressure declined which further increased the mixture ratio.
At point C, the power level had dropped to the lowest value throughout the test while the mixture
ratio had reached the highest value. Though still below stoichiometric, Point C correlated to the
highest heat flux experienced during the test.

Figure 5.26. Test 59, Propellant Manifold Pressure
To highlight the significance of mixture ratio on heat loading, a 14% rise in mixture ratio
towards stoichiometric resulted in a ~23% increase in heat flux and ~20% rise in hot wall
temperature. It is expected that this assessment likely underscores the true impact mixture ratio
has on heat flux as power level decreased by 6% during the mixture ratio shift. If power level was
to remain constant and this assessment was to take into consideration a true mixture ratio change,
the increase in heat flux loading and wall temperature likely would have been larger. As fuel is
typically the primary choice of coolant in rocket combustors, the cooling system designer will be
a major contributor to the system level trade of what mixture ratio provides an acceptable cooling
and performance for the combustor.
134

Figure 5.27. Test 59, Outerbody Hot Wall Temperature and Heat Flux

Table 5.6. Test 59, Heat Flux Variation with Operation Conditions

B

Predicted
Chamber
Pressure (psia)
138
137

C

130

Reference
Point
A

2.9
3.0

2.30

Hot Wall
Temperature
(deg F)
715

2.65

811

3.3

2.83

857

Mixture Ratio

Heat Flux
(kW/cm^2)

Test 64 was a 5 second duration test operated a predicted chamber pressure of 160 psia and
mixture ratio of 2.79. Outerbody and injector calorimetry results are shown in Figure 5.51 and
Figure 5.52, respectively. The outerbody hot wall temperature calculated to be ~887 deg F, while
the heat flux was calculated to be ~2.95 kW/cm^2 throughout the test. The injector hot wall
temperature operated at ~331 deg F on average while the heat flux operated at ~0.87 kW/cm^2 on
average throughout the test. This test helps to further highlight the significance of mixture ratio on
heat loading. Interpolating the results shown in Figure 5.19, the heat flux for this predicted chamber
pressure operating at a mixture ratio at or near stoichiometry should have resulted in a heat flux of

135

~3.45 kW/cm^2. The heat flux results for this test were ~17% lower operating at the suppressed
mixture ratio.

Figure 5.28. Test 64, Outerbody Calorimetry Results from Pulsed Short Duration Testing

136

Figure 5.29. Test 64, Injector Calorimetry Results from Pulsed Short Duration Testing
Test 65 was the last test in the Test Campaign 2.0 series and was the longest test completed
for this research. It was an endurance test operated at 60 seconds in duration intended to
accumulate as many wave passes on the combustor in one firing as possible. The 60 second
duration was limited by the amount of coolant available at the facility. The test was operated a
predicted chamber pressure of 115 psia and mixture ratio of 2.88. Outerbody and injector
calorimetry results are shown in Figure 5.30 and Figure 5.31, respectively. The outerbody hot wall
temperature operated at ~716 deg F on average while the heat flux operated at ~2.30 kW/cm^2 on
average throughout the test. The injector hot wall temperature operated at ~287 deg F on average
while the heat flux operated at ~0.73 kW/cm^2 on average throughout the test. As shown in Figure
5.32, the wave pass frequency was 12.3 kHz resulting in ~738,000 wave passes on each cooling
passage in the combustor.
137

Figure 5.30. Test 65, Outerbody Calorimetry Results from Pulsed Short Duration Testing

138

Figure 5.31. Test 65, Injector Calorimetry Results from Pulsed Short Duration Testing

139

Figure 5.32. Test 65, Power Spectral Density of Radial Accelerometer
5.2.3 Pulsed Short Duration Testing
Following heat flux characterization testing, a combination of pulsed short duration testing
and endurance testing was completed. Endurance testing was discussed in Section 5.2.2 and pulsed
short duration testing will be discussed here. Tests 55-58 and 61-63 were pulsed short duration
tests completed to evaluate thermal cycling impacts on the combustor. The primary objective of
the pulsed short duration testing was to evaluate the impacts of thermal loading and the subsequent
LCF performance of the combustor hot wall. Though aimed at studying LCF performance, these
tests also contributed substantially to the total wave passes used for the HCF assessment.
For pulsed short duration testing, the start sequence was altered to complete as many
thermal cycles as possible with the available high-pressure water as coolant. With the water supply
tank full, it was estimated that 115 sec of runtime could be achieved at the total coolant flowrate
used during testing. To be conservative and avoid depletion of coolant during hot fire testing, the
140

coolant never flowed longer than 100 seconds. For the pulsed short duration testing, the coolant
supply was not turned off in between each test. Instead, the coolant supply was left operational
and the combustor was allowed to cool to nearly ambient temperature before the next short
duration firing. A thermal cycle was considered a combination of one start and one shutdown of
the combustor. Each short duration firing included the following sequence of events, all while
coolant remained flowing at the desired operating conditions:
•

The predet propellant circuits were charged in preparation for ignition

•

The oxygen run valve was opened, allowing oxygen to flow at the desired operating
conditions flowrate

•

The fuel run valve was opened, allowing fuel to flow at the desired operating condition
flowrate

•

Ignition was commanded by activating the predet spark plug

•

The oxygen run valve was closed, initiating the shutdown transient

•

The oxygen circuit purge downstream of the run valve was initiated to purge remaining
exhaust gases in preparation for the next ignition event

•

The fuel run valve was closed

•

The fuel circuit purge downstream of the run valve was initiated to aid in the purging of
remaining exhaust gases in preparation for the next ignition event

•

The cycle was repeated.
Test 55 was intended to be the first pulsed short duration test. A spark plug failure

following the first ignition event resulted in the completion of only one thermal cycle. Despite the
test objectives not being met, this test proved valuable in the evaluation of how quickly a thermal
cycle could be completed. Figure 5.33 is the thermal cycle event that occurred from the single hot
fire event during Test 55. As shown in the figure, the hot wall temperature is predicted to reach
thermal steady state ~ 1 second after ignition. In actuality, thermal steady state is likely reached in
a fraction of this time, but this calorimetry assessment is limited by the response lag of the
thermocouples measuring the water temperatures. Following the shutdown command the

141

combustor returns to nearly ambient conditions in less than 2 seconds. Using these guidelines a
minimum pause of 2 seconds between the next ignition command was used.

Figure 5.33. Test 55, Description of a Thermal Cycle
Test 56 was the first successful pulsed short duration test. The test included 10 thermal
cycles, and each firing was commanded to the same predicted chamber pressure of 106 psi for the
duration of the test. The total hot fire duration of the 10 thermal cycles was 20 seconds. The thermal
cycle characteristics subjected on the outerbody hot wall and injector hot wall can be seen in Figure
5.34 and Figure 5.35, respectively. The predicted/computed outerbody hot wall temperature was
~761 deg F on average while the heat flux averaged ~2.45 kW/cm^2 for the test. The hot wall
temperature following shutdown of each pulsed firing event climbed slightly for the first 3 tests

142

and then remained steady for the remaining tests. This is likely attributable to a steady state
temperature being reached during the cooling cycles prior to the next hot fire event. The slight
climb in temperature for the first 3 tests likely could have been mitigated by increasing the pause
between each pulsed duration firing event. This additional pause time was not pursued as it would
have reduced the amount of firing events achieved during the a given test which was limited in run
duration due to the coolant supply.
The injector hot wall temperature operated at ~308 deg F on average while the heat flux
operated at ~0.82 kW/cm^2 on average throughout the test. The repeatability in the coolant delta
T and corresponding calorimetry data is a notable feature of the pulsed short duration testing. Some
variation does exist across the thermal cycles but the repeatability remains near or below the
uncertainty of the thermocouples used. A notable feature in the injector calorimetry data is the rise
in hot wall temperature prior to each combustor ignition event. It is expected that this is the predet purge pushing hot pre-det combustion products through the combustion chamber from the
previous ignition event. Data from a thermocouple in the pre-det supply line to the combustion
chamber trends with this conclusion. As shown in Section 2, the injector cooling system wraps
around the pre-det supply port and would experience heat transfer from these hot combustion
products.

143

Figure 5.34. Test 56, Outerbody Calorimetry Results from Pulsed Short Duration Testing
Due to high frequency data acquisition limitations, the high speed data collection system
was only activated for the first firing event during each pulsed short duration test. Because each
firing event during the test duration was commanded to the same operating conditions, the high
speed data collected during the first firing event was assumed to be similar to the remaining firing
events that did not have high speed data collected. Figure 5.36 presents a PSD of the
circumferentially mounted accelerometer measuring radial accelerations. Similar to the trends
observed during previous WC 2.0 tests, the wave pass frequency of 12.9 kHz was identifiable
along with its second harmonic.

144

Figure 5.35. Test 56, Injector Calorimetry Results from Pulsed Short Duration Testing

145

Figure 5.36. Test 56, Power Spectral Density of Radial Acceleration
Figure 5.37 presents a closer look at the first thermal cycle of Test 56. As shown in the
figure, the hot wall reached a steady state temperature for over 1 second. In actuality, this duration
was likely closer to 1.5 seconds when taking into consideration the response time of the
thermocouple. To increase the amount of thermal cycles that could be completed during testing,
combustor hot fire time was decreased by 0.25 seconds for each thermal cycle. Additionally,
propellant and igniter purge operations were shortened, along with a reduction in the dwell time
in between hot fire events. These accommodations increased the amount of thermal cycles from
quantity 10 to 20. Test 57 included 19 thermal cycles, and each firing was commanded to the same
predicted chamber pressure of 105 psi for the duration of the test. 20 thermal cycles were expected
but the combustor failed to ignite on the 15th thermal cycle but continued to ignite for the remaining
cycles. A thermocouple was present in the hot gas supply line to the combustion chamber,
downstream of the predet. The temperature data from this thermocouple is shown in Figure 5.38,
which concluded that the pre-det failed to ignite for the 15th cycle. The total hot fire duration of
the 19 thermal cycles was ~33 seconds.

146

Figure 5.37. Test 56, Outerbody Calorimetry Results for First Thermal Cycle
The thermal cycle characteristics for Test 57 subjected on the outerbody hot wall and
injector hot wall can be seen in Figure 5.39 and Figure 5.40 respectively. The outerbody hot wall
temperature operated at ~763 deg F on average while the heat flux operated at ~2.49 kW/cm^2 on
average throughout the test. The injector hot wall temperature operated at ~302 deg F on average
while the heat flux operated at ~0.80 kW/cm^2 on average throughout the test. Figure 5.41 presents
a closer look at the first thermal cycle of Test 57. As shown in the figure, the hot wall reached a
steady state temperature for over 0.50 seconds. In actuality, this duration was likely closer to 1.5
seconds when taking into consideration the response time of the thermocouple. An issue occurred
triggering the high speed data acquisition during this test. As this test operated at nearly identical
inlet conditions as the Test 56, the wave pass frequency was estimated to be the same.

147

Figure 5.38. Test 57, Temperature in Pre-Det Supply Line that Supplies the Combustion Chamber
Ignition Port

148

Figure 5.39. Test 57, Outerbody Calorimetry Results from Pulsed Short Duration Testing

149

Figure 5.40. Test 57, Injector Calorimetry Results from Pulsed Short Duration Testing

150

Figure 5.41. Test 57, Outerbody Calorimetry Results for First Thermal Cycle
The thermal cycle characteristics for Test 58 subjected on the outerbody hot wall and
injector hot wall can be seen in Figure 5.42 and Figure 5.43 respectively. The test included 20
thermal cycles, and each firing was commanded to the same predicted chamber pressure of 106
psi for the duration of the test. The flowrate setpoints to reach the predicted chamber pressure can
be found in Table 5.2. The total hot fire duration of the 20 thermal cycles was 35 seconds. The
outerbody hot wall temperature operated at ~766 deg F on average while the heat flux operated at
~2.50 kW/cm^2 on average throughout the test. The injector hot wall temperature operated at ~310
deg F on average while the heat flux operated at ~0.84 kW/cm^2 on average throughout the test.
For comparison, it is worth noting that Space Shuttle Main Engine (SSME) throat level heat fluxes
are ~8 kW/cm^2.

151

Figure 5.42. Test 58, Outerbody Calorimetry Results from Pulsed Short Duration Testing

152

Figure 5.43. Test 58, Injector Calorimetry Results from Pulsed Short Duration Testing
Test 60 experienced a pre-det spark plug failure and only achieved two thermal cycles. The
intended predicted chamber pressure was 105 psia, but the oxygen leak caused the combustor to
operate at a predicted chamber pressure of ~84 psia and mixture ratio of ~3.0. The total hot fire
duration of the two thermal cycles was 3.5 seconds. The outerbody hot wall temperature operated
at ~560 deg F on average while the heat flux operated at ~1.65 kW/cm^2 on average throughout
the test. The injector hot wall temperature operated at ~240 deg F on average while the heat flux
operated at ~0.58 kW/cm^2 on average throughout the test.
The predet spark plug was replaced and the same test was repeated for Test 61. Twenty
thermal cycles were achieved, and the combustor was operated at a predicted chamber pressure of
~87 psia and mixture ratio of 2.72. As shown in Figure 5.44, outerbody heat flux appeared to vary
from thermal cycle to thermal cycle. Additionally, it appears that the heat flux was varying between
153

two distinct modes. Propellant manifold pressure remained constant for each thermal cycle as
shown in Figure 5.45. This indicates that the same propellant inlet conditions were provided to the
combustor and it is likely not a facility issue causing variations in operating conditions between
each thermal cycle. As shown in Figure 5.46 some variations in heat loading from thermal cycle
to thermal cycle do exist in the injector calorimetry data but the variations are far less prominent
as on the outerbody and do not align with the two distinct modes experienced on the outerbody.

Figure 5.44. Test 61, Outerbody Calorimetry Results from Pulsed Short Duration Testing

154

Figure 5.45. Test 61, Propellant Manifold Pressures

155

Figure 5.46. Test 61, Injector Calorimetry Results from Pulsed Short Duration Testing
Test 62 was intended to be a repeat of Test 61. The oxygen leak present during testing
resulted in an underestimation of the available oxygen mass to complete the test. As shown in the
propellant manifold pressure data in Figure 5.47, the first 5 thermal cycles were completed at ~87
psia chamber pressure and mixture ratio of 2.72. The remaining tests declined from this operating
condition to the lowest operating conditions of ~65 psia chamber pressure and mixture ratio of
2.15 on the last thermal cycle. The decline in operating conditions is present in the outerbody and
injector thermal loading data shown in Figure 5.48 and Figure 5.49, respectively. Even with the
decline in operating conditions, the outerbody calorimetry data appears to experience some thermal

156

cycles with elevated heat loading. Similar to Test 61, these large heat loading fluctuations
experienced on the outerbody do not exist on the injector calorimetry data.

Figure 5.47. Test 62, Propellant Manifold Pressures
As highlighted on Test 60 and 61, the phenomenon causing the large shifts in heat loading
are only present on the outerbody. The coolant temperature variations causing these shifts are
outside of the uncertainty of the type-k thermocouples used and are not expected to be driven by
instrumentation uncertainty. Because of the oxygen leak, the combustor was operating at off
nominal mixture ratios that were not characterized on HS 1.0 testing. Due to the facility limitation,
high speed data was only collected for the first thermal cycle of each pulsed short duration testing
as the combustor was expected to exhibit the same performance during each thermal cycle. That
being said, the first thermal cycle for Test 61 operated at the larger heat loading mode while the

157

first thermal cycle for Test 62 operated at the lower heat loading mode. This offered the ability to
compare high frequency data between the two distinct operating conditions.
Figure 5.50 presents a PSD of the radial accelerometer for the first thermal cycle during
Test 61 and Test 62. Test 61 exhibited localized PSD spikes at the wave pass frequency and its
first harmonic. Test 62 exhibited broadband low frequency noise and with a significantly lower
PSD amplitude at the wave pass frequency and its first harmonic. The elevated PSD response in
Test 61 indicates a better-quality detonation wave relative to Test 62, indicative of less parasitic
deflagration. The visibility of the first harmonic on Test 62 indicates detonative operation but the
elevated low frequency noise may correlate to increased parasitic deflagration and less
performance. The PSD on the left (Test 61) correlates to the higher heat loading mode while the
PSD on the right correlates to the lower heat loading mode (Test 62). With limited data at these
operating conditions, one can only speculate, but this evidence could be indicative of the heat flux
increase experienced during detonative operation when compared to detonative operation with
increased amounts of parasitic deflagration present. The heat flux during detonative operation was
~49% larger when compared to detonative operation with increased amounts of parasitic
deflagration. It is recommended that future testing explore similar operating conditions on HS 1.0
and WC 2.0 hardware to further characterize the two distinct operating conditions.

158

Figure 5.48. Test 62, Outerbody Calorimetry Results from Pulsed Short Duration Testing

159

Figure 5.49. Test 62, Injector Calorimetry Results from Pulsed Short Duration Testing

160

Figure 5.50. Test 61 and Test 62, Power Spectral Density of Radial Accelerometer

Test 63 was completed at the same operating conditions as Test 61 and Test 62. The high
frequency data acquisition failed to activate for this test, providing no data from the accelerometers
or high frequency propellant manifold pressures. The two distinct operating modes were again
present as seen in the outerbody calorimetry results in Figure 5.51. As described for Test 61 and
62, the two distinct operating modes are expected to be one with elevated detonative performance
and the other operating with detonations but increased parasitic deflagration activity. Similar to
Test 61 and Test 62, the two modes are less visible in the injector calorimetry results in Figure
5.52. Using the conclusions drawn from Test 61 and Test 62, the results indicate that the heat
loading environment on the injector face may be less sensitive to the strength of the detonative
wave and may approach the same environment of a deflagrative combustor. These conclusions are
expected to be highly dependent on the injector design and the designer should approach early
designs with conservatism as little data exists on this environment.

161

Figure 5.51. Test 63, Outerbody Calorimetry Results from Pulsed Short Duration Testing

162

Figure 5.52. Test 63, Injector Calorimetry Results from Pulsed Short Duration Testing

163

STRUCTURAL EVALUATION

Along with the thermal challenges presented in previous chapters, RDRCs will also face a
variety of structural challenges. These challenges exist in multiple elements of the launch vehicle
design, to include the system level and the component level. At the system level, vibrations induced
by the passing detonation wave in the RDRE may propagate to local engine components,
secondary structures, or even the payload interface if strong enough in magnitude. It is expected
that the high frequency system level loads generated from the RDRE will attenuate prior to
reaching the payload and may not be a significant contributor to vehicle level loads. At the
combustor level, the passing detonation wave and thermal loading is expected to provide cyclic
loading on the cooling channel design presenting a variety of challenges to include low cycle
fatigue (LCF) and high cycle fatigue (HCF). The focus of this chapter will be to provide a first
order assessment of the combustor design challenges aimed to inform future RDRE designs and
highlight areas for future research.
Before proceeding further into the structural assessment, a brief summary of fatigue failure
will prove informative. HCF occurs when a material undergoes repeating loading cycles at stress
levels below the yield strength of the material. Because the loading event is below the yield
strength, no macro level plastic strain is induced in the material, and it elastically returns to its
original shape and dimensions. HCF failure is primarily driven by the propagation of microscopic
cracks and typically occurs after a large number of cycles (typically greater than 10^5). LCF occurs
when a material undergoes repeating loading cycles at stress levels beyond the yield strength of
the material. Because the loading event is beyond the yield strength, plastic strain is induced in the
material. LCF failure is primarily driven by the accumulation of plastic strain which leads to crack
initiation and then propagation. LCF failure occurs at lower cycle counts (typically less than 10^5).
There have been several prior studies of HCF/LCF in rocket combustors dating back to the
pioneering work of Quentmeyer [13]. This work employed a simple cylindrical cooling jacket with
a shaped center body to provide the area variation in a DeLaval nozzle. More recently, Sung and
Anderson [48] used a similar geometry to evaluate LCF using JP-8 and hydrogen peroxide
propellants with water as coolant. Both of these works focused on conventional constant pressure
combustion as the RDE community is only beginning to work this problem in earnest. Other work
at Purdue (Stopka et al [20]) completed an assessment based on a notional detonative waveform
164

and combustor liner manufactured from Copper 110. Their results indicated that combustor
operating duration would be limited to ~10 sec for an operating pressure of 0.69 MPa. Sung and
Anderson studied common thrust chamber life approaches and compared their low cycle fatigue
predictions [48]. The results ranged from 50 to 220 thermal cycles [48].
The structural evaluation completed in this chapter uses an extensive list of equations and
variables. Table 6.1 identifies each parameter used in the assessment and includes a description.

165

Table 6.1. Structural Evaluation Parameter List and Description
Parameter
E
𝐾′
𝑛′
∆𝜎
𝜎
∆𝜀𝑡𝑜𝑡
∆𝜀𝑝𝑙
∆𝜀𝑒𝑙
𝜀𝑡𝑜𝑡
𝜀𝑝𝑙
𝜀𝑒𝑙
𝜎𝑚𝑜𝑛,𝑇
𝜎𝑚𝑜𝑛,𝐸
𝜀𝑚𝑜𝑛,𝑇
𝜀𝑚𝑜𝑛,𝐸
𝜎𝑓′
2𝑁𝑓
𝑏
𝜀𝑓′
𝑏
𝜎𝑚𝑜𝑛,𝑦
CW
tw
𝜐
𝛼
𝑇ℎ𝑤
𝑇𝑐𝑤
𝑇𝑐𝑎
𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑎𝑥
𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑖𝑛
𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥
𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑖𝑛
∆𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ
𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
∆𝜎𝑒𝑓𝑓,𝑡ℎ
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑒𝑎𝑛
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑎𝑚𝑝
∆𝑃
∆𝑃𝑜𝑝
∆𝑃𝑑𝑒𝑡
𝑃𝑜𝑝
𝑃𝑐𝑜𝑜𝑙
𝑃𝑑𝑒𝑡
𝜎𝑡𝑎,𝑝𝑟
B
𝑁𝑡ℎ
2𝑁𝑓,𝑡ℎ
𝑁𝑓,𝑡ℎ
𝑁𝑝𝑟
2𝑁𝑓,𝑝𝑟
𝑁𝑓,𝑝𝑟
𝜎𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥
𝜎𝑡𝑎,𝑝𝑟,𝑜𝑝
𝜎𝑡𝑎,𝑝𝑟,𝑑𝑒𝑡
𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏
𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑒𝑎𝑛
𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑎𝑚𝑝

Description
Young’s Modulus
Cyclic Strength Coefficient
Cyclic Strain Hardening Exponent
Cyclic Stress Range
Cyclic Stress Amplitude
Cyclic Total Strain Range
Cyclic Plastic Strain Range
Cyclic Elastic Strain Range
Cyclic Total Strain Amplitude
Cyclic Plastic Strain Amplitude
Cyclic Plastic Strain Amplitude
Monotonic True Stress
Monotonic Engineering Stress
Monotonic True Strain
Monotonic Engineering Strain
Fatigue Strength Coefficient
Loading Reversals
Fatigue Strength Exponent
Fatigue Ductility Coefficient
Fatigue Ductility Exponent
Monotonic Yield Stress
Channel Width
Hot Wall Thickness
Poisson’s Ratio
Coefficient of Thermal Expansion
Hot Wall Temperature
Cold Wall Temperature
Bulk Coolant Temperature
Maximum Axial (x-direction) Plastic Strain from Thermal Loading
Minimum Axial (x-direction) Plastic Strain from Thermal Loading
Maximum Tangential (z-direction) Plastic Strain from Thermal Load
Minimum Tangential (z-direction) Plastic Strain from Thermal Load
Tangential (z-direction) Plastic Strain Range from Thermal Loading
Maximum Effective Plastic Strain from Thermal Loading
Maximum Effective Total Strain from Thermal Loading
Minimum Effective Plastic Strain from Thermal Loading
Minimum Effective Total Strain from Thermal Loading
Effective Stress Range from Thermal Loading
Maximum Effective Stress from Thermal Loading
Minimum Effective Stress from Thermal Loading
Effective Total Strain Range from Thermal Loading
Mean Effective Stress from Thermal Loading
Effective Stress Amplitude from Thermal Loading
Difference in Pressure Across the Cooling Channel Hot Wall
Difference in Pressure Across the Cooling Channel Hot Wall when Detonation Wave Passing
Difference in Pressure Across the Cooling Channel Hot Wall when Detonation Wave NOT Passing
Operational Pressure in the Combustion Chamber
Coolant Pressure in the Cooling Channel
Peak Detonation Pressure in the Combustion Chamber
Cyclic Pressure Stress in the Tangential Direction
Block Loadings
Quantity of Thermal Loading Cycles Applied
Quantity of Thermal Loading Reversals that Cause Failure
Quantity of Thermal Loading Cycles that Cause Failure
Quantity of Pressure Loading Cycles Applied
Quantity of Pressure Loading Reversals that Cause Failure
Quantity of Pressure Loading Cycles that Cause Failure
Maximum Tangential (z-direction) Stress from Thermal Loading
Cyclic Pressure Stress in the Tangential (z-direction) Direction when Detonation Wave NOT Passing
Cyclic Pressure Stress in the Tangential (z-direction) Direction when Detonation Wave Passing
Maximum Combined Tangential (z-direction) Stress from Thermal and Cyclic Pressure Loading
Minimum Combined Tangential (z-direction)Stress from Thermal and Cyclic Pressure Loading
Maximum Tangential (z-direction) Plastic Strain from Combined Thermal and Cyclic Pressure Loading
Minimum Tangential (z-direction) Plastic Strain from Combined Thermal and Cyclic Pressure Loading
Maximum Effective Plastic Strain from Combined Thermal and Cyclic Pressure Loading
Minimum Effective Plastic Strain from Combined Thermal and Cyclic Pressure Loading
Maximum Effective Total Strain from Combined Thermal and Cyclic Pressure Loading
Minimum Effective Total Strain from Combined Thermal and Cyclic Pressure Loading
Effective Total Strain Range from Combined Thermal and Cylcic Pressure Loading
Maximum Combined Effective Stress from Combined Thermal and Cyclic Pressure Loading
Minimum Combined Effective Stress from Combined Thermal and Cyclic Pressure Loading
Mean Effective Stress from Combined Thermal and Cyclic Pressure Loading
Effective Stress Amplitude from Combined Thermal and Cyclic Pressure Loading

166

6.1

Material Properties

Traditional rocket combustors face a challenging operational environment that includes
exposure to high temperatures and pressures. The operational environment limits the materials
available for the design and presents manufacturing challenges. Due to the operational and
manufacturing challenges, high strength copper and nickel alloys are often employed. Because of
the high heat flux environment experienced during rocket combustion, regenerative cooling is
typically employed to keep hot wall temperatures within an acceptable level. To dissipate this heat
flux, high strength copper alloys such as GRCop-84 and GRCop-42 were developed specifically
for these rocket applications. High strength nickel alloys are also commonly employed but
typically used in areas of the combustion chamber that do no experience high heat fluxes, such as
manifolds and closeouts.
Figure 6.1 shows monotonic yield strength vs operational temperature for Oxygen Free
High Conductivity Copper (OFHC) and two NASA developed copper alloys (GRCop-84 and
GRCop-42) used in rocket combustors [41]. The first notable feature of the figure is the yield
strength benefits of copper alloys such as GRCop-84 and GRCop-42 when compared to OFHC.
At room temperature, nearly six times the yield strength is offered by extruded GRCop-84. This
highlights a major benefit of high strength copper alloys which result in strength improvements,
reduction in the weight of the rocket combustor, increased design flexibility, and the thermal
conductivities necessary for regenerative cooling. The second notable feature is the reduction in
yield strength for the GRCop-84 and GRCop-42 alloys when operating at rocket like conditions
(~1000 deg F/800 K). The yield strength from room temperature to rocket like conditions decreases
by nearly half. Another notable feature is the variation in yield strength depending on the processes
used to form the materials and their post treatments. An example of how manufacturing approach
and post treatments impact material properties can be seen by GRCop-84 formed by Laser Powder
Bed Fusion (L-PBF) offering a ~25% improvement of yield strength when compared to
traditionally manufactured Hot Isostatic Pressed (HIPed) GRCop-84.

167

Figure 6.1. Yield Strength vs Temperature for High Strength Copper Alloys Commonly Used in
Rocket Combustors [41]
To assess the RDRC localized loading events, the relationship of stress and strain in the
elastic and plastic region is needed. Additionally, the stress vs strain relationship for cyclic loading
is necessary as this is a fatigue assessment and not a monotonic loading assessment. Limited
material properties data exists in the open literature at rocket like temperatures. This data becomes
even more limited when additively manufactured material properties are considered. The WC 1.0
and WC 2.0 combustors used for this research were additively manufactured from L-PBF GRCop84. As shown in Figure 6.2, Minneci et al present detailed monotonic stress vs strain data for
extruded GRCop-84 [41]. The monotonic data provided for L-PBF manufactured materials is at
room temperature though monotonic data is provided at rocket relevant temperatures for extruded
GRCop-84. A notable feature is the monotonic stress vs strain data between extruded GRCop-84
and HIPed L-PBF GRCop-84 is similar at room temperatures. Using this similarity, it was assumed
for this study that HIPed L-PBF GRCop-84 material properties at elevated temperatures were equal

168

to the more readily available extruded GRCop-84 data. Using this assumption, the available cyclic
stress vs strain data for extruded GRCop-84 at elevated temperatures was applied to this study.

Figure 6.2. (Left) Monotonic Stress vs Strain for High Strength Copper Alloys Commonly Used
in Rocket Combustors [41]; (Right) Monotonic Stress vs Strain for Extruded GRCop-84 at Various
Temperatures, Zoomed in to Low Strain Region
Lerch et al. from NASA presented cyclic stress range vs plastic strain range for extruded
GRCop-84 that was used for this study [36]. This data was provided at rocket like temperatures
and is shown in Figure 6.3. The data was obtained for an R-Ratio (ratio of minimum stress to
maximum stress for the applied loading cycles) of -1. The nominal curve fits provided in Figure
6.3 come from reference data for the NASA Reusable Launch Vehicle (RLV) Program [36] and
are not curve fits of the data provided in the plots. The curve fits were provided to show the
similarities of the data points in the plots to the curve fits generated from the NASA RLV Program
[36]. Access to RLV Program data was not available in the open literature. The data points at 673
K (400 deg C) in Figure 6.3 were used to estimate the variability that would be expected on the
nominal curve fit provided by Lerch et al. from the RLV Program data. Using the limited
information on Figure 6.3, the data was binned by plastic strain and then a standard deviation was
calculated for each bin. A multiple of the standard deviation was then added and subtracted to the
mean to create upper and lower bounds that captured the scatter of the data. The multiple used for
the upper bound was 9 and the lower bound was 3. The resultant upper and lower bounds along
169

with the nominal curve fit provided by Lerch et al. is shown in Figure 6.4. Because of the limited
data available data at elevated temperatures in the literature, it is recommended that future studies
work to obtain fatigue data at rocket relevant temperatures, manufacturing techniques, and design
conditions. It is expected that the upper and lower bounds may be conservative but additional data
is required to further assess and alleviate the bounds.

Figure 6.3. Cyclic Stress Range vs Plastic Strain Range for Extruded GRCop-84 at Rocket
Relevant Temperatures; R-Ratio = -1 [36]

170

Figure 6.4. Cyclic Stress Range vs Plastic Strain Range for Extruded GRCop-84 at 673 K;
Generated Using Cyclic Stress vs Strain Data from [36]; R-Ratio = -1; Lerch et al Curve Fit
Represents data From NASA Reusable Launch Vehicle Program and is Considered the Nominal
Material Property for this Study
To understand the relationship of cyclic stress vs strain in the elastic and plastic loading
regime, the Ramberg Osgood relationship was employed:
1

∆𝜀𝑡𝑜𝑡
∆𝜎
∆𝜎 𝑛′
=
+ ( ′)
2
2𝐸
2𝐾

Equation 6-1

where ∆𝜀𝑡𝑜𝑡 is the total cyclic strain range, ∆𝜎 is the cyclic stress range, E is the Young’s Modulus,
𝐾 ′ is the cyclic strength coefficient, and 𝑛′ is the cyclic strain hardening exponent [19]. The first
∆𝜎

half of the Ramberg Osgood relationship (2𝐸 ) represents the materials behavior in the elastic
1
′
∆𝜎
loading regime. The second half of the Ramberg Osgood relationship [(2𝐾′ )𝑛 ] represents the

materials behavior in the plastic loading regime. The data provided in Figure 6.4 is in terms of ∆𝜎

171

∆𝜎

and plastic strain range (∆𝜀𝑝𝑙 ). This data was converted to cyclic stress amplitude ( 2 ) and cyclic
∆𝜀

plastic strain amplitude ( 2𝑝𝑙) and is shown in Figure 6.5.

Figure 6.5. Cyclic Stress Amplitude vs Plastic Strain Amplitude for Extruded GRCop-84 at 673K;
Generated Using Cyclic Stress vs Strain Data from [36]; R-Ratio = -1; Lerch et al Curve Fit
Represents data From NASA Reusable Launch Vehicle Program and is Considered the Nominal
Material Property for this Study
A power law fit was then applied to the cyclic stress amplitude and plastic strain amplitude
data in Figure 6.5 to find the coefficients used in the plastic portion of the Ramberg Osgood
relationship. The resultant coefficients are shown in Equation 6-2 for the nominal fit, Equation 6-3
for the lower bound fit, and Equation 6-4 for the upper bound fit.
′

∆𝜀𝑝𝑙 𝑛
∆𝜀𝑝𝑙 0.1000
∆𝜎
= 𝐾′ (
) = 310.8 (
)
2
2
2

Equation 6-2

172

′

𝑛
∆𝜀𝑝𝑙 0.4148
∆𝜎
′ ∆𝜀𝑝𝑙
=𝐾 (
) = 2991.5 (
)
2
2
2

Equation 6-3

′

𝑛
∆𝜀𝑝𝑙 0.0776
∆𝜎
′ ∆𝜀𝑝𝑙
=𝐾 (
) = 223.7 (
)
2
2
2

Equation 6-4

The Young’s Modulus for GRCop-84 at rocket like operational temperatures was not
available in the available literature. For this study, it was assumed to be equivalent to that of pure
copper. The variation in Young’s Modulus for pure copper with temperature was provided by
Ledbetter et al. and shown in Figure 6.6 [5]. Data from Figure 6.6 was plotted and a linear curve
fit was applied. The resulting equation is shown in Equation 6-5
𝐸 = −42.895 (𝑇) + 137869

Equation 6-5

where E is Young’s modulus in MPa and T is temperature in K. It should be noted that the scatter
in the data in Figure 6.6 was considered to have little impact on the study results so upper and
lower bounds were not applied. Material property data at 673 K was used for this study as many
of the hot fires in Test Campaign 1.0 and 2.0 resulted in hot wall temperatures near this value. At
673 K, the Young’s Modulus varied from 85,000 MPa to 115,000 MPa. Thermal stresses drive the
hot wall into the plastic loading regime. The variation in Young’s Modulus impacts the elastic
loading portion of the Ramberg Osgood relationship. Using the Ramberg Osgood relationship
nominal fit values along with stresses expected in the hot wall, less than 5% variability is expected
in the resultant strain from Young’s Modulus variability. This was considered negligible for this
assessment.

173

Figure 6.6. Young’s Modulus vs Temperature for Pure Copper at Rocket Relevant Temperatures
[5]
The coefficients for the Ramberg Osgood correlation at 673 K can be found in Table 6.2
where the Young’s Modulus was found from Equation 6-5. A plot of cyclic stress amplitude vs
strain amplitude using the Ramberg Osgood correlations can be found in Figure 6.7 for the nominal
fit, upper bound, and lower bound. Included in Figure 6.7 is the cyclic stress vs total strain data
points from Figure 6.4 [41]. To include these data points, they were first converted to cyclic stress
amplitude vs plastic strain amplitude and then the elastic strain contribution was added to the
𝜎

provided plastic data. This was completed by adding 𝐸 to the cyclic plastic strain amplitude data,
resulting in cyclic total plastic amplitude. Also included in Figure 6.7 are the monotonic stress vs
total strain data points from Figure 6.2 [36]. The monotonic data was converted from engineering
stress vs strain to true stress vs strain using
𝜎𝑚𝑜𝑛,𝑇 = 𝜎𝑚𝑜𝑛,𝐸 (1 + 𝜀𝑚𝑜𝑛,𝐸 )

Equation 6-6

174

𝜀𝑚𝑜𝑛,𝑇 = 𝑙𝑛(1 + 𝜀𝑚𝑜𝑛,𝐸 )

Equation 6-7

where 𝜎𝑚𝑜𝑛,𝑇 is the monotonic true stress, 𝜎𝑚𝑜𝑛,𝐸 is the monotonic engineering stress, 𝜀𝑚𝑜𝑛,𝑇 is
monotonic true strain, and 𝜀𝑚𝑜𝑛,𝐸 is monotonic engineering strain. It should be noted that the
nominal cyclic stress vs total strain Ramberg Osgood relationship matched closely to the
monotonic stress vs total strain data. Future studies may find this relationship useful if only
monotonic stress vs strain data is available for use.

Table 6.2. Cycle Stress Strain Data Constants Derived for Ramberg Osgood Fit, Extruded GRCop84 at 673 K; R-Ratio = -1
Approach

Temperature
(K)

Elastic
Modulus (E)
[MPa]

Cyclic Strength
Coefficient (K’)
[MPa]

Cyclic Strain
Hardening
Exponent (n’)

Nominal Fit

673

109,000

310.8

0.1000

Upper Bound

673

109,000

2991.5

0.4148

Lower Bound

673

109,000

223.7

0.0776

Figure 6.7. Cyclic Stress Amplitude vs Total Strain Amplitude at 673 K Using the Ramberg
Osgood Coefficients in Table 6.2; Cyclic Stress vs Total Strain Data from Reference [36];
Monotonic Stress vs Total Strain Data from Reference [41]
175

Lerch et al. from NASA also presented total strain life data for extruded GRCop-84 that
was used for this study [36]. This data was provided at rocket like temperatures and is shown in
Figure 6.8. This data was also provided at the 673 K temperature used to derive the Ramberg
Osgood correlations above. The data was obtained for an R-Ratio (ratio of minimum stress to
maximum stress in the applied loading cycles) of -1. The nominal curve fits provided in Figure 6.3
come from reference data for the NASA Reusable Launch Vehicle (RLV) Program [36] and are
not curve fits of the data provided in the plots. The curve fits were provided to show the similarities
of the data points in the plots to the curve fits generated from the NASA RLV Program [36].
Access to RLV Program data was not found to be available in the open literature. The data points
at 673 K (400 deg C) in Figure 6.8 were used to determine a nominal power law fit of the total
strain life as shown Figure 6.9. A discussion on variability and data scatter on the strain life curve
will be provided below.

Figure 6.8. Total Strain Life Data for Extruded GRCop-84 at Rocket Relevant Temperatures; RRatio = -1 [36]

176

Figure 6.9. Total Strain Life for Extruded GRCop-84 at 673 K; Generated Using Total Strain Life
Data from [36]; R-Ratio = -1
The total strain in Figure 6.9 has elastic and plastic contributions. The strain life
relationship in the elastic regime can be described by the Basquin relationship
𝜎𝑓′
∆𝜀𝑒𝑙
=
(2𝑁𝑓 )𝑏
2
𝐸

Equation 6-8

where ∆𝜀𝑒𝑙 is the cyclic elastic strain range, 𝜎𝑓′ fatigue strength coefficient, 2𝑁𝑓 is the amount of
loading reversals (2 reversals = 1 cycle), and 𝑏 is the fatigue strength exponent [19]. The strain life
relationship in the plastic regime can be described by the Coffin Manson relationship
∆𝜀𝑝𝑙
𝑐
= 𝜀𝑓′ (2𝑁𝑓 )
2

Equation 6-9

177

where ∆𝜀𝑒𝑙 is the cyclic plastic strain range, 𝜀𝑓′ is the fatigue ductility coefficient, and 𝑐 is the
fatigue ductility exponent [19]. When combined, these equations form the Basquin Coffin Manson
relationship below for total strain life [19].
𝜎𝑓′
∆𝜀𝑡𝑜𝑡
𝑐
=
(2𝑁𝑓 )𝑏 + 𝜀𝑓′ (2𝑁𝑓 )
2
𝐸

Equation 6-10

Using the data provided in Figure 6.9 and the nominal Ramberg Osgood relationship, the
total strain could be broken into its elastic and plastic components as shown in Figure 6.10. It
should be noted that the power law fit determined in Figure 6.9 was used beyond the range of data
points it was derived for to generate the results in Figure 6.10. The elastic and plastic components
can then be curve fit to determine the Basquin Coffin Manson coefficients provided in Table 6.3.
The Basquin Coffin Manson coefficients in Table 6.3 are used in Equation 6-10 to produce the
total strain curve fit provided in Figure 6.11. As shown in Figure 6.11, the Basquin Coffin Manson
relationship provides a good prediction of strain life in both the elastic and plastic regimes. The
upper and lower bounds represent a variability of +/-68.27% and capture the scatter of the total
strain life data points from Lerch et al. [36]. It should be noted that the Ramberg Osgood and
Basquin Coffin Manson relationships developed for this study were for a material temperature of
673 K. In the study below, some assessments are made at temperatures other than 673 K. In those
cases, the relationships developed for 673 K were used.

178

Figure 6.10. Basquin Coffin Manson Relationship for Extruded GRCop-84 at 673 K; Generated
Using Strain Life Data from [36]; R-Ratio = -1

Table 6.3. Basquin Coffin Manson Coefficients for Extruded GRCop-84 at 673 K; R-Ratio = -1
Temperat
Approach
ure (K)
Nominal
Fit

673

Fatigue
Strength
Coefficient
(𝝈′𝒇 ) [𝑴𝑷𝒂]

Fatigue
Strength
Exponent (b)

Fatigue
Ductility
Coefficient
(𝜺′𝒇 )

Fatigue
Ductility
Exponent (c)

250.7

-0.043

0.1258

-0.439

179

Figure 6.11. Total Strain Life Using Basquin Coffin Manson Coefficients in Table 6.3 for Extruded
GRCop-84 at 673 K; Total Strain Life Data Points from Reference [36]; R-Ratio = -1; Upper and
Lower Bounds Represent +/- 68.27%
The monotonic yield strength data from Figure 6.1 was plotted for a range of rocket like
temperatures and a linear curve fit applied. The resulting equation is listed in Equation 6-11
𝜎𝑚𝑜𝑛,𝑦 = −0.195 (𝑇) + 285.5

Equation 6-11

where the material temperature (T) is in Kelvin and the material yield strength (𝜎𝑚𝑜𝑛,𝑦 ) is in MPa.
The coefficient of thermal expansion used for this assessment was 0.000019 (1/K) and the Poisson
ratio was 0.33 [45]. These values were assumed to remain constant with temperature for this study.

180

6.2

Problem Description

The structural loading events in an RDRC are driven by the detonation event and thermal
loading. Figure 6.12 provides an overview of a cooling channel design and a summary of the
loading environment the hot wall experiences when the combustor is operating. The cooling
channel design used for the following fatigue assessments are listed in Table 6.4. The focal point
of this assessment is the hot wall. The hot wall provides the mechanical strength to contain the
chamber pressure and provides a conductive path to dissipate heat into the coolant to maintain an
acceptable operating temperature. As shown in Figure 6.12, the detonation wave can be seen
passing from left to right. Each pass of the detonation wave results in a localized increase in
pressure in the combustion chamber. Prior to the hot fire event, the hot wall is at ambient
temperatures. Shortly after combustor ignition, large heat fluxes cause temperatures in the hot wall
to approach and often exceed 1000 deg F.

Figure 6.12. Structural Arrangement and Loading Summary

Table 6.4. Cooling System Design Used for the Fatigue Assessments
Channel Width (CW)

Hot Wall Thickness (tw)

0.0762 cm (0.030 in.)

0.1016 cm (0.040 in.)

181

Figure 6.13 offers a simplified not-to-scale summary of the stresses experienced in the hot
wall during a hot fire event for an RDRC. During the start transient, the hot wall heats up and
experiences large thermal stresses. Thermal gradients between the hot wall, cold wall, cooling
channel ribs and closeout wall contribute to this stress. While the start and shutdown transients are
represented by linear changes in stress, there would presumably be some oscillations in stress due
to growing/shrinking amplitudes of the detonation fronts during these periods. For a copper alloy
chamber with a hot wall operating at 1000 deg F / 800 K, the cold wall will be ~200-300 deg cooler
while the closeout wall is even cooler. At elevated temperatures, the hot wall attempts to expand
but is constrained in place by the lower temperature cooling channel ribs and hoop strength of the
combustor. For typical operating conditions in a traditional rocket combustor, these thermal
stresses exceed the yield strength of the material and induce plastic strains into the hot wall.
Repeated starts and shutdowns continue to plastically deform the hot wall and eventually the wall
cracks and fails due to low cycle fatigue (LCF). This thermal loading LCF event is the life limiting
feature for traditional rocket combustor design and an important consideration in modern rocket
engine design as re-use is increasingly important.

Figure 6.13. Hot Wall Stress from Loading Conditions Present in Rotating Detonation Engine
182

As shown in Figure 6.13, during steady state operation the hot wall experiences fluctuating
stresses driven by pressure pulsations from the passing detonation wave. Note, the figure
drastically underrepresents the true number of pressure pulsation cycles placed on a combustor
during operation. The frequency of pressure pulsations applied at any given point in the
combustion chamber hot wall from the passing detonation wave is on the order of 10’s of kHz for
rocket like RDRCs. A common operational time for the first stage of a launch vehicle is on the
order of 2 to 3 minutes. For an RDRC, this would result in excess of 1 million pressure pulsation
cycles being placed on the hot wall at any given location in the proximity of the passing detonation
wave. The resultant cyclic loading from the pressure pulses is hypothesized to be a new high cycle
fatigue failure mechanism and is evaluated further in this study.
As highlighted in Figure 6.13, each RDRC hot fire event undergoes a spectrum of load
histories driven by thermal and mechanical stresses. Assuming the combustor operates at a steady
state power level, each hot fire event results in one thermal stress cycle on the hot wall. While
operating at steady state, the combustor also experiences a large quantity of pressure loading events
from the passing detonation wave. The amplitude of the pressure fluctuations are expected to vary
with time but for the purpose of this study they are considered constant. It should also be noted
that the spectrum of load histories have a mean stress and are not fully reversed. A fully reversed
load is when the stress alternates between tension and compression, fully reversing each cycle. A
detailed fatigue assessment of the hot wall requires the spectrum of loading events to be analyzed
using a linear damage approach. Two fatigue assessments are presented below. The first
assessment evaluates the low cycle fatigue life impacts for rotating detonation engines due to the
larger thermal loading. The second assessment evaluates the life impact from the cyclic loading
present from the passing detonation wave. The second assessment takes into consideration the low
cycle fatigue thermal environment and the high cycle fatigue cyclic pressure environment.

6.3

Low Cycle Fatigue Assessment

From the experimental data collected during Test Campaign 1.0 and 2.0, it is evident that
RDRC’s experience larger thermal loads when compared to traditional rocket combustors at
comparable operating pressures. This LCF assessment solely evaluates the impact from the
increased thermal load and disregards the cyclic pressure stresses as shown in Figure 6.14. LCF
induced by thermal stresses is known to be a common failure mechanism in traditional rocket
183

combustors, indicating that RDRCs will likely have reduced LCF lives. The thermal stresses are
expected to induce plastic strain in the hot wall. Kuyper et al. [42] (from Rocketdyne) offer a
simplified approximate solution to calculate the plastic strain in rocket combustors using Equation
6-12 through Equation 6-14 below

𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑎𝑥 = 𝛼

𝜎𝑚𝑜𝑛,𝑦
(𝑇ℎ𝑤 − 𝑇𝑐𝑤)
(𝑇ℎ𝑤 + 𝑇𝑐𝑤)
+𝛼(
− 𝑇𝑐𝑎) −
2(1 − 𝜐)
2
𝐸

Equation 6-12

𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 = 𝛼

(𝑇ℎ𝑤 − 𝑇𝑐𝑤) 𝜎𝑚𝑜𝑛,𝑦
−
2(1 − 𝜐)
𝐸

Equation 6-13

2

2
(𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥
+ 𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑎𝑥
1/2
3
2
+ 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑎𝑥
)1/2

𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 =

Equation 6-14

where 𝑇ℎ𝑤 is the hot wall temperature, 𝑇𝑐𝑤 is the cold wall temperature, 𝜐 is Poisson’s Ratio, 𝛼
is the coefficient of thermal expansion, 𝑇𝑐𝑎 is the bulk coolant temperature, 𝜎𝑦 is the yield stress
of the material, 𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 is the maximum plastic strain in the tangential direction from thermal
stresses, 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑎𝑥 is the maximum plastic strain in the axial direction from thermal stresses,
and 𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 is the maximum effective plastic strain from thermal stresses. The major
assumptions for Equation 6-12 through Equation 6-14 can be found in Table 6.5. The maximum
strains occur when the combustor is operating and experiencing a thermal load from the
combustion event. Kuyper et al. highlight that thermal loading drives hot wall strains into the
plastic regime at temperatures as low as ~200 deg F which is well below rocket like temperatures
[42]. The minimum strains are zero and occur when the combustor is not operating, and no thermal
load is present as shown in Equation 6-15 through Equation 6-17.
𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ,𝑚𝑖𝑛 = 0

Equation 6-15

𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑖𝑛 = 0

Equation 6-16

𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 = 0

Equation 6-17

184

Table 6.5. Equation 6-12 - Equation 6-14 Assumptions
Assumption

Elastic Theory

Isotropic
Material
Properties

Justification
A major assumption of this model is that it uses elastic theory to compute total
strains. Kuyper et al. acknowledge that the strains will be partly plastic [42]. The
model determines the shape the hot wall would assume if unconstrained, and then
calculates the strains produced by forcing it to its constrained shape and
dimensions.
The material for this assessment was assumed to have the same mechanical
properties in all directions

Figure 6.14. Hot Wall Loading Condition Assumptions Used for the Low Cycle Fatigue
Assessment
The objective of this LCF assessment is to complete a hot fire cycle life comparison
between RDEs and traditional rocket engines. This assessment is closely linked to heat flux as that
is the driving mechanism for the hot wall temperatures and thermal gradients experienced during
operation. The hot fire testing completed for this study provided insight into the larger heat fluxes
that will be experienced by RDEs when compared to traditional rocket combustors operating at
the same conditions. The heat flux data was collected at relatively low power settings and
summarized in Figure 5.20. Future studies are recommended to evaluate heat flux trendlines
between RDEs and traditional rocket combustors at higher power levels. Only power levels tested

185

during this research were used to complete the LCF assessment as insight into heat flux was
available.
Using Equation 6-12 through Equation 6-14, the Kuyper et al. methodology was
implemented for several conditions that were operated during Test Campaign 2.0 [42]. The tests
represent a range of chamber pressures and include the following: Test 54 at 1.48 MPa (215 psia)
chamber pressure, Test 53 at 1.02 MPa (148 psia) chamber pressure, Test 57 at 0.72 MPa (105
psia) chamber pressure, and Test 45 at 0.53 MPa (77 psia) chamber pressure. The hot wall
temperatures and cold wall temperatures for these operational cases can be found in Table 6.6 for
RDE operation and traditional rocket combustor operation. The values for RDE’s were determined
from Test Campaign 2.0 calorimetry data and the values for traditional rocket combustors were
predicted using the methodologies outlined in Section 3.

Table 6.6. Operating Conditions Used for LCF Assessment
Configuration

Chamber
Pressure [MPa]

Hot Wall Temperature
(Thw) [K]

Cold Wall
Temperature (Tcw)
[K]

RDE

1.48

826

698

RDE

1.02

768

656

RDE

0.72

656

571

RDE

0.53

533

478

1.48

693

600

1.02

611

537

0.72

525

472

0.53

488

433

Traditional Rocket
Engine
Traditional Rocket
Engine
Traditional Rocket
Engine
Traditional Rocket
Engine

Kuyper et al. [42] reference work from Mendelson et al. [15] as an approach to determine
the total effective plastic stress from thermal loading

𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 =

2(1 + 𝑣) 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
+ 𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
3
𝐸

186

Equation 6-18

𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 =

2(1 + 𝑣) 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
+ 𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 = 0
3
𝐸

Equation 6-19

where 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 is the maximum effective stress and 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 is the minimum effective stress.
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 and 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 can be found through the relationships below in Equation 6-20 and
Equation 6-21. The minimum total effective plastic strain and minimum effective stress from
thermal loading are zero as the calculations are considered when the combustor is not operating.
The following relationships equate stress to a perfectly plastic response. The stresses determined
using these relationships are used to calculate the effective total strains which are then used to
determine the effective elastic strains. This is completed by subtracting the effective plastic strains
from the effective total strains. This methodology violates the assumption of a perfectly plastic
response, and the results should be treated as an approximation.

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 = 𝐾 ′ (𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 )
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 = 𝐾 ′ (𝜀𝑝𝑙,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 )

𝑛′

𝑛′

Equation 6-20

Equation 6-21

=0

Using the methodology outlined above and the nominal Ramberg Osgood material
properties from Section 0, the effective strains in the hot wall from thermal loading were calculated
and can be seen in Figure 6.15. Figure 6.16 zooms in on the effective elastic strain for reference.
As shown in Figure 6.15 and Figure 6.16 the effective strains are larger for RDRE’s due to the
larger thermal environments they experience when compared to traditional rocket combustors. The
effective strains increase with chamber pressure as the thermal load increases. As shown in Figure
6.15, effective plastic strain is the dominant contributor to the total effective strain. At lower power
levels, plastic strain accounted for ~70% of the total strain. As power levels increased, hot wall
temperatures also increased, resulting in larger thermal stresses and corresponding larger plastic
strains. At higher power levels, plastic strain accounted for ~90% of the total strain. As Kuyper et
al. highlight, to keep the thermal stresses below the yield stress, hot wall temperatures need to
operate at ~ < 200 deg F / 266 K for common combustor materials [42]. This is an unrealistic
operating condition for most rocket combustors and highlights that low cycle fatigue should always

187

be considered in the cooling channel design process, especially for combustors that will experience
large quantities of thermal cycles and operate at high chamber pressures.

Figure 6.15. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Nominal Ramberg Osgood Material Properties from Table 6.2

Figure 6.16. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Nominal Ramberg Osgood Material Properties from Table 6.2

188

The analysis was repeated using the methodology outlined above but substituting the upper
and lower bound Ramberg Osgood material properties from Section 0. The effective strains in the
hot wall from thermal loading can be seen in Figure 6.17 and Figure 6.18 for the lower bound
Ramberg Osgood material properties. The effective strains in the hot wall from thermal loading
can be seen in Figure 6.19 and Figure 6.20 for the upper bound Ramberg Osgood material
properties.

Figure 6.17. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Upper Bound Ramberg Osgood Material Properties from Table 6.2

189

Figure 6.18. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Upper Bound Ramberg Osgood Material Properties from Table 6.2

Figure 6.19. Effective Total, Plastic, and Elastic Strain Comparison Between Rotating Detonation
Engines and Traditional Rocket Engines for Operating Conditions Tested During Test Campaign
2.0; Calculated Using Lower Bound Ramberg Osgood Material Properties from Table 6.2
190

Figure 6.20. Effective Elastic Strain Comparison Between Rotating Detonation Engines and
Traditional Rocket Engines for Operating Conditions Tested During Test Campaign 2.0;
Calculated Using Lower Bound Ramberg Osgood Material Properties from Table 6.2
As the thermal cycle is not fully reversed, a mean stress approach is required to determine
combustor LCF life. The Smith Watson Topper mean stress approach was used as outlined by
Equation 6-22 through Equation 6-26 below
(𝜎𝑓′ )2
∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥
=
(2𝑁𝑓,𝑡ℎ )2𝑏 + 𝜎𝑓′ 𝜀𝑓′ (2𝑁𝑓,𝑡ℎ )𝑏+𝑐
2
𝐸

Equation 6-22

∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ = 𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 − 𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛

Equation 6-23

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 = 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑒𝑎𝑛 + 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑎𝑚𝑝

Equation 6-24

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑒𝑎𝑛 =

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 + 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
2

Equation 6-25

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑎𝑚𝑝 =

𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 − 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛
2

Equation 6-26

191

where 𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑎𝑥 is the maximum thermal effective stress calculated using Equation 6-20 and
𝜎𝑒𝑓𝑓,𝑡ℎ,𝑚𝑖𝑛 is the minimum thermal effective stress calculated using Equation 6-21 [19]. The Smith
Watson Topper approach works well over a wide range of materials and is good for general use
[19]. The results from the Smith Watson Topper approach can be seen in Table 6.7 through Table
6.12.
Table 6.7 and Table 6.8 represent results using nominal Ramberg Osgood and nominal
Basquin Coffin Manson material properties. Table 6.9 and Table 6.10 represent results using upper
bound Ramberg Osgood and nominal Basquin Coffin Manson material properties. Table 6.11 and
Table 6.12 represent results using lower bound Ramberg Osgood and nominal Basquin Coffin
Manson material properties. The results are provided for RDE operation and traditional rocket
combustor operation for comparison.
A summary of the available start/shutdown cycle life between an RDE and traditional
rocket combustor at similar operating conditions can be found in Figure 6.21 through Figure 6.23
below. Figure 6.21 represents the results using nominal Ramberg Osgood and nominal/upper
bound/lower bound Basquin Coffin Manson material properties. Figure 6.22 represents the results
using upper bound Ramberg Osgood and nominal/upper bound/lower bound Basquin Coffin
Manson material properties. Figure 6.23 represents the results using lower bound Ramberg Osgood
and nominal/upper bound/lower bound Basquin Coffin Manson material properties.
As the trends suggest in the effective strain data, the life results indicate that lower hot fire
cycles can be completed by RDEs due to the larger heat loadings they experience when compared
to traditional rocket combustors. The predicted reduction in life varies between ~30% to ~90%
between RDE’s and traditional rocket combustors depending on the operating condition. As
highlighted in Chapter 5, more experimental RDRC thermal loading data is needed at higher
pressures to evaluate trends but the results from Figure 6.21 through Figure 6.23 indicate that
start/shutdown cycles will be limited at high chamber pressures. Included on each figure is the
average operating condition of the WC 2.0 hardware and the start/shutdown cycles it achieved. In
all nominal material property cases, the achieved start/shutdown cycle life was lower than the
predicted not to exceed value, indicating that additional life was available on the combustor. For
lower bound Basquin Coffin Manson material properties, the achieved start/shutdown cycle life
exceed the predicted not to exceed value. Post test inspections found no issues or cracks in the

192

combustion chamber hot wall, indicating the lower bound Basquin Coffin Manson material
properties may be conservative.
In practice the combustor designer will have a maximum wall temperature that can be
sustained as a design metric. This maximum wall temperature will be the same whether a
traditional rocket combustor or RDE is being designed. To achieve the desired wall temperature,
the primary design variable the designer must manage will be coolant flowrate, with larger
flowrates improving cooling. At the system level, the larger coolant flowrates will come with
larger pressure drops. In a regenerative cooling design, the propellant used to cool the thrust
chamber is also fed through the injector and ignited in the combustion chamber. Larger coolant
pressure drops directly impacts the performance of the rocket engine if the problem cannot be
managed upstream by turbopump pressure production or increased pressure capacity in the
propellant tank and feed system. As rocket tanks/feed systems and rocket engine designs already
operate at the limitations of high strength materials, this conclusion will ultimately drive increased
weight into the system unless unconventional cooling techniques can be successfully employed.

Table 6.7. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Nominal Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(mm/mm)

𝟐𝑵𝒇, 𝒕𝒉
(Reversa
ls)

𝑵𝒇, 𝒕𝒉
(Cycle
s)

1.48

198

0

99.0

99.0

0

0.02504

250

125

1.02

195

0

97.5

97.5

0

0.02193

350

175

0.72

188

0

94.0

94.0

0

0.01610

875

438

0.53

175

0

87.5

87.5

0

0.00988

4200

2100

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

193

Table 6.8. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Nominal Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(mm/mm)

𝟐𝑵𝒇, 𝒕𝒉
(Reversa
ls)

𝑵𝒇, 𝒕𝒉
(Cycle
s)

1.48

190

0

95.0

95.0

0

0.01799

630

315

1.02

184

0

92.0

92.0

0

0.01378

1400

700

0.72

174

0

87.0

87.0

0

0.00949

4900

2450

0.53

169

0

84.5

84.5

0

0.00795

10000

5000

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

Figure 6.21. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Nominal
Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin Coffin
Manson Material Properties

194

Table 6.9. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Upper Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties
𝟐𝑵𝒇, 𝒕𝒉
∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(Revers
(mm/mm)
als)

Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

1.48

451

0

225.5

225.5

0

0.02433

32

16

1.02

420

0

210.0

210.0

0

0.02121

52

26

0.72

352

0

176.0

176.0

0

0.01541

170

85

0.53

256

0

128.0

128.0

0

0.00960

1600

800

𝑵𝒇, 𝒕𝒉
(Cycles)

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

Table 6.10. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Upper Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(mm/mm)

𝟐𝑵𝒇, 𝒕𝒉
(Revers
als)

𝑵𝒇, 𝒕𝒉
(Cycles)

1.48

376

0

188.0

188.0

0

0.01728

110

55

1.02

319

0

159.5

159.5

0

0.01316

325

163

0.72

249

0

124.5

124.5

0

0.00929

1900

950

0.53

220

0

110.0

110.0

0

0.00810

5000

2500

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

195

Figure 6.22. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Upper
Bound Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin
Coffin Manson Material Properties
Table 6.11. Smith Watson Topper Life Results for Rotating Detonation Combustor Operational
Cases; Lower Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson
Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙 𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)**
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎 𝟐𝑵𝒇, 𝒕𝒉
(Reversals)
(mm/mm)

𝑵𝒇, 𝒕𝒉
(Cycles
)

1.48

159

0

79.37

79.37

0

0.02570

390

195

1.02

157

0

78.51

78.51

0

0.02261

550

275

0.72

153

0

76.48

76.48

0

0.01680

1250

625

0.53

146

0

73.16

73.16

0

0.01048

5200

2600

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

196

Table 6.12. Smith Watson Topper Life Results for Traditional Combustor Operational Cases;
Lower Bound Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(mm/mm)

𝟐𝑵𝒇, 𝒕𝒉
(Reversals
)

𝑵𝒇, 𝒕𝒉
(Cycles
)

1.48

154

0

77.21

77.21

0

0.01869

940

470

1.02

151

0

75.45

75.45

0

0.01448

1900

950

0.72

146

0

72.87

72.87

0

0.01007

6000

3000

0.53

143

0

71.58

71.58

0

0.00847

10500

5250

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)

Figure 6.23. Start/Shutdown Cycle Life Comparison Between Rotating Detonation Engine and
Traditional Rocket Engine for Operating Conditions Tested During Test Campaign 2.0; Lower
Bound Ramberg Osgood Material Properties; Nominal/Upper Bound/Lower Bound Basquin
Coffin Manson Material Properties

197

6.4

Combined Low Cycle and High Cycle Fatigue Assessment

The prior LCF assessment only takes into consideration the thermal loads to life the
combustion chamber. The cyclic pressure stresses from the passing detonation wave are also
expected to degrade the combustor life and introduce a potentially new HCF failure mechanism.
This combined LCF and HCF assessment takes into consideration the cyclic pressure stresses
identified in Figure 6.13. This assessment requires knowledge of the pressure differential across
the cooling channel. This pressure differential is driven by the coolant pressure, the operating
chamber pressure, and the peak pressure from the passing detonation wave. Assuming the
combustor is regeneratively cooled and bi-propellant, one of the propellants is used as the coolant.
The coolant is typically the fuel rather than oxidizer but in some cases oxidizer is used. Regardless
of propellant choice as the coolant, the propellant is flowed through the cooling passage upstream
of being injected into the chamber for combustion.
The pressure drop of the coolant from the supply to the combustion chamber depends
heavily on the friction losses of the propellant traveling through the cooling channel and the
injector stiffness. For this assessment, coolant supply pressure was assumed to be double the
chamber pressure. This assumption aligns with common rocket engine pressure conditions and is
representative of the pressure drop that would be experienced from the cooling system to the
combustion chamber for a propellant. It should be noted that this assumption is highly specific to
the location within the cooling system in the combustion chamber as pressure drop causes this
value to continuously decrease towards the injector face.
The detailed characteristics of the pressure pulsation are beyond the scope of this study and
depend on the combustor, injector design, operating conditions, and propellant combination.
Research to date has offered limited insight into its true peaks, cycle to cycle variations, and decay
times. For an ideal detonation of rocket propellants (perfectly mixed propellants filling a
tube/channel), the maximum pressure associated with the detonation wave is an order of magnitude
larger than the average pressure in the chamber. This ideal scenario is believed to over dramatize
the loading event on the combustion chamber hot wall as propellants in an RDRC are not perfectly
mixed and significant attenuation is expected from the strongest detonation pressure occurring
some distance from the wall.
The results from an LES study indicate that the maximum pressure near the hot wall from
the passing detonation wave was ~8 times larger than the combustor operating pressure. This peak

198

pressure ratio was used to model the structural environment for this study. Recent RDRC
performance modeling informed by experimental stagnation pressure measurements indicate this
assumption is likely conservative and the results will vary with operating pressure [47].
Additionally, detonation pressure ratio is expected to decrease as operating pressure increases [47].
The RDE community is realizing that actual RDRE’s don’t approach the theoretical pressure ratios
because only a fraction of the total heat release supports the detonation. Parasitic deflagration
becomes more prominent at higher operating pressures and the detonation pressure ratio degrades
accordingly. It should be noted that this is a major assumption that will vary significantly with the
design and propellant combination.
Using the cooling system pressure assumptions and the assumed detonation pressure ratio
of 8, the pressure loading environment experienced by the hot wall can be formulated as shown in
Figure 6.24. Using this assumption, as operational chamber pressure increases, the peak detonation
pressure experienced in the combustion chamber will increase more rapidly than the cooling
system pressure required to feed propellant into the combustion chamber. This trend highlights
that stresses from peak detonation pressure will become more severe as the operational chamber
pressure of the combustor increases. Though this is assumed for this assessment, it should be noted
that current research indicates that detonation pressure ratios may not increase with operational
pressure [47]. Further research in this area is recommended to validate the structural concerns
presented in this study.

199

Figure 6.24. Pressure Loads Experienced by Hot Wall; Assumed Coolant Pressure to be 2x the
Average Chamber Pressure; Assumed Peak Detonation Pressure to be 8x the Average Chamber
Pressure
The stresses induced by the passing detonation wave can be approximated by treating the
hot wall like a beam
1
𝐶𝑊 2
𝜎𝑡𝑎,𝑝𝑟 = ∆𝑃
2
𝑡𝑤 2

Equation 6-27

where 𝜎𝑡𝑎,𝑝𝑟 is the cyclic pressure stress in the tangential direction, CW is the channel width, and
tw is the hot wall thickness. ∆𝑃 is the difference between the coolant pressure and the
instantaneous chamber pressure [45,49]. Jorgensen et al. highlight that Equation 6-27 agrees well
with two-dimensional finite element simulations when CW and tw are smaller than 1 mm [45].
When CW and tw are larger than 1 mm, Equation 6-27 provides conservative results [45]. The
assumptions and justifications for the use of Equation 6-27 are provided in Table 6.13. It should
be noted that the assumptions result in stresses only applied in the tangential direction.

200

Table 6.13. Equation 6-27 Assumptions
Assumption

Justification

Elastic Material
Loading

When thermal stresses are not considered, the material is expected to remain in the
elastic region for combustors with standard cooling geometry (high aspect ratio
cooling channels). When thermal stresses are considered, the elastic assumption is
violated and the results should be used with caution. Future studies should used
more advanced analysis techniques such as FEA.

Rigid Supports

This equation assumes the hot wall is rigidly supported on each end. Cooling
channels ribs provide this support. The cooling channel ribs are thicker than the
hot wall and supported by a thick cooling channel closeout. The ribs and cooling
channel closeout also do not experience the elevated temperatures seen by the hot
wall because they are well cooled. The ribs were assumed to be rigid for this
assessment.

Uniform Pressure
Distribution

Pressure is assumed to be uniformly distributed across the hot wall for this
assessment. In actual operation, the detonation wave will be passing over the hot
wall and the resultant dynamic pressure distribution will not be uniform.

No Axial or
Torsion Loads

Axial loads are expected to be reacted by the much thicker cooling channel
closeout wall and were considered negligible for this assessment. There is no
moment expected to be applied to the combustor and therefore, torsional loads are
expected to be negligible.

Homogenous
Material

The material for this assessment was considered to be homogeneous with
consistent mechanical properties

The ∆𝑃 term in Equation 6-27 is cyclic during RDRC operation. The cooling channel is
pressurized with coolant, applying a nearly constant pressure load to the cold wall. The stress
generated from the coolant pressure is additive to the thermal stresses generated in the hot wall.
The average chamber pressure results in a nearly constant pressure load, counteracting the pressure
load applied by the coolant. The tangential stress generated in the hot wall from this loading
environment can be found by
∆𝑃𝑜𝑝 = 𝑃𝑜𝑝 − 𝑃𝑐𝑜𝑜𝑙

𝜎𝑡𝑎,𝑝𝑟,𝑜𝑝 =

Equation 6-28

1
𝐶𝑊 2
∆𝑃𝑜𝑝
2
𝑡𝑤 2

Equation 6-29

201

where 𝑃𝑜𝑝 is the operational pressure in the combustion chamber and 𝑃𝑐𝑜𝑜𝑙 is the coolant pressure
in the cooling channel. The passing detonation wave causes a cyclic pressure pulsation, also
counteracting the pressure load applied by the coolant. The tangential stress generated in the hot
wall when the peak pressure from the detonation wave is applied to the cooling channel of interest
can be found by
∆𝑃𝑑𝑒𝑡 = 𝑃𝑑𝑒𝑡 − 𝑃𝑐𝑜𝑜𝑙

Equation 6-30

1
𝐶𝑊 2
𝜎𝑡𝑎,𝑝𝑟,𝑑𝑒𝑡 = ∆𝑃𝑑𝑒𝑡
2
𝑡𝑤 2

Equation 6-31

where 𝑃𝑑𝑒𝑡 is the peak detonation pressure. Equation 6-29 and Equation 6-31 were used to
calculate the tangential stresses in the hot wall for a variety of operating conditions and cooling
channel widths. The operating conditions represent a range of operational chamber pressures
varying from an RL10 class combustor (~3.10 MPa operational chamber pressure) to an SSME
class combustor (~22.41 MPa operational chamber pressure). The results can be seen in Table 6.14
through Table 6.16 below.

Table 6.14. Pressure Stress Summary, Channel Width (CW) = 0.030 in / 0.762 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8
Operating
Chamber
Pressure
[𝑷𝒐𝒑 ]
(MPa)

Operating
Chamber
Pressure
[𝑷𝒅𝒆𝒕 ]
(MPa)

Coolant
Pressure
[𝑷𝒄𝒐𝒐𝒍 ]
(MPa)

∆𝑷𝒐𝒑
(MPa)**

Detonation
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒅𝒆𝒕 ]
(MPa)*

Operating
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒐𝒑]
(MPa)**

∆𝑷𝒅𝒆𝒕
(MPa)*

3.10

24.82

6.21

18.62

-3.10

5.24

-0.87

8.62

68.95

17.24

51.71

-8.62

14.54

-2.42

15.51

124.11

31.03

93.08

-15.51

26.18

-4.36

22.41

179.26

44.82

134.45

-22.41

37.81

-6.30

*Occurs when detonation wave is applying pressure to the cooling channel hot wall (Reduces Stress in
Hot Wall by Opposing Thermal Stress)
**Occurs when the detonation wave is not applying pressure to the cooling channel hot wall (Increases
Stress in Hot Wall by Combining with Thermal Stress)

202

Table 6.15. Pressure Stress Summary, Channel Width (CW) = 0.065 in / 1.651 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8
Operating
Chamber
Pressure
[𝑷𝒐𝒑 ]
(MPa)

Operating
Chamber
Pressure
[𝑷𝒅𝒆𝒕 ]
(MPa)

Coolant
Pressure
[𝑷𝒄𝒐𝒐𝒍 ]
(MPa)

∆𝑷𝒐𝒑
(MPa)**

Detonation
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒅𝒆𝒕 ]
(MPa)*

Operating
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒐𝒑]
(MPa)**

∆𝑷𝒅𝒆𝒕
(MPa)*

3.10

24.82

6.21

18.62

-3.10

24.58

-4.10

8.62

68.95

17.24

51.71

-8.62

68.27

-11.38

15.51

124.11

31.03

93.08

-15.51

122.89

-20.48

22.41

179.26

44.82

134.45

-22.41

177.51

-29.59

*Occurs when detonation wave is applying pressure to the cooling channel hot wall (Reduces Stress in
Hot Wall by Opposing Thermal Stress)
**Occurs when the detonation wave is not applying pressure to the cooling channel hot wall (Increases
Stress in Hot Wall by Combining with Thermal Stress)

Table 6.16. Pressure Stress Summary, Channel Width (CW) = 0.100 in / 2.540 mm, Hot Wall
Thickness (tw) = 0.040 in / 1.016 mm, Detonation Pressure Ratio = 8
Operating
Chamber
Pressure
[𝑷𝒐𝒑 ]
(MPa)

Operating
Chamber
Pressure
[𝑷𝒅𝒆𝒕 ]
(MPa)

Coolant
Pressure
[𝑷𝒄𝒐𝒐𝒍 ]
(MPa)

∆𝑷𝒐𝒑
(MPa)**

Detonation
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒅𝒆𝒕 ]
(MPa)*

Operating
Pressure
Stress
[𝝈𝒕𝒂,𝒑𝒓,𝒐𝒑]
(MPa)**

∆𝑷𝒅𝒆𝒕
(MPa)*

3.10

24.82

6.21

18.62

-3.10

58.17

-9.70

8.62

68.95

17.24

51.71

-8.62

161.60

-26.93

15.51

124.11

31.03

93.08

-15.51

290.87

-48.48

22.41

179.26

44.82

134.45

-22.41

420.15

-70.02

*Occurs when detonation wave is applying pressure to the cooling channel hot wall (Reduces Stress in
Hot Wall by Opposing Thermal Stress)
**Occurs when the detonation wave is not applying pressure to the cooling channel hot wall (Increases
Stress in Hot Wall by Combining with Thermal Stress)

Even though the thermal stresses in the hot wall are expected to be larger in magnitude
than the cyclic pressure stresses, using Equation 6-31 to evaluate cooling system dimensions
proves to be a useful exercise. Figure 6.25 disregards thermal stresses and evaluates the tangential
stresses in the hot wall. The tangential stress in the figure represents when the detonation wave is
passing a cooling passage of interest. Thermal stresses would place the place the hot wall in the

203

plastic regime at temperatures ~200 deg F, which is well below standard hot wall operating
temperatures for rocket combustors [42]. The results are shown for different channel widths along
with the yield strength for GRCop-84 at 673K and 873K.
Figure 6.25 informs the designer on the sensitivity hot wall tangential stresses to the
selected cooling channel width and operating pressure. The sensitivity to channel width is evident
in Figure 6.25 with low aspect ratio cooling channels (large cooling channel width) resulting in
larger tangential stresses. Low aspect ratio cooling channel designs experience larger bending
stresses as the rib supports are spread further apart, offering less support at the midspan of the hot
wall as the detonation wave passes. As high aspect ratio designs are common practice in rocket
cooling system designs due their improved cooling performance, it is recommended that low
aspect ratio designs be avoided entirely.

Figure 6.25. Pressure Loads Experienced by Hot Wall; Assumed Coolant Pressure to be 2x the
Average Chamber Pressure; Assumed Peak Detonation Pressure to be 8x the Average Chamber
Pressure

204

A normal hot fire event for an RDE will experience a sequence of loading events. The first
loading event in the sequence is driven by the thermal load as the combustor temperature rises
from ambient to operational temperature. This loading event commences when the combustor is
shutdown. The second loading event is driven by the cyclic pressure loading. To properly analyze
this fatigue loading event a linear damage approach should be used that incorporates the mean
stress effects for the thermal and pressure loading. A Linear Damage Block Loading approach was
used
𝑁𝑝𝑟
𝑁𝑡ℎ
𝐵[
+
]=1
𝑁𝑓,𝑡ℎ 𝑁𝑓,𝑝𝑟

Equation 6-32

where B is the number of allowable loading blocks before failure occurs, 𝑁𝑡ℎ is the number of
thermal loading cycles applied, 𝑁𝑓,𝑡ℎ is the number of cycles to failure for the thermal stresses,
𝑁𝑝𝑟 is the number of pressure loading cycles applied, and 𝑁𝑓,𝑝𝑟 is the number of cycles to failure
for the pressure stresses [19]. When B is calculated it informs the designer how many hot fire
cycles can be placed on the combustor with each hot fire cycle including the cumulative effects of
thermal cycling and mechanical cycling.
To complete the combined loading assessment, the Kuyper et al. approach from Section
6.4 was modified to incorporate the stresses from cyclic pressure loading. To modify the Kuyper
et al. approach, the maximum tangential stress from thermal loading was needed. The maximum
tangential plastic strain from Equation 6-13 can be converted to a tangential stress using the plastic
portion of the Ramberg Osgood equation as shown below.

𝜎𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 = 𝐾 ′ (𝜀𝑝𝑙,𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 )

𝑛′

Equation 6-33

The combined tangential stress in the hot wall can then be found by combining the tangential
thermal stress and tangential pressure stress. The combined tangential stress is varying as the
detonation wave travels around the combustor annulus. The combined tangential stress when the
detonation wave is not passing over the cooling channel of interest can be found using Equation
6-34 below. As the pressure stresses from the passing detonation wave counteracts the thermal
stresses, the maximum stress in the hot wall during combined loading occurs when the passing

205

detonation wave is not applying pressure to the hot wall (i.e. detonation wave not passing by the
hot wall).
The combined tangential stress when the detonation wave is passing over the cooling
channel of interest can be found using Equation 6-35 below. The minimum stress in the hot wall
when the combustor is firing is when the passing detonation wave is applying pressure to the hot
wall. The variation in these stresses is cyclic as the detonation wave rotates around the combustor
annulus, pulsing the hot wall on each pass. The maximum and minimum stresses below cycle up
and down in magnitude around the maximum thermal stress found in Equation 6-33. For reference,
a summary of the maximum and minimum combined tangential stress calculations is provided in
Figure 6.26.
𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 = 𝜎𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 − 𝜎𝑡𝑎,𝑝𝑟,𝑜𝑝

Equation 6-34

𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 = 𝜎𝑡𝑎,𝑡ℎ,𝑚𝑎𝑥 − 𝜎𝑡𝑎,𝑝𝑟,𝑑𝑒𝑡

Equation 6-35

Figure 6.26. Summary of Maximum and Minimum Combined Tangential Stress Calculations
The maximum and minimum combined loading plastic tangential strains can then be found
using the Equation 6-36 and Equation 6-37 below.
1

𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 𝑛′
𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 = (
)
𝐾′

Equation 6-36

1

𝜎𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 𝑛′
𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 = (
)
𝐾′

Equation 6-37

206

Using the combined tangential plastic strain from Equation 6-36 and Equation 6-37 along with the
axial plastic strain from Equation 6-12, the maximum and minimum combined effective plastic
strain can be found using Equation 6-38 and Equation 6-39 below.
2

𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 =

31/2
2

𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 =

31/2

2
2
(𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
+ 𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ + 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ
)1/2

Equation 6-38

2
2
(𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
+ 𝜀𝑝𝑙,𝑡𝑎,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ + 𝜀𝑝𝑙,𝑎𝑥,𝑡ℎ
)1/2

Equation 6-39

Using the same methodology as presented in Section 6.3, the total effective combined stresses can
then be calculated and the Smith Watson Topper mean strain life evaluation can be completed by
modifying the respective equations. Equation 6-40 through Equation 6-48 below represent the
modified approach to complete the Smith Watson Topper assessment [19].

𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 =

2(1 + 𝑣) 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
+ 𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥
3
𝐸

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 = 𝐾 ′ (𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 )

𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 =

Equation 6-41

2(1 + 𝑣) 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
+ 𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
3
𝐸

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 = 𝐾 ′ (𝜀𝑝𝑙,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛 )

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥

𝑛′

Equation 6-40

𝑛′

Equation 6-42

Equation 6-43

(𝜎𝑓′ )2
∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏
=
(2𝑁𝑓,𝑝𝑟 )2𝑏 + 𝜎𝑓′ 𝜀𝑓′ (2𝑁𝑓,𝑝𝑟 )𝑏+𝑐
2
𝐸

Equation 6-44

∆𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏 = 𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 − 𝜀𝑡𝑜𝑡,𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛

Equation 6-45

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 = 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑒𝑎𝑛 + 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑎𝑚𝑝

Equation 6-46

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 + 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
2

Equation 6-47

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑒𝑎𝑛 =

207

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑎𝑚𝑝 =

𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑎𝑥 − 𝜎𝑒𝑓𝑓,𝑐𝑜𝑚𝑏,𝑚𝑖𝑛
2

Equation 6-48

Using the process outlined above, a Linear Damage Block Loading assessment was
completed using the Smith Watson Topper mean stress correction approach. Section 6.3 identified
the strain life degradation expected for RDRC’s due to their larger thermal load when compared
to traditional rocket combustors. The purpose of this assessment was to evaluate the degradation
to operational life from the cyclic pressure loading. That being said, heat flux and combustor wall
temperatures were held constant at 5 kW/cm^2 and 673 K, respectively.
The Smith Watson Topper results for the thermal portion of the block loading assessment
can be seen in Table 6.17. Table 6.17 represents the thermal loading results for nominal Ramberg
Osgood and nominal/upper bound/lower bound Basquin Coffin Manson material properties. The
Smith Watson Topper results for the cyclic pressure loading portion of the block loading
assessment can be seen in Table 6.18 through Table 6.20. Table 6.18 represents the cyclic pressure
loading results for nominal Ramberg Osgood and nominal Basquin Coffin Manson material
properties. Table 6.19 represents the cyclic pressure loading results for nominal Ramberg Osgood
and lower bound Basquin Coffin Manson material properties. Table 6.20 represents the cyclic
pressure loading results for nominal Ramberg Osgood and upper bound Basquin Coffin Manson
material properties.

208

Table 6.17. Smith Watson Topper Results for Thermal Loading, Heat Flux = 5 kW/cm^2, Hot Wall Temperature = 673 K; Nominal
Ramberg Osgood Material Properties, Nominal/Upper/Lower Basquin Coffin Manson Material Properties
Material
Property
Nominal
BCM^
Lower
BCM^
Upper
BCM^

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒂𝒙
(MPa)**

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒊𝒏
(MPa)*

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒕𝒉,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒕𝒉𝒆𝒓𝒎
(mm/mm)

𝟐𝑵𝒇, 𝒕𝒉
(Reversals)

𝑵𝒇, 𝒕𝒉
(Cycles)

193.50

0

96.75

96.75

0.000

0.02064

450

225

193.50

0

96.75

96.75

0.000

0.02064

142

71

193.50

0

96.75

96.75

0.000

0.02064

756

378

209

*Occurs when combustor is not operating (no thermal load)
**Occurs when combustor is operating (thermal load)
^BCM = Basquin Coffin Manson

Table 6.18. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation Wave, Detonation Pressure Ratio = 8;
Nominal Ramberg Osgood Material Properties; Nominal Basquin Coffin Manson Material Properties
Chamber
Pressure
(MPa)
3.10

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒂𝒙
(MPa)*

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒊𝒏
(MPa)**

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒄𝒐𝒎𝒃 𝟐𝑵𝒇, 𝒑𝒓
(Reversals)
(mm/mm)

𝑵𝒇, 𝒑𝒓
(Cycles)

193.64

192.84

193.24

0.3971

0.996

0.000722

4.0E+10

2.00E+10

8.62

193.89

192.09

192.99

0.9007

0.991

0.001620

1.1E+07

5.50E+06

15.5

194.24

191.61

192.92

1.3159

0.986

0.002360

8.1E+05

4.05E+05

22.4

194.63

191.39

193.01

1.6196

0.983

0.002917

2.2E+05

1.10E+05

*Occurs when detonation wave is not applying pressure to the cooling channel hot wall
**Occurs when detonation wave is applying pressure to the cooling channel hot wall

Table 6.19. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation Wave, Detonation Pressure Ratio = 8;
Nominal Ramberg Osgood Material Properties; Lower Bound Basquin Coffin Manson Material Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒂𝒙
(MPa)*

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒊𝒏
(MPa)**

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒄𝒐𝒎𝒃
𝟐𝑵𝒇, 𝒑𝒓
(Reversals)
(mm/mm)

𝑵𝒇, 𝒑𝒓
(Cycles)

3.10

193.64

192.84

193.24

0.3971

0.996

0.000722

1.3E+10

6.3E+09

8.62

193.89

192.09

192.99

0.9007

0.991

0.001620

3.5E+06

1.7E+06

15.5

194.24

191.61

192.92

1.3159

0.986

0.002360

2.6E+05

1.3E+05

22.4

194.63

191.39

193.01

1.6196

0.983

0.002917

7.0E+04

3.5E+04

*Occurs when detonation wave is not applying pressure to the cooling channel hot wall
**Occurs when detonation wave is applying pressure to the cooling channel hot wall

210
Table 6.20. Smith Watson Topper Results for Cyclic Pressure Loading from Passing Detonation Wave, Detonation Pressure Ratio = 8;
Nominal Ramberg Osgood Material Properties; Upper Bound Basquin Coffin Manson Material Properties
Chamber
Pressure
(MPa)

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒂𝒙
(MPa)*

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒊𝒏
(MPa)**

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒎𝒆𝒂𝒏
(MPa)

𝝈𝒆𝒇𝒇,𝒄𝒐𝒎𝒃,𝒂𝒎𝒑
(MPa)

𝑹𝒓𝒂𝒕𝒊𝒐

∆𝜺𝒕𝒐𝒕,𝒆𝒇𝒇,𝒄𝒐𝒎𝒃
𝟐𝑵𝒇, 𝒑𝒓
(Reversals)
(mm/mm)

𝑵𝒇, 𝒑𝒓
(Cycles)

3.10

193.64

192.84

193.24

0.3971

0.996

0.000722

6.7E+10

3.4E+10

8.62

193.89

192.09

192.99

0.9007

0.991

0.001620

1.9E+07

9.3E+06

15.5

194.24

191.61

192.92

1.3159

0.986

0.002360

1.4E+06

6.8E+05

22.4

194.63

191.39

193.01

1.6196

0.983

0.002917

3.7E+05

1.9E+05

*Occurs when detonation wave is not applying pressure to the cooling channel hot wall
**Occurs when detonation wave is applying pressure to the cooling channel hot wall

The Smith Watson Topper results above were used to complete the linear damage
assessment. For this assessment, the quantity of block loadings was set to 1 in Equation 6-32, 𝑁𝑡ℎ
was varied, and 𝑁𝑝𝑟 was calculated to determine the available run time. The results for a chamber
pressure of 3.10 MPa and 8.62 MPa can be seen in Table 6.21. The results for a chamber pressure
of 15.5 MPa and 22.4 MPa can be seen in Table 6.22. The results are provided for nominal
Ramberg Osgood and nominal/upper/lower bound Basquin Coffin Manson material properties. A
wave pass frequency of 13 kHz was used to calculate run time from the available pressure cycles
calculated.

Table 6.21. Linear Damage Assessment Results for Chamber Pressure of 3.10 MPa and 8.62 MPa;
Nominal Ramberg Osgood Material Properties; Nominal/Upper/Lower Bound Basquin Coffin
Manson Material Properties; Wave Pass Frequency = 13 kHz to Calculate Run Time from Cycles

211

Table 6.22. Linear Damage Assessment Results for Chamber Pressure of 15.5 MPa and 22.4 MPa;
Nominal Ramberg Osgood Material Properties; Nominal/Upper/Lower Bound Basquin Coffin
Manson Material Properties; Wave Pass Frequency = 13 kHz to Calculate Run Time from Cycles

A summary of the combined loading assessment results is provided in Figure 6.27 and
Figure 6.28 below. These figures are intended to demonstrate the reduction in operational life due
to the cyclic pressure stresses. Figure 6.27 provides results for a nominal Ramberg Osgood and
nominal Basquin Coffin Manson material properties. The figure assumes the same thermal
environment for all operating pressures. In reality, the designer will face a larger thermal load at
higher operating pressures and the dotted line that represents available life for traditional rocket
combustors will have a negative slope. Figure 6.28 provides results for a nominal Ramberg Osgood
and lower bound Basquin Coffin Manson material properties.
The results highlight that RDE’s exhibit the same failure mechanism as traditional rocket
combustors (thermal cycling) but also exhibit a new HCF failure mechanism with high frequency
cyclic pressure loading applications from the passing detonation wave. RDE’s will be more
sensitive to the thermal cycling failure mechanism as they experience larger thermal loading. As
the detonation pressure ratio increases or the wave pass frequency increases, this HCF failure
mechanism becomes more prominent. The high chamber pressure results are highly dependent on
the detonation pressure ratio assumed and a recent study by Dille et al. indicate that these ratios
may not bas as high as that assumed for this study [47].
212

The results highlight that high chamber pressure RDE’s are likely to be run duration limited
from the new HCF failure mechanism and the first use case of an RDE is likely to be in an RL10
class combustor. The reduction in chamber life between Figure 6.27 and Figure 6.28 highlights
the importance of this studies results on material properties. The average chamber pressure
achieved during WC 2.0 testing and the achieved thermal cycles and run duration are included on
Figure 6.27 and Figure 6.28 for reference. Figure 6.27 indicates that significant life remained for
the WC 2.0 hardware. Figure 6.28 indicates that the WC 2.0 combustor should have failed due to
thermal cycling. Actual test results and visual inspections of the WC 2.0 hardware highlight that
lower bound Basquin Coffin Manson material properties are likely overly conservative.

Figure 6.27. Summary of Combined Loading Assessment; Nominal Ramberg Osgood Material
Properties; Nominal Basquin Coffin Manson Material Properties; Detonation Pressure Ratio = 8;
Wave Pass Frequency = 13 kHz to Determine Run Time from Cycles

213

Figure 6.28. Summary of Combined Loading Assessment; Nominal Ramberg Osgood Material
Properties; Lower Basquin Coffin Manson Properties; Detonation Pressure Ratio = 8; Wave Pass
Frequency = 13 kHz to Determine Run Duration from Cycles

214

CONCLUSIONS

Multiple 1.6”/4.1 cm diameter RDE combustors were designed, fabricated, and tested. The
RDE’s were entirely additively manufactured out of GRCop-84, including injector holes,
propellant manifolds, cooling channels, and cooling manifolds. The igniter was brought the
backside of the injector face, offering more insight into a flight like ignition system. The water
cooled RDRC tested the most accumulated 309 seconds of hot fire testing and 121
starts/shutdowns. Testing included long duration testing and pulsed short duration testing. Long
duration testing was completed to characterize heat flux and HCF loading. Pulsed short duration
testing was completed to evaluate thermal cycling impacts to the combustor structure and evaluate
LCF loading. Of the 309 seconds of total test time, pulsed short duration testing comprising 197
seconds and long duration testing comprising 112 seconds. The hardware experienced 118 LCF
loadings on the combustor cooling passages, equivalent to the amount of thermal cycle starts and
shutdowns. An endurance test was completed at 60 seconds in duration, demonstrating operation
well beyond thermal steady state. Additionally, ~3.7 million HCF loadings were placed on the
combustor cooling passages, equivalent to the approximate amount of detonation wave passes
present for all of the WC 2.0 testing.
Operating pressures ranged from 5 to 15 atm. The highest pressure conditions resulted in
hot gas wall temperatures exceeding 1000°F on the outerbody of the combustor and injector face
temperatures peaking at 350°F. Water calorimetry was used to compute heat fluxes, which were
then compared to traditional rocket engine throat level heat fluxes calculated using Bartz equations
under average operating conditions. The outerbody heat fluxes reached up to 3.7 kW/cm², while
injector face heat fluxes reached a maximum of 1.6 kW/cm². When compared to Bartz throat level
values, the outer-body heat fluxes varied from 0.9 to 1.6 times the throat level values, and injector
heat fluxes ranged from 0.3 to 0.5 times the throat level values.
A combined thermal and pressure loading fatigue assessment was completed that took into
consideration mean stresses and cumulative damage from the spectrum of loading events.
Traditional rocket combustor life is typically limited by the thermal cycles that can be placed on
the cooling channel hot wall. The fatigue analysis results highlight the reduction in available low
cycle fatigue life as RDE's experience larger thermal loads when compared to traditional rocket
combustors. Low cycle fatigue life will become especially challenging in higher chamber pressure
215

combustors where thermal environments are more extreme, and the ability keep hot wall
temperatures within acceptable levels is more challenging.
The study also highlights that the passing detonation wave provides a high cycle fatigue
(HCF) failure mechanism that is not present in traditional rocket combustors. This failure
mechanism is the result of the pressure pulse provided by the passing detonation wave causing a
variable load on the hot wall. This variable load is applied at frequencies commonly in the 10's of
kHz, resulting in large quantities of loading cycles when operated at rocket like durations (>60
sec). This HCF failure mechanism is most impactful at larger chamber pressures where the
detonation pressure ratio causes peak pressures to be elevated, resulting in larger cyclic stresses
and strains in the hot wall. The results indicate that high chamber pressure combustors may
experience HCF life exceedances within seconds of operation.
The results provided in this document highlight that additional studies are needed to
explore thermal and structural characteristics of rotation detonation engines. The following are
recommendations for future studies:
•

If future studies are to use similar coolant exit arrangements as this study, it is
recommended that a larger quantity of passages are outfitted with thermocouples to collect
more samples of coolant exit temperature. Depending on the quantity of passages outfitted
with thermocouples, this setup would approach the average measurement that would be
collected in a manifolded coolant exit. Additionally, this approach could provide evidence
of obstructed passages, either from the manufacturing process or ingress of foreign object
debris during testing. If manifolding the coolant exit is to be used, the manufacturing
challenges should be explored by the designer. Techniques for manifolding the coolant
exit are listed below along with the challenges the designer is faced with implementing
them:
•

Printing the Exit Manifold in the Additive Manufacturing Process: This
complicates powder removal and requires CT imaging of the hardware to verify
powder removal was completed successfully. At the combustor sizes utilized for
this work, CT imaging was estimated to double the cost of the hardware build.

•

Welding on an Exit Manifold Post Additive Manufacturing Process: With the
GRCop-84 material used in this work, electron beam welding would have to be

216

utilized. This process requires a weld program with multiple test samples and would
have required significantly more machining. It is estimated that this would have
nearly doubled the cost of the hardware build.
•

Attaching a Manifold by Bolted Joint with Seal: Due to the small size of this design,
adding a bolted joint and seal would have driven the size of the hardware to be
larger. The additional size of the hardware would have caused the additive
manufacturing price to rise and would have required more post machining.
Additionally, seals are prone to leaks and failures if exposed to elevated
temperature environments.

•

The test setup was limited on the achievable power setting. Larger power levels are
recommended to be explored to characterize heat flux to higher power settings.

•

Longer duration tests or repeated tests with significant duration should be explored to
accumulate as many high cycle fatigue loadings as achievable. This is recommended to
further explore the new HCF failure mechanism that may be present in RDEs.

•

Heat flux was found to be sensitive to mixture ratio. Further mixture ratio studies should
be completed to characterize heat flux.

•

The cases in Test Campaign 2.0 that indicate the combustor was cycling between
detonative combustion and cases with increased parasitic deflagration should be further
explored. These cases could potentially offer useful linkage to the variation in heat flux
between detonative and deflagrative combustion.

217

REFERENCES

[1] Parker Seal Group, O-Ring Division. (2001). Parker O-Ring Handbook.
[2] Cook, R.T., Fryk, E.E., & Newell, J.F. (1983). SSME main combustion chamber life prediction.
[3] Bennewitz, J. W., Burr, J. R., Bigler, B. R., Burke, R. F., Lemcherfi, A., Mundt, T., Rezzag,
T., Plaehn, E. W., Sosa, J., Walters, I. V., Schumaker, S. A., Ahmed, K. A., Slabaugh, C.
D., Knowlen, C., & Hargus, W. A. (2023). Experimental validation of rotating detonation
for
rocket
propulsion.
Scientific
Reports,
13(1),
14204–14204.
https://doi.org/10.1038/s41598-023-40156-y
[4] Smith, R. D., & Stanley, S. B. (2021). Experimental Investigation of Rotating Detonation
Rocket Engines for Space Propulsion. Journal of Propulsion and Power, 37(3), 463–473.
https://doi.org/10.2514/1.B37959
[5] Ledbetter, H. M., & Naimon, E. R. (1974). Elastic Properties of Metals and Alloys. II. Copper.
Journal of Physical and Chemical Reference Data, 3(4), 897–935.
https://doi.org/10.1063/1.3253150
[6] Walters, I. V., Journell, C. L., Lemcherfi, A., Gejji, R. M., Heister, S. D., & Slabaugh, C. D.
(2020). Operability of a Natural Gas–Air Rotating Detonation Engine. Journal of
Propulsion and Power, 36(3), 453–464. https://doi.org/10.2514/1.B37735
[7] Lim, D. (2019). Experimental Studies of Liquid Injector Response and Wall Heat Flux in a
Rotating Detonation Rocket Engine. Purdue University. ProQuest Dissertations
Publishing.
[8] Stechmann, D. P. (2017). Experimental Study of High-Pressure Rotating Detonation
Combustion in Rocket Environments. Purdue University. ProQuest Dissertations
Publishing.
[9] Bykovskii, F. A., Zhdan, S. A., & Vedernikov, E. F. (2006). Continuous Spin Detonations.
Journal of Propulsion and Power, 22(6), 1204–1216. https://doi.org/10.2514/1.17656
[10] Stechmann, D. P., Heister, S. D., & Harroun, A. J. (2019). Rotating Detonation Engine
Performance Model for Rocket Applications. Journal of Spacecraft and Rockets, 56(3),
887–898. https://doi.org/10.2514/1.A34313
[11] Fiorino, N. T., Dechert, J. R., Snow, N. J., Schauer, F. R., Polanka, M. D., Schumaker, S. A.,
& Sell, B. C. (2021). Improving the stability and operating envelope for a small scale, high
frequency rotating detonation engine (Rde). AIAA Scitech 2021 Forum, 1–15.
[12] Kudo, Y., Nagura, Y., Kasahara, J., Sasamoto, Y., & Matsuo, A. (2011). Oblique detonation
waves stabilized in rectangular-cross-section bent tubes. Proceedings of the Combustion
Institute, 33 (2), 2319–2326. https://doi.org/10.1016/j.proci.2010.08.008

218

[13] Quentmeyer, R. (1977). Experimental fatigue life investigation of cylindrical thrust chambers.
American Institute of Aeronautics and Astronautics. AIAA Conference Papers.
[14] Hilburger, M. W. (Mark W. (2020). Buckling of thin-walled circular cylinders. National
Aeronautics and Space Administration, Langley Research Center.
[15] Mendelson, A., Manson, S. (1959) Practical Solution of Plastic Deformation Problems in
Elastic-Plastic Range. NASA Technical Report R-28, 1959.
[16] Gradl, P. R., Protz, C., Cooper, K., Garcia, C., Ellis, D., & Evans, L. (2019). Grcop-42
development and hot-fire testing using additive manufacturing powder bed fusion for
channel-cooled combustion chambers. AIAA Propulsion and Energy Forum and
Exposition, 2019. https://doi.org/10.2514/6.2019-4228
[17] Teasley, T. W., Fedotowsky, T. M., Gradl, P. R., Austin, B. L., Heister, S. D. (2023). Current
State of NASA Continuously Rotating Detonation Cycle Engine Development. AIAA
2023-1873. AIAA SCITECH 2023 Forum. January 2023.
[18] Incopera, F.P., DeWitt, D.P., “Fundamentals of Heat and Mass Transfer,” 5th Ed., John Wiley
& Sons, Inc., New York, 2002.
[19] Sangid, M. (2021). AAE 554 - Fatigue of Structures and Materials [Course Syllabus]. Purdue
University.
[20] Krzysztof Stopka, John Smallwood, Aman Chokshi, Stephen D. Heister and Michael Sangid.
Structural and Fatigue Analysis of a Rotating Detonation Rocket Engine. AIAA 20231869. AIAA SCITECH 2023 Forum. January 2023.
[21] Lemmon, E.W., Bell, I.A., Huber, M.L., McLinden, M.O., “REFPROP Documentation,
Release 10”, National Institute of Standards and Technology, US Department of
Commerce, June 4, 2018.
[22] Stevens, C. A., Fotia, M. L., Hoke, J. L., & Schauer, F. R. (2018). Quasi-steady heat transfer
measurements in an RDE. AIAA Aerospace Sciences Meeting, 2018, 210059.
https://doi.org/10.2514/6.2018-1884
[23] Theuerkauf, S. W., Schauer, F. R., Anthony, R., Paxson, D. E., Stevens, C. A., & Hoke, J. L.
(2016). Comparison of simulated and measured instantaneous heat flux in a rotating
detonation
engine.
54th
AIAA
Aerospace
Sciences
Meeting.
https://doi.org/10.2514/6.2016-1200
[24] Theuerkauf, S. W., Schauer, F. R., Anthony, R., & Hoke, J. L. (2014). Average and
instantaneous heat release to the walls of an RDE. 52nd AIAA Aerospace Sciences
Meeting - AIAA Science and Technology Forum and Exposition, SciTech 2014.
https://doi.org/10.2514/6.2014-1503

219

[25] Theuerkauf, S. W., King, P. I., Schauer, F. R., & Hoke, J. L. (2013). Thermal management
for a modular rotating detonation engine. 51st AIAA Aerospace Sciences Meeting
Including the New Horizons Forum and Aerospace Exposition 2013, Aerospace Sciences
Meeting. https://doi.org/10.2514/6.2013-1176
[26] Schwer, D., & Kailasanath, K. (2011). Numerical investigation of the physics of rotatingdetonation-engines. Proceedings of the Combustion Institute, 33(2), 2195–2202.
https://doi.org/10.1016/j.proci.2010.07.050
[27] S. Gordon and B. J. McBride, Computer Program for Calculating and Fitting Thermodynamic
Functions, 2014, http://www.grc.nasa.gov/www/CEAWeb/.
[28] Naraghi, M. (1995). RTE, A Computer Code for Rocket Thermal Evaluation. NASA. Lewis
Research Center, The Sixth Annual Thermal and Fluids Analysis Workshop, 1995.
[29] Lopes, N. C., Chao, Y., Dasarla, V., Sullivan, N. P., Ricklick, M. A., & Boetcher, S. K. S.
(2022). Comprehensive Review of Heat Transfer Correlations of Supercritical CO2 in
Straight Tubes Near the Critical Point: A Historical Perspective. Journal of Heat Transfer,
144(12). https://doi.org/10.1115/1.4055345
[30] Anderson, J. D., “Hypersonic Viscous Interactions,” Hypersonic Aerothermodynamics,
AIAA Education Series. John D. Anderson, Reston, VA, 2006. Pg. 375-412
[31] Yang, J., & Naraghi, M. H. (2020). A fin analogy model for thermal analysis of regeneratively
cooled rocket engines. In AIAA Propulsion and Energy 2020 Forum (pp. 1–17).
https://doi.org/10.2514/6.2020-3817
[32] Kailasanath, K. (2011). The rotating-detonation-wave engine concept: A brief status report.
In 49th AIAA Aerospace Sciences Meeting Including the New Horizons Forum and
Aerospace Exposition. https://doi.org/10.2514/6.2011-580
[33] Lu, F. K., & Braun, E. M. (2014). Rotating Detonation Wave Propulsion: Experimental
Challenges, Modeling, and Engine Concepts. Journal of Propulsion and Power, 30(5),
1125–1142. https://doi.org/10.2514/1.B34802
[34] Heiser, W. H., & Pratt, D. T. (2002). Thermodynamic Cycle Analysis of Pulse Detonation
Engines. Journal of Propulsion and Power, 18(1), 68–76. https://doi.org/10.2514/2.5899
[35] Anderson, W. S., Heister, S. D., Kan, B., & Hartsfield, C. (2020). Experimental Study of a
Hypergolically Ignited Liquid Bipropellant Rotating Detonation Rocket Engine. Journal of
Propulsion and Power, 36(6), 851–861. https://doi.org/10.2514/1.B37666
[36] Lerch, B. and Ellis, D. (2005). Comparison of Fatigue Behavior of Copper
Alloys [PowerPoint slides]. MS&T05, Glenn Research Center at Lewis Field
[37] Heister, S. D., Anderson, W. E., William E., Pourpoint, T., Cassady, J. (2019). Rocket
propulsion. Cambridge University Press.

220

[38] Lim, D. (2019). Experimental Studies of Liquid Injector Response and Wall Heat Flux in a
Rotating Detonation Rocket Engine. ProQuest Dissertations Publishing.
[39] Gradl, P. R., Greene, S. E., Protz, C., Bullard, B., Buzzell, J., Garcia, C., Wood, J., Cooper,
K., Hulka, J., & Osborne, R. (2018). Additive manufacturing of liquid rocket engine
combustion devices: A summary of process developments and hot-fire testing results. 2018
Joint Propulsion Conference. https://doi.org/10.2514/6.2018-4625
[40] Anderson, J. (2011) Fundamentals of Aerodynamics. 5th Edition. McGraw Hill Publishers.
[41] Minneci, R. P., Lass, E. A., Bunn, J. R., Choo, H., & Rawn, C. J. (2021). Copper-based alloys
for structural high-heat-flux applications: a review of development, properties, and
performance of Cu-rich Cu-Cr-Nb alloys. International Materials Reviews, 66(6), 394–
425. https://doi.org/10.1080/09506608.2020.1821485
[42] Kuyper, D. J., & Burge, H. L. (1967). Simplified thermal fatigue analysis for liquid rocket
combustion chambers. Journal of Spacecraft and Rockets, 4(1), 126–128.
https://doi.org/10.2514/3.28824
[43] Conway, J. B., Stentz, R. H., and Berling, J. T. (1973). High Temperature, Low-Cycle Fatigue
of Copper-Base Alloys in Argon; Part I – Preliminary Results for 12 Alloys at 1000 deg F
[Final Report, Jan. 1973]. 1973. Print.
[44] Walters, I. V., Lemcherfi, A., Gejji, R. M., Heister, S. D., & Slabaugh, C. D. (2021).
Performance Characterization of a Natural Gas–Air Rotating Detonation Engine. Journal
of Propulsion and Power, 37(2), 292–304. https://doi.org/10.2514/1.B38087
[45] Jorgensen, E. D., Cordero, Z. C., & Vaccaro, D. (2022). Structural Optimization of
Regeneratively Cooled Rotating Detonation Rocket Engines. In AIAA Science and
Technology
Forum
and
Exposition,
AIAA
SciTech
Forum
2022.
https://doi.org/10.2514/6.2022-0092
[46] Desai, Y. (2018). LES of Stechmann Case. Hypercomp (performed under AFRL Phase I SBIR
as subcontract to INSpace LLC), 2018.
[47] Dille, K. J., Frederick, M. D., Slabaugh, C. D., & Heister, S. D. (2024). Rotating detonation
combustor performance informed through a novel megahertz-rate stagnation pressure
measurement. Physics of Fluids (1994), 36(2). https://doi.org/10.1063/5.0195465
[48] Sung, I. K., & Anderson, W. (2005). A subscale-based rocket combustor life prediction
methodology. 41st AIAA/ASME/SAE/ASEE Joint Propulsion Conference and Exhibit.
[49] Roark, R. J., Raymond J., Young, W. C., Warren C., Budynas, R. G., Richard G., & Sadegh,
A. M. (2012). Roark’s formulas for stress and strain. (8th ed.). McGraw-Hill.

221

APPENDIX A. HARDWARE CONFIGURATION SUMMARY

Table A.1. Hardware Configuration Summary
Material

Combustion
Chamber
OD/ID

Outerbody Cooling
Channel
Dimensions/Quantity

GRCop-84

1.60”/1.32”

N/A

GRCop-84

1.60”/1.32”

N/A

Water
Cooled

GRCop-84

1.60”/1.32”

.030” x .030” / 67

WC
2.0

Water
Cooled

GRCop-84

1.60”/1.32”

WC
2.1

Water
Cooled

GRCop-42

1.60”/1.32”

ID

Type

HS
1.0
HS
1.1

Heat
Sink
Heat
Sink

WC
1.0

Chamber
Pressure
Measurement
0.68” from
Injector Face
0.10” from
Injector Face

Thermocouple
Shrouding

Nozzle Exit
OD/ID

Hot
Fire
Tested

No

N/A

Yes

No

N/A

Yes

No

No

N/A

Yes

.100” x .030” / 36

No

Yes

1.75”/1.18”

Yes

.030” x .030” / 67

No

Yes

1.75”/1.18”

No

Note: The innerbody and injector cooling system design remained the same between WC 1.0 and WC 2.0/2.1. Refer to Table 2.2 for more
information

222

Figure A.1. Water Cooled 1.0 Dimension Summary

223

Figure A.2. Water Cooled 2.0/2.1 Dimension Summary

224

APPENDIX B. PLUMBING AND INSTRUMENTATION DIAGRAMS

Figure B.1. Plumbing and Instrumentation Diagram

225

Figure B.2. Coolant and Instrumentation Diagram

226



## Metadata
- Source file: junk_drawer/John Smallwood dissertation (FINAL).pdf
- Extracted: 2026-05-18
- Category: academic-homework
