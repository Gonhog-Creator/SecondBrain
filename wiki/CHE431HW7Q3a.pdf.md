# CHE431HW7Q3a.pdf

Source: junk_drawer/CHE431HW7Q3a.pdf

Category: [[academic-homework]]

## Summary
% Problem 3a - Bode Plot s = tf('s'); % Define each block Kc = 1; % Set to 1 initially; adjust as needed for part (b) Gc = Kc * (2*s + 1)/(0.1*s + 1); Gp = 0.4/(s*(5*s + 1)); Gv = 2/(0.2*s + 1); Gm = 1; % Open-loop transfer function Gol = Gc * Gp * Gv * Gm;

## Full Content
% Problem 3a - Bode Plot
s = tf('s');
% Define each block
Kc = 1; % Set to 1 initially; adjust as needed for part (b)
Gc = Kc * (2*s + 1)/(0.1*s + 1);
Gp = 0.4/(s*(5*s + 1));
Gv = 2/(0.2*s + 1);
Gm = 1;
% Open-loop transfer function
Gol = Gc * Gp * Gv * Gm;
% Bode plot
figure;
margin(Gol); % shows Bode plot with gain and phase margins
title('Open-loop Bode Plot for Problem 3a');

Published with MATLAB® R2024b

1



## Metadata
- Source file: junk_drawer/CHE431HW7Q3a.pdf
- Extracted: 2026-05-18
- Category: academic-homework
