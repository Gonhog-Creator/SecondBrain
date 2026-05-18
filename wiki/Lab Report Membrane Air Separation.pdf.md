# Lab Report Membrane Air Separation.pdf

Source: junk_drawer/Lab Report Membrane Air Separation.pdf

Category: [[academic-lab]]

## Summary
November 15th, 2024 Dr. Kimberly Dickey Laboratory Support Professional North Carolina State University 911 Partners Way Raleigh, NC 27606 Dear Dr. Dickey, We hope this letter finds you well. We are writing to transmit the results and trends observed during our last experiment focused on separating air through a membrane, aimed at generating an oxygen-rich permeate stream and a nitrogen-rich residue stream. This experiment

## Full Content
November 15th, 2024
Dr. Kimberly Dickey
Laboratory Support Professional
North Carolina State University
911 Partners Way
Raleigh, NC 27606
Dear Dr. Dickey,
We hope this letter finds you well. We are writing to transmit the results and trends
observed during our last experiment focused on separating air through a membrane, aimed at
generating an oxygen-rich permeate stream and a nitrogen-rich residue stream. This experiment
was designed to advance our understanding of gas separation processes through experimental
and model simulation methods. This experiment's primary objective is to investigate the
separation efficiency of oxygen and nitrogen as influenced by several parameters, including feed
pressure, stage cut, and the configuration of the membrane modules, either in series or parallel.
Throughout the experiment, we varied the stage cut, defined as the ratio of the permeate
flow rate to the feed flow rate, to assess its impact on the effectiveness of the membrane
separation. Data was collected on flow rates and oxygen percentages from both the permeate and
residue streams, which allowed us to analyze how these factors contributed to the overall
separation performance. Through the results, it was concluded that increasing the stage cut
decreased the % O2 in the permeate and increased the % N2 in the retentate. It was also observed
that changing the pressure would result in steeper slopes or curves of % O2 or % N2 to stage cut,
and typically higher pressures resulted in higher % O2 in the permeate. One point of note was at a
stage cut of 0.3 for the series configuration, which showed higher pressures would result in lower % O2 in
the permeate past this point. The empirical data was complemented by a simulation model to

provide a comprehensive understanding of the mechanisms involved in membrane separation.
The results of this experiment enhanced our existing knowledge of membrane technology
and its application in gas separation. A detailed analysis of our collected data and findings was
provided to demonstrate how this experiment reinforced our existing knowledge of gas
membrane separation and how we can operate at optimal configurations to achieve better
efficiency. We appreciate the opportunity to execute this experiment.
If you have any questions while reviewing this report, please don’t hesitate to reach out.
Sincerely,
___________________
Jose Barbeito

Raghu Vansh Mereddy
Raghu Mereddy

_Aaron Dornseif__

Robert Hart__

Aaron Dornseif

Robert Hart

___________________
Linda Pomiranceva

__________________
Elisa Schlesner Alves

Membrane Air Separation
Group 10
Jose Maria Barbeito, Robert Hart, Elisa Schlesner Alves, Linda Pomiranceva, Aaron Dornseif,
Raghu Mereddy

Abstract
This experiment investigated the membrane separation of an air stream into an oxygen-rich
permeate stream and a nitrogen-rich residue stream, utilizing both experimental trials and virtual
simulation. By varying feed pressure, stage cut, and repeating trials for three distinct configurations:
a parallel configuration for co-current flow, a single module configuration for co-current flow with
analysis after the first stage, and a series configuration for co-current flow with analysis after the
second stage.[1]
In addition to our experimental work, a VBA simulation program was employed to model the
co-current membrane separation of a multi-component gas mixture. The simulation utilized input
data and compared the results against the experimental findings. Data collection included flow rates
and oxygen percentages at both the permeate and retentate streams, with 12 trials conducted for each
configuration across three pressure settings (20 psig, 40 psig, and 60 psig), and four-stage cuts (0.1,
0.3, 0.5, and 0.7).
Data analysis allowed us to interpret the relationship between stage cut and the mole
percentages of oxygen in the permeate and nitrogen in the retentate. Our findings highlight
significant trends related to parametric variations, contributing valuable insights into the
effectiveness of membrane separation under different operating conditions. A comparative
analysis of the experimental data was conducted to evaluate the consistency and accuracy of the
modeling approach. The results demonstrated that the series configuration achieved a crossover in
oxygen concentration due to increased nitrogen diffusion. Conversely, the parallel configuration
maintained higher oxygen concentrations, as the feed concentration remained consistent across
stages. These findings align with predictions from Fick’s Law. Overall, this experiment aims to
enhance the understanding of membrane technologies for gas separation applications [1].

