# Ford Lynch Master's Thesis.pdf

Source: junk_drawer/Ford Lynch Master's Thesis.pdf

Category: [[academic-paper]]

## Summary
PERFORMANCE OF SUPERSONIC TURBOMACHINERY FOR ROTATING DETONATION ENGINES by Ford Lynch A Thesis Submitted to the Faculty of Purdue University In Partial Fulfillment of the Requirements for the degree of Master of Science in Mechanical Engineering

## Full Content
PERFORMANCE OF SUPERSONIC TURBOMACHINERY FOR
ROTATING DETONATION ENGINES
by
Ford Lynch

A Thesis
Submitted to the Faculty of Purdue University
In Partial Fulfillment of the Requirements for the degree of

Master of Science in Mechanical Engineering

School of Mechanical Engineering
West Lafayette, Indiana
August 2023

THE PURDUE UNIVERSITY GRADUATE SCHOOL
STATEMENT OF COMMITTEE APPROVAL

Dr. Guillermo Paniagua
School of Mechanical Engineering
Dr. James Braun
School of Mechanical Engineering
Dr. Eckhard Groll
School of Mechanical Engineering
Dr. Terrence Meyer
School of Mechanical Engineering

Approved by:
Dr. Nicole Key

2

Dedicated to the Lord Jesus Christ, who has guided my footsteps from the beginning, and to my
family, who have always supported me through the good and the bad.

3

ACKNOWLEDGMENTS

I would like to thank Prof. Guillermo Paniagua and Prof. James Braun for inviting me to
join the PETAL team when I was still very much an outsider to research. Their many hours of
guidance for this thesis have helped me succeed even when I did not think it was possible. I would
also like to thank Prof. Eckhard Groll for advising me during graduate school just like he did for
my father many years ago. To the PETAL and Zucrow employees and students who helped with
this research, you have my profound thanks; I would not have been able to conduct any combustor
tests without you. A final thanks goes to Fatih Meral, who was a great coworker and friend for
the brief time that we worked together.
The many projects of this thesis research were funded by both the Maf’at division of the
Israel Ministry of Defense and Tree Associates in the UK. While the project timelines have been
stressful, our conversations over the past several months have been a joy.

4

TABLE OF CONTENTS

LIST OF TABLES .......................................................................................................................... 8
LIST OF FIGURES ...................................................................................................................... 10
NOMENCLATURE ..................................................................................................................... 15
ABSTRACT.................................................................................................................................. 18
1

INTRODUCTION ................................................................................................................. 19
1.1 State of the Art .................................................................................................................. 20
1.1.1 Detonation Engines .................................................................................................... 20
1.1.2 Axial Bladed Supersonic Turbines ............................................................................ 23
1.1.3 Axial Bladeless Supersonic Turbines ........................................................................ 25
1.1.4 Radial Bladed Supersonic Turbines........................................................................... 26
1.1.5 Dynamometers ........................................................................................................... 27
1.2 Research Objectives .......................................................................................................... 31
1.3 Research Methodology ..................................................................................................... 32
1.4 Thesis Layout .................................................................................................................... 33

2

COOLED COMBUSTOR ..................................................................................................... 34
2.1 Background ....................................................................................................................... 34
2.1.1 Heat Flux Estimate from an Uncooled RDC ............................................................. 34
2.1.2 Preliminary Design Choices for the Cooled RDC ..................................................... 36
2.1.3 URANS Calculations for the Cooled RDC ............................................................... 38
2.2 Cooled RDC Design ......................................................................................................... 41
2.2.1 Initial Version ............................................................................................................ 41
2.2.2 Intermediate Version ................................................................................................. 45
2.2.3 Final Version ............................................................................................................. 48
2.3 Cooled RDC Instrumentation ........................................................................................... 50
2.4 Cooled RDC Manufacturing ............................................................................................. 55
2.5 Cooled RDC Coolant Tubes ............................................................................................. 58
2.5.1 Calculated Mass Flow Rates ...................................................................................... 58
2.5.2 Tube Design ............................................................................................................... 60
2.5.3 Tube Manufacturing .................................................................................................. 62
5

2.6 Cooled RDC Integration with THOR ............................................................................... 63
2.7 Cooled RDC Test Results ................................................................................................. 66
3

SUPERSONIC TURBOMACHINERY ................................................................................ 69
3.1 Axial Bladed Supersonic Turbine ..................................................................................... 69
3.1.1 Background ................................................................................................................ 69
3.1.2 Impeller Design ......................................................................................................... 72
3.1.3 CAD Assembly .......................................................................................................... 73
3.1.4 Shaft Analysis ............................................................................................................ 74
3.2 Axial Bladeless Supersonic Turbine ................................................................................. 77
3.2.1 Background ................................................................................................................ 77
3.2.2 Impeller Design ......................................................................................................... 82
3.2.3 CAD Assembly .......................................................................................................... 86
3.3 Radial Bladed Supersonic Turbine ................................................................................... 88
3.3.1 Background ................................................................................................................ 88
3.3.2 Impeller Design ......................................................................................................... 90
3.3.3 CAD Assembly .......................................................................................................... 94
3.3.4 Inlet Modifications..................................................................................................... 95
3.3.5 Shroud Modifications ................................................................................................ 96
3.3.6 Final CAD Assembly ................................................................................................. 97

4

AIRBRAKE DYNAMOMETER .......................................................................................... 98
4.1 Background ....................................................................................................................... 98
4.2 Turbocharger Performance Maps ................................................................................... 102
4.3 Mounting System ............................................................................................................ 106
4.3.1 Initial Designs .......................................................................................................... 106
4.3.2

Intermediate Designs ............................................................................................... 108

4.3.3 Final Design ............................................................................................................. 109
4.4 Oil System....................................................................................................................... 111
4.5 Instrumentation and Rotating Hardware ......................................................................... 112
4.5.1 Compressor Exit Tube ............................................................................................. 112
4.5.2 RPM Sensor ............................................................................................................. 114
4.5.3 Torque Sensor .......................................................................................................... 116

6

4.5.4 Bearings ................................................................................................................... 116
4.5.5 Couplings ................................................................................................................. 116
4.6 Fully Integrated System .................................................................................................. 117
5

CONCLUSION.................................................................................................................... 119

APPENDIX A. COMBUSTOR DRAWINGS ........................................................................... 122
APPENDIX B. COMBUSTOR TUBE DRAWINGS ................................................................ 134
APPENDIX C. SUPERSONIC TURBINE DRAWINGS .......................................................... 152
APPENDIX D. SHAFT ANALYSIS FOR AXIAL BLADED TURBINE ................................ 157
APPENDIX E. SCREW ANALYSIS FOR RADIAL BLADED TURBINE ............................ 192
APPENDIX F. TURBOCHARGER PERFORMANCE MAPS ................................................ 201
APPENDIX G. LABVIEW PROGRAM FOR RPM SENSOR ................................................. 207
REFERENCES ........................................................................................................................... 212

7

LIST OF TABLES

Table 2.1: Maximum wall temperature for different cooling configurations. .............................. 37
Table 2.2: Flow straightener configurations. ................................................................................ 53
Table 2.3: Nitrogen coolant mass flow rates and total pressures at the venturi throat 𝑝01 and the
venturi exit 𝑝02 for the two venturis across a selection of reactant mass flow rates. .................. 59
Table 2.4: Tube lengths; Sections 1-1 through 1-7 were routed into Chamber 1, and Sections 2-1
through 2-7 were routed into Chamber 2. ..................................................................................... 62
Table 3.1: Inputs for the MATLAB script that generated the three initial turbines. .................... 70
Table 3.2: Parameter definitions for the bladeless turbine. .......................................................... 84
Table 3.3: Parameters for the six hub configurations. .................................................................. 94
Table D.1: Coupling boundary conditions. ................................................................................. 169
Table D.2: Bearing continuity conditions; bearings have angular 𝜃, not linear 𝑣, deflection. ... 169
Table D.3: External loads on the shaft. ....................................................................................... 178
Table D.4: Internal shear forces and bending moments within the shaft.................................... 179
Table D.5: Angular and linear deflections at the component cross-sections. ............................. 180
Table D.6: Definitions of variables used in fatigue analysis. ..................................................... 181
Table D.7: Shaft dimensions. ...................................................................................................... 186
Table D.8: Material properties. ................................................................................................... 187
Table D.9: Endurance limit modifying factors (also known as Marin Factors). ........................ 187
Table D.10: Notch dimensions. .................................................................................................. 187
Table D.11: Stress concentration parameters.............................................................................. 187
Table D.12: Fatigue stress analysis for critical section 𝐴 (the coupling). .................................. 188
Table D.13: Fatigue stress analysis for critical section 𝐵 (the upstream bearing)...................... 189
Table D.14: Fatigue stress analysis for critical section 𝐶 (the downstream bearing). ................ 190
Table D.15: Fatigue stress analysis for critical section 𝐷 (the turbine). ..................................... 191
Table E.1: Load conditions. ........................................................................................................ 193
Table E.2: Properties of the material in the grip. ........................................................................ 193
Table E.3: Properties of the screw. ............................................................................................. 193
Table E.4: Fastener parameter definitions from Section 8-4 and Table 8-7 ............................... 194

8

Table E.5: Fastener parameter calculations. ............................................................................... 195
Table E.6: Frustum parameter definitions from Section 8-5. ..................................................... 196
Table E.7: Frustum thicknesses. ................................................................................................. 197
Table E.8: Frustum “D” values. .................................................................................................. 197
Table E.9: Frustum stiffnesses for Class 10.9 screws only......................................................... 197
Table E.10: Factor of safety parameter definitions. .................................................................... 198
Table E.11: Factors of safety parameters for Class 10.9 screws only. ....................................... 199
Table E.12: Torque required to achieve preload for Class 10.9 screws only. ............................ 199
Table E.13: Factors of safety for M6-1 Class 10.9 screws only. ................................................ 199
Table E.14: Factors of safety for M8-1.25 Class 10.9 screws only. ........................................... 199
Table E.15: Torque (N*m) required to achieve preload for M6-1 screws only. ........................ 200
Table E.16: Torque (N*m) required to achieve preload for M8-1 screws only. ........................ 200
Table E.17: Factors of Safety (FOS) for M6-1 screws only. ...................................................... 200
Table E.18: Factors of Safety (FOS) for M8-1.25 screws only. ................................................. 200

9

LIST OF FIGURES

Figure 1-1: Comparison of pressure-volume diagrams (left) and temperature-entropy diagrams
(right) for three idealized thermodynamic cycles; adapted from [17]. ......................................... 21
Figure 1-2: (a) Schematic of wave structure in 3D side view; adapted from [3]. (b) Schematic of
wave structure in the radial-azimuthal plane; adapted from [19]. ................................................ 23
Figure 1-3: Iso-temperature contour on a three-dimensional rotating detonation combustor:
(A) detonation front, (B) oblique shock wave, (C) contact surface, (D) blocked injection due to the
higher post-detonation pressure, (E) refilling zone, and (F) slip-line [5]. .................................... 24
Figure 1-4: Closed-cycle (top) and open-cycle (bottom) test configurations; adapted from [7]. . 25
Figure 1-5: (a) Cross-sectional view of the bladeless turbine (b) Three-dimensional view of the
turbine with the wavy hub [27]. .................................................................................................... 26
Figure 1-6: (a) Top view of the optimized 3D rotor geometry (b) flow field distortion from the
RDC outlet to the rotor blade inlet [34]. ....................................................................................... 27
Figure 1-7: Example performance maps for a compressor (left) and a turbine (right) [35]. ........ 28
Figure 1-8: Water brake mechanism [39]. .................................................................................... 29
Figure 1-9: Airbrake mechanism [41]........................................................................................... 30
Figure 1-10: Induction eddy current mechanism [38]. ................................................................. 31
Figure 2-1: Heat flux from the uncooled combustor model at 1.2 kg/s (air + fuel): (a) instantaneous
snapshot on the inner end wall, (b) instantaneous snapshot on the outer end wall, (c) average heat
flux along the axial direction for both inner and outer end walls. ................................................ 35
Figure 2-2: (a) Cross-section of the numerical domain, (b) structured mesh of the combustor. .. 38
Figure 2-3: Four snapshots of the unsteady temperature in the cooled combustor. ..................... 39
Figure 2-4: Comparison of heat flux in the axial direction for the uncooled hub (inner end wall)
and the film-cooled shroud (outer end wall). ................................................................................ 40
Figure 2-5: Mass flow averaged profiles of temperature (top) and Mach number (bottom). ....... 41
Figure 2-6: Isometric and side cutaway views of the initial combustor design. ........................... 44
Figure 2-7: Side section views of the initial combustor design. ................................................... 44
Figure 2-8: Isometric and side cutaway views of the intermediate combustor design. ................ 47
Figure 2-9: Side section views of the intermediate combustor design. ........................................ 47
Figure 2-10: Isometric and side views of the final combustor design. ......................................... 49
Figure 2-11: Side section views of the final combustor design. ................................................... 49
Figure 2-12: Isometric and side section views of the combustor probe fittings and stators. ........ 50
10

Figure 2-13: Isometric and cutaway views of the probe holes in the film-cooled section. .......... 51
Figure 2-14: Isometric and cutaway views of the holes in the uncooled exhaust section. ........... 52
Figure 2-15: Diagrams of the flow straightener features. ............................................................. 53
Figure 2-16: Top view diagram for the probe locations of the eight flow straighteners. ............. 54
Figure 2-17: Side view diagram for the probe locations of the eight flow straighteners. ............. 54
Figure 2-18: Isometric and side views of the cooled combustor model for the 3D-printer. ......... 55
Figure 2-19: Diagrams of the flow straighteners with the 3D-printed support material in red. ... 56
Figure 2-20: Four views of the cooled combustor manufacturing process: (a) at the beginning of
the print, (b) at the end of the print, (c) after the threads and O-ring surfaces are machined, and (d)
after the innermost slot wall is machined. .................................................................................... 56
Figure 2-21: Image of the eight flow straighteners after post-print machining. ........................... 57
Figure 2-22: Five views of the uncooled exhaust flange manufacturing process: (a) the flange after
initial CNC lather operations, (b) the completed flange, (c) the completed window insert, (d) the
outside of the stacked combustor, and (e) the inside of the stacked combustor. .......................... 57
Figure 2-23: Isometric views of the combustor and tubing on the THOR stand. ......................... 61
Figure 2-24: Isometric view of the tubing CAD; Sections 1-1 through 1-7 (in blue) were routed
into Chamber 1 and Sections 2-1 through 2-7 (in green) were routed into Chamber 2. ............... 61
Figure 2-25: Images of the tube sections before (top) and after (bottom) bending. ..................... 63
Figure 2-26: Image of the nitrogen coolant tubes assembled on the combustor. ......................... 63
Figure 2-27: Images of the nitrogen tubes leading into the cooled combustor. ............................ 64
Figure 2-28: Images of the cooled combustor instrumentation. ................................................... 65
Figure 2-29: Image of the author standing next to the cooled RDC mounted on the THOR stand.
....................................................................................................................................................... 65
Figure 2-30: Images of the exhaust flange before and after testing. ............................................. 66
Figure 2-31: Phantom Camera images of the detonation wave for the highest mass flow test. ... 67
Figure 2-32: Cooled slot temperatures for a reactant mass flow rate of 2 lbm/s. ......................... 68
Figure 2-33: Cooled and uncooled slot temperatures for a reactant mass flow rate of 1 lbm/s.... 68
Figure 3-1: Three initial axial bladed turbine designs: (from left to right) a thirteen-blade design,
a ten-blade design, and an eight-blade design. ............................................................................. 70
Figure 3-2: Blade profile of the axial bladed turbine. ................................................................... 71
Figure 3-3: Mach number contour for an axial bladed turbine operating in supersonic flow. ..... 71
Figure 3-4: Downstream (left) and upstream (right) views of the axial bladed turbine. .............. 72

11

Figure 3-5: Downstream (left) and upstream (right) views of the 3D-printed axial bladed turbine.
....................................................................................................................................................... 73
Figure 3-6: Isometric and side section views of the cooled combustor outfitted with the axial bladed
supersonic turbine. ........................................................................................................................ 74
Figure 3-7: Diagram of the shaft analysis dimensions and nomenclature. ................................... 75
Figure 3-8: Pressure-enthalpy diagram for the SCO2 cycle (courtesy of Fatih Meral). ............... 78
Figure 3-9: Component diagram for the SCO2 cycle (courtesy of Fatih Meral). ......................... 78
Figure 3-10: Pressure contour (top) and Mach number contour (bottom) for a bladeless turbine
operating in saturated liquid-vapor CO2. ...................................................................................... 79
Figure 3-11: Pressure contour for a bladeless turbine operating in saturated liquid CO2............. 79
Figure 3-12: Mach number around the air injection throat of THOR........................................... 81
Figure 3-13: Pressure contour and Mach number contours for a bladeless turbine operating in
THOR with unvitiated air in the absence of a rotating detonation wave. ..................................... 81
Figure 3-14: Two orientations for the wave profile of the bladeless turbine. ............................... 82
Figure 3-15: Main dimensions for the bladeless turbine. ............................................................. 84
Figure 3-16: Four snapshots of the bladeless turbine creation: (a) the imported quarter-sector of
the first wavy profile with two construction circles, (b) the enclosed sketch of the first wavy profile
showing values for 𝐷1 and 𝐷𝑚𝑎𝑥, (c) the two wavy profiles, (d) the two wavy profiles with the
upstream circle and the helical guide curves. ............................................................................... 85
Figure 3-17: Four bladeless turbines created by importing Curves 1 and 2 and setting the spiral
direction to be either clockwise or counterclockwise. .................................................................. 86
Figure 3-18: Isometric and side section views of the bladeless turbine mounted in THOR. ....... 87
Figure 3-19: Pressure contour for a radial turbine operating in saturated liquid-vapor CO2. ....... 88
Figure 3-20: Pressure contour for a radial turbine operating in liquid CO2.................................. 89
Figure 3-21: Radial blade profiles with thicker leading edges for operating in liquid CO2. ........ 89
Figure 3-22: Pressure contour for a radial turbine operating in air............................................... 90
Figure 3-23: Snapshots of the radial turbine creation: (a) the blade and hub imported as hollow
surfaces, (b) the blade and hub as solid bodies, (c) the blade, hub, and shroud as solid bodies. .. 91
Figure 3-24: Six different configurations for the radial turbine hub modifications. .................... 93
Figure 3-25: Diagram of the radial turbine inlet, throat, and exit areas for Configuration 1. ...... 93
Figure 3-26: Diagram of the initial radial turbine CAD assembly. .............................................. 94
Figure 3-27: Three options for the radial turbine inlet: (1) six fittings without sintered mufflers, (2)
one fitting with a muffler but poor seals, (3) one fitting with a muffler and better seals. ............ 95

12

Figure 3-28: Two options for the radial turbine shroud. ............................................................... 96
Figure 3-29: Diagram of the final radial turbine CAD assembly. ................................................ 97
Figure 4-1: Diagram of the test setup for the axial bladed turbine. ............................................ 100
Figure 4-2: Images of the turbocharger and its CAD model. ..................................................... 100
Figure 4-3: Fluid flows for the axial bladed turbine’s four-step test procedure. ........................ 101
Figure 4-4: Fluid flows for the axial bladeless turbine’s two-step test procedure. ..................... 102
Figure 4-5: Fluid flows for the radial bladed turbine’s two-step test procedure. ....................... 102
Figure 4-6: Uncorrected compressor power as a function of uncorrected quantities. ................ 104
Figure 4-7: Uncorrected turbine power as a function of uncorrected quantities. ....................... 105
Figure 4-8: Corrected compressor power as a function of corrected quantities. ........................ 105
Figure 4-9: Corrected turbine power as a function of corrected quantities. ............................... 106
Figure 4-10: Two images of the initial aluminum turbocharger mounts. ................................... 107
Figure 4-11: Diagrams of the turbocharger mounted to the THOR stand. ................................. 108
Figure 4-12: Welded and machined mounts for the turbocharger. ............................................. 109
Figure 4-13: Isometric and side views of the final turbocharger mount. .................................... 110
Figure 4-14: Images of the manufacturing progress on the final turbocharger mount. .............. 111
Figure 4-15: Oil system for the turbocharger dynamometer. ..................................................... 112
Figure 4-16: Instrumentation diagram for the turbocharger compressor outlet tube. ................. 113
Figure 4-17: RPM sensor characteristics: (a) a diagram of the working principle, (b) the actual
RPM sensor, (c) a screenshot of the raw voltage measured with the myRIO. ........................... 115
Figure 4-18: Measured voltage (top) and calculated RPM (bottom) for a hand-spun test. ........ 115
Figure 4-19: CAD Assembly for the dynamometer, torque sensor, and radial turbine. ............. 118
Figure 4-20: Instrumentation diagram for the dynamometer (courtesy of Fatih Meral). ........... 118
Figure D-1: Component nomenclature diagram. ........................................................................ 157
Figure D-2: External load definitions. ........................................................................................ 160
Figure D-3: Boundary/continuity conditions. ............................................................................. 161
Figure D-4: Segment 1 in 𝑥𝑦 plane............................................................................................. 163
Figure D-5: Segment 1 in 𝑥𝑧 plane. ............................................................................................ 164
Figure D-6: Segment 2 in 𝑥𝑦 plane............................................................................................. 165
Figure D-7: Segment 2 in 𝑥𝑧 plane. ............................................................................................ 166

13

Figure D-8: Segment 3 in 𝑥𝑦 plane............................................................................................. 167
Figure D-9: Segment 3 in 𝑥𝑧 plane. ............................................................................................ 168
Figure D-10: External load variable sign conventions. .............................................................. 174
Figure D-11: External loads for an unbalance rotation angle of 0°. ........................................... 175
Figure D-12: External loads for an unbalance rotation angle of 45°. ......................................... 175
Figure D-13: External loads for an unbalance rotation angle of 270°. ....................................... 176
Figure D-14: Internal axial force and torque diagrams. .............................................................. 176
Figure D-15: Shear force and bending moment diagrams. ......................................................... 177
Figure D-16: Angular and linear deflections diagrams............................................................... 177
Figure D-17: Critical element locations and increment angle. ................................................... 185
Figure E-1: Nomenclature and orientation for the components in the screw analysis. .............. 192
Figure E-2: Loads 1 and 2 considered in the screw analysis. ..................................................... 192
Figure E-3: Diagram of fastener parameters. .............................................................................. 194
Figure E-4: Diagram of frustum parameters. .............................................................................. 196
Figure F-1: Compressor scatter data points. ............................................................................... 202
Figure F-2: Turbine scatter data points. ...................................................................................... 202
Figure F-3: Interpolation grid for compressor efficiency as a function of corrected quantities. 203
Figure F-4: Interpolation grid for turbine efficiency as a function of corrected quantities. ....... 203
Figure F-5: Compressor efficiency as a function of corrected quantities. .................................. 204
Figure F-6: Turbine efficiency as a function of corrected quantities.......................................... 204
Figure F-7: Corrected compressor power as a function of corrected quantities. ........................ 205
Figure F-8: Corrected turbine power as a function of corrected quantities. ............................... 205
Figure F-9: Corrected compressor torque as a function of corrected quantities. ........................ 206
Figure F-10: Corrected turbine torque as a function of corrected quantities. ............................. 206
Figure G-1: RPM plot for a calculation frequency of 1 Hz. ....................................................... 208
Figure G-2: RPM plot for a calculation frequency of 2 Hz. ....................................................... 209
Figure G-3: LabVIEW block diagram for the true cases. ........................................................... 210
Figure G-4: LabVIEW block diagram for the false cases........................................................... 211

14

NOMENCLATURE

Abbreviations
CAD

Computer-Aided Design

CFD

Computational Fluid Dynamics

DMLS

Direct Metal Laser Sintering

CO2

Carbon Dioxide

ORC

Organic Rankine Cycle

PETAL

Purdue Experimental Turbine Aerothermal Lab

PDE

Pulse Detonation Engine

RDC

Rotating Detonation Combustor

RDE

Rotating Detonation Engine

RDTE

Rotating Detonation Turbine Engine

RPM

Rotations Per Minute

SDE

Standing Detonation Engine

SCO2

Supercritical Carbon Dioxide

THOR

Turbine-integrated High-pressure Optical RDE

TCC

Turbocharger Compressor

TCT

Turbocharger Turbine

URANS

Unsteady Reynolds Averaged Navier Stokes

15

Symbols
𝑚̇

mass flow rate [kg/s]

𝑊̇

power [W or kW]

𝐴

area [m2]

𝐶𝑑

discharge coefficient [-]

𝐶𝑝

specific heat of a gas at constant pressure [J/(kg*K)]

ℎ

enthalpy [J/kg]

𝑀

Mach number [-]

𝑁

rotational speed [RPM]

𝑝

pressure [Pa]

𝑅

specific gas constant [J/(kg*K)]

𝑇

temperature [K]

𝑈

flow velocity [m/s]

𝛾

ratio of specific heats [-]

𝜂

efficiency [-]

𝜃

angle [°]

𝜌

density [kg/m3]

𝜏

torque [N*m]

𝜔

rotational speed [rad/s]

16

Subscripts
0#

total (stagnation) quantity for station #

𝑐

coolant

ℎ𝑒𝑙𝑖𝑥

helix (angle)

𝑠𝑙𝑜𝑝𝑒

slope (angle)

𝑚𝑒𝑐ℎ

mechanical

𝑡ℎ𝑒𝑟𝑚

thermodynamic

𝑡𝑜𝑡

total (stagnation) quantity

𝑅𝑃𝑀

rotations per minute

∞

mainstream

17

ABSTRACT

Rotating detonation combustion has been investigated since the 1960s and has gained much
attention in the past decade due to its promise of pressure gain. In theory, the pressure gain can
provide higher power output at inlet total temperatures similar to those of Brayton cycle engines,
leading to increased efficiency and decreased engine size. However, complexities presented by
detonative combustion have prevented it from becoming widely adopted, especially for
turbomachinery applications. A rotating detonation combustor with a transonic or supersonic
exhaust imposes rapid fluctuations in pressure, temperature, and flow angle at the inlet of the
turbine. To account for these fluctuations, ad hoc turbine designs have been proposed over the last
few years, including supersonic bladed and bladeless variants. Computational fluid dynamics
simulations have shown that it is possible to extract a meaningful amount of work from these
turbines, but dedicated experimental test rigs are needed to validate these designs at relevant
conditions in long-duration tests.
Toward this goal, this thesis focuses on three research elements. The first element is the
design of a cooled rotating detonation combustor with a downstream turbine that can operate for
long durations. The cooled combustor is accomplished in a two-part procedure: (1) repurposing
Purdue University’s Turbine-integrated High-pressure Optical Rotating detonation engine (THOR)
and (2) designing a lightweight, gaseous film-cooled combustor shroud with ample configurations
for pressure, temperature, and optical measurements.
The second element is the design of three supersonic turbines for use in RDEs: an axialflow bladed turbine, an axial-flow bladeless turbine, and an axial-inflow/radial-outflow bladed
turbine. Each turbine is designed for cold flow testing, and provisions for mounting the axial-flow
bladed turbine downstream of the cooled combustor are proposed. Supplemental turbine hardware
is also designed to provide precise and repeatable conditions for the turbine tests.
The third element is the construction of an energy absorption dynamometer to measure the
power output of the different supersonic turbines. Four types of dynamometers are explored,
including hydraulic brakes, electromagnetic brakes, electric generator brakes, and airbrakes.
Although the literature declares the electromagnetic brake to be more accurate, the most costeffective solution is to utilize the compressor side of a donated turbocharger. Combining all
research elements yields a new test rig for this new class of supersonic turbines.
18

1

INTRODUCTION

New aeroengine architectures for commercial and military applications are faced with
demands for greater thermal and spatial efficiency. In addition to efficiency, new architectures are
desired to operate over a wider range of speeds and inlet conditions than those for which traditional
technologies like subsonic turbomachinery and supersonic ramjets are designed. These engines
typically use deflagration combustion, in which a combustion wave propagates at a subsonic
velocity. An alternate type of combustion is detonation combustion, in which a combustion wave
propagates at a sonic velocity relative to a strong leading shock wave. Compared to deflagration
combustion, detonation combustion creates a pressure increase from which additional power may
be extracted. Thus, pressure gain combustion has the potential to manifest more compact engines
that fulfill the demands on efficiency and operating conditions.
One promising application of detonation combustion is the Rotating Detonation Engine
(RDE) [1], in which a continuous detonation wave passes circumferentially through a fuel-air
mixture in a circular annulus. As discussed in the next section, the RDE offers certain advantages
over other detonation engine forms. For example, an RDE can operate from subsonic to supersonic
speeds, and the fuel injection and purge systems operate continuously. However, the RDE also
presents unique challenges, including high thermal stresses on the combustor walls and integration
with turbomachinery.
To overcome the difficulties of RDEs, past research has generally focused on the following
areas: (1) numerical or experimental studies of the RDC alone [2, 3], (2) numerical simulations of
the interaction between the RDC and a downstream turbine [4, 5], (3) experimental investigations
of the RDC with existing turbine architectures [6, 7], and (4) computational optimizations of
supersonic turbines for RDC exhaust flow [8, 9]. Thus, there is still a lack of experimental
knowledge regarding the behavior of fully integrated Rotating Detonation Engines with supersonic
turbines. After reviewing the current state of the art in RDE research, this document transitions to
the experimental research objectives and methodology. Finally, this chapter concludes with a brief
discussion about the document’s layout for subsequent sections.

19

1.1

State of the Art

1.1.1 Detonation Engines
The term detonation is sometimes used synonymously with an explosion, which indicates
a rapid energy release in a combustible mixture, but in detonative propulsion, a detonation refers
to a shock wave sustained by the energy released by combustion [10]. The earliest recorded
investigations of detonation research are credited to French scientists Berthelot, Vieielle, Mallard,
and Le Chatelier in 1881, and the first zero-dimensional models of detonation waves were
described independently by English chemist Chapman in 1899 and French scientist Jouguet in
1905 [1, 11, 12, 13]. Decades later, in 1940, Russian scientist Zel’dovich showed that detonative
combustion could increase a cycle’s thermodynamic efficiency compared to that of closed-volume
combustion, but his calculated increase in efficiency was so low that he concluded detonative
combustion was not a viable approach in power generation [14]. Since the time of Zel’dovich,
this conclusion has been revised; many studies have shown detonation combustion to be a viable
if not yet realized option for power and thrust generation, as reviewed by [1, 2, 15].
The flow physics of detonations are out of the scope of this thesis, but many texts [10, 16]
provide information on this topic. Instead, the following section focuses on the thermodynamic
advantages of using detonations in propulsion systems. The most common thermodynamic cycle
in air-breathing propulsion is the Brayton Cycle, in which constant pressure (isobaric) combustion
occurs. To increase the pressure-volume work extraction from a Brayton Cycle, one might
consider the Humphrey Cycle, in which constant volume (isochoric) combustion creates a pressure
rise. However, the Humphrey Cycle is not used in turbomachinery since it is difficult to contain
continuous flow deflagration at constant volume. Interestingly, detonative combustion occurs at
nearly constant volume, as described by the Fickett-Jacobs Cycle; specific volume decreases
slightly, leading to a higher combustor exit pressure than those of the Brayton or Humphrey Cycles.
Figure 1-1 [17] shows pressure-volume and temperature-entropy diagrams for idealized
Brayton, Humphrey, and Fickett-Jacobs Cycles. Segment 1-2 indicates isentropic compression;
Segment 2-3 represents combustion, and Segment 3-4 shows isentropic expansion. Although
aeroengine cycles are usually open cycles, Segment 4-1 is included to indicate that Points 4 and 1
share the same isobar. Additionally, real cycles have neither isentropic compression nor isentropic
expansion, but the isentropic work assumption allows for easier comparison, especially regarding

20

cycle efficiency. The thermal efficiency expressions for the Brayton, Humphrey, and FickettJacobs cycles are given by (1), (2), and (3), respectively. In a study that used hydrogen, methane,
and acetylene as fuels, the thermal efficiencies of the Brayton, Humphrey, and Fickett-Jacobs
Cycle were on average 35%, 53%, and 58%, respectively [1]. In this simple analysis, a detonation
engine based on the Fickett-Jacobs Cycle could offer more than a 20% increase in efficiency
compared to deflagration engines based on the Brayton Cycle.

3

3
3

3

3

3

1

4

4

4

1

4

4

4

Figure 1-1: Comparison of pressure-volume diagrams (left) and temperature-entropy diagrams
(right) for three idealized thermodynamic cycles; adapted from [17].
𝛾−1

𝑇1
𝑝1 𝛾
𝜂𝐵𝑟𝑎𝑦𝑡𝑜𝑛 = 1 − = 1 − ( )
𝑇2
𝑝2

(1)

1

1

𝛾
𝑇3′ 𝛾
𝛾−1 (𝑇3′ ) − 1
(
)
−
1
𝑇1 𝑇
𝑝1 𝛾
𝑇
𝜂𝐻𝑢𝑚𝑝ℎ𝑟𝑒𝑦 = 1 − 𝛾 ⋅ ⋅ 2
= 1−𝛾⋅( )
⋅ 2
𝑇′
𝑇2 (𝑇3′ ) − 1
𝑝2
( 𝑇3 ) − 1
𝑇2
2

(2)

1

𝑇3′′ 𝛾
(
) −1
𝑇1
𝑇2
𝜂𝐹𝑖𝑐𝑘𝑒𝑡𝑡−𝐽𝑎𝑐𝑜𝑏𝑠 = 1 − 𝛾 ⋅ ⋅
𝑇2 (𝑇3′′ ) − 1
𝑇2

21

(3)

In addition to cycle efficiency considerations, a few more comparisons may be made
between deflagrations and detonations. Deflagrations propagate on the order of meters per second
(m/s) while detonations can propagate at kilometers per second (km/s). If the upstream Mach
number is arbitrarily set to 5, the following relationships may be observed in deflagrations and
detonations [1, 17]. Relative to the flow upstream and downstream of the combustion zone,
deflagrations travel at Mach 0.001 and 0.003, respectively, and detonations travel at Mach 5-10
and 1.0, respectively. Deflagrations and detonations have respective static pressure ratios near
unity and 13-55; the respective static temperature ratios are around 10 and 8-21. Thus, detonations
produce wide property ranges that are much larger than the corresponding deflagration properties.
To achieve the benefits of detonation combustion, many engine architectures have been
proposed, including the Standing Detonation Engine (SDE), the Pulse Detonation Engine (PDE),
and the Rotating Detonation Engine (RDE). An SDE is like a supersonic combustion ramjet
(scramjet), where compression is achieved by a series of wedge-induced oblique shocks; the
difference is that an SDE injects fuel upstream of the final oblique shock, resulting in a detonation
wave [18]. The downside of an SDE is that flight Mach number is limited to the range of 5-7;
however, this limitation is not exhibited in a PDE, which can operate from rest to Mach 4 [1]. In
a PDE, the combustor is typically a long tube, wherein a fuel-air mixture is ignited at the closed
end and a detonation wave propagates toward the open end. After the wave exits the tube, the tube
is purged with unvitiated air. The downsides to the PDE are that the detonation must be reinitiated
with each cycle, and the time spent in purging/refilling limits the cycle speed to 10-100 Hz [1, 18].
Unlike an SDE, an RDE can operate from subsonic to hypersonic speeds, and unlike a PDE,
an RDE functions at 1,000-10,000 Hz and has a detonation that does not need to be reinitiated with
each cycle [1]. A typical RDE combustor occupies the annulus between two coaxial cylinders;
fuel and oxidizer are injected at the combustor inlet, and a pre-detonator mounted normal to the
combustor wall initiates the detonation wave [17, 3]. The detonation passes circumferentially in
the circular annulus, and high-pressure, high-temperature products are exhausted through a shock
wave-expansion fan interaction, as depicted by Figure 1-2 [3, 19]. RDE technology is not yet
widely implemented due to a plenitude of variables that affect combustion stability, including the
injection scheme, equivalence ratio, detonation initiation, combustor shape, back pressure
propagation, and detonation combustion mode [17]. These variables are interrelated through
complex mechanisms that are not yet well understood, hence the need for ongoing RDE research.

22

(a)
(b)
Figure 1-2: (a) Schematic of wave structure in 3D side view; adapted from [3].
(b) Schematic of wave structure in the radial-azimuthal plane; adapted from [19].
1.1.2 Axial Bladed Supersonic Turbines
In the previous section, an RDE was described as an improvement upon deflagration
engines since combustion is almost isochoric, as modeled by the Fickett-Jacobs and Humphrey
Cycles. In the research of Su et al. [4], the isentropic compression and expansion assumptions of
the Humphrey Cycle were relaxed in the derivation of an analytical model to describe an RDE’s
thermodynamic performance. A parametric analysis of this model showed that greater thermal
efficiency may be attained by increasing either the compressor pressure ratio, the combustor
pressure rise ratio, or the heating ratio. A different study by Sousa et al. [5] expanded an existing
MATLAB® Simulink model of an engine with a deflagration combustor and a subsonic turbine
to account for an RDC paired with a supersonic turbine. The new model showed an 8% increase
in thermal efficiency over the deflagration turbine engine for low compression ratios.
Aside from cycle analyses, many studies have focused on the design of new supersonic
turbines to account for the fluctuations produced by the RDC. Figure 1-3 [5] shows one possible
RDE configuration, where flow is axial throughout the engine and distinct airfoils comprise the
supersonic turbine. (Other architectures are presented in subsequent sections.) In this axial bladed
turbine, airfoil profiles may be generated by the Method of Characteristics, as described by
Mushtaq et al. [8]. Since empirical studies for supersonic RDE turbines are rare, optimization
procedures are required, with special attention focused on the non-isentropic loss mechanisms [9].
In the work of Liu et al. [20], the primary loss mechanism was shown to be shock waves on the

