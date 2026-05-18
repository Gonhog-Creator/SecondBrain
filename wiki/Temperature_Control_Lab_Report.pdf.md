# Temperature_Control_Lab_Report.pdf

Source: junk_drawer/Temperature_Control_Lab_Report.pdf

Category: [[other]]

## Summary
October 11th, 2024 Dr. Kimberly Dickey Laboratory Support Professional North Carolina State University 911 Partners Way Raleigh, NC 27606 Dear Dr. Dickey, I hope this letter finds you well. Within the attached experimental report, you will find information detailing several temperature control methods for a water mixing system. The five relevant control algorithms were proportional, integral, derivative, proportional-integral, and

## Full Content
October 11th, 2024
Dr. Kimberly Dickey
Laboratory Support Professional
North Carolina State University
911 Partners Way
Raleigh, NC 27606
Dear Dr. Dickey,
I hope this letter finds you well. Within the attached experimental report, you will find
information detailing several temperature control methods for a water mixing system. The five
relevant control algorithms were proportional, integral, derivative, proportional-integral, and
proportional-integral-derivative control. The main objective of this experiment was to compare
the effectiveness of three different automatic feedback control schemes with that of manual
control.
Based on the results, both systems were viable control methods—the percent differences
between the manual and automatic control systems were 1.19% and 4.91%, respectively. The PI
automatic control algorithm was found to be the superior method for temperature control when
using automatic control, but manual control ultimately demonstrated greater accuracy. This
experimental effort solidified our understanding of various feedback control schemes, and the
MATLAB simulation results mirrored these findings, particularly in demonstrating the stability
of the PI control. During this experiment, we observed occasional discrepancies in our recorded
data. This discrepancy primarily came from the observed cold stream flow rate, which varied
notably when recording the value for data collection.
As chemical engineers, we can apply this knowledge to achieve desired parameters in
unit operations or process systems. Further inquiries about this topic include why manual
controls showed a lower percent difference than automatic controls.
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

Temperature Control
Group 10
Jose Maria Barbeito, Robert Hart, Elisa Schlesner Alves, Linda Pomiranceva, Aaron Dornseif,
Raghu Mereddy

Abstract
A series of runs for three different feedback control algorithms—proportional-only (P),
proportional-integral (PI), and proportional-integral-derivative (PID)—were conducted to
compare the effectiveness of each algorithm in achieving a stable set point temperature of 105°C
for a mixed liquid stream. The system controller maintained a steady temperature and flow rate
for a hot stream while adjusting the flow of a cold water stream according to the prescribed
algorithm. A MATLAB simulation was utilized to model the temperature response of the system,
facilitating an analysis of the control strategies in a virtual environment before conducting
physical experiments. By varying the proportional gain (KP), integral gain (KI), and derivative
gain (KD), the contributions of each control type were assessed. The optimal response was
characterized by quick adjustments with minimal oscillations, a small offset, quick settling, and
low sensitivity to disturbances. The feedback control actions were also compared with those of
manual control.
In the proportional control runs, higher P values correlated with more sensitive controller
responses, resulting in sharper initial temperature corrections but sustained oscillations. Although
these responses were minimized with lower P values, a greater offset ensued. The inclusion of
integral control for PI runs was most effective at lower I values, eliminating oscillations and the
offset inherent in proportional control. The addition of derivative control stabilized the PID
feedback control for lower D values at the expense of response speed. Based on these features,
process performance was optimized using the PI automatic control method with optimal P, I, and
D values of 0.8, 0.055, and 0, respectively. The optimal values for the MATLAB simulation were
found to be KP = 10, KI = 1, and KD = 0. While the automatic control scheme demonstrated
effective temperature control, manual control was deemed to be more precise.

ii

List of Contents
Introduction........................................................................................................................1
Theory................................................................................................................................. 2
Experimental...................................................................................................................... 6
Results and Discussion.......................................................................................................8
Conclusion........................................................................................................................ 21
Recommendations............................................................................................................ 22
Nomenclature................................................................................................................... 23
References......................................................................................................................... 25
Appendices........................................................................................................................26

iii

List of Tables

Table 1. Guideline for selecting direct- and reverse-acting controllers........................ 3
Table 2. Controller Operated in Manual Mode.............................................................26
Table 3. Controller Operated in Automatic Mode........................................................27

