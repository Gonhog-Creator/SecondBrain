# CHE 330 - Convection and Radiation Experiment Handout (08_26_2019).pdf

Source: junk_drawer/CHE 330 - Convection and Radiation Experiment Handout (08_26_2019).pdf

Category: [[academic-lecture]]

## Summary
Department of Chemical & Biomolecular Engineering North Carolina State University CHE330 Convection and Radiation Experiment Objective To study, analyze, and compare the extents by which free convection, forced convection, and radiation contribute to the heat transfer from a heated cylinder under various temperature and air flow conditions.

## Full Content
Department of Chemical & Biomolecular Engineering
North Carolina State University
CHE330

Convection and Radiation Experiment

Objective
To study, analyze, and compare the extents by which free convection, forced convection, and
radiation contribute to the heat transfer from a heated cylinder under various temperature and air
flow conditions.

Background and Theory
(1) Natural or Free Convection
When a hot object is suspended in stationary ambient fluid (which can be gas or liquid), heat will
be lost from the hot object via natural or free convection. Natural convection occurs because hot
fluid, being less dense generally, will rise above cooler fluid that is generally denser. Thus, the
fluid immediately surrounding a hot object will get heated and will rise and be displaced by cooler
ambient fluid. The resulting fluid circulation will carry heat away from the hot object and dissipate
it to the rising fluid. The heat transfer rate from the hot object via natural convection, Qnc, is given
by:
Qnc = Hnc As (Ts - Ta)

(1)

where Hnc is the natural convection heat transfer coefficient,
Ts is the surface temperature of the hot object,
Ta is the temperature of the ambient fluid away from the hot object,
As is the heat transfer surface area of the hot object.
For a hot metal cylinder of diameter D that is suspended in ambient air, which is the
special case of interest in this experiment, Hnc is given by the following simplified
empirical equation [1]:

 P. Lim, M. Cooper, K. Dickey and A. Crothers, Dept. of Chemical & Biomolecular

Engineering, NC State University, Raleigh, NC 27695, revised January 2, 2016.

Hnc(W/m2K) =1.32[(Ts - Ta)/D]0.25

(2)

(2) Forced Convection
When a mechanical means such as a fan, blower, or pump is used to drive a fluid over a hot object,
heat is transferred from the hot object to the fluid flowing over it, and the mode of heat transfer is
known as forced convection. The heat transfer rate from the hot object via forced convection, Qfc,
is analogous to Equation 1:
Qfc = Hfc As (Ts - Ta)

(3)

where Hfc is the forced convection heat transfer coefficient and the other parameters are as defined
previously. Hfc can be estimated from an empirical correlation for the Nusselt number defined for
the forced convection system, i.e.
𝐻𝑓𝑐 𝐷
𝐾

≡ 𝑁𝑢 = 0.3 +

0.62 𝑅𝑒 0.5 𝑃𝑟 0.33
[1+(

0.4 0.66 0.25 [1 + (
𝑃𝑟

)

]

𝑅𝑒

0.5

)
282000

]

(4)

This correlation was developed for forced convection of fluid over a straight cylinder of diameter
D [2]. In the correlation, Re and Pr are, respectively, the Reynolds and Prandtl numbers of the fluid
defined by

𝑅𝑒 ≡
𝑃𝑟 ≡

𝑈𝑐 𝐷
𝑣

=

𝜌𝑈𝑐 𝐷
𝜇

𝐶𝑝 𝜇
𝐾

(5)
(6)

where ν ≡ μ/ρ = kinematic viscosity of the fluid,
μ = viscosity of the fluid,
ρ = density of the fluid,
C p = specific heat of the fluid,
k = thermal conductivity of the fluid,
Uc ≡ corrected velocity of the fluid (corrected for blockage) = 1.22Ua for air flow
Ua ≡ free-stream air velocity

(3) Radiation
In contrast to conduction and convection that require a medium for heat transfer, radiation requires
no medium for heat transfer. Radiation transfers energy via electromagnetic waves that can travel

through vacuum. The rate of radiant energy transfer from an emitting object with a surface area As
and a temperature Ts to its surroundings at temperature Ta by is given by:
Qr =   F As (𝑇𝑠4 − 𝑇𝑎4 )

(7)