ii

Table of Contents
Introduction....................................................................................................................................1
Theory............................................................................................................................................. 2
Experimental Procedure................................................................................................................6
Results and Discussion.................................................................................................................10
Conclusion.................................................................................................................................... 16
Recommendations........................................................................................................................ 18
Nomenclature............................................................................................................................... 19
References..................................................................................................................................... 21
Appendices....................................................................................................................................22

iii

List of Tables
Table 1. Valve Arrangements for the Various Configuration Settings for a Bore-side
Feed...………………………………………………………………………………………..……7
Table 2. Data Table for Parallel Configuration..………………………..…………………… 22
Table 3. Data Table for Series Configuration (Permeate Analysis of the First Stage)..........22
Table 4. Data Table for Series Configuration (Permeate Analysis of the Second Stage).… 23

iv

List of Figures
Figure 1. Relative Permeabilities of Some Common Gasses and Vapors in Silicon
Membrane…………………………………………………………………………….………….4
Figure 2. Experimental setup for the Membrane Air Separation Experiment with a Parallel
Connection of Two Membrane Separator Modules, a Co-current Flow Configuration, and a
Bore Feed.…………………………………………………………..…………..…………..……5
Figure 3. A Schematic Picture of the PRISM Separator With a Bore-side Air Feed…….…6
Figure 4. Parallel Membrane Module Configuration With Co-current Airflow.….………..8
Figure 5. Single Membrane Module Configuration……………………………..……………8
Figure 6. Series Membrane Module Configuration With Co-current Airflow .……….……8
Figure 7.Graph of % O2 and % N2 for the System in Parallel Configuration.…….………10
Figure 8. Graph of % O2 and % N2 for the System in Series (First Stage)
Configuration………………………………………………………..…………...………..……11
Figure 9. Graph of % O2 and % N2 for the System in Series (Second Stage)
Configuration.………………………………………………………………………...……...…12
Figure 10. VBA Data for Parallel and Single Membrane (First Stage)
Configurations..…………………………………………………………………………………13
Figure 11. VBA Simulated Data for Series 2 Membrane Module
Configuration.…………………………………………………………………….……………14

v

Introduction
We use the term permeation to refer to a vapor species that moves through a polymer
membrane. This process has three main stages: sorption, diffusion, and desorption. Sorption
involves the absorption of the vapor into the membrane, while desorption refers to the release of
the dissolved vapor back into the atmosphere. Both processes are equilibrium processes
governed by Henry's Law, which describes their relationship at equilibrium [1].
Permeation has numerous applications across industries and daily life. In gas separation
processes, it plays a crucial role in evaluating the effects of hydrogen on high-strength steel,
particularly in the petroleum and petrochemical sectors. In the medical field, for example,
permeation is key for drug delivery systems, such as polymer-based patches that release
medication through a membrane according to concentration gradients [2].
For an effective gas separation process to take place, a partial pressure gradient is
necessary. This gradient creates two different sides: the permeate, which contains the substance
that successfully passes through the membrane, and the retentate, which consists of the residual
substances that do not permeate the membrane [3]. In our experiment, the effectiveness of the
separation will be evaluated based on the levels of oxygen in the permeate stream and nitrogen in
the retentate stream. Another method to assess effectiveness is stage cut, the ratio of the permeate
flow rate to the feed flow rate [1].
Two hollow-fiber PRISM separators are used in this experiment. The modules contain
3,100 hollow fibers bundled in a stainless steel casing, with a membrane area of 3.5 m2. Oxygen
and nitrogen will permeate through the membrane at distinct flow rates, which will be measured
by two flowmeters. The percentages of each component will be measured in mol % using two
oxygen analyzers [1].