23

turbine airfoils’ leading edges. Since shocks are generated upstream of any object in supersonic
flow, novel techniques are required to mitigate pressure losses across bladed turbines.

Figure 1-3: Iso-temperature contour on a three-dimensional rotating detonation combustor:
(A) detonation front, (B) oblique shock wave, (C) contact surface, (D) blocked injection due to
the higher post-detonation pressure, (E) refilling zone, and (F) slip-line [5].
In experimental studies of supersonic turbines paired with RDCs, two main configurations
may be used: closed-loop and open-loop. Schematics of these arrangements are provided in Figure
1-4 [7]. In a closed-loop test, the air entering the combustor is from the compressor exit. In an
open-loop test, the air entering the combustor is from a reservoir independent of the compressor
exit flow. In experiments by Naples et al. [7], a T63 reverse-flow turboshaft engine was configured
to operate in both open-loop and closed-loop configurations. A deflagrative combustor was used
in open-loop tests to characterize engine performance, and an RDC was used in closed-loop tests
to examine how high-frequency unsteadiness affects engine performance. Thus, a closed-loop
system can demonstrate a self-sustaining engine, but an open-loop configuration gives more
flexibility if the compressor cannot satisfy RDC inlet requirements.
An experiment by Rhee et al. [21] utilized a closed-loop system, where a commercial
engine’s deflagration combustor was swapped with an RDC. Although a true detonation wave
may not have been achieved, the rig’s rotational speed increased during hot-flow experiments,
indicating that the RDE might be self-sustaining. In an investigation by Zhou et al. [6], an openloop system was utilized since the focus was not on self-sufficiency. Instead, the goal was to study

24

the four-part propagation behavior of detonation waves: (1) two-wave initiation, (2) increase of
pressure instability, (3) strong-weak wave alternation, and (4) singular stable detonation. While
all experimental studies demonstrated RDE feasibility, none focused on the interaction between
RDC and supersonic axial turbines, as was the motivation behind the numerical simulations.
Therefore, there is a need for experimental validation of the novel supersonic axial turbine designs.

Figure 1-4: Closed-cycle (top) and open-cycle (bottom) test configurations; adapted from [7].
1.1.3 Axial Bladeless Supersonic Turbines
The axial bladed supersonic turbine described in Section 1.1.21.1.2 was shown by Paniagua
et al. [22] to have high total pressure losses at the hub and shroud. In a following analysis, Vinha
et al. [23] hypothesized that the power lost to friction effects could be harnessed with an axial
bladeless turbine (Patent EP2868864A1 [24]). This turbine is analogous to Tesla’s radial bladeless
turbine (also known as a boundary layer turbine), where power is sourced from viscous drag rather
than tangential lift on an airfoil. Braun et al. [25] proposed a slight modification to the bladeless
turbine, where a helical sinusoid (or “wavy”) profile replaced the smooth profile proposed by
Vinha et al. The advantage of the wavy profile is that it can extract power from both viscous drag
and tangential lift, unlike the smooth bladeless turbine, yet it does not exhibit the large drop in
total pressure that is prevalent in a supersonic bladed turbine.

25

Computational Fluid Dynamics (CFD) simulations were performed for a base case in [26],
where the wavy profile had an amplitude-to-channel height of 10% and a 45° helix angle, and the
inlet flow had a Mach number range of 1.25-2.4 and a 0° swirl angle. A 2D profile and a 3D
contour plot of the base case are represented in Figure 1-5 [27]. To improve upon the base case,
an optimization scheme was proposed in [27]; the resulting periodic geometry had steep “ascents”
and gradual “descents” rather than a simple sinusoidal profile. In addition to steady inlet flows,
the wavy turbine may be used downstream of an RDC, as discussed in [28]. Interestingly, CFD
predicts that the wavy turbine only extracts power when the helix angle matches hub rotation—
the rotation direction of the oblique shock is not important. This numerical prediction has not yet
been validated through experiments, so additional research must be conducted.

Figure 1-5: (a) Cross-sectional view of the bladeless turbine
(b) Three-dimensional view of the turbine with the wavy hub [27].
1.1.4 Radial Bladed Supersonic Turbines
Similar to the axial turbines of Sections 1.1.2 and 1.1.3, radial supersonic turbines have
been extensively researched; these turbines may have axial inflow / radial outflow, radial inflow /
axial outflow, or (less common) radial inflow and outflow. One application of radial turbines is
the Organic Rankine Cycle (ORC), which is commonly used in waste heat recovery devices. In
ORCs, working fluids include CO2, cyclic hydrocarbons, and fluorocarbons since they allow for
transcritical or supercritical turbine inlet flow. The use of radial supersonic turbines in ORCs is
beyond the scope of this document, but further details are given in [29, 30, 31]. Instead, the

26

following information focuses on radial turbines used in RDEs. A radial-outflow turbine may be
placed downstream of an axial-flow RDC, and a radial inflow turbine may be placed downstream
of a radial-flow RDC, which is simply a flattened version of the axial-flow RDC.
In investigations by Higashi et al. [32], a single-stage radial inflow and outflow turbine
was placed around the outer diameter of a radial-flow RDC. The combustion tests resulted in a
small rise in rotational speed, but neither a true detonation nor maximum turbine performance was
realized. In experiments by Huff et al. [33], a radial-flow RDC was used to feed a radial-inflow/
axial-outflow automotive turbocharger. Here, detonations and maximum turbine performance
were achieved, but the turbine was not made for supersonic flows. Simulations performed by
Inhestern et al. [34] optimized an axial-inflow/radial-outflow turbine for both uniform supersonic
flows and unsteady RDC exhaust flows. This turbine, shown in Figure 1-6, features a unique
upstream cone to reduce shock losses at the passage inlets and damp high-frequency oscillations
from the RDC. Experimental validation of this optimized turbine is an object of future work.

(a)
(b)
Figure 1-6: (a) Top view of the optimized 3D rotor geometry
(b) flow field distortion from the RDC outlet to the rotor blade inlet [34].
1.1.5 Dynamometers
Sections 1.1.1-1.1.4 discussed the advantages of RDEs as well as a few novel supersonic
turbines designed for use in RDEs. This section focuses on a critical component of testing these
turbines: the dynamometer. In simple terms, a dynamometer is a device that either supplies power
to or absorbs power from a piece of rotating equipment. In turbomachinery, compressor testing

27

requires a power supplier, such as an engine or motor, while turbine testing requires a power
absorber, such as a brake or generator. A dynamometer creates the variations needed to assess the
test article’s performance at different operating conditions, such as efficiency or power at a given
rotational speed and mass flow rate. When a set of operating conditions has been recorded, a plot
called a performance map is created. A performance map usually consists of a two-dimensional
contour map plotted against two independent parameters on the abscissa and ordinate with isospeed lines crisscrossing the operating region; examples are shown in Figure 1-7 [35].

Figure 1-7: Example performance maps for a compressor (left) and a turbine (right) [35].
When performance is being evaluated, there are three locations at which power may be
found: (1) across the turbomachine, (2) at the dynamometer, or (3) in the shaft connecting the two.
Turbomachine measurements of mass flow rate (𝑚̇) and enthalpy (ℎ) provide the thermodynamic
power, as given by (4); shaft measurements of torque (𝜏) and rotational speed (𝜔) provide the
mechanical power, as given by (5); and dynamometer measurements provide thermodynamic,
mechanical, and/or electrical power, as discussed below. Ideally, all methods yield comparable
results, but this may not hold due to measurement uncertainties.
𝑊̇𝑡ℎ𝑒𝑟𝑚 = 𝑚̇(ℎ𝑖𝑛 − ℎ𝑜𝑢𝑡 ) = 𝑚̇𝐶𝑝 (𝑇𝑡𝑜𝑡, 𝑖𝑛 − 𝑇𝑡𝑜𝑡, 𝑜𝑢𝑡 )

(4)

2𝜋
60

(5)

𝑊̇𝑚𝑒𝑐ℎ = 𝜏𝜔 = 𝜏 ⋅ 𝑁𝑅𝑃𝑀 ⋅

28

Since this thesis focuses on supersonic turbines, the following text refers only to powerabsorbing dynamometers, which are commonly grouped into four categories: (1) hydraulic brakes,
(2) aerodynamic or air brakes, (3) induction eddy current brakes; and (4) alternating/direct current
brakes [36]. For each category, mechanical power may be obtained from shaft speed and torque,
which is measured by a strain gauge mounted on the shaft or by a load sensor mounted on the
dynamometer gimbal at a known distance (or moment arm) from the rotation axis. Hydraulic,
aerodynamic, and eddy current brakes dissipate thermal energy, while alternating/direct current
brakes dissipate electrical energy, as reviewed in [36, 37, 38, 39].
A hydraulic dynamometer uses an incompressible fluid like water or oil to absorb power;
the working principle is demonstrated in Figure 1-8. The fluid is pumped into a sealed chamber
that contains a disk or set of disks, which is connected to the turbine via a shaft. As the fluid passes
the spinning disk, viscous shear creates drag on the disk and thus a load on the turbine. Many
hydraulic dynamometer versions have been developed and are well-documented in the literature.
For example, Nikpour et al. [37] developed a water brake dynamometer for a radial inflow turbine
for an automotive turbocharger in the early 1990s. In more recent years, Naples et al. [7] used a
water brake dynamometer to test a T63 helicopter engine paired with an RDC. Banazadeh et al.
[39] created a fuzzy logic controller for a water brake dynamometer coupled with a turbine engine.

Figure 1-8: Water brake mechanism [39].

29

Aerodynamic dynamometers use a compressible fluid, usually air, to absorb power from
the turbine; these dynamometers are essentially compressors with a variable throttle valve at the
inlet or outlet. Many studies have utilized automotive turbocharger compressor impellers due to
their abundance and low acquisition cost. For example, Huff et al. [33] directed the exhaust of a
radial-outflow RDC into the turbine of a Garrett turbocharger and used the compressor to measure
the power supplied by the turbine. A Garrett turbocharger was also used in the study by Schauer
et al. [40], where the turbine was fed by the exhaust of a PDC and was metered by the compressor.
A similar procedure was again used by Rouser et al. [41]; the setup for this experiment is given in
Figure 1-9. The downside to airbrake dynamometers is that compressor operation is limited by
surge and choke, which may prevent the turbine from reaching its optimum operating conditions.

Figure 1-9: Airbrake mechanism [41].
Eddy current and AC/DC motor dynamometers do not use a working fluid to dissipate
energy. Instead, eddy current brakes generate heat with Ohmic losses, and AC/DC motors generate
electricity. In an eddy current dynamometer, a rotor has teeth along the outer diameter, like a spur
gear, and spins inside a stator with energized coils placed circumferentially around the rotor. As
the teeth pass the coils, eddy currents are induced in the coils. Since a lot of heat is produced,
Szymko et al. [38] used sub-cooled boiling to cool the system; Szymko also replaced the stator
30

windings with stationary disks beside the rotor and placed permanent magnets on the rotor disk,
as shown in Figure 1-10. In an AC/DC motor dynamometer, the rotor and stator contain windings,
permanent magnets, or both, and the turbine is braked by changing the electrical load on the motor.

Figure 1-10: Induction eddy current mechanism [38].
1.2

Research Objectives
The overarching goal of the research presented in this thesis is to advance the integration

of turbines downstream of rotating detonation combustors. To achieve this, the focus of this work
is split into three different objectives.
The first objective involves the development of a rotating detonation combustor that can
withstand long-duration tests with a light-weight cooling scheme in which air or nitrogen is used
for cooling the end walls. Many RDCs at university labs operate for a very short time (less than a
second) for diagnostic purposes. Since these tests are short, university RDCs are not usually
cooled to avoid the complexity of a cooling system. Unfortunately, due to inertia, RDCs with
turbines need to run for multiple seconds to reach a steady state condition. Uncooled RDCs would
not be able to survive, so a novel lightweight gas-cooled cooling scheme must be developed; in
propulsive applications, water or liquid cooling is not viable due to its additional weight.
The second objective involves the experimental design of supersonic turbines for RDEs.
The turbines selected for this research are the three presented in Section 1.1: the axial-inflow/
outflow bladed turbine (Section 1.1.2), the axial-inflow/outflow bladeless turbine (Section 1.1.3),
and the axial-inflow/radial-outflow bladed turbine (Section 1.1.4). Using previously generated
blade profiles, special design accommodations for manufacturability must be taken for each

31

turbine. In addition to the blade profiles, hardware such as the shroud, hub, bearings, shaft, and
instrumentation must be included in the design process.
The third objective involves the development of a low-cost experimental test stand and
dynamometer that can be used to characterize the performance of each supersonic turbine.
Furthermore, the spatial footprint of most commercial dynamometers exceeds that of the space
available for the supersonic turbine test rig. Since commercial dynamometers are not appropriate
for this case, a dynamometer must be constructed to meet the demands of speed and power, and it
must be economical for both development cost and lab space. A final requirement is that the
dynamometer must be manufactured within a reasonable timeframe; the water brakes presented in
[37] and [39] took years to develop, which is much longer than the current project’s timeline.

1.3

Research Methodology
To achieve the three objectives listed in Section 1.2, the following methodology is followed.

The first method focuses on the development of a combustor with a film-cooled jacket. Based on
previous research, the basic geometry for the cooling gas injection scheme includes three stepped
slots that inject tangentially to the combustor wall and parallel to the combustor axis. This basic
geometry is modified in the present work such that the combustor can be easily mounted on Purdue
University’s Turbine-integrated High-pressure Optical RDE (THOR). The film-cooled jacket is
3D-printed from stainless steel while the exhaust nozzle is machined from mild steel. Additional
design modifications are created such that the axial bladed supersonic turbine can be mounted to
the RDE exhaust nozzle section. Lastly, locations for placing pressure and temperature sensors on
the combustor are proposed.
The second method focuses on the experimental design of the three supersonic turbines,
the profiles of which were generated in previous numerical studies. Since each numerical study
generated a unique output file containing the blade geometry, SOLIDWORKS® Student Edition
is used to modify each turbine to be manufacturable. This includes changes to the shaft connection,
hub, shroud, and blade profiles. Some deviations from the simulated geometry are inevitable, but
all efforts to minimize these deviations are taken. Since the axial bladed turbine is designed to be
used in the cooled combustor, it is 3D-printed from stainless steel. Since the cooled combustor
cannot be easily reconfigured for the axial bladeless and radial bladed turbines, these turbines are
designed for cold-flow experiments and are made from an aluminum alloy.
32

The third objective focuses on the development of the test stand and dynamometer. As
mentioned in Section 1.2, the dynamometer must be affordable, quickly constructed, and durable
for testing at high speeds and powers. To this end, an aerodynamic dynamometer in the form of
an industrial turbocharger is selected. The turbocharger’s acquisition was accomplished through
previous PETAL students, so the remaining tasks include outfitting the turbocharger with an oil
system, installing a throttling valve on the compressor outlet, designing a shaft extension to which
a supersonic turbine can be connected, and creating a rigid mounting system for the turbocharger
and the turbine. In addition, performance maps for both the turbine and the compressor are created
from manufacturer data. After completing the three objectives with the methodology listed above,
a new system for experimentally assessing supersonic turbines in RDEs is presented.

1.4

Thesis Layout
This thesis is organized into three chapters. Chapter 2 provides details about the cooled

combustor, including CFD results from past work, Computer-Aided Design (CAD) models,
instrumentation capabilities, the 3D printing manufacturing process, and preliminary results from
a short test campaign in THOR. Chapter 3 offers insight into the turbine design modifications
from a CAD standpoint, including both the impeller alterations and the structures needed to house
the turbines; the articles that have been manufactured to date are also presented. Chapter 4 covers
the turbocharger modifications required to create an airbrake dynamometer, including the selection
of the mounting system, the bearings, the couplings, the torque sensor, and the throttle valve. In
this way, Chapters 2, 3, and 4 cover Objectives 1, 2, and 3, respectively. Chapter 5 concludes the
thesis research with notes about the current status of the project and recommendations for further
work related to supersonic turbines in Rotating Detonation Engines.

33

2

COOLED COMBUSTOR

In this chapter, the design of a novel cooling system for a Rotating Detonation Combustor
is discussed. This cooling system focuses on the combustor’s outer end wall (the shroud); the
inner end wall (the hub) remains uncooled to avoid complexities that are described in Section 2.1.

2.1

Background
Rotating Detonation Combustors (RDCs) have been numerically analyzed and tested at

universities, national labs, and industries all around the world. Most RDC research has focused
on understanding detonation wave dynamics and uncooled RDC performance. Theuerkauf et al.
[42] investigated heat flux levels within RDCs. Roy et al. [43] performed conjugate heat transfer
analyses by using periodic boundary conditions from Rotating Detonation Combustor simulations.
Braun et al. [44] investigated the convective heat flux within RDCs and found that the average
convective heat flux levels are nearly the same between the detonation front and downstream of
the triple point. However, there is still a dearth of research on the cooling of RDCs; only recently
has research focused on cooled RDCs. At the National Energy Technology Laboratory [45], a
water-cooled RDC was evaluated. At Nagoya University, Goto et al. [46] used small holes in the
combustor outer wall to cool the hollow RDC. The present research objective was to numerically
analyze and experimentally validate an RDC’s performance with hydrogen-air combustion,
nitrogen gas film cooling, and stepped axial injection cooling slots.

2.1.1 Heat Flux Estimate from an Uncooled RDC
To estimate the cooling required for the combustor, a simulation of an uncooled rotating
detonation combustor was conducted. The simulation used the software CFD++, which was
developed by Metacomp [47]. In a work by Athmanathan et al. [19], a combustor model was
created for a non-premixed hydrogen-air mixture; for this model, the fluid domain contained a
structured mesh with about 45 million cells. For the required cooling estimation, the model by
Athmanathan et al. was reused and reconfigured. The viscous sublayer was resolved to ensure that
properties in the sublayer, such as heat flux, were captured. Also, the wall temperature was set to
600 K. Figure 2-1 shows the CFD simulation results for the end wall heat fluxes. The contour

34

plots of Figure 2-1(a) and (b) depict the instantaneous heat flux on the inner and outer end walls,
respectively; it may be noted that the highest heat fluxes were located downstream of the
detonation wave. Figure 2-1(c) depicts the average heat flux along the axial direction for the inner
and outer walls; that is, the average azimuthal heat fluxes are plotted for each axial location. This
plot showed that the average of the average heat flux was around 3 MW/m2 for the region
immediately downstream of the detonation wave.

Figure 2-1: Heat flux from the uncooled combustor model at 1.2 kg/s (air + fuel):
(a) instantaneous snapshot on the inner end wall, (b) instantaneous snapshot on the outer end
wall, (c) average heat flux along the axial direction for both inner and outer end walls.
35

2.1.2 Preliminary Design Choices for the Cooled RDC
Due to the high wall heat flux levels, this rotating detonation combustor required a cooling
scheme to stay below the material’s melt temperature during continuous operation. One solution
was to use gaseous film cooling on the combustion chamber walls. While this cooling scheme is
pervasive in the subsonic deflagration combustors of most commercial turbomachinery, new
challenges were faced when designing a cooling setup for a rotating detonation combustor. If the
coolant flow through the injector was subsonic, the fluctuating pressure levels in the combustion
chamber from the detonation wave would cause the coolant pressures to fluctuate. Also, as the
detonation wave passed an injection point, the wave’s downstream pressure could push hot
combustion products into the coolant reservoir.

Exposing the combustor walls to the hot

combustion gases could lead to the combustor liner’s premature failure.
To mitigate the effects of variable combustion chamber pressure, coolant pressure could
be increased to choke the coolant flow at either the injection sites or upstream of them. Choking
the coolant flow would make the coolant flow rate insensitive to the changing pressures in the
combustion chamber. While the coolant film inside the combustor would still be influenced by
perturbations from the detonation wave, the coolant flow rate would at least remain constant during
continuous operation. It must be noted that choking the coolant flow was not an infallible construct.
Changing the coolant pressure at or upstream of the injection site had a direct effect on the blowing
ratio, which is the ratio of coolant mass flux to mainstream mass flux; this is given by (6):

𝑀=

𝜌𝑐 𝑈𝑐
𝜌∞ 𝑈∞

(6)

where 𝜌𝑐 and 𝜌∞ represent the coolant and mainstream flow densities, respectively, and 𝑈𝑐 and
𝑈∞ represent the coolant and mainstream flow velocities, respectively.
In his summary of advancements in film cooling, Goldstein [48] reviewed the results of
many previous researchers. These studies showed that for different cooling layouts, high blowing
ratios can either positively or negatively affect the film cooling effectiveness. For layouts with
coolant injection perpendicular to the mainstream, a high blowing ratio made the coolant separate
(or blow off) from the surface and prevented the desired film from forming. For layouts with
injection parallel to the mainstream, higher blowing ratios increase the film cooling effectiveness.

36

Therefore, parallel coolant injection was selected for this RDC. Next, the injector type was decided
between two injector types: (1) discrete holes, or (2) continuous concentric slots.
If the discrete holes were not close together, there would be hot spots between the holes
due to the lack of cooling at those locations. The same was true for the continuous concentric slots;
if they were not close together, there would be hot spots just upstream of each consecutive slot.
Since there were many potential patterns for discrete hole locations and fewer combinations of
continuous slot locations, continuous slots were selected for this RDC. After selecting the injector
type, the injector orientation could be selected; this was dependent on the combustor’s wall shape.
For parallel injection with continuous slots, three wall shapes were available: (1) straight, (2)
slightly conical, and (3) stepped. It was desired to expand the flow from upstream to downstream,
which indicates an increasing flow area, so the straight wall shape was eliminated.
If the walls were slightly conical, the continuous concentric slots would have to be parallel
or almost parallel to the mainstream flow direction. However, if the stepped walls were selected,
the concentric slots could be inset on each step such that no angle would be needed for parallel
injection. For a combustor setup with continuous concentric cooling slots and stepped end walls,
Goldstein described a variety of models for film cooling effectiveness [48]. One such model was
used to produce the expected maximum wall temperature as a function of the number of slots, the
slot height, the wall thickness, and the coolant pressure. The results of this analysis are in Table
2.1. Better designs have larger slot heights and smaller wall thicknesses, but larger slot heights
lead to higher coolant mass flow rates.

Thus, by balancing the maximum allowable wall

temperature and coolant flow rates, a setup with three continuous concentric slots with equal slot
heights and wall thicknesses was chosen for this cooled combustor.

Table 2.1: Maximum wall temperature for different cooling configurations.
Configuration
1
2
3
4
5
6

Number
of Slots
3
3
3
3
2
3

Slot
Height
[mm]
1
1
1
2
2
1.5

Wall
Thickness
[mm]
0.4
1
1
1
1
1.5

Coolant
Pressure
[bar]
3
3
4.15
3
3
3

37

Effect of
Wall
Thickness
0%
-25%
-25%
-15%
-15%
-20%

𝒎̇

Coolant
[kg/s]
1.228
1.228
1.699
2.413
1.617
1.823

𝑻𝒎𝒂𝒙

[K]
776
1082
1000
778
855
913

2.1.3 URANS Calculations for the Cooled RDC
As described in Section 2.1.2, a cooling mechanism with three continuous concentric slots
in a stepped combustor wall was selected for this RDC. To figure out where to place the steps in
the combustor wall, CFD++ was once again used, wherein an Unsteady Reynolds Averaged Navier
Stokes (URANS) solver was applied. To reduce the model’s complexity, the three cooling slots
were placed only in the combustor’s outer wall; the hub remained uncooled. Creating a model
for a film-cooled hub was and is possible, but it would have required more time and resources for
the project. Since the project’s goal was to build and test a cooled RDE, it was decided to forego
a cooled hub for the time being. It was also decided at the project’s initiation that the cooled
combustor would mount to Purdue University’s Turbine-integrated High-pressure Optical RDE
(THOR), which burns a non-premixed hydrogen-air mixture [49]. THOR had a modular design,
so reusing the uncooled hub in conjunction with the cooled outer body did not pose any issues.
A two-dimensional representation of the fluid domain for the initial combustor design with
three cooling slots in the outer wall is given in Figure 2-2. In Figure 2-2(a), the fluid domains for
the three cooling injection sites are represented by horizontal blue-green sections. The white
regions bordering the coolant injectors represent the combustor’s outer walls. (More details on
the wall design are covered in Section 2.2.) The gray areas at the bottom depict the fuel injection
ring and the uncooled hub retained from THOR. For the fluid domain in Figure 2-2(a), a structured
computational mesh with around 50 million cells was created in ICEM, as shown in Figure 2-2(b).
Care was taken to ensure that the viscous sublayer was resolved in the CFD simulations.

Figure 2-2: (a) Cross-section of the numerical domain, (b) structured mesh of the combustor.
38

At the domain inlet, a premixed hydrogen-air mixture was implemented; the THOR is a
non-premixed RDE, but the premixed injection scheme simplified the simulations. At the domain
outlet, downstream of the slots, a diverging section allowed the exhaust to fully expand to
supersonic flow. For the film-cooling scheme, room-temperature air selected was selected. (The
actual tests used nitrogen because of facility availability.) From initial computational results (not
included in this thesis), it was determined that the first two slots required higher coolant pressures
than the third slot since the third slot was in the transonic/supersonic combustor exhaust. After
the simulation reached a stable detonation, four snapshots of the unsteady coolant flows were taken;
these are shown in Figure 2-3 below. From 𝑇 = 0 to 𝑇 = 1⁄8 ⋅ 𝑇𝑑 (where 𝑇𝑑 = 𝑇𝑑𝑒𝑡𝑜𝑛𝑎𝑡𝑖𝑜𝑛 ), the
coolant pressures were not great enough to push coolant into the combustion chamber. However,
at 𝑇 = 1⁄4 ⋅ 𝑇𝑑 , coolant started to flow into the chamber and continued to flow into the chamber
until 𝑇 = 7⁄8 ⋅ 𝑇𝑑 , when the wave pressure overcame the coolant pressure once again.
=1 8

=

4

=1 4

=7 8

Figure 2-3: Four snapshots of the unsteady temperature in the cooled combustor.
As may be noted from the times listed in Figure 2-3, over one-fourth of a detonation cycle
was uncooled; that is, for 𝑇 = [0, 1⁄8] ⋅ 𝑇𝑑 and 𝑇 = [7⁄8 , 1] ⋅ 𝑇𝑑 , the detonation wave pressure
was greater than that of the coolant injection slots, resulting in a lack of film cooling for that
timeframe. In other words, a moving quarter of the combustor’s outer wall circumference was
always uncooled due to the rotating detonation wave’s presence. This may be explained by the
fact that the coolant flows at the injection sites were not choked. However, since the coolant mass
flows were fixed, the implication was that flow was choked somewhere upstream of the cooling

39

slots. (The need for upstream choked flow is revisited in Section 2.5.) The fixed mass flows also
implied that although coolant was not flowing into the “detonation zone”, the mass flow rate had
locally increased for the region immediately surrounding the detonation zone.
To determine if the three-slot cooling scheme was effective, a comparison was made for
the heat flux in the uncooled center hub and the cooled outer wall. This comparison is provided
in Figure 2-4, which shows heat flux as a function of axial distance in the combustor. The leftmost
point represents the premixed hydrogen-air injection site while the rightmost point represents the
combustor exhaust. As noted on the plot, there was a four-fold reduction in heat flux on the shroud
(outer wall) compared to the hub (inner wall) for the region where film cooling was present. The
heat flux on the hub was mostly constant since the hub was uncooled.

Figure 2-4: Comparison of heat flux in the axial direction for the uncooled hub (inner end wall)
and the film-cooled shroud (outer end wall).
The total coolant mass flow constituted around 30% of the core mass flow rate. As noted
previously, the coolant mass flow could not be a perfect split between the three slots; the first two
slots required more coolant mass flow because they injected the coolant around the strong
detonation, which was hotter than the transonic/supersonic exhaust. Interestingly, the film cooling
also altered the temperature profile in the uncooled expanding exhaust section, as shown in Figure
2-5 below. While the uncooled combustor simulation described in Section 2.1.1 provided an exit
temperature of 2000 K, the cooled combustor limited the exit temperature to 1500 K on average.
Despite the temperature decrease, a transonic exhaust was retained for the cooled combustor.
40

Figure 2-5: Mass flow averaged profiles of temperature (top) and Mach number (bottom).
2.2

Cooled RDC Design
Using the numerical study results, a three-slot cooled combustor jacket could be designed.

To describe every design change is not feasible for this thesis; some ideas were not well-founded
and have been omitted. For the sake of brevity, three versions are shown in the subsections below.
Section 2.2.1 reviews the cooled combustor’s initial version, which was made before the author’s
efforts toward the project. Sections 2.2.2 and 2.2.3 cover the combustor’s intermediate and final
models, respectively.

2.2.1 Initial Version
To create the three-slot film-cooled combustor, three major questions had to be answered:
(1) How would the slot walls be made? (2) How would the coolant be injected into the slots?
(3) How would the combustor be mounted to the existing THOR hardware? Regarding question
(1), there were a few ways to make the slot walls. One option was to roll 1.5-mm-thick sheets of
stainless steel (or another metal that was stable at high temperatures) into cylinders with the proper

41

radii set by the CFD simulations. This was not the best option because forming sheet metal was
not accurate to the diametral tolerance needed for the combustor, and the weld bead at the seam
would diminish the film cooling’s uniformity. To avoid the accuracy problem of sheet metal, a
second option was to turn all the slot walls on a CNC lathe. It would be expensive and difficult to
remove the material from the 1.5-mm slot channels with conventional CNC tool holders, but
another possibility was to turn each wall from a separate piece of raw material. Once all slot walls
were manufactured, they could be secured to a common base.
A third option was to 3D print the slot walls from a stainless-steel alloy. While more
expensive than sheet rolling or CNC turning, this option provided the greatest flexibility for
designing the coolant passages upstream of the slots. This led to question (2)—how would the
coolant be injected into the slots? To answer this question, two decisions had to be made. The
first decision regarded the upstream tubing orientation; the tubes had to connect to the slots either
parallel or perpendicular to the combustor axis. Ideally, the tubes would be parallel to the axis to
match the cooling injection scheme. However, as shown in Figure 2-6, the air injection ring of
THOR (the gray piece at the far left) prevented parallel tubing, meaning that the tubes had to
connect to the slots perpendicular to the combustor axis. With the tubing orientation determined,
the second decision could be considered: this involves the number of tubes for each slot.
THOR has four air tubes placed circumferentially around the air injection ring, so it was
convenient to retain this four-tube design for the coolant tubes. Ideally, four tubes would connect
to each slot such that coolant gas composition, pressure, or temperature could be varied for each
slot. However, it would be difficult to route three tubes at the same circumferential location into
the small axial distance separating each slot. Therefore, it was decided to route the tubing to two
chambers (or plenums) upstream of the three slots. Four tubes would connect to Chamber 1 and
another four tubes would connect to Chamber 2. Since the first two slots were axially close
together and required more mass flow than the third slot, the first two slots were connected to
Chamber 1 while the third slot was connected to Chamber 2. In the isometric view of Figure 2-6
below, the outer walls of Chambers 1 and 2 are represented by blue-gray and aqua, respectively.
In the side cutaway view, the Slot 1 and 2 inner walls are represented by light green, and the Slot
3 inner wall is represented by aqua.
Question (3) for the cooled combustor design was about mounting the combustor on the
existing THOR hardware. For the initial design, it was thought that the most cost-effective solution

42

could be obtained through a combination of CNC-machined and 3D-printed parts. In this way, the
Chamber 1 outer wall was designed to be CNC-machined, and the walls of Slots 1 and 2 were
designed to be 3D-printed as one piece on a direct metal laser sintering (DMLS) apparatus. To
ensure that flow between Slots 1 and 2 was balanced, a unique hole pattern was implemented in
the Slot 2 inner wall; the holes were converted from circles to teardrops with a maximum overhang
angle of 45° to avoid the need for printing support material inside the hole. Since Chamber 2 was
connected to only Slot 3, the two were designed to be CNC-machined from a single piece of
stainless steel. The final combustor component was the flange, shown in pink in Figure 2-6, that
clamped the chamber and slot walls to THOR’s air injection ring. This flange would be turned on
a CNC lathe from mild steel since the exhaust temperature was projected to be low.
Since the slot walls had a thickness and separation distance of only 1.5 mm each, there
were concerns that thermal and mechanical stresses on the slot walls would cause permanent
deformation. To give extra support to the slot walls, eight ribs were added at 45° increments
around the combustor. These extended from the slot wall exteriors to the chamber wall interiors
and created eight separate mini sectors within each chamber. The ribs were indexed to align with
the tube connection ports, and a break was instituted in each rib that coincided with the tube
connection ports. This ensured that flow from each tube would be halved into two 45° mini sectors;
put another way, each tube fed a 90° sector of each chamber. These ribs are shown in Figure 2-7
below. The top image contains a section view set at 0° to the front plane and shows the broken
ribs around the tube connection ports; the bottom image contains a section view set at 45° to the
front plane and shows the unbroken ribs that separate the four 90° sectors.
There were three main issues with this initial combustor design. The first issue was the
lack of self-centering features on the slot and chamber walls, which means that it was difficult to
ensure all walls were concentric. If the slot walls were not aligned, the film coating would not
have a uniform thickness, leading to decreased cooling efficacy. The second issue was the absence
of alignment pins for the 3D-printed part containing the walls for Slots 1 and 2. This opened the
possibility for the 3D-printed part to become misaligned from the Chamber 1 outer wall and the
tube ports. If the ports were not aligned above the broken ribs, then the flow would not be evenly
distributed in the sectors, leading to decreased film cooling effectiveness yet again. The third issue
was that the mating surfaces between the chamber walls did not allow enough room for the O-ring
glands. All three issues had to be fixed, leading to an intermediate design.

43

Figure 2-6: Isometric and side cutaway views of the initial combustor design.

Figure 2-7: Side section views of the initial combustor design.

44

2.2.2 Intermediate Version
For the cooled combustor’s intermediate design, the configuration of slot and chamber
walls was retained from the initial design; that is, Chamber 1 still fed Slots 1 and 2, and Chamber
2 fed Slot 3. The main update came in the form of a new combination of 3D-printed and CNCmachined parts. The walls for Slots 1 and 2 were merged with the outer wall of Chamber 1 such
that the all walls could be 3D-printed as a single piece of stainless steel. Merging these pieces
came as a recommendation from the 3D printing manufacturer; having the slot walls 3D-printed
and the chamber wall machined had the same cost as printing a single piece. In addition, the single
piece avoided the previously mentioned alignment issue, in which the slot ribs could become
misaligned from the tube connection ports. (More on the cooled combustor manufacturing is
covered in Section 2.4.) The merged component consisting of the walls for Chamber 1 and Slots
1 and 2 is shown in light green in Figure 2-8 below.
Aside from combining the upstream chamber and slot walls, a few other features were
altered. First, the teardrop holes in the Slot 2 inner wall were lengthened to allow more flow from
Chamber 1 into Slot 1; the initial teardrop pattern did not have enough passage area for flow
entering Slot 1. Second, the number of supporting ribs between the chamber and slot walls was
reduced from eight to four. Four ribs offered sufficient support, so the broken ribs around the tube
holes were removed. Third, the chamber wall thickness was decreased from 8 millimeters to 5
millimeters to reduce the part’s printing time and overall weight. Unfortunately, reducing the
chamber wall thickness also reduced the available material for tube fitting thread engagement by
almost half. This led to the fourth revision, which was the addition of conical extrusions to the
outside walls of each chamber. Just like the teardrop holes, these conical extrusions had maximum
overhang angles of less than 45° to avoid the need for support material.
A fifth revision was the introduction of instrumentation probe holes in the chamber's outer
walls. To determine the film cooling effectiveness during a hot RDE test, the chamber pressures
and temperatures had to be measured; these parameters were also desired for the flow in the slots.
To accomplish this, six probe holes were created for each 90° sector—two probe holes per slot—
and each six-hole group was separated between two circumferential locations within each 90°
sector. The two final revisions were to increase the O-ring seal surface area between the chamber
walls and to reorient the optical access window in the flange for manufacturability. Apart from
the seven revisions, the main combustor geometry was retained from the initial design. The

45