iv

List of Figures

Figure 1. Scheme of the temperature control apparatus................................................7
Figure 2: Final Mixed Temperature versus Controller Output Value.......................... 9
Figure 3: Temperature vs. Time (Group 1)....................................................................11
Figure 4: Temperature vs. Time (Group 2)................................................................... 12
Figure 5: Temperature vs. Time (Group 3)................................................................... 13
Figure 6: Temperature Distribution Between Run One and Run Two of Fine-Tuning
Trials (5°F Intervals)........................................................................................................15
Figure 7: Temperature Distribution Between Run One and Run Two of Fine-Tuning
Trials (5°F Intervals)........................................................................................................16
Figure 8: MATLAB simulation results for virtual automatic control, showing the
variation of KP while both KI and KD were held constant at 0.....................................18
Figure 9: MATLAB simulation results for virtual automatic control, illustrating the
variation of KI while KP and KD were held constant at 10 and 0, respectively........... 19
Figure 10: MATLAB simulation results for virtual automatic control, showing the
variation of KD while KP and KI were held constant at 10 and 1, respectively............ 20

v

Introduction
Process control that is both effective and efficient is crucial to achieve the desired
outcomes in any operational unit or process framework. Historically, manual control—where
human operators manage the process—has been the most straightforward approach and utilized
for many years [1]. However, it is often characterized by imprecision, unreliability, and
inefficiency, and also has a larger potential for human error, especially when used in challenging
situations or over extended durations [2]. In contrast, the introduction of automated control
systems allowed for more precise, reliable, and efficient outcomes. These systems typically
employ either mechanical or electronic devices, which are often integrated into computers that
allow for a more targeted control of the processes [1].
The most prevalent type of automatic control system is feedback control. A feedback
control system constantly observes a process and adjusts it to ensure that one or more output
parameters remain within a specified range [3]. In this method, the actual value of a controlled
variable is continuously compared to the previously defined target value, known as the set point.
When discrepancies arise between the controlled variable and the set point, adjustments are made
to a manipulated variable that influences the controlled variable [1]. If the control algorithm is
effective, these changes will force the output, which is the controlled variable, to follow the
desired input, which in this case is the set point [3].
A typical feedback control system consists of several components. A sensor will measure
the controlled variable's current state and relay this information to a controller. The difference
between the set point and the actual measurement will then be assessed. A defined algorithm will
process this error signal, resulting in adjustments made to the manipulated variable. In addition
to manual and automatic trials, MATLAB was utilized to simulate the feedback control system,

1

enabling a thorough evaluation of the different control algorithms before practical
implementation.

Theory
In this experiment, 5 different types of control were introduced and later analyzed.
1) Proportional Control
This is the simplest form of control algorithm, in which the controller output C(t) and the
controller action are directly proportional to the error, e(t), as expressed mathematically in
Equation 1,

(1)
In which the proportional constant KP is known as the controller/proportional gain and is
an adjustable parameter. Co is defined as the bias setting in which the controller output may be
raised or lowered independent of the error, also seen as the controller output before any
identification or response to the error is set in. The ± sign indicates that both signs can apply,
depending if the controller is set up to act directly or reverse. A direct-acting means that an
increase in its output will lead to an increase in the controller action, and the opposite is true for a
reverse-acting controller. When selecting the type of controller, the guidelines provided in Table
1 can be used.

2

Table 1. Guideline for selecting direct- and reverse-acting controllers.
Process Gain

Positive

Negative

Direct-Acting Actuator

Direct-Acting Controller

Reverse-Acting Controller

Reverse-Acting Actuator

Reverse-Acting Controller

Direct-Acting Controller

Proportional control will always generate an offset, defined as a steady-state deviation
from the set point. Although it cannot be eliminated, it can be reduced by increasing the
controller gain KP. In contrast, a KP that is too large can create a prolonged oscillation.
Proportional control is only used for specific processes that can tolerate some offsets or are not
sluggish. Sluggish applies to processes that have long dead times and respond slowly to changes
made in the manipulated variable.

2) Integral Control
Integral control can eliminate offset when used alongside proportional control or
proportional (PI) and derivative control (PID). In an integral control system, the output C(t) is
described by Equation 2.