1

Theory
Permeation describes the process of a vapor or gas passing through a membrane, typically
made of a polymer [1]. Three distinct steps can be described in permeation: sorption, diffusion,
and desorption. Sorption refers to the absorption of vapor (or solute) species into the membrane,
while desorption involves the release of the dissolved solute back into the vapor phase. Sorption
and desorption are equilibrium processes that Henry’s Law can characterize in Equation 1.
Ci=Si Pi

(1)

In this equation, Ci represents the molar concentration of solute i, measured in mol/unit
volume, Si is its solubility, measured in mol/unit volume/unit pressure, Pi denotes its partial
pressure, in pressure units. The diffusion of solute i through the membrane is governed by Fick's
First Law, expressed in Equation 2.

(2)
The diffusive flux Ji is defined as the amount of solute, in mols, passing through a unit
area per unit time, with Di indicating the diffusivity of solute i, δ being the thickness of the
membrane, PTotal is the total pressure, and yi being the mole fraction of solute i.
Permeability, the product of diffusivity and solubility, allows us to express the permeation
rate of solute i through the membrane modules. This term is represented in Equation 3 and has
units of mol/m.s.Pa.

(3)
Permeance is introduced in Equation 4, and it is the ratio between permeability and the
thickness of the membrane layer. The units for permeance are mol/m2.s.Pa

2

(4)
Combining Equations 2 and 3 and introducing permeance as a term in the equation, we
develop a relationship between permeability and the diffusive flux of solute i, which is expressed
in Equation 5.

(5)
The permeation rate of solute i is expressed in Equation 6, combining terms such as
permeability and permeance,

(6)
Am is the total surface area per membrane module, which in our experiment has a value of
3.5 m2, and Fi is measured in units of mol/unit time.
A method to evaluate the effectiveness of the membrane separation is defined as the stage
cut, a measure that takes the ratio of the permeate flow rate to the feed flow rate. Stage cut is
expressed in Equation 7,

(7)
After assuming that the gasses behave as ideal mixtures and that the process operates
under isothermal conditions, Equation 7 can be further simplified to

(8)

3

If both streams have the same pressure value, further simplification implies that

(9)
Selectivity, another key technical term, is the ratio of permeability of species i relative to
that belonging to species j. Selectivity is important in the membrane separation process because
it indicates that a higher value will yield a better separation of species i and j. The term is
introduced in Equation 10.

(10)
A list of relative permeabilities of different common gasses and vapors is provided in
Figure 1. Those with higher permeabilities are said to be “fast"; meanwhile, a low permeability
indicates that the gas is “slow". The permeability gradient is the basis for the membrane
separation conducted in this experiment, separating the stream into two different streams: the
permeate, which is oxygen-rich, and the retentate, which is nitrogen-rich [1].

Figure 1. Relative Permeabilities of Some Common Gasses and Vapors in Silicon
Membranes.
Experimental

4

Figure 2. Experimental Setup for the Membrane Air Separation Experiment with a
Parallel Connection of Two Membrane Separator Modules, a Co-current Flow
Configuration, and a Bore Feed.
Figure 2 illustrates the experimental setup, which shows two separator modules with
co-current flow arranged in parallel, with the air feed introduced from the bore side.
Additionally, the separator modules can be configured in series using quick-connect fittings. The
experiments utilize two hollow-fiber PRISM separators manufactured by Air Products &
Chemicals. Figure 2 demonstrates the separation process occurring within a module, where air is
fed from the bore side. Each module contains 3,100 hollow fibers bundled within a stainless steel
casing with an outside diameter of 1 inch (25.4 mm) and a length of 3 feet (0.91m), providing
approximately 3.5 m2 of membrane area. The hollow fibers have an approximate outer diameter
of 450 microns and an inner diameter of about 300 microns; they are made from polysulfone that
has been post-treated with silicone to eliminate defects. During the separation process, oxygen
and nitrogen permeate through the fiber walls into the cylindrical shell at different rates, where
they are collected in a manifold as the permeate stream. Meanwhile, the less permeable nitrogen
and residual oxygen travel through the fiber lumens and exit from the end of the separator as the