location and size of the slots and slot walls were retained, and the supersonic exhaust angle was
held at 12.5°. Also, the walls for Chamber 2 and Slot 3 remained as a single part; both this part
and the clamping flange were still to be CNC-machined. The intermediate combustor design is
shown in Figure 2-8 and Figure 2-9.
Despite the revisions presented above, the intermediate design faced a few issues. Just like
the initial design, slot wall concentricity was not guaranteed since the slot walls were not all mated
to the same part. Also, tube fittings in this design were 1” double-ferrule Parker A-Lok fittings
with SAE 1-5/16” x 1 straight threads, which were too large for the small axial distance in which
they were placed. Routing 1-inch tubes to these fittings would be difficult due to the limited access
to tubing tools. A third issue was the use of face-seal O-ring grooves; users of THOR’s other
configurations provided their experience about how face-seal O-rings would frustratingly fall out
in the assembly process. A final issue was the placement of instrumentation holes; each sector had
two rows of three ports, and one row was too close to the tube connection ports, which might have
biased the measurements. These issues were fixed for the final combustor design.

46

Figure 2-8: Isometric and side cutaway views of the intermediate combustor design.

Figure 2-9: Side section views of the intermediate combustor design.

47

2.2.3 Final Version
After fixing the issues that pervaded the intermediate combustor design, a final design was
reached. The main improvement was that the part containing the Chamber 2 and Slot 3 walls was
combined with the part containing the walls of Chamber 1, Slot 1, and Slot 2; this part was designed
to be 3D-printed as one piece. The reason behind this was to lower the cost; printing one part and
machining the other cost about 1.5 times the cost of printing the combustor as a solid piece. This
also fixed the concerns regarding the slot concentricity; barring a disfiguration from the large heat
transfer, the slots would always be concentric and aligned with each other. Another design
modification included reducing the coolant tube size from 1” to ½”. This came about because the
coolant mass flows were not high enough to warrant the use of such large tubing. (Details about
the mass flows are provided in Section 2.5.) This size reduction conveniently provided additional
room for the tube fittings and the tools required to secure the fittings.
A third improvement was to exchange the face-seal O-rings glands for concentric-seal
glands. One O-ring was removed when the chamber and slot walls were combined in one 3Dprinted part, leaving just one O-ring seal between the 3D-printed part and the CNC-machined part
containing the mounting flange and the diverging exhaust section. This seal was changed to have
the same gland dimensions as those given by the air injection ring of THOR for convenience. A
final improvement was changing the instrumentation probe holes in the chamber walls. These
were placed at more reasonable circumferential positions between the tube fitting sites and the
support ribs. In addition, the through holes were replaced by SAE 5/16” x 4 threaded holes
intended to be used by 1/8” or 1/16” double-ferrule Parker A-Lok fittings. The final combustor
design is shown in Figure 2-10 and Figure 2-11 below. Mechanical drawings for the final 3Dprinted and CNC-machined parts are provided in Appendix A.

48

Figure 2-10: Isometric and side views of the final combustor design.

Figure 2-11: Side section views of the final combustor design.

49

2.3

Cooled RDC Instrumentation
To determine the film cooling effectiveness for the combustor’s outer end wall, a unique

instrumentation setup was required. This setup is depicted in Figure 2-12 and includes probes
placed in the coolant chambers and slots as well as in the diverging supersonic exhaust section. In
the proceeding text, the cooled section probe locations are discussed first, followed by the
uncooled exhaust section probe locations.

Figure 2-12: Isometric and side section views of the combustor probe fittings and stators.
The cooled combustor’s final design included 24 threaded ports in the coolant chamber
walls, which were separated into two groups of three ports for each 90° sector of the combustor.
The axial probe locations were determined by placing the holes as close to the slot openings as
possible while leaving enough room between the fittings for quick installation. The azimuthal or
circumferential locations depended on the teardrop hole locations in the wall separating Slots 1
and 2. Four teardrops were placed in each 90° sector with equal separation distance. The teardrop
midlines were located at ±11.25° and ±33.75° relative to the tube fittings, and the walls separating
the teardrops were located at 0°, ±22.5°, and ±45° to the tube fittings. The ±11.25° midlines and
0° walls were unusable due to their proximity to the tube fittings, and the ±45° walls had ribs
intersecting them. This left only the ±33.75° midlines and ±22.5° walls.

50

To measure quantities in Slot 1, the probes could either go through the teardrop midlines
at ±33.75° or the teardrop separation walls at ±22.5°. To better reflect the conditions in Slot 1, it
was decided to go through the walls at ±22.5°; the midlines may not measure the pressure drop as
the flow enters Slot 1. To measure quantities in Slot 2, the probe hole could be placed at any
location between the tube fittings and the support ribs, but the holes were set to coincide with the
teardrop vertices at ±22.5°. The same could be said for Slot 3; the azimuth location was not
necessarily a concern, so the probes were set to match the locations for the Slot 1 and 2 probes.
Therefore, from the perspective of looking downstream to upstream, the first group of three ports
was indexed at -33.75° (counterclockwise) from the tube fitting locations while the second group
was at +22.5° (clockwise) from the tube fittings. These locations are depicted in Figure 2-13; the
Slot 1 probes +22.5° at are denoted by the red-colored conical extrusions, and the other graycolored conical extrusions denote the possible locations for the Slot 2 and 3 probes.

Figure 2-13: Isometric and cutaway views of the probe holes in the film-cooled section.
Moving on from the film-cooled section, the supersonic exhaust had the instrumentation
ports shown in Figure 2-14. Five equidistant axial locations were selected to generate the wall
temperature and pressure profiles along the region in which the axial bladed turbine would reside.
(See Section 3.1 for the axial bladed turbine geometry.) A window was cut into the diverging
section across the same axial span as the five probe holes to provide optical access to the turbine.
If the spark plug pre-detonator did not function properly, the window could also be used to route

51

a focused laser beam into the RDC exhaust; the laser beam would ignite a deflagration that would
propagate upstream as a detonation. The third type of probe present in the exhaust section was the
dual-use flow straighteners or stator vanes. The primary use was to dampen the rapidly fluctuating
turbine inlet conditions and potentially increase the turbine power consumption. The secondary
use was to house small pressure probe holes at different chord and spanwise locations; from these
measurements, a pressure contour map of the turbine inlet flow could be created.

Figure 2-14: Isometric and cutaway views of the holes in the uncooled exhaust section.
A diagram of the flow straighteners is provided in Figure 2-15. The 2D blade profile was
created from a NACA 0030 profile; this profile was extruded to the THOR hub and the flanged
diverging exhaust section. The axial chord and the maximum height at the trailing edge were each
approximately 25 millimeters, the blade width was approximately 7 millimeters, and the mounting
holes had SAE #4-40 threads. Since the stators were so small, there was not much room on the
blade tips for the connections to the external pressure transducers. To conserve space, the probe
holes were connected to the bottoms of the threaded screw holes. For the initial tests, both screws
were used for each stator to prove that the stators would survive hot RDE tests. Once the stators
were proven, future tests would replace one screw—either the upstream (leading) or downstream
(trailing) screw—with a stainless-steel tube to connect the probe hole to a pressure transducer. If
the one-screw system did not appear safe, then high-temperature epoxy would be added between
the blade tip and shroud for extra reinforcement.

52

Because there were eight flow straighteners with two screw holes each, there were sixteen
opportunities for pressure measurement. The different chord and span locations were decided on
a percentage scale; the holes were placed at 0%-100% of the chord in 20% increments and at 40%
to 70% of the span in 10% increments. The probe hole combinations are given in Table 2.2 below;
the blade side is listed with respect to the turbine, which spins clockwise from the perspective of
downstream to upstream. Figure 2-16 shows the stator’s top view and the chordwise probe hole
locations; Figure 2-17 shows the stator’s a side view and the spanwise probe hole locations. To
achieve these intricate probe hole features, the stators were 3D-printed like the cooled combustor.

Figure 2-15: Diagrams of the flow straightener features.

Table 2.2: Flow straightener configurations.

Stator
Number
1
2
3
4
5
6
7
8

Probe Hole 1: Leading/Upstream
Blade Side
Chord
Span
w.r.t.
Position
Position
Turbine
(%)
(%)
N/A
0
50
N/A
0
75
N/A
100
40
Suction
20
50
Suction
40
50
Suction
40
70
Suction
60
50
Suction
80
50
53

Probe Hole 2: Trailing/Downstream
Side of
Chord
Span
Blade w.r.t.
Position
Position
Turbine
(%)
(%)
N/A
0
40
N/A
0
25
N/A
100
50
Pressure
20
50
Pressure
40
50
Suction
40
30
Pressure
60
50
Pressure
80
50

Figure 2-16: Top view diagram for the probe locations of the eight flow straighteners.

Figure 2-17: Side view diagram for the probe locations of the eight flow straighteners.

54

2.4

Cooled RDC Manufacturing
The vendor for 3D-printed pieces was Innovative 3D Manufacturing in Franklin, IN. The

printed pieces included the merged part for the combustor’s slot and chamber walls and the eight
flow straighteners. All 3D-printed pieces were made from stainless steel alloy 316L since this
offered superior corrosion resistance compared to mild steel at a more affordable price than a
superalloy such as Inconel. Mechanical drawings for the printed pieces are given in Appendix A.
Figure 2-18 below shows the cooled combustor model sent to the printer; the teardrops in the tube
ports and probe holes avoid the need for support material. Figure 2-19 shows the support material
added to the flow straighteners during the print; this material was removed after tapping the probe
holes. Figure 2-20 shows a few images from the combustor’s printing and post-print machining
processes, and Figure 2-21 shows an image of the finalized flow straighteners.
The vendor for the CNC-machined pieces was Logo 2 Manufacturing in Alicante, Spain.
The machined pieces included the combustor’s diverging exhaust flange and the optical window
insert. Since the uncooled exhaust temperatures were not projected to be as high as those in the
cooled section, the flange was machined from a mild carbon steel alloy, and the window insert was
machined from aluminum alloy 7075. A quote was procured for both pieces machined from
stainless steel, but this was more than the project budget could afford. Mechanical drawings for
the machined pieces are provided in Appendix A. Figure 2-22 shows a few images of the pieces
during and after manufacturing, including two pictures of the flange on the 3D-printed combustor.

Figure 2-18: Isometric and side views of the cooled combustor model for the 3D-printer.
55

Figure 2-19: Diagrams of the flow straighteners with the 3D-printed support material in red.

Figure 2-20: Four views of the cooled combustor manufacturing process: (a) at the beginning of
the print, (b) at the end of the print, (c) after the threads and O-ring surfaces are machined, and
(d) after the innermost slot wall is machined.

56

Figure 2-21: Image of the eight flow straighteners after post-print machining.

Figure 2-22: Five views of the uncooled exhaust flange manufacturing process: (a) the flange
after initial CNC lather operations, (b) the completed flange, (c) the completed window insert,
(d) the outside of the stacked combustor, and (e) the inside of the stacked combustor.

57

2.5

Cooled RDC Coolant Tubes
The film cooling gas was set as nitrogen in the combustor design’s initial stages. Injecting

the nitrogen into the film cooling slots required two components: (1) a choked-flow venturi to
meter the coolant mass flow rate entering each chamber, and (2) the tubing to connect the venturi
to the 3D-printed combustor. In the following subsections, the design process for the nitrogen
tubing is reviewed. Section 2.5.1 describes coolant mass flow rates required by the combustor,
Section 2.5.2 reviews the tubing design, and Section 2.5.3 details the manufacturing of the stainless
steel tubing for the film-cooled combustor.

2.5.1 Calculated Mass Flow Rates
In Section 2.1, it was noted that each injection slot would ideally be choked to prevent the
backflow of combustion products into the cooling slots, but since this would require a very high
coolant mass flow rate, the coolant slots did not have choked flow. Instead, the flow was choked
upstream of the cooling slots such that the coolant mass flow rates remained constant; the backflow
of some combustion products was of lesser concern. The desired mass flow rates were based on
the CFD simulations that had transonic/supersonic flow upstream of the axial bladed turbine; these
are listed in Table 2.3. To choke the flow upstream of the coolant slots, it was convenient to use
two cavitating venturis with inner diameters of 0.1 4” and 0.1 3” in the lines feeding Chamber 1
(Slots 1 and 2) and Chamber 2 (Slot 3), respectively. These cavitating venturis both had a
discharge coefficient, 𝐶𝑑 , of 0.993; this value was used in the following calculations.
A venturi has two important locations: (1) the throat or orifice, and (2) a point immediately
downstream of the throat. Since the orifice has choked flow, the choked mass flow rate is found
by setting the Mach number to unity (𝑀 = 1) in the compressible mass flow rate expression (7)
and then reducing to achieve (8). The venturi throat total pressure, 𝑝01 , is found by using the
desired coolant mass flow rate, assuming a total temperature (𝑇0 ) of 300 K, and rearranging (8).
The total pressure immediately downstream of the throat, 𝑝02 , may be found by combining the
equations for the venturi discharge coefficient (9) and the ideal gas law (10) Downstream of the
venturi, the total pressure should only be a little less than 𝑝02 due to pressure loss, but at some far
downstream point, such as the coolant chamber or slots, the total pressure will no longer match
𝑝02 due to the detonation wave pressure overcoming the unchoked coolant slot pressure.

58

−(𝛾+1)

𝐴 ∙ 𝑝0

𝛾
𝛾 − 1 2 2(𝛾−1)
𝑚̇ =
∙ √ ∙ 𝑀 ∙ (1 +
𝑀 )
𝑅
2
√𝑇0
−(𝛾+1)

𝐴 ∙ 𝑝0

