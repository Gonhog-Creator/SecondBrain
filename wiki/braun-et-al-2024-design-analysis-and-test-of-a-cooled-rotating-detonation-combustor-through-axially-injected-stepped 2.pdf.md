# braun-et-al-2024-design-analysis-and-test-of-a-cooled-rotating-detonation-combustor-through-axially-injected-stepped (2).pdf

Source: junk_drawer/braun-et-al-2024-design-analysis-and-test-of-a-cooled-rotating-detonation-combustor-through-axially-injected-stepped (2).pdf

Category: [[academic-homework]]

## Summary
AIAA SciTech Forum 8-12 January 2024, Orlando, FL AIAA SCITECH 2024 Forum 10.2514/6.2024-0815 Design, Analysis, and Test of a Cooled Rotating Detonation Combustor through axially injected stepped cooling slots

## Full Content
AIAA SciTech Forum
8-12 January 2024, Orlando, FL
AIAA SCITECH 2024 Forum

10.2514/6.2024-0815

Design, Analysis, and Test of a Cooled Rotating
Detonation Combustor through axially injected stepped
cooling slots

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

James Braun1, Ford Lynch2, William Andress3, Avidh Bavkar4, Venkat Athmanathan5, Guillermo Paniagua6
Purdue University, West-Lafayette, Indiana, 47907, USA

The present paper investigates the flow physics of a cooled rotating detonation combustor.
First, an analytical model is developed for the slotted cooling designs, followed by a section on
3D RANS and URANS simulations to verify the analytical findings. Second, a cooling jacket
is designed and machined to be integrated within an existing rotating detonation combustor.
The jacket contains several measurements ports to measure temperature and pressure.
Stators are added to measure stagnation pressure and achieve straight outflow. Finally, an
experimental campaign is carried out on an existing RDE test platform with the axially
injected stepped cooling slots. High speed imaging, as well as pressure and temperature probes
are used to quantify the amount of coolant and the effectiveness of the cooling scheme.

1. Introduction
Uncooled Rotating Detonation Combustors (RDCs) have been numerically analyzed and tested at universities,
national labs, and industry all around the world. Most of these efforts have focused on detonation wave dynamics and
uncooled RDC performance. There is still a dearth of research on the cooling of such combustors. Heat flux levels
within RDCs were experimentally investigated by Theuerkauf et al. [1] Similarly, Roy et al. [2] performed conjugate
heat transfer analyses by using periodic boundary conditions from Rotating Detonation Combustor simulations. Braun
et al. [3] investigated the convective heat flux within RDCs and found that the average convective heat flux levels are
nearly the same between the detonation front and downstream of the triple point. At the National Energy Technology
Laboratory [4], a water-cooled RDC has been tested recently. At Nagoya University, hollow combustors are cooled
through small holes on the outer wall [5]. The objective of the present research is to numerically analyze, and
experimentally validate the performance of an RDC with hydrogen-air combustion, stepped axial injection cooling
slots, and nitrogen gas film cooling.

1

Research Assistant Professor, School of Mechanical Engineering, AIAA Member.

2

Graduate student, AIAA student

3

Graduate student, AIAA student

4

Undergraduate student, AIAA student

5

Research Scientist, School of Mechanical Engineering, AIAA member
Professor, School of Mechanical Engineering, AIAA Fellow

6

1
Copyright © 2024 by James Braun , Ford Lynch , William Andress , Avidh Bavkar , Venkat Athmanathan , Guillermo Paniagua.
Published by the American Institute of Aeronautics and Astronautics, Inc., with permission.

2. Numerical Analysis of the Cooled Combustor
2.1.

Heat Flux Estimation

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