5

retentate stream. Two flowmeters are used to measure the volumetric flow rates of the permeate
and retentate streams in liters (standard temperature and pressure) per minute, while two oxygen
analyzers assess the oxygen concentrations in both streams, expressed as a percentage by mole.
This experiment will solely focus on a co-current configuration, although it is important to
recognize the counter-current configuration can also be effective.

Figure 3. A Schematic Picture of the PRISM Separator with a Bore-side Air Feed
In Figure 2, the valves positioned at sections of the apparatus labeled A, B, C, and D are
adjusted to configure each tested setup. The required valve settings for each configuration under
investigation are summarized in Table 1 and later illustrated in Figures 4, 5, and 6.

Experimental Procedure
To begin this experiment, one must turn the power strip on and open the air supply valve.
Next, the two flow meters should be zeroed using the side switches. The two oxygen sensors
should also be activated and set to percentage mode. Their sensor caps need to be removed and
each one of them must be calibrated to atmospheric oxygen levels by adjusting the calibration
knob, replacing the caps once calibration is complete. Then, one must configure valves A, B, C,

6

and D to the first experimental setup, in parallel, displayed in Table 1. Airflow should also be
adjusted to 20 psig for our first trial using the regulator valve. The needle valve is to be set to
achieve a stage cut of 0.1, while also maintaining the airflow at 20 psig.
After these steps, one should record the oxygen percentages and flow rates; the top
readings correspond to the combined permeate streams for both membranes, while the bottom
readings reflect the combined retentate streams. This process is to be repeated for stage cuts of
0.3, 0.5, and 0.7. Then, the airflow must be increased to 40 psig and the previous steps must be
repeated for those values of stage cuts. Following that, the airflow regulator must be set to 60
psig and the steps should be repeated.
Finally, valves A, B, C, and D must be configured to a single membrane setup, as
illustrated in Figure 2. This configuration allows for measurements of the permeate and retentate
streams for the bottom membrane, the first in the series. Once this setup is complete, the last
steps are to be repeated. Once all data is collected, one must turn off the air supply, power strip,
and both oxygen sensors [1].
Table 1. Valve Arrangements for the Various Configuration Settings for a Bore-side Feed.
Configuration

Directional Valve Settings
A

B

C

D

←

↑

↓

↑

Single module configuration, →
co-current flow (analysis of
permeate & retentate after 1st
stage)

↓

↓

↑

Series configuration,
co-current flow (analysis of
permeate & retentate after
2nd stage)

↑

↑

↓

Parallel configuration,
co-current flow

→

7

Figure 4. Parallel Membrane Module Configuration With Co-current Airflow.

Figure 5. Single Membrane Module Configuration.

Figure 6. Series Membrane Module Configuration With Co-current Airflow.

8

System Shutdown
In case of an emergency, one must immediately close the compressed air supply valve.
Then, the needle valve should be partially opened, but not completely to avoid damaging the
valve mechanism. Next, the compressed air valve must be shut and the pressure regulating valve
must be fully opened to release any remaining air before closing it again. To preserve battery life,
one should turn off the switches on both oxygen analyzers. If the analyzers will not be used for
an extended period, sensor electrodes should be stored in an inert, oxygen-free environment to
prolong their lifespan. One must avoid exposing the electrodes to air for prolonged periods, as
they are costly to replace [1].

9

Results and Discussion

This experiment consisted of three system configurations across three pressures with four
different stage cuts, resulting in 36 unique trials. For each trial, the percent O2 in the permeate
and retentate were measured, in addition to the percent N2 in the permeate and retentate.

