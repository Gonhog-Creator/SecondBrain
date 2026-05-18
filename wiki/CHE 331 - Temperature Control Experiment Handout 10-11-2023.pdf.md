# CHE 331 - Temperature Control Experiment Handout (10-11-2023).pdf

Source: junk_drawer/CHE 331 - Temperature Control Experiment Handout (10-11-2023).pdf

Category: [[academic-lab]]

## Summary
Department of Chemical & Biomolecular Engineering North Carolina State University CHE 331 Temperature Control Experiment* OBJECTIVE The objectives of this experiment are to study the characteristic features of three different control algorithms of a feedback control scheme and to compare the outcomes of the control actions with the outcome of manual control on the mixing of two liquid streams to produce a mixed stream of

## Full Content
Department of Chemical & Biomolecular Engineering
North Carolina State University
CHE 331

Temperature Control Experiment*

OBJECTIVE
The objectives of this experiment are to study the characteristic features of three different control
algorithms of a feedback control scheme and to compare the outcomes of the control actions with
the outcome of manual control on the mixing of two liquid streams to produce a mixed stream of
a desired temperature.
INTRODUCTION
Effective process control is essential in achieving desired results in any unit operation or process
scheme. Manual control by human labor is the simplest mode of control and has been in practice
long before the development of automatic control; however, it is imprecise, unreliable and
inefficient, particularly under difficult operating conditions and over an extended period.
Automatic control is more precise, reliable and efficient, and can be achieved by means of a
mechanical or electronic device—often a computer. This device acts according to a prescribed
algorithm chosen by the user in order to achieve the desired control.
In feedback control, which is the most common form of automatic control, the measured value of
a controlled variable is compared to the desired target value—called the set point. An appropriate
adjustment is then made as needed to a manipulated variable that affects the controlled variable.
The adjustment should direct the controlled variable to the set point, if the control algorithm is
effective. Figure 1 shows a block diagram for a generalized feedback control scheme. As shown
in Figure 1, a sensor measures the value of the controlled variable which is then compared to the
set point. Any difference—denoted by e(t)-- between the set point and the controlled variable is
Disturbance

Set Point

e(t)

Controller

C(t)

Actuator

Process

Controlled
Variable

Sensor
Figure 1. Feedback Control System.
* P. Lim, M. Cooper, K. Dickey and A. Crothers, Department of Chemical & Biomolecular
Engineering, North Carolina State University, Raleigh, NC 27695 revised August 7, 2022.

1

taken by the controller. e(t) is translated accordingly to a prescribed algorithm into an adjustment
on the manipulated variable. Depending on the prescribed algorithm, a range of control actions
may be taken.
In this experiment, you will use a mixing apparatus to study the characteristic features of three
common control algorithms of a feedback control scheme and to compare the outcomes of the
controller actions with the corresponding outcome of manual control. Before discussing the
control theory, you should familiarize yourself with the definitions of some frequently used
terms.
DEFINITIONS
Actuator (sometimes also known as the final control element) is the device which carries out a
change in the manipulated variable in response to a controller output.
Controller is the device which receives a process variable (PV) measurement, compares it to its
set point (SP), and, if necessary, comes up with an output signal that calls for a corrective action
to minimize the difference between the set point and measured value.
Dead time is the time lag between the initiation of an input change and the actual start of the
response.
Derivative control is a mode of control which uses the rate of change of error to estimate when
the set point will be reached, allowing control action to prevent the measured value of a process
variable (PV) overshooting the set point (SP). Derivative control is designed to stabilize
feedback control and reduce oscillation, but does not eliminate offset.
Derivative gain (KD = KPD) is a proportionality constant relating controller output to derivative
time; it is a tuning parameter for derivative action. A large KD will speed up the controller
response, but at the expense of a larger overshoot or a more sustained oscillation.
Derivative time (D) is the time constant that characterizes the derivative control action; for a
given controller gain KP, D is directly proportional to KD. Derivative time is the degree of
sensitivity of the output to derivative control.
Error is the difference between the set point (SP) and the measured value of a process (or
controlled) variable (PV), i.e., e = SP − PV.
Integral control is a mode of control in which the controller output is dependent on the
cumulative error history over some time period (see Equation 2).
Integral gain (KI = KP/I) is the proportionality constant which relates the controller output to
the integral of error with respect to time; it is an adjustable tuning parameter for integral action.
A larger KI will speed up the controller response, but at the expense of a larger overshoot or a
more sustained oscillation.

2

Integral time (I, also called the reset time) is the time constant that characterizes the integral
control action; a small I corresponds to a large integral gain KI, and the converse is true. Integral
time is the degree of sensitivity of the output to integral control. 1/I is called the reset rate.
Controller or proportional gain (KP) is the adjustable parameter for a proportional control
algorithm; it specifies the magnitude of the controller output and affects the response time of the
controller. Proportional gain is the degree of sensitivity of the output to proportional control.
Offset is the difference between the set point and the measured value of a process variable at
steady state; it is a characteristic feature of proportional-only control algorithm.
Proportional control is a mode of control in which the controller output is directly proportional
to the error, see Eqn 1 below; its characteristic feature is an offset.
Set point is the desired, target value for a controlled process variable.
BACKGROUND AND THEORY
(1) Proportional Control
Proportional control is the most basic form of control algorithm in which the controller output
C(t)--and, hence, the controller action--is directly proportional to the error e(t) as expressed
mathematically in Equation 1:
C(t) = Co  KPe(t)  Co  KP[SP − PV(t)]

