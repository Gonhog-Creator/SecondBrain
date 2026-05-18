# Homework Set 1 (Solutions)  (1).pdf

Source: junk_drawer/Homework Set 1 (Solutions)  (1).pdf

Category: [[academic-homework]]

## Summary
CHE 435/525 – Process Systems Analysis and Control Spring 2025 Homework Set 1. Math Prerequisites, Dynamic Modeling, and Simulation (Solutions) Question 1 (a) z = −1+√3 i

## Full Content
CHE 435/525 – Process Systems Analysis and Control

Spring 2025

Homework Set 1. Math Prerequisites, Dynamic Modeling, and Simulation (Solutions)

Question 1
(a)
z = −1+√3 i

Im
z

√3

-1

Re

(b)
z = −1+√3 i
•

Modulus:
|z| = √1 + 3 = 2

•

Argument

For x < 0, and y ≥ 0,the argument of a complex number z = x+iy can be calculated by:
y

∡z = tan−1 (x) + Π .
2Π

Hence, ∡z = tan−1 (−√3) + Π = 3 𝑟𝑎𝑑𝑖𝑎𝑛𝑠
(c)
Let :
z = eiθ = cos θ + i sin θ.
From part b,
|z| = √𝑐𝑜𝑠 2 θ +𝑠𝑖𝑛2 θ = 1.

(d)
z=reiθ (r > 0 and θ are both real)
Im
z
r
θ
Re

Question 2
(a)
𝑥(𝑡 = 3) ≈ 8.1213

(b)

MATLAB Code
% Part (a)
% beginning and end t-values
t_range = [0,5];
% initial condition
x0 = 0;
% solve ODE with ode45
[t_sol,x_sol] = ode45(@my_ode1, t_range, x0);
% find x(3)
x_3 = interp1(t_sol, x_sol, 3);
% plot solution
plot(t_sol, x_sol, '-', 3, x_3, 'o');
xlabel('t');
ylabel('x');
% define ODE function
function dxdt = my_ode1(t, x)
dxdt = sqrt(t^2 + x^2);
end
% ---------------% Part (b)
% beginning and end t-values
t_range = [0,60];
% initial condition
IC = [1; 1; 1];
% solve ODE with ode45
[t_sol,Vec_sol] = ode45(@my_ode2, t_range, [1; 1; 1]);
[x_sol, y_sol, z_sol] = deal(Vec_sol(:,1), Vec_sol(:,2), Vec_sol(:,3));
% plot solution

plot3(x_sol, y_sol, z_sol, '-');
grid("on");
xlabel('x');
ylabel('y');
zlabel('z');
% define ODE function
function dVecdt = my_ode2(t, variables)
[x, y, z] = deal(variables(1), variables(2), variables(3));
[s, r, b] = deal(10, 28, 8/3);
dxdt = s*(y-x);
dydt = x*(r-z) - y;
dzdt = x*y - b*z;
dVecdt = [dxdt; dydt; dzdt];
end

Question 3
(a) Feedback Control:
Measure variable: y
Manipulated variable: D, R, or B

(b) Feedforward Control:
Measured variable: F
Manipulated variable: D, R, or B

Question 4
(a)

(b)

Question 5
Assume the feed contains only A and B, and no C.
•

Component balances in the reactor:

𝑑𝑛𝐴
= 𝑞𝑖 𝑐𝐴𝑖 − 𝑞𝑐𝐴 − 𝑉𝑟1
𝑑𝑡
𝑑𝑛𝐵
= 𝑞𝑖 𝑐𝐵𝑖 − 𝑞𝑐𝐵 + 𝑉𝑟1 − 𝑉𝑟2
𝑑𝑡
𝑑𝑛𝐶
= −𝑞𝑐𝐶 + 𝑉𝑟2
𝑑𝑡
𝐸
𝑅𝑇

𝐸
𝑅𝑇

