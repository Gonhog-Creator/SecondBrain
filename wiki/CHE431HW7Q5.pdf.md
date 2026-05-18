# CHE431HW7Q5.pdf

Source: junk_drawer/CHE431HW7Q5.pdf

Category: [[academic-homework]]

## Summary
% Part (a) - Step Response with Nominal Delay (tau = 1) s = tf('s'); Gc = 0.5 / (s * (0.1*s + 1)); tau = 1; G = exp(-tau * s); % Delay as exponential % Closed-loop transfer function sys_cl = feedback(Gc * G, 1); % Step response figure; step(sys_cl, 10);

## Full Content
% Part (a) - Step Response with Nominal Delay (tau = 1)
s = tf('s');
Gc = 0.5 / (s * (0.1*s + 1));
tau = 1;
G = exp(-tau * s); % Delay as exponential
% Closed-loop transfer function
sys_cl = feedback(Gc * G, 1);
% Step response
figure;
step(sys_cl, 10);
title('Closed-Loop Step Response for \tau = 1');
grid on;
% Step info for checking overshoot
info = stepinfo(sys_cl);
fprintf('Overshoot: %.2f%%\n', info.Overshoot);
fprintf('Steady-State Error: %.4f\n', 1 - dcgain(sys_cl));
% Part (b) - Determine maximum stable delay by checking phase margin
taus = 0:0.1:5; % Sweep delays
PMs = zeros(size(taus)); % Store phase margins
for i = 1:length(taus)
G_delay = exp(-taus(i) * s);
L = Gc * G_delay;
[~, PM, ~, ~] = margin(L);
PMs(i) = PM;
end
% Plot phase margin vs delay
figure;
plot(taus, PMs, 'LineWidth', 2);
xlabel('Time Delay \tau (s)');
ylabel('Phase Margin (degrees)');
title('Phase Margin vs. Time Delay');
grid on;
% Find max stable delay (phase margin > 0)
stable_taus = taus(PMs > 0);
T_max = max(stable_taus);
fprintf('Maximum Stable Delay: %.2f seconds\n', T_max);
Overshoot: 7.59%
Steady-State Error: 0.0000
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
1

Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Warning: The closed-loop system is unstable.
Maximum Stable Delay: 3.00 seconds

2

Published with MATLAB® R2024b

3



## Metadata
- Source file: junk_drawer/CHE431HW7Q5.pdf
- Extracted: 2026-05-18
- Category: academic-homework