(1)

The proportionality constant KP in Equation 1, known as the controller (or proportional) gain, is
an adjustable parameter. CO is the bias setting by which the controller output may be raised or
lowered independent of the error; it may also be viewed as the controller output when the
controller is first turned on before any response to the error is set in. The  sign in Equation 1, as
well as in Equations 2−5 to follow, indicates that either the + or the − sign could apply,
depending on whether the controller is direct-acting or reverse-acting. A controller is said to be
direct-acting if an increase in its output leads to an increase in the controller action; the converse
is true for a reverse-acting controller. The choice for a direct- or reverse-acting controller
depends on the sign of the process gain and whether a direct- or reverse-acting actuator (or final
control element) is used. The guidelines in Table 1 can be used to select a direct- or reverseacting controller.
Table 1. Guideline for selecting direct- and reverse-acting controllers.
Process Gain
Direct-Acting Actuator
Reverse-Acting Actuator

Positive
Direct-Acting Controller
Reverse-Acting Controller

Negative
Reverse-Acting Controller
Direct-Acting Controller

In either case, proportional control by itself (or proportional-only control) will always result in
offset, which is a steady state deviation from the set point. The offset may be reduced, though
not eliminated, by increasing the controller gain KP, but this may come at the expense of a
sustained oscillation when KP is set too high. Proportional-only control is used only for processes
3

that can tolerate some offsets or are not sluggish. A process is said to be sluggish or have a long
dead time if it responds slowly to changes in a manipulated variable
(2) Integral Control
In order to eliminate the offset, integral control must be used, either by itself, which is rare, or in
conjunction with proportional control (known as in PI) or proportional and derivative control
(known as PID). The output C(t) of an integral-only controller, as described mathematically by
Equation 2,
C(t) = Co  (1/I) e(t)dt

(2)