(2)
𝛕I is known as the integral/reset time and is an adjustable parameter for Integral Control.
Co is the bias setting of the controller. What allows the offset to be eliminated or a steady state
correction is the integral control forcing the controller to change continuously as long as there is
an error. This method acts slowly when compared to proportional control because there is a need
to monitor and evaluate the error history with time. The response can be speeded up by reducing
the reset time, but it will result in prolonged oscillations and larger overshoots.
3

3) Derivative Control
Equation 3 successfully describes the output for derivative control, C(t).
(3)
The derivative time, expressed as 𝛕D is the adjustable parameter of derivative control.
This type of control acts in such a way that allows the controller to adjust the manipulated
variable before the controlled variable gets affected too much by being pushed under or beyond
the set point. It is designed to reduce oscillations and generate stabilization in feedback control
by making a gradual change in the controlled variable, either toward or away from the target
point. It takes longer to reach a steady state while simultaneously tending to propagate any noise
in the controlled variable. The derivative controller tends to over-predict and over-adjust the
manipulated variable, which is why it is commonly used in conjunction with the proportional and
integral control (PID). By itself, it is not able to eliminate the offset.

4) Proportional-Integral (PI) Control
This type of control combines the rapid and sensitive response of proportional control
with integral control and its ability to eliminate offset. The output C(t) of a PI controller is
described by Equation 4 below.

(4)
In this equation, KI, the integral gain, is defined by KI= KP/𝛕I. When the elimination of
offsets is important, PI controllers are implemented, having control over flow, pressure,
temperature, level, and composition.

4

5) Proportional-Integral-Derivative (PID) Control
Equation 5 successfully introduces the output C(t) of a PID controller.

(5)
The derivative gain, KD, is defined as KD= KP𝛕D. This type of control is useful for
sluggish processes or situations where PI control generates an excessive amount of oscillations.
To determine if a process is sluggish enough for the implementation of a PID controller, one
should analyze the ratio between dead time and the characteristic time constant, i.e. 𝛕Dead/𝛕P. If the
ratio is bigger than 1, a PID control will work better, meaning that the process is sufficiently
sluggish. However, if 𝛕Dead/𝛕P is less than 0.5, the process is not sluggish enough. If the ratio falls
between 0.5 and 1, either a PI or a PID controller would work.

Calculations for Experimental Final Temperature
First, we assume the specific heat and density of water is 1.0 Btu/(lbm.oF) or 1.0
kcal/(kg.oC) and 8.34lbm/gal or 1.0g/ml, respectively. Next, we calculate the expected
temperature using the equations and relations below.
Equation 6 describes the change in enthalpy of hot and cold streams, assuming negligible
temperature loss and that only energy transfer is occurring.

(6)
Additionally, if flow work is assumed to be negative, Equation 6 reduces to:

(7)

5

Where ṁ is the mass flow rate, Cp is the heat capacity, ΔT is the change in temperature
from the inlet to the final mixture, and the subscripts C and H are associated with the cold and hot
streams, respectively. If you even further assume that Cp is constant between the two streams,
the equation used to estimate the final temperature becomes.

(8)
Experimental
Figure 1 displays a representation of how the temperature control apparatus works. It
combines hot and cold water streams to create a mixed stream at an intermediate temperature.
The mixing tank (4) has a capacity of 1750 ml. Temperatures of the hot, cold, and mixed streams
are monitored throughout the experiment using thermocouples. The temperature of the latter is
relayed to a temperature controller (5), which provides feedback to a pneumatic valve (3) that
controls the flow of cold water. The controller then compares the thermocouple output with a
user-defined set point, using the difference to generate an output based on the specified control
algorithm. This output, in the form of a current signal, is sent to a signal converter, which
transforms it into a pneumatic signal (mA to psig). This signal adjusts the air pressure in the
valve, allowing it to open anywhere from 0% (fully closed) to 100% (fully open).

6

Figure 1. Scheme of the temperature control apparatus
A 40-gallon water heater (1) serves as the hot water reservoir. Temperatures and flow
rates for both streams can be read from digital displays and rotameters (2a, 2b). The cold water
rotameter displays the flow rate in gallons per minute, while the hot water rotameter is calibrated
such that
(9)
To allow the flow of the hot and cold water, the manual Hoke valves must be fully
opened. The valves are considered to be fully open when the blue arrowhead handle points
upward on the hot water line and downward on the cold water line; when the opposite is true,
they are fully closed. Pressure gauges on both lines display the respective pressures. The cold
water line has a feature that allows for adjusting the temperature of the cold water stream. The
temperature can be lowered or raised by closing the through-flow valve and opening the bypass
valve, which redirects the cold water flow to a cooling or heating coil, situated in a
constant-temperature bath. These adjustments for line pressure, hot water flow rate, and cold

