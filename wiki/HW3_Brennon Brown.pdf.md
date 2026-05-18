# HW3_Brennon Brown.pdf

Source: junk_drawer/HW3_Brennon Brown.pdf

Category: [[academic-homework]]

## Summary
CHE 435 - Process Systems Analysis and Control Spring 2025 – Dr. Tang Brennon Brown HW3 1. Recall the Cartesian representation of a complex number z = reiθ and the polar representation z = reiθ. You already know that to convert polar to Cartesian representation, x = rcos θ and y = rsin θ. a. When converting z = x + yi to z = reiθ, obviously we have r = √x2 + y2 . However, the simplistic formula “θ = arctan(y/x)” is applicable only if x > 0, since “arctan” is

## Full Content
CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
1. Recall the Cartesian representation of a complex number z = reiθ and the polar
representation z = reiθ. You already know that to convert polar to Cartesian representation,
x = rcos θ and y = rsin θ.

a. When converting z = x + yi to z = reiθ, obviously we have r = √x2 + y2 . However, the
simplistic formula “θ = arctan(y/x)” is applicable only if x > 0, since “arctan” is
valued in (–π/2, +π/2).

i.
ii. Analyze Each Case:
1. When x > 0 (Quadrants I and IV):
a. θ = arctan(y/x)
2. When x < 0 and y > 0 (Quadrant II):
a. θ = π + arctan(y/|x|)
3. When x < 0 and y ≤ 0 (Quadrant III):
a. θ = π + arctan(y/|x|)
4. When x = 0 and y > 0 (positive y-axis):
a. θ = π/2
5. When x = 0 and y < 0 (negative y-axis):
a. θ = -π/2
iii. Complete Formula θ:
1. arctan(y/x), for x > 0
2. π + arctan(y/|x|), for x < 0, y > 0
3. π + arctan(y/|x|), for x < 0, y ≤ 0

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
4. π/2, for x = 0, y > 0
5. -π/2, for x = 0, y < 0
b. Recall from the previous homework: |z1z2| = |z1|·|z2|, ∡(z1z2) = ∡z1 + ∡z2, and
whenever z2 is nonzero, |z1/z2| = |z1|/|z2|, ∡(z1/z2) = ∡z1 – ∡z2. In particular, |z2| =
|z|2, ∡(z2) = 2∡z, |1/z| = 1/|z|, ∡(1/z) = –∡z. Please ﬁnd the polar representations of
the following numbers (where a, b, c are positive real constants):