depends on the cumulative history of the error over the monitoring time period. I is known as
the integral or reset time and it is a characteristic and adjustable parameter for integral control.
CO is again the bias setting of the controller.
Integral control forces the controller to change continuously as long as there is an error, and this
makes possible the elimination of the offset or a steady state correction for a disturbance or a set
point change. Because of the need to monitor and evaluate the error history with time, integral
control is necessarily slower acting than proportional control. Integral response could be
speeded up by reducing the integral or reset time I, but this often comes at the expense of larger
overshoots and more sustained oscillations.
(3) Derivative Control
The output C(t) of a derivative-only controller is described mathematically by Equation 3,
C(t) = Co  D[de(t)/dt] = Co −+ Dd[(PV(t)]/dt

(3)

where D, the derivative time, is an adjustable parameter characteristic of derivative control.
Derivative control acts in a predictive manner that allows the controller to make changes to the
manipulated variable before the controlled variable is affected too much (pushed under or
beyond the set point) by a disturbance or an input change. It is designed to reduce oscillation
and stabilize a feedback control by making a more gradual change in the controlled variable,
either toward or away from the set point. By stretching out changes, derivative control takes
longer to reach a steady state and at the same time, it tends to propagate any noise in the
controlled variable. The later can make the derivative action ineffective because the derivative
controller will tend to over-predict and over-adjust the manipulated variable. Derivative control
is typically used in conjunction with the proportional and integral control (as in PID) because, by
itself, it is unable to eliminate offset.
(4) Proportional-Integral (PI) Control
Combinations of the basic control elements, proportional, integral and derivative, are often used
to combine some desirable attributes. Thus, proportional-integral (PI) control combines the rapid
and sensitive response of proportional control with the ability of integral control to eliminate
offset and proportional-integral-derivative (PID) control adds stability and reduces oscillatory
tendency of PI under certain circumstances. Other combinations, such proportional-derivative
(PD) and integral-derivative (ID), though theoretically possible are not used in practice because
4

they offer no significant advantages to negate their drawbacks, i.e., the presence of an offset in
PD and the conflicting nature of integral and derivative actions in ID. It has been estimated that
93% of feedback control in chemical process industries is based on PI, 2% on P-only, and 5% on
PID [1].
The output C(t) of a PI controller is described mathematically by Equation 4,
C(t) = Co  KP[e(t) + (1/I) e(t)dt] = Co  [KPe(t) + KI e(t)dt]

(4)

where KI, the integral gain, is defined by KI = KP/I. PI controllers are used for processes that
are not sluggish and for which the elimination of the offset is important, e.g., flow and level
control, pressure and temperature control, and composition control.
(5) Proportional-Integral-Derivative (PID) Control
The output C(t) of a PID controller is described mathematically by Equation 5,
C(t) = Co  KP{e(t) + (1/I) e(t)dt + D[de(t)/dt]}
= Co  {KPe(t) + KI e(t)dt + KD[de(t)/dt]}

(5)

where KD, the derivative gain, is defined as KD = KPτD. PID control is useful for sluggish
processes or processes for which PI control will show excessive oscillations.
A useful guideline for determining if a process is sufficiently sluggish to warrant a PID
controller is provided by the ratio of its dead time dead and its characteristic time constant P,
dead/P. If dead/P > 1, the process is sufficiently sluggish that a PID control will work better
than a PI control. If dead/P < 0.5, the process is not sluggish enough to require a PID control.
If 0.5 < dead/P < 1, either PI or PID control could work.
Proper Setting or Tuning of the Parameters of a Controller
A controller must be properly tuned in order for it to effectively control a process. Tuning
involves finding the combinations of parameters (KP, KI, and KD) that will direct the controlled
variable to the set point in a quick and stable manner. In this experiment, you will tune a
temperature controller and find the best combination of parameters that will effectively control
the temperature of a mixed stream resulting from the mixing of hot and cold streams.
EXPERIMENTAL
The mixing apparatus, shown in Figure 2, mixes hot and cold water streams to produce a mixed
stream with an intermediate temperature. The mixing tank (4) has a volume of 1750 ml. The hot,
cold and mixed stream temperatures are measured by thermocouples. The mixed stream
temperature value is used by a temperature controller (5) to provide a feedback control on a
pneumatic valve (3) that regulates the cold water flow. The thermocouple output is compared
with the set point (which is specified by the user) and the difference is used by the controller to
generate a controller output in accordance with the control algorithm specified by you. The
controller output in the form a current signal goes to a signal converter where it is converted to a
pneumatic signal (mA to psig). The latter adjusts the air pressure on the pneumatic valve so that

5

its valve opening can vary anywhere between 0-100% open, i.e., 0% corresponds to a fully
closed valve and 100% corresponds to a fully open valve.
A 40-gallon water heater (1) provides a hot water reservoir. Temperatures and flow rates of both
streams may be read off digital displays and rotameters (2a, 2b) for both streams. The cold water
rotameter reading gives the flowrate in gal/min while the hot water rotameter has the following
calibration:
volumetric flow rate v = 18*(rotameter reading RR) mL/min
(6)
To enable hot and cold water flow, manual Hoke valves must be fully opened. These valves are
fully open when the blue arrowhead handle is pointing upward on the hot flow line and
downward on cold flow line; the Hoke valves are fully shut when the converse is true. Pressure
gages on both lines register the line pressures. The cold water line has a provision (not shown in
the above figure) for changing the temperature of the cold water stream. The temperature may be
lowered (or raised) by closing the through-flow

Figure 2. Process schematic of temperature control apparatus [2].
valve and opening the bypass valve that permits the cold water flow to be diverted to a cooling
(or heating) coil maintained in a constant-temperature bath (such as an ice bath). The provisions

6

for changing the line pressures, flow rate of the hot flow, and temperature of the cold flow are
useful for studying the effects of controlled disturbances on the performance of the various
control algorithms.
The controller used is an Omega CN8DPT-305 Series programmable temperature controller that
can be operated in MANUAL or AUTOMATIC mode. In automatic mode, the controller can
function as a proportional-only controller (with KI = 0 and KD = 0), or a proportional-integral (PI)
controller (with KD = 0), or a proportional-integral-derivative (PID) controller.
With the controller set in an automatic mode, data are logged by the computer. The software
allows the operator to change controller settings at the keyboard. Set point, proportional gain,
integral gain, and derivative gain can all be set from the menu on the monitor. Each run is
labeled and saved at the end of the run by the user. You should bring a memory stick so that you
can copy the individual data files for each run for further analysis at your convenience. For
example, after the experiment, you may use Excel to plot the temperature response profiles of
several runs on a single figure to show a parametric trend.
You should be aware that the water lines from the main should have a gage pressure of 20-60psi.
If the water pressure should ever drop below 10 psig or the flow should fall below 0.20gpm, the
heater will automatically shut down. Notify the TA immediately if you notice any major
fluctuation in water pressure or flow rate.
PROCEDURE
Setting up the Apparatus
1. Open the water supply valves to the hot water heater and to the cold water line (both are
yellow-handled valves). Turn both valves counterclockwise to open and clockwise to shut.
2. With reference to Figure 1, fully open the Hoke 3-way valve on the hot water stream (blue
handle) so that the hot water will flow through the double-pipe heat exchanger. The valve
handle of V1 should point up. CAUTION: The system should never be operated with the hot
water flowing through the pneumatic control valve.
3. Open the Hoke 3-way valve on the cold water stream (blue handle) so that the cold water will
flow toward the control valve. The valve handle of V3 should be pointing down.
4. Turn on the air valve by moving the yellow handle counterclockwise.
5. Wait until the water temperature in the hot water heater rises to a steady-state value (which
should be around 140-150°F).
6. Set the flow rate of the hot water stream to a value of 55 (note: the experiment preview video
says 75, but the flow rate setting has changed since filming) on the scale of Rotameter 1 by
adjusting the rightmost black Whitey needle valve (when one is facing the control panel and
the apparatus).

7

Controller Operated in Manual Mode
1. The CN8DPT-305 controller can be operated as a direct- or reverse-acting controller.
Because the system under study is cooling the hot water stream by adding a varying amount
of cold water to achieve a moderate mixed-stream temperature, the controller must be
operated as a direct-acting controller. Consequently, negative controller output values are
used to open the pneumatic control valve on the cold water line.
2. The Platinum software package is used during the manual trials to monitor the mixed stream
temperature. The “Manual Control” feature in the software cannot be used to operate the
controller during the manual trials because this feature in the software attempts to reach a
setpoint temperature and does not allow the control valve to remain at a steady open position.
To open the Platinum Software:
a. Turn on the desktop computer and log in with the following credentials:
Username: cbe.hgolpou.shared
Password: CHE331Temp.Cont.!
b. Create a folder on the desktop to save your data files (e.g. Temp Control Data 5 Aug
2022).
c. Open the Platinum program located on the desktop by double-clicking it.
d. The Communication Setup dialog box shown in Figure 3 should appear.

Figure 3. The Communication Setup dialog box will appear when the Platinum Series
Software is launched.
e. Select USB for Connection Type, and Modbus_RTU for Communication Protocol. If the
Comm Port is not listed as COM4, you may have to check the “Auto Discover” box and
then click the green refresh button to the right of the “Port” dialog box to find it. Choose
COM 4 on the COM Port Selection and click the “Connect” button. The Platinum
Monitor dialog box, shown in Figure 4, should open. This window allows you to
interface with the controller using the computer, and displays the process variable – the
mixed stream temperature in degrees Fahrenheit.

8

Mixed Stream
Temperature in
degrees
Farenheit.

Figure 4. The Platinum Monitor dialog box allows user to interface with the controller
using input specifications and displays the process variable – the temperature of the mixed
stream.
3. Each manual control trial will run for approximately 1-2 minutes (60-120 seconds), until a
steady-state mixed stream temperature is achieved. Record the steady-state flow rates of the
hot and cold steams immediately after opening the control valve and again at the end of each
run. Be sure to also record the uncertainty associated with each measurement. In the last 20
seconds of each run, monitor the temperature of the mixed stream to see if it has attained a
steady value. You should adjust length of each trial as needed to reach a steady-state, mixedstream temperature. The mixed-stream temperature must be read from the Platinum Monitor
Window (shown in Figure 4) during the manual trials as the controller will be displaying the
controller output value. Be sure to record the flow rates and temperatures of both streams
at the end of a run after steady state is reached as the data will be needed later to check
against the results of a steady-state energy balance analysis (see Appendix B).
4. Using the keypad on the front of the controller, press the “↑” key until OPER is displayed.
Then press “◄┘” to select. Use the left and right arrow keys (◄►) to scroll until MANL is
displayed. Then press“◄┘” to select. Again use the left and right arrow keys (◄►) until
M.CNT is displayed. Press “◄┘” to select. Now you can vary the controller output using the
left and right arrow keys (◄►) to manually open the pneumatic control valve on the cold
water line. Wait until the Platinum Monitor window displays a temperature of about 135°F
for the effluent from the mixing unit before initiating each run.

9

5. Press the left arrow key (◄) on the keypad to increase the signal on the control valve to a
-12.0 output value and simultaneously start a stop watch. Notice that as soon as the controller
output is decreased below zero, the valve stem of the control valve rises with a corresponding
increase in the pressure output from the Foxboro I-to-P transducer, and, at the same time,
there is a concomitant decrease in the temperature of the mixed flow. The hot flow rotameter
(Rotameter 1) may also register a step drop in the flow rate of the hot stream. The opening of
the control valve on the cold water line evidently lowers the pressure of the hot water line
and this in turn lowers the flow rate of the hot stream. For convenience and expedience, the
same initial hot flow rate should be used for the same series of parametric runs. However, for
energy balance analysis (see later), the actual steady-state flow rates of the hot stream after
opening the control valve should be used.
6. At the end of the run, press the right arrow button (►) on the keypad to return the setting for
the controller output to zero. Wait for the effluent of the mixing unit to return to a
temperature of 135°F, and then repeat Step 5 with the controller output set at values of -14, 16, -18, & -20.
7. Plot the temperatures of the mixed stream at the ends of the 60 second runs as a function of
the controller output in Excel. Draw a smooth curve through the data points and use the
curve to project the controller output value that will give the desired set-point temperature
for the mixed stream.
8. Repeat Step 5 with the projected controller output value from Step 7 to verify that the desired
set-point temperature can be achieved experimentally. Note: You should perform a final
manual control run with the objective of reaching the desired set point based on the results
of the previous manual control runs.
Computer Settings for the Controller Operated in Automatic Mode (Steps 1-5 should have been
completed during the Manual trials)
1. Turn on the desktop computer and log in with the following credentials:
Username: cbe.hgolpou.shared
Password: CHE331Temp.Cont.!
2. Create a folder on the desktop to save your data files (e.g. Temp Control data 5 Aug 2022).
3. Open the Platinum program located on the desktop by double-clicking it.
4. The Communication Setup dialog page shown in Figure 3 should appear.
5. Select USB for Connection Type, and Modbus_RTU for Communication Protocol. If the
Comm Port is not listed as COM4, you may have to check the “Auto Discover” box and then
click the green refresh button to the right of the “Port” dialog box to find it. Choose COM 4
on the COM Port Selection and click the “Connect” button. The Platinum Monitor dialog
box, shown in Figure 5, should open. This window allows you to interface with the controller

10

using the computer, and displays the process variable – the mixed stream temperature in
degrees Fahrenheit.

#1

Figure 5. The Platinum Monitor dialog box allows user to interface with the controller
using input specifications, and displays the process variable (mixed stream temperature).
The blue “Setpoints,” and “Outputs” buttons are used to setup the automatic control trials.
The blue “PID Control” button is used to vary P, I & D values during individual automatic
control trials. The gray “Run” and “Idle” buttons are used to start and stop data logging
during automatic control trials.
6. Click the blue “Outputs” button (circled in blue in Figure 5) to open the Outputs dialog box
which is shown in Figure 6. For the controller to run properly, Output 3 must be in PID mode
and the Output Action should be “Direct.” All other outputs should remain in the “OFF”
position. Close the Outputs dialog box.
7. Return to the Platinum Monitor dialog box. Click the blue “Setpoints” button (circled in blue
in Figure 5) to open the Setpoints dialog box shown in Figure 7. Specify the Setpoint 1
temperature as “105.0” and select “Absolute”. Note: Setpoint 2 is not used and should be left
unchanged. Close the Setpoints dialog box.

11

Figure 6. Screen shot of how the outputs should be specified for the automatic control
portion of the experiment.
8. Return to the Platinum Monitor dialog box. Click the blue “PID Control” button (circled in
blue in Figure 5) to open the PID_Control Dialog box shown in Figure 8. (You may want to
arrange the “Platinum Monitor” and “PID_Control” dialog boxes so both are visible as
you will be using both of these windows throughout the experiment.) Under PID 1, leave
the “Bounds” values unchanged at the values shown in Figure 8. Under “Action,” make sure
the “Direct” option is selected. Leave “Adaptive Control Enable” unchecked. The “Tuning”
section of the PID_Control dialog box is where you will vary the values for proportional
gain, integral gain and derivative gain. Note: In this software, Proportional Gain (KP) is
referred to as “P”, Integral Gain (KI) is referred to as “I”, and Derivative Gain (KD) is
referred to as “D”.

Figure 7. Screen shot the Setpoints Dialog Box setup.
9. Specify the values for P, I and D, making sure to hit the “enter” key on the keyboard after
each value is entered. For the initial automatic control trial, set P = 1.0, I = 0 and D = 0 as
shown in Figure 8. Click the “Update” button (it will appear to the left of the “Refresh”

12

button only after changes are made to P, I and D values) to send the PID values to the
controller.
10. Verify that the control apparatus is properly set and is ready to proceed with the run. Check,
in particular, that (i) the temperature and flow rate of the hot stream remain steady, (ii) the
valve opening of the air-actuated control valve on the cold stream has been manually re-set to
zero after a previous run (the cold flow should always start at a zero flow rate in any run),
(iii) the air valve is turned on again if it has been turned off after a previous run (to bring the
cold flow rate down to zero in preparation for the next run), and (iv) the temperature of the
effluent stream leaving the mixing pot (which differs from that of the hot stream due to heat
loss) starts at approximately the same value (in the 135-145oF range) for all runs. Record the
flow rate of the hot stream off Rotameter 1 and the temperatures of the hot and cold
streams off the temperature display on the control panel. (The thermocouples for the hot
and cold streams—labeled 1 and 2, respectively—can be accessed by a dial switch on the
temperature display panel and the temperature mixed stream can be read off the main display
on the control panel or from the Platinum Monitor Window on the computer). Record the
uncertainty associated with each of the measurements as well.

Figure 8. PID Control Dialog Box used to vary the values for proportional, integral and
derivative gain.
11. To initiate the first automatic control run, return to the “Platinum Monitor” dialog box and
click on the green “Graphing” button to initiate the data logging feature of the software. The
“Data Charting” window will open in a separate dialog box as shown in Figure 9a. The
process variable (mixed-stream temperature) and setpoint will automatically be plotted in the
top figure of the “Data Charting” window, and the PID response will be plotted in the bottom
13

figure. You may uncheck the PID 1 and PID 2 boxes to enlarge the temperature plot if
desired (the data will still be logged) as shown in Figure 9b. Once you are ready to start
the trial, click the “clear” button in the graphing window and then immediately hit the
gray “Run” button located in the “Platinum Monitor” dialog box (circled in red in
Figure 5). Simultaneously start a stop watch/timer for 3 minutes. Once the “Run” button

(a)

(b)

Figure 9. The graphing window during a run. (a) Shows the graphing window default
settings. (b) Shows the graphing window with only temperature plotted (PID 1 and PID 2
have been unselected).
14

is clicked, the controller immediately attempts to reach the setpoint by continuously adjusting
the opening of the pneumatic valve on the cold water stream. Figure 10 depicts an example
of how temperature versus time is shown in the “Data Charting” window during an automatic
control run.

Figure 10. Example of how the Data Charting Window appears during an automatic
control trial with temperature of the mixed stream (Process Value) plotted as a function of
time.
12. About 15-30 seconds before the end of each automatic trial, be sure to manually record the
temperatures and flowrates of both the hot and cold streams, along with their respective
measurement uncertainties. You will need this information for the steady state energy
balance calculations (Appendix B). Note: The COMPUTER SOFTWARE DOES NOT
RECORD flowrates or temperatures of the hot and cold water streams – it only records the
temperature of the mixed water stream.
13. At the end of 3 minutes (180 seconds), click the “Save” button in the “Graphing” window.
Name the file (it is recommended that the file name includes the values of P, I & D used in
that particular trial) and save it to the folder you created on the desktop in Step 2. At the
prompt, click “OK” to confirm that data was saved. Then click the “Idle” button (circled in
red in Figure 5) in the “Platinum Monitor” Window to close the control valve on the cold
water stream. Note: the controller face reads “OPER” (rather than the mixed stream
temperature) when in IDLE mode.

15

14. Before starting the next automatic control run, allow the effluent temperature to return to
>135℉. In the PID Control window, input the next set of P, I and D values to be tested. Be
sure to click the “update” button to send the new values to the controller. Once the effluent
temperature is >135℉, start the next run by clicking the “clear” button in the “Graphing”
window and then immediately clicking the “Run” button in the “Platinum Monitor” window
while simultaneously starting a stopwatch/timer for 3 minutes. Note: Be sure to manually
record the temperatures and flowrates of both the hot and cold streams at the beginning
and end of each automatic control run.
Occasionally the Platinum graphing software will lock up with a “Chart contains no
elements” error message. If this happens during the experiment, use Task Manager to force
close the Platinum Software, and restart the Platinum software. It should reload with the last
set of saved values.
15. Perform a series of runs looking at the effect of varying the proportional Gain (P) on the
performance of proportional-only control. In the PID_Control Window, set Integral Gain (I)
and Derivative Gain (D) both to zero, and systematically vary P to take on the following
values: 0.4, 0.6, 0.8, and 1.0. In each of the P runs, be sure to start the run with a zero flow
rate for the cold stream (Rotameter 2 at 0) and as close to the same initial effluent
temperature (~135°F) as possible. Plot and compare the temperature response curves of the
various runs on a single plot in Excel (an example plot is shown in Figure 11), and choose
one proportional gain value with the “best” combination of the following desired attributes:
fast response, small offset, good stability/minimal oscillations, quick settling, low sensitivity
to disturbances. This value of P will be chosen as the “optimal” value and used in the
subsequent PI and PID automatic trials.

16

Figure 11. An example of how to plot all proportional control trials in a single figure in
Excel for comparison.
16. Use the “optimal” P setting determined in Step 15 to perform a second series of runs to
determine the effect of varying Integral Gain KI (I) on the performance of PI control. In the
PID_Control window, set Proportional Gain (P) to the optimal value determined in Step 15,
set Derivative Gain KD (D) to zero, and systematically vary KI to take on the following
values: 0.05, 0.1, 0.25, and 0.5. Compare the temperature response curves of the various PI
runs and find one with the “optimal” combination of the following desired attributes: fast
response, minimal error, good stability/minimal oscillations, quick settling, and low
sensitivity to disturbances.
17. Use the “optimal” P and I settings determined in Steps 15 & 16 to perform a third series of
runs to determine the effect of varying the Derivative Gain KD (D) on the performance of
proportional-integral-derivative control (PID). Systematically vary D to take on the
following values: 5, 10, 25, and 50. Again, compare the temperature response curves of
the various PID runs and find one with the “optimal” combination of the attributes
mentioned in Steps 15 & 16.
18. Perform a final set of experimental trials attempting to fine-tune KP (P), KI (I), and KD (D)
settings to achieve the setpoint temperature at the end of the 3 minute trial with minimal
oscillations. A minimum of four fine-tuning trials should be completed unless the setpoint
temperature is achieved with minimal oscillation. Use the knowledge obtained from
experimental observations in previous trials to inform your choices of KP, KI and KD settings.
19. Copy the data files from the desktop folder to a memory stick or personal Google Drive
folder.
Shutdown of the Apparatus Upon Completion of Experiment
1. Turn off the water heater.
2. Turn off the power strip.
3. Close the black Whitney needle valve on the hot water stream so that Rotameter 1 reads zero
flow.
4. Close the water supply valves to the heater and to the cold water line (both are yellowhandled valves). Turn both valves clockwise to shut.
5. Close the air valve by moving the yellow handle clockwise.
6. Exit the Platinum program.
7. Log off the computer.
DATA ANALYSIS
17

1. Determine if each trial (ALL manual and automatic trials should be analyzed) satisfied the
steady-state energy balance described in Appendix A by calculating the % discrepancy
between the theoretical temperature expectation (Tmix, theory) and the experimental temperature
measurement (Tmix, experimental). Assume the specific heat and density of water to be 1.0
Btu/(lbm.oF) or 1.0 kcal/(kg.oC) and 8.34 lbm/gal or 1.0 g/mL, respectively. Highlight trials
that had very low percent discrepancies and those with high discrepancies and explain why
discrepancies were observed. (As a general rule of thumb, if the % discrepancy between
theory and experiment is 5% or less, the results are considered to be in good agreement.)
2. Describe the results of the manual control run and comment on its effectiveness.
3. Present plots of all automatic control trials and describe the results. Present the plots in
logical groupings to establish clear-cut parametric trends. Discuss the contribution of each
control mode, i.e., explain how proportional, integral, and derivative control types each affect
the control of the system.
4. Present results of fine-tuning trials. Describe why you chose specific values KP, KI and KD
settings in each trial.
5. Present a frequency distribution histogram, as shown in Figure 12, for the fine-tuning trials or
other trials that need additional evidence to determine which settings were superior. A
frequency distribution diagram presents the number of readings that were taken at a
particular temperature. Use this plot to justify your choice of the optimal run. The “countif”
command and the bar chart feature in Excel are useful for making this plot.
200
180

Number of readings

160
140
120
100

Opt 1

80

Opt 2

60

Opt 3

40
20
0
<40

40-42

42-44

44-46

46-48

48-50

>50

Temperature Range (°F)

Figure 12. Example of a frequency distribution chart for temperature.

6. Use the Matlab Simulink program that is provided (PID_TControl.mdl) and described in
Appendix B to perform a series of simulation runs to establish the trends that would be

18

expected for varying the parameter settings of the PID controller. Summarize the theoretical
trends and compare to experimental results. Summarize reasons for differences.
SAFETY
Wear safety glasses at all times. Avoid contact with the piping system as the hot surfaces may
burn your skin. Avoid touching the metal controller box as it has been known to produce minor
electrical shocks. To avoid a serious electrical shock, never operate the controller equipment
with wet hands.
REFERENCES
1. Riggs J.B., Korchinski W.J., Kayihar A. Edited by Albright L.F. “Albright's Chemical
Engineering Handbook” CRC Press, Chapter 15, pp. 1208. 2008.
2. Cagley L., El-Zaatari B., Hensley J., Santos A., Yik T., “Temperature Control Lab” CHE330,
North Carolina State University, April 2012.
3. Luyben, Michael L. “Essentials of Process Control,” McGraw-Hill, New York (1997).
4. Prett, David M. “Fundamental Process Control,” Butterworths, Boston (1988).
5. Riggs, James B. “Chemical Process Control,” Ferret Publishing, Lubbock, Texas (1999).
6. Seborg, Edgar, and D. A. Mellichamp. “Process Dynamics and Control,” John Wiley and
Sons, New York (1989).
7. Stephanopoulos, George “Chemical Process Control: An Introduction to Theory and
Practice,” Prentice-Hall, Englewood Cliffs, New Jersey (1984).

19

Appendix A: Steady State Energy Balance
Steady State Energy Balance
First, an equation for the steady state energy balance is derived. Assuming negligible
temperature loss and the only energy transfer occurs between the two streams, the change in
enthalpy of the cold and hot streams (i.e. ΔHC and ΔHH, respectively) can be equated:
Δ𝐻𝐶 = −Δ𝐻𝐻

(1)

Next, assuming negligible flow work, Eq. 1 reduces to:
𝐶𝑝 Δ𝑇𝐶 𝑚̇𝐶 = −𝐶𝑃 Δ𝑇𝐻 𝑚̇𝐻

(2)

where 𝑚̇ is the mass flow rate, Cp is the heat capacity of the streams, ΔT is the change in
temperature from the inlet to the mixture temperature, and the substrips C and H designate the
cold and hot streams respectively) Both sides of Eq. 2 can be divided by Cp since the heat
capacities of the streams are approximately equal and expanding ΔT for both streams:
(𝑇𝑚 − 𝑇𝐶 )𝑚̇𝐶 = −(𝑇𝑚 − 𝑇𝐻 )𝑚̇𝐻