7

water temperature are valuable for investigating how controlled disturbances impact the
performance of various control algorithms.
The controller in use is an Omega CN8DPT-305 Series programmable temperature
controller, capable of operating in either manual or automatic mode. In automatic mode, the
controller can act as a proportional-only controller, with KI=0 and KD=0, a proportional-integral
controller, with KD=0, or as a proportional-integral-derivative controller. In automatic mode, data
is logged by the computer. The software allows the operator to modify controller settings via the
keyboard. Users can adjust the set point, proportional gain, integral gain, and derivative gain in
the monitor. Each run is labeled and saved at the end by the user. Data must be plotted into
graphing software, such as Excel, to create plots of the temperature response profiles from
multiple runs on a single graph to illustrate parametric trends.

Results and Discussion
Part 1: Percent Discrepancy Between the Theoretical Temperature and the Experimental
Temperature of Manual and Automatic Control
For every manual and automatic trial, calculations were made to check if each reached a
steady state by calculating the % discrepancy between the theoretical temperature of the mixed
stream, Tmix, theory, and the calculated temperature of the mixed stream, Tmix, experimental. A good
agreement between the two values was observed if the percent discrepancy was lower than 5%.
The average discrepancy for the manual control data was 1.19%. In comparison, the
automatic control had an average discrepancy of 4.91%. While both ways of temperature control
were relatively accurate, automatic control had higher outliers in percent discrepancy.
Specifically, run 8 and run 12 of the automatic control trials had average discrepancies of nearly

8

22%. These outliers were likely the result of the flow rate being very low at the time the cold
water flow rate was noted. Both runs read a cold flow of 0.09 ml/min, and the other data points
analyzed averaged around 0.54 mL/min.
The manual control measurements were more precise due to the existence of large
outliers in the automatic control data points. These values happened to be taken at a local
minimum and therefore don’t match the theoretical number calculated using equations 6, 7, and
8. If this experiment was performed again, the automatic control could very well provide more
consistent measurements.

2. Results of the manual control runs
Manual control trials were an acceptable method of control. This was concluded by the
low difference in the mixing temperatures of the experiment versus the theoretical mixing
temperature.

Figure 2. Final Mixed Temperature versus Controller Output Value

9

It is speculated that manual control saw better results because the transition time
associated with manual control was on a longer scale, allowing for the instantaneous
measurements to reach a steady state before being recorded. The automatic control differed in
this regard because it changed states instantly causing the recorded value for this to be at an
unsteady state. Based on this data, from a numerical approach, manual control is an effective
strategy for control. It is possible other factors could count against manual control being an
effective method. The primary issue against the effectiveness of manual control is it requires an
operator. Manual control also has more margin for error, given a human operator may incorrectly
set desired inputs. From the experiment it was observed that no restrictions were set for inputting
a specific value, this supports that errors in operation are possible and should be considered when
determining the effectiveness of a control method. Based on the results it is reasonable to
conclude that manual control may be a viable operation method but should be considered
carefully.

Part 3: Analyzing the Contributions of Proportional, Integral, and Derivative Control Types on
Automatic Control Systems
Below are the results for the automatic trials, graphing the temperature of the mixed
stream over time. There were three groups of tests, testing the three control types: proportional,
integral, and derivative (P, I, and D) controllers. After all three control types were tested, several
tests were performed to fine-tune the three optimal values selected to achieve a mixing
temperature of 105°F. But first, it is necessary to understand how each independent variable
affects the decrease in temperature.

10

In the first group, I and D were held constant at a value of 0, with P changing to values of
0.4, 0.6, 0.8, and 1.

Figure 3. Temperature vs. Time (Group 1)

It can be seen in Figure 1 that as P increases, the initial plunge in temperature increases,
reaching lower and lower temperatures. Along with this change, the final mixing temperature
decreases as P increases, dropping from a final mixing temperature of 125°F to 116°F. In
addition to the increase in depth and lowering final mixing temperature, the temperature
fluctuated sinusoidally more with increasing P values, as can be seen comparing P=1 to P=0.4.
After the four trials, an optimal P value of 0.8 was chosen, giving a balance between sinusoidal
action and final mixing temperature.

