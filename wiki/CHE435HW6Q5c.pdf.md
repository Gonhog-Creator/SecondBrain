# CHE435HW6Q5c.pdf

Source: junk_drawer/CHE435HW6Q5c.pdf

Category: [[academic-homework]]

## Summary
Table of Contents ......................................................................................................................................................... 1 % Problem 5: Feedforward–Feedback Loop Simulation clear; clc; s = tf('s'); % Parameters Kp = 2; tau_p = 95; theta_p = 20; Kd = 0.5;

## Full Content
Table of Contents
......................................................................................................................................................... 1
% Problem 5: Feedforward–Feedback Loop Simulation
clear; clc;
s = tf('s');
% Parameters
Kp = 2;
tau_p = 95;
theta_p = 20;
Kd = 0.5;
tau_d = 45;
theta_d = 20;
% Pade approximations for delays (1st order)
Gp = Kp * pade(exp(-theta_p*s), 1) / (tau_p*s + 1);
Gd = Kd * pade(exp(-theta_d*s), 1) / (tau_d*s + 1);
% (a) Feedforward controller (ideal cancellation, Gd/Gp)
Gff = -Kd * (tau_p*s + 1) / (Kp * (tau_d*s + 1));
% (b) Feedback controller design with tau_c = 30
tau_c = 30;
Kc = (tau_p / (Kp * (tau_c + theta_p)));
tauI = tau_p;
Gc = Kc * (1 + 1/(tauI*s)); % PI Controller
% (c) Feedback-only response to disturbance step
T_fb = feedback(Gd, Gc*Gp);
figure(1);
step(T_fb, 200);
title('Figure 1: Feedback-only Step Response to Disturbance');
xlabel('Time (s)');
ylabel('y(t)');
grid on;
% (d) Feedforward + Feedback response (correct Gd used)
numerator_ff = minreal(Gd + Gff*Gp);
T_ff_fb = feedback(numerator_ff, Gc*Gp);
figure(2);
step(T_ff_fb, 200);
title('Figure 2: Feedforward + Feedback Response (Correct Gd)');
xlabel('Time (s)');
ylabel('y(t)');
1

grid on;
% (e) Erroneous disturbance model used in feedforward design
Gd_wrong = 0.5 * pade(exp(-30*s), 1) / (60*s + 1);
Gff_wrong = -0.25 * (tau_p*s + 1) / (tau_d*s + 1); % Based on incorrect Gd
numerator_wrong = minreal(Gd + Gff_wrong*Gp); % Real (true Gd)
T_ff_fb_wrong = feedback(numerator_wrong, Gc*Gp);
figure(3);
step(T_ff_fb_wrong, 200);
title('Figure 3: Feedforward + Feedback with Erroneous G_d Model');
xlabel('Time (s)');
ylabel('y(t)');
grid on;

2

3

Published with MATLAB® R2024b

4



## Metadata
- Source file: junk_drawer/CHE435HW6Q5c.pdf
- Extracted: 2026-05-18
- Category: academic-homework