(3)

where Tm is the temperature of the mixed streams. Solving for T m:
𝑇 𝑚̇ +𝑇 𝑚̇

𝑇𝑚 = 𝐻𝑚̇ 𝐻+𝑚̇𝐶 𝐶
𝐶

20

𝐻

(4)

Appendix B: Use of Matlab Simulink to Model the PID Control of an Adiabatic Mixing
Process
Development of the Matlab Simulink Program
The Matlab Simulink program that is designed to model the temperature response of the PIDcontrolled mixing tank is named PID_TControl. The necessary files can be found on the CHE
330 Moodle site.
Conceptually, the file is made up of four parts: (1) a process unit that specifies the mixing
process as governed by material balance and energy balance (Eqn 4), (2) a PID controller unit
that operates according to Eqn 5, (3) a temperature comparison unit that provides feedback to the
PID controller unit, and (4) three display units (known as scopes) that plot the following three
variables as a function of run time: T(t), FC(t), and E(t) = T(t) – TS. Consult the Matlab Help
section for a tutorial on how to construct a Simulink program.
Running the Matlab Simulink Program and Evaluating the Simulation Results
The Simulink program requires the installation of the Matlab software to run on a PC. Matlab is
available on the on EOS PCs at NCSU as well as through NCSU’s Virtual Computing
Laboratory (VCL). It is also available to download at the NCSU EOS website.
Note: these instructions are written for the MATLAB 2023 version of the software available on
NCSU’s VCL – if you encounter issues using a different version of MATLAB, try accessing this
version of MATLAB through VCL.
To run the Simulink program, open MATLAB and click the “New” button, then “Function”.
Delete all text in the “Editor” window. Cut-and-paste the code included in the PID_TControl.mdl