To estimate the cooling required for the combustor, a simulation of an uncooled rotating detonation combustor
was used. The simulations were performed with CFD++ of Metacomp [6] on a structured mesh with about 45 million
cells, which was used and validated in previous work[7,10]. The combustor is a non-premixed combustor running on
a hydrogen-air mixture [7]. The viscous sublayer was resolved to ensure capturing of the viscous sublayer. The wall
temperature was set to 600K. Figure 1[7]. The viscous sublayer was resolved to ensure capturing of the viscous
sublayer. The wall temperature was set to 600K. Figure 1a and b depict the instantaneous heat flux on the wall in
which the highest heat fluxes are noted downstream of the detonation wave. Figure 1c depicts the average heat flux
along the axial direction, with average heat loads up to 3 MW/m 2.

Figure 1: Heat flux from the uncooled THOR combustor at 1.2 kg/s: (a) instantaneous snapshot on the inner end
wall, (b) instantaneous snapshot on the outer end wall, (c) average heat flux along the axial direction.

2

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

2.2.

Preliminary Design Choices for the Cooling Jacket

Due to the high levels of wall heat flux, as noted above, rotating detonation combustors require a cooling scheme
to allow continuous operation. One possible solution is the use of gaseous film cooling to protect the walls of the
combustion chamber. While this cooling scheme is pervasive in the deflagration combustors of turbomachine engines,
additional challenges are faced when designing a cooling setup for a rotating detonation combustor. The fluctuating
pressure levels in the combustion chamber mean that coolant flow rates will fluctuate as well. As the moving
detonation wave passes an injection point, the increase in pressure could even lead to momentary ingestion of hot air
into the coolant reservoir. To mitigate the effects of the variable combustion chamber pressure, coolant pressure could
be increased to choke the cooling passages. Choking the passages would make the coolant flow rate insensitive to the
changing pressures in the combustion chamber. However, increasing the coolant pressure also leads to increased
coolant blowing ratio , which poses additional challenges in the design of the film cooling setup. In his summary of
advancements in film cooling, Goldstein [8] reviewed the results of many previous researchers. These studies showed
that for different film cooling layouts, high blowing ratios can have either a positive or negative effect on cooling
effectiveness. For those layouts with coolant injection perpendicular to the mainstream, coolant jets with high blowing
ratios will blow off the surface and thus not form the desired film of cool air. For layouts with injection parallel to the
mainstream flow direction, higher blowing ratios lead to increased film cooling effectiveness.
In addition to the choice of injection angle, designers also have a choice between injection through either discrete
holes or continuous slots. As shown in Goldstein’s review, injection through discrete holes can lead to hot spots
between requiring additional coolant mass flow to prevent exceeding of wall temperature limits. Continuous slots
avoid this behavior.
For the aforementioned reasons, the preliminary cooling design focused on injection tangential to the surface
using continuous slots. Goldstein describes a variety of models for film cooling effectiveness with this setup [8]. For
slot tangential injection, the primary two are

1

𝜂=

1 + [0.329
𝜂=

𝑐𝑝∞ 0.8
𝜉 ]
𝑐𝑝2

(1)

1
𝑐𝑝∞
[0.329(4.01 + 𝜉)0.8 − 1]
1+
𝑐𝑝2

(2)

−0.25
𝑥 𝜇2
[ 𝑅ⅇ2 ]
𝑀𝑠 𝜇∞

(3)

Where,
𝜉=

Between these two equations, equation (1) assumes that the boundary layer starts at the point of injection while
the equation (2) assumes that the boundary layer has started upstream of the point of injection. Equation (1) gives
higher adiabatic wall temperature estimates, so it was selected for the analysis. Wall thickness was assumed to be 1.5
mm. The limit on wall thickness was to aid in manufacture and to make the wall more able to withstand the high
pressures of the passing wave. From Goldstein, having a thick wall compared to the slot height reduces the cooling
effectiveness, so the slot height was set at 1.5 mm to limit the detriment in performance. From the plots in Goldstein’s
work, this will still come with around a 15% reduction in cooling effectiveness, increasing slot height further would
increase slot area further and require higher cooling mass flows.
Maximum coolant pressure was assumed to be four bar while the minimum pressure was determined from the
pressure ratio required to keep the slot choked at the average combustor pressure. Figure 2 shows the results of a 1-D
analysis varying coolant pressure and number of slots. Figure 2a shows that increasing the number of slots and coolant
pressure increases mass flow while decreasing maximum adiabatic wall temperature. There are diminishing returns