11

In the second group, the integral control variable was changed, testing values of 0.05, 0.1,
0.25, and 0.5. All trials were run with constant values for P and D, being 0.8 and 0 accordingly.

Figure 4. Temperature vs. Time (Group 2)

As can be seen in Figure 2, increasing the value of I introduces a wave-like form to the
temperature mixing, with the most severe peaks occurring at a value of 0.5. These peaks have a
maximum range of around twenty degrees, giving wide temperature fluctuations. In addition to
the wave-like signals, increasing the integral control variable lowered the final temperature
value, giving a much farther final temperature to the set control point of 105°F. After running all
four trials, the optimal value of 0.05 was chosen.

12

In the third group, the derivative control variable (D) was varied while P and I were held
at constant values of 0.8 and 0.05 respectively. Values for D were chosen to be 5, 10, 25, and 50.

Figure 5. Temperature vs. Time (Group 3)

As can be seen in Figure 3, increasing the value of D introduced a wave-like function to
the mixing temperature over time, similar to the effect of changing the integral control variable
yet with a smaller “wavelength.” A value of 5 had no sinusoidal effect, broadening the initial
plunge effect from the P and I values chosen from previous trials. Despite this positive effect, it
caused the final mixing temperature to stabilize much slower, meaning the final temperature of
105°F was not reached within the 3-minute window. Because of this, the optimal value chosen
for the derivative control value was 0.
Part 4: Results of Fine-Tuning Trials
For the fine-tuning trials, previous optimal values were altered to reach the target
temperature of 105°F with the least amount of overshoot and highest accuracy. Initially, four runs
13

were scheduled, but due to the success of the trial, only two runs were required. Run 1 had P, I,
and D values of 0.8, 0.06, and 0, respectively. This initial control was extremely close to our
target value, bringing the final mixing temperature to 104.99 at the three-minute mark. In an
attempt to achieve a better result during the measuring window (two minutes and 30 seconds
after the start of the trial), a second run was performed with P, I, and D values of 0.8, 0.055, and
0 respectively. This trial brought the final mixing temperature to 105.02 at the end of the
three-minute mark, with values within the 2-and-a-half-minute measuring window hovering
between 104.8 and 105.1. Because of this success, subsequent trials were deemed unnecessary
by the teaching advisor.
In conclusion, we chose a proportional control value of 0.8 due to the less severe initial
plunge compared to higher P values in addition to the small distance to the final target
temperature. A value of 0.055 was chosen for the integral control value due to its positive effect
on the final temperature while not imparting a wave-like effect on the temperature. A final value
of 0 was chosen for the derivative effect, primarily due to the conclusion that while a low D
value has some positive effect on the mixing temperature, the increase in stabilization time led to
more negative effects than positive effects.

Part 5: Frequency Distribution of Fine-Tuning Trials
By separating the temperature range into intervals of 5°F, temperature readings for both
runs can be counted and analyzed. As can be seen in the graph, Run 2 already had the majority of
values within the 100°F to 105°F target range.

14

Figure 6: Temperature Distribution Between Run One and Run Two of Fine-Tuning
Trials (5°F Intervals).

Despite this, it was concluded that a slight change in the integral control value could
lower the number of readings above 120°F and between 95°F and 100°F. From Run 1 to Run 2,
“I” was changed from 0.06 to 0.055. The number of readings between 95°F and 100°F dropped
from 27 to 0, and the number of readings above 120°F dropped from 9 to 0. The only other
considerable change was that the number of readings in the 105°F to 110°F range increased from
5 to 17, though this was considered acceptable. Overall, the change was considered a success.
For the reader's enjoyment, a similar graph with more precise temperature ranges has been
provided, showing an increase in temperature readings at the 105°F target for Run 2 compared to
Run 1.

15

Figure 7: Temperature Distribution Between Run One and Run Two of Fine-Tuning
Trials (5°F Intervals)
By separating the temperature range into intervals of 1°F, temperature readings for both
runs can be counted and analyzed as they approach the desired temperature of 105°F. As
displayed in Figure 5, Run 1 already had the majority of values within the 100°F to 101°F target
range. As the temperature approaches 105°F, Run 2 begins to have more measured values in the
desired range than Run 1. This further shows how accurate Run 2 was to the desired temperature.