Figure A1. Simulink window for simulation.
21

file on Moodle (click on the “MATLAB Code for Temperature Control Simulator” link to access
the code) into MATLAB’s “Editor” window. Click on “Save”, then “Save As”. In the Save As
window that pops up, click on the “Save as type” drop-down menu and select “All files”. Then,
input your desired file name with a .mdl extension (e.g. a suitable file name would be
Untitled.mdl). You should see your file name (with the .mdl extension) in the “Current Folder”
window in MATLAB. Double-click on this file name in the Current Folder window.
The block diagram shown in Figure A1, which will function as a control panel, should appear on
screen. The process unit, PID controller unit, temperature comparison feedback unit, and scopes
are color-coded, respectively, in green, magenta, orange and cyan. The setpoint temperature may
be changed from 40.0oC (remember to change it to the correct set point keeping in mind unit
conversions) to match the experimental conditions by double-clicking the TS block and erasing
the current value and entering the new value. Likewise, the values for TC, TH, FH, and V may be
changed by double clicking the Process block and modifying the entries to match the
experimental conditions; the parameter settings for KP, KI and KD may be varied by doubleclicking the PID block.
To run the simulation:
1. Click the “Run” button (the green, round, right-pointing arrow icon) found in the
“SIMULATE” panel above the process flow diagram shown in Figure A1.
2. The results of the simulation can be viewed graphically by double clicking the “Scope
for…” block with the variable you want to see. For example, double-clicking the “Scope
for T” (temperature) and “Scope for FC” (flowrate) blocks in the process flow diagram
would bring up the plots shown in Figures A2 and A3 respectively (which correspond to
KP = 12, KI = 10 and KD= 50).

