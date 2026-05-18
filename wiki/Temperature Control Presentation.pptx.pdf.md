# Temperature Control Presentation.pptx.pdf

Source: junk_drawer/Temperature Control Presentation.pptx.pdf

Category: [[academic-lab]]

## Summary
Evaluation of Control Methods for a Temperature Control Apparatus Presenters: Jose Maria Barbeito Raghu Mereddy Linda Pomiranceva Q&A: Aaron Dornseif Robert Hart Elisa Schlesner Alves

## Full Content
Evaluation of Control Methods for a
Temperature Control Apparatus
Presenters:
Jose Maria Barbeito
Raghu Mereddy
Linda Pomiranceva
Q&A:
Aaron Dornseif
Robert Hart
Elisa Schlesner Alves
Department of Chemical and Biomolecular
Engineering
North Carolina State University

October 11th, 2024

1

This presentation focuses on
Manual
Control

FineTuning

Automatic
Control

Analysis of
controller
parameters
2

The experimental apparatus is made of multiple control valves, temperature
thermocouples, and a mixing chamber.

3

Percent discrepancy between Tmix, theory and Tmix, experimental showed that
manual trials were more precise

Method

Tmix, theory (avg)

Tmix, experimental (avg)

% Difference
(avg)

Manual

108.93 ± 5.84

107.76

1.20%

Automatic

113.18 ± 6.70

108.75

4.91%

4

Low difference between the Tmix, calculated and Tmix, theoretical showed that
manual control is a viable control method

5

It is important to determine how each
parameter influences the final mixing
temperature, before the system can be
optimized

6

Adjusting KP changes final temperature at low values but introduces
oscillatory patterns at higher values

Optimal KP : 0.8

7

Adjusting KI corrects KP offset to target temperature, but causes overshoots
and overcorrects at higher values

Optimal KI :
0.055

8

Adjusting KD increases time to target temperature at low values and
introduces wave-like function at high values

Optimal KD : 0

9

By fine-tuning, we determined that the optimal settings to decrease the
final mixing temperature to 105°C were P: 0.8, I: 0.055, and D: 0

10

Looking at the frequency of each run at varying temperatures, we reinforced that
Run 2, where P:0.8, I:0.055, D:0.0, is the better setting for achieving 105°C.

11

Through a MATLAB simulation we determined that larger Kp values reduce
offset from the starting point

Optimal KP : 10

12

The MATLAB simulation showed that lower KI values reduce oscillations
around the setpoint.

Optimal KI : 1

13

The MATLAB simulation showed that smaller KD values create a smoother
approach to the setpoint.

Optimal KD : 0

14

The MATLAB simulation showed that smaller KD values create a smoother
approach to the setpoint.

Optimal KD : 0

15

Conclusion:
Automatic control can give superior control over the process when utilized
properly. When poorly utilized, manual control can give better results.
Method

Tmix, theory

Tmix,

(avg)

experimental

%
Difference
(avg)

(avg)

Manual

108.93 ± 5.84

107.76

1.20%

Automatic

113.18 ± 6.70

108.75

4.91%

Questions?

16

References
[1] M. Cooper, P. Lim, K. Dickey, and K. Dickey, “Temperature Control Experiment” CHE 331 Course Handout, North Carolina
State University, Raleigh, NC.
[2] O’BRIEN, TERRY. n.d. “Which Is Better: Automatic or Manual Internal Controls? | Schellman.” Schellman Compliance.
https://www.schellman.com/blog/soc-examinations/automated-or-manual-soc-controls.
[3] “Feedback Control System - an Overview | ScienceDirect Topics.” n.d. Www.sciencedirect.com.
https://www.sciencedirect.com/topics/engineering/feedback-control-system.



## Metadata
- Source file: junk_drawer/Temperature Control Presentation.pptx.pdf
- Extracted: 2026-05-18
- Category: academic-lab