Part 6: Matlab Simulation
The MATLAB Simulink program (PID_TControl.mdl) was used to simulate the
automatic control of an adiabatic mixing process, where the objective was to reach a setpoint of
40°C for a mixing tank within five minutes. The simulation was designed to examine how
varying the proportional gain (KP), integral gain (KI), and derivative gain (KD) impacts the
system’s response. By comparing the simulation results with experimental data, we aimed to
better understand the factors that contribute to optimizing the PID control system.

16

In a proportional controller, the output signal is directly proportional to the input error,
which represents the difference between the setpoint and the current process variable. The
proportional gain (KP) determines how sensitive the controller is to this error. When KP is large,
even small deviations from the setpoint result in significant adjustments, which can cause the
system to overcorrect and lead to oscillations or instability. Conversely, if KP is too small, the
controller may respond sluggishly, causing the system to take longer to reach the desired
setpoint. Effective tuning of KP is crucial to achieving a balance between rapid response and
system stability, avoiding either excessive oscillation or slow convergence.
In the first set of simulations, KP was varied while both KI and KD were held at zero. This
setup allowed for the observation of how proportional control alone affects system behavior. The
results showed that larger values of KP caused a faster approach to the setpoint by immediately
reducing the error between the process value and the desired temperature. For instance, when KP
was increased from 0.1 to 10, the system reached the setpoint much faster, confirming that
proportional gain is crucial for reducing initial error. However, despite faster correction, there
remained a steady-state error, as expected when KP alone is used. This is because proportional
control does not fully eliminate the error- it only reduces it based on the size of the error at any
given time.

17

Figure 8: MATLAB simulation results for virtual automatic control, showing the variation
of KP while both KI and KD were held constant at 0
Next, the integral gain (KI) was introduced to the system to address the steady-state error.
By accumulating the error over time, KI continuously adjusts the control output to drive the error
toward zero. The simulations demonstrated that adding KI helped eliminate the residual error that
KP could not correct. As the value of KI was increased, the system’s ability to reduce steady-state
error improved. However, excessively high values of KI led to increased overshoot and slower
initial response, as the controller took more aggressive corrective action. The optimal KI value of
1 struck a balance between eliminating steady-state error and maintaining system stability, which
provided a smoother and more efficient control response.

18

Figure 9: MATLAB simulation results for virtual automatic control, illustrating the
variation of KI while KP and KD were held constant at 10 and 0, respectively
Finally, the role of derivative gain (KD) was explored. KD acts on the rate of change of the
error, which helps prevent overshoot and dampens oscillations in the system. After identifying
the optimal values for KP and KI, varying KD allowed for fine-tuning the system’s response. A KD
value of 0 produced the most stable system behavior with minimal oscillations and overshoot.
Increasing KD further did not offer significant improvements and, in some cases, led to increased
noise sensitivity, which made the system less stable.

19

Figure 10: MATLAB simulation results for virtual automatic control, showing the variation
of KD while KP and KI were held constant at 10 and 1, respectively
When comparing the simulation results to the experimental data, there were noticeable
similarities. In both the simulations and the lab experiments, increasing KP reduced the error
quickly, but a residual error remained without the integral action. The experimental data also
confirmed that adding KI successfully minimized this steady-state error, much like in the
simulations. One key difference was the presence of more oscillations in the experimental
results, which were less apparent in the simulations. These discrepancies are likely due to
real-world factors such as sensor noise, time delays, and environmental disturbances, which the
simulations did not fully account for.
In conclusion, the MATLAB simulations provided valuable insights into how each PID
control parameter affects system performance. KP is essential for reducing initial error, KI is
necessary to eliminate steady-state error, and KD helps stabilize the system by reducing overshoot

20

and oscillations. The theoretical trends observed in the simulations were consistent with the
experimental results, though real-world disturbances introduced some variations. This
demonstrates that while simulations are an excellent tool for understanding control dynamics,
real-world applications require additional consideration of external factors.