3

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

with respect to both pressure and slot count. Figure 2b shows a trace of the expected adiabatic wall temperature for a
1 and 3 slot design with a coolant pressure of 3 bar.

Figure 2: a) Impact of variable coolant pressure on mass flow and maximum wall temperature, b) wall
temperature profiles for 1 and 3 slot designs at a pressure of 3 bar.

This analysis is an upper estimate of wall temperature. The less optimistic correlation for film cooling
effectiveness was used. It only considers the cooling effectiveness from the most recent slot and ignores that upstream
coolant flows are either mixed into the mainstream or stay in a coolant layer past the next slot. In addition, it ignores
that the flow of coolant would be cooling the other side of the wall as well. For these reasons, and considering a
maximum wall temperature of 1000 K, a three-slot design was chosen for further analysis.

2.3.

URANS Calculations

As described in 2.2, a cooling mechanism with a three continuous concentric slots in a stepped combustor wall
was selected for this RDC.. A 2D representation of the fluid domain is given in Figure 2a. The computational mesh
was made of a structured mesh in ICEM. The total mesh size was around 50 million cells (Figure 2b), in which care
was taken to resolve the viscous sublayer in the main combustion chamber. To simplify the geometry, a premixed
simulation was performed, in which hydrogen-air was imposed at the inlet of the domain. The first two slots require
higher feed pressures than the third slot which lies in the transonic/supersonic exhaust of the combustor. Additionally,
downstream of the slots, a diverging section allows the combustor to fully expand to supersonic conditions.

4

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 2: a) Cross-section of the numerical domain with three injection slots, b) structured mesh of the combustor.

After reaching steady state, Figure 3 shows a snapshot of unsteady interaction of the jets with the main detonation
wave. At T=1/8Tdetonation, the cooling slots do not have enough pressure to push cooling into the combustion chamber,
but at T= 1/4Tdetonation, cooling starts to flow into the main combustion chamber all the way till T=7/8T detonation.

=1

=3 4

=1 4

=

Figure 3: Four unsteady snapshots of temperature of the cooled combustor
Figure 4 shows the heat flux reduction thanks to the cooling scheme; a four-fold reduction was achieved with
coolant injection on the shroud (upper end wall), whereas the inner end wall (hub) is unaltered because no cooling
jacket was present.

5

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 4: Heat flux along the axial direction: Comparison between cooled and uncooled combustor

The cooling mass flow constituted around 30% of the core mass flow. Additionally, the exhaust profile can be
altered as shown in Figure 5; the uncooled combustor provides an exit temperature of 2000 K whereas the cooling
jacket lowers the exit temperatures to around 1500 K on average while keeping a transonic-supersonic exhaust.

Figure 5: Mass flow averaged exhaust profile of temperature (top) and Mach number (bottom).

6

3. Design of the Combustor

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

3.1.

Design of the Combustor