𝛾 1 + 𝛾 2(𝛾−1)
)
𝑚̇𝑐ℎ𝑜𝑘𝑒𝑑 =
∙√ ∙(
𝑅
2
√𝑇0
𝐶𝑑 =

(7)

(8)

𝑚̇
𝐴 ∙ √2 ⋅ 𝜌01 ⋅ (𝑝01 − 𝑝02 )
𝑝0
𝜌0 =
𝑅 ⋅ 𝑇0

(9)
(10)

Using the above procedure, a set of venturi throat and discharge pressures were found for
the nitrogen coolant mass flow rates that produced transonic/supersonic flow upstream of the axial
bladed turbine in the CFD simulations. In the simulations, two mass flow rates were selected for
the reactants (air and hydrogen): 1.0 lbm/s and 2.0 lbm/s. For each reactant mass flow rate, there
was a range of nitrogen coolant mass flow rates that produced the desired transonic/supersonic
flow. For example, for a reactant mass flow rate of 1.0 lbm/s, the upstream and downstream
chamber coolant mass flow rates could be 0.1-0.3 lbm/s and 0.1-0.2 lbm/s, respectively. For a
reactant mass flow rate of 2.0 lbm/s, the upstream and downstream chamber coolant mass flow
rates could be 0.3-0.4 lbm/s and 0.2-0.3 lbm/s, respectively. While the coolant mass flow rates
were close to each other, the pressures varied widely. The upstream chamber venturi throat
pressures varied from 370 psi to 1470 psi, and the downstream chamber venturi throat pressures
varied from 370 psi to 1120 psi. All pressures and mass flow rates that were used in the RDC test
campaign are listed in Table 2.3 below.

Table 2.3: Nitrogen coolant mass flow rates and total pressures at the venturi throat (𝑝01 ) and the
venturi exit (𝑝02 ) for the two venturis across a selection of reactant mass flow rates.
𝑚̇𝐴𝑖𝑟 + 𝐻2
(lbm/s)
1.0
1.0
1.0
2.0
2.0

Venturi 1 (for Chamber 1)
𝑚̇𝑁2
𝑝01
𝑝02
(psi)
(psi)
(lbm/s)
0.1
368
268
0.2
736
537
0.3
1104
805
0.3
1104
805
0.4
1472
1073

59

Venturi 2 (for Chamber 2)
𝑚̇𝑁2
𝑝01
𝑝02
(psi)
(psi)
(lbm/s)
0.1
374
273
0.2
748
545
0.2
748
545
0.2
748
545
0.3
1122
818

2.5.2 Tube Design
One design change listed in Section 2.2 was to decrease the tube size from 1” to ½”. This
provided greater access to the fittings on the 3D-printed combustor, and it also provided more
flexibility in designing the tube routing. Since the two chambers were each separated into four
90° sectors, four nitrogen tubes were required for each chamber. Using eight separate nitrogen
lines was not feasible, so a “tube tree” model was used. Downstream of each cavitating venturi,
the tube entered a ½” tee, which created two additional ½” branches. Then, the same technique
was replicated to create the four tube branches needed for each coolant chamber. In this way, six
total ½” tees were used to split the two venturi exit lines into the eight lines for the combustor.
The next step was to design the tube paths around the existing hardware on THOR.
The tube paths were generated with 3D sketches in SOLIDWORKS; the sketch profiles
contained lines representing the straight sections and arcs to represent the 1.5” bend radius for ½”
tubing. The paths were manipulated until they resembled a “tube tree” beginning with one ½”
tube and ending with eight ½” branches. After verifying that the “tube tree” model would update
correctly for dimension changes, the model was imported into the assembly containing the THOR
test stand. Then, the tube lengths and curve angles were altered until there was no interference
with the existing THOR hardware. The final tube design is shown in Figure 2-23 and Figure 2-24,
and the tube lengths are tabulated in Table 2.1. Additional dimensions for each tube section may
be found in the tube mechanical drawings in Appendix B.
Two comments may be made about the final design. First, only one high-speed run valve
was available for the nitrogen lines (the other valves were reserved for fuel, air, etc.), so the plan
was to connect one nitrogen line to this valve and the other nitrogen line to a low-speed valve on
the test cell’s nitrogen panel. However, this plan changed a bit, as described in Section 2.6.
Second, the initial combustor testing used THOR’s existing pre-detonator assembly, which
directed a spark-induced detonation wave into the rotating detonation combustor via the center
body. For future testing with the axial bladed turbine, the center body pre-detonator would be
removed to make way for the shaft, and the pre-detonator tube would be mounted to the exhaust
flange. More details on the axial bladed turbine are in Section 3.1.

60

Figure 2-23: Isometric views of the combustor and tubing on the THOR stand.

Figure 2-24: Isometric view of the tubing CAD; Sections 1-1 through 1-7 (in blue) were routed
into Chamber 1 and Sections 2-1 through 2-7 (in green) were routed into Chamber 2.

61

Table 2.4: Tube lengths; Sections 1-1 through 1-7 were routed into Chamber 1,
and Sections 2-1 through 2-7 were routed into Chamber 2.
Section #
1-1
1-2
1-3
1-4
1-5
1-6
1-7
2-1
2-2
2-3
2-4
2-5
2-6
2-7

Overall Length
(ft)
(in)
5.11
61.18
2.89
34.70
2.89
34.70
1.60
19.17
1.60
19.17
1.60
19.17
1.60
19.17
4.34
52.05
3.09
37.10
3.09
37.10
2.10
25.20
2.10
25.20
2.10
25.20
2.10
25.20

2.5.3 Tube Manufacturing
Using the design presented in the last section, the tubes could at last be bent, cut, and fitted.
Since the nitrogen pressures were low, ½” tubing with a wall thickness of 0.049” was selected.
Conveniently, there were many short sections of ½” x 0.049” tubing leftover from other projects
in the fabrication shop, so no 0’ sections had to be cut for this project. These short pieces are
shown in the top image of Figure 2-25; the longest piece was around 5’ long and the shortest was
around ’ long. Each piece was marked with the straight section lengths and bend arc lengths
stipulated by the drawings in Appendix B, and the bends were created by hand with a Swagelok
bending tool with a 1.5” bend radius.
In the design process, care had been taken to have primarily 90° bends in the standard
Cartesian planes; as opposed to non-perpendicular bends, the 90° bends were easy to check with a
carpenter’s speed square. Only a handful of 30° and 45° bends were in the design, but these were
the “last” bends in each section, meaning it was okay if they were inaccurate to about ±5. After
the tubes were bent to the proper angles, the extra material on either end was removed with a chop
saw for stainless steel. Next, recently cut sections were deburred and cleaned with isopropanol.
Finally, the tubes were fitted and trimmed until a well-fitting assembly was achieved. The bent
and assembled tubes are shown in Figure 2-25 and Figure 2-26, respectively.

62

Figure 2-25: Images of the tube sections before (top) and after (bottom) bending.

Figure 2-26: Image of the nitrogen coolant tubes assembled on the combustor.
2.6

Cooled RDC Integration with THOR
With most of the tubes bent and fitted, the cooled combustor could finally be mounted on

the THOR stand. As mentioned in Section 2.5.2, the original plan had been to connect one nitrogen
line to the extra run valve on the THOR stand’s side and the other nitrogen line to a low-speed
valve on the test cell’s nitrogen panel. This plan changed slightly such that both nitrogen lines
63

were connected to low-speed valves on the nitrogen panel. Using these valves meant that they had
to actuate before pre-detonation, but this posed no issue. The mounted combustor is shown in
Figure 2-27, which uses red, blue, and green arrows to denote the air tubes, the nitrogen tubes for
Chamber 1 (Slots 1 and 2), and the nitrogen tubes for Chamber 2 (Slot 3), respectively.
After connecting the tubing to the venturis, it was time to instrument the combustor. Here,
it may be useful to reference the probe hole location and design decisions provided in Section 2.3.
The instrumentation used for the initial combustor test campaign is shown in Figure 2-28, and a
size comparison between the RDE stand and the author is provided in Figure 2-29. For the cooled
combustor section, three thermocouples (TCs) and three pressure transducers (PTs) were installed
into the ports corresponding to Slots 1, 2, and 3 (abbreviated as S1, S2, and S3, in the figure). For
the uncooled exhaust section, five probes were installed in the holes along the combustor axis:
three pressure transducers alternated with two thermocouples. The probe’s frequency response
was less than 5 kHz, which meant that a detonation wave traveling at anything above 2 kHz would
not be resolved. While the ideal setup would capture pressure and temperature fluctuations
between each wave cycle, the 5 kHz probes were acceptable for the initial tests.

Figure 2-27: Images of the nitrogen tubes leading into the cooled combustor.

64

Figure 2-28: Images of the cooled combustor instrumentation.

Figure 2-29: Image of the author standing next to the cooled RDC mounted on the THOR stand.

65

2.7

Cooled RDC Test Results
Once the pressure probes and thermocouples had been installed, the cooled RDC could

finally be tested with the reactant and nitrogen coolant mass flow rates given in Table 2.3 above.
The average test lasted about ten seconds, with detonation combustion lasting only two seconds in
that time; the initial and final few seconds were reserved for pre-detonation ignition and a nitrogen
purge in the coolant slots. Between each test, air was purged through the RDC to cool the uncooled
center body for about ten minutes. While waiting on the cooldown, the hardware was checked for
heat warpage or other damage, but only some surface rust and discoloration were reported on the
uncooled exhaust flange. A glimpse of the flange before and after the test is shown in Figure 2-30
below. Although not shown, no discoloration was found on the film-cooled combustor.
For each test, a Phantom high-speed camera operating at 100 kHz was used to determine
the type of detonation waves in the RDC. Throughout the test matrix, several wave modes were
observed depending on the reactant and coolant mass flow rates. The test with the highest flow
rates had 2 lbm/s of reactants and 0.7 lbm/s of coolant; in this test, a single rotating wave was
observed. This wave is shown in Figure 2-31; the top row shows the raw images and the bottom
the same images with annotated circles showing the wave rotating direction.

Figure 2-30: Images of the exhaust flange before and after testing.

66

Figure 2-31: Phantom Camera images of the detonation wave for the highest mass flow test.
After completing the test matrix, the dataset was analyzed to determine the film- cooling
effectiveness. Figure 2-32 depicts the cooling slot temperatures for the maximum mass flow rate
test with 2 lbm/s of reactants and 0.7 lbm/s of coolant; cooling slot temperatures did not exceed
310 K during this two-second test. Figure 2-33 depicts the cooling slot temperatures for two tests
with and without cooling; both tests had a 1 lbm/s reactant flow rate and a duration of 0.5 seconds.
In the uncooled test, the first and second slots reached temperatures of 490 K and 560 K,
respectively; in the cooled test, all slots remained below 310 K. Although not shown, longer tests
at this mass flow had a similar result; all slot temperatures remained below 320 K. Therefore, the
film-cooled combustor’s preliminary test campaign showed that the three-slot cooling scheme was
effective at limiting the temperature rise in the coolant slots. The combustor’s success meant that
film-cooling is a viable option for implementing RDCs in turbomachinery.

67

Figure 2-32: Cooled slot temperatures for a reactant mass flow rate of 2 lbm/s.

Figure 2-33: Cooled and uncooled slot temperatures for a reactant mass flow rate of 1 lbm/s.

68

3

SUPERSONIC TURBOMACHINERY

In the literature review of Section 1.1, three novel supersonic turbines were conceptualized
in the context of past research. Section 1.1.2 described the axial bladed turbine and the challenges
associated with placing a turbine in the fluctuating supersonic exhaust of a rotating detonation
combustor. Section 1.1.3 established the axial bladeless turbine as an alternative to the bladed
turbine in that it can extract power from the flow without the large pressure drop associated with
shock losses. Section 1.1.4 provided details about axial-inflow/radial-outflow turbines and their
potential for supercritical CO2 cycles as well as the exhaust of a rotating detonation combustor.
This chapter is separated into three sections corresponding to the three supersonic turbines. Each
section begins with a background on the current research, including applications and progress
completed before the author’s work. Each section then transitions to the mechanical design of the
turbine impeller and the supplemental hardware needed for successful testing.

3.1

Axial Bladed Supersonic Turbine

3.1.1 Background
One important milestone in the project that funded the film-cooled combustor’s design,
manufacture, and test was the development of an axial bladed turbine that could be mounted in the
film-cooled combustor’s diverging exhaust section. From the URANS CFD simulations of Section
2.1.3, the film-cooled combustor was shown to have a transonic to supersonic exhaust. Using the
simulation results, an axial bladed turbine could be optimized for transonic to supersonic flow. To
do this, students at the Purdue Experimental Turbine Aerothermal Laboratory (PETAL) developed
a MATLAB routine to generate blade profiles based on inputs such as steady-state speed, inlet
total temperature and pressure, blade chord and height, and hub dimensions. A full list of inputs
is available in Table 3.1. Several blade geometries were generated with the MATLAB code, but
the geometry parameters in Table 3.1 are listed for only three turbines; the main difference between
these turbines is the number of blades. After creating the blade profiles, a 3D preview was made
for an impeller with the routine’s blade and hub profiles. The 3D plots for the three turbines listed
in Table 3.1 are given in Figure 3-1.

69

Table 3.1: Inputs for the MATLAB script that generated the three initial turbines.
Parameter
# Blades
Speed (kRPM)
Chord (cm)
Height (cm)
Thickness / Chord (-)
Pitch / Chord (-)
Hub Radius at Inlet (mm)
Hub Radius at Outlet (mm)
Tip Radius (mm)
Inlet Velocity (m/s)
Inlet Mach Number (-)
Inlet Total Temperature (K)
Inlet Total Pressure (bar)
Inlet Flow Angle (°)

Turbine 1
13
50
1.5
2.94
0.15
1.53
47.39
38.64
76.82
1319
1.7
1950
6.02
0

Turbine 2
10
50
2.0
2.94
0.15
1.49
47.39
38.64
76.82
1319
1.7
1950
6.02
0

Turbine 3
8
50
2.5
2.94
0.15
1.49
47.39
38.64
76.82
1319
1.7
1950
6.02
0

Figure 3-1: Three initial axial bladed turbine designs: (from left to right) a thirteen-blade design,
a ten-blade design, and an eight-blade design.
The axial bladed turbine’s final iteration contained eight blades and a 20-mm chord; the
profile for this turbine is shown in Figure 3-2. The next step was to estimate the power extraction
for this turbine. This was completed using two different methods: the first used 1D isentropic flow
equations, and the second used a 2D CFD solver. Except for the 20-mm chord, the inputs for each
analysis were the same as those provided in Table 3.1. The 1D isentropic analysis is not shown

70

here, but it showed that the maximum work output for a turbine with no losses was approximately
146 kW. The 2D CFD analysis was closer to reality, for its work estimation was 72 kW. A
snapshot of the Mach contour in the blade passage produced by the CFD simulation is provided in
Figure 3-3 below. In this figure, a bow shock is visible at the blade’s leading edge, as is expected
for all turbine blades in supersonic flow.

Figure 3-2: Blade profile of the axial bladed turbine.

Figure 3-3: Mach number contour for an axial bladed turbine operating in supersonic flow.
71

3.1.2 Impeller Design
After showing that the eight-blade turbine could extract a viable amount of work from the
supersonic RDC exhaust flow, the next step was to import the blade profile given in Figure 3-2
above into SOLIDWORKS to create a model that could be manufactured. The blade tips were
trimmed to match the diverging exhaust flange’s 12.5° profile; the leading and trailing tip radii
were 83 mm and 85 mm, respectively. The converging hub profile of the THOR center body was
extended for the turbine hub profile; this produced a conical solid body with leading and trailing
edge diameters of 106 mm and 94 mm, respectively, and a thickness of 30 mm. This initial hub
did not have a hole for the shaft, and it was much too thick; the overly large rotational moment of
inertia would decrease the turbine’s ability to achieve its optimum speed. Therefore, the hub was
modified to have a 12-mm shaft hole with two 3-mm shaft keyways separated by 180°. The hub
thickness was reduced from 30 mm to 12.5 mm for an area extending from the shaft hole to about
10 mm offset from the blade roots. The final turbine design is shown in Figure 3-4 below, and a
mechanical drawing of this turbine is provided in Appendix C.

Figure 3-4: Downstream (left) and upstream (right) views of the axial bladed turbine.
The axial bladed turbine was 3D-printed concurrently with the film-cooled combustor and
flow straighteners at Innovative 3D Manufacturing in Franklin, Indiana. The material for the
turbine was the same as the combustor: stainless steel alloy 316L. A stronger material might have
been selected, such as a superalloy like Inconel, but this was overly expensive for the project
72

budget. As noted for the combustor and flow straighteners, a material with appropriate strength
and corrosion resistance at high temperatures was desired, and the most economical material that
fulfilled these demands was stainless steel. The printed turbine is shown in Figure 3-5; the grainy
texture is a remnant of the sintering process and could be removed with additional CNC machining.
One note about the turbine is that, as of the writing of this thesis, the turbine had not been balanced,
but this would be accomplished in the project’s next phase.

Figure 3-5: Downstream (left) and upstream (right) views of the 3D-printed axial bladed turbine.
3.1.3 CAD Assembly
In addition to the turbine rotor adaptations listed above, the other components needed for
the turbine were designed or selected. These parts included the shaft, the bearings, the bearing
retainers, and the shaft coupling. The complete assembly of the axial bladed turbine within the
film-cooled combustor of Chapter 2 is shown in the CAD screenshots of Figure 3-6. Regarding
the isometric view on the left, it may be noted that the turbine has a clockwise rotation direction;
this direction was constrained by the airbrake dynamometer; more details on this are provided in
Chapter 4. (Also included in Chapter 4 is a discussion of the bearings and shaft coupling selected
for the supersonic turbomachinery.) Another important note from the figure is that the bearing
retainers are mounted to the existing hub components of THOR. Mounting the bearings in this
manner was intended to avoid the cost of machining an entirely new hub for the turbine. However,
this assembly posed two challenges that had not yet been overcome as of the writing of this thesis.
73

The two issues that prevented the axial bladed turbine from being attached and tested in
the film-cooled combustor involved the questions of where to mount the dynameter and how to
balance the setup. The airbrake dynamometer, although compact to most commercially available
dynamometers, still did not lend itself to be easily mounted to the THOR stand. More on this topic
is discussed in Chapter 4. The issue regarding the turbine balancing was caused by the fact that
the hub components of THOR could not be axially aligned to an acceptable tolerance. The THOR
hub parts shown in Figure 3-6 did not have self-centering features such as pins or conical surfaces.
This meant that the hub components’ only alignment was provided by the eight circumferential
bolts that connect each downstream section to the adjoining upstream section. Unfortunately, the
bolt holes’ radial tolerance was not sufficient for a turbine spinning at 50,000 RPM. Therefore, an
alternative solution was to test the axial turbine on a cold-air flow apparatus that could be mounted
on the dynamometer stand without the challenges posed by the RDC. The design of this cold-air
flow test apparatus was in development during the writing of this thesis and is therefore omitted.

Figure 3-6: Isometric and side section views of the cooled combustor outfitted with the axial
bladed supersonic turbine.
3.1.4 Shaft Analysis
Before the decision was made to test the axial bladed turbine on a cold-air stand apart from
the film-cooled RDC, a shaft analysis was conducted for a simple shaft with the same diameter
and length as the shaft presented in Figure 3-6. The shaft analysis was completed in two parts: the
74

first part involved solving for the external and internal forces with the fourth-order deflection
method, and the second part involved calculating the factors of safety at the critical cross-sections.
It must be noted that this procedure could have been completed much more quickly with a finiteelement method software such as SOLIDWORKS or ABAQUS CAE, but the complexity of the
analysis was not realized until the “manual” shaft analysis was well underway. Nonetheless, the
complete manual shaft analysis is provided in Appendix D; summary findings are presented below.
For the simple shaft analysis, only the external loads imposed by the four main components
were imposed; those components included the coupling, the turbine, the upstream bearing, and the
downstream bearing. These are represented by Components 2 through 5 in Figure 3-7 below; the
shaft is represented by Component 1. Also shown in the figure are the segment lengths and the
nomenclature of all components used in the analysis. The boundary and continuity conditions
imposed on the shaft are included in Appendix D. Since the shaft was statically indeterminant,
these conditions were required to solve the system’s unknown forces.

Although the shaft

conditions at the coupling were unknown, they could be estimated. High-speed couplings like
those listed in the R+W Coupling Catalog [50] tend to have maximum lateral and angular
misalignments of 0.05 mm and 0.5°, respectively. Any coupling misalignment causes the shaft to
deflect, but this deflection is smaller than the coupling deflection.

= 12

=

=

120

1

=
20

Figure 3-7: Diagram of the shaft analysis dimensions and nomenclature.
75

For this shaft analysis, the shaft deflections caused by the coupling were set to be two and
five times smaller than the maximum lateral and angular misalignments allowed for a high-speed
coupling. That is, the shaft deflections at the coupling were the following: 0.025 mm and 0.25°
for the 𝑥𝑦-plane and 0.010 mm and 0.10° for the 𝑥𝑧-plane. Moving on from the coupling, the
bearings each received continuity conditions, meaning that they had no lateral deflection—only
angular deflection. Next, the turbine only required the force estimates; boundary conditions were
not needed since the manual analysis started at the shaft’s left end. Using some results from the
CFD analysis of Section 3.1.1, the thrust was set at 1200 N and the torque was set at 20 N-m. The
last input for the shaft analysis was the centrifugal force caused by the rotor imbalance. Although
the turbine had not been balanced at the time of the shaft analysis, an initial estimate placed an
unbalance mass of 0.005 kg at 5 mm offset from the rotation axis. This created a large unbalance
force at 50,000 RPM, but it resulted in a conservative estimate for the shaft analysis.
Coding the equations generated in the shaft analysis turned out to be challenging but
successful. After solving for the unknowns, a set of plots was created for the shear force and
bending moment diagrams, the angular and linear deflections, and the forces at three unbalance
rotation angles. These plots are all contained in Appendix D. After finding forces at the coupling,
bearing, and turbine locations on the shaft, the results were exported from MATLAB into
Microsoft Excel for a fatigue failure analysis. Failure usually occurs at the critical cross-section
with the greatest internal bending moment, regardless of the internal shear, axial, or torque loads.
Therefore, only the critical cross-section at the upstream bearing was analyzed for the failure
analysis. In this section, twelve critical elements were placed around the circumference of the
shaft; then, the stresses at each critical element were analyzed with various failure criteria. The
results of this analysis are shown in Appendix D. The lowest fatigue and yielding factors of safety
occurred for Cross-Section 𝐶 (the downstream bearing). However, all factors of safety remained
above unity, indicating that the shaft was still expected to have infinite life.
Since the turbine mounting system of Section 3.1.3 would not be used, at least in the scope
of this thesis, the shaft analysis results were not completely applicable to the project’s future.
However, the MATLAB code and Excel spreadsheet were made in a way such that they could be
updated for the new assembly’s shaft dimensions. With the shaft analysis concluded, the axial
bladed supersonic turbine design had been successfully brought through another phase, and future
work would focus on testing the axial bladed turbine in cold air.

76

3.2

Axial Bladeless Supersonic Turbine

3.2.1 Background
In [28], an optimization scheme was proposed for using an axial bladeless turbine in
rotating detonation combustors; this turbine can be thought of as a spiral drum that extracts power
from shock waves at the hub. Like the axial bladed turbine, it was possible to place a bladeless
turbine in a film-cooled combustor such as the one described in Chapter 2. However, the project
that sponsored the development of the film-cooled combustor and the axial bladed turbine did not
have the resources to design and manufacture a bladeless turbine for the cooled combustor. Instead,
the bladeless turbine would be made through a project in conjunction with Purdue University’s
Herrick Laboratories, in which the turbine would be used in a supercritical carbon dioxide (SCO2)
cycle. In simple terms, the project goal was to replace the expansion valve in a SCO2 refrigeration
system with a turbine made for low-power extraction; offsetting the power required by the
compressor in a refrigeration system increased the overall cycle efficiency. For the sake of brevity,
this thesis does not cover the SCO2 cycle’s thermodynamic analysis; thermodynamics are only
discussed in the context of the bladeless turbine.
The cycle and component diagrams for the SCO2 system’s initial configuration are given
in Figure 3-8 and Figure 3-9, respectively. In the cycle diagram, the turbine is represented by the
blue process line from Station 7, which is in the supercritical region, to Station 8, which is in the
saturated liquid-vapor dome. A second configuration (not shown) replaced the expansion valve
between Stations 12 and 13 with another turbine; here, the turbine operated on the border between
the saturated liquid and saturated liquid-vapor regions. To develop a bladeless turbine for the
SCO2 cycle, the optimization procedure presented in [27] was used. At this point, two numerical
routines were created, one for a turbine operating in the saturated liquid-vapor region and another
for a turbine operating on the saturated liquid line. The results for the two routines are presented
in Figure 3-10 and Figure 3-11, respectively. The vapor dome turbine could extract approximately
200 W for the following conditions: 20 cm average radius, 4 cm length, 30° inflow angle, and
0.22 kg/s mass flow rate. A similarly sized turbine operating in the liquid region could not extract
as much power, so the project focus shifted to only the vapor dome turbine.

77

Figure 3-8: Pressure-enthalpy diagram for the SCO2 cycle (courtesy of Fatih Meral).
Gas Cooler

7

6

Generator

5
4
Intermediate
Cooling

HP Compressor

Expander

11
10

9

2

M

13

LP Compressor

MT Evaporator

12

3

1
LT Evaporator

Figure 3-9: Component diagram for the SCO2 cycle (courtesy of Fatih Meral).

78

Figure 3-10: Pressure contour (top) and Mach number contour (bottom) for a bladeless turbine
operating in saturated liquid-vapor CO2.

Figure 3-11: Pressure contour for a bladeless turbine operating in saturated liquid CO2.

79

After the CFD simulations proved that the bladeless turbine would extract a useful amount
of work in the supercritical CO2 cycle, the turbine could progress toward the test phase. Ideally,
the turbine would be tested in an actual supercritical CO2 refrigeration system, but this presented
difficulties. First, the power produced by the turbine had to be absorbed by a compact device (or
dynamometer) that could be mounted to the existing CO2 system at Herrick Labs. As described in
Chapter 4, a dynamometer was already in development for the axial bladed turbine, so it was not
difficult to conceptually apply the dynamometer to the bladeless turbine. However, the device of
Chapter 4 could not easily be mounted among the densely packed components in the CO2 system
without running up hardware costs. A second issue was the time to design and manufacture a
sealed turbine housing to prevent the CO2 from escaping into the ambient. Therefore, since
mounting the bladeless turbine in the CO2 system was not feasible at the time, a solution was
needed to provide adequate testing of the bladeless turbine outside the CO2 system.
A solution presented itself in the form of air testing at Purdue’s Zucrow Laboratories. Since
one of the original goals for the bladeless turbine was to test it in a rotating detonation combustor,
the Turbine-integrated High-pressure Optical RDE (THOR) would once again be used. Although
the most recent bladeless turbine optimization had been for the saturated liquid-vapor region of
CO2, the turbine design was tweaked to operate in air conditions like those of the SCO2 cycle. The
air injection nozzle of THOR was retained to produce supersonic flow at the turbine inlet; the
contour plot of Figure 3-12 shows the Mach number approaching 1.8 just a short distance
downstream of the throat. The other hub components typically mounted downstream of the throat
for a detonation test were replaced by the bladeless turbine apparatus. The CFD simulation results
for the bladeless turbine operating in THOR are shown in Figure 3-13. This turbine produced
5.3 kW for a mass flow of 1.6 kg/s and a speed of 30,000 RPM.

80

Figure 3-12: Mach number around the air injection throat of THOR.

Figure 3-13: Pressure contour and Mach number contours for a bladeless turbine operating in
THOR with unvitiated air in the absence of a rotating detonation wave.
For the optimized wavy profile shown in Figure 3-13, there are two orientations, which are
mirror images of each other. The first orientation has gradual “ascents” and steep “descents” in a
periodic clockwise direction, and the second orientation has steep “ascents” and gradual “descents”
in a periodic clockwise direction. Figure 3-14 below shows these orientations. The blue 90° sector

81

was imported directly from the CFD output file, and the red 270° sector was generated by copying
and rotating the blue sector three times to complete a full wavy profile.

Figure 3-14: Two orientations for the wave profile of the bladeless turbine.
3.2.2 Impeller Design
After optimizing the bladeless turbine first for supercritical CO2 and then for air, the next
step was to import one of the blade profiles given in Figure 3-14 above into SOLIDWORKS to
create a model that could be manufactured. Creating this model required an in-depth process, first
to adjust the wavy profile and then to make the helical solid body. Although not shown here, the
quarter-sector data from the CFD output file did not comprise a complete 90°; there was a small
gap at one end. Thus, the first step was to fill this gap with an arc such that it maintained tangency
with the profile. After filling the gap, the quarter-sector profile was given a circular pattern, which
enclosed the sketch. Then, the two construction circles were created on the wavy profile: the first
circle intersected the profile at the midpoint between the peaks and troughs, and the second circle
intersected the profile’s peaks. Global variables were used to constrain the circle diameter values
to ensure the enclosed wavy profile would update for any dimension changes.
After honing the process of parameterizing the wavy profile, the next step was to create the
helical solid body. To do this, three sketches were created on three different sketch planes, which
were separated by distances 𝐿1 and 𝐿2 . The first sketch contained a simple circle with no waves

82

or other features; the global variable named 𝐷1 constrained the circle diameter. The second
contained the first wavy profile with a peak circle diameter constrained by the global variable 𝐷2 .
The third sketch contained the second wavy profile with a peak circle diameter defined by the
global variable 𝐷3 . A diagram of the interaction between these dimensions is provided in Figure
3-15, and the variable definitions are listed in Table 3.2. The most confusing dimension was 𝐷𝑚𝑎𝑥 ;
this was defined as the largest midpoint diameter of an “ideal” wavy profile (i.e., neither of the
profiles defined by 𝐷1 and 𝐷2 ) that had the same peak circle diameter as 𝐷1 . This value had to be
found with manual iterations since no explicit relationship could be procured.
The last hurdle for the bladeless turbine was making the helical guide curves for a loft
feature across the three sketches. The three most important variables for any helix are the helix
angle, the pitch, and the length. The helix length was a sum of 𝐿1 and 𝐿2 , and the helix angle was
set at 65° from CFD optimizations. Since the bladeless turbine was tapered from the inlet to the
outlet, the pitch had to be defined in terms of the taper/slope angle and the average radius; the helix
pitch is given by (13). After fully defining one helix, the three sketch profiles had to be edited
such that they pierced the helix at a consistent location on each profile. Then, three additional
helices, identical to the first, were made at 90° around the rotation axis. Ideally, there would be
one helical guide curve per wavy period, but four helices produced a turbine with minimal
distortion. After validating the entire process, a PowerPoint tutorial was created to help future
bladeless turbine designers; four snapshots from this tutorial are shown in Figure 3-16.

𝐷2 = 𝐷𝑚𝑎𝑥 − 𝐿1 𝑡𝑎𝑛(𝜃𝑠𝑙𝑜𝑝𝑒 )

(11)

𝐷3 = 𝐷2 − 𝐿2 tan(𝜃𝑠𝑙𝑜𝑝𝑒 )

(12)

2𝜋 ∙ 𝑅𝑚𝑒𝑎𝑛
2𝜋 ∙ (𝐷1 + 𝐷2 )
=
2 ∙ 𝑡𝑎𝑛(𝜃ℎ𝑒𝑙𝑖𝑥 ) 4 ∙ 𝑡𝑎𝑛(𝜃ℎ𝑒𝑙𝑖𝑥 )

(13)

𝑃𝑖𝑡𝑐ℎ =

83

Figure 3-15: Main dimensions for the bladeless turbine.

Table 3.2: Parameter definitions for the bladeless turbine.
Variable
𝐷1
𝐷2
𝐷3
𝐷𝑚𝑎𝑥

𝐿1
𝐿2
𝜃ℎ𝑒𝑙𝑖𝑥
𝜃𝑠𝑙𝑜𝑝𝑒

Value Equation/Source
Definition
130 mm
THOR
diameter of a circle just downstream of THOR nozzle
124.5 mm
(11)
midpoint-to-midpoint diameter of the first wavy
profile, which is separated from the circle by 𝐿1
117.5 mm
(12)
midpoint-to-midpoint diameter of the second wavy
profile, which is separated from the first profile by 𝐿2
126.2 mm
trial & error maximum midpoint-to-midpoint diameter of an “ideal”
wavy profile with a peak-to-peak diameter that
matches 𝐷1 ; no explicit relation was found for this
10 mm
CFD
distance between the circle and the first wavy profile;
found by comparison to CFD
40 mm
CFD
distance between the first and second wavy profiles;
found by comparison to CFD
65°
CFD
guide curve helix angle; found by comparison to CFD
10°
THOR
guide curve slope angle; matches THOR nozzle slope

84

Figure 3-16: Four snapshots of the bladeless turbine creation: (a) the imported quarter-sector of
the first wavy profile with two construction circles, (b) the enclosed sketch of the first wavy
profile showing values for 𝐷1 and 𝐷𝑚𝑎𝑥 , (c) the two wavy profiles, (d) the two wavy profiles
with the upstream circle and the helical guide curves.
Writing the PowerPoint tutorial for the bladeless turbine turned out to be beneficial for the
author. A discussion with the advisors about the bladeless turbine revealed that there was more
than just one wavy profile orientation. First, there were the two mirrored profiles shown in Figure
3-14. Second, each profile could spiral clockwise or counterclockwise about the rotation axis.
Thus, four turbines were available for testing; these turbines are shown in Figure 3-17 below. The
airbrake dynamometer of Chapter 4 required the turbine rotation direction to be clockwise relative
to the downstream-to-upstream perspective, so four additional CFD simulations were performed
to find which turbine profile performed the best with a clockwise rotation direction. The highest-

85

performing combination turned out to be Curve 1 with clockwise helical guide curves. Once this
combination was discovered, the hub was hollowed to reduce the rotational moment of inertia, and
a hole was added for the shaft, like the axial bladed turbine modifications of Section 3.1.2. The
mechanical drawing for this turbine is given in Appendix C.

Figure 3-17: Four bladeless turbines created by importing Curves 1 and 2 and setting the spiral
direction to be either clockwise or counterclockwise.
3.2.3 CAD Assembly
After the turbine profile had been finalized, the other components needed for the turbine
could be designed or selected, just as they were for the axial bladed turbine of Section 3.1. Unlike
the axial bladed turbine, the bladeless turbine would be mounted in THOR without intending to
conduct an RDE test; instead, the test would only involve cold air. Therefore, the THOR center
body was replaced by the bladeless turbine. The goal was to reuse the bearings and coupling from
86

the axial bladed turbine tests and avoid unnecessary redesigns. However, a few issues were
encountered in the design of the hardware required to test on THOR; these are indeed the same
issues that faced the axial bladed turbine, as discussed in Section 3.1.3.
The first problem revolved around the airbrake dynamometer’s placement on THOR, as
discussed in Chapter 4. The second problem involved balancing the turbine. Although the
bladeless turbine did not require the long center body that hindered the bladed turbine testing, the
bladeless turbine was still affixed to THOR components that were not designed for high-speed
turbomachinery. The proposed assembly is shown in Figure 3-18 below; here, the bladeless
turbine was connected to the throat of THOR with a bearing retainer like that for the bladed turbine.
Since these parts were not suitable, the bladeless turbine would have to be assessed on a cold-air
flow apparatus instead of THOR, as was the case for the bladed turbine. This decision finished
the bladeless turbine’s design phase for this thesis research. The turbine design’s success meant
that future work could focus solely on testing the turbine in cold air.

Figure 3-18: Isometric and side section views of the bladeless turbine mounted in THOR.

87

3.3

Radial Bladed Supersonic Turbine

3.3.1 Background
In [34], an axial-inflow/radial-outflow turbine was optimized for various inlet conditions,
including both unsteady RDC exhaust flows and uniform supersonic flows. This made it also a
suitable candidate for testing in the supercritical CO2 system described in Section 3.2. Like the
numerical analyses performed on the bladeless turbine, two sets of CFD simulations were
conducted for the radial turbine: the first was for the saturated liquid-vapor dome and the second
was for the saturated liquid region. The simulation results are provided in the pressure contours
of Figure 3-19 and Figure 3-20 The vapor dome turbine extracted approximately 2.6 kW with the
following conditions: 40 mm inlet diameter, 120 mm outlet diameter, 0° inflow angle, and
0.22 kg/s mass flow. A similarly sized turbine operating in the liquid region did not perform as
well, but one coping mechanism was to increase the blade leading edge thickness to that shown in
Figure 3-21. This forced the liquid CO2 to enter the saturated liquid-vapor dome immediately
downstream of the leading edge, wherein better performance was achieved.

Figure 3-19: Pressure contour for a radial turbine operating in saturated liquid-vapor CO2.

88

Figure 3-20: Pressure contour for a radial turbine operating in liquid CO2.

Figure 3-21: Radial blade profiles with thicker leading edges for operating in liquid CO2.
As described in Section 3.1.1, the axial bladeless turbine could not easily be mounted in
the supercritical CO2 test stand at Herrick Labs because of two reasons: (1) there was very little
room for the turbine and dynamometer on the stand, and (2) a sealed turbine housing was needed
to retain the CO2 within the system. The same two issues faced the radial turbine design, but
unfortunately, the radial turbine could not be mounted on THOR for cold air testing for one reason:
size. The radial turbine inlet was much smaller than the diverging section downstream of the air

89

injection throat, so the flow would have to pass through another converging section before the
turbine. This seemed unnecessary, so another approach was taken. As shown in the following
sections, an entirely new test stand was designed for the radial turbine; this included an inlet with
flow conditioning, a shroud at the blade tips, and a mount for the shaft and bearings. Like the
bladeless turbine tests on THOR, the radial turbine would be tested with cold air, meaning that it
could exhaust to the ambient with no issues. A final CFD simulation was performed on the radial
turbine to check its performance in air; the resulting pressure contour is given in Figure 3-22.

Figure 3-22: Pressure contour for a radial turbine operating in air.
3.3.2 Impeller Design
After optimizing the radial turbine first for supercritical CO2 and then for air, the next step
was to import the blade profile into SOLIDWORKS to make a manufacturable model. Just like
the bladeless turbine of Section 3.2, creating the radial turbine model required an in-depth process
to create the impeller and modify the hub. Since the blade profile was made in NUMECA’s
AutoBlade™, the output file was slightly different than that for the bladeless turbine; the blade
and hub profiles were provided in an Initial Graphics Exchange Specification (IGES) file format
rather than a MATLAB-generated curve. Importing this IGES file into SOLIDWORKS revealed
a model with only hollow surface geometry, which could not be used by a CNC machine.
90

Furthermore, only three surfaces existed in the model: the hub, a single blade, and the shroud.
Therefore, the radial turbine modifications began with making solid bodies that could easily be
modified for manufacturing purposes.
First, the radial turbine blade surfaces were enclosed with boundary surfaces at the blade
and tip. This allowed the blade surfaces to be knitted and filled as a solid body, which was then
used in a circular pattern to create 10 solid blade bodies about the rotation axis. Next, the hub
profile was enclosed with a boundary surface on the open end, and then surfaces were knitted and
filled. At this point, the hub and blades were merged as one continuous solid body, meaning that
additional changes, such as blade root fillets, were connected to both the blades and the hub.
Interestingly, the turbine blade tips extended into the shroud surface near the passage outlets, so
these tips were trimmed to avoid interference. The last step was to convert the shroud surface into
a solid, which was much like the previous processes. A surface offset from the initial shroud
surface was created, the two surfaces were joined by a surface between their boundaries, and then
all surfaces were knitted and filled as a solid body. Three screenshots were taken while solidifying
the bodies, as shown in Figure 3-23 below.

Figure 3-23: Snapshots of the radial turbine creation: (a) the blade and hub imported as hollow
surfaces, (b) the blade and hub as solid bodies, (c) the blade, hub, and shroud as solid bodies.
After verifying that all surfaces were closed and filled, a few modifications to the radial
turbine could be made. The first was the inclusion of a shaft on the hub; unlike the axial bladed
turbine of Section 3.1 or the axial bladeless turbine of Section 3.2, a shaft could not pass through
the hub to have a nut attach from the opposite side. If a hole were made through the turbine, the

91

nut would displace the radial turbine nose cone, which was of primary significance to the turbine’s
performance. This shaft is shown in the turbine’s mechanical drawings in Appendix C. Aside
from the shaft addition, communications with a machinist at HW Webb Engineers Limited in
Suffolk, UK, exposed the fact that the gap between the blade roots at the passage throat was only
about 1.2 mm, which was too narrow and deep to make on a CNC machine. Therefore, to increase
the hub throat gap, either the blade profiles or the hub had to be modified.
After consulting with the engineering team, it was decided against modifying the blade
profile. The only option left was to increase the conical hub diameter such that the minimum throat
gap was a bit larger. To alter the hub, a few different ideas were brainstormed. The first idea was
to create a new hub profile at a 1-mm outward offset from the original hub geometry; all following
ideas were based on this principle. The second idea was to create a 2-mm offset, but in doing this,
it was observed that the nose cone deviated too much from the original model. To compensate for
this, the third idea had an extended cone geometry in addition to the 2-mm offset. A fourth idea
was to place fillets at the blade roots, but these fillets were difficult for the machinist to program
into the CNC machine. A fifth and final idea was to have an offset varying from 3 mm at the
passage throat to 0 mm at the outlet; the transition was accomplished with a set of tangential arcs.
Figure 3-24 below shows the five design ideas as well as the case with no offset.
For all five radial turbine hub modifications, the inlet, throat, and exit areas were measured
in SOLIDWORKS by first creating sketch planes at these locations. Then, the blade geometry
intersecting the planes was projected onto sketches and enclosed such that the passage area could
be measured. Diagrams of the inlet, throat, and exit locations and the areas at these locations are
shown in Figure 3-25. In addition, the measured areas and the calculated area ratios are recorded
in Table 3.3. The goal in creating five different hub modifications was to keep the throat-to-exit
area ratio as close to the base case, which had a throat-to-exit ratio of 8.0%. By this metric, the
best modification was Configuration 5, which had the 2-mm offset and blade fillets. However,
since the fillets posed an issue for the machinist, Configuration 5 was removed. Configurations 2,
3, and 4 all had similar throat-to-exit area ratios at 8.2%, but since Configuration 4 mostly retained
the nose cone’s original shape, this was selected as the final modification.
After analyzing the potential hub modifications, the final modification had a blade root
throat gap of approximately 2.8 mm. The original design had a gap of 1.2 mm, and the minimum
gap set by the machinist was 2.6 mm. The ideal gap size was above 3.5 mm, but the only hub

92

modification that achieved this was Configuration 6 (the 3-mm variable offset), but this hub profile
deviated too much from the optimized geometry. Therefore, after sending the radial turbine’s final
version to the manufacturing engineer at HW Webb Engineers, the focus could shift to the other
hardware needed for the radial turbine test in cold air.

Figure 3-24: Six different configurations for the radial turbine hub modifications.

Figure 3-25: Diagram of the radial turbine inlet, throat, and exit areas for Configuration 1.

93

Table 3.3: Parameters for the six hub configurations.
Hub Throat
Blade
Config- Offset Gap Variable Extende Root
uration (mm) (mm) Offset? d Cone? Fillets?
No Hub N/A
0.21
N/A
N/A
N/A
1
0
1.24
2
1
2.02
3
2
2.79
4
2
2.79
Yes
5
2
3.81
Yes
6
3
2.79
Yes
-

Inlet Throat Exit Throat- ThroatArea
Area
Area
Inlet
Exit
2
2
2
(mm ) (mm ) (mm ) Ratio Ratio
154.7
77.7
969.2 50.2% 8.0%
128.3
65.0
807.7 50.7% 8.0%
123.5
63.2
772.5 51.2% 8.2%
115.1
60.5
740.9 52.6% 8.2%
115.1
60.5
740.9 52.6% 8.2%
114.5
59.8
734.6 52.2% 8.1%
105.9
56.9
807.7 53.8% 7.0%

3.3.3 CAD Assembly
After the radial profile had been finalized, the other components needed for the turbine
could be sourced like they were for the axial bladed turbine of Section 3.1 and the axial bladeless
turbine of Section 3.2. Unlike those turbines, there were no intentions to mount the radial turbine
on the THOR stand; it was known from the beginning that new hardware was required for this
turbine. This hardware included an inlet with flow conditioning to dampen turbulent fluctuations
incurred upstream, a housing for the turbine bearings, the support structures for the inlet and
bearing housing, and an array of pressure measurements. (A discussion of the bearings and shaft
coupling is reserved for Chapter 4.) Figure 3-26 below shows an initial component assembly for
the radial turbine. Note that a sintered muffler and a honeycomb mesh would condition the flow,
and total and differential static pressures would be recorded at the inlet and outlet.

Figure 3-26: Diagram of the initial radial turbine CAD assembly.
94

3.3.4 Inlet Modifications
A few options were available for the radial turbine inlet, as shown in Figure 3-27 below;
here, the word “inlet” refers to how flow enters the turbine apparatus, not necessarily the passage
inlets between each blade. The first option was to use several small tube fittings situated in the
inlet end cap as well as around the flow conditioning chamber’s circumference. No matter how
many fittings were used for this option, it always had awkward tubing angles and no way to add
sintered mufflers for each fitting. A revised option was to have an end cap with two opposing 1”
NPT flanges, one each for the tube fitting and the sintered muffler; the larger flange bolted to the
flange encircling the conditioning chamber. This design, however, offered only poor sealing
between each flange due to the mismatched sizes. A third option was to use two opposing 1” NPT
flanges with the same bolt pattern radius; four bolts were screwed through both flanges into the
material surrounding the settling chamber. The third option offered the best flange seals as well
as a sintered muffler for the inlet flow, so the third option was selected for the final design.

Figure 3-27: Three options for the radial turbine inlet: (1) six fittings without sintered mufflers,
(2) one fitting with a muffler but poor seals, (3) one fitting with a muffler and better seals.
95

3.3.5 Shroud Modifications
After finalizing the inlet design, the last step was to optimize the shroud piece containing
the conditioning chamber and the instrumentation. At the rotor outlet, the initial model had an
eight-bolt connection, and the space between the shroud and the rotor mount was maintained by
simple tubular pieces. In addition, the shroud was designed as a single piece with a 200-mm outer
diameter for the inlet and outlet flanges. This shroud had eight counterbored holes for differential
static pressure measurement at the inlet and two threaded holes for total pressure measurement at
the inlet and outlet. The initial design’s biggest flaw was the lack of alignment features for the
outlet bolts; the holes’ clearance fits did not have a tight enough tolerance to prevent the blade tips
from scraping the shroud and potentially damaging something.
A better design was suggested by HW Webb Engineers Limited, as shown in Figure 3-28.
This design focused on a two-piece shroud, where the alignment problem was solved by merging
the outlet flange with the bolt spacers and a ring that could fit into the rotor mount. In addition,
the outer diameter was reduced from 200 mm to 165 mm to lower raw material cost. Since this
size reduction also limited the outlet area, the screw count was reduced from eight to four to
prevent flow field distortion. The screw size was also changed to M6 x 1 after a screw analysis
showed that M8 x 1.25 screws were unnecessarily large; this analysis is contained in Appendix E.
A final improvement was the use of threaded fasteners for all probes; the counterbored holes were
too deep for such a small size, and the threaded holes were much easier to make.

Figure 3-28: Two options for the radial turbine shroud.
96

3.3.6 Final CAD Assembly
Through the combined effort of the author and HW Webb Engineers Limited, the final
design of the radial turbine apparatus was achieved, as shown in Figure 3-29. A few notes about
this final design may be made. First, the turbine outlet shroud piece was changed a bit from the
model shown in Figure 3-28; the dimensions used in the bolt analysis were now a bit larger than
the actual model, but the changes to the factors of safety were negligible. Second, the support
structures for the rotor mount and the inlet shroud piece were changed to offer better strength to
the system; for instance, the thickness and height were increased to match the rotation axis of the
airbrake dynamometer. A third set of modifications involved the shaft; the shaft diameter was
increased to 15 mm for the bearing section and 12 mm for the coupling connection. Mechanical
drawings for select machined pieces may be found in Appendix C.

Figure 3-29: Diagram of the final radial turbine CAD assembly.
At the time of the writing this thesis, the radial bladed turbine was in the process of being
manufactured at HW Webb Engineers Limited in the UK. Since the radial turbine apparatus had
been more developed than those of the axial bladed or axial bladed turbines, the radial turbine
would be able to be tested as soon as it arrived at Zucrow Labs. The other turbines still required
mounting structures, but ideas were in the works to create mounts like the radial turbine mount;
these would mount to the same plate with the dynamometer without the need for costly retrofitting.
In summary, the design of the three turbines in this chapter was one small but successful step in
advancing the science of novel supersonic turbomachinery.
97

4

AIRBRAKE DYNAMOMETER

In the literature review of Section 1.1, four common types of dynamometers and their
working principles were described; these included (1) hydraulic brakes, (2) aerodynamic or air
brakes, (3) induction eddy current brakes; and (4) alternating/direct current brakes. For the test of
the supersonic turbines in the present research, an airbrake dynamometer was selected for its low
acquisition and development cost. This chapter is separated into several sections to describe the
different development areas; these include a background on using a turbocharger as an airbrake
dynamometer (4.1), the turbocharger performance maps (4.2), the mounting architecture for the
turbocharger (4.3), the oil system for the dynamometer (4.4), the instrumentation and rotating
hardware (4.5), and the fully integrated system (4.6).

4.1

Background
The operating principle of a dynamometer is to absorb the power extracted by the turbine

from the fluid flow. The test engineer must be able to vary the dynamometer’s resistance such that
the turbine’s performance for different conditions may be assessed. At this point, the turbine’s
performance may be determined in one of three ways: (1) turbine thermodynamics, (2) airbrake
thermodynamics, or (3) mechanical torque. Option (1) is to measure the mass flow rate (𝑚̇) and
the total temperatures inlet (𝑇𝑡𝑜𝑡, 𝑖𝑛 ) and outlet (𝑇𝑡𝑜𝑡, 𝑜𝑢𝑡 ) ; then the thermodynamic power
expression (4) can be used to calculate the power extracted by the turbine from the fluid flow. This
method may prove challenging since the temperature profiles at a supersonic turbine’s inlet and
outlet are not uniform; many temperature measurements are required to create an accurate
temperature map. Option (2) is to measure the total temperatures at the airbrake’s inlet and outlet
and then use (4) to calculate the power. This is more accurate than method (1) since the
temperature profiles at the brake inlet and outlet are more uniform than those of the turbine.
Option (3) is to measure the shaft speed (𝜔) and torque (𝜏) between the turbine and the
airbrake; then the mechanical power expression (5) can be used to calculate the extracted power.
Although there are no temperature uncertainties involved with the mechanical power method, its
accuracy is limited by the torque sensor’s ability to detect rapid fluctuations in turbine torque.
Therefore, for the airbrake dynamometer, two methods of calculating the power were included in

98

the design. First, the thermodynamic power would be calculated across the brake (the turbocharger
compressor), and second, the mechanical power would be measured with a torque sensor between
the brake and the test article. Some deviation in the calculated power values would be inevitable,
but it was theorized that the deviations would be small.
To build an airbrake dynamometer, the brake (compressor) had to sustain the high speeds
and power supplied by the supersonic turbines. For this project, the most economical option was
to retrofit an existing engine turbocharger; turbochargers are designed for high speeds and long
operational life. Before the author’s involvement, an industrial engine turbocharger was donated
to PETAL by Cummins Holset. (The identification number is omitted at the request of Cummins.)
Early project ideas involved removing the compressor impeller from the turbocharger and
installing it on a separate rig, where it connected to the test article. At one point, it was stated that
the supersonic turbines would be unable to accelerate the system from rest to operating speed, like
how internal combustion engines cannot start without an initial work input. Thus, it was decided
to retain the turbocharger turbine as a booster for spinning up the system at the test initiation. More
details on the startup procedures are covered later in this section.
The next step in the dynamometer’s conceptual design phase was to decide how to connect
the turbocharger to the test turbines. One idea was to replace the existing shaft with a longer shaft,
but the turbocharger turbine was forge-welded to the existing shaft, preventing its removal. The
only feasible option was to remove the shaft nut on the turbocharger compressor and replace it
with a threaded shaft extension, which then connected to the test turbines. Since the axial bladed
turbine of Section 3.1 and the axial bladeless turbine of Section 3.2 were each designed for the
THOR test stand, the only logical place for the turbocharger was upstream of the RDC with the
shaft passing through THOR’s hollow center body. The diagram for the axial bladed turbine setup
is shown in Figure 4-1; the other turbines are similar and thus not shown. Figure 4-2 shows the
inlets and outlets of the Holset turbocharger as well as a CAD model that was made for visual
representation in the ensuing assemblies.

99

Figure 4-1: Diagram of the test setup for the axial bladed turbine.

Figure 4-2: Images of the turbocharger and its CAD model.
Since the turbocharger turbine would spin up the system, a multi-step starting procedure
was required. To help visualize the following discussion, the fluid flow diagrams for the three
supersonic turbines are shown in Figure 4-3, Figure 4-4, and Figure 4-5. For each flow diagram,
Step 1 injects high-pressure (HP) air into the turbocharger turbine (TCT) to spin up the system.
At this time, the turbocharger compressor (TCT) starts to push ambient air through a throttle valve

100

paired with a data acquisition device (DAQ) to measure outlet pressure and temperature. Step 2
for the axial bladed turbine purges nitrogen through the film-cooled combustor, and Step 3 predetonates the RDC. Step 4 stops the high-pressure airflow to the turbocharger turbine, and the
compressor throttle valve opens or closes to generate the turbine’s range of operating conditions.
Since the bladeless and radial turbines were to have air tests only, Steps 2 and 3 from the
axial bladed turbine operation were omitted from these diagrams. Note that the bladeless turbine
still has air passed through the RDC (just not combustion products), and the radial turbine has a
test apparatus apart from the RDC. In the axial bladed and bladeless turbine sections of Chapter
3, the issues with testing a turbine on THOR were reviewed, followed by the idea to test the two
axial turbines apart from the THOR stand. Therefore, Figure 4-3 and Figure 4-4 only reflect the
initial design intent—not the most recent development.

Figure 4-3: Fluid flows for the axial bladed turbine’s four-step test procedure.

101

Figure 4-4: Fluid flows for the axial bladeless turbine’s two-step test procedure.

Figure 4-5: Fluid flows for the radial bladed turbine’s two-step test procedure.
4.2

Turbocharger Performance Maps
Before the supersonic turbines could be tested, the turbocharger had to be calibrated. To

do this, there were two options. The first option involved testing the turbocharger at Zucrow Labs
and generating its performance maps without a test turbine, and the second option was to use a
dataset provided by Cummins. The second option was chosen to avoid the amount of time required
to accurately recreate all operating conditions. Unfortunately, the dataset did not contain explicit
variable definitions or instrumentation diagrams, but it did appear to have been post-processed, for
each variable was organized into succinct groups linked to a single parameter. For the compressor,
the data contained 30 points per variable and was organized into five groups of constant speed
with six elements per speed group. For the turbine, the data contained 60 points per variable and
was organized into six groups of constant pressure ratio with ten elements per pressure ratio group.
Plotting the data on two-variable plots did not yield much information about the trends or
the operating conditions, so three-variable contour plots were explored. Three-variable contour
102

plots have one variable each for the abscissa (x-axis), the ordinate (y-axis), and the unfilled or
filled contour regions. The issue with contour plots was that they required a grid with uniform or
semi-uniform spacing, but the Cummins data was understandably not uniform. Therefore, a twodimensional interpolation scheme was used to find the values for a user-defined rectangular grid
spanning the ranges of two variables from the dataset; these variables occupied the ensuing plot’s
abscissa and ordinate. The scheme utilized MATLAB’s scatteredInterpolant function,
which had three interpolation methods (linear, nearest neighbor, and natural neighbor) and two
extrapolation methods (linear and nearest neighbor). After some trial and error, the natural
neighbor interpolation method and linear extrapolation method were used.
Three issues were addressed in creating the contour maps. The first issue was that if the
mesh grid density was increased too high, the contour plot displayed regions of high and low values
between the original data points. These regions were not physical, so the mesh grid density had to
be kept below a subjective threshold for each variable combination. The second issue was that the
uniform grids always had points outside the original operating region. (The grid for a sample
contour map is shown in Appendix F.) To deal with these points, the extrapolation method in
MATLAB’s scatteredInterpolant function could be set to ‘none’, but this did not yield
acceptable results. Therefore, a workaround was found by plotting a white-only contour map on
the areas outside the operation region. The third issue involved plotting the constant speed lines
in the operating region. The compressor data were grouped by constant speeds, so its speed lines
could be made quite easily. However, the turbine data were grouped by constant pressure ratio,
so an additional interpolation scheme was used to create unfilled contour lines for speed lines.
After addressing all issues, the MATLAB routine was used to create several compressor
and turbine performance maps. Plotting the Cummins data was not immediately useful since the
atmospheric conditions present at the Cummins test cell would not be the same as those at the
PETAL test cell. To compensate, the pertinent variables were corrected according to the equations
in [51]; the premise was to compare the inlet conditions to a reference temperature (𝑇𝑟𝑒𝑓 ) and
pressure (𝑝𝑟𝑒𝑓 ) to find the dimensionless temperature (14) and pressure (15). These quantities
were used to find the corrected parameters for mass flow rate (16), speed (17), work, (18), and
torque (19). Having the performance maps for these corrected parameters would predict the
turbocharger behavior given the PETAL tests’ inlet conditions. Figure 4-6 and Figure 4-8 show
the compressor performance maps for corrected and uncorrected work, respectively, and Figure

103

4-7 and Figure 4-9 show the turbine maps for the same respective quantities.

Additional

performance maps for the other corrected quantities may be found in Appendix F.
𝑇𝑡𝑜𝑡, 𝑖𝑛
where 𝑇𝑟𝑒𝑓 = 288.1 𝐾
𝑇𝑟𝑒𝑓

(14)

𝑝𝑡𝑜𝑡, 𝑖𝑛
where 𝑝𝑟𝑒𝑓 = 101. 2 𝑘𝑃𝑎
𝑝𝑟𝑒𝑓

(15)

𝜃0 =
𝛿0 =

√𝜃0
𝑚̇𝑐 = 𝑚̇ ⋅ (
)
𝛿0
𝑁𝑐 =
𝑊̇𝑐 =

(16)

𝑁
√𝜃0
𝑊̇

(√𝜃0 ⋅ 𝛿0 )

𝑇𝑐 =

𝑇
𝛿0

Figure 4-6: Uncorrected compressor power as a function of uncorrected quantities.

104

(17)

(18)
(19)

Figure 4-7: Uncorrected turbine power as a function of uncorrected quantities.

Figure 4-8: Corrected compressor power as a function of corrected quantities.

105

Figure 4-9: Corrected turbine power as a function of corrected quantities.
4.3

Mounting System
In concert with the turbocharger performance map generation, the turbocharger mounting

system was designed. To describe every design change is not feasible for this thesis; some ideas
were not well-founded and have been omitted. For the sake of brevity, three versions are shown
in the subsections below. Section 4.3.1 reviews the initial version, including the main idea for
placing the turbocharger on the THOR stand. Sections 4.3.2 and 4.3.3 show intermediate and final
turbocharger dynamometer mount assemblies, respectively.

4.3.1 Initial Designs
Before the author’s work on the project, a flimsy assembly of T-slot aluminum rails
supported the turbocharger. The turbocharger was not affixed to the rails but was merely balanced
on the rails with two threaded rods; this “mount” was very much inadequate for any tests. The
author’s work began with determining where to place the turbocharger on the THOR stand and
how to connect it to the axial bladed turbine.

106

(At the time, this was the only turbine in

development; the scope of the thesis research later increased to include the axial bladeless and
radial bladed turbines.) If the turbocharger were placed downstream of the axial bladed turbine, it
would be in the hot RDE exhaust.

This exhaust would alter the compressor performance

unpredictably, so the only position for the turbocharger was upstream of the RDE. The problem
with this location was that it housed THOR’s pre-detonation and fuel systems. These components
are denoted in Figure 2-23 and Figure 2-27.
The pre-detonator and fuel manifold could be moved to alternate locations with new tubes
routed around the turbocharger, but it was not known if the turbocharger could fit on THOR. A
new turbocharger mount was designed and built to fit the turbocharger on THOR. Like the first
structure, the new mount used T-slot aluminum rails, but this mount was more substantial. If
adjustments were needed, the aluminum rails could easily be adjusted and discarded after fitting
the turbocharger on THOR. Figure 4-10 below shows the two initial aluminum mount structures,
and Figure 4-11 shows the CAD assembly for the aluminum structure placed on the back of THOR.
An important note is that the RDC rests on a “floating” plate that flexes from the RDC thrust; this
plate was too weak to support the turbocharger, so it had to be mounted to the unmoving plate
below the thrust load sensor.

Figure 4-10: Two images of the initial aluminum turbocharger mounts.

107

Figure 4-11: Diagrams of the turbocharger mounted to the THOR stand.
4.3.2 Intermediate Designs
When the aluminum frame was constructed, THOR was reserved for other test campaigns.
While waiting for THOR to become available for the turbocharger fitting procedure, two
intermediate turbocharger mounts were designed. The T-slot aluminum framing was not sufficient
for the turbocharger operation, so the next design used welded rectangular steel tube to support the
turbocharger. For this design, there was a question about how the turbocharger would align with
the axial bladed turbine in the film-cooled combustor. As discussed in Sections 3.1.3 and 3.2.3,
the THOR center body did not have adequate alignment features, so the axial turbines doubtfully
would align with the turbocharger at the outset. Therefore, the welded frame had three adjustment
features: (1) it could slide laterally, (2) it could move up or down by adjusting the nut position on
the threaded rods, and it could pivot in the circular slots on the mounting plate. These adjustments
are annotated in Figure 4-12 below.
The downfall of the welded steel design was that it had too many bolt-and-nut fasteners;
for a high-speed test, any vibrations caused by rotational imbalances could cause the nuts to loosen
and allow the equipment to fall. This had to be avoided, so a different idea was pursued. For this
design, the mount consisted of several machined pieces that bolted together in a manner less likely

108

to loosen from vibrations. In addition, the pieces had more degrees of freedom in case minute
adjustments to the alignment were required. While theoretically more robust, the machined mount
still did not solve the project’s overarching problem. For any system spinning at tens of thousands
of RPM, consistent alignment is imperative. Although the machined mount was adjustable, the
lack of proper centering features in THOR meant that the system’s alignment would have to be
checked before each turbine test. PETAL did not own the tools required for this operation, so a
third iteration of the turbocharger mount was created.

Figure 4-12: Welded and machined mounts for the turbocharger.
4.3.3 Final Design
The final turbocharger mount was a collaborative work with HW Webb Engineers Limited
in Suffolk, UK, which manufactured the turbocharger mount, the bladeless turbine, and the radial
turbine. This mount did not involve any THOR components since those had the previously
described alignment issues. Instead, the turbocharger was affixed to a new plate with two
machined steel vertical support structures. The slotted adjustment features present in the previous
designs were completely discarded; instead of aligning the turbocharger to a misaligned turbine,
the turbocharger was a permanent fixture on the dynamometer stand. The turbines were then

109

designed without modular hub pieces like those in THOR, meaning all pieces had a consistent fit.
Any minute misalignment was compensated by the shaft coupling.
A diagram of the final design is shown in Figure 4-13. The cylindrical gray piece beside
the turbocharger outlet was its actual position measured by a coordinate measurement machine
(CMM). (The turbocharger model had been made for visual representation, and the turbocharger
was shipped to the UK before PETAL’s CMM could be used to update the model.) Below the
mounting plate for the turbocharger and turbines, rubber bobbins rested between the plate and the
table below (not shown) to absorb any vibrations. As of the writing of this thesis, HW Webb
Engineers had not finished machining the mount, but the existing pieces are shown in Figure 4-14.

Figure 4-13: Isometric and side views of the final turbocharger mount.

110

Figure 4-14: Images of the manufacturing progress on the final turbocharger mount.
4.4

Oil System
In addition to the mounting system described in Section 4.3, the turbocharger dynamometer

required an oil system to lubricate the internal bearings. In a turbocharger’s standard environment,
the turbine side is connected to a hot engine exhaust; some heat is absorbed by the turbine housing
and the bearings. For this application, the oil is also a coolant for the bearings. For the airbrake
dynamometer, the turbine would only be connected to an unheated high-pressure air supply—not
a hot exhaust flow. Therefore, the oil system did not need an oil cooler, as the heat generated by
friction was believed to be so small that it would dissipate from the oil reservoir. Thus, the oil
system only required a pump, a filter, some hoses, and some fittings.
The oil system built for the airbrake dynamometer is shown in Figure 4-15. A Cummins
representative recommended that the turbocharger oil system should supply SAE 10W-30 oil at a
flow rate of four to eight liters per minute (one to two gallons per minute), a pressure of 2-6 bar
(30-90 psi), and a temperature of less than 120°C. When the oil system was being designed, there
were some ideas about using the same oil system to lubricate the bearings in the supersonic turbine
apparatuses, so the flow rate requirement was doubled. A search for a pump of this size yielded
the Piusi Viscomat Vane Pump [52]. Sealed bearings were later selected for the turbines, so the
oil pump was now twice the necessary size. Therefore, an extra hose was placed at the pump outlet
to function as a relief line if the turbocharger’s oil inlet pressure was too high.
111

Figure 4-15: Oil system for the turbocharger dynamometer.
4.5

Instrumentation and Rotating Hardware
To determine the supersonic turbines’ performance, an instrumentation setup was required

for the airbrake dynamometer. Because both the thermodynamic power and the mechanical power
were desired, two primary measurement locations were selected.

Since the turbocharger

compressor functioned as the power absorption brake, it needed more instrumentation than the
turbocharger turbine. Therefore, for the thermodynamic power, pressure and temperature would
be measured at the compressor inlet and outlet, and for the mechanical power, speed and torque
would be measured in the shaft between the bearing and the turbine. This section discusses each
component, and the bearings and couplings are included at the section’s end.

4.5.1 Compressor Exit Tube
The turbocharger compressor was an axial-inflow/radial-outflow impeller. For the axial
inlet, measurements would include ambient conditions like pressure, temperature, and potentially
relative humidity. Because the compressor housing routed the radial outflow into a single duct,
the outlet flow probes had to be placed somewhere along the duct. However, probes placed along

112

the duct would demonstrate much variability due to the pressure field fluctuations induced by
changing the flow from axial to radial to ducted. According to the investigation in [53], the
pressure field downstream of a 180° pipe bend needed around six diameters to recover to its prebend profile. While the compressor outlet duct was different from a 180° pipe bend, the idea of
extending the duct was applied to the instrumentation scheme. The resulting instrumentation tube,
complete with pressure probes, thermocouples, and a throttle valve, is shown in Figure 4-16.
It was assumed that the outlet duct’s straight section began in-plane with the rotation axis,
meaning that the existing duct extended approximately two diameters downstream from the bend.
The additional four diameters were attained by the tube shown in Figure 4-16; close to the sixdiameter mark, four thermocouples and a total pressure rake would be placed in the flow, and
additional holes could be used for static pressure transducers. Downstream of the probes was a
butterfly valve; the one shown here is [54]. This butterfly valve would be used to vary the load on
the test turbines; by throttling this valve, the compressor would move toward its surge or stall line,
absorbing more power in the process. A final note about the system is that the instrumentation
scheme did not include an air mass flow rate sensor, but measuring the static and stagnation
quantities would allow the Mach number and mass flow rates to be indirectly calculated. With all
these measurements, the thermodynamic power absorbed by the compressor could be calculated.

Figure 4-16: Instrumentation diagram for the turbocharger compressor outlet tube.
113

4.5.2 RPM Sensor
The Cummins Holset turbocharger cartridge was manufactured with a hole for a variablereluctance RPM sensor; the sensor that came with the turbocharger was the JAQUET ATS-1 DSE
1010 [55]. A variable-reluctance sensor works on the following principle: the sensor’s metal tip
is situated near a notch in the shaft connecting the turbocharger turbine and compressor, and as the
notch passes the sensor, it changes the magnetic field (or reluctance) surrounding the sensor. This
magnetic perturbation induces a short voltage pulse in the sensor wires, which can be measured by
a data acquisition system. One rotation corresponds to one sinusoidal voltage pulse, so as the
rotational speed increases, the voltage signal’s amplitude increases while its period decreases. If
the voltage pulses are counted for a certain amount of time, the turbocharger’s rotational speed in
rotations per minute (RPM) may be calculated.
For the airbrake dynamometer, a National Instruments™ myRIO was used to detect the
voltage pulses, and a LabVIEW Virtual Instrument (VI) was used to convert the pulses to RPM.
Figure 4-17 below shows a diagram of the JAQUET sensor as well as the voltage signal detected
by the myRIO. It was desired that instantaneous speed be displayed for the supersonic turbine
tests, so an algorithm was developed to convert rotations to RPM on the fly. The algorithm had a
while loop structure, wherein a rotation was counted if the sensor signal exceeded a threshold of
0.025 volts; this threshold was set just above the signal’s noise. For any given pulse, only the first
detected instance above the 0.025-volt threshold was counted to prevent multiple counts of the
same voltage pulse. This was accomplished with a true-false case structure, which is shown in the
VI front panel and block diagrams of Appendix G.
An additional feature in the VI allowed the user to change the RPM calculation frequency.
Low calculation frequencies were erroneous for high speeds since the speed could have many
fluctuations in the window between calculations. High calculation frequencies were erroneous for
low speeds since the calculations might occur faster than the pulse frequency. Therefore, for low
speeds (less than 5,000 RPM), it was recommended that the calculation frequency be no more than
5 Hz, but this could be tailored by the user during the test. Figure 4-18 below shows the voltage
signal and calculated speed in RPM for a signal for a simple test in which the turbocharger was
spun by hand. A comparison of calculation frequencies for the hand-spun tests is shown in 0. As
of the writing of this thesis, the RPM sensor had not been calibrated for high speeds, but this was
to be completed once the turbocharger modifications had been completed.

114

Figure 4-17: RPM sensor characteristics: (a) a diagram of the working principle, (b) the actual
RPM sensor, (c) a screenshot of the raw voltage measured with the myRIO.

Figure 4-18: Measured voltage (top) and calculated RPM (bottom) for a hand-spun test.
115

4.5.3 Torque Sensor
To measure the torque between the turbocharger compressor and the supersonic turbine, a
torque transducer sensor was required. Unlike the variable-reluctance RPM sensor in the previous
section, a torque sensor’s working principle is complex; the details are left to the reader. The
torque sensor for the airbrake dynamometer was selected in collaboration with the sponsor for the
supercritical CO2 refrigeration system, which spanned the axial bladeless and radial bladed
turbines. For a different test article, the sponsor had purchased a torque transducer from Sensor
Technologies in Oxfordshire, UK. That transducer came with a proprietary software, TorqView,
that could record the torque, speed, and power in a rotary shaft. Since that test article worked well,
the sponsor purchased a similar transducer for the turbocharger dynamometer.

4.5.4 Bearings
Since the supersonic turbomachinery was designed for high rotational speeds, the bearings
supporting the turbines had to match those speeds. Several bearing types were available; these
included roller bearings and ball bearings, which could both be configured for axial and/or radial
loads. Compared to roller bearings, ball bearings can typically reach higher speeds at the cost of
having smaller loads, but this was not an issue since the supersonic turbines needed high speeds
(up to 50,000 RPM) for small loads (less than 2.0 kN for both axial and radial directions). The
bearings selected for the test turbines were selected in collaboration with the sponsor for the
supercritical CO2 refrigeration system. The sponsor had previously interacted with The Barden
Corporation in the UK, so the bearings were selected with help from a representative from Barden.

4.5.5 Couplings
In addition to the high-speed bearing requirement, the supersonic turbines also required
high-speed couplings for the connection between the turbocharger shaft extension and the torque
sensor and the connection between the torque sensor and the test turbine. Several coupling types
were available: these included beam, bellows, disc (or disc-pack), rigid, Oldham, etc. Finding a
coupling that could sustain the speed requirement proved to be challenging; many couplings were
simply not durable enough or were more expensive than the project could afford. After contacting
a few suppliers, the project sponsor for the supercritical CO2 refrigeration system selected a disk

116

coupling from Mayr GmbH & Co KG. This coupling was rated for a nominal torque of 35 N*m,
a peak torque of 52 N*m, and a maximum operating speed of 60,000 RPM.

4.6

Fully Integrated System
After plotting the turbocharger’s performance maps (Section 4.2), designing a turbocharger

mounting system (Section 4.3), creating an oil system (Section 4.4), and selecting the apparatuses
for the instrumentation and rotating hardware (Section 4.5), it was time to assemble all components
in one integrated system. Compared to the axial turbines, the radial turbine had a more independent
test apparatus since it did not have the alignment issues posed by THOR. Therefore, the airbrake
dynamometer would be used first for the radial turbine and then the axial turbines once their new
cold-air test apparatuses were completed. The assembly containing the dynamometer, the torque
sensor, the couplings, and the radial turbine apparatus is shown in Figure 4-19 below; this assembly
was constructed with significant help from HW Webb Engineers Limited. The table represented
in the figure was a heavy welded steel table owned by PETAL, so it had no problems supporting
the airbrake dynamometer. All other components in the figure were at PETAL, with the machinist
in the UK, or soon to be purchased as of the writing of this thesis.
The instrumentation diagram for the fully integrated system is shown in Figure 4-20. On
the left, the high-pressure air would pass through a choked-flow venturi to meter the mass flow
rate entering the supersonic turbine. Just upstream and downstream of the turbine, total pressures
and temperatures would be measured to estimate the turbine’s thermodynamic power extraction.
The more precise power calculations would use the pressure and temperatures across the
turbocharger compressor. These quantities would also be measured across the turbocharger
turbine to determine its performance, although this was of lesser significance than the compressor.
The last subsystem is the oil system; here, pressure and temperature were not needed for power
calculations, but they would help determine if the turbocharger was lubricated properly and how
much energy was being lost through bearing friction or heat transfer from the airflows. Having
completed the development phase of the airbrake dynamometer, the project could be handed off
to the next graduate student researchers to conduct the testing of the supersonic turbomachinery.

117

Figure 4-19: CAD Assembly for the dynamometer, torque sensor, and radial turbine.

Figure 4-20: Instrumentation diagram for the dynamometer (courtesy of Fatih Meral).

118

5

CONCLUSION

Compared to deflagration combustion, detonation combustion offers a higher rate of
energy release, higher thermodynamic efficiency, a more compact heat release chamber, and a
pressure increase from which additional power may be extracted. Using rotating detonation
combustors in gas turbines requires novel mitigation techniques for the large heat fluxes incurred
at the detonation chamber walls as well as the fluctuations in the transonic/supersonic exhaust.
These techniques include cooling the combustor walls and new turbine architectures like the axialflow bladeless turbine, and an axial-inflow/radial-outflow bladed turbine. For this thesis research,
the three objectives were to (1) design a cooled combustor for long-duration tests, (2) design three
supersonic turbines for manufacturability, and (3) develop an airbrake dynamometer.
The first objective was fulfilled by developing the film-cooled combustor described in
Chapter 2. Past research had optimized the three-slot design with CFD and empirical quantities,
so the thesis research focused on designing the combustor for manufacturability. The film-cooled
combustor walls were 3D-printed from stainless steel, and the diverging exhaust section was CNCmachined from mild steel. The combustor instrumentation included pressure and temperature
measurements in the cooling slots and along the supersonic exhaust portion, and pressure probes
were placed in the flow straighteners between the detonation chamber and the exhaust section. A
successful test campaign showed that the three-slot film-cooling scheme was effective at limiting
the temperature rise at the combustor walls. During the tests, the maximum flow rates were 2 lbm/s
of air and hydrogen in the combustor and 0.7 lbm/s of nitrogen in the cooling slots; temperatures
remained below 310 K in the cooling slots, which exceeded 500 K for in an uncooled test. The
longest-duration test was five seconds and retained a similarly low temperature rise.
The second objective was fulfilled by modifying three supersonic turbine designs for the
applications described in Chapter 3. The axial-flow bladed turbine was designed for use in the
diverging exhaust section downstream of the film-cooled combustor. Using a blade profile from
previous work, the turbine model was created and 3D-printed from stainless steel. Additional
components such as a shaft and bearings were designed or selected. The axial-flow bladeless
turbine that had previously been optimized for a rotating detonation combustor section was
redesigned for a supercritical CO2 refrigeration cycle. The 2D wave profile was imported from
MATLAB into SOLIDWORKS, and a method for converting the profile into a helical, slightly
119

conical rotor was discovered and recorded. In a similar vein, the axial-inflow, radial-outflow
bladed turbine was optimized for the supercritical CO2 refrigeration cycle, and a method for
modifying the turbine hub for manufacturability was proposed. Both the bladeless and radial
turbines were being manufactured during the writing of this thesis.
The third objective was fulfilled by developing the airbrake dynamometer described in
Chapter 4. An industrial turbocharger had been previously donated by Cummins, and the current
research focused on adapting this turbocharger for the dynamometer. These adaptations included
a new mounting system that kept the turbocharger aligned with the other rotating hardware; a
portable oil system that could lubricate the turbocharger and test turbine bearings; and a shaft
extension that connected the turbocharger compressor with the other rotating hardware. To find
thermodynamic power, an instrumentation tube was designed for temperature and pressure
measurements at the compressor outlet; a throttle valve on the tube would modulate the power
consumed by the compressor. To find mechanical power, a variable-reluctance sensor would
measure speed and a transducer would measure torque, speed, and power. A final advancement
was the creation of a MATLAB script to plot the turbocharger’s uncorrected and corrected
performance maps, which would help calibrate the turbocharger for the supersonic turbine tests.
Having completed the research objectives, some suggestions may be made for the future
of this supersonic turbomachinery research. First, the cooled combustor should receive more tests
to determine the film-cooling scheme’s optimum operating conditions.

These tests should

implement all instrumentation ports on the 3D-printed jacket as well as the pressure probe holes
in the flow straighteners. Due to design limitations, the thermocouples on the 3D-printed jacket
can only measure the temperature on the slot walls’ coolant side, but a numerical scheme (such as
finite differences) could estimate the temperature on the slot walls’ combustion side from the slot
wall’s thermal conductivity. Alternatively, small holes could be drilled through the slot walls to
place the pressure transducers and the thermocouples in the detonation chamber. In either case,
the instrumentation should have a high response rate to fully resolve the detonation cycle.
Second, having the supersonic turbines manufactured during or after the writing of this
thesis implies that they will be tested soon. The radial turbine has a more advanced assembly than
the other turbines, but the radial turbine architecture may inspire the final assemblies for the axial
bladed and bladeless turbines. For the axial turbines, the support structures must be mounted to
the same base plate as the turbocharger and the torque sensor. The THOR stand was not used to

120

test the axial turbines because the turbines would move independently of the turbocharger; this
movement can only be avoided if the turbines and turbocharger share the same foundation. In
addition to ensuring proper alignment, each turbine must be balanced on the dynamometer stand
at an outside service before testing. Balancing and alignment are critical to safe operation.
Third, the turbocharger dynamometer must be calibrated before the turbines can be tested.
The dynamometer can measure both mechanical power and thermodynamic power, but these may
differ at the outset. In this case, the performance maps may be used to determine the turbocharger’s
expected behavior and alleviate the differences in power measurements. In addition to power, the
butterfly valve at the turbocharger compressor outlet must be calibrated. The valve has singledegree precision for the 90° sector between the open and closed positions, and these rotational
positions must be translated to the turbocharger’s throttle positions given in the performance maps.
Calibrating the power measurements and outlet valve positions will provide repeatable conditions
and lower the uncertainty of the supersonic turbine tests.
The author gained much knowledge from the multi-part design and test phases of this thesis
research. Several months were invested into SOLIDWORKS to design and redesign each turbine’s
components; many weeks went into the MATLAB development of the shaft analysis as well as
the turbocharger performance maps; and incalculable hours went into organizing all the files for
future use by PETAL members. While most of the brainstorming and troubleshooting procedures
are not documented in this thesis, the author hopes that the tangible ideas have been conveyed
without unnecessary verbiage. Finally, the author wishes that the reader may have a greater
understanding and appreciation for the components and systems required to assess the performance
of supersonic turbomachinery for rotating detonation combustors.

121

APPENDIX A. COMBUSTOR DRAWINGS

This appendix contains the drawings for the four combustor parts: the 3D-printed cooling
jacket (A.1), the eight 3D-printed exhaust flow straighteners (A.2), the CNC-machined exhaust
flange (A.3), and the CNC-machined exhaust flange window insert (A.4). For the eight exhaust
flow straighteners, the drawings are arranged according to the order in Table 2.2.

122

A.1

3D-Printed Film-Cooled Combustor

123

A.2

3D-Printed Exhaust Flow Straighteners

124

125

126

127

128

129

130

131

A.3

CNC-Machined Exhaust Flange

132

A.4

CNC-Machined Exhaust Flange Window Insert

133

APPENDIX B. COMBUSTOR TUBE DRAWINGS

This appendix contains the combustor tube drawings; these drawings were used for
reference during the tube bending, cutting, and fitting procedures. The first sheet shows four CAD
assembly views of the combustor stand and the tubing; the second sheet shows the tube
nomenclature; and the third sheet shows the important dimensions for each tube segment. Note
that the tubes for the upstream coolant chamber (which fed the first two slots) were labeled as 1#, where # indicated the tube number. Similarly, the tubes for the downstream coolant chamber
(which fed the third slot) were labeled as 2-#. The next fourteen sheets each contain the standard
four views for the tube segments made for the film-cooled combustor.

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

APPENDIX C. SUPERSONIC TURBINE DRAWINGS

This appendix contains the drawings for the four supersonic turbines: the axial inflow/
outflow bladed turbine (C.1), the axial inflow/outflow bladeless turbine (C.2), and the axial
inflow / radial outflow bladed turbine (C.3). The axial bladed turbine was 3D-printed from this
drawing; more details are contained in Section 3.1. The bladeless turbine drawing shows the
clockwise rotation of Curve 2, as described in Section 3.2. The radial turbine drawing shows an
intermediate rotor design; the shaft dimensions changed slightly for the final design, and the rotor
hub was modified according to the procedure outlined in Section 3.3. In addition to the radial
turbine rotor drawing is the shroud drawing for an intermediate design; the final shroud design
contained two pieces with the same overall dimensions as those shown in this drawing.

152

C.1

Axial Bladed Turbine

153

C.2

Axial Bladeless Turbine

154

C.3

Radial Bladed Turbine

155

156

APPENDIX D. SHAFT ANALYSIS FOR AXIAL BLADED TURBINE

The shaft analysis is separated into the following sections:
•

Section D.1 provides a component nomenclature diagram and a list of assumptions.

•

Section D.2 provides the Deflection Analysis. This utilized guidelines and equations from
Mechanics of Materials: A Lecturebook [56].

•

Section D.3 provides the Fatigue Analysis. This utilized guidelines and equations from
Shigley’s Mechanical Engineering Design [57].

D.1

Nomenclature and Assumptions

= 12

=
120

=
1

Figure D-1: Component nomenclature diagram.

157

=
20

The following assumptions were used in this shaft analysis:
1. All components had a contact width of 10 mm against the shaft. Since this was such a
small distance compared to the shaft length, the components were assumed to have point
loads (rather than distributed loads).
2. The shaft weight was negligible compared to the other forces.
3. The turbine was estimated to have a total mass of 1.5 kg, a thrust (axial force) of 1200 N,
a torque of 20 N*m, an unbalanced mass of 0.005 kg at a radius of 0.005 m from the
rotation axis, and a rotational speed of 50,000 RPM.
4. Neither the coupling nor the upstream bearing exerted an axial force, so the downstream
bearing absorbed all the turbine thrust in a stepped shoulder feature.
5. The loads exerted by the coupling on the shaft were unknown, so the linear and angular
deflections were estimated. High-speed couplings like those in the R+W Coupling Catalog
[50] tend to have maximum lateral and angular misalignments of 0.05 mm and 0.5°,
respectively. The shaft deflections caused by the coupling were set to be two and five
times smaller than the maximum lateral and angular misalignments allowed for a highspeed coupling. That is, the shaft deflections at the coupling were the following: 0.025 mm
and 0.25° for the 𝑥𝑦-plane and 0.010 mm and 0.10° for the 𝑥𝑧-plane.
6. The deflection analysis used a simple shaft with a single diameter of 12 mm; all other
stepped features were ignored.
7. The fatigue analysis retained the simple shaft diameter of 12 mm, but the notch sensitivities
at the bearings were estimated from a shoulder diameter of 18 mm between the two
bearings and a fillet radius of 1 mm for the steps between 12 mm and 18 mm. This gave a
conservative estimate for the fatigue factors of safety.
8. The shaft material was assumed to be AISI 1045 carbon steel with an elastic modulus of
200 GPa, an ultimate tensile strength of 630 MPa, and a yield strength of 530 MPa.

158

D.2

Deflection Analysis

The deflection analysis is separated into the following sections:
•

Section D.2.1 defines the external loads.

•

Section D.2.2 defines the internal loads and the boundary/continuity conditions.

•

Section D.2.3 shows the equations from equilibrium.

•

Section D.2.4 shows the equations from the first shaft segment in the 𝑥𝑦 plane.

•

Section D.2.5 shows the equations from the first shaft segment in the 𝑥𝑧 plane.

•

Section D.2.6 shows the equations from the second shaft segment in the 𝑥𝑦plane.

•

Section D.2.7 shows the equations from the second shaft segment in the 𝑥𝑧 plane.

•

Section D.2.8 shows the equations from the third shaft segment in the 𝑥𝑦 plane.

•

Section D.2.9 shows the equations from the third shaft segment in the 𝑥𝑧 plane.

•

Section D.2.10 shows the equations from the boundary and continuity equations.

•

Section D.2.11 shows an equation summary.

•

Section D.2.12 shows the results from the deflection analysis.

159

D.2.1 External Load Definitions

21

41

1

1

1

21
21

=0

41

=0

1

1

21

1
21

1

41

=
=

= 20

1

21
1

= 100

1

1

2 1
60

2

n

=
=

2

= 0.00

=

= 1.

.81 2 = 14.7

0

0.00

= 68 .4

Figure D-2: External load definitions.
Notes on the External Loads:
•

𝐹𝑖𝑗,𝑥𝑦𝑧 – external force of component 𝑖 on component 𝑗 in the 𝑥, 𝑦, or 𝑧 directions.

•

𝑀𝑖𝑗,𝑦𝑧 – external moment of component 𝑖 on component 𝑗 in the 𝑦 or 𝑧 directions.

•

𝑇𝑖𝑗,𝑥 – external torque component 𝑖 on component 𝑗 in the 𝑥 direction.

•

𝑖𝑗 may be 21, 31, 41, or 51, which correspond to loads on the shaft (1) from the coupling
(2), the turbine (3), the upstream bearing (4), and the downstream bearing (5), respectively.

•

𝛼 is the rotation angle of the shaft, or equivalently the rotation angle of the unbalanced
mass. 𝛼 = 0° at the +𝑧 axis and spins clockwise in the 𝑦𝑧 plane (-𝑥 direction) to match
the rotation direction of the turbine.

160

D.2.2 Boundary/Continuity Conditions and Internal Load Definitions

0 = 0.2 °
1 0 = 0.10°
1 0 = 0.02
1 0 = 0.010
1

=
=

1
1
1
1

=
=

2
2

2

=
=

2

2

2

=0
=0

2
2

=
=

=0
=0

Figure D-3: Boundary/continuity conditions.
Notes on the Boundary/Continuity Conditions and the Internal Loads:
•

𝑉𝑖,𝑦𝑧 (𝑥) – internal shear force in segment 𝑖 in the 𝑦 or 𝑧 directions; a function of 𝑥.

•

𝑀𝑖,𝑦𝑧 (𝑥) – internal bending moment in segment 𝑖 in the 𝑦 or 𝑧 directions; a function of 𝑥.

•

𝜃𝑖,𝑦𝑧 (𝑥) – angular deflection (slope) in segment 𝑖 in the 𝑦 or 𝑧 directions; a function of 𝑥.

•

𝑣𝑖,𝑦𝑧 (𝑥) – linear/lateral deflection in segment 𝑖 in the 𝑦 or 𝑧 directions; a function of 𝑥.

•

𝐸 – modulus of elasticity (Pa) set by the shaft material

•

𝐼 = 𝜋𝑑4 ⁄64 – Cartesian second area moment

•

𝑖 may be 1, 2, or 3, which correspond to segments 𝐴𝐵, 𝐵𝐶, and 𝐶𝐷, respectively.

•

Boundary conditions exist at the shaft ends and are created by the coupling and turbine.

•

Continuity conditions exist between the shaft ends and are created by the bearings.

•

Applying a linear deflection at the coupling creates an unknown force on the shaft.

•

Applying an angular deflection at the coupling creates an unknown moment on the shaft.

161

D.2.3 Equations from Turbine Estimations and Equilibrium

Turbine Load Estimations
𝐹31𝑥 = 1200 𝑁

(20)

𝐹31y = 𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 ⋅ n(α) − 𝐹𝑤𝑒𝑖𝑔ℎ𝑡

(21)

𝐹31𝑧 = 𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 ⋅

(α)

(22)

𝛼 = [0, 60°] (-x spin direction from +z axis)

(23)

𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 = 𝑚𝑢𝑛𝑏𝑎𝑙𝑎𝑛𝑐𝑒 ⋅ 𝜔2 ⋅ 𝑅𝑢𝑛𝑏𝑎𝑙𝑎𝑛𝑐𝑒

(24)

= (0.00 𝑘𝑔) ( 0𝑘 ⋅

2𝜋 1 2
⋅ ) (0.00 𝑚)
60 𝑠

= 68 .4 𝑁
𝑚
𝐹𝑤𝑒𝑖𝑔ℎ𝑡 = 𝑚𝑡𝑢𝑟𝑏𝑖𝑛𝑒 ⋅ 𝑔 = (1. 𝑘𝑔) ( .81 2 ) = 14.7 𝑁
𝑠

(25)

𝑇31𝑥 = 20 𝑁 ⋅ 𝑚

(26)

Equilibrium
∑ 𝐹𝑥 : 0 = 𝐹51𝑥 + 𝐹31𝑥

(27)

∑ 𝐹𝑦 : 0 = 𝐹21𝑦 + 𝐹41𝑦 + 𝐹51𝑦 + 𝐹31𝑦

(28)

∑ 𝐹𝑧 : 0 = 𝐹21𝑧 + 𝐹41𝑧 + 𝐹51𝑧 + 𝐹31𝑧

(29)

∑ 𝑀𝐴𝑥 : 0 = 𝑇21𝑥 + 𝑇31𝑥

(30)

∑ 𝑀𝐴𝑦 : 0 = −𝐿𝐴𝐵 ⋅ 𝐹41𝑧 − 𝐿𝐴𝐶 ⋅ 𝐹51𝑧 − 𝐿𝐴𝐷 ⋅ 𝐹31𝑧 + 𝑀21𝑧

(31)

∑ 𝑀𝐴𝑧 : 0 = 𝐿𝐴𝐵 ⋅ 𝐹41𝑦 + 𝐿𝐴𝐶 ⋅ 𝐹51𝑦 + 𝐿𝐴𝐷 ⋅ 𝐹31𝑦 + 𝑀21𝑥

(32)

162

D.2.4 Equations from Segment 1 in 𝒙𝒚-Plane: 𝟎 < 𝒙 < 𝑳𝑨𝑩

21

1

21
1

Figure D-4: Segment 1 in 𝑥𝑦 plane.
Shear Force in 𝑦-direction
0 = −𝑉1𝑦 (𝑥) + 𝐹21𝑦

∑ 𝐹𝑦 :

𝑉1𝑦 (𝑥) = 𝐹21𝑦

(33)

Bending Moment about Point 𝐻 in 𝑧-direction
∑ 𝑀𝐻𝑧 :

0 = 𝑀1𝑧 (𝑥) − 𝑥𝐹21𝑦 + 𝑀21𝑧

𝑀1𝑧 (𝑥) = 𝑥𝐹21𝑦 − 𝑀21𝑧 , where
𝑑𝜃1𝑦
𝑀1𝑧 (𝑥) = 𝐸𝐼
𝑑𝑥

(34)

Angular Deflection in 𝑦-direction
1
∫ 𝑀1𝑧 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑦 − 𝑀21𝑧 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
= ( 𝐹21𝑦 − 𝑥𝑀21𝑧 ) + 𝐶1
𝐸𝐼 2

𝜃1𝑦 (𝑥) =

(35)

Linear Deflection in 𝑦-direction
𝑣1𝑦 (𝑥) = ∫ 𝜃1𝑦 (𝑥) 𝑑𝑥
1 𝑥2
( 𝐹 − 𝑥𝑀21𝑧 ) + 𝐶1 ] 𝑑𝑥
𝐸𝐼 2 21𝑦
1 𝑥3
𝑥2
= ( 𝐹21𝑦 − 𝑀21𝑧 ) + 𝑥𝐶1 + 𝐶2
𝐸𝐼 6
2
= ∫[

(36)

163

D.2.5 Equations from Segment 1 in 𝒙𝒛-Plane: 𝟎 < 𝒙 < 𝑳𝑨𝑩

1

1

21
21

Figure D-5: Segment 1 in 𝑥𝑧 plane.
Shear Force in 𝑧-direction
∑ 𝐹𝑧 : 0 = −𝑉1𝑧 (𝑥) + 𝐹21𝑧
𝑉1𝑧 (𝑥) = 𝐹21𝑧

(37)

Bending Moment about Point 𝐻 in 𝑦-direction
∑ 𝑀𝐻𝑦 : 0 = −𝑀1𝑦 (𝑥) + 𝑥𝐹21𝑧 + 𝑀21𝑦
𝑀1𝑦 (𝑥) = 𝑥𝐹21𝑧 + 𝑀21𝑦 , where
𝑑𝜃1𝑧
𝑀1𝑦 (𝑥) = 𝐸𝐼
𝑑𝑥

(38)

Angular Deflection in 𝑧-direction
1
∫ 𝑀1𝑦 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑧 + 𝑀21𝑦 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
= ( 𝐹21𝑧 + 𝑥𝑀21𝑦 ) + 𝐶3
𝐸𝐼 2

𝜃1𝑧 (𝑥) =

(39)

Linear Deflection in 𝑧-direction
𝑣1𝑧 (𝑥) = ∫ 𝜃1𝑧 (𝑥) 𝑑𝑥
1 𝑥2
( 𝐹 + 𝑥𝑀21𝑦 ) + 𝐶3 ] 𝑑𝑥
𝐸𝐼 2 21𝑧
1 𝑥3
𝑥2
= ( 𝐹21𝑧 + 𝑀21𝑦 ) + 𝑥𝐶3 + 𝐶4
𝐸𝐼 6
2
= ∫[

(40)

164

D.2.6 Equations from Segment 2 in 𝒙𝒚-Plane: 𝑳𝑨𝑩 < 𝒙 < 𝑳𝑨𝑪

21

41

2

21
2

Figure D-6: Segment 2 in 𝑥𝑦 plane.
Shear Force in 𝑦-direction
∑ 𝐹𝑦 : 0 = −𝑉2𝑦 (𝑥) + 𝐹21𝑦 + 𝐹41𝑦
𝑉2𝑦 (𝑥) = 𝐹21𝑦 + 𝐹41𝑦

(41)

Bending Moment about Point 𝐻 in 𝑧-direction
∑ 𝑀𝐻𝑧 : 0 = 𝑀2𝑧 (𝑥) − 𝑥𝐹21𝑦 − (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 + 𝑀21𝑧
𝑀2𝑧 (𝑥) = 𝑥𝐹21𝑦 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 − 𝑀21𝑧 , where
𝑑𝜃2𝑦
𝑀2𝑧 (𝑥) = 𝐸𝐼
𝑑𝑥

(42)

Angular Deflection in 𝑦-direction
1
∫ 𝑀2𝑧 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑦 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 − 𝑀21𝑧 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
𝑥2
= ( 𝐹21𝑦 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑦 − 𝑥𝑀21𝑧 ) + 𝐶5
𝐸𝐼 2
2

𝜃2𝑦 (𝑥) =

(43)

Linear Deflection in 𝑦-direction
𝑣2𝑦 (𝑥) = ∫ 𝜃2𝑦 (𝑥) 𝑑𝑥
1 𝑥2
𝑥2
( 𝐹21𝑦 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑦 − 𝑥𝑀21𝑧 ) + 𝐶5 ] 𝑑𝑥
𝐸𝐼 2
2
3
3
1 𝑥
𝑥
𝑥2
𝑥2
= ( 𝐹21𝑦 + ( − 𝐿𝐴𝐵 ) 𝐹41𝑦 − 𝑀21𝑧 ) + 𝑥𝐶5 + 𝐶6
𝐸𝐼 6
6
2
2
= ∫[

165

(44)

D.2.7 Equations from Segment 2 in 𝒙𝒛-Plane: 𝑳𝑨𝑩 < 𝒙 < 𝑳𝑨𝑪

2

2

21
21

41

Figure D-7: Segment 2 in 𝑥𝑧 plane.
Shear Force in 𝑧-direction
∑ 𝐹𝑧 : 0 = −𝑉2𝑧 (𝑥) + 𝐹21𝑧 + 𝐹41𝑧
𝑉2𝑧 (𝑥) = 𝐹21𝑧 + 𝐹41𝑧

(45)

Bending Moment about Point 𝐻 in 𝑦-direction
∑ 𝑀𝐻𝑦 : 0 = −𝑀2𝑦 (𝑥) + 𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + 𝑀21𝑦
𝑀2𝑦 (𝑥) = 𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + 𝑀21𝑦 , where
𝑑𝜃2𝑧
𝑀2𝑦 (𝑥) = 𝐸𝐼
𝑑𝑥

(46)

Angular Deflection in 𝑧-direction
1
∫ 𝑀2𝑦 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + 𝑀21𝑦 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
𝑥2
= ( 𝐹21𝑧 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑧 + 𝑥𝑀21𝑦 ) + 𝐶7
𝐸𝐼 2
2

𝜃2𝑧 (𝑥) =

(47)

Linear Deflection in 𝑧-direction
𝑣2𝑧 (𝑥) = ∫ 𝜃2𝑧 (𝑥) 𝑑𝑥
1 𝑥2
𝑥2
( 𝐹21𝑧 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑧 + 𝑥𝑀21𝑦 ) + 𝐶7 ] 𝑑𝑥
𝐸𝐼 2
2
3
3
1 𝑥
𝑥
𝑥2
𝑥2
= ( 𝐹21𝑧 + ( − 𝐿𝐴𝐵 ) 𝐹41𝑧 + 𝑀21𝑦 ) + 𝑥𝐶7 + 𝐶8
𝐸𝐼 6
6
2
2
= ∫[

166

(48)

D.2.8 Equations from Segment 3 in 𝒙𝒚-Plane: 𝑳𝑨𝑪 < 𝒙 < 𝑳𝑨𝑫

21

41

1

21

Figure D-8: Segment 3 in 𝑥𝑦 plane.
Shear Force in 𝑦-direction
∑ 𝐹𝑦 : 0 = −𝑉3𝑦 (𝑥) + 𝐹21𝑦 + 𝐹41𝑦 + 𝐹51𝑦
𝑉3𝑦 (𝑥) = 𝐹21𝑦 + 𝐹41𝑦 + 𝐹51𝑦

(49)

Bending Moment about Point 𝐻 in 𝑧-direction
∑ 𝑀𝐻𝑧 : 0 = 𝑀3𝑧 (𝑥) − 𝑥𝐹21𝑦 − (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 − (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑦 + 𝑀21𝑧
𝑀3𝑧 (𝑥) = 𝑥𝐹21𝑦 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 + (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑦 − 𝑀21𝑧 , where
𝑑𝜃3𝑦
𝑀3𝑧 (𝑥) = 𝐸𝐼
𝑑𝑥

(50)

Angular Deflection in 𝑦-direction
1
∫ 𝑀3𝑧 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑦 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑦 + (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑦 − 𝑀21𝑧 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
𝑥2
𝑥2
= ( 𝐹21𝑦 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑦 + ( − 𝑥𝐿𝐴𝐶 ) 𝐹51𝑦 − 𝑥𝑀21𝑧 ) + 𝐶9
𝐸𝐼 2
2
2

𝜃3𝑦 (𝑥) =

(51)

Linear Deflection in 𝑦-direction
𝑣3𝑦 (𝑥) = ∫ 𝜃3𝑦 (𝑥) 𝑑𝑥
1 𝑥2
𝑥2
𝑥2
( 𝐹21𝑦 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑦 + ( − 𝑥𝐿𝐴𝐶 ) 𝐹51𝑦 − 𝑥𝑀21𝑧 ) + 𝐶9 ] 𝑑𝑥
𝐸𝐼 2
2
2
3
3
2
3
1 𝑥
𝑥
𝑥
𝑥
𝑥2
𝑥2
= ( 𝐹21𝑦 + ( − 𝐿𝐴𝐵 ) 𝐹41𝑦 + ( − 𝐿𝐴𝐶 ) 𝐹51𝑦 − 𝑀21𝑧 ) + 𝑥𝐶9 + 𝐶10
𝐸𝐼 6
6
2
6
2
2
= ∫[

167

(52)

D.2.9 Equations from Segment 3 in 𝒙𝒛-Plane: 𝑳𝑨𝑪 < 𝒙 < 𝑳𝑨𝑫

21
21

41

1

Figure D-9: Segment 3 in 𝑥𝑧 plane.
Shear Force in 𝑧-direction
∑ 𝐹𝑧 : 0 = −𝑉3𝑧 (𝑥) + 𝐹21𝑧 + 𝐹41𝑧 + 𝐹51𝑧
𝑉3𝑧 (𝑥) = 𝐹21𝑧 + 𝐹41𝑧 + 𝐹51𝑧

(53)

Bending Moment about Point 𝐻 in 𝑦-direction
∑ 𝑀𝐻𝑦 : 0 = −𝑀3𝑦 (𝑥) + 𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑧 + 𝑀21𝑦
𝑀3𝑦 (𝑥) = 𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑧 + 𝑀21𝑦 , where
𝑑𝜃3𝑧
𝑀3𝑦 (𝑥) = 𝐸𝐼
𝑑𝑥

(54)

Angular Deflection in 𝑧-direction
1
∫ 𝑀3𝑦 (𝑥) 𝑑𝑥
𝐸𝐼
1
= ∫[𝑥𝐹21𝑧 + (𝑥 − 𝐿𝐴𝐵 )𝐹41𝑧 + (𝑥 − 𝐿𝐴𝐶 )𝐹51𝑧 + 𝑀21𝑦 ] 𝑑𝑥
𝐸𝐼
1 𝑥2
𝑥2
𝑥2
= ( 𝐹21𝑧 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑧 + ( − 𝑥𝐿𝐴𝐶 ) 𝐹51𝑧 + 𝑥𝑀21𝑧 ) + 𝐶11
𝐸𝐼 2
2
2

𝜃3𝑧 (𝑥) =

(55)

Linear Deflection in 𝑧-direction
𝑣3𝑧 (𝑥) = ∫ 𝜃3𝑧 (𝑥) 𝑑𝑥
1 𝑥2
𝑥2
𝑥2
( 𝐹21𝑧 + ( − 𝑥𝐿𝐴𝐵 ) 𝐹41𝑧 + ( − 𝑥𝐿𝐴𝐶 ) 𝐹51𝑧 + 𝑥𝑀21𝑦 ) + 𝐶9 ] 𝑑𝑥
𝐸𝐼 2
2
2
3
3
2
3
1 𝑥
𝑥
𝑥
𝑥
𝑥2
𝑥2
= ( 𝐹21𝑧 + ( − 𝐿𝐴𝐵 ) 𝐹41𝑧 + ( − 𝐿𝐴𝐶 ) 𝐹51𝑧 + 𝑀21𝑦 ) + 𝑥𝐶11 + 𝐶12
𝐸𝐼 6
6
2
6
2
2
= ∫[

168

(56)

D.2.10 Equations from Boundary and Continuity Conditions
Applying the conditions listed below to the equations from the previous sections created
the remaining equations needed to solve for the unknown external and internal loads.

Table D.1: Coupling boundary conditions.
#

Coupling Condition

#

Coupling Condition

1

𝜃1𝑦 (0) = 0.2 °

3

𝑣1𝑦 (0) = 0.02 𝑚𝑚

2

𝜃1𝑧 (0) = 0.10°

4

𝑣1𝑧 (0) = 0.010 𝑚𝑚

Table D.2: Bearing continuity conditions; bearings have angular (𝜃), not linear (𝑣), deflection.
#

Bearing Condition

#

Bearing Condition

#

Bearing Condition

1

𝜃1𝑦 (𝐿𝐴𝐵 ) = 𝜃2𝑦 (𝐿𝐴𝐵 )

5

𝑣1𝑦 (𝐿𝐴𝐵 ) = 0

9

𝑣2𝑦 (𝐿𝐴𝐵 ) = 0

2

𝜃1𝑧 (𝐿𝐴𝐵 ) = 𝜃2𝑧 (𝐿𝐴𝐵 )

6

𝑣1𝑧 (𝐿𝐴𝐵 ) = 0

10

𝑣2𝑧 (𝐿𝐴𝐵 ) = 0

3

𝜃2𝑦 (𝐿𝐴𝐶 ) = 𝜃3𝑦 (𝐿𝐴𝐶 )

7

𝑣2𝑦 (𝐿𝐴𝐶 ) = 0

11

𝑣3𝑦 (𝐿𝐴𝐶 ) = 0

4

𝜃2𝑧 (𝐿𝐴𝐶 ) = 𝜃3𝑧 (𝐿𝐴𝐶 )

8

𝑣2𝑧 (𝐿𝐴𝐶 ) = 0

12

𝑣3𝑧 (𝐿𝐴𝐶 ) = 0

Coupling Boundary Condition #1: 𝜃1𝑦 (0) = 0.2 °
0.2 ⋅

𝜋
1 02
= ( 𝐹21𝑦 − 0 ⋅ 𝑀21𝑧 ) + 𝐶1
180 𝐸𝐼 2
= 𝐶1

(57)

Coupling Boundary Condition #2: 𝑣1𝑦 (0) = 0.10°
0.10 ⋅

𝜋
1 03
02
= ( 𝐹21𝑦 − 𝑀21𝑧 ) + 0 ⋅ 𝐶1 + 𝐶2
180 𝐸𝐼 6
2
= 𝐶2

(58)

Coupling Boundary Condition #3: 𝜃1𝑧 (0) = 0.02 𝑚𝑚
1 02
( 𝐹 + 0 ⋅ 𝑀21𝑦 ) + 𝐶3
𝐸𝐼 2 21𝑧
= 𝐶3

0.02 𝑚𝑚 =

(59)

Coupling Boundary Condition #4: 𝑣1𝑧 (0) = 0.010 𝑚𝑚
1 03
02
( 𝐹21𝑧 + 𝑀21𝑦 ) + 0 ⋅ 𝐶3 + 𝐶4
𝐸𝐼 6
2
= 𝐶4

0.010 𝑚𝑚 =

169

(60)

Bearing Boundary Condition #1: 𝜃1𝑦 (𝐿𝐴𝐵 ) = 𝜃2𝑦 (𝐿𝐴𝐵 )
1 𝐿2𝐴𝐵
1 𝐿2𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑦 − 𝐿𝐴𝐵 𝑀21𝑧 ) + 𝐶1 =
(
𝐹21𝑦 + (
− 𝐿𝐴𝐵 𝐿𝐴𝐵 ) 𝐹41𝑦 − 𝐿𝐴𝐵 𝑀21𝑧 ) + 𝐶5
𝐸𝐼 2
𝐸𝐼 2
2
𝐿2𝐴𝐵
0=−
𝐹 − 𝐶1 + 𝐶5
2𝐸𝐼 41𝑦

(61)

Bearing Boundary Condition #2: 𝜃1𝑧 (𝐿𝐴𝐵 ) = 𝜃2𝑧 (𝐿𝐴𝐵 )

1 𝐿2𝐴𝐵
1 𝐿2𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑧 + 𝐿𝐴𝐵 𝑀21𝑦 ) + 𝐶3 = (
𝐹21𝑧 + (
− 𝐿2𝐴𝐵 ) 𝐹41𝑧 + 𝐿𝐴𝐵 𝑀21𝑦 ) + 𝐶7
𝐸𝐼 2
𝐸𝐼 2
2
𝐿2𝐴𝐵
0=−
𝐹 − 𝐶3 + 𝐶7
2𝐸𝐼 41𝑧

(62)

Bearing Boundary Condition #3: 𝜃2𝑦 (𝐿𝐴𝐶 ) = 𝜃3𝑦 (𝐿𝐴𝐶 )
1 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑦 + (
− 𝐿𝐴𝐶 𝐿𝐴𝐵 ) 𝐹41𝑦 − 𝐿𝐴𝐶 𝑀21𝑧 ) + 𝐶5
𝐸𝐼 2
2
1 𝐿2𝐴𝐶
𝐿2𝐴𝐶
𝐿2𝐴𝐶
= (
𝐹21𝑦 + (
− 𝐿𝐴𝐶 𝐿𝐴𝐵 ) 𝐹41𝑦 + (
− 𝐿𝐴𝐶 𝐿𝐴𝐶 ) 𝐹51𝑦 − 𝐿𝐴𝐶 𝑀21𝑧 ) + 𝐶9
𝐸𝐼 2
2
2
𝐿2𝐴𝐶
0=−
𝐹 − 𝐶5 + 𝐶9
2𝐸𝐼 51𝑦

(63)

Bearing Boundary Condition #4: 𝜃2𝑧 (𝐿𝐴𝐶 ) = 𝜃3𝑧 (𝐿𝐴𝐶 )

1 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑧 + (
− 𝐿𝐴𝐶 𝐿𝐴𝐵 ) 𝐹41𝑧 + 𝐿𝐴𝐶 𝑀21𝑦 ) + 𝐶7
𝐸𝐼 2
2
1 𝐿2𝐴𝐶
𝐿2𝐴𝐶
𝐿2𝐴𝐶
= (
𝐹21𝑧 + (
− 𝐿𝐴𝐶 𝐿𝐴𝐵 ) 𝐹41𝑧 + (
− 𝐿2𝐴𝐶 ) 𝐹51𝑧 + 𝐿𝐴𝐶 𝑀21𝑦 ) + 𝐶11
𝐸𝐼 2
2
2
𝐿2𝐴𝐶
0=−
𝐹 − 𝐶7 + 𝐶11
2𝐸𝐼 51𝑧

(64)

Bearing Boundary Condition #5: 𝑣1𝑦 (𝐿𝐴𝐵 ) = 0
1 𝐿3𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑦 −
𝑀 ) + 𝐿𝐴𝐵 𝐶1 + 𝐶2
𝐸𝐼 6
2 21𝑧
𝐿3𝐴𝐵
=
(𝐹 −
𝑀 ) + 𝐿𝐴𝐵 𝐶1 + 𝐶2
6𝐸𝐼 21𝑦 𝐿𝐴𝐵 21𝑧

0=

(65)

Bearing Boundary Condition #6: 𝑣1𝑧 (𝐿𝐴𝐵 ) = 0
1 𝐿3𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑧 +
𝑀 ) + 𝐿𝐴𝐵 𝐶3 + 𝐶4
𝐸𝐼 6
2 21𝑦
𝐿3𝐴𝐵
=
(𝐹 +
𝑀 ) + 𝐿𝐴𝐵 𝐶3 + 𝐶4
6𝐸𝐼 21𝑧 𝐿𝐴𝐵 21𝑦

