# MSE 360 HW7.pdf

Source: junk_drawer/MSE 360 HW7.pdf

Category: [[academic-homework]]

## Summary
MSE 360: Kinetic Processes in Materials Homework #7 Instructions: Answer the following questions on a separate piece of paper. Be sure that your name and date are on the first page. Upload your work as a PDF to Moodle for credit. All work must be done individually. (There are 2 problems: Problem 2 starts on 2nd page) 1. The following equation (Equation 4.43) provides the solution for transient finite (symmetric) planar diffusion in a plate of thickness L starting from a uniform initial concentra

## Full Content
MSE 360: Kinetic Processes in Materials
Homework #7
Instructions: Answer the following questions on a separate piece of paper. Be sure that your
name and date are on the first page. Upload your work as a PDF to Moodle for credit. All work
must be done individually.
(There are 2 problems: Problem 2 starts on 2nd page)

1. The following equation (Equation 4.43) provides the solution for transient finite
(symmetric) planar diffusion in a plate of thickness L starting from a uniform initial
concentration of 𝐶𝑖0 when the concentrations at the edges of the plate are set to 𝐶𝑖∗ at t =0:
∞

𝐶𝑖 (𝑥, 𝑡) = 𝐶𝑖∗ + (𝐶𝑖0 − 𝐶𝑖∗ )

4
1
𝑥
2 2
2
∑(
sin [(2𝑗 + 1)𝜋 ] 𝑒 −(2𝑗+1) 𝜋 𝐷𝑡/𝐿 )
𝜋
2𝑗 + 1
𝐿
𝑗=0

At “long times,” this solution can be reasonably approximated by using only the first term
in series without significant error. In order to determine a reasonable value for “long time”
and to visualize the effect that this approximation has on the solution compared to retaining
additional terms in the series, use a software program of your choice (e.g. Excel, Matlab,
Mathematica) to make a set of plots for this solution using j = 1, 3, and 10 terms in the
series at each of the following three times:
𝐿2

a. 𝑡 = 0.01 [𝜋2𝐷]
𝐿2

b. 𝑡 = 0.1 [𝜋2𝐷]
𝐿2

c. 𝑡 = 1 [𝜋2𝐷]
Assume 𝐶𝑖∗ = 0. Comment on the results.

2. Steel often contains trace amounts of H2, which can lead to embrittlement. To avoid
embrittlement, steel is often degassed prior to use in order to remove these trace H 2
impurities. Degassing steel involves placing the steel in a vacuum, where the H 2
concentration in the vacuum can be considered zero at all times. Degassing proceeds by
three steps: 1) Solid-state diffusion of H2 from the steel bulk to the steel surface. 2) Desorption of H2 from the surface of the steel. 3) Gas-phase diffusion of the H2 away from
the steel surface.

Schematic diagram of the cross-section of a steel plate of thickness 𝛿 with a constant H2
concentration of 𝐶𝐻02 .
a) Based on what you know about the typical rates of the three steps involved in the steel degasification process, which of the three steps is likely to be the rate-determining step and
why?
b) Consider a steel plate which initially contains a uniform concentration (𝐶𝐻02 ) of 1015
molecules/cm3, as shown above. Assuming that the desorption of H2 from the surface of
the steel is the rate determining step in steel degasification, draw a diagram illustrating the
H2 concentration profile across the steel plate at five times: t = 0 < 𝑡1 < 𝑡2 < 𝑡3 < 𝑡∞ .
c) Assuming that solid-state diffusion of H2 from the bulk to the surface of the steel is the rate
determining step in steel degasification, draw a diagram illustrating the H 2 concentration
profile across the steel plate at five times: t = 0 < 𝑡1 < 𝑡2 < 𝑡3 < 𝑡∞ .
d) Assuming that solid-state diffusion of H2 from the bulk to the surface of the steel is the rate
determining step in steel degasification, is this a finite, semi-infinite, or infinite boundaryvalue problem?
e) Assuming that solid-state diffusion of H2 from the bulk to the surface of the steel is the rate
determining step in steel degasification, provide the two boundary conditions and one
initial condition for this transient diffusion problem. Note that x = 0 corresponds to the
center of the steel plate. Assume the steel plate is 1 mm thick.

f) By employing your boundary conditions and initial conditions to evaluate this transient
diffusion problem, you arrive at the following solution for the time-dependent
concentration of H2 at the center of the steel plate [C(x = 0, t)]:
𝜋 2
𝐶(0, 𝑡) = 𝐶𝐻02 𝑒𝑥𝑝 [−𝐷𝑡 ( ) ]
𝛿
where 𝛿 is the thickness of the steel plate and 𝐶𝐻02 is the initial (t = 0) concentration of H2
in the steel plate. The H2 embrittlement is avoided if the H2 concentration in the steel is
reduced below 1013 molecules/cm3. If the diffusivity of H2 in steel under degassing
conditions is 10-6 cm2/s, how long must the steel be degassed to ensure the H2 concentration
at the center of the plate falls below 1013 molecules/cm3? Assume the steel plate is 1 mm
thick.
g) How long must a 4-mm thick steel plate be degassed to avoid H2 embrittlement?



## Metadata
- Source file: junk_drawer/MSE 360 HW7.pdf
- Extracted: 2026-05-18
- Category: academic-homework