The implementation of the cooling jacket in THOR’s rotating detonation combustor is shown in Figure 6 below.
In previous work, the university developed a modular RDC for optical diagnostics, so pieces of this RDC are reused
for the cooled design[9]. The repurposed components include the combustion reactant air injection ring and the center
body, which are shown in a slate gray color. The cooling jacket, shown in green, consists of the three previously
described cooling slots as well as eight injection holes and 24 instrumentation ports. The eight injection holes are
placed normal to the cooling jacket exterior, and two inner plenums redirect the cooling gas into the tangential cooling
slots. The first plenum feeds the first two slots while the second plenum feeds the third slot. Each plenum is divided
into four chambers around the cooling jacket circumference; each chamber occupies a 90° sector. Each plenum has
four injection ports (one port per chamber). The two separate plenums allow for different injection parameters, such
as gas composition, pressure, and/or temperature; this means that some experimental optimization may be conducted.
Since the cooling sleeve has a complex geometry that would be difficult to machine, the cooling sleeve was designed
to be 3D printed. Other design considerations specific to 3D printing are discussed in 4.1.
As discussed in 2.3, the CFD simulations predict that the RDC exit will have a rapidly fluctuating Mach number.
However, the Mach number remains above unity, meaning that a diverging exit area will expand the flow, thereby
increasing velocity and decreasing pressure. This diverging section is featured in the combustor flange, shown in pink
in Figure 6. For this divergence, an angle of 12.5° to the horizontal was arbitrarily selected. The availability of
mounting a turbine downstream of the detonation chamber, inside the diverging section of the flange was considered.
The turbine design is not discussed in this paper, but the turbine was optimized for a low supersonic fluctuating flow.
A unique miniature stator (Figure 7) was designed to straighten the combustor exit flow before it enters the turbine,
to improve power extraction. The stator features a NACA 0030 blade profile, which indicates the max camber is 0%
of the chord and the thickness is 30% of the chord. Even though the stator does not have distinct pressure and suction
sides, the pressure and suction side nomenclature from the turbine are copied to the stator. Each stator blade is bolted
to the combustor flange and has hub and tip profiles that match the center body and the divergence angle, respectively.

Figure 6: CAD of the cooled combustor.

7

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 7: CAD of one stator blade.

3.2.

Measurement Capabilities

As discussed in 2.2, it may be beneficial to choke the cooling slots since this would prevent backflow of the
combustion products into the cooling chambers. To determine if the slots choke during the tests, pressure and
temperature must be measured inside the cooling slots. To that end, the cooling jacket was designed with 24 threaded
ports for instrumentation: sixteen for the first plenum and eight for the second plenum. These ports may be configured
for pressure probes or thermocouples. Since the first plenum is shared by the first two cooling slots, care was taken to
ensure that the pressures in the plenum and each slot may be measured separately. Ideally, the total pressure in the
first plenum will match that of the first two slots, but the complex geometry may create pressure disturbances.
Thermocouples may be placed in the plenums in a similar manner to the pressure probes, and surface thermocouples
may also be utilized to determine the slot wall temperature.
In the diverging section of the flange, six static pressure taps are placed along the flow direction; these taps are
spaced equally across the chord of the turbine blades. A small window overlooks the turbine blade flow path and may
be used for optical access to the turbine. Although there are no probes inside the combustion chamber, the combustor
exit is instrumented by implementing the stator blades. Each stator blade is mounted with two screws, and each screw
hole is connected to 1/32” hole that serves as a pressure tap to the stator blade surface. These surface pressure taps are
visible in Figure 7 and are labeled Probe Holes 1 and 2. Hollow screws (or vent screws) are used to connect the surface
hole to an external pressure probe. Since there are eight flow straighteners, eight combinations of probe hole
orientations were created. These combinations are listed in Table 1. As stated previously, the stators do not necessarily
have pressure or suction sides since the stators have a 0° of incidence. However, for simplicity, the table below labels
the stator sides with respect to the turbine pressure and suction sides.

8

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Table 1: Flow straightener configurations.

Stator
Number
1

Blade Side
w.r.t. Turbine
N/A

Probe Hole 1
Chord
Position (%)
0

Span
Position (%)
50

Side of Blade
w.r.t. Turbine
N/A

Probe Hole 2
Chord
Position (%)
0

Span
Position (%)
40

2

N/A

0

75

N/A

0

25

3

N/A

100

40

N/A

100

50

4

Suction Side

20

50

Pressure Side

20

50

5

Suction Side

40

50

Pressure Side

40

50

6

Suction Side

40

30

Suction Side

40

70

7

Suction Side

60

50

Pressure Side

60

50

8

Suction Side

80

50

Pressure Side

80

50

4. Experimental Assessment
4.1.

Manufacturing of the Cooled Combustor