0=

(66)

Bearing Boundary Condition #7: 𝑣2𝑦 (𝐿𝐴𝐵 ) = 0
1 𝐿3𝐴𝐵
𝐿3𝐴𝐵 𝐿2𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑦 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑦 −
𝑀 ) + 𝐿𝐴𝐵 𝐶5 + 𝐶6
𝐸𝐼 6
6
2
2 21𝑧
𝐿3𝐴𝐵
=
(𝐹 − 2𝐹41𝑦 −
𝑀 ) + 𝐿𝐴𝐵 𝐶5 + 𝐶6
6𝐸𝐼 21𝑦
𝐿𝐴𝐵 21𝑧

0=

170

(67)

Bearing Boundary Condition #8: 𝑣2𝑧 (𝐿𝐴𝐵 ) = 0
0=
=

1 𝐿3𝐴𝐵
𝐿3𝐴𝐵 𝐿2𝐴𝐵
𝐿2𝐴𝐵
(
𝐹21𝑧 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑧 +
𝑀 ) + 𝐿𝐴𝐵 𝐶7 + 𝐶8
𝐸𝐼 6
6
2
2 21𝑦

𝐿3𝐴𝐵
(𝐹 − 2𝐹41𝑧 +
𝑀 ) + 𝐿𝐴𝐵 𝐶7 + 𝐶8
6𝐸𝐼 21𝑧
𝐿𝐴𝐵 21𝑦