where σ = Stefan Boltzmann constant = 56.7 10-9 W/m2 K4
ξ = the emissivity of the surface (dimensionless)
F = view factor for the emitting object, often assumed to be 1.0.
To conform to the standard form of heat transfer equation, Q = H As ΔT, which introduces
the heat transfer coefficient H for either conduction and convection, one may analogously
define a radiation energy transfer coefficient Hr such that the standard form of the heat
transfer equation also applies to radiation energy transfer, i.e.
FAs(𝑇𝑠4 − 𝑇𝑎4 ) = Qr  Hr As (Ts - Ta)

(8)

which requires that
𝐻𝑟 ≡

F (𝑇𝑠4 − 𝑇𝑎4 )
(Ts−Ta)

= F (𝑇𝑠2 + 𝑇𝑎2 )(𝑇𝑠 + 𝑇𝑎 )

(9)

Unlike the heat transfer coefficients for conduction and convection, which have some theoretical
basis, the energy transfer coefficient Hr defined for radiation does not have a sound theoretical
basis. It is essentially a fitting parameter with no predictive capability. Equation 9 indicates that
Hr will vary greatly with temperature.

Method Designed for Studying Convection and Radiation Heat Transfer
A horizontal metal cylinder of known diameter and length is heated electrically at a
known adjustable rate while being exposed to air under varying airflow conditions. The
cylinder is insulated at both ends and at contact points with support to minimize
conduction losses. The voltage and current applied to the cylinder will be measured,
along with the air speed and temperatures of the cylinder and ambient air. The
contributions of free convection, forced convection, and radiation to the heat loss from
the heated cylinder under the various temperature and airflow conditions will be
determined by an analysis of the data in conjunction with the prescribed equations for the
heat transfer coefficients of the three heat transfer modes.

Equipment Setup
The apparatus is the HT14 Combined Convection and Radiation Apparatus made by Armfield,
which is represented by a mimic diagram on a computer screen as shown in Figure 1. Air enters
the vertical duct from the bottom of the apparatus, flowing upward toward a heated cylinder. After
the air is heated, it leaves the top of the apparatus and enters the atmosphere. During trials testing
forced convection, a fan is used to drive air over the heated cylinder; the fan is not used in trials
testing free convection. Air velocity (Ua) is measured using an anemometer located in the middle
of the duct, while the temperature of the heater (Ts) and inlet air (Ta) are measured by
thermocouples.
The HT14 apparatus is supported by HT10XC Heat Transfer Service Unit, which is an orange
color box with dials and switches and which provides an option for manually setting and recording
the experimental parameters. Furthermore, there is a remote option through an USB connection
that permits the Service Device Unit to be hooked up to a Windows 10 computer so that the
apparatus can be monitored and controlled from the computer (via the mimic diagram, see Section
(2) under Procedure).

Procedure
(1) Pre-Experiment Check
Familiarize yourself with the HT14 Combined Convection and Radiation Apparatus, the
HT10XC Heat Transfer Service Unit.
Ensure that the horizontal cylinder on the HT14 apparatus is located at the top of the stainless steel
duct, with the thermocouple located on one end of the cylinder. If
necessary, loosen the thumb screw on the mounting support that holds the cylinder and rotate the
cylinder to adjust the dotted angular scale indicator to -90°. Ensure that the thumb screw is securely
tightened after any adjustment.
Ensure that the USB cable is connected to both the HT10XC service unit and the computer.
Also ensure the following: (1) the thermocouple that is attached to the heated cylinder is connected
to the socket T10 on the front of the HT10XC service unit, (2) the thermocouple that is located in
the vertical duct is connected to the socket T9 on the service unit, (3) the main lead from the fan
(terminated at the connection box alongside the fan) is connected to the socket marked Output 1
at the rear of the HT10XC, (4) the lead from the anemometer in the vertical duct is connected to
the socket marked Ua on the front of the service unit, and (5) the service unit is plugged onto a
wall socket.

Figure 1. Mimic diagram of experimental apparatus.

Toggle the LCB circuit breaker switch to OFF; the fan will not be used in the study of natural
convection but will be used in the study of forced convection. Open the throttle plate at the front
of the fan to allow air to enter the fan casing, by turning the adjusting knob anticlockwise.
Set the VOLTAGE CONTROL potentiometer to minimum (anticlockwise) and the selector switch
to REMOTE then connect the power lead from the heated cylinder on HT14 to the socket marked
O/P 3 at the rear of the service unit.