Finally, the cooling sleeve was designed to be made on a direct metal laser sinter 3D printer by Innovative 3D
Manufacturing in Franklin, IN. The material was selected to be SAE 316L stainless steel since this offered fair
corrosion resistance at high temperatures while also not being too expensive. Figure 8 shows the axial stepped cooling
jacket, which was printed in the orientation shown in Figure 8b. One notable feature is the conical extension on each
injection and instrumentation port. The cone angle was set to 45° such that no support material would need to be
printed, thus reducing time on the printer and cost. Another feature (not shown) is that the wall separating Slots 1 and
2 has teardrop-shaped holes to allow cooling gas to pass from the first plenum into Slot 1. These teardrops terminate
before injection into the detonation chamber. The angle of the teardrop was set to 45° to avoid support material, just
like with the conical extensions. The teardrops did not necessarily save time on the printer, but there was no easy
access to the plenum interior, hence the need for supportless printing. In addition to the cooling sleeve, a flange was
designed to hold the cooling jacket to the base of the THOR rig. This sleeve was machined from carbon steel by Logo
2 Manufacturing in Alicante, Spain; carbon steel was chosen over other materials for its low cost and ease of
machining. Figure 10a and b shows the flange at an intermediate stage and the final product, respectively; Figure 10c
shows the optical access window insert (made from aluminum alloy 7075); and Figure 10d and e show the assembled
combustor and exhaust flange.

9

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 8: Manufacturing of the cooling jacket.

Figure 9: Manufacturing of the uncooled flange and window insert.

10

4.2.

Test Data Analysis

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Thermocouples were affixed to the rear-side of all three film-cooling slots to determine surface temperature of
each cooling slot. Additionally, pressure taps were integrated into the film-cooling apparatus such that static pressures
are also available for each slot. See the cutaway in Figure 10.

Figure 10 a) CAD cross section for instrumentation, b) layout in the THOR test stand, c) downstream imaging
before and after the test

For all tests, a Phantom high-speed camera operating at 100 kHz was used in conjunction with a mirror to visualize
the detonation waves from the aft of the combustor, looking forward. Due to the combustor exhaust during firing, the
resulting high-speed footage exhibits noticeable distortion. Nevertheless, detonation waves were still visible and are
shown in Figure 8. A still image taken before the test starts is shown on the left, and then the following sequence
depicts a single detonation wave propagation in a clockwise direction. For clarity, the detonation wave is highlighted
by the circle in the lower sequence.

11

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 11 high speed imaging with single wave detection
The full test matrix for this campaign is shown in Table 2: Test matrix.Table 2. Despite 33 tests having been run,
only 23 of the tests had successful ignition. The remaining were either cold-flows or failed-ignitions due to pre-det
issues. For this data analysis, only the ignited tests have been considered. Test #32 is an uncooled control case.
Table 2: Test matrix.
Test
#

Duration
(sec)

1
2
3
4
5
6
7
8
9
10
11
12
13
14
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33

0.3
0.3
0.3
0.3
0.3
1
1
1.5
2
2
2.5
2.5
1
2
2
2
2
2
2
2
2
2
2.5
2.5
2.5
2.5
3
3
3
3
0.5
5

Type