Plug in 𝑛𝐴 = 𝑉𝑐𝐴 , 𝑛𝐵 = 𝑉𝑐𝐵 , 𝑛𝐶 = 𝑉𝑐𝐶 , 𝑟1 = 𝑘1 exp (− 1 ) 𝑐𝐴 , 𝑟2 = 𝑘2 exp (− 2 ) 𝑐𝐵
𝑑𝑐

𝐸

𝑉 𝑑𝑡𝐴 = 𝑞𝑖 𝑐𝐴𝑖 − 𝑞𝑐𝐴 − 𝑉𝑘1 exp (− 𝑅𝑇1 ) 𝑐𝐴
𝑉

𝑑𝑐𝐵
𝐸
𝐸
= 𝑞𝑖 𝑐𝐵𝑖 − 𝑞𝑐𝐵 + 𝑉 [𝑘1 exp (− 1 ) 𝑐𝐴 − 𝑘2 exp (− 2 ) 𝑐𝐵 ]
𝑑𝑡
𝑅𝑇
𝑅𝑇
𝑑𝑐

𝐸

𝑉 𝑑𝑡𝐶 = −𝑞𝑐𝐶 + 𝑉𝑘2 exp (− 𝑅𝑇2 ) 𝑐𝐵

•

Mass balance in the jacket:
Since the volume in the jacket does not change, we can write:
𝑞𝑐𝑖 = 𝑞𝑐 .

•

Energy balance for the reactor:
Assuming the molar heat capacity for A, B, C are 𝐶𝑃,𝐴 , 𝐶𝑃,𝐵 , 𝐶𝑃,𝐶 , which do not change with
temperature.
The general energy balance equation:
𝑑𝐻
= 𝐻̇𝑖𝑛 − 𝐻̇𝑜𝑢𝑡 + 𝑄̇
𝑑𝑡

Also, knowing using the relation between enthalpy of material A, B, and C to remove 𝑐𝐶 𝐶𝑃,𝐶 on the righthand-side:
̂𝐵 = 𝐻
̂𝐴 + ∆𝐻1 = 𝐶𝑃,𝐴 𝑇 + ∆𝐻1
𝐻
̂𝐶 = 𝐻
̂𝐴 + ∆𝐻1 + ∆𝐻2 = 𝐶𝑃,𝐴 𝑇 + ∆𝐻1 + ∆𝐻2 = 𝐶𝑃,𝐵 𝑇 + ∆𝐻2
𝐻
The total energy in the reactor:
𝐻 = 𝑉[𝑐𝐴 𝐶𝑃 + 𝑐𝐵 (𝐶𝑃,𝐴 𝑇 + ∆𝐻1 ) + 𝑐𝐶 (𝐶𝑃,𝐴 𝑇 + ∆𝐻1 + ∆𝐻2 )]𝑇
𝐻̇𝑖𝑛 and 𝐻̇𝑜𝑢𝑡 are as follows:
𝐻̇𝑖𝑛 = 𝑞𝑖 (𝑐𝐴𝑖 𝐶𝑃,𝐴 + 𝑐𝐵𝑖 𝐶𝑃,𝐵 )𝑇𝑖
𝐻̇𝑜𝑢𝑡 = 𝑞[𝑐𝐴 𝐶𝑃,𝐴 𝑇 + 𝑐𝐵 (𝐶𝑃 𝑇 + ∆𝐻1 ) + 𝑐𝐶 (𝐶𝑃,𝐴 𝑇 + ∆𝐻1 + ∆𝐻2 )]
The 𝑄̇ = heat exchange with jacket:
𝑄̇ = −𝑈𝐴(𝑇 − 𝑇𝑐 )
Plug in these equations to get a general form of energy balance:
𝑑[𝑉(𝑐𝐴 𝐶𝑃,𝐴 +𝑐𝐵 𝐶𝑃,𝐵 +𝑐𝐶 𝐶𝑃,𝐶 )𝑇]
𝑑𝑡

=