(68)

Bearing Boundary Condition #9: 𝑣2𝑦 (𝐿𝐴𝐶 ) = 0
1 𝐿3𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑦 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑦 −
𝑀 ) + 𝐿𝐴𝐶 𝐶5 + 𝐶6
𝐸𝐼 6
6
2
2 21𝑧
𝐿3𝐴𝐶
𝐿𝐴𝐵
=
(𝐹 + (1 −
) 𝐹41𝑦 −
𝑀 ) + 𝐿𝐴𝐶 𝐶5 + 𝐶6
6𝐸𝐼 21𝑦
𝐿𝐴𝐶
𝐿𝐴𝐶 21𝑧

0=

(69)

Bearing Boundary Condition #10: 𝑣2𝑧 (𝐿𝐴𝐶 ) = 0

1 𝐿3𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑧 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑧 +
𝑀 ) + 𝐿𝐴𝐶 𝐶7 + 𝐶8
𝐸𝐼 6
6
2
2 21𝑦
𝐿3𝐴𝐶
𝐿𝐴𝐵
=
(𝐹21𝑧 + (1 −
) 𝐹41𝑧 +
𝑀 ) + 𝐿𝐴𝐶 𝐶7 + 𝐶8
6𝐸𝐼
𝐿𝐴𝐶
𝐿𝐴𝐶 21𝑦

0=

(70)

Bearing Boundary Condition #11: 𝑣3𝑦 (𝐿𝐴𝐶 ) = 0
1 𝐿3𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑦 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑦 + (
−
𝐿𝐴𝐶 ) 𝐹51𝑦 −
𝑀 ) + 𝐿𝐴𝐶 𝐶9 + 𝐶10
𝐸𝐼 6
6
2
6
2
2 21𝑧
𝐿3𝐴𝐶
𝐿𝐴𝐵
=
(𝐹 + (1 −
) 𝐹41𝑦 − 2𝐹51𝑦 −
𝑀 ) + 𝐿𝐴𝐶 𝐶9 + 𝐶10
6𝐸𝐼 21𝑦
𝐿𝐴𝐶
𝐿𝐴𝐶 21𝑧

0=

(71)

Bearing Boundary Condition #12: 𝑣3𝑧 (𝐿𝐴𝐶 ) = 0

1 𝐿3𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿3𝐴𝐶 𝐿2𝐴𝐶
𝐿2𝐴𝐶
(
𝐹21𝑧 + (
−
𝐿𝐴𝐵 ) 𝐹41𝑧 + (
−
𝐿𝐴𝐶 ) 𝐹51𝑧 +
𝑀 ) + 𝐿𝐴𝐶 𝐶11 + 𝐶12
𝐸𝐼 6
6
2
6
2
2 21𝑦
𝐿3𝐴𝐶
𝐿𝐴𝐵
=
(𝐹21𝑧 + (1 −
) 𝐹41𝑧 − 2𝐹51𝑧 +
𝑀 ) + 𝐿𝐴𝐶 𝐶11 + 𝐶12
6𝐸𝐼
𝐿𝐴𝐶
𝐿𝐴𝐶 21𝑦

0=

171

(72)

D.2.11 Equation Summary
All the following equations were presented in previous sections, so the equation numbers
do not advance in this section. These equations were rearranged into matrix-vector form and
solved with MATLAB. Then the internal quantities (shear force, bending moment, angular
deflection, and linear deflection) were found at discrete points along the shaft to get the plots in
the next section.

Turbine Load Estimations
𝐹31𝑥 = 1200 𝑁

(20)

𝐹31y = 𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 ⋅ n(α) − 𝐹𝑤𝑒𝑖𝑔ℎ𝑡

(21)

𝐹31𝑧 = 𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 ⋅

(α)

(22)

𝛼 = [0, 60°] (-x spin direction from +z axis)

(23)

𝐹𝑐𝑒𝑛𝑡𝑟𝑖𝑓𝑢𝑔𝑎𝑙 = 𝑚𝑢𝑛𝑏𝑎𝑙𝑎𝑛𝑐𝑒 ⋅ 𝜔2 ⋅ 𝑅𝑢𝑛𝑏𝑎𝑙𝑎𝑛𝑐𝑒 = 68 .4 𝑁

(24)

𝑚
𝐹𝑤𝑒𝑖𝑔ℎ𝑡 = 𝑚𝑡𝑢𝑟𝑏𝑖𝑛𝑒 ⋅ 𝑔 = (1. 𝑘𝑔) ( .81 2 ) = 14.7 𝑁
𝑠

(25)

𝑇31𝑥 = 20 𝑁 ⋅ 𝑚

(26)

Equilibrium Equations:
∑ 𝐹𝑥 : 0 = 𝐹51𝑥 + 𝐹31𝑥

(27)

∑ 𝐹𝑦 : 0 = 𝐹21𝑦 + 𝐹41𝑦 + 𝐹51𝑦 + 𝐹31𝑦

(28)

∑ 𝐹𝑧 : 0 = 𝐹21𝑧 + 𝐹41𝑧 + 𝐹51𝑧 + 𝐹31𝑧

(29)

∑ 𝑀𝐴𝑥 : 0 = 𝑇21𝑥 + 𝑇31𝑥

(30)

∑ 𝑀𝐴𝑦 : 0 = −𝐿𝐴𝐵 ⋅ 𝐹41𝑧 − 𝐿𝐴𝐶 ⋅ 𝐹51𝑧 − 𝐿𝐴𝐷 ⋅ 𝐹31𝑧 + 𝑀21𝑧

(31)

∑ 𝑀𝐴𝑧 : 0 = 𝐿𝐴𝐵 ⋅ 𝐹41𝑦 + 𝐿𝐴𝐶 ⋅ 𝐹51𝑦 + 𝐿𝐴𝐷 ⋅ 𝐹31𝑦 + 𝑀21𝑥

(32)

172

Coupling Boundary Conditions:
𝜋
𝐶1 = 0.2 ⋅
180
𝜋
𝐶2 = 0.10 ⋅
180

(57)
(58)

𝐶3 = 2. ⋅ 10−5 𝑚

(59)

𝐶4 = 1.0 ⋅ 10−5 𝑚

(60)

Bearing Boundary Conditions:
0=−

𝐿2𝐴𝐵
𝐹 − 𝐶1 + 𝐶5
2𝐸𝐼 41𝑦

(61)

0=−

𝐿2𝐴𝐵
𝐹 − 𝐶3 + 𝐶7
2𝐸𝐼 41𝑧

(62)

𝐿2𝐴𝐶
0=−
𝐹 − 𝐶5 + 𝐶9
2𝐸𝐼 51𝑦

(63)

𝐿2𝐴𝐶
0=−
𝐹 − 𝐶7 + 𝐶11
2𝐸𝐼 51𝑧

(64)

𝐿3𝐴𝐵
(𝐹 −
0=
𝑀 ) + 𝐿𝐴𝐵 𝐶1 + 𝐶2
6𝐸𝐼 21𝑦 𝐿𝐴𝐵 21𝑧

(65)

0=

𝐿3𝐴𝐵
(𝐹 +
𝑀 ) + 𝐿𝐴𝐵 𝐶3 + 𝐶4
𝐸𝐼 21𝑧 𝐿𝐴𝐵 21𝑦

(66)

0=

𝐿3𝐴𝐵
(𝐹 − 2𝐹41𝑦 −
𝑀 ) + 𝐿𝐴𝐵 𝐶5 + 𝐶6
6𝐸𝐼 21𝑦
𝐿𝐴𝐵 21𝑧

(67)

𝐿3𝐴𝐵
(𝐹 − 2𝐹41𝑧 +
0=
𝑀 ) + 𝐿𝐴𝐵 𝐶7 + 𝐶8
6𝐸𝐼 21𝑧
𝐿𝐴𝐵 21𝑦

(68)

𝐿3𝐴𝐶
𝐿𝐴𝐵
(𝐹21𝑦 + (1 −
)𝐹 −
𝑀 ) + 𝐿𝐴𝐶 𝐶5 + 𝐶6
6𝐸𝐼
𝐿𝐴𝐶 41𝑦 𝐿𝐴𝐶 21𝑧

(69)

𝐿3𝐴𝐶
𝐿𝐴𝐵
(𝐹21𝑧 + (1 −
)𝐹 +
0=
𝑀 ) + 𝐿𝐴𝐶 𝐶7 + 𝐶8
6𝐸𝐼
𝐿𝐴𝐶 41𝑧 𝐿𝐴𝐶 21𝑦

(70)

0=

0=

𝐿3𝐴𝐶
𝐿𝐴𝐵
(𝐹21𝑦 + (1 −
) 𝐹 − 2𝐹51𝑦 −
𝑀 ) + 𝐿𝐴𝐶 𝐶9 + 𝐶10
6𝐸𝐼
𝐿𝐴𝐶 41𝑦
𝐿𝐴𝐶 21𝑧

(71)

0=

𝐿3𝐴𝐶
𝐿𝐴𝐵
(𝐹21𝑧 + (1 −
) 𝐹 − 2𝐹51𝑧 +
𝑀 ) + 𝐿𝐴𝐶 𝐶11 + 𝐶12
6𝐸𝐼
𝐿𝐴𝐶 41𝑧
𝐿𝐴𝐶 21𝑦

(72)

173

D.2.12 Deflection Analysis Results
The deflection analysis results are presented in an array of figures and tables. The first
three figures show the external loads on the shaft created by the coupling, bearings, and turbine.
The next two figures show the internal loads, including the axial force, torque, shear force, and
bending moment. The last figure shows the angular and linear deflection across the span of the
shaft. Below the figures, three tables list the external loads, the internal loads, and the angular and
linear deflections at 30° rotation increments. (Recall that the shaft rotates in the -𝑥 direction with
𝛼 = 0° aligned with the +𝑧 axis.) For the internal loads and deflections tables, only the quantities
at the component locations are shown; the values for all discrete points along the shaft are omitted
from this thesis to conserve space.

Figure D-10: External load variable sign conventions.

174

Figure D-11: External loads for an unbalance rotation angle of 0°.

Figure D-12: External loads for an unbalance rotation angle of 45°.

175

Figure D-13: External loads for an unbalance rotation angle of 270°.

Figure D-14: Internal axial force and torque diagrams.

176

Figure D-15: Shear force and bending moment diagrams.

Figure D-16: Angular and linear deflections diagrams.

177

Table D.3: External loads on the shaft.

178

α (°)

F21y
(N)

F21z
(N)

F31x
(N)

F31y
(N)

0
30
60
90
120
150
180
210
240
270
300
330
360

262.0
232.6
211.2
203.3
211.2
232.6
262.0
291.3
312.7
320.6
312.7
291.3
262.0

45.7
53.5
75.0
104.3
133.6
155.0
162.9
155.0
133.6
104.3
75.0
53.5
45.7

1200
1200
1200
1200
1200
1200
1200
1200
1200
1200
1200
1200
1200

-14.7 685.4 -291.4 37.7 -1200 44.1 -768.8
328.0 593.6 -214.9 17.2 -1200 -345.7 -664.3
578.8 342.7 -158.9 -38.8 -1200 -631.1 -378.9
670.7 0.0 -138.4 -115.2 -1200 -735.6 11.0
578.8 -342.7 -158.9 -191.7 -1200 -631.1 400.8
328.0 -593.6 -214.9 -247.7 -1200 -345.7 686.2
-14.7 -685.4 -291.4 -268.2 -1200 44.1 790.7
-357.4 -593.6 -367.9 -247.7 -1200 434.0 686.2
-608.3 -342.7 -423.9 -191.7 -1200 719.4 400.8
-700.1 0.0 -444.4 -115.2 -1200 823.9 11.0
-608.3 342.7 -423.9 -38.8 -1200 719.4 -378.9
-357.4 593.6 -367.9 17.2 -1200 434.0 -664.3
-14.7 685.4 -291.4 37.7 -1200 44.1 -768.8

F31z
(N)

F41y
(N)

F41z
(N)

F51x
(N)

F51y
(N)

F51z T21x T31x M21y M21z
(N) (N-m) (N-m) (N-m) (N-m)
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0
20.0

-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0

-8.0
-8.3
-9.2
-10.4
-11.5
-12.4
-12.7
-12.4
-11.5
-10.4
-9.2
-8.3
-8.0

26.0
24.8
24.0
23.6
24.0
24.8
26.0
27.2
28.0
28.3
28.0
27.2
26.0

Table D.4: Internal shear forces and bending moments within the shaft.
α
(°)

179

0
30
60
90
120
150
180
210
240
270
300
330
360

VAy
(N)
262.0
232.6
211.2
203.3
211.2
232.6
262.0
291.3
312.7
320.6
312.7
291.3
262.0

VBy VCy VDy VAz
(N)
(N)
(N)
(N)
262.0 -29.4 14.7 45.7
232.6 17.7 -328.0 53.5
211.2 52.3 -578.8 75.0
203.3 64.9 -670.7 104.3
211.2 52.3 -578.8 133.6
232.6 17.7 -328.0 155.0
262.0 -29.4 14.7 162.9
291.3 -76.6 357.4 155.0
312.7 -111.1 608.3 133.6
320.6 -123.8 700.1 104.3
312.7 -111.1 608.3 75.0
291.3 -76.6 357.4 53.5
262.0 -29.4 14.7 45.7

VBz
VCz
VDz MAz MBz MCz MDz MAy MBy MCy MDy
(N)
(N)
(N) (N-m) (N-m) (N-m) (N-m) (N-m) (N-m) (N-m) (N-m)
45.7 83.4 -685.4 -26.0 5.4
-0.3
0.0
-8.0 -2.6 13.7
0.0
53.5 70.7 -593.6 -24.8 3.1
6.6
0.0
-8.3 -1.9 11.9
0.0
75.0 36.2 -342.7 -24.0 1.4
11.6
0.0
-9.2 -0.2
6.9
0.0
104.3 -11.0 0.0 -23.6 0.8
13.4
0.0 -10.4 2.1
0.0
0.0
133.6 -58.1 342.7 -24.0 1.4
11.6
0.0 -11.5 4.5
-6.9
0.0
155.0 -92.7 593.6 -24.8 3.1
6.6
0.0 -12.4 6.2 -11.9 0.0
162.9 -105.3 685.4 -26.0 5.4
-0.3
0.0 -12.7 6.8 -13.7 0.0
155.0 -92.7 593.6 -27.2 7.8
-7.1
0.0 -12.4 6.2 -11.9 0.0
133.6 -58.1 342.7 -28.0 9.5 -12.2 0.0 -11.5 4.5
-6.9
0.0
104.3 -11.0 0.0 -28.3 10.1 -14.0 0.0 -10.4 2.1
0.0
0.0
75.0 36.2 -342.7 -28.0 9.5 -12.2 0.0
-9.2 -0.2
6.9
0.0
53.5 70.7 -593.6 -27.2 7.8
-7.1
0.0
-8.3 -1.9 11.9
0.0
45.7 83.4 -685.4 -26.0 5.4
-0.3
0.0
-8.0 -2.6 13.7
0.0

Table D.5: Angular and linear deflections at the component cross-sections.
α
(°)
0
30
60
90
120

180

150
180
210
240
270
300
330
360

θAy
(rad)
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03
4.36
E-03

θBy
(rad)
-1.69
E-03
-2.04
E-03
-2.29
E-03
-2.38
E-03
-2.29
E-03
-2.04
E-03
-1.69
E-03
-1.35
E-03
-1.09
E-03
-1.00
E-03
-1.09
E-03
-1.35
E-03
-1.69
E-03

θCy
(rad)
7.75
E-04
2.59
E-03
3.92
E-03
4.40
E-03
3.92
E-03
2.59
E-03
7.75
E-04
-1.04
E-03
-2.37
E-03
-2.85
E-03
-2.37
E-03
-1.04
E-03
7.75
E-04

θDy
(rad)
7.61
E-04
2.91
E-03
4.49
E-03
5.06
E-03
4.49
E-03
2.91
E-03
7.61
E-04
-1.39
E-03
-2.96
E-03
-3.54
E-03
-2.96
E-03
-1.39
E-03
7.61
E-04

θAz
(rad)
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03
1.75
E-03

θBz
(rad)
-1.37
E-03
-1.28
E-03
-1.03
E-03
-6.83
E-04
-3.37
E-04
-8.41
E-05
8.46
E-06
-8.41
E-05
-3.37
E-04
-6.83
E-04
-1.03
E-03
-1.28
E-03
-1.37
E-03

θCz
(rad)
3.97
E-03
3.48
E-03
2.16
E-03
3.41
E-04
-1.47
E-03
-2.80
E-03
-3.29
E-03
-2.80
E-03
-1.47
E-03
3.41
E-04
2.16
E-03
3.48
E-03
3.97
E-03

θDz
(rad)
4.64
E-03
4.07
E-03
2.49
E-03
3.41
E-04
-1.81
E-03
-3.38
E-03
-3.96
E-03
-3.38
E-03
-1.81
E-03
3.41
E-04
2.49
E-03
4.07
E-03
4.64
E-03

vAy
(m)
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05
2.50
E-05

vBy
(m)
-6.44
E-20
-1.73
E-19
2.61
E-19
1.52
E-19
-1.73
E-19
-1.73
E-19
-1.73
E-19
-1.73
E-19
-7.15
E-19
-7.15
E-19
-9.32
E-19
-6.44
E-20
-6.44
E-20

vCy
(m)
4.88
E-19
-5.96
E-18
4.34
E-18
-1.54
E-18
4.88
E-19
-5.96
E-18
-2.66
E-18
-2.60
E-18
3.25
E-18
4.55
E-18
2.17
E-18
-2.93
E-18
-5.42
E-19

vDy
(m)
1.53
E-05
5.61
E-05
8.59
E-05
9.69
E-05
8.59
E-05
5.61
E-05
1.53
E-05
-2.55
E-05
-5.53
E-05
-6.62
E-05
-5.53
E-05
-2.55
E-05
1.53
E-05

vAz
(m)
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05
1.00
E-05

vBz
(m)
-4.05
E-19
-5.68
E-19
-9.47
E-19
-2.54
E-20
3.54
E-19
9.77
E-19
1.03
E-18
8.96
E-19
-2.15
E-19
-5.25
E-20
-9.47
E-19
-2.15
E-19
-4.05
E-19

vCz
(m)
6.95
E-18
4.34
E-18
-6.78
E-20
-5.42
E-20
1.30
E-18
-4.01
E-18
-2.55
E-18
-5.64
E-18
-3.09
E-18
-4.61
E-19
-6.78
E-20
-3.25
E-18
6.95
E-18

vDz
(m)
8.84
E-05
7.74
E-05
4.76
E-05
6.83
E-06
-3.39
E-05
-6.38
E-05
-7.47
E-05
-6.38
E-05
-3.39
E-05
6.83
E-06
4.76
E-05
7.74
E-05
8.84
E-05

D.3

Fatigue Analysis

The fatigue analysis is separated into the following sections:
•

Section D.3.1 tabulates all variables used in the fatigue analysis,

•

Section D.3.2 shows the locations of the twelve critical elements for each critical section.

•

Section D.3.3 shows the results from the fatigue analysis.

D.3.1 Variable Definitions
The table below lists all variables used in the fatigue analysis, including the variable
symbols, meanings, equations, and reference numbers from Shigley’s Mechanical Engineering
Design [57]. More information on the stress-life method may be found in Chapter 6 of [57];
Section 6-19 provides a step-by-step procedure for fatigue analyses.

Table D.6: Definitions of variables used in fatigue analysis.
Symbol

Meaning

Equation / Value

Ref. #
in [57]

𝑑

shaft diameter

𝑑 = 0.012 𝑚

NA

𝐴

cross-sectional area

𝐴 = 𝜋𝑑 2 ⁄4

NA

𝛼 = [0°: 1°: 60°]
rotation angle of the shaft
or the unbalanced mass where 𝛼 = 0° is aligned with +z axis and increases
clockwise in 𝑦𝑧 plane (-𝑥 direction); 𝛼 ≠ 𝛾

NA

𝛾 = [0°: 0°: 60°]
where 𝛾 = 0° is aligned with +z axis and increases
clockwise in 𝑦𝑧 plane (-𝑥 direction); 𝛾 ≠ 𝛼

NA

𝑉𝑦 or 𝑉𝑧

internal shear forces in 𝑦 / See Deflection Analysis for tables of 𝑉𝑦 and 𝑉𝑧 at
𝑧 directions, respectively
cross-sections 𝐴, 𝐵, 𝐶, and 𝐷.

NA

𝑀𝑦 or 𝑀𝑧

bending moments in 𝑥𝑧 /
See Deflection Analysis for tables of 𝑀𝑦 and 𝑀𝑧 at
𝑥𝑦 planes (moment
cross-sections 𝐴, 𝐵, 𝐶, and 𝐷.
vectors in 𝑦 / 𝑧 directions)

NA

𝛼

𝛾

angular increment
between the critical
elements

𝛽

angle between +𝑧 axis and
neutral axis

𝑀𝑅

resultant bending moment
(moment vector along
neutral axis)

𝛽 = tan−1 (

𝑀𝑦
)
𝑀𝑧

1
2
2 2
𝑀𝑅 = (𝑀𝑧 + 𝑀𝑦 )

181

NA

NA

Table D.6 Continued
Symbol

Meaning

Cartesian second area
𝐼𝑦 or 𝐼𝑧 moments about 𝑦 / 𝑧 axes
for a circular shaft

Equation / Value

Ref. #
in [57]

𝜋𝑑 4
64

Tab.
A-18

𝐼𝑦 = 𝐼𝑧 = 𝐼 =

𝜋𝑑 4
𝐽=
2
𝐹𝑎𝑥𝑖𝑎𝑙
𝐹𝑎𝑥𝑖𝑎𝑙
𝜎𝑎𝑥𝑖𝑎𝑙 =
=
𝐴
𝜋𝑑 2 ⁄4

𝐽

polar second area moment
for a circular shaft

𝜎𝑎𝑥𝑖𝑎𝑙

axial force normal stress
in 𝑥 direction

𝜎𝑏𝑒𝑛𝑑