Air + H2
Air
H2
Chamber 1 N2
Chamber 2 N2
Mass Flow Pressure Pressure Mass Flow Pressure Mass Flow Pressure
(lbm/s)
(psi)
(psi)
(lbm/s)
(psi)
(lbm/s)
(psi)
Cold
1
334
N/A
0.1
365
0
0
Cold
1
334
N/A
0
0
0.09
370
Cold
1
334
N/A
0.38
365
0.22
370
Cold
1
334
N/A
0.29
365
0.19
370
Ignition
1
334
525
0.1
365
0.09
370
No ignition
1
334
525
0.1
365
0.09
370
Ignition
1
334
525
0.1
365
0.07
370
No ignition
1
334
525
0.1
365
0.1
370
Partial ignition
1
334
525
0.1
365
0.1
370
Ignition
1.39
473
691
0.1
365
0.1
370
No ignition
1
333
527
0.1
365
0.1
370
No ignition
1
333
527
0.1
365
0.1
370
Ignition
1
341
499
0.1
365
0.1
380
Ignition
1
343
546
0.1
365
0.1
380
Ignition
1
340
540
0.1
364
0.1
369
Ignition
1
340
540
0.2
780
0.2
770
Ignition
1
340
540
0.2
730
0.2
745
Ignition
1
343
537
0.2
730
0.2
740
Ignition
1
342
532
0.3
1128
0.2
745
Ignition
1
341
642
0.3
1150
0.2
742
Ignition
1
343
643
0.3
1108
0.2
742
Ignition
1.5
490
756
0.3
1108
0.2
744
Ignition
1.5
490
823
0.3
1108
0.2
744
No ignition
1.5
506
805
0.3
1106
0.2
743
Ignition
1.5
504
806
0.3
1106
0.2
743
Ignition
2
655
1068
0.3
1110
0.2
739
Ignition
2
668
1070
0.3
1099
0.2
747
Ignition
2
666
1070
0.2
730
0.2
742
Ignition
2
671
1066
0.3
1096
0.3
1137
Ignition
2
669
1063
0.4
1458
0.3
1107
Ignition
1
344
539
0
0
0
0
Ignition
1
340
548
0.3
1106
0.2
738

12

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