(3) Experimental Procedure
Turn on the power switch on the HT10 service unit and activate the HT14 software program. Load
Exercise C. Click the
button on the toolbar to invoke the mimic diagram of the HT14
apparatus. When the temperature readings displayed for T9 and T10 are stable (they should be
identical or very close to each other), click the
button to record the initial readings for T9 and
T10, along with that for V, I, and Ua, which should each equal to 0.
Experimental trials should be completed using the optimized run order shown in Table 1; the
specified run order minimizes time needed to complete all specified testing by reducing the
difference in temperature between data points. To begin, set the heater voltage on the mimic
diagram to 20.0 volts by scrolling the up and down arrows on the dialog box for the heater control
at 83. Note that the number entry on the heater control box is NOT the actual heater voltage but it
is proportional to the heater voltage. The actual heater voltage is shown below the heater control
box with the V unit. The readings for heater current, air flow velocity Ua, ambient air temperature

in the duct T9, and the surface temperature of the heated cylinder T10 are displayed on the mimic
diagram. When the T10 reading stabilizes, click the
button to record the readings of all five
parameters: T9, T10, V, I, and Ua in Table on the toolbar. Then click the
button for the next
run.
Repeat the above procedure for each trial specified in Table 1. Avoid setting the heater voltage in
excess of 20 V when studying natural convection; otherwise the life of the heating element that is
embedded in the metal cylinder will be sharply reduced at an excessively high temperature. For
trials investigating forced convection and radiation (e.g. when applied air velocity > 0 m/s), turn
on the fan on the HT14 apparatus. Click the
button on the toolbar to invoke the mimic
diagram of the HT14 apparatus. Adjust the screw on the throttle plate to achieve the desired airflow
velocity (Ua) of 1.0 m/s. A continuous adjustment of the throttle plate screw may be needed to
maintain a constant Ua value. When the system reaches a steady state, as indicated by stable
readings for the five parameters being monitored (in particular, T10), click the button to record
the readings of T9, T10, V, I, and Ua.

Data Analysis
The dimensions of the heated cylinder are given as D = 0.010m and L = 0.070 m. Therefore, the
heat transfer area for the heated cylinder is As = πDL = 0.0022 m2 The emissivity of the cylinder
surface is given as ξ = 0.95. The view factor F for the heated cylinder is assumed to be 1.00.

 Rate of electrical heat input to the cylinder is given by Qin = V*I
 Total rate of heat loss from the cylinder is given by QTot = Qc + Qr
 Rate of heat loss due to natural convection is given by Qc = HcAs (Ts - Ta)
Table 1. Optimized trial order for Convection and Radiation experiment.
RUN #
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

Voltage (V)
20
20
15
20
12
15
20
20
12
15
8
15
15

Air Velocity (m/s)
0
1
0
3
0
1
5
7
1
3
0
5
7

14
15
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

12
12
8
12
5
8
8
5
8
5
5
5

3
5
1
7
0
3
5
1
7
3
5
7

 Rate of heat loss due to radiation is given by Qr = HrAs (Ts - Ta)
 Heat transfer coefficients for natural convection, forced convection, and radiation (Hnc, Hfc,
and Hr) can be calculated from the data using Equations 2, 4-6 and 9.
1) Plot on a single figure Hnc and Hr as a function of T10 reading in K. Determine the cross-over
temperature at which Hnc and Hr are numerically equal. Discuss important trends and
conclusions.
2) Plot on a single figure Hfc and Hr as a function of T10 reading in K for the various tested airflow
velocities. For each airflow velocity, determine the cross-over temperature at which Hfc and Hr
are projected to be numerically equal by interpolating/extrapolating based on the appropriate
linear and non-linear fits of data trends. Consider the uncertainties of projected cross-over
temperatures. Discuss important trends and conclusions.
3) Compare the calculated heat transfer rate due to convection Qc (Qnc and Qfc) with the calculated
heat transfer rate due to radiation Qr for varying voltages and air velocities. Discuss important
trends and conclusions.
4) Compare Qin and QTot amongst a selection of trials to demonstrate any differences. Discuss
important trends and conclusions.

References
1. W. H. McAdams, Heat Transmission, 3rd edn., McGraw-Hill, New York (1959).
2. S. W. Churchill and M. Bernstein, “A Correlating Equation for Forced Convection from Gases
and Liquid to a Circular Cylinder in Cross Flow”, J. Heat Transfer, 99, 300-306 (1977).



## Metadata
- Source file: junk_drawer/CHE 330 - Convection and Radiation Experiment Handout (08_26_2019).pdf
- Extracted: 2026-05-18
- Category: academic-lecture