Figure 7: Graph of % O2 and % N2 for the System in Parallel Configuration.
Figure 7 demonstrates that as the stage cut increases the O2 % decreases in the permeate.
This inverse relationship highlights the balance between separation efficiency and the
composition of the output streams. It is also observed that for higher pressures the negative slope
of the curve increases, meaning O2 % has a greater dependence on changes in stage cut. This
finding suggests the efficiency of the process is increased under these conditions, allowing for
finer adjustments in the composition of the permeate stream.
It is also observed that the permeate O2 % taken at different pressures trends towards
converging at higher stage cuts, which indicates that the impact of pressure on oxygen

10

percentage at higher stage cuts becomes less significant. Conversely, the retentate N2 % diverges
as the stage cut increases. The figure shows that N2 % has a positive correlation to the stage cut
in the retentate, reinforcing the notion that as more feed is processed, meaning a larger value of
stage cut, the concentration of nitrogen increases.
From this figure, it can be observed that the O2% in the permeate and N2% retentate are
inversely proportional. This trend emphasizes the nature of the separation process: while the
oxygen percentage lowers in the permeate, the nitrogen percentage rises in the retentate.

Figure 8. Graph of % O2 and % N2 for the System in Series (First Stage) Configuration.
Figure 8 shows similar trends as the parallel co-current configuration- with O2 % having
a negative correlation with stage cut and the convergence and divergence of the permeate and
retentate respectively. This configuration differs in ways as well. The minimum O2 % in the
permeate is higher by approximately 10% when compared to the parallel setup. This higher
baseline level of oxygen percentage suggests that the separation efficiency is altered in this setup,
possibly due to variations in operating conditions that influence gas permeation rates.

11

The O2% also seems to vary less with changes in stage cut in comparison to the previous
configuration, which allows for the conclusion that this configuration offers a more stable
performance. Changes in the pressure seemed to increase the O2 % sensitivity to stage cut,
however, changes in pressure had a less pronounced effect when compared to the parallel
co-current configuration. This finding suggests that although pressure adjustments can enhance
the efficiency of the separation, the effect of pressure changes on percentage oxygen variability
is minimized in this setup.

Figure 9. Graph of % O2 and % N2 for the System in Series (Second Stage) Configuration.
Figure 9 shows the O2 % in the permeate is 34% and intersects at a stage cut of 0.3. This
means that at stage cuts below 0.3, it is more beneficial to have a higher pressure to increase the
amount of oxygen in the permeate stream, increasing the amount of nitrogen in the retentate
stream. At higher pressures, the permeate to % O2 appeared to follow an exponential decay trend,
when compared to the mostly linear plots of the other configurations. From Figure 9 it is

12

observed that % O2 reaches its lowest value in the permeate at a pressure of 60 and stage cut of
0.7.

VBA Simulation Analysis

Figure 10. VBA Data for Parallel and Single Membrane (First Stage) Configurations.
Figure 10 shows that the % O2 in the permeate decreases as the stage cut increases and
higher pressures correspond to steeper slopes. Figure 10 also shows that the % N2 in the retentate
increases as the stage cut increases. As the pressure increases, the % N2 has a greater dependence
on the stage cut.

13

Figure 11. VBA Simulated Data for Series 2 Membrane Module Configuration.
Based on the experimental data, the parallel and single membrane (series 1) module
configurations demonstrated similar permeate and retentate stream compositions at similar
pressures and stage cuts. The most notable difference is in the flow rates—the parallel
configuration can process higher feed flow rates at the same pressure and stage cut as the single
membrane module configuration since it has twice the surface area available for separation.
Given that the VBA simulation requires user variation of the feed flow rate to obtain the stage
cuts used in the experiment, it was not possible to differentiate between the two configurations
within the simulations. For these reasons, the two configurations were modeled by the same
simulation (Figure 10). The retentate concentrations from the first simulation were then used as
the feed concentrations for the second simulation of the series 2 membrane module configuration
(Figure 11).