As an initial demonstration of the cooling-slot effectiveness, the temperature profile of the uncooled control case
(Test #32) is plotted alongside that of Test #33, the longest duration cooled test; these temperature profiles are depicted
in Figure 12. The vertical dashed lines denote the start and end times of each test. As can be seen, the uncooled test
experiences a rapid increase in slot temperature over the short test duration, whereas the cooled test experiences no
significant increase in slot temperature, enabling a much longer test duration.

Figure 12: Temperature vs. time for an uncooled (top) and a cooled test (bottom).

The start and end times used here are derived from thrust measurements by virtue of a load-cell integrated into
the RDC frame. Due to installation, an absolute value of the RDC thrust was not measured, however the load-cell data
provides a relative comparison that enables the determination of the test window, as shown in Figure 13. A rollingaverage is applied to smooth the noisy thrust data, and a threshold value is set halfway between the initial sensor value
and the maximum recorded value. The test duration is then simply found by counting the time spent above the
threshold.

Figure 13: Start-stop signal for the test based on load cell information.

13

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

This simple method was found to be robust enough to determine test start and end points for all ignited tests.
Figure 14: Test duration for each test shows the measured test-time from this method, which can be compared to the
target times in the test matrix shown in Table 2.

Figure 14: Test duration for each test.

To determine the impact of the coolant mass-flow on the cooling performance, the blowing ratio (BR) is defined
as follows:

𝐵𝑅 =

𝑚̇𝑐𝑜𝑜𝑙𝑎𝑛𝑡
𝑚̇𝑁2
=
𝑚̇𝑓𝑢𝑒𝑙+𝑜𝑥𝑖𝑑𝑖𝑧𝑒𝑟 𝑚̇𝑎𝑖𝑟 + 𝑚̇𝐻2

(4)

A higher value of BR indicates more cooling; for instance, a value of 1 indicates that the cooling mass flow rate
is equal to propellant mass flow rate, whereas a value of 0 indicates an uncooled test. For these experiments, the
blowing ratio never exceeded 0.5 to avoid ignition/detonation difficulty due to excessive nitrogen dilution.
The slot temperature increase can be shown by the average rate of slot temperature change, expressed as the
following ratio:

(𝑇𝑓𝑖𝑛𝑎𝑙 − 𝑇𝑖𝑛𝑖𝑡𝑖𝑎𝑙 )
𝑡𝑡𝑒𝑠𝑡

(5)

where 𝑇𝑓𝑖𝑛𝑎𝑙 and 𝑇𝑖𝑛𝑖𝑡𝑖𝑎𝑙 are the temperatures recorded at the end and at the start of the test respectively, and 𝑡𝑡𝑒𝑠𝑡 is
the test duration. The decision to use this rate instead of a direct temperature delta (𝑇𝑓𝑖𝑛𝑎𝑙 − 𝑇𝑖𝑛𝑖𝑡𝑎𝑙 ) or ratio
(𝑇𝑓𝑖𝑛𝑎𝑙 𝑇𝑖𝑛𝑖𝑡𝑎𝑙 ) was made to remove the dependence on test duration.
By plotting this rate against the previously defined blowing ratio, a correlation between coolant mass flow rate
and slot temperature increase rate can be observed (Figure 15), colored by the total mass flow rate (coolant and

14

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

propellant). During the testing, high-speed camera footage revealed that in many tests, a single detonation wave was
not observed. Rather, two or more counter-rotating waves were seen in a “slapping mode”. To indicate these nonsingular modes, the unfilled markers in Figure 15 correspond to multi-wave solutions, whereas the single-wave
solutions are shown as filled-in markers.

Figure 15: Average rate of slot temperature change.

As can be seen, the uncooled test has the highest slot temperature change, but as cooling increases, the slot
temperature change is less pronounced. For a clearer view, the slapping-mode tests have been omitted in Figure 16.
Uncertainty bands are based on a thermocouple uncertainty of +/- 3 Kelvin, however conduction and velocity errors
are unaccounted for in this analysis. Above blowing ratios of 0.2, the rate of change in the slot temperature was below
10 K/second. Slot 2 featured the highest rate of change, possibly due to the highest strength of the detonation wave at
that location.

Figure 16: Average rate of slot temperature change for single-wave-mode tests.

Slot pressures were also plotted for comparison between the cooled and uncooled tests. The feed slots observed
a higher-pressure during combustion because the slots experienced back flow from the RDE as the detonation wave
passed each slot. This is visible in Figure 17 (bottom), for which the pressure increases during the combustion wave.

15

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

Figure 17: Pressure trace as a function of time for an uncooled test (top) and cooled test (bottom).

The slot pressure ratios (final vs. intial) are plotted against the blowing ratio in Figure 18. Once again, single
wave solutions are denoted with solid markers, and hollow markers indicate multi-wave solutions. These results are
also colored by the slot temperature change. In average slot 2 experiences the highest blockage from the wave, and
single wave detonation events influence the cooling plenums more. The third cooling slot was less affect by the
detonation wave as the wave strength was already decreased. For a blowing ratio near 0.3, slot 2 featured highest
pressure increase during the hot fire.

Figure 18: Slot static pressure versus blow ratio.

16

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

5. Conclusions
A new cooling scheme for rotating detonation combustors was successfully demonstrated in this paper. The
stepped cooling scheme was first analyzed starting from Goldstein’s work and numerically assessed through CFD on
a rotating detonation combustor. This rotating detonation combustor was already tested in an uncooled configuration,
and a cooling jacket was designed with CAD and created by 3D printing. Finally, an experimental campaign was
carried out on an existing RDE test platform with the axial injection stepped cooling slots. High speed imaging and
pressure and temperature probes were used to quantify the amount of cooling that was added and the effectiveness of
the cooling scheme. The temperature readings recorded successful cooling of the hardware throughout the test matrix
at low ang high blowing ratios. The experiments revealed a wide range of operating conditions for which a single
mode was detected, but for various conditions of the cooling slot, other modes were also detected such as the slapping
mode operation. Above blowing ratios of 0.2, the rate of change in the three slots was minimal. The effect of the wave
on the pressure within the cooling jacket was also assessed, and pressure blockage of up to 60% was found in the
middle slot (which also featured highest temperature changes), whereas the downstream slot was less affected by the
detonation wave.

6. Acknowledgements
The authors also thank the US Department of Energy for the appointment of Prof. Paniagua to the Faculty
Research Participation Program at the NETL. The authors would also like to thank the Government of Israel, the
Ministry of Defense, Mission to the USA for the support in the experimental campaign, and Peter Salek and Bebe
Wang for their help running the experiments.

7. References
[1]

S. W. Theuerkauf, F. R. Schauer, R. Anthony, D. E. Paxson, C. A. Stevens, and J. L. Hoke, “Comparison of
simulated and measured instantaneous heat flux in a rotating detonation engine,” 54th AIAA Aerosp. Sci.
Meet., vol. 0, no. January, 2016, doi: 10.2514/6.2016-1200.

[2]

A. Roy, Bedick C., Strakey P., Sidwell T., Ferguson D., Sisler A., Nix., A., “Development of a threedimensional transient wall heat transfer model of a rotating detonation combustor,” 54th AIAA Aerosp. Sci.
Meet., vol. 0, no. January, pp. 1–12, 2016, doi: 10.2514/6.2016-0902.

[3]

J. Braun, J. Sousa, and G. Paniagua, “Numerical Assessment of the Convective Heat Transfer in Rotating
Detonation Combustors Using a Reduced-Order Model,” Appl. Sci., vol. 8, no. 6, p. 893, May 2018, doi:
10.3390/app8060893.

[4]

K. B. Johnson, D. H. Ferguson, and A. C. Nix, “Use of Convolutional Neural Network Image Classification
and High-Speed Ion Probe Data Towards Real-Time Detonation Characterization in a Water-Cooled Rotating
Detonation Engine,” Proc. ASME Turbo Expo, vol. 3-B, pp. 1–15, 2022, doi: 10.1115/GT2022-83401.

[5]

K. Goto et al., “Cylindrical Rotating Detonation Engine with Propellant Injection Cooling,” J. Propuls. Power,
vol. 38, no. 3, pp. 410–420, 2022, doi: 10.2514/1.B38427.

[6]

S. Chakravarthy, O. Peroomian, U. Goldberg, and S. Palaniswamy, “The CFD++ Computational Fluid
Dynamics Software Suite,” in SAE Technical Paper Series, Sep. 1998, vol. 1. doi: 10.4271/985564.

[7]

Athmanathan V., Braun J., Ayers Z.M., Fugger C.A., Webb A.M., Slipchenko M.N., Paniagua G., Roy S.,
Meyer T.R., “On the effects of reactant stratification and wall curvature in non-premixed rotating detonation
combustors,” Combust. Flame, vol. 240, p. 112013, Jun. 2022, doi: 10.1016/j.combustflame.2022.112013.

17

[8]

R. J. Goldstein, “Film Cooling,” in Advances in Heat Transfer, 1971, pp. 321–379. doi: 10.1016/S00652717(08)70020-0.

[9]

Athmanathan V., Fisher J.M., Ayers Z., Cuadrado D.G., Andreoli V., Braun J., Meyer T., Paniagua G., Fugger
C.A., Roy S.., “Turbine-integrated High-pressure Optical RDE (THOR) for injection and detonation dynamics
assessment,” in AIAA Propulsion and Energy 2019 Forum, Aug. 2019, pp. 1–15. doi: 10.2514/6.2019-4041.

Downloaded by James Braun on September 6, 2024 | http://arc.aiaa.org | DOI: 10.2514/6.2024-0815

[10] Athmanathan V., Rahman K.R., Lauriola D., Braun J., Paniagua G., Slipchenko M., Roy S., Meyer T., 2021,
“Femtosecond/picosecond rotational coherent anti-Stokes Raman scattering thermometry in the exhaust of a rotating
detonation combustor”. Combustion and Flame. Vol. 231, paper 111504 (12 pages). September
https://doi.org/10.1016/j.combustflame.2021.111504

18



## Metadata
- Source file: junk_drawer/braun-et-al-2024-design-analysis-and-test-of-a-cooled-rotating-detonation-combustor-through-axially-injected-stepped (2).pdf
- Extracted: 2026-05-18
- Category: academic-homework