i.
ii. For z1 = 1/(1 + ai):
1. r1 = 1/sqrt(1 + a^2)
2. θ1 = -arctan(a)
3. Therefore, z1 = [1/sqrt(1 + a^2)] * e^(-i*arctan(a))
iii. For z2 = (1 - ai)/[(1 + bi)(1 + ci)^2]:
1. r2 = sqrt(1 + a^2)/[sqrt(1 + b^2)(1 + c^2)]
2. θ2 = -arctan(a) - arctan(b) - 2arctan(c)
3. Therefore, z2 = [sqrt(1 + a^2)/(sqrt(1 + b^2)(1 + c^2))] * e^(i*(arctan(a) + arctan(b) + 2arctan(c)))
iv. For z3 = (1 - bi)^3/(1 - a^2 + 2aci), where |a| < 1:
1. r3 = (1 + b^2)^(3/2)/sqrt((1 - a^2)^2 + 4a^2c^2)
2. θ3 = -3arctan(b) - arctan(2ac/(1 - a^2))
3. Therefore, z3 = [(1 + b^2)^(3/2)/sqrt((1 - a^2)^2 + 4a^2c^2)] * e^(i*(3arctan(b) + arctan(2ac/(1 - a^2))))
v. For z4 = [(1 - ai)(1 + bi)/(1 + ai)^2] * e^(-ci):
1. r4 = [sqrt(1 + a^2) * sqrt(1 + b^2)]/(1 + a^2)
2. θ4 = -3arctan(a) + arctan(b) - c
3. Therefore, z4 = [sqrt(1 + a^2) * sqrt(1 + b^2)/(1 + a^2)] * e^(i*(3arctan(a) - arctan(b) + c))

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
2. A heater for a semiconductor wafer has ﬁrst-order dynamics, that is, the transfer function
relating changes in temperature T to changes in the heater input power level P is where K
has units [°C/kW] and τ has units [min]. The process is at steady state when an engineer
changes the power input stepwise from 1 to 2 kW. She notes the following:
, The
process temperature initially is 100 °C. • 4 minutes after changing the power input, the
temperature is 400 °C. • 30 minutes later the temperature is 500 °C.
a. What are K and τ in the process transfer function?
i. Calculate Process Gain (K):
1. Initial temperature = 100°C
2. Final temperature = 500°C
3. Temperature change (ΔT) = 500°C - 100°C = 400°C
4. Power change (ΔP) = 2 kW - 1 kW = 1 kW
5. K = ΔT/ΔP = 400°C/1 kW = 400°C/kW
ii. Calculate Time Constant (τ):
1. Using T(t) = Tﬁnal - (Tﬁnal - Tinitial)e^(-t/τ)
2. At t = 4 minutes, T = 400°C
3. 400 = 500 - (500 - 100)e^(-4/τ)
4. 400 = 500 - 400e^(-4/τ)
5. 400e^(-4/τ) = 100
6. e^(-4/τ) = 0.25
7. -4/τ = ln(0.25)
8. τ = -4/ln(0.25) = 2.89 minutes
iii. Final Values:
1. K = 400°C/kW
2. τ = 2.89 minutes
b. If at another time the engineer changes the power input linearly at a rate of 0.5
kW/min, what can you say about the maximum rate of change of process
temperature: When will it occur? How large will it be?
i. Rate of Change Formula:
1. dT/dt = (K/τ)(dP/dt)e^(-t/τ)
2. Power rate of change = 0.5 kW/min
3. Substituting values:
a. dT/dt = (400/2.89)(0.5)e^(-t/2.89)
b. dT/dt = 69.24e^(-t/2.89)
ii. Rate of temperature changed
1. dT/dt = (K/τ)(dP/dt)e^(-t/τ)
2. dP/dt = 0.5 kW/min
3. Maximum rate occurs at t = 0 when e^(-t/τ) = 1
4. Maximum rate = (400/2.89)(0.5) = 69.2°C/min
iii. Final Values:
1. Occurs immediately (t = 0)
2. Value = 69.2°C/min

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
3. Second-order system considered as parallel connection of two ﬁrst-order systems: Transfer
function: G(s) = Y(s)/U(s) = 10/[(5s+1)(3s+1)] Find y(t→∞) for:
a. Step input of height M:
i. Input in Frequency Domain:
ii.
1. A step input of height M can be represented in the Laplace domain
as:
a. U(s) = M/s
2. Output in the Laplace Domain:
a. Using the transfer function:
i. Y(s) = G(s)·U(s) = [10/(5s+1)(3s+1)]·[M/s]
ii. So:
iii. Y(s) = 10M/[s(5s+1)(3s+1)]
b. Partial Fraction Decomposition:
i. Decompose Y(s):
1. 10/[(5s+1)(3s+1)] = A/(5s+1) + B/(3s+1)
ii. Multiply through by (5s+1)(3s+1):
1. 10 = A(3s+1) + B(5s+1)
iii. Expand:
1. 10 = 3As + A + 5Bs + B
iv. Group terms:
1. 10 = (3A + 5B)s + (A + B)
v. Coefficients:
1. For s: 3A + 5B = 0
2. For constant: A + B = 10
vi. Substitute into 3A + 5B = 0:
1. 3A + 5(10 - A) = 0
2. 3A + 50 - 5A = 0
3. -2A + 50 = 0
4. A = 25
vii. Substitute A = 25 into A + B = 10:
1. 25 + B = 10
2. B = -15
viii. Partial fraction decomposition is:
1. 10M/[s(5s+1)(3s+1)] = A/s + B/(5s+1) +
C/(3s+1)
c. Finding the Steady-State Output:
i. ﬁnal value theorem:
1. y(t→∞) = lim[s→0] sY(s)
ii. Plugging into our equation:
1. y(t→∞) = lim[s→0] s·[10M/s(5s+1)(3s+1)] =
10M/[(5·0+1)(3·0+1)] = 10M/(1·1) = 10M
d. y(t→∞) = 10M

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
b. Unit impulse input δ(t):
1. The unit impulse input in the s-domain is U(s) = 1
2. The output in the s-domain is:
a. Y(s) = G(s)U(s) = 10/[(5s+1)(3s+1)] × 1
b. Y(s) = 10/[(5s+1)(3s+1)]
3. Using inverse Laplace transform of 1/(as+1) = e^(-t/a):
a. y(t) = 25e^(-t/5) - 15e^(-t/3)
4. y(t→∞) = 0
4. Underdamped Second-Order System [Seborg 5.14]