14

Both VBA simulations agreed with the empirical data: higher-stage cuts yielded lower
concentrations of oxygen in the permeate and greater concentrations of nitrogen in the retentate.
As the feed pressure increased, the permeate flow rate increased but stream compositions
remained relatively unchanged. Although Figure 10 shows that higher feed pressures
corresponded to slightly higher permeate and retentate purities in oxygen and nitrogen,
respectively, these mole percent differences lie within an 11% range and 3% overall average
difference. The parallel and series 1 membrane module configurations produced higher oxygen
recoveries, whereas the series 2 configuration produced higher nitrogen recoveries. Additionally,
the series 2 simulation displayed a permeate O2% intersection around a stage cut of 0.3 with 25%
O2 in the permeate, which aligns with the experimental data (Figure 9). For the series 2
configuration, the simulation exhibited much lower O2% in the retentate at higher stage cuts and
the % N2 in the retentate varied less with changes in pressure compared to that of Figure 9.
The collected data and VBA simulation results underscore the fact that membrane
separation is an equilibrium process relying on several factors such as diffusion. The
interrelationship between the permeate and retentate streams highlights the need to optimize
operating conditions according to the desired purified component. If a higher concentration of
oxygen in the permeate is desired, the stage cut should be lowered and a parallel or series 1
configuration should be utilized. Maximizing the applied pressure can enhance the separation
because diffusion can be driven by high-pressure differences. These trends closely align with the
experimental data, confirming the reliability and accuracy of the VBA simulations as well as the
collected data.

15

Conclusion
In conclusion, this experiment, which involved three system configurations across three
distinct pressures and four distinct stage cuts, yielded 36 unique trials in total that effectively
measured the percent oxygen and nitrogen in both permeate and retentate streams. The results
indicated a clear inverse relationship between the oxygen percentage in the permeate and the
nitrogen percentage in the retentate, particularly as stage cuts increased. It was noted that, as
stage cut rises, the oxygen percentage in the permeate decreases, with higher pressures
increasing the susceptibility of this relationship.
Figure 7 illustrates that at higher pressures, the negative slope of the curve becomes
steeper, highlighting the dependence of oxygen percentages on changes made to stage cut values.
While the permeate oxygen percentages converge at higher stage cuts, the retentate nitrogen
percentages diverge, demonstrating a positive correlation with stage cuts. This behavior follows
the trends observed in the parallel co-current configuration, with a few observed distinctions: the
minimum oxygen percentage in the permeate was approximately 10% higher in this
configuration, and there was less variability associated with changes in the stage cut.
The findings of our experiment suggest that the system is less sensitive to variable
fluctuations in the parallel co-current setup, which could be an advantage when a consistent
oxygen percentage is desired. The intersection point at a stage cut value of 0.3 suggests a critical
point in the separation process. Moreover, the data shows an exponential decay trend in the
permeate oxygen percentage at higher pressures, contrasting with the mostly linear trends
obtained from the other configurations. An increase in the flow rate of the permeate was also
connected to yielding a lower purity due to a more ineffective separation of the streams.

16

Overall, the membrane air separation experiment reinforces the existing knowledge that
the process operates as an equilibrium process influenced by diffusion mainly because of the
observed trends that the purity of the permeate was reduced when the flow rate was increased. To
maximize the purity of the permeate, the most efficient strategy was proved to be minimizing the
stage cut while maximizing the applied pressure. Consistent patterns in the retentate nitrogen
percentages across the setups confirm the reliability of these observations.
The VBA simulations for the parallel and single membrane module configurations
yielded similar results, with both configurations demonstrating consistent trends in the mole
percent oxygen (O2) in the permeate and mole percent nitrogen (N2) in the retentate. As the
stage cut increased, the O2 concentration in the permeate decreased, and the N2 concentration in
the retentate increased. Additionally, higher feed pressures led to higher permeate flow rates but
had minimal effect on stream compositions. The simulations confirmed that higher-stage cuts
resulted in lower O2 concentrations in the permeate and greater N2 concentrations in the
retentate, with small variations in the O2 and N2 mole percentages between different
configurations. These results were consistent with the empirical data, validating the accuracy of
the VBA model and supporting the observed trends in oxygen and nitrogen recoveries.
Overall this experiment was a great way to learn about air membrane separation. It
demonstrated the practical application of key concepts such as Henry’s Law, Fick’s Law, and
fluid dynamics. By combining hands-on experimentation with simulations and analysis, it
offered a clearer understanding of these principles in real-world contexts.