𝑀𝑦 𝑧 𝑀𝑧 𝑦
−
bending moment normal 𝜎𝑏𝑒𝑛𝑑 =
𝐼𝑦
𝐼𝑧
stress in 𝑥 direction; max
4
𝜋𝑑
𝑑
at outer surface
(𝑀𝑦 ⋅ ⋅
=
64
2

(𝛾) − 𝑀𝑧 ⋅

Eq.
3-22

𝑑
⋅ n(𝛾))
2

Eq.
3-27

𝜎𝑡𝑜𝑡

total normal stress in 𝑥
direction

𝜎𝑡𝑜𝑡 = 𝜎𝑎𝑥𝑖𝑎𝑙 + 𝜎𝑏𝑒𝑛𝑑

NA

𝜎𝑚𝑖𝑛

minimum normal stress

n(𝜎)

NA

𝜎𝑚𝑎𝑥

maximum normal stress

NA

𝜎𝑎

alternating or amplitude
normal stress

𝜎𝑚

mean or midrange normal
stress

ax(𝜎)
𝜎𝑚𝑎𝑥 − 𝜎𝑚𝑖𝑛
𝜎𝑎 = |
|
2
𝜎𝑚𝑎𝑥 + 𝜎𝑚𝑖𝑛
𝜎𝑚 =
2

transverse shear stress,
ignored because its max is
at neutral axis

𝜏𝑡𝑟𝑎𝑛𝑠 =

torsional shear stresses on
𝜏𝑥𝑦 or 𝜏𝑥𝑧 𝑥 face in 𝑦 / 𝑧 directions;
max at outer surface

𝜏𝑥𝑦 = 𝜏𝑥𝑧 = 𝜏 =

𝜏𝑡𝑟𝑎𝑛𝑠

1

Tab.
A-18

1

Eq.
6-8
Eq.
6-9

4𝑉
𝐴

Tab.
3-2

𝑇𝑟 𝑇 ⋅ 𝑑⁄2
=
𝐽
𝜋𝑑 4 ⁄ 2

Eq.
3-37

𝜏𝑚𝑖𝑛

minimum shear stress

n(𝜏)

NA

𝜏𝑚𝑎𝑥

maximum shear stress

ax(𝜏)

NA

The transverse shear stress caused by the shear force was neglected because it was maximized

on the shaft’s neutral axis and minimized on the shaft’s outer surface; this was flip-flopped from
the bending moment normal stress and torsional shear stress, which were maximized at the shaft’s
outer surface and minimized on the shaft’s neutral axis [57]. Failure usually occurs at a shaft’s
outer surface, so the transverse shear was ignored in this analysis.

182

Table D.6 Continued
Ref. #
in [57]

Symbol

Meaning

Equation / Value

𝜏𝑎

alternating or amplitude
shear stress

𝜏𝑚

mean or midrange shear
stress

𝜏𝑚𝑎𝑥 − 𝜏𝑚𝑖𝑛
𝜏𝑎 = |
|
2
𝜏𝑚𝑎𝑥 + 𝜏𝑚𝑖𝑛
𝜏𝑚 =
2

𝑆𝑢𝑡

ultimate tensile strength

630 MPa for AISI 1045 Steel

Tab.
A-20

𝑆𝑦

yield strength

530 MPa for AISI 1045 Steel

Tab.
A-20

𝑆𝑒′

material endurance limit

See textbook.

Eq.
6-10

𝑆𝑒

fully corrected endurance
limit

𝑆𝑒 = 𝑘𝑎 𝑘𝑏 𝑘𝑐 𝑘𝑑 𝑘𝑒 𝑆𝑒′

Eq.
6-17

𝑘𝑎

surface factor

See textbook.

Eq.
6-18

𝑘𝑏

size factor

See textbook.

Eq.
6-19

𝑘𝑐

load factor

See textbook.

Eq.
6-25

𝑘𝑑

temperature factor

See textbook.

Eq.
6-27

𝑘𝑒

reliability factor

See textbook.

Eq.
6-28

𝐾𝑡 or 𝐾𝑡𝑠

stress concentration
factors

See Table A-15.

Tab.
A-15

Eq.
6-8
Eq.
6-9

𝑞 or 𝑞𝑠

notch sensitivities

See Figure 6-26 (𝑞) and Figure 6-27 (𝑞𝑠 ).

Fig.
6-26,
6-27

𝐾𝑓 or 𝐾𝑓𝑠

fatigue stress
concentration factors

𝐾𝑓 = 1 + 𝑞(𝐾𝑡 − 1)
𝐾𝑓𝑠 = 1 + 𝑞𝑠 (𝐾𝑡𝑠 − 1)

Eq.
6-32

𝜎𝑎′ #1

von Mises alternating
stress, including axial
stress concentration

𝜎𝑎′ = {[𝐾𝑓,𝑎𝑥𝑖𝑎𝑙 ⋅ 𝜎𝑎,𝑎𝑥𝑖𝑎𝑙 + 𝐾𝑓,𝑏𝑒𝑛𝑑 ⋅ 𝜎𝑎,𝑏𝑒𝑛𝑑 ]
1
2 2

+ [𝐾𝑓𝑠,𝑡𝑜𝑟𝑠 ⋅ 𝜏𝑎,𝑡𝑜𝑟𝑠 ] }

183

2

Eq.
6-66

Table D.6 Continued
Symbol

Meaning

𝜎𝑎′ #2

von Mises alternating
stress, neglecting axial
stress concentration

′
𝜎𝑚
#1

von Mises mean stress,
including axial stress
concentration

′
𝜎𝑚
#22

von Mises mean stress,
neglecting axial stress
concentration

′
𝜎𝑚𝑎𝑥

von Mises maximum
stress, neglecting axial
stress concentration

Ref. #
in [57]

Equation / Value
2
𝜎𝑎′ = {[𝐾𝑓,𝑏𝑒𝑛𝑑 ⋅ 𝜎𝑎,𝑡𝑜𝑡 ] +

1
2 2

[𝐾𝑓𝑠,𝑡𝑜𝑟𝑠 ⋅ 𝜏𝑎,𝑡𝑜𝑟𝑠 ] }

′
𝜎𝑚
= {[𝐾𝑓,𝑎𝑥𝑖𝑎𝑙 ⋅ 𝜎𝑚,𝑎𝑥𝑖𝑎𝑙 + 𝐾𝑓,𝑏𝑒𝑛𝑑 ⋅ 𝜎𝑚,𝑏𝑒𝑛𝑑 ]

2

1
2 2

+ [𝐾𝑓𝑠,𝑡𝑜𝑟𝑠 ⋅ 𝜏𝑚,𝑡𝑜𝑟𝑠 ] }
2
′
𝜎𝑚
= {[𝐾𝑓,𝑏𝑒𝑛𝑑 ⋅ 𝜎𝑚,𝑡𝑜𝑡 ] +

1
2 2

[𝐾𝑓𝑠,𝑡𝑜𝑟𝑠 ⋅ 𝜏𝑚,𝑡𝑜𝑟𝑠 ] }

2
′
𝜎𝑚𝑎𝑥
= {𝐾𝑓,𝑏𝑒𝑛𝑑
(𝜎𝑚,𝑡𝑜𝑡 + 𝜎𝑎,𝑡𝑜𝑡 )

Eq.
6-67
Eq.
7-5

2
1
2 2

2
+ 𝐾𝑓𝑠,𝑡𝑜𝑟𝑠
(𝜏𝑚,𝑡𝑜𝑟𝑠 + 𝜏𝑎,𝑡𝑜𝑟𝑠 ) }

fatigue factor of safety
𝑛𝑓 according to the Goodman
Goodman
criterion

Eq.
7-4

−1

′
𝜎𝑎′ 𝜎𝑚
𝑛𝑓 = ( +
)
𝑆𝑒 𝑆𝑢𝑡

Eq.
7-15
Eq.
7-8

𝑛𝑓 Soderberg

fatigue factor of safety
according to the
Soderberg criterion

′
𝜎𝑎′ 𝜎𝑚
𝑛𝑓 = ( + )
𝑆𝑒 𝑆𝑦

Eq.
6-50

𝑛𝑓 –
Gerber

fatigue factor of safety
according to the Gerber
criterion