𝑞𝑖 (𝑐𝐴𝑖 𝐶𝑃,𝐴 + 𝑐𝐵𝑖 𝐶𝑃,𝐵 )𝑇𝑖 − 𝑞(𝑐𝐴 𝐶𝑃,𝐴 + 𝑐𝐵 𝐶𝑃,𝐵 + 𝑐𝐶 𝐶𝑃,𝐶 )𝑇 − 𝑈𝐴(𝑇 − 𝑇𝑐 )
For further simplification, first expand the derivation on the left-hand-side, and then replace 𝑐𝐶 by
𝑐𝐶 = 𝑐𝐴𝑖 + 𝑐𝐵𝑖 − 𝑐𝐴 − 𝑐𝐵
After plugging in equations of species balances, the final simplified form is:
𝑑𝑇

𝑉(𝑐𝐴 𝐶𝑃,𝐴 + 𝑐𝐵 𝐶𝑃,𝐵 + 𝑐𝐶 𝐶𝑃,𝐶 ) 𝑑𝑡 = 𝑞𝑖 (𝑐𝐴𝑖 𝐶𝑃,𝐴 + 𝑐𝐵𝑖 𝐶𝑃,𝐵 )(𝑇𝑖 − 𝑇) − 𝑈𝐴(𝑇 − 𝑇𝑐 ) +
𝐸
𝑅𝑇

𝐸
𝑅𝑇

(−∆𝐻1 )𝑉𝑘1 exp (− 1 ) 𝑐𝐴 + (−∆𝐻2 )𝑉𝑘2 exp (− 2 ) 𝑐𝐵 .
𝑘𝐽

It is also appropriate to use the specific heat to replace the molar heat capacity by: 𝐶𝑃,𝐴 (𝑚𝑜𝑙∙𝐾) =
𝑘𝐽

𝑀𝐴 𝑆𝐴 (𝑘𝑔∙𝐾), where MA is the molecular weight for A. Similarly, this applies to B and C:
𝑑𝑇

𝑉(𝑐𝐴 𝑀𝐴 𝑆𝐴 + 𝑐𝐵 𝑀𝐵 𝑆𝐵 + 𝑐𝐶 𝑀𝐶 𝑆𝐶 ) 𝑑𝑡 = 𝑞𝑖 (𝑐𝐴𝑖 𝑀𝐴 𝑆𝐴 + 𝑐𝐵𝑖 𝑀𝐵 𝑆𝐵 )(𝑇𝑖 − 𝑇) − 𝑈𝐴(𝑇 − 𝑇𝑐 ) +
𝐸
𝑅𝑇

𝐸
𝑅𝑇

(−∆𝐻1 )𝑉𝑘1 exp (− 1 ) 𝑐𝐴 + (−∆𝐻2 )𝑉𝑘2 exp (− 2 ) 𝑐𝐵
•

Energy balance for the jacket:
𝑑𝑇

𝑉𝑗 𝑐𝑗 𝐶𝑃 𝑑𝑡𝑐 = 𝑞𝑐𝑖 𝑐𝑗 𝐶𝑃 (𝑇𝑐𝑖 − 𝑇𝑐 ) + 𝑈𝐴(𝑇 − 𝑇𝑐 ) or
𝑑𝑇

𝜌𝑗 𝑉𝑗 𝑆𝑗 𝑑𝑡𝑐 = 𝜌𝑗 𝑞𝑐𝑖 𝑆𝑗 (𝑇𝑐𝑖 − 𝑇𝑐 ) + 𝑈𝐴(𝑇 − 𝑇𝑐 )

Where
𝜌𝑗 is the density of the coolant.
𝑆𝑗 is the specific heat of the coolant.
𝑉 is the volume of the jacket.

Question 6

Category: Example Type:
Liquid
Manometer
Column

Elastic
Element

Bourdon Tube

Electrical
Sensing

Piezoelectric
Transducers

Mechanism:
A U-shaped tube where one end is open
to the atmosphere and the other is
influenced by the fluid being measured.
A column of liquid (e.g. water) is
measured by its height difference on
either side of the U-bend.
A thin tube bent in an arc and sealed at
one end, sees the fluid being measured.
The pressure of the fluid straightens the
tube which causes a rotation in a needle
to represent a pressure measurement.
Utilizes piezoelectric material where a
strain caused by a change in pressure
causes a change in electric charge that
can be measured as a change in voltage.
The voltage change can be related as
proportional to the pressure change.