17

Recommendations
Based on findings from this experiment, some recommendations can be made for further
replications to enhance understanding of diffusion and optimization of membrane separation
processes. Additional configurations could be explored, such as counter-current setups. This
could provide insights into how flow direction influences the efficiency and purity of the process.
The addition of a wider range of feed pressures could help identify the starting points at
which oxygen and nitrogen separation efficiency begin to change in a significant manner.
Pressure values lower than 20 psig and higher than 60 psig could be important to identify optimal
operating conditions.
Following the previous recommendation, the addition of smaller increments in stage cuts,
such as 0.15, 0.20, and 0.25, could yield more data on how slight adjustments affect separation
outcomes. Just like adding a wider range of feed pressures, smaller changes in stage cuts could
also help identify optimal operating conditions.
In regards to our VBA simulation, something that could provide more detailed results is
the integration of more sophisticated modeling software into this experiment. A more detailed
prediction of the permeation process under varied parameters would be possible, which could
further be compared to experimental data to observe similarities and differences in the results
observed.

18

Nomenclature

Variable

Definition

Permeation

The movement of a vapor through a polymer
membrane

Sorption

The first stage of permeation

Diffusion

The second stage of permeation

Desorption

The third stage of permeation

Ci

The molar concentration of the solute i, in
units of mol/unit volume

Si

The solubility of solute i, in units of mol/unit
volume/unit pressure

Pi

The partial pressure of the solute i, in pressure
units

Ji

The diffusive flux of solute i, in units of
mol/unit time/unit area

Di

The diffusivity of solute i, in units of (length
unit)2/unit time

δ

The thickness of the membrane layer across
which diffusion of solute i occurs, in length
units

Ptotal

The total pressure, in pressure units

Yi

The mole fraction of solute i

Permeability

The product of diffusivity and solubility

Permeance

The ratio between permeability and the
thickness of the membrane layer

Fi

The molar flow rate, in units of mol/unit time.

Am

The total surface area per membrane module
19

that is normal to the permeation flow
θ

Stage cut, the ratio of permeate flow to the
feed flow rate

Retentate/raffinate/residue/non-permeate

Stream that goes through the membrane
module without crossing the membrane film

Permeate

Stream that goes through the membrane
module crossing the membrane film

ɑij selectivity

The ratio of permeability of species i relative
to that of species j

20

References
[1] M. Cooper, P. Lim, K. Dickey, and K. Dickey, “Membrane Air Separation Experiment” CHE
331 Course Handout, North Carolina State University, Raleigh, NC.
[2] “What Is Permeation? (a Definitive Guide).” n.d. Www.twi-Global.com.
https://www.twi-global.com/technical-knowledge/faqs/what-is-permeation.
[3] FUJIFILM. 2022. “How Do Gas Separation Membranes Work? | Complete Guide.” Fujifilm |
Blog. December 28, 2022.
https://gsmblog-us.fujifilm.com/blog/how-do-gas-separation-membranes-work/.

21

Appendices
Raw Data Tables
Table 2. Data Table for Parallel Configuration

Table 3. Data Table for Series Configuration (permeate analysis of the first stage)

22

Table 4. Data Table for Series Configuration (permeate analysis of the second stage)

23



## Metadata
- Source file: junk_drawer/Lab Report Membrane Air Separation.pdf
- Extracted: 2026-05-18
- Category: academic-lab
