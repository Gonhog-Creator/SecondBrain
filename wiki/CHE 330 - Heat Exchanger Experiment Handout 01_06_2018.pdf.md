# CHE 330 - Heat Exchanger Experiment Handout (01_06_2018).pdf

Source: junk_drawer/CHE 330 - Heat Exchanger Experiment Handout (01_06_2018).pdf

Category: [[academic-lab]]

## Summary
DEPARTMENT OF CHEMICAL & BIOMOLECUALR ENGINEERING NORTH CAROLINA STATE UNIVERSITY CHE 330 EVALUATION OF A DOUBLE-PIPE HEAT EXCHANGER† 1. Introduction Heat transfer is a common, important unit operation in the process industry. There are three modes of heat transfer: conduction, convection, and radiation. Conduction is the transfer of heat across a solid or stationary layer of a material. Convection occurs when heat is transferred via the motion of

## Full Content
DEPARTMENT OF CHEMICAL & BIOMOLECUALR ENGINEERING
NORTH CAROLINA STATE UNIVERSITY
CHE 330

EVALUATION OF A DOUBLE-PIPE HEAT EXCHANGER†

1. Introduction
Heat transfer is a common, important unit operation in the process industry. There are three modes
of heat transfer: conduction, convection, and radiation. Conduction is the transfer of heat across a
solid or stationary layer of a material. Convection occurs when heat is transferred via the motion of
a fluid, either under a temperature-induced density gradient (free convection) or a pressure gradient
(forced convection). Radiation is heat transfer via electromagnetic waves. Although radiation often
involves a high-temperature body (e.g. the sun), high temperature is not a necessary attribute for
radiation; for instance, the nightly heat loss from home occurs primarily through infrared radiation.
Efficient design of a heat transfer process requires a good understanding of the governing
parameters. For convective and conductive heat transfer, the heat transfer rate Q is governed by the
heat transfer area (A), the temperature driving force (∆T), and the overall heat transfer coefficient
(U) that is a composite of the thermal conductivity (k) of the material and local convective heat
transfer coefficient (h) at one or more phase boundary (see Theory). For a specified Q, a lower
equipment cost—which corresponds to a small heat transfer area A—is associated with either a
high ∆T or a high U.
Though not much used industrially, the double-pipe heat exchanger provides a simple, convenient
and clear-cut model for studying the key factors affecting convective and conductive heat transfer.
2. Objective
The objective of this experiment is to determine the heat transfer and resistance characteristics of a
single-pass, double-pipe heat exchanger that can operate in a co-current or counter-current mode.
3. Theory
A simple schematic of a double-pipe heat exchanger is given in Figure 1. In the studied case, hot
fluid flows through the inner tube of the heat exchanger, while cold water flows in the outer tube
(i.e. the “shell”). Heat is exchanged between the streams through the wall of the inner pipe. For a
double-pipe heat exchanger operating at steady state, the rate of heat transfer (Q) may be described
by the following general heat transfer equations [1]:

Q − 
=
mCˆ P (Te − To ) = m ' Cˆ P '(Te '− To ') = UA∆Tln

(1)

where m and m ' are the mass flow rates of the hot and cold streams, Ĉ P and Cˆ P ' are the specific
______________________________________________________________________________
†
M. Cooper, P. Lim, K. Dickey & A. Crothers, Department of Chemical Engineering, North
Carolina State University, Raleigh, NC 27695-7905, revised on January 6, 2018.

(a)

(b)

Figure 1. Schematic of double-pipe heat exchanger operation in (a) co-current and (b)
counter-current heat transfer configurations [2].
heat capacities of the hot and cold streams, and ∆Tln is the log mean temperature difference:

∆Tln ≡ log mean temperature difference ≡

∆Tone end − ∆Tother end
∆Tone end
ln
∆Tother end

(2)

Depending on whether the hot and cold water flow in the same direction (co-current heat exchange
configuration) as shown in Figure 1 (a), or opposite directions (counter-current heat exchange
configuration) as shown in Figure 1 (b), ∆Tln is defined differently:
•