Conclusion
The comparative analysis of manual and automatic control methods yielded insightful
results regarding their effectiveness in achieving steady state and accurate temperature readings.
The findings indicated that while both control methods maintained a low average discrepancy
between the theoretical and experimental mixed stream temperatures- 1.19% for manual control
and 4.91% for automatic control- the manual approach exhibited greater precision, likely due to
the longer transition times allowing measurements to stabilize before recording data.
Despite the overall accuracy of the automatic control system, it displayed notable
outliers, particularly in runs 8 and 12, which were influenced by low cold water flow rates. These
outliers, occurring at local minima, significantly impacted the average discrepancies.
Nevertheless, the automatic system demonstrated a higher capacity to achieve a steady state at
the desired temperature more frequently than the manual control.
The optimization trials for the automatic control system revealed key insights into the
effects of the proportional, integral, and derivative (PID) controller parameters on temperature
management. The selected optimal values — 0.8 for proportional, 0.055 for integral, and 0 for
derivative control—facilitated precise temperature regulation, effectively minimizing overshoot
and ensuring a consistent final temperature of approximately 105°F. The MATLAB simulations
played a crucial role in analyzing the system's response to different PID settings, allowing for a

21

comprehensive comparison of their effects on temperature control. By visualizing the
temperature response curves, MATLAB helped identify the most effective control parameters,
providing a solid foundation for our experimental design. The selected optimal values (KP=10,
KI=1, and KD=0) facilitated precise temperature regulation, effectively minimizing overshoot and
ensuring a consistent final temperature of approximately 105°F(40.5°C).
While manual control showed higher accuracy in specific instances, the automatic control
system's ability to achieve a steady state and meet temperature targets makes it a compelling
choice for future operations. Our findings suggest that manual control may be a viable
operational method. Still, with the right adjustments and fine-tuning, automatic control could
offer improved efficiency and accuracy in future experiments.

Recommendations
For future replications of this experiment, we recommend reading over the benefits and
drawbacks that each type of controller offers and understanding each very well before coming to
the experiment. When experimenting, different combinations of the parameters P, I, and D
(proportional, integral, and derivative, respectively) should be tested to check for alternative
manners to direct the controlled variable to the set point and measure how each of them impacts
the results. Another recommendation for the experimental setup would be to mark the hot water
flow meter graduations with a contrasting color, such as white so that measurements can more
accurately be discerned and thus more accurate experimental data.

22

Nomenclature
Variable

Definition

e(t)

Error- the difference between the set point and
the controlled variable, i.e. e= SP - PV

PV

Process variable

SP

Setpoint

KD

Derivative gain, KD= KP𝛕D

𝛕D

Derivative time

KI

Integral gain, KI= KP/𝛕I

𝛕I

Integral/reset time

KP

Controller/proportional gain

Co

Bias setting by which the controller output
may be raised or lowered independent of the
error

C(t)

Controller output

PI

Proportional control

PID

Proportional and derivative control

PD

Proportional-derivative

ID

Integral-derivative

𝛕Dead

Dead time

P

Proportional gain (during automatic mode)

I

Integral gain (during automatic mode)

D

Derivative gain (during automatic mode)

Tmix, theory

Theoretical temperature expectation

Tmix, experimental

Experimental temperature measurement

ΔHC

Enthalpy of the cold stream

ΔHH

Enthalpy of the hot stream
23

Cp

Heat capacity

ṁ

Mass flowrate

Tm

The temperature of the mixed streams

ΔT

Change in temperature from the inlet to the
mixture temperature

24

References
[1] M. Cooper, P. Lim, K. Dickey, and K. Dickey, “Temperature Control Experiment” CHE 331
Course Handout, North Carolina State University, Raleigh, NC.
[2] O’BRIEN, TERRY. n.d. “Which Is Better: Automatic or Manual Internal Controls? |
Schellman.” Schellman Compliance.
https://www.schellman.com/blog/soc-examinations/automated-or-manual-soc-controls.
[3] “Feedback Control System - an Overview | ScienceDirect Topics.” n.d.
Www.sciencedirect.com.
https://www.sciencedirect.com/topics/engineering/feedback-control-system.

25

Appendices
Raw Data Tables
Table 2. Controller Operated in Manual Mode

26

Table 3. Controller Operated in Automatic Mode

27



## Metadata
- Source file: junk_drawer/Temperature_Control_Lab_Report.pdf
- Extracted: 2026-05-18
- Category: other