′ 𝑆 2
1 𝑆𝑢𝑡 2 𝜎𝑎′
2𝜎𝑚
𝑒
√
) )
𝑛𝑓 = ( ′ ) ( ) (−1 + 1 + (
′
2 𝜎𝑚
𝑆𝑒
𝑆𝑢𝑡 𝜎𝑎

Eq.
7-12

𝑛𝑓 ASMEElliptic

fatigue factor of safety
according to the ASMEElliptic criterion

−1

2 −1 2

2

′
𝜎𝑎′
𝜎𝑚
𝑛𝑓 = (( ) + ( ) )
𝑆𝑒
𝑆𝑦

yielding factor of safety
𝑛𝑦 –
according to the Langer
Langer #1
criterion

𝑛𝑦 =

yielding factor of safety
𝑛𝑦 –
according to the Langer
Langer #2
criterion

𝑛𝑦 =

2

Eq.
6-52

𝑆𝑦
′
𝜎𝑎′ + 𝜎𝑚

Eq.
6-43

𝑆𝑦
′
𝜎𝑚𝑎𝑥

Eq.
7-16

In this analysis, the fatigue stress concentration factors for axial and bending normal stresses,
𝐾𝑓,𝑎𝑥𝑖𝑎𝑙 and 𝐾𝑓,𝑏𝑒𝑛𝑑 , were very similar. Thus, the same 𝐾𝑓 was applied to both normal stresses,
′
yielding the somewhat simplified expressions for 𝜎𝑎′ and 𝜎𝑚
.
184

D.3.2 Critical Element Locations
The four critical cross-sections analyzed in the fatigue analysis were located at the coupling
(𝐴), the upstream bearing (𝐵), the downstream bearing (𝐶), and the turbine (𝐷). In each crosssection, twelve critical elements were placed around the circumference of the shaft. Then, the
equations listed in the previous section were applied to each critical element to find which one had
the lowest factor of safety. The figure below shows the twelve critical elements and the orientation
of the increment angle, 𝛾.

Figure D-17: Critical element locations and increment angle.

185

D.3.3 Fatigue Analysis Results
The fatigue analysis results are presented in the tables below. The first five tables show
the “user inputs” to the fatigue analysis; these include the shaft dimensions, the material properties,
the endurance limit modifying factors, the notch dimensions, and the notch stress concentration
factors. The four following tables show the stress analysis results for the four critical crosssections, which were at the coupling (𝐴), the upstream bearing (𝐵), the downstream bearing (𝐶),
and the turbine (𝐷). To conserve space, each table only lists the normal and shear stresses at 30°
rotation increments. (Recall that the shaft rotates in the -𝑥 direction with 𝛼 = 0° aligned with the
+𝑧 axis.) The lowest fatigue factor of safety was found at the downstream bearing’s cross-section
(𝐶); the Soderberg criterion showed 𝑛𝑓 = 1. for critical elements 1, 2, and 12. The lowest
yielding factor of safety was also found at the downstream bearing’s cross-section (𝐶); the Langer
line showed 𝑛𝑦 = 1. for critical elements 1 and 2.
Two conclusions were made from this shaft analysis. (1) Conducting a shaft analysis with
MATLAB and Excel (as opposed to FEA software) was quite difficult and is not recommended
for future endeavors. While it was beneficial to see how the deflection analysis and fatigue
analysis worked together, it was very time-consuming to troubleshoot the equations, adjust the plot
formatting, and refine the table layouts. (2) Because fatigue factors of safety are all higher than
unity, the shaft for the axial bladed turbine will survive the tests. However, it would be beneficial
to check this shaft analysis with FEA software such as SOLIDWORKS or ABAQUS CAE. Unlike
the shaft analysis shown here, FEA software can analyze complex shaft features, including steps,
fillets, and keyways, for various operating conditions, thereby yielding more accurate results at a
much faster pace.

Table D.7: Shaft dimensions.
Symbol
Dshaft
dshaft
rfillet
I=πd4/64
J=πd4/32

Value
0.018
0.012
0.001
1.018E-09
2.036E-09

Units
Meaning
m shaft diameter between bearings; unused in deflection analysis
m
shaft diameter on both ends; set in deflection analysis
m
fillet radius between steps
4
m
Cartesian second area moment
4
m
polar second area moment

186

Table D.8: Material properties.
Symbol
Material
Treatment
Sut
Sy

Value
AISI 1045
CD
630
530

Units Table
[-]
[-]
MPa A-20
MPa A-20

Meaning
selected as initial an estimate
cold drawn
ultimate tensile strength
yield strength

Table D.9: Endurance limit modifying factors (also known as Marin Factors).
Symbol
ka
kb
kc
kd
ke
kf
S'e
Se

Value
0.751
1.990
1.000
1.031
0.702
1.000
315.000
340.709

Equation
(6-18)
(6-19)
(6-25)
(6-27)
(6-28)
(6-10)
(6-17)

Units
[-]
[-]
[-]
[-]
[-]
[-]
MPa
MPa

Meaning & Notes
surface factor; machined (a=3.04 , b=-0.217)
size factor; 7.62mm < d < 51mm
load factor; combined loading
temperature factor; max operating temp = 120°C
reliability factor; 99.99% reliability
additional factor for a user-determined situation
material endurance limit
fully corrected endurance limit

Table D.10: Notch dimensions.
Symbol
D
d
r
D/d
r/d

Value
0.018
0.012
0.001
1.500
0.083

Units
mm
mm
mm
[-]
[-]

Meaning
larger diameter beside the notch
smaller diameter beside the notch
notch radius
ratio for Figure A-15
ratio for Figure A-15

Table D.11: Stress concentration parameters.
Stress Concentration Factor
Symbol
Tension Kt,tension
Bending Kt,bending
Torsion Kts,shear

Value
2.00
1.75
1.52

Fatigue Stress Concentration
Factor
Figure Symbol Value Equation
6-26 Kf,tension 1.75
(6-32)
6-26 Kf,bending 1.56
(6-32)
6-27
Kfs,shear
1.42
(6-32)

Notch Sensitivity

Figure Symbol
A-15-7 qtension
A-15-9 qbending
A-15-8 qs,torsion

187

Value
0.75
0.75
0.80

Table D.12: Fatigue stress analysis for critical section 𝐴 (the coupling).
Stress Analysis for Critical Section A

188

α (°)
(wrt z)
0
30
60
90
120
150
180
210
240
270
300
330
360

My
(N-m)
-8.0
-8.3
-9.2
-10.4
-11.5
-12.4
-12.7
-12.4
-11.5
-10.4
-9.2
-8.3
-8.0

Mz
(N-m)
-26.0
-24.8
-24.0
-23.6
-24.0
-24.8
-26.0
-27.2
-28.0
-28.3
-28.0
-27.2
-26.0

The stress concentration
factors (Kf , Kfs ) were added in
M
σ'a , σ'm
, σ'ma x) and not the quantites
shown in the top eight rows.

The green highlighted cells
contain the lowest nf; the
yelllow highlighted cells contain
the lowest ny.

MR
(N-m)
27.2
26.2
25.7
25.8
26.6
27.7
28.9
29.9
30.3
30.2
29.5
28.4
27.2

Faxial
β (°)
(wrt z)
(N)
-162.8
0.0
-161.4
0.0
-159.0
0.0
-156.3
0.0
-154.3
0.0
-153.4
0.0
-153.9
0.0
-155.5
0.0
-157.6
0.0
-159.9
0.0
-161.8
0.0
-162.9
0.0
-162.8
0.0
Quantity
σmi n , τmi n
σma x , τma x
σ a , τa
σ m , τm
°I
σmi n , τmi n
°I
σma x , τma x
σ'a
σ'm
σ'ma x
nf - Goodman
nf - Soderberg
nf - Gerber
nf - ASME Elliptic
ny - Langer #1
ny - Langer #2

Tinternal
(N-m)
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
Equation
NA
NA
(6-8)
(6-9)
NA
NA
(7-4)
(7-5)
(7-15)
(7-8)
(6-50)
(7-12)
(6-52)
(6-43)
(7-16)

Element 1
γ (°) =
0
σx,tot
τx
(MPa)
(MPa)
-47.3
-58.9
146.3
-58.9
141.2
-58.9
139.4
-58.9
141.2
-58.9
146.3
-58.9
153.2
-58.9
160.1
-58.9
165.2
-58.9
167.0
-58.9
165.2
-58.9
160.1
-58.9
153.2
-58.9

Element 2
γ (°) =
30
σx,tot
τx
(MPa)
(MPa)
35.6
-58.9
102.1
-58.9
95.2
-58.9
90.1
-58.9
88.3
-58.9
90.1
-58.9
95.2
-58.9
102.1
-58.9
109.0
-58.9
114.1
-58.9
115.9
-58.9
114.1
-58.9
109.0
-58.9

Element 3
γ (°) =
60
σx,tot
τx
(MPa)
(MPa)
109.0
-58.9
30.5
-58.9
23.6
-58.9
16.7
-58.9
11.7
-58.9
9.8
-58.9
11.7
-58.9
16.7
-58.9
23.6
-58.9
30.5
-58.9
35.6
-58.9
37.5
-58.9
35.6
-58.9

Element 4
γ (°) =
90
σx,tot
τx
(MPa)
(MPa)
153.2
-58.9
-49.2
-58.9
-54.3
-58.9
-61.2
-58.9
-68.1
-58.9
-73.1
-58.9
-75.0
-58.9
-73.1
-58.9
-68.1
-58.9
-61.2
-58.9
-54.3
-58.9
-49.2
-58.9
-47.3
-58.9

Element 5
γ (°) =
120
σx,tot
τx
(MPa)
(MPa)
156.3
-58.9
-115.7
-58.9
-117.6
-58.9
-122.7
-58.9
-129.6
-58.9
-136.5
-58.9
-141.5
-58.9
-143.4
-58.9
-141.5
-58.9
-136.5
-58.9
-129.6
-58.9
-122.7
-58.9
-117.6
-58.9

Element 6
γ (°) =
150
σx,tot
τx
(MPa)
(MPa)
117.6
-58.9
-151.3
-58.9
-149.4
-58.9
-151.3
-58.9
-156.3
-58.9
-163.3
-58.9
-170.2
-58.9
-175.2
-58.9
-177.1
-58.9
-175.2
-58.9
-170.2
-58.9
-163.3
-58.9
-156.3
-58.9

Element 7
γ (°) =
180
σx,tot
τx
(MPa)
(MPa)
47.3
-58.9
-146.3
-58.9
-141.2
-58.9
-139.4
-58.9
-141.2
-58.9
-146.3
-58.9
-153.2
-58.9
-160.1
-58.9
-165.2
-58.9
-167.0
-58.9
-165.2
-58.9
-160.1
-58.9
-153.2
-58.9

Element 8
γ (°) =
210
σx,tot
τx
(MPa)
(MPa)
-35.6
-58.9
-102.1
-58.9
-95.2
-58.9
-90.1
-58.9
-88.3
-58.9
-90.1
-58.9
-95.2
-58.9
-102.1
-58.9
-109.0
-58.9
-114.1
-58.9
-115.9
-58.9
-114.1
-58.9
-109.0
-58.9

Element 9
γ (°) =
240
σx,tot
τx
(MPa)
(MPa)
-109.0
-58.9
-30.5
-58.9
-23.6
-58.9
-16.7
-58.9
-11.7
-58.9
-9.8
-58.9
-11.7
-58.9
-16.7
-58.9
-23.6
-58.9
-30.5
-58.9
-35.6
-58.9
-37.5
-58.9
-35.6
-58.9

Element 10
γ (°) =
270
σx,tot
τx
(MPa)
(MPa)
-153.2
-58.9
49.2
-58.9
54.3
-58.9
61.2
-58.9
68.1
-58.9
73.1
-58.9
75.0
-58.9
73.1
-58.9
68.1
-58.9
61.2
-58.9
54.3
-58.9
49.2
-58.9
47.3
-58.9

Element 11
γ (°) =
300
σx,tot
τx
(MPa)
(MPa)
-156.3
-58.9
115.7
-58.9
117.6
-58.9
122.7
-58.9
129.6
-58.9
136.5
-58.9
141.5
-58.9
143.4
-58.9
141.5
-58.9
136.5
-58.9
129.6
-58.9
122.7
-58.9
117.6
-58.9

Element 12
γ (°) =
330
σx,tot
τx
(MPa)
(MPa)
-117.6
-58.9
151.3
-58.9
149.4
-58.9
151.3
-58.9
156.3
-58.9
163.3
-58.9
170.2
-58.9
175.2
-58.9
177.1
-58.9
175.2
-58.9
170.2
-58.9
163.3
-58.9
156.3
-58.9

-47.3
-58.9
167.0
-58.9
107.2
0.0
59.8
-58.9
0
0
270
0
107.2
118.3
195.8
2.0
1.9
2.5
2.6
2.4
2.7

35.6
115.9
40.2
75.8
0
300

9.8
109.0
49.6
59.4
150
0

-75.0
-58.9
153.2
-58.9
114.1
0.0
39.1
-58.9
180
0
0
0
114.1
109.3
184.1
2.0
1.8
2.4
2.5
2.4
2.9

-143.4
-58.9
156.3
-58.9
149.9
0.0
6.5
-58.9
210
0
0
0
149.9
102.3
186.7
1.7
1.6
2.0
2.1
2.1
2.8

-177.1
-58.9
117.6
-58.9
147.3
0.0
-29.7
-58.9
240
0
0
0
147.3
106.3
155.7
1.7
1.6
2.0
2.1
2.1
3.4

-167.0
-58.9
47.3
-58.9
107.2
0.0
-59.8
-58.9
270
0
0
0
107.2
118.3
112.5
2.0
1.9
2.5
2.6
2.4
4.7

-115.9
-35.6
40.2
-75.8
300
0

-109.0
-9.8
49.6
-59.4
0
150

-153.2
-58.9
75.0
-58.9
114.1
0.0
-39.1
-58.9
0
0
180
0
114.1
109.3
126.7
2.0
1.8
2.4
2.5
2.4
4.2

-156.3
-58.9
143.4
-58.9
149.9
0.0
-6.5
-58.9
0
0
210
0
149.9
102.3
176.0
1.7
1.6
2.0
2.1
2.1
3.0

-117.6
-58.9
177.1
-58.9
147.3
0.0
29.7
-58.9
0
0
240
0
147.3
106.3
204.4
1.7
1.6
2.0
2.1
2.1
2.6

40.2
127.1
154.5
3.1
2.8
3.7
3.7
3.2
3.4

-58.9
-58.9
0.0
-58.9
0
0

49.6
118.1
149.4
3.0
2.7
3.7
3.8
3.2
3.5

-58.9
-58.9
0.0
-58.9
0
0

40.2
127.1
108.1
3.1
2.8
3.7
3.7
3.2
4.9

-58.9
-58.9
0.0
-58.9
0
0

49.6
118.1
102.6
3.0
2.7
3.7
3.8
3.2
5.2

-58.9
-58.9
0.0
-58.9
0
0

Table D.13: Fatigue stress analysis for critical section 𝐵 (the upstream bearing).
Stress Analysis for Critical Section B

189

α (°)
(wrt z)
0
30
60
90
120
150
180
210
240
270
300
330
360

My
(N-m)
-2.6
-1.9
-0.2
2.1
4.5
6.2
6.8
6.2
4.5
2.1
-0.2
-1.9
-2.6

Mz
(N-m)
5.4
3.1
1.4
0.8
1.4
3.1
5.4
7.8
9.5
10.1
9.5
7.8
5.4

The stress concentration
factors (Kf , Kfs ) were added in
M
σ'a , σ'm
, σ'ma x) and not the quantites
shown in the top eight rows.

The green highlighted cells
contain the lowest nf; the
yelllow highlighted cells contain
the lowest ny.

MR
(N-m)
6.0
3.6
1.4
2.3
4.7
6.9
8.7
10.0
10.5
10.4
9.5
8.0
6.0

Faxial
(N)
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0

β (°)
(wrt z)
-25.1
-31.8
-8.5
70.5
72.8
63.4
51.4
38.5
25.2
11.9
-1.2
-13.9
-25.1
Quantity
σmi n , τmi n
σma x , τma x
σ a , τa
σ m , τm
°I
σmi n , τmi n
°I
σma x , τma x
σ'a
σ'm
σ'ma x
nf - Goodman
nf - Soderberg
nf - Gerber
nf - ASME Elliptic
ny - Langer #1
ny - Langer #2

Tinternal
(N-m)
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
Equation
NA
NA
(6-8)
(6-9)
NA
NA
(7-4)
(7-5)
(7-15)
(7-8)
(6-50)
(7-12)
(6-52)
(6-43)
(7-16)

Element 1
γ (°) =
0
σx,tot
τx
(MPa)
(MPa)
-15.0
-58.9
-18.3
-58.9
-8.2
-58.9
-4.5
-58.9
-8.2
-58.9
-18.3
-58.9
-32.1
-58.9
-45.9
-58.9
-56.0
-58.9
-59.7
-58.9
-56.0
-58.9
-45.9
-58.9
-32.1
-58.9

Element 2
γ (°) =
30
σx,tot
τx
(MPa)
(MPa)
-29.1
-58.9
-21.5
-58.9
-7.7
-58.9
2.4
-58.9
6.1
-58.9
2.4
-58.9
-7.7
-58.9
-21.5
-58.9
-35.3
-58.9
-45.4
-58.9
-49.1
-58.9
-45.4
-58.9
-35.3
-58.9

Element 3
γ (°) =
60
σx,tot
τx
(MPa)
(MPa)
-35.3
-58.9
-19.0
-58.9
-5.1
-58.9
8.7
-58.9
18.8
-58.9
22.5
-58.9
18.8
-58.9
8.7
-58.9
-5.1
-58.9
-19.0
-58.9
-29.1
-58.9
-32.8
-58.9
-29.1
-58.9

Element 4
γ (°) =
90
σx,tot
τx
(MPa)
(MPa)
-32.1
-58.9
-11.3
-58.9
-1.2
-58.9
12.6
-58.9
26.4
-58.9
36.5
-58.9
40.2
-58.9
36.5
-58.9
26.4
-58.9
12.6
-58.9
-1.2
-58.9
-11.3
-58.9
-15.0
-58.9

Element 5
γ (°) =
120
σx,tot
τx
(MPa)
(MPa)
-20.3
-58.9
-0.7
-58.9
3.0
-58.9
13.1
-58.9
27.0
-58.9
40.8
-58.9
50.9
-58.9
54.6
-58.9
50.9
-58.9
40.8
-58.9
27.0
-58.9
13.1
-58.9
3.0
-58.9

Element 6
γ (°) =
150
σx,tot
τx
(MPa)
(MPa)
-3.0
-58.9
10.2
-58.9
6.5
-58.9
10.2
-58.9
20.3
-58.9
34.1
-58.9
47.9
-58.9
58.0
-58.9
61.7
-58.9
58.0
-58.9
47.9
-58.9
34.1
-58.9
20.3
-58.9

Element 7
γ (°) =
180
σx,tot
τx
(MPa)
(MPa)
15.0
-58.9
18.3
-58.9
8.2
-58.9
4.5
-58.9
8.2
-58.9
18.3
-58.9
32.1
-58.9
45.9
-58.9
56.0
-58.9
59.7
-58.9
56.0
-58.9
45.9
-58.9
32.1
-58.9

Element 8
γ (°) =
210
σx,tot
τx
(MPa)
(MPa)
29.1
-58.9
21.5
-58.9
7.7
-58.9
-2.4
-58.9
-6.1
-58.9
-2.4
-58.9
7.7
-58.9
21.5
-58.9
35.3
-58.9
45.4
-58.9
49.1
-58.9
45.4
-58.9
35.3
-58.9

Element 9
γ (°) =
240
σx,tot
τx
(MPa)
(MPa)
35.3
-58.9
19.0
-58.9
5.1
-58.9
-8.7
-58.9
-18.8
-58.9
-22.5
-58.9
-18.8
-58.9
-8.7
-58.9
5.1
-58.9
19.0
-58.9
29.1
-58.9
32.8
-58.9
29.1
-58.9

Element 10
γ (°) =
270
σx,tot
τx
(MPa)
(MPa)
32.1
-58.9
11.3
-58.9
1.2
-58.9
-12.6
-58.9
-26.4
-58.9
-36.5
-58.9
-40.2
-58.9
-36.5
-58.9
-26.4
-58.9
-12.6
-58.9
1.2
-58.9
11.3
-58.9
15.0
-58.9

Element 11
γ (°) =
300
σx,tot
τx
(MPa)
(MPa)
20.3
-58.9
0.7
-58.9
-3.0
-58.9
-13.1
-58.9
-27.0
-58.9
-40.8
-58.9
-50.9
-58.9
-54.6
-58.9
-50.9
-58.9
-40.8
-58.9
-27.0
-58.9
-13.1
-58.9
-3.0
-58.9

Element 12
γ (°) =
330
σx,tot
τx
(MPa)
(MPa)
3.0
-58.9
-10.2
-58.9
-6.5
-58.9
-10.2
-58.9
-20.3
-58.9
-34.1
-58.9
-47.9
-58.9
-58.0
-58.9
-61.7
-58.9
-58.0
-58.9
-47.9
-58.9
-34.1
-58.9
-20.3
-58.9

-59.7
-4.5
27.6
-32.1
270
90

-49.1
6.1
27.6
-21.5
300
120

-35.3
22.5
28.9
-6.4
0
150

-32.1
40.2
36.2
4.1
0
180

-20.3
54.6
37.4
17.2
0
210

-3.0
61.7
32.4
29.4
0
240

4.5
59.7
27.6
32.1
90
270

-6.1
49.1
27.6
21.5
120
300

-22.5
35.3
28.9
6.4
150
0

-40.2
32.1
36.2
-4.1
180
0

-54.6
20.3
37.4
-17.2
210
0

-61.7
3.0
32.4
-29.4
240
0

-58.9
-58.9
0.0
-58.9
0
0
43.2
153.0
144.7
2.7
2.4
3.2
3.2
2.7
3.7

-58.9
-58.9
0.0
-58.9
0
0
43.2
148.4
144.9
2.8
2.5
3.3
3.3
2.8
3.7

-58.9
-58.9
0.0
-58.9
0
0
45.2
144.9
148.8
2.8
2.5
3.3
3.3
2.8
3.6

-58.9
-58.9
0.0
-58.9
0
0
56.5
144.7
157.7
2.5
2.3
3.1
3.1
2.6
3.4

-58.9
-58.9
0.0
-58.9
0
0
58.5
147.0
167.9
2.5
2.2
3.0
3.1
2.6
3.2

-58.9
-58.9
0.0
-58.9
0
0
50.6
151.7
173.8
2.6
2.3
3.1
3.1
2.6
3.0

-58.9
-58.9
0.0
-58.9
0
0
43.2
153.0
172.1
2.7
2.4
3.2
3.2
2.7
3.1

-58.9
-58.9
0.0
-58.9
0
0
43.2
148.4
163.7
2.8
2.5
3.3
3.3
2.8
3.2

-58.9
-58.9
0.0
-58.9
0
0
45.2
144.9
154.7
2.8
2.5
3.3
3.3
2.8
3.4

-58.9
-58.9
0.0
-58.9
0
0
56.5
144.7
153.0
2.5
2.3
3.1
3.1
2.6
3.5

-58.9
-58.9
0.0
-58.9
0
0
58.5
147.0
148.0
2.5
2.2
3.0
3.1
2.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
50.6
151.7
144.6
2.6
2.3
3.1
3.1
2.6
3.7

Table D.14: Fatigue stress analysis for critical section 𝐶 (the downstream bearing).
Stress Analysis for Critical Section C

190

α (°)
(wrt z)
0
30
60
90
120
150
180
210
240
270
300
330
360

My
(N-m)
13.7
11.9
6.9
0.0
-6.9
-11.9
-13.7
-11.9
-6.9
0.0
6.9
11.9
13.7

Mz
(N-m)
-0.3
6.6
11.6
13.4
11.6
6.6
-0.3
-7.1
-12.2
-14.0
-12.2
-7.1
-0.3

The stress concentration
factors (Kf , Kfs ) were added in
M
σ'a , σ'm
, σ'ma x) and not the quantites
shown in the top eight rows.

The green highlighted cells
contain the lowest nf; the
yelllow highlighted cells contain
the lowest ny.

MR
(N-m)
13.7
13.6
13.5
13.4
13.5
13.6
13.7
13.9
14.0
14.0
14.0
13.9
13.7

Faxial
(N)
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0

β (°)
(wrt z)
91.2
61.1
30.6
0.0
-30.6
-61.1
-91.2
-121.1
-150.6
-180.0
150.6
121.1
91.2
Quantity
σmi n , τmi n
σma x , τma x
σ a , τa
σ m , τm
°I
σmi n , τmi n
°I
σma x , τma x
σ'a
σ'm
σ'ma x
nf - Goodman
nf - Soderberg
nf - Gerber
nf - ASME Elliptic
ny - Langer #1
ny - Langer #2

Tinternal
(N-m)
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
Equation
NA
NA
(6-8)
(6-9)
NA
NA
(7-4)
(7-5)
(7-15)
(7-8)
(6-50)
(7-12)
(6-52)
(6-43)
(7-16)

Element 1
γ (°) =
0
σx,tot
τx
(MPa)
(MPa)
91.4
-58.9
-28.1
-58.9
-57.6
-58.9
-68.5
-58.9
-57.6
-58.9
-28.1
-58.9
12.3
-58.9
52.7
-58.9
82.3
-58.9
93.1
-58.9
82.3
-58.9
52.7
-58.9
12.3
-58.9

Element 2
γ (°) =
30
σx,tot
τx
(MPa)
(MPa)
81.5
-58.9
12.1
-58.9
-28.3
-58.9
-57.9
-58.9
-68.7
-58.9
-57.9
-58.9
-28.3
-58.9
12.1
-58.9
52.5
-58.9
82.1
-58.9
92.9
-58.9
82.1
-58.9
52.5
-58.9

Element 3
γ (°) =
60
σx,tot
τx
(MPa)
(MPa)
52.5
-58.9
51.9
-58.9
11.5
-58.9
-28.9
-58.9
-58.5
-58.9
-69.3
-58.9
-58.5
-58.9
-28.9
-58.9
11.5
-58.9
51.9
-58.9
81.5
-58.9
92.3
-58.9
81.5
-58.9

Element 4
γ (°) =
90
σx,tot
τx
(MPa)
(MPa)
12.3
-58.9
80.6
-58.9
51.0
-58.9
10.6
-58.9
-29.8
-58.9
-59.4
-58.9
-70.2
-58.9
-59.4
-58.9
-29.8
-58.9
10.6
-58.9
51.0
-58.9
80.6
-58.9
91.4
-58.9

Element 5
γ (°) =
120
σx,tot
τx
(MPa)
(MPa)
-28.3
-58.9
90.5
-58.9
79.7
-58.9
50.1
-58.9
9.7
-58.9
-30.7
-58.9
-60.2
-58.9
-71.1
-58.9
-60.2
-58.9
-30.7
-58.9
9.7
-58.9
50.1
-58.9
79.7
-58.9

Element 6
γ (°) =
150
σx,tot
τx
(MPa)
(MPa)
-58.5
-58.9
79.1
-58.9
89.9
-58.9
79.1
-58.9
49.5
-58.9
9.1
-58.9
-31.3
-58.9
-60.9
-58.9
-71.7
-58.9
-60.9
-58.9
-31.3
-58.9
9.1
-58.9
49.5
-58.9

Element 7
γ (°) =
180
σx,tot
τx
(MPa)
(MPa)
-70.2
-58.9
49.3
-58.9
78.9
-58.9
89.7
-58.9
78.9
-58.9
49.3
-58.9
8.9
-58.9
-31.5
-58.9
-61.1
-58.9
-71.9
-58.9
-61.1
-58.9
-31.5
-58.9
8.9
-58.9

Element 8
γ (°) =
210
σx,tot
τx
(MPa)
(MPa)
-60.2
-58.9
9.1
-58.9
49.5
-58.9
79.1
-58.9
89.9
-58.9
79.1
-58.9
49.5
-58.9
9.1
-58.9
-31.3
-58.9
-60.9
-58.9
-71.7
-58.9
-60.9
-58.9
-31.3
-58.9

Element 9
γ (°) =
240
σx,tot
τx
(MPa)
(MPa)
-31.3
-58.9
-30.7
-58.9
9.7
-58.9
50.1
-58.9
79.7
-58.9
90.5
-58.9
79.7
-58.9
50.1
-58.9
9.7
-58.9
-30.7
-58.9
-60.2
-58.9
-71.1
-58.9
-60.2
-58.9

Element 10
γ (°) =
270
σx,tot
τx
(MPa)
(MPa)
8.9
-58.9
-59.4
-58.9
-29.8
-58.9
10.6
-58.9
51.0
-58.9
80.6
-58.9
91.4
-58.9
80.6
-58.9
51.0
-58.9
10.6
-58.9
-29.8
-58.9
-59.4
-58.9
-70.2
-58.9

Element 11
γ (°) =
300
σx,tot
τx
(MPa)
(MPa)
49.5
-58.9
-69.3
-58.9
-58.5
-58.9
-28.9
-58.9
11.5
-58.9
51.9
-58.9
81.5
-58.9
92.3
-58.9
81.5
-58.9
51.9
-58.9
11.5
-58.9
-28.9
-58.9
-58.5
-58.9

Element 12
γ (°) =
330
σx,tot
τx
(MPa)
(MPa)
79.7
-58.9
-57.9
-58.9
-68.7
-58.9
-57.9
-58.9
-28.3
-58.9
12.1
-58.9
52.5
-58.9
82.1
-58.9
92.9
-58.9
82.1
-58.9
52.5
-58.9
12.1
-58.9
-28.3
-58.9

-68.5
93.1
80.8
12.3
90
270

-68.7
92.9
80.8
12.1
120
300

-69.3
92.3
80.8
11.5
150
330

-70.2
91.4
80.8
10.6
180
360

-71.1
90.5
80.8
9.7
210
30

-71.7
89.9
80.8
9.1
240
60

-71.9
89.7
80.8
8.9
270
90

-71.7
89.9
80.8
9.1
300
120

-71.1
90.5
80.8
9.7
330
150

-70.2
91.4
80.8
10.6
360
180

-69.3
92.3
80.8
11.5
30
210

-68.7
92.9
80.8
12.1
60
240

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.9
205.1
1.7
1.5
2.1
2.2
1.9
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.8
204.9
1.7
1.5
2.1
2.2
1.9
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.7
204.2
1.7
1.5
2.1
2.2
1.9
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.5
203.2
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.4
202.3
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.3
201.6
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.2
201.3
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.3
201.6
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.4
202.3
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.5
203.2
1.7
1.6
2.1
2.2
2.0
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.7
204.2
1.7
1.5
2.1
2.2
1.9
2.6

-58.9
-58.9
0.0
-58.9
0
0
126.3
145.8
204.9
1.7
1.5
2.1
2.2
1.9
2.6

Table D.15: Fatigue stress analysis for critical section 𝐷 (the turbine).
Stress Analysis for Critical Section D

191

α (°)
(wrt z)
0
30
60
90
120
150
180
210
240
270
300
330
360

My
(N-m)
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0

Mz
(N-m)
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0

The stress concentration
factors (Kf , Kfs ) were added in
M
σ'a , σ'm
, σ'ma x) and not the quantites
shown in the top eight rows.

The green highlighted cells
contain the lowest nf; the
yelllow highlighted cells contain
the lowest ny.

MR
(N-m)
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0

Faxial
(N)
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0
1200.0

β (°)
(wrt z)
18.4
-174.3
-26.6
#DIV/0!
0.0
153.4
-123.7
180.0
-9.5
-90.0
-56.3
123.7
116.6
Quantity
σmi n , τmi n
σma x , τma x
σ a , τa
σ m , τm
°I
σmi n , τmi n
°I
σma x , τma x
σ'a
σ'm
σ'ma x
nf - Goodman
nf - Soderberg
nf - Gerber
nf - ASME Elliptic
ny - Langer #1
ny - Langer #2

Tinternal
(N-m)
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
-20.0
Equation
NA
NA
(6-8)
(6-9)
NA
NA
(7-4)
(7-5)
(7-15)
(7-8)
(6-50)
(7-12)
(6-52)
(6-43)
(7-16)

Element 1
γ (°) =
0
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 2
γ (°) =
30
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 3
γ (°) =
60
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 4
γ (°) =
90
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 5
γ (°) =
120
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 6
γ (°) =
150
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 7
γ (°) =
180
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 8
γ (°) =
210
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 9
γ (°) =
240
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 10
γ (°) =
270
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 11
γ (°) =
300
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

Element 12
γ (°) =
330
σx,tot
τx
(MPa)
(MPa)
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9
10.6
-58.9

10.6
10.6
0.0
10.6
32
31

10.6
10.6
0.0
10.6
170
322

10.6
10.6
0.0
10.6
252
322

10.6
10.6
0.0
10.6
305
62

10.6
10.6
0.0
10.6
305
211

10.6
10.6
0.0
10.6
36
194

10.6
10.6
0.0
10.6
31
32

10.6
10.6
0.0
10.6
322
170

10.6
10.6
0.0
10.6
322
252

10.6
10.6
0.0
10.6
62
305

10.6
10.6
0.0
10.6
211
305

10.6
10.6
0.0
10.6
194
36

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

-58.9
-58.9
0.0
-58.9
0
0
0.0
145.5
145.5
4.3
3.6
4.3
3.6
3.6
3.6

APPENDIX E. SCREW ANALYSIS FOR RADIAL BLADED TURBINE

This screw analysis followed the steps proposed by Shigley’s Mechanical Engineering
Design [57]. The tables shown here reference equations and tables from Chapter 8 of the textbook.
For example, “Table 8-1” refers to a table within the textbook, not a table within this thesis.

E.1

Input Parameters

Figure E-1: Nomenclature and orientation for the components in the screw analysis.

Figure E-2: Loads 1 and 2 considered in the screw analysis.

192

Table E.1: Load conditions.
Parameter
Inlet Pressure
Inlet Pressure
Inlet Diameter
Outlet Diameter
Inlet Area
Outlet Diameter
Load 1
Load 2
Pmin
Pmax

Definition / Source
From CFD
From CFD
From CAD
From CAD
Ain = π/4*(Din)2
Aout = π/4*(Dout)2
Load 1 = Pin * Ain
Load 2 = Pin * Aout
Minimum Tensile Load
Maximum Tensile Load

Value
10
1000000
0.04
0.12
0.00126
0.01131
1257
11310
0
11310

Units
bar
Pa
m
m
m2
m2
N
N
N
N

Load 2 was not a real load on the turbine because it was the product of the inlet pressure and the
outlet area. However, since Load 2 was greater than Load 1, this analysis used Load 2 for a more
conservative estimate. In addition, the tensile load (P) was assumed to fluctuate between Load 2
and a value of 0 N since the only non-zero load would occur during the radial turbine tests.

Table E.2: Properties of the material in the grip.
Symbol
E
t

Definition
material or
property class
modulus of
elasticity
material
thickness

Units
-

Washer
steel matching
screw class

Part 1

Part 2

Part 3

AL 7075 AL 7075 AL 7075

Source
-

GPa

207

71

71

71

Table 8-8

mm

1.5

15.0

45.0

35.0

CAD

Table E.3: Properties of the screw.

mm
GPa
MPa
MPa

Class
8.8
80
207
600
830

Class
9.8
80
207
650
900

Class
10.9
80
207
830
1040

Class
Source
12.9
80
CAD
207
Table 8-8
970 Table 8-11
1220 Table 8-11

MPa

129

140

162

190

Symbol

Definition

Units

L
E
Sp
Sut

length
modulus of elasticity
minimum proof strength
minimum tensile strength
fully corrected endurance
strength for screw with rolled
threads

Se

193

Table 8-17

E.2

Fastener Parameters

Figure E-3: Diagram of fastener parameters.
Table E.4: Fastener parameter definitions from Section 8-4 and Table 8-7
Symbol
d
p
t
t1
t2
t3
h
L

Definition
fastener nominal diameter
fastener pitch
washer thickness
part 1 thickness (unthreaded)
part 2 thickness (unthreaded)
part 3 thickness (threaded)
length of unthreaded material between
screw head and screw hole
screw length, rounded up to nearest integer
if a decimal

LT

screw minimum threaded length; use the
calculation rather than the McMaster value

ℓ

grip length

ℓd
ℓt
Ad
At
E
kb

length of unthreaded portion in grip
length of threaded portion in grip
area of unthreaded portion
area of threaded portion
screw modulus of elasticity
screw stiffness

194

Equation / Source
McMaster
McMaster
McMaster
CAD
CAD
CAD

Units
mm
mm
mm
mm
mm
mm

h = t + t1 + t2

mm

McMaster or
L > h + 1.5*d
LT = 2*d+6 if L < 125
LT = 2*d+12 if L < 200
LT = 2*d+25 if L > 200
ℓ = h + t3/2 if t3 < d
ℓ = h + d/ if t3 > d
ℓd = L - LT
ℓt = ℓ - ℓd
Ad = π/4*(d)2
Table 8-1
Table 8-8
kb = AdAtE / (Adℓt+Atℓd)

mm
mm
mm
mm
mm
mm2
mm2
GPa
MN/m

Table E.5: Fastener parameter calculations.
Nominal
Bolt Size
M6-1
M8-1.25
M10-1.5
M12-1.75
M14-2
M16-2

d
h
L
LT
ℓ
ℓd
ℓt
At
Ad
kb
(mm) (mm) (mm) (mm) (mm) (mm) (mm) (mm2) (mm2) (MN/m)
6
61.5 80.0 18.0 64.5 62.0
2.5
20.1 28.3 89.3
8
61.5 80.0 22.0 65.5 58.0
7.5
36.6 50.3 152.3
10
61.5 80.0 26.0 66.5 54.0 12.5 58.0 78.5 229.2
12
61.5 80.0 30.0 67.5 50.0 17.5 84.3 113.1 318.6
14
61.5 80.0 34.0 68.5 46.0 22.5 115.0 153.9 418.6
16
61.5 80.0 38.0 69.5 42.0 27.5 157.0 201.1 539.0

195

E.3

Frustum Parameters

Figure E-4: Diagram of frustum parameters.

Table E.6: Frustum parameter definitions from Section 8-5.
Frustum Part #
Thickness
Begin D
End D
a
Washer
t
Di = 1.5d
Dii = Di + 2tatan(30°) Note: Di must
b
1
t1
Dii
Diii = Dii + 2tbtan(30°) match Dvi;
c
2
ℓ/ - (t+t1)
Diii
Div = Diii + 2tctan(30°) both must
d
2
t2 - [ℓ/ - (t+t1)]
Div
Dv = Div - 2tdtan(30°) equal 1.5*d.
e
3
ℓ-h
Dv
Dvi = Dv - 2tetan(30°)
Frustum Stiffness: For frustum “a”, there is a begin “D” and an end “D”. The smaller D is
used for Di in the equation below.
𝑘𝑎 =

𝜋𝐸𝑎 𝑑 tan( 0°)
0. 774𝜋𝐸𝑎 𝑑
≈
(2𝑡 tan( 0°) + 𝐷𝑖 − 𝑑)(𝐷𝑖 + 𝑑)
(1.1 𝑡𝑎 + 𝐷𝑖 − 𝑑)(𝐷𝑖 + 𝑑)
ln ( 𝑎
) ln (
)
(2𝑡𝑎 tan( 0°) − 𝐷𝑖 + 𝑑)(𝐷𝑖 − 𝑑)
(1.1 𝑡𝑎 − 𝐷𝑖 + 𝑑)(𝐷𝑖 − 𝑑)

Member Stiffness:
𝑘𝑚 =

1
1
1
1
1
1
+ + +
+
𝑘𝑎 𝑘𝑏 𝑘𝑐 𝑘𝑑 𝑘𝑒

Joint Stiffness Constant:
𝐶=

𝑘𝑏
𝑘𝑏 + 𝑘𝑚

196

Table E.7: Frustum thicknesses.
Nominal
ta
Bolt Size (mm)
M6-1
1.5
M8-1.25
1.5
M10-1.5
1.5
M12-1.75 1.5
M14-2
1.5
M16-2
1.5

tb
(mm)
15
15
15
15
15
15

tc
(mm)
15.75
16.25
16.75
17.25
17.75
18.25

td
(mm)
29.25
28.75
28.25
27.75
27.25
26.75

te
(mm)
3.0
4.0
5.0
6.0
7.0
8.0

ttotal
(mm)
64.5
65.5
66.5
67.5
68.5
69.5

Dv
(mm)
12.5
16.6
20.8
24.9
29.1
33.2

Dvi
(mm)
9.0
12.0
15.0
18.0
21.0
24.0

Table E.8: Frustum “D” values.
Nominal
Di
Bolt Size (mm)
M6-1
9.0
M8-1.25 12.0
M10-1.5 15.0
M12-1.75 18.0
M14-2
21.0
M16-2
24.0

Dii
(mm)
10.7
13.7
16.7
19.7
22.7
25.7

Diii
(mm)
28.1
31.1
34.1
37.1
40.1
43.1

Div
(mm)
46.2
49.8
53.4
57.0
60.5
64.1

Table E.9: Frustum stiffnesses for Class 10.9 screws only.
Nominal
ka
kb
kc
kd
ke
km
Bolt Size (MN/m) (MN/m) (MN/m) (MN/m) (MN/m) (MN/m)
M6-1
6501
933
4454
980
1380
313
M8-1.25 10853 1279
5071
1420
1840
431
M10-1.5 16290 1664
5695
1921
2300
558
M12-1.75 22811 2088
6326
2485
2760
692
M14-2 30417 2551
6964
3116
3220
833
M16-2 39106 3052
7606
3817
3680
982

197

C
0.22
0.26
0.29
0.32
0.33
0.35

E.4

Factors of Safety
Table E.10: Factor of safety parameter definitions.
Symbol
At
Sp
Sut
Se

Definition
area of threaded portion
minimum proof strength
minimum tensile strength
fully corrected endurance strength
for screw with rolled threads

Fi

preload

Fp

proof load

Pmax
Pmin
σi

maximum load per screw
minimum load per screw
preload stress component

σa

alternating stress component

σm

mean stress component

nP
nL
n0

factor of safety guarding against
yielding at the proof strength
factor of safety guarding against
overloading
factor of safety guarding against
joint separation

nf

factor of safety guarding against
fatigue failure

T

torque required to achieve preload

198

Equation / Source
Table 8-1
Table 8-11
Table 8-11

Units
mm2
MPa
MPa

Table 8-17

MPa

Equation 8-31
Fi = 0.75*Fp if removable
Fi = 0.9*Fp if permanent
Equation 8-32
Fp = At*Sp
maximum load / # screws
minimum load / # screws
σi = Fi / At
Equation 8-35
σa = C*(Pmax-Pmin) / (2At)
Equation 8-36
σm = C*(Pmax+Pmin) / (2At) + σi
Equation 8-28
np = Sp*At / (C*P+Fi)
Equation 8-29
nL = (Sp*At-Fi) / (C*P)
Equation 8-30
n0 = Fi / (P*(1-C))
Equation 8-38
nf = Se*(Sut-σi) /
(Sut*σa+Se*(σm-σi))
Equation 8-27
T = K*Fi*d

N
N
N
N
MPa
MPa
MPa
N*m

Table E.11: Factors of safety parameters for Class 10.9 screws only.
Parameter
At (mm2)
Sp (MPa)
Sut (MPa)
Se (MPa)
Fp (N)
Fi (N)
σi (MPa)

M6-1
20.1
830
1040
162
16683
12512
622.5

M8-1.25
36.6
830
1040
162
30378
22784
622.5

Table E.12: Torque required to achieve preload for Class 10.9 screws only.
Coating
Black-Oxide
Zinc
Lubricant
Cadmium

M6-1
22.5
15.0
13.5
12.0

M8-1.25
30.0
20.0
18.0
16.0

Table E.13: Factors of safety for M6-1 Class 10.9 screws only.
# Bolts
2
4
6
8
10
12

Pmax (N)
5655
2827
1885
1414
1131
942

Pmin (N) σa (MPa) σm (MPa)
0
31
654
0
16
638
0
10
633
0
8
630
0
6
629
0
5
628

nP
1.21
1.27
1.29
1.30
1.31
1.31

nL
3.32
6.64
9.96
13.28
16.61
19.93

n0
2.84
5.69
8.53
11.38
14.22
17.07

nf
1.80
3.60
5.40
7.20
9.01
10.81

Table E.14: Factors of safety for M8-1.25 Class 10.9 screws only.
# Bolts
2
4
6
8
10
12

Pmax (N) Pmin (N) σa (MPa) σm (MPa)
5655
0
20.167
643
2827
0
10.084
633
1885
0
6.722
629
1414
0
5.042
628
1131
0
4.033
627
942
0
3.361
626

199

nP
1.25
1.29
1.31
1.31
1.32
1.32

nL
5.14
10.29
15.43
20.58
25.72
30.87

n0
5.45
10.90
16.36
21.81
27.26
32.71

nf
2.79
5.58
8.37
11.16
13.95
16.74

E.5

Results
Table E.15: Torque (N*m) required to achieve preload for M6-1 screws only.
Coating
Black-Oxide
Zinc
Lubricant
Cadmium

Class 8.8
16.3
10.9
9.8
8.7

Class 9.8
17.6
11.8
10.6
9.4

Class 10.9
22.5
15.0
13.5
12.0

Class 12.9
26.3
17.5
15.8
14.0

Table E.16: Torque (N*m) required to achieve preload for M8-1 screws only.
Coating
Black-Oxide
Zinc
Lubricant
Cadmium

Class 8.8
21.7
14.5
13.0
11.6

Class 9.8
23.5
15.7
14.1
12.5

Class 10.9
30.0
20.0
18.0
16.0

Class 12.9
35.1
23.4
21.1
18.7

Table E.17: Factors of Safety (FOS) for M6-1 screws only.
nP – FOS for yielding
nL – FOS for
n0 – FOS for joint
nf – FOS for fatigue
at the proof strength
overloading
separation
failure
# Class Class Class Class Class Class Class Class Class Class Class Class Class Class Class Class
Bolts 8.8 9.8 10.9 12.9 8.8 9.8 10.9 12.9 8.8 9.8 10.9 12.9 8.8 9.8 10.9 12.9
2 1.2 1.2 1.2 1.2 2.4 2.6 3.3 3.9 2.1 2.2 2.8 3.3 1.6 1.8 1.8 2.1
4 1.2 1.3 1.3 1.3 4.8 5.2 6.6 7.8 4.1 4.5 5.7 6.6 3.3 3.6 3.6 4.2
6 1.3 1.3 1.3 1.3 7.2 7.8 10.0 11.6 6.2 6.7 8.5 10.0 4.9 5.3 5.4 6.4
8 1.3 1.3 1.3 1.3 9.6 10.4 13.3 15.5 8.2 8.9 11.4 13.3 6.5 7.1 7.2 8.5

Table E.18: Factors of Safety (FOS) for M8-1.25 screws only.
nP – FOS for yielding
nL – FOS for
n0 – FOS for joint
nf – FOS for fatigue
at the proof strength
overloading
separation
failure
# Class Class Class Class Class Class Class Class Class Class Class Class Class Class Class Class
Bolts 8.8 9.8 10.9 12.9 8.8 9.8 10.9 12.9 8.8 9.8 10.9 12.9 8.8 9.80 10.9 12.9
2 1.2 1.2 1.3 1.3 3.7 4.0 5.1 6.0 3.9 4.3 5.5 6.4 2.5 2.8 2.8 3.3
4 1.3 1.3 1.3 1.3 7.4 8.1 10.3 12.0 7.9 8.5 10.9 12.7 5.1 5.5 5.6 6.6
6 1.3 1.3 1.3 1.3 11.2 12.1 15.4 18.0 11.8 12.8 16.4 19.1 7.6 8.3 8.4 9.9
8 1.3 1.3 1.3 1.3 14.9 16.1 20.6 24.0 15.8 17.1 21.8 25.5 10.1 11.0 11.2 13.2
From the factors of safety listed above, it was concluded that just two M6-1 Class 8.8 screws were
satisfactory. However, four screws were used in the final design to keep everything aligned.

200

APPENDIX F. TURBOCHARGER PERFORMANCE MAPS

This appendix contains several performance maps that are not shown in Section 4.2. The
following list provides a brief description of these performance maps.
•

Figure F-1 (compressor) and Figure F-2 (turbine) show the manufacturer data against the
corrected mass flow rate and total pressure ratio. The dotted black line represents the
operating region boundary, although this may not be the true boundary; it is only the
boundary from the provided data.

•

Figure F-3 (compressor) and Figure F-4 (turbine) show the interpolation grid as a function
of the corrected mass flow rate and total pressure ratio. The grid points outside the
operating region were used for extrapolation in the interpolation scheme, but the contours
through these exterior points were hidden in the final performance maps.

•

Figure F-5 (compressor) and Figure F-6 (turbine) show the efficiency as a function of the
corrected mass flow rate and total pressure ratio. Each operating region is annotated with
iso-lines for efficiency, corrected speed, and total temperature ratio.

•

Figure F-7 (compressor) and Figure F-8 (turbine) show the corrected work as a function of
the corrected mass flow rate and total pressure ratio. Each operating region is annotated
with iso-lines for work, corrected speed, and total temperature ratio. Except for the
corrected speed and total temperature ratio annotations, these corrected work figures are
the same as Figure 4-8 (compressor) and Figure 4-9 (turbine) in Section 4.2.

•

Figure F-9 (compressor) and Figure F-10 (turbine) show the corrected torque as a function
of the corrected mass flow rate and total pressure ratio. Each operating region is annotated
with iso-lines for torque, corrected speed, and total temperature ratio.

201

Figure F-1: Compressor scatter data points.

Figure F-2: Turbine scatter data points.

202

Figure F-3: Interpolation grid for compressor efficiency as a function of corrected quantities.

Figure F-4: Interpolation grid for turbine efficiency as a function of corrected quantities.

203

Figure F-5: Compressor efficiency as a function of corrected quantities.

Figure F-6: Turbine efficiency as a function of corrected quantities.

204

Figure F-7: Corrected compressor power as a function of corrected quantities.

Figure F-8: Corrected turbine power as a function of corrected quantities.

205

Figure F-9: Corrected compressor torque as a function of corrected quantities.

Figure F-10: Corrected turbine torque as a function of corrected quantities.

206

APPENDIX G. LABVIEW PROGRAM FOR RPM SENSOR

This appendix shows four screenshots of the LabVIEW Virtual Instrument (VI) for the
variable-reluctance turbocharger RPM sensor described in Section 4.5.2. The first two images
(Figure G-1 and Figure G-2) show the VI’s front panel, including the three user inputs (Voltage
Threshold, Voltage Sampling Frequency, and RPM Calculation Frequency) and two waveform
charts showing the sampled voltage (top) and the calculated RPM (bottom). These images were
taken during two short tests where the turbocharger was spun by hand; the voltage threshold was
set at 0.03 volts and the voltage sampling frequency was set at 2 kHz. The two tests had RPM
calculation frequencies of 1 Hz and 2 Hz, respectively. Since the RPM signal is visibly different
from one plot to the next, the RPM calculation frequency must be properly calibrated for the
turbocharger’s operating range. The second two images (Figure G-3 and Figure G-4) show the
VI’s block diagram; the first image shows the “true” cases within the simulation loop, and the
second image shows the “false” cases. A pseudo-code for this block diagram is provided below.
A simulation loop operates at the frequency set by the “Voltage Sampling Frequency”.
•

If the voltage is greater than the “Voltage Threshold”, the “true case” is entered.
o If the “Detector” equals zero, the “Rotation Counter” is incremented by one and the
“Detector” is set to equal to one.
o If the “Detector” already equals one, the “Rotating Counter” is not incremented,
and the “Detector” remains equal to one.

•

If the voltage is less than the “Voltage Threshold”, the “false case” is entered.
o The “Detector” is set to zero, and the “Rotation Counter” remains the same.

•

For each simulation loop iteration, the “Differential Time (dt) Counter” is incremented by
one. When the “dt Counter” equals the limit set by Equation (73), then the RPM is
calculated with Equation (74).
dt Count Limit =
RPM =

Voltage Sampling Frequency
RPM Calculation Frequency

60
⋅ Rotation Counter
RPM Calculation Frequency

207

(73)
(74)

Figure G-1: RPM plot for a calculation frequency of 1 Hz.

208

Figure G-2: RPM plot for a calculation frequency of 2 Hz.

209

210
Figure G-3: LabVIEW block diagram for the true cases.

211
Figure G-4: LabVIEW block diagram for the false cases.

REFERENCES

[1] P. Wolański, "Detonative propulsion," Proceedings of the Combustion Institute, vol. 34, no.
1, pp. 125-158, 2013.
[2] F. K. Lu, E. M. Braun, L. Massa and D. R. Wilson, "Rotating Detonation Wave Propulsion:
Experimental Challenges, Modeling, and Engine Concepts," Journal of Propulsion and
Power, vol. 30, no. 5, pp. 1125-1142, 2014.
[3] Z. Rui, W. Dan and W. Jianping, "Progress of continuously rotating detonation engines,"
Chinese Journal of Aeronautics, vol. 29, no. 1, pp. 15-29, 2016.
[4] L. Su, F. Wen, S. Wang and Z. Wang, "Analysis of energy saving and thrust characteristics
of rotating detonation turbine engine," Aerospace and Technology, vol. 124, May 2022.
[5] J. Sousa, G. Paniagua and C.-M. E. Morata, "Thermodynamic analysis of a gas turbine
engine with a rotating detonation combustor," Applied Energy, vol. 195, pp. 247-256, 2017.
[6] S. Zhou, H. Ma, Y. Ma, C. Zhou, D. Liu and L. Shuai, "Experimental study on a rotating
detonation combustor with an axial-flow turbine," Acta Astronautica, vol. 151, pp. 7-14,
2018.
[7] A. Naples, J. Hoke, R. Battelle and F. Schauer, "T63 Turbine Response to Rotating
Detonation Combustor Exhaust Flow," Journal of Engineering for Gas Turbines and Power,
vol. 141, no. 2, 2019.
[8] N. Mushtaq, G. Colella and P. Gaetani, "Design and Parametric Analysis of a Supersonic
Turbine for Rotating Detonation Engine Applications," International Journal of
Turbomachinery Propulsion and Power, vol. 7, no. 1, 2022.
[9] J. Sousa, E. Collado-Morata and G. Paniagua, "Design and optimization of supersonic
turbines for detonation combustors," Chinese Journal of Aeronautics, vol. 35, no. 11, pp. 3344, 2022.
[10] S. R. Turns, An Introduction to Combustion, 3rd ed., New York, New York: McGraw-Hill,
2012, pp. 616-637.

212

[11] P. E. M. Berthelot, P. M. E. Vieille, M. Ernest-François and H. L. Le Chatelier, Weekly
Reports of the Sessions of the Academy of Sciences, vol. 93, pp. 18-22; 145-148, 1881.
[12] D. L. Chapman, "VI. On the Rate of Explosion in Gases," Philosophical Magazine Series 5,
vol. 47, no. 284, pp. 90-104, 1899.
[13] J. C. É. Jouguet, "Sur la propagation des réactions chimiques dans les gaz," Journal de
mathématiques pures et appliquées, vol. 1, pp. 347-425, 1905.
[14] Y. B. Zel'dovich, "To the Question of Energy Use of Detonation Combustion," Journal of
Propulsion and Power, vol. 22, no. 3, pp. 588-592, 2006.
[15] B. A. Rankin, Kaemming, T. A, S. W. Theuerkauf and F. R. Schauer, "Overview of
Performance, Application, and Analysis of Rotating Detonation Engine Technologies,"
Journal of Propulsion and Power, vol. 33, no. 1, January 2017.
[16] K. Kuo, Principles of Combustion, 2 ed., Hoboken, New Jersey: John Wiley & Sons, 2005,
pp. 354-436.
[17] Q. Xie, Z. Ji, H. Wen, Z. Ren, P. Wolanski and B. Wang, "Review on the Rotating Detonation
Engine and Its Typical Problems," Transactions on Aerospace Research, vol. 261, no. 4, pp.
107-163, 2020.
[18] K. Kailasanath, "Review of Propulsion Applications of Detonation Waves," American
Institute of Aeronautics and Astronautics (AIAA) Journal, vol. 38, no. 9, pp. 1698-1708,
2000.
[19] V. Athmanathan, J. Braun, Z. M. Ayers, C. A. Fugger, A. M. Webb, M. N. Slipchenko, G.
Paniagua, S. Roy and T. R. Meyer, "On the effects of reactant stratification and wall
curvature in non-premixed rotating detonation combustors," Combustion and Flame, vol.
240, February 2022.
[20] Z. Liu, J. Braun and G. Paniagua, "Characterization of a Supersonic Turbine Downstream of
a Rotating Detonation Combustor," Journal of Engineering for Gas Turbines and Power,
vol. 141, no. 3, 2019.
[21] H. Rhee, C. Ishiyama, J. Higashi, K. Akira, K. Matsuoka, J. Kasahara, A. Matsuo and I.
Funaki, "Experimental Study on a Rotating Detonation Turbine Engine with an Axial

213

Turbine," in 26th International Colloquium on the Dynamics of Explosions and Reactive
Systems, Boston, 2017.
[22] G. Paniagua, M. Iorio, N. Vinha and J. Sousa, "Design and analysis of pioneering high
supersonic axial turbines," International Journal of Mechanical Sciences, vol. 89, pp. 65-77,
December 2014.
[23] N. Vinha, G. Paniagua, J. Sousa and B. H. Saracoglu, "Axial Bladeless Turbine Suitable for
High Supersonic Flows," Journal of Propulsion and Power, vol. 32, no. 4, July 2016.
[24] N. F. Vinha, G. Paniagua, J. F. Sousa and B. H. Saracoglu, "Axial fluid machine and method
for power extraction". Europe Patent EP2868864A1, 6 May 2015.
[25] J. Braun, G. Paniagua, F. Falempin and B. Le Naour, "Bladeless turbines for unsteady high
speed flows," in 21st AIAA International Space Planes and Hypersonics Technologies
Conference, Xiamen, China, 2017.
[26] J. Braun, G. Paniagua, F. Falempin and B. Le Naour, "Design and Experimental Assessment
of Bladeless Turbines for Axial Inlet Supersonic Flows," Journal of Engineering for Gas
Turbines and Power, vol. 142, no. 4, April 2020.
[27] J. Braun, G. Paniagua and F. Falempin, "Aerothermal Optimization of Bladeless Turbines,"
Journal of Engineering for Gas Turbines and Power, vol. 143, no. 3, March 2021.
[28] J. Braun, F. Falempin and G. Paniagua, "Energy analysis of a detonation combustor with a
bladeless turbine, a propulsion unit for subsonic to supersonic flight," Energy Conversion
and Management, vol. 262, 15 June 2022.
[29] A. P. Weiß, T. Popp, J. Müller, J. Hauer, D. Brüggemann and M. Preißinger, "Experimental
characterization and comparison of an axial and a cantilever micro-turbine for small-scale
Organic Rankine Cycle," Applied Thermal Engineering, vol. 140, pp. 235-244, 2018.
[30] F. Alshammari, A. Karvountzis-Kontakiotis, A. Pesyridis and I. Alatawi, "Design and study
of back-swept high pressure ratio radial turbo-expander in automotive organic Rankine
cycles," Applied Thermal Engineering, vol. 164, 5 January 2020.
[31] A. Uusitalo and M. Zocca, "Design and numerical analysis of supersonic radial-inflow
turbines for transcritical ORC processes," Energy Conversion and Management, vol. 277, 1
February 2023.

214

[32] J. Higashi, C. Ishiyama, S. Nakagami, K. Matsuoka, J. Kasahara, A. Matsuo, I. Funaki and
H. Moriai, "Experimental Study of Disk-Shaped Rotating Detonation Turbine Engines," in
55th AIAA Aerospace Sciences Meeting, Grapevine, Texas, 2017.
[33] R. T. Huff, S. A. Boller, M. D. Polanka, F. R. F. M. L. Schauer and J. L. Hoke, "Radial
Rotating Detonation Engine Driven Bleed Air Turbine," Journal of Propulsion and Power,
vol. 37, no. 2, March 2021.
[34] L. B. Inhestern, J. Braun, J. Paniagua and J. R. S. Cruz, "Design, Optimization, and Analysis
of Supersonic Radial Turbines," Journal of Engineering for Gas Turbines and Power, vol.
142, no. 3, March 2020.
[35] J. D. Mattingly, Elements of Propulsion: Gas Turbines and Rockets, J. A. Schetz, Ed.,
Reston, Virginia: The American Institute of Aeronautics and Astronautics, Inc., 2006, pp.
444-446.
[36] National Aeronautics and Space Administration, "Turbine Design and Application," in NASA
Special Publication SP-290, Washington, D.C., 1975, pp. 368-374.
[37] B. Nikpour, "Measurement of the Performance of a Radial Inflow Turbine," Manchester,
1990.
[38] S. Szymko, N. R. McGlashan, R. Martinez-Botas and K. R. Pullen, "The development of a
dynamometer for torque measurement of automitive turbocharger turbines," Proceedings of
the Institution of Mechanical Engineers, Part D: Journal of Automobile Engineering, vol.
221, no. 2, pp. 225-239, 2007.
[39] A. Banazadeh and H. A. Gol, "Model-Based Fuzzy Control of a Gas Turbine Coupled with
a Dynamometer," Journal of Propulsion and Power, vol. 34, no. 5, September 2018.
[40] F. Schauer, R. Bradley and J. Hoke, "Interaction of a Pulsed Detonation Engine with a
Turbine," in 41st AIAA Aerospace Sciences Meeting & Exhibit, Reno, NV, 2003.
[41] K. P. Rouser, P. I. King, F. R. Schauer, R. Sondergaard, J. L. Hoke and L. P. Goss, "TimeResolved Flow Properties in a Turbine Driven by Pulsed Detonations," Journal of
Propulsion and Power, vol. 30, no. 6, pp. 1528-1536, 2014.

215

[42] S. W. Theuerkauff, F. R. Schauer and R. Anthony, "Comparison of Simulated and Measured
Instantaneous Heat Flux in a Rotating Detonation Engine," in 54th AIAA Aerospace Sciences
Meeting, San Diego, 2016.
[43] A. Roy, C. Bedick, P. Strakey, T. Sidwell and D. Ferguson, "Development of a ThreeDimensional Transient Wall Heat Transfer Model of a Rotating Detonation Combustor," in
54th AIAA Aerospace Sciences Meeting, San Diego, 2016.
[44] J. Braun, J. Sousa and G. Paniagua, "Numerical Assessment of the Convective Heat Transfer
in Rotating Detonation Combustors Using a Reduced-Order Model," Applied Sciences, vol.
8, no. 6, p. 893, May 2018.
[45] K. B. Johnson, D. H. Ferguson and A. C. Nix, "Use of Convolutional Neural Network Image
Classification and High-Speed Ion Probe Data Toward Real-Time Detonation
Characterization in a Water-Cooled Rotating Detonation Engine," in Proceedings of the
ASME Turbo Expo 2022: Turbomachinery Technical Conference and Exposition. Volume
3B: Combustion, Fuels, and Emissions, Rotterdam, 2022.
[46] K. Goto, K. Ota, A. Kawasaki, N. Itouyama, H. Watanabe, K. Matsuoka, J. Kasahara, A.
Matsuo, I. Funaki and H. Kawashima, "Cylindrical Rotating Detonation Engine with
Propellant Injection Cooling," Journal of Propulsion and Power, vol. 38, no. 3, pp. 410-420,
2022.
[47] S. Chakravarthy, O. Peroomian and U. Goldberg, "The CFD++ Computational Fluid
Dynamics Software Suite," SAE Technical Paper Series, vol. 1, September 1998.
[48] R. J. Goldstein, "Film Cooling," Advanced in Heat Transfer, vol. 7, pp. 321-379, 1971.
[49] V. Athmanathan, J. M. Fisher, Z. M. Ayers, D. G. Cuadrado, V. Andreoli, J. Braun, T. R.
Meyer, G. Paniagua, C. A. Fugger and S. Roy, "Development of a turbine-integrated highpressure optical RDE (THOR) for time-resolved fluid dynamic measurements using highspeed optical diagnostics," AIAA Propulsion and Energy, August 2019.
[50] R+W America, "Precision Couplings Guidebook," 2022. [Online]. Available: https://
www.rw-america.com/fileadmin/documents/secured/
R_W_Guidebook_PK_EN_Auflage11_screen.pdf. [Accessed 10 June 2022].

216

[51] A. J. Volponi, "Gas Turbine Parameter Corrections," in The ASME International Gas
Turbine & Aerospace Congress & Exhibition, Stockholm, 1998.
[52] Piusi USA Inc., "Viscomat Vane Electric Pump," [Online]. Available: https://
www.piusi.com/usa/products/viscomat-vane. [Accessed 4 April 2022].
[53] M. Anwer, R. M. C. So and Y. G. Lai, "Perturbation by and recovery from bend curvature
of a fully developed turbulent pipe flow," Physics of Fluids A: Fluid Dynamics, vol. 1, no.
8, August 1989.
[54] Valworx,

"2-1/2"

Electric

Actuated

Butterfly

Valve,"

[Online].

Available:

https://www.valworx.com/product/electric-actuated-butterfly-valve-2-12-lug-epdm-120vac-eps-positioner. [Accessed 2 February 2023].
[55] TE Connectivity, "Variable Reluctance Speed Sensors," [Online]. Available: https://
www.te.com/usa-en/product-CAT-SPS0005.html. [Accessed 24 April 2022].
[56] C. Krousgrill, K. Zhao and A. Raman, Mechanics of Materials: A Lecturebook, XanEdu
Publishing Inc, 2019.
[57] R. G. Budynas and J. K. Nisbett, Shigley's Mechanical Engineering Design, 11th ed., New
York, New York: McGraw-Hill Education, 2020.

217



## Metadata
- Source file: junk_drawer/Ford Lynch Master's Thesis.pdf
- Extracted: 2026-05-18
- Category: academic-paper