a. Calculate all important parameters and write an approximate transfer function in
the form: R'(s)/P'(s) = K/(τ²s² + 2ζτs + 1) where: R' is the instrument output deviation
(mm), P' is the actual pressure deviation (psi).
i. Calculate Gain (K):
1. ΔP = 31 psi - 15 psi = 16 psi
2. ΔR = 11.2 mm - 8 mm = 3.2 mm
3. K = ΔR / ΔP = 3.2 mm / 16 psi = 0.2 mm/psi
ii. Calculate Overshoot (OS):
1. OS = (Peak Value - Final Value) / Final Value
2. OS = (12.7 mm - 11.2 mm) / (11.2 mm - 8) = 1.5/3.2 = 0.46875
iii. Calculate Damping Coefficient (ζ):
1. OS = exp(-πζ / sqrt(1 - ζ²))
2. 0.46875 = exp(-πζ / sqrt(1 - ζ²))
3. ln(0.46875) = -πζ / sqrt(1 - ζ²)
4. -0.7576 = -πζ / sqrt(1 - ζ²)
5. 0.7576/π = ζ / sqrt(1-ζ²). Let's name 0.7576/π as C
6. C = ζ / sqrt(1-ζ²)
7. C² = ζ²/(1-ζ²)
8. C² - C² * ζ² = ζ²
9. C² = ζ² * (1+C²)
10. ζ = C/sqrt(1+C²)
11. ζ = 0.234
iv. Calculate Time to ﬁrst peak (Tp):
1. Given as 2.3
v. Calculate damped period (Td):

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
1. Td = 2 * Tp = 4.6 s
vi. Calculate Natural Period (τ):
1. Td = 2πτ/sqrt(1-ζ²)
2. τ = Tdsqrt(1-ζ²)/(2π) = 4.6sqrt(1-0.234²)/(2π) ≈ 0.712 s
3. τ² = 0.507
vii. Assemble Transfer Function:
1. R'(s)/P'(s) = K / (τ²s² + 2ζτs + 1) = 0.2/(0.507s² + 2 * 0.234 * 0.712s + 1)
2. = 0.2/(0.507s² + 0.333s + 1)
b. Write an equivalent differential equation model in terms of actual (not deviation)
variables.
i. From Transfer Function:
1. 0.507s²R'(s) + 0.333sR'(s) + R'(s) = 0.2P'(s)
ii. Inverse Laplace Transform:
1. 0.507(d²R'/dt²) + 0.333(dR'/dt) + R' = 0.2P'
iii. Use actual variables:
1. R' = R - 8
2. P = P' + 15
3. P' = P – 15
iv. Substitute and Simplify:
1. 0.507(d²R/dt²) + 0.333(dR/dt) + (R-8) = 0.2(P-15)
2. 0.507(d²R/dt²) + 0.333(dR/dt) + R - 8 = 0.2P - 3
3. 0.507(d²R/dt²) + 0.333(dR/dt) + R = 0.2P + 5
5. High-order dynamics due to connection of multiple simpler low-order models [Seborg 6.7],
A pressure-measuring device analyzed and modeled Device responds to pressure changes
as a ﬁrst-order process in parallel with a second-order process First-order process
characteristics: Gain = -3, Time constant = 20 min, Additional test data: Step change in P
from 4 to 6 psi, Actual output Pm (not Pm') plotted in ﬁgure.

a. Determine Q'(s)
i. From the block diagram:
1. The ﬁrst-order process model for Q'(s) is given as: Q'(s) = (-3)/(20s +
1)P'(s).
2. Q'(s) = [-3P'(s)]/(20s + 1)
b. Estimate the values of: K (gain), τ (time constant), ζ (damping coefficient)

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
i. K (gain):
1. The second-order process transfer function is:
a. R'(s) = K/(τ²s² + 2ζτs + 1)P'(s)
2. The steady-state output Pm happens when s = 0.
a. G(s) = -3/(20s + 1) + K/(τ²s² + 2ζτs + 1
3. For steady state (s = 0):
a. Q'(s) = -3/1 and R'(s) = K
4. Output Pm is the summation of Q'(s) and R'(s):
a. Pm = Q'(s) + R'(s)
5. From the graph:
a. Input step change: ΔP = 2 psi (from 4 to 6 psi)
b. Output response (ΔPm) reaches ~22%
6. Solve for K:
a. ΔPm = Q'(s) + R'(s) = -3 × 2 + K × 2 = 22
b. -6 + 2K = 22 → K = 14
ii. ζ (damping coefficient):
1. The damped natural frequency (ωd) is related to tp as:
a. tp = π/ωd
b. ωd = π/tp = π/15 ≈ 0.2094 rad/min
2. The natural frequency (ωn) is related to ωd as:
a. ωn = ωd/sqrt(1 - ζ²)
3. Damping ratio ζ
a. Using the overshoot (Mp) from the plot:
i. Mp = (Peak value - Steady-state value)/(Steady-state
value) = (26 - 22)/22 = 0.1818
b. The overshoot (Mp) is related to ζ as:
i. Mp = exp(-πζ/sqrt(1-ζ²))
c. Taking the natural logarithm:
i. ln(0.1818) = -πζ/sqrt(1-ζ²)
ii. -1.705 = -πζ/sqrt(1-ζ²)
d. Solving for ζ:
i. ζ = 0.412
4. τ (time constant):
a. τ = 1/ωn
b. ωn = ωd/sqrt(1-ζ²) = 0.2094/sqrt(1-(0.412)²) ≈ 0.2284
c. Solve for τ:
i. τ = 1/ωn ≈ 1/0.2284 ≈ 4.38 min
c. What is the overall transfer function for the measurement device Pm'(s)/P'(s)?
i. Pm'(s)/P'(s) = -3/(20s + 1) + 14/(τ²s² + 2ζτs + 1)
1. Substitute τ = 4.38 and ζ = 0.412:
a. τ² = (4.38)² = 19.18
b. 2ζτ = 2 × 0.412 × 4.38 ≈ 3.61
c. Pm'(s)/P'(s) = -3/(20s + 1) + 14/(19.18s² + 3.61s + 1)

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
6. Second-order dynamics due to recycle connections. [Seborg 6.19]. Consider the following
connection of isothermal reactors. A ﬁrst-order reaction A → B occurs in both reactors, with
reaction rate constant k. The volumes of liquid in the reactors, V, are constant and equal;
the ﬂow rates F₀, F₁, F₂ and R are constant. Assume constant physical properties and a
negligible time delay for the recycle line.
a. Write a mathematical model for this process.
i. First Reactor:
1. Rate of accumulation = Inﬂow - Outﬂow - Reaction rate
2. V(dC₁/dt) = F₀C₀ - F₁C₁ - kVC₁
ii. Simplify:
1. dC₁/dt = (F₀C₀)/V - (F₁C₁)/V - kC₁
iii. Second Reactor:
1. Rate of accumulation = Inﬂow - Outﬂow - Reaction rate
2. V(dC₂/dt) = F₁C₁ - F₂C₂ - kVC₂
iv. Simplify:
1. dC₂/dt = (F₁C₁)/V - (F₂C₂)/V - kC₂
v. Equations:
1. dC₁/dt = (F₀C₀)/V - (F₁C₁)/V - kC₁
2. dC₂/dt = (F₁C₁)/V - (F₂C₂)/V - kC₂
b. Derive a transfer function model relating the output concentration of A, C₂ to the
inlet concentration of A, C₀.
i. Laplace Transform of the Material Balance Equations
ii. For reactor 1:
1. VsC₁(s) = F₀C₀(s) - F₁C₁(s) - kVC₁(s)
iii. Solve for C₁(s):
1. (Vs + F₁ + kV)C₁(s) = F₀C₀(s)
2. C₁(s) = F₀/(Vs + F₁ + kV)C₀(s)
iv. For reactor 2:
1. VsC₂(s) = F₁C₁(s) - F₂C₂(s) - kVC₂(s)
v. Solve for C₂(s):
1. (Vs + F₂ + kV)C₂(s) = F₁C₁(s)
vi. Substitute C₁(s) = F₀/(Vs + F₁ + kV)C₀(s):
1. C₂(s) = [F₁/(Vs + F₂ + kV)][F₀/(Vs + F₁ + kV)]C₀(s)
vii. Simplify:
1. C₂(s) = F₀F₁/[(Vs + F₁ + kV)(Vs + F₂ + kV)]C₀(s)
viii. Transfer function:
1. C₂(s)/C₀(s) = F₀F₁/[(Vs + F₁ + kV)(Vs + F₂ + kV)]
c. Verify that, in the limit of no recycle (R → 0), the transfer function derived in (b) is
equivalent to the transfer function of the two tanks connected in series.
i. When R → 0:
1. F₁ = F₂, meaning there is no recycle ﬂow.
ii. The simpliﬁed transfer function becomes:
1. C₂(s)/C₀(s) = F₀F₁/[(Vs + F₁ + kV)(Vs + F₁ + kV)]

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
d. Show that when k = 0 and a very large recycle ﬂow rate is used (i.e., the limit as R →
∞), the transfer function derived in (b) becomes the transfer function of a single tank
that has the volume equal to 2V and a gain of 1. Hint: Recognize that F₁ = R + F₂ and
F₀ = F₂.
i. When k = 0:
1. No chemical reaction occurs, so C₂ depends entirely on ﬂow and
mixing.
ii. When R → ∞:
1. For very large recycle ﬂow, F₁ >> F₂, and the system behaves as if the
two reactors are a single tank with a total volume of 2V.
iii. The transfer function for a single tank of volume 2V is:
1. C₂(s) = C₀(s)/(2Vs)
iv. Gain of such a system = 1

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
7. In industrial practice, engineers often do not build models from ﬁrst principles, but instead
put a step signal (or other designed signals) on the input and “identify” the model from the
resulting output response data. This procedure, called “system identiﬁcation”, can be done
either by engineer’s ﬂesh-eye readings, rough calculations, or statistical software. Matlab
and Python have well established toolboxes for it. On the other hand, since system
identiﬁcation is an extremely time-consuming (and hence expensive) task, it remains a
focus of today’s industrial control technology research and development. To answer the
following question, you may want to read Sections 7.1 and 7.2 of Seborg ﬁrst. A process
consists of two stirred tanks with input q and outputs T₁ and T₂ (see ﬁgure below). To test the
hypothesis that the dynamics in each tank are basically ﬁrst-order, a step change in q is
made from 82 to 85 L/min, with output responses given in the table.
a. Find the transfer functions T₁(s)/Q(s) and T₂(s)/T₁(s). Assume that they are of the
form K/(τs + 1).
i. Input: q (ﬂow rate)
ii. Outputs: T₁(t) (temperature response from Tank 1) and T₂(t) (temperature
response from Tank 2)
iii. Dynamics in both tanks are assumed ﬁrst-order:
1. Tank 1: T₁(s)/Q(s) = K₁/(τ₁s + 1)
2. Tank 2: T₂(s)/T₁(s) = K₂/(τ₂s + 1)
iv. Using the general ﬁrst-order system response to a step input:
1. T(t) = Tﬁnal + (Tinitial - Tﬁnal)e^(-t/τ)
v. Analyze the Tank 1 response
1. From the table, the response of T₁(t)
2. Steady-state gain (K₁):
a. The step change in q is Δq = 85 - 82 = 3 L/min
b. The steady-state change in T₁ is ΔT₁ = 23.31 - 20.00 = 3.31 °C
c. K₁ = ΔT₁/Δq = 3.31/3 = 1.103 °C/L/min
3. Time constant (τ₁):
a. From the data, T₁(t) reaches 63.2% of its total change by t = 3
min
b. τ₁ = 3 min
c. The transfer function for Tank 1 is:
d. T₁(s)/Q(s) = 1.103/(3s + 1)
vi. Analyze the Tank 2 response
1. From the table, the response of T₂(t)
2. Steady-state gain (K₂):
a. The steady-state change in T₂ is ΔT₂ = 26.00 - 25.77 = 0.23 °C
b. K₂ = ΔT₂/ΔT₁ = 0.23/3.31 = 0.0694
3. Time constant (τ₂):
a. From the data, T₂(t) reaches 63.2% of its total change by t =
1.5 min
b. τ₂ = 1.5 min
4. The transfer function for Tank 2 is:

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
a. T₂(s)/T₁(s) = 0.0694/(1.5s + 1)
b. Calculate the model responses to the same step change in q and plot with the
experimental data.
i. Tank 1 Model:
1. Input Q(s), transfer function T₁(s)/Q(s) = 1.103/(3s + 1)
ii. Tank 2 Model:
1. Input T₁(s), transfer function T₂(s)/T₁(s) = 0.0694/(1.5s + 1)
iii. The overall response is:
1. T₂(s)/Q(s) = [1.103/(3s + 1)] × [0.0694/(1.5s + 1)]

iv.

CHE 435 - Process Systems Analysis and Control
Spring 2025 – Dr. Tang
Brennon Brown
HW3
8. Process control in depth: Lead-lag dynamics [Seborg 6.4] Consider a process model (for
simplicity, you may assume K = 1): Y(s)/U(s) = K(τ₂s + 1)/(τ₁s + 1)(τ₂s + 1), (τ₁ > τ₂) For a step
input, prove that:
a. y(t) can exhibit an extremum (maximum or minimum value) in the step response
only if: (1 - τ₂/τ₁)/(1 - τ₂/τ₁) > 1
i. Write the step response:
ii. Take Y(s) and separate it using partial fraction expansion:
1. Y(s) = 1/s - (τ₁ - τ₂)/τ₁ × 1/(τ₁s + 1)
iii. Transform back to the time domain:
1. y(t) = 1 - [(τ₁ - τ₂)/τ₁]e^(-t/τ₁) - (τ₂/τ₁)e^(-t/τ₂)
iv. Differentiate y(t):
1. dy(t)/dt = [(τ₁ - τ₂)/τ₁] × (1/τ₁)e^(-t/τ₁) + (τ₂/τ₁) × (1/τ₂)e^(-t/τ₂)
v. Simplify:
1. dy(t)/dt = [(τ₁ - τ₂)/(τ₁τ₁)]e^(-t/τ₁) - (τ₂/τ₁τ₂)e^(-t/τ₂)
vi. Set dy(t)/dt = 0 to ﬁnd the condition for extrema:
1. [(τ₁ - τ₂)/τ₁²]e^(-t/τ₁) = (1/τ₁)e^(-t/τ₂)
vii. Cancel terms and rearrange:
1. (τ₁ - τ₂)/τ₁ = e^[t(1/τ₂ - 1/τ₁)]
viii. Taking the natural logarithm:
1. t = [τ₁τ₂/(τ₁ - τ₂)]ln[(τ₁ - τ₂)/τ₁]
ix. For the extremum
1. (1 - τ₂/τ₁)/(1 - τ₂/τ₁) > 1
b. Overshoot occurs only for τ₂/τ₁ > 1
i. Overshoot occurs
1. y(t) = 1 - [(τ₁ - τ₂)/τ₁]e^(-t/τ₁) - (τ₂/τ₁)e^(-t/τ₂)
ii. For y(t) to exceed 1
1. τ₂/τ₁ > 1, i.e., τ₂ > τ₁
a. we are given τ₁ > τ₂, so overshoot does not occur unless this
condition is violated.
c. Inverse response occurs (namely an extreme of y(t) has a different sign from K) only
for τ₂ < 0.
i. From the step response:
1. y(t) = 1 - [(τ₁ - τ₂)/τ₁]e^(-t/τ₁) - (τ₂/τ₁)e^(-t/τ₂)
ii. Initially, at t = 0:
1. y(0) = 1 - (τ₁ - τ₂)/τ₁ - τ₂/τ₁ = 1 - 1 = 0
iii. For an inverse response to occur, set τ₂ < 0. The inverse response exists only
when τ₂ < 0.
d. If an extremum in y exists, the time at which it occurs can be found analytically.
What is it?
i. The time at which the extremum occurs is:
1. t = [τ₁τ₂/(τ₁ - τ₂)]ln[(τ₁ - τ₂)/τ₁]



## Metadata
- Source file: junk_drawer/HW3_Brennon Brown.pdf
- Extracted: 2026-05-18
- Category: academic-homework