Co-current Heat Exchange:
(T − T ') − (Te − Te ')
∆Tln =o o
(T − T ')
ln o o
(Te − Te ')

•

(3)

Counter-current Heat Exchange:
(T − T ') − (Te − To ')
∆Tln =o e
(T − T ')
ln o e
(Te − To ')

(4)

where To and To’ are the inlet temperatures of the hot and cold streams, while Te and Te’ are the
outlet temperatures of the hot and cold streams [1].
3.1.Wilson Method of Analysis
A key driver in heat exchange design is the overall heat transfer coefficient (U). Larger U values
require less heat exchange area to transfer a given amount of heat. Understanding the factors
influencing U requires a closer look at the path taken by heat as it transfers from the hot stream to
the cold stream. The cross-section of a typical double-pipe heat exchanger is described in Figure 2.
Since the hot stream in the inner pipe is at a higher temperature than the cold stream in the outer
pipe, the resulting temperature gradient causes heat to transfer from the hot stream to the cold

Figure 2. Cross-section of a typical double-pipe heat exchanger [3].
stream. However, in real-life practice the transferring heat encounters significant resistance from a
number of heat transfer resistors, as described by Equation 5:
1
1
1
𝑡𝑡𝑤𝑤
𝑅𝑅𝑖𝑖 𝑅𝑅𝑜𝑜
=
+
+
+� + �
𝑈𝑈𝑈𝑈 ℎ𝑖𝑖 𝐴𝐴𝑖𝑖 ℎ𝑜𝑜 𝐴𝐴𝑜𝑜 𝑘𝑘𝑤𝑤 𝐴𝐴𝑤𝑤
𝐴𝐴𝑖𝑖 𝐴𝐴𝑜𝑜

(5)

where hi and ho are the local convective heat transfer coefficients on the inside and outside surfaces
of the heat exchange tube, Ai and Ao are the corresponding areas of the inside and outside heat
exchange surfaces, Ri/Ai and Ro/Ao are the corresponding scale resistances on the inside and
outside heat exchange surfaces, tw, kw and Aw the wall thickness, thermal conductivity and mean
surface area (= 0.5Ai + 0.5Ao) of the material of construction of the heat exchange tube [1].

These heat transfer resistances (and Equation 5) are analogous to those for resistors in series in an
electric circuit. With this in mind, the total heat transfer resistance between the hot and cold streams
1
is equivalent to . Referencing Equation 5 and Figure 4, we can model the flow of energy as it
𝑈𝑈𝑈𝑈
travels from the hot stream to the cold stream, accounting for each heat transfer resistance that is
overcome along the way:
1
• Convective heat transfer resistance in the hot stream � 𝐴𝐴 � – resistance encountered by heat
•

ℎ𝑖𝑖 𝑖𝑖

as it transfers across the hot fluid’s boundary layer (see proceeding discussion)
𝑅𝑅
Scale resistance on the hot side �𝐴𝐴𝑖𝑖 � – resistance to heat transfer due to build-up of minerals
𝑖𝑖

or other deposits on the inside of the inner tube wall

•
•
•

𝑡𝑡

Conductive resistance �𝑘𝑘 𝑤𝑤𝐴𝐴 � – heat transfer resistance associated with heat transfer
𝑤𝑤 𝑤𝑤

through the metal pipe wall separating the hot and cold streams
𝑅𝑅
Scale resistance on the cold side �𝐴𝐴𝑜𝑜 � – resistance to heat transfer due to build-up of
𝑜𝑜

minerals or other deposits on the outside of the inner tube wall
1
Convective heat transfer resistance in the cold stream � 𝐴𝐴 � – resistance encountered by
ℎ𝑜𝑜 𝑜𝑜

heat as it transfers across the cold fluid’s boundary layer (see proceeding discussion)

Convective heat transfer resistance in a moving fluid arises from heat traveling across a transition
region between the stagnant, stationary fluid next to the pipe wall and the free-flowing section of
the stream unaffected by the wall (this region is described in transport phenomena as the “boundary
layer”); this phenomenon is described in Figure 3. The size of the boundary layer is affected by the
velocity of the fluid, the shape of the wall, and the physical properties of the fluid. In general, as
fluid velocity goes up, boundary layer thickness goes down. Thick boundary layers provide more
resistance to heat transfer than thin boundary layers. Boundary layer thickness is the primary
determinant of local convective heat transfer coefficient for each stream in the heat exchanger [1].

Figure 3. Model of fluid flow against a wall, showing boundary layer profile [4].
On a theoretical basis, provided that the flow is in the fully-developed turbulent regime, the local
convective heat transfer coefficient for a tubular surface may be estimated using the Dittus-Boelter
correlation:
𝑁𝑁𝑁𝑁 = 0.023𝑅𝑅𝑒𝑒 0.8 𝑃𝑃𝑟𝑟 0.3

(6)

where Nu is the Nusselt number, Re is the Reynolds number, and Pr is the Prandtl number. The
Nusselt number gives the ratio of heat transfer by convection to heat transfer by conduction, and
will therefore depend on the size of the boundary layers. Substitution of physical parameters for the
well-known Nu, Re, and Pr expressions gives the Dittus-Boelter correlation:

 ρvD 
hD
= 0.023 

k
 µ 

0.8


0.3
 CP µ 


 k 

(7)

For flow in a tube, D in Equation 7 is given by Di, the inside diameter of the tube (i.e. the outer
diameter of the inner pipe minus twice the wall thickness). For flow in the annular space between
concentric pipes, an estimate of the effective hydraulic diameter Dh can be made by treating the
region as a tube with hydraulic area Ah:

 ODouter − 2t w,outer 
 ODinner 
 − π 
Ah = π 

2
 2 


2

Dh = 2

2

‘ (8)

Ah

π

(9)

where ODouter is the outer diameter of the outer pipe, tw,outer is the wall thickness of the outer pipe,
and ODinner is the outer diameter of the inner pipe.
According to the correlation, if flow velocity (v) is varied while all other variables are held
constant, h should be proportional to v0.8:


 k 0.7 ρ 0.8CP 0.3  0.8
0.8
=
h 0.023 
v ≡ α v
0.5 0.2
 µ D


(10)

where the proportionality constant α is dependent on the physical properties of the fluid and the
temperature.
Equation 10 may be used in conjunction with Equation 7 to determine hi or ho from the
experimental data. This is the basis of the Wilson method of analysis. If the flowrate inside the
tube is varied while all other parameters are held constant, Equation 5 and 8 give

 1
 R R 
t
1
1
1
=
+ w +  i + o  +
≡ Ci +
0.8
UA  ho Ao k w Aw  Ai Ao  α i Ai vi
α i Ai vi 0.8
It follows that a plot of

(11)

1
1
1
versus 0.8 should yield a straight line with a slope equal to
and
UA
vi
α i Ai

an intercept equal to Ci.
Similarly, if UA is measured as a function of the flowrate in the annulus space,
 1
 R R 
t
1
1
1
=
+ w +  i + o  +
≡ Co +
0.8
UA  hi Ai k w Aw  Ai Ao  α o Ao vo
α o Ao vo 0.8

(12)

1
1
1
versus 0.8 should yield a straight line with a slope equal to
and an intercept
UA
α o Ao
vo
equal to Co. The value of thermal resistance of the wall (tw/(kwAw)) can be calculated from the
physical data. Once the values of αiAi, Ci, αoAo, and Co are known, the value of total scale
resistance (Ri/Ai + Ro/Ao) may be determined. The values determined for αi and αo from the
Wilson analysis may be compared with the corresponding values calculated from the physical
properties of the fluid using Equation 10 [1].

A plot of

4. Equipment
The experimental setup is shown in Figures 4-7. The heat exchanger consists of two concentric
stainless steel (Type 314) tubes with the dimensions specified in Table 1. The heat exchanger has
the following provisions: (1) two sets of rotameters and mass flow meters to measure the flowrates
of the heat-exchanging streams, (2) six thermisters to measure the temperatures of the streams at
the inlets, outlets and mid-points of the heat exchanger, (3) a re-circulating hot water reservoir
whose feed temperature is maintained constant by an electric heater in conjunction with a
temperature controller, (4) a re-circulating chilled water reservoir whose feed temperature is
maintained constant by the building’s chiller, (5) a pump that circulates the hot stream through the
heat exchanger and returns it to the reservoir tank, and (6) the heat exchange mode can be varied
between countercurrent and cocurrent by varying the settings of the cold flow valves as shown in
Figures 6 and 7.

Figure 4. Heat exchanger experimental setup.

Figure 5. Thermistor readout panel.

Figure 6. Valve settings for counter-current flow. Figure 7. Valve settings for co-current flow.
Table 1. Dimensions of double-pipe heat exchanger pipes.
Pipe
Inner
Outer

Outside Diameter, m

Wall Thickness, m

Length, m

0.0127

0.00076

3.048

Heat Transfer Area, m2
Average
Outer, Ao Inner, Ai

0.0190

0.00124

3.048

0.1216

0.1070

0.1143

Thermistor readings can be read off the thermistor panel by pressing the appropriate “Step” buttons
successively. Thermistors 1, 2, and 3 monitor the temperatures of the hot stream at the inlet, outlet
and mid-point, respectively, and they are activated by the left “Step” button on the panel.
Thermistors 4, 5, and 6 monitor the temperatures of the cold stream at the inlet, outlet and midpoint, respectively, and they are activated by the upper right “Step” button on the panel. The
“Step” buttons below the upper right “Step” button are not in service. For example, Figure 5 shows
the output from Thermistor 1.
The calibration equation for the hot-flow and cold flow rotameters are given, respectively, by:
𝑣𝑣ℎ𝑜𝑜𝑜𝑜−𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 = �1.296 ∗ 𝑅𝑅𝑅𝑅ℎ𝑜𝑜𝑜𝑜−𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 − 1.075�

𝐿𝐿
𝑚𝑚𝑚𝑚𝑚𝑚

𝑣𝑣 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐−𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 = �1.029 ∗ 𝑅𝑅𝑅𝑅𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐−𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 + 0.499�

where RR denotes the rotameter readings.

𝐿𝐿
𝑚𝑚𝑚𝑚𝑚𝑚

(13)
(14)

5. Experimental Strategy and Procedure
The heat transfer characteristics of the heat exchanger are determined using the Wilson's method of
analysis as described in the Theory section. Specifically, UA is measured as a function of the
flowrates and inlet temperatures of the fluid in the inner tube and the annular space.

Observe safety precautions as noted in the Laboratory Safety Procedures. In particular, avoid
contact with hot surfaces. Hot water is circulated through the inner tube of the heat exchanger by
the pump and re-circulating cold water from a chilled water reservoir is fed, first cocurrently and
then countercurrently, through the annular space between the concentric tubes. The flowrates of
the streams are measured by means of the rotameters and flow meters and the inlet and outlet
temperatures of the streams are measured by means of the thermisters. Care should be taken to
establish that the flows are turbulent and that steady state has been reached before recording the
data and going to a new run. How do you ensure that these two conditions are, in fact, met?
For each heat exchange mode, vary the hot and cold streams by 4 x 4 combinations for a total of 16
runs. Vary each of the hot and cold streams four times. Use the same set of four flowrates for the
hot stream while the flowrate of the cold stream is varied four times (the hot and cold streams may,
however, have different sets of four flowrates). Evenly space the four flowrate settings over as wide
a flow range as possible to extend the range of the Wilson analysis. For each of the 16
combinations of settings, record the flowrates and the inlet and outlet temperatures of the two
streams once steady state has been reached (typically 30-60 seconds). Then change the heat
exchange mode and repeat the flowrate and temperature measurements for the same 4 x 4
variations of the hot and cold streams for another set of 16 runs. Prior to entering the lab to
perform the experiment, prepare a spreadsheet/table containing the 16 flow combinations for each
configuration (i.e., 16 flow combinations for the co-current configuration and 16 flow combinations
for the counter-current flow configuration). Bring two copies of the table for use in the lab: one for
the raw data collector, and one for the person changing the flow rates during the experiment.
To ensure that all 32 trials are completed in reasonable time, it is recommended that the heat
exchange mode be kept the same until all 16 trials are complete and that the flow parameters are
systematically varied one at a time. Avoid switching the heat exchange mode back and forth or
varying more than one parameter at one time as these could introduce a large upset to the system
and extend the wait time for the steady state. Whenever the heat exchange mode is switched, an
extended wait time should be provided (about 15 minutes) for the first run to ensure that steady
state is reached.
After changing the hot or cold water flowrate, a suggested time to allow the system to reach steady
state is 30-60 seconds. From a theoretical perspective, at steady state Qhot should equal Qcold;
however, you may find that Qhot and Qcold are not quite equal in the laboratory. It can be reasonably
assumed that steady state has been reached if Qhot and Qcold are within 15% of each other. As a
confirmation that steady state has been reached, Equation 15 should be used:
|𝑄𝑄ℎ𝑜𝑜𝑜𝑜 − 𝑄𝑄𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 |
≤ 0.15
𝑄𝑄𝑎𝑎𝑎𝑎𝑎𝑎

where Qavg is the average of Qhot and Qcold.

(15)

6. Data Analysis
It is requested that you include the following information in a technical report:
• For each run, use the inlet and outlet temperature readings and the flowrate readings to
determine the respective energy gain/loss of the annular flow and the tube flows. Perform

•
•
•

•
•

an energy balance on the hot/cold streams for all trials. Does the amount of heat transferred
from the hot stream equal the amount of heat absorbed by the cold stream? Should it?
Explain.
Plot the temperature profile for each tested heat transfer configuration and discuss.
Calculate the overall heat transfer coefficient and demonstrate its dependence on the
flowrate by plotting 1/UA vs. 1/v0.8 for both sets of hot and cold flow data. The plots should
display 1/UA vs. 1/v0.8 for the same runs as were plotted in 1).
Perform the Wilson analysis and determine important values (e.g. αi, ho) and their
respective ranges of uncertainties. Discuss the findings and compare the results with the
corresponding values calculated from physical properties (evaluate at the average of the
inlet and outlet temperatures).
Calculate the value of heat transfer resistances and their uncertainties. Which term(s) in
Equation 5 caused the most resistance to heat transfer?
Determine which variables (if any) change between co-current and counter-current trials
and to what degree. Which mode is most efficient?

References
1. "Perry's Chemical Engineers' Handbook," by R. H. Perry and D. Green, Sixth Edition, pp
10-14 to 10-20, McGraw-Hill: New York (1984).
2. H. Bengtson and L. Stonecypher (Ed.), “Double Pipe Heat Exchanger Design,” located at
http://www.brighthub.com/engineering/mechanical/articles/64548.aspx, last accessed May 17,
2012.
3. J. Brown, A. Busaileh, D. French, D. Garrison and J. Johnson, “Heat Exchanger Experiment,”
CHE 330 Student Report (Spring 2012).
4. “Boundary layer flow” in McGraw-Hill Encyclopedia of Science and Technology, 5th edition,
McGraw-Hill: New York (2004).

Nomenclature
Notation
Definition
A
Heat exchange surface area upon which the overall heat transfer coefficient U is based
Heat exchange area defined by the inner surface area of the inner tube
Ai
Ao
Heat exchange area defined by the outer surface area of the inner tube
Aw
Mean heat exchange area of the inner tube = (Ai + Ao)/2
α
Proportionality constant defined in Equation 10
αi
Proportionality constant for the tube flow, see Equation 11
αo
Proportionality constant for the annular flow, see Equation 12
Ci
Intercept on Wilson plot for tube flow, see Equation 11
Co
Intercept on Wilson plot for annular flow, see Equation 12
Specific heat of the hot stream or generalized specific heat in Equation 7
Ĉ P
Specific heat of the cold stream
Cˆ '
P

h
hi
ho
k
kw
m
m '
Q
Ri
Ro
tw
To
To'
Te
Te'
U
<v>
<vi>
<vo>
∆Tln
ρ
µ

Local convective heat-transfer coefficient defined in Equation 7
Local convective heat-transfer coefficient on the inner (or hot) side of the heat
exchange surface
Local convective heat-transfer coefficient on the outer (or cold) side of the heat
exchange surface
Thermal conductivity
Thermal conductivity of the heat exchange tube material
Mass flowrate of the hot stream
Mass flowrate of the cold stream
Heat transfer rate
Heat transfer resistance due to surface scale on the inner heat exchange surface
Heat transfer resistance due to surface scale on the outer heat exchange surface
Thickness of the heat exchange wall
Inlet temperature of the hot stream
Inlet temperature of the cold stream
Outlet temperature of the hot stream
Outlet temperature of the cold stream
Overall heat transfer coefficient
Average flow velocity
Average flow velocity in the inner tube
Average flow velocity in the annular space
Log mean temperature difference defined by Equation (2), (6) or (8)
Fluid density
Fluid viscosity



## Metadata
- Source file: junk_drawer/CHE 330 - Heat Exchanger Experiment Handout (01_06_2018).pdf
- Extracted: 2026-05-18
- Category: academic-lab