Figure A2. Temperature trend as a function of time from simulation.
22

Figure A3. Cold water flowrate trend as a function of time from simulation.
To save the results of a simulation:
1. Prior to starting a simulation run, click the “Signal Table” icon found within the
“PREPARE” subwindow shown in Figure A1. Then check the box for “Log Data” in the
“Process” line.
2. Return to the process flow diagram and run the simulation with the desired parameters.
3. Click the “Data Inspector” button within “REVIEW RESULTS” subwindow shown in
Figure A1. When the “Simulation Data Inspector” window opens, make sure that the box
to the left of “T” is checked for the current run. Then click the “Export” button (the
button with the arrow going from left to right).
4. When the Export window opens, export the data as an Excel file as shown in Figure A3.
You can name your file as desired to keep track of the parameters varied in each
simulation. After saving your data, return to the process flow diagram (Figure A1) and
run the next simulation.

23

A3. Export window depicting how to save Matlab simulation data as an Excel data file.
Use the PID_TControl simulation program to study the parametric trends of varying the process
specifications or the PID parameters. Compare the simulation trends with the experimental
trends that you observed or will observe in the lab. For the simulation, use the values defined in
Table A1 for KP, KI and KD. (Note: You may find little difference between PID controlled
simulations with varying values of KD). Figure A4 gives an example output plot from MATLAB
for simulation of PID control.
Table A1. Parameter values to use for MATLAB temperature control simulation.
Trial
1
2
3
4
5
6
7
8
9

KP
0.1
1
10
Optimal KP for P simulations
Optimal KP for P simulations
Optimal KP for P simulations
Optimal KP for P simulations
Optimal KP for P simulations
Optimal KP for P simulations

24

KI
0
0
0
0.01
1
10
Optimal KI for PI simulations
Optimal KI for PI simulations
Optimal KI for PI simulations

KD
0
0
0
0
0
0
1
10
30

70

60

Temperature (°C)

50

40

30
Kd 1

20

Kd 10
10
Kd 30
0
0

50

100

150

200

250

300

350

Time (s)

Figure A4. PID simulation results with a KP value of 1, a KI value of 1 and various values of
KD .

25



## Metadata
- Source file: junk_drawer/CHE 331 - Temperature Control Experiment Handout (10-11-2023).pdf
- Extracted: 2026-05-18
- Category: academic-lab
