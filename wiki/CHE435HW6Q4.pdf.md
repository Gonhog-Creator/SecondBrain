# CHE435HW6Q4.pdf

Source: junk_drawer/CHE435HW6Q4.pdf

Category: [[academic-homework]]

## Summary
Table of Contents ......................................................................................................................................................... 1 --- User-defined process parameters --- .................................................................................................... 1 --- Transfer function setup --- ................................................................................................................ 1 --- (a) Direct Synthesis Tuning --- 

## Full Content
Table of Contents
......................................................................................................................................................... 1
--- User-defined process parameters --- .................................................................................................... 1
--- Transfer function setup --- ................................................................................................................ 1
--- (a) Direct Synthesis Tuning --- .......................................................................................................... 1
--- (b) Cohen-Coon Tuning --- ............................................................................................................... 1
--- Closed-loop systems --- .................................................................................................................... 1
--- Plot Step Responses --- .................................................................................................................... 1
--- Display Controller Parameters --- ....................................................................................................... 2
% PI Controller Comparison: Direct Synthesis vs. Cohen-Coon
clc; clear; close all;

--- User-defined process parameters --K = 3;
tau = 2;
theta = 1;

% Process gain
% Process time constant
% Process dead time

--- Transfer function setup --s = tf('s');
Gp = K * exp(-theta * s) / (tau * s + 1);

% FOPTD model

--- (a) Direct Synthesis Tuning --Kc_DS = tau / (K * (theta + tau));
PI_DS = Kc_DS * (1 + 1 / (tau * s));

--- (b) Cohen-Coon Tuning --Kc_CC = (tau / (K * theta)) * (0.9 + theta / (12 * tau));
tauI_CC = ((30 + 3 * (theta / tau)) / (9 + 20 * (theta / tau))) * theta;
PI_CC = Kc_CC * (1 + 1 / (tauI_CC * s));

--- Closed-loop systems --CL_DS = feedback(PI_DS * Gp, 1);
CL_CC = feedback(PI_CC * Gp, 1);

--- Plot Step Responses --t = 0:0.01:30;
figure;
step(CL_DS, t); hold on;
1

step(CL_CC, t);
legend('Direct Synthesis', 'Cohen-Coon');
title('Step Response Comparison of PI Controllers');
xlabel('Time (s)');
ylabel('Output');
grid on;

--- Display Controller Parameters --fprintf('--- Controller Parameters ---\n');
fprintf('Direct Synthesis:
Kc = %.4f, TauI = %.4f\n', Kc_DS, tauI_DS);
fprintf('Cohen-Coon:
Kc = %.4f, TauI = %.4f\n', Kc_CC, tauI_CC);
--- Controller Parameters --Unrecognized function or variable 'tauI_DS'.
Error in CHE435HW6Q4 (line 39)
fprintf('Direct Synthesis:
Kc = %.4f, TauI = %.4f\n', Kc_DS, tauI_DS);
^^^^^^^
Published with MATLAB® R2024b

2



## Metadata
- Source file: junk_drawer/CHE435HW6Q4.pdf
- Extracted: 2026-05-18
- Category: academic-homework