Application:
Measures the gauge
pressure of a fluid in a
pipe or vessel.
Typically limited on
fluid compatibility with
the column liquid fluid.
Measures the gauge
pressure of a fluid in a
pipe or vessel. Comes
in various spans of
pressure measurement
ranges. Very common
instrument in industry.
Linear deformation
over a relatively large
span and immunity to
EMF allows
Piezoelectric
Transducers to be used
in harsh environments.
Capable in micro-scale
sensors as a microeletromechanical
system (MEMS).

Question 7

Discussion:
The plots above depict the reactor's nonlinear dynamic behavior, as the cooling jacket temperature is
changed. At lower temperatures, such as 290 K, the reactor maintains a relatively stable operation,
illustrating how effective heat removal helps sustain system equilibrium. However, at higher temperatures,
such as 305 K, significant oscillations and instability occur due to inadequate cooling, leading to
temperature spikes and corresponding fluctuations in reactant A concentration.

MATLAB Code
% Parameters
V = 100;
% Reactor volume in L
q = 100;
% Flow rate in L/min
rho = 1000;
% Density in g/L
C = 0.239;
% Specific heat capacity in J/g K
Ti = 350;
% Inlet temperature in K
cAi = 1;
% Inlet concentration in mol/L
UA = 5e4;
% Heat transfer coefficient in J/min K
k0 = 7.2e10;
% Pre-exponential factor in 1/min
EoverR = 8750;
% Activation energy divided by gas constant R in K
minus_deltaHr = 5e4; % Heat of reaction in J/mol
% Initial conditions
cA0 = 0.5;
% Initial concentration of A in mol/L
T0 = 350;
% Initial reactor temperature in K
init = [cA0, T0];
tspan = [0, 10];

% 10 minutes

% Simulate with cooling temperature ordered for plotting
Tc_values = [290, 300, 305]; % Cooling temperatures in K
colors = {'b', 'k', 'r'};
% Color for each cooling temperature
legend_entries = {'Tc = 290 K', 'Tc = 300 K', 'Tc = 305 K'};
% Temperature Plot
figure;
hold on;
title('Reactor Temperature Response');
xlabel('Time (minutes)');
ylabel('Temperature (K)');
% Concentration Plot
figure;
hold on;
title('Reactor Concentration of A');
xlabel('Time (minutes)');
ylabel('Concentration of A (mol/L)');
for i = 1:length(Tc_values)
Tc = Tc_values(i);
% Solve ODEs
[t, sol] = ode15s(@(t, y) reactorODEs(t, y, V, q, rho, C, Ti, cAi, UA, Tc,
k0, EoverR, minus_deltaHr), tspan, init);
% Extract solutions
cA = sol(:, 1);
T = sol(:, 2);
% Plot temperature
figure(1); % Select the temperature figure
plot(t, T, 'Color', colors{i},'LineWidth', 2);
% Plot concentration
figure(2); % Select the concentration figure

plot(t, cA, 'Color', colors{i}, 'LineWidth', 2);
end
% Finalize temperature plot
figure(1);
legend(legend_entries, 'Location', 'best');
grid on;
hold off;
% Finalize concentration plot
figure(2);
legend(legend_entries, 'Location', 'best');
grid on;
hold off;
function dydt = reactorODEs(t, y, V, q, rho, C, Ti, cAi, UA, Tc, k0, EoverR,
minus_deltaHr)
cA = y(1);
T = y(2);
k = k0 * exp(-EoverR / T); % Reaction rate constant in 1/min
% ODEs
dcAdt = q * (cAi - cA) / V - k * cA;
dTdt = (q * rho * C * (Ti - T) + minus_deltaHr * V * k * cA + UA * (Tc - T)) / (V
* rho * C);
dydt = [dcAdt; dTdt];
end



## Metadata
- Source file: junk_drawer/Homework Set 1 (Solutions)  (1).pdf
- Extracted: 2026-05-18
- Category: academic-homework
