# NE235 Lecture 6 (1).pdf

Source: junk_drawer/NE235 Lecture 6 (1).pdf

Category: [[academic-lecture]]

## Summary
NE235 Nuclear Reactor Operations Module #6 Subcritical Multiplication & Behavior Of Sub-Critical Reactors Dept. of Nuclear Engineering North Carolina State University NE235 Nuclear Reactor Operations Training Module #6 Module #6 Contents:

## Full Content
NE235 Nuclear Reactor Operations
Module #6
Subcritical Multiplication & Behavior
Of Sub-Critical Reactors
Dept. of Nuclear Engineering
North Carolina State University

NE235 Nuclear Reactor Operations Training
Module #6
Module #6 Contents:
1. Sub-Criticality
2. Characteristics of Sub-Critical Multiplication
3. Reactor Behavior During Start-Up
4. Introduction to 1/M Approach to Criticality
Laboratory Session next week (Thurs. 10/6):
• Lab #4 – 1/M Approach to Criticality
Homework #6 – Due Thursday 10/13/2022

NE235 Nuclear Reactor Operations Training

2

NE235 Nuclear Reactor Operations Training
Module #6
Recap from Module #4
Keff=ηƒεpℒFℒTH
>730 pcm | Super Prompt Critical

Keff

>1 | Supercritical
=1 | Critical
<1 | Sub-Critical

NE235 Nuclear Reactor Operations Training

r=

𝐾𝑒𝑓𝑓 −1
𝐾𝑒𝑓𝑓

=730 pcm | Prompt Critical
=0 pcm

| Delayed Critical

<0 pcm

| Sub-Critical

3

Source Neutrons (S) –vs- Fission Neutrons (Nf)
Fission Neutrons; Nf - Increase through subcritical multiplication, then
exponentially in super-critical reactor

Nf

Critical at power levels up to 1 MW: ΦTH ~1x1013 n/cm2/sec (nominal)

Delayed
»
Supercriticality

1 < Keff < 1.0073
0 < ρnet < 730pcm

Critical @ 10W (Rods at ACP):

ΦTH ~1x108 n/cm2/sec (nominal)

Keff = 1; ρnet = 0
Subcritical
Multiplication

S

»

Keff <1
ρnet <0

Use subcritical multiplication
equations to predict behavior!

Sub-Critical (Shutdown - Rods In): ΦTH ~103-104 n/cm2/sec (nominal)

Source Neutrons; S ~ Constant for each Start-Up
NE235 Nuclear Reactor Operations Training

4

Sub-Criticality
Reactor is Sub-Critical ∴ Keff <1
So what is happening to neutron population?
If Ni = # Fission Neutrons in Generation i
Then Ni+1 = # Fission Neutrons in Next Generation i+1
Where Ni+1 = Ni * Keff
So, if Keff < 1
Ni+1 < Ni
Ni+2 < Ni+1
∴ 𝐍𝐢 → 𝟎 𝒂𝒔 𝒕 → ∞
Therefore, the number of neutrons lost per generation:
= Ni - Ni+1
Reference:
= Ni - (Ni * Keff)
Reactor Theory
= Ni (1 - Keff)
Manual;
Ch.1 §1.5.2

NE235 Nuclear Reactor Operations Training

5

Sub-Criticality
But, We have “Source” Neutrons, S:
• γ, 𝑛 on Deuterium and Beryllium – Photoneutrons

• Spontaneous Fission of 235𝑈, 238𝑈, etc…
• (𝛼, 𝑛) on 18𝑂, in fuel
• PuBe Source

Total Source
Neutrons (S),
~ Constant
During Start-up

• Photo-Fission (e.g. of 238𝑈) – very small factor
So, with Keff < 1,

𝑺 = 𝑵𝒊 𝟏 − 𝑲𝒆𝒇𝒇

𝑬𝒒 #𝟏. 𝟏𝟐

# Of Source Neutrons = # Lost Per Generation

NE235 Nuclear Reactor Operations Training

6

Sub-Criticality
After many generations the reactor will reach “sub-critical equilibrium”
Where:

𝑵𝒆𝒒 = 𝑺

𝟏
𝟏−𝑲𝒆𝒇𝒇

𝐸𝑞 #1.24

Therefore, during a start-up as reactor approaches criticality and
Keff approaches 1 (Keff→ 𝟏):
a) # of source neutrons S stays the same.
b) # of neutrons lost from fission chain decreases : e.g. Ni(1-Keff)
decreases.
𝟏
) will increase for
𝟏−𝑲𝒆𝒇𝒇

c) Equilibrium neutron population Neq = S(
each step increase in Keff
NE235 Nuclear Reactor Operations Training

7

Characteristics of Sub-Critical
Multiplication in Reactor
Rules of Sub-Critical Multiplication:
Rule #1: Equal changes in Keff (or ρ) DO NOT result in equal changes in
equilibrium neutron population Neq
(Ex: See Table 1.1 next slide)
• 𝑨𝒔 𝑲𝒆𝒇𝒇 𝟎. 𝟔 → 𝟎. 𝟕 ∶ 𝑵𝒆𝒒 𝟓𝟎𝟎 → 𝟔𝟔𝟕 ∆= +𝟏𝟔𝟕
• 𝑨𝒔 𝑲𝒆𝒇𝒇 𝟎. 𝟕 → 𝟎. 𝟖 ∶ 𝑵𝒆𝒒 𝟔𝟔𝟕 → 𝟏𝟎𝟎𝟎 ∆= +𝟑𝟑𝟑

Rule #2: Each time the difference between Keff and 1 is cut in half,
Neq doubles (therefore the NFM Count Rate doubles)
(Ex: See Table 1.1 next slide)
• 𝑨𝒔 𝑲𝒆𝒇𝒇 𝟎. 𝟔 → 𝟎. 𝟖 ∶ 𝑵𝒆𝒒 𝟓𝟎𝟎 → 𝟏𝟎𝟎𝟎
• 𝑨𝒔 𝑲𝒆𝒇𝒇 𝟎. 𝟖 → 𝟎. 𝟗 ∶ 𝑵𝒆𝒒 𝟏𝟎𝟎𝟎 → 𝟐𝟎𝟎𝟎
NE235 Nuclear Reactor Operations Training

8

Characteristics of Sub-Critical
Multiplication in Reactor
Table 1.1:
Neutron Population
–vs- Keff
N0+N1 = 200 + 200*0.6
N0+N1+N2 = 200 + 200*0.6 + 200*0.6*0.6

Neq = 200*(1/0.4)

NE235 Nuclear Reactor Operations Training

9

Characteristics of Sub-Critical
Multiplication in Reactor
Rules of Sub-Critical Multiplication (continued):
Rule #3:

As Keff → 1, more generations are required to reach
equilibrium.

NE235 Nuclear Reactor Operations Training

Keff

# Gen to Eq.

0.9

130

0.99

1373

0.999

13808

0.9999

138147

10

Characteristics of Sub-Critical
Multiplication in Reactor
Figure 1.3:
# of Generations
(time) to
Equilibrium (Neq) as
a function of Keff

NE235 Nuclear Reactor Operations Training

11

Characteristics of Sub-Critical
Multiplication in Reactor
Figure 1.4:
Reactor Neutron Flux
Monitor (NFM)
Startup Trace
Y axis = time
X axis = log count rate

NE235 Nuclear Reactor Operations Training

12

Characteristics of Sub-Critical
Multiplication in Reactor
These rules relating changes to neutron population (N) to changes
in Keff can be used to predict reactor behavior during startup &
approach to criticality.
Since neutron population (N) is proportional to the startup countrate (CR) as
indicated on the Neutron Flux Monitor (NFM), we can relate CR to Keff :
𝑪𝑹 ∝ 𝑵𝒆𝒒 = 𝑺

𝟏
𝟏−𝑲𝒆𝒇𝒇

where Keff < 1 (from Eq. 1.24)

∴ A change in Keff (e.g. K1 to K2) will make a predictable change in CR:
𝑪𝑹𝟏 ∝ 𝑺

𝟏
𝟏−𝑲𝟏

𝒂𝒏𝒅

𝑪𝑹𝟐 ∝ 𝑺

𝑪𝑹𝟐
𝟏 − 𝑲𝟏
∴
=
𝑪𝑹𝟏
𝟏 − 𝑲𝟐

𝟏
𝟏−𝑲𝟐

where S is constant

𝑬𝒒. #𝟏. 𝟐𝟔

∴ As the NFM countrate changes, we can evaluate changes in Keff
as we approach criticality.
NE235 Nuclear Reactor Operations Training

13

Example: Reactor Behavior During Startup
Example: Predict Reactor Behavior During a Start-up
Given:
• Reactor is subcritical with ρnet = -200 pcm (e.g. from rod positions)
• Neutron Flux Monitor (NFM) Initial Count Rate (CR0) = 50 CPS
Calculate Keff & Equilibrium Count Rate (CR) for the following step
changes in reactivity at times 1,2, and 3:
Time

ρnet

Keff

CR

0

r0 = -200pcm

K0 = ?

CR0 = 50

1

r1 = -100pcm

K1= ?

CR1= ?

2

r2 = -50pcm

K2= ?

CR2= ?

3

r3 = -5pcm

K3= ?

CR3= ?

NE235 Nuclear Reactor Operations Training

14

Example: Reactor Behavior During Startup
First, convert r (pcm) to K:
𝝆=

𝑲−𝟏
𝑲

𝟏

∴ 𝑲 = 𝟏−𝝆 (where for reference, 𝟎. 𝟎𝟎𝟏 ∆𝒌
= 𝟏𝟎𝟎 𝒑𝒄𝒎 )
𝒌
𝟏

So, r 0 = - 200 pcm = -0.002 DK/K, so 𝑲𝟎 = 𝟏−(−𝟎.𝟎𝟎𝟐) = 𝟎. 𝟗𝟗𝟖𝟎
Now, add +100 pcm to r0 so ρ1 = -100 pcm & 𝑲𝟏 =
𝟏−𝑲

𝟏
= 𝟎. 𝟗𝟗𝟗𝟎
𝟏−(−𝟎.𝟎𝟎𝟏)

𝟏−𝟎.𝟗𝟗𝟖𝟎

Now from Eq #1.26: CR1 = CR0 𝟏−𝑲𝟎 ; 𝒔𝒐 𝟓𝟎 𝟏−𝟎.𝟗𝟗𝟗𝟎 = 𝟏𝟎𝟎
𝟏

Time

ρnet

Keff

CR

0

r0 = -200pcm

K0 = 0.9980

CR0 = 50

1

r1 = -100pcm

K1 = 0.9990

CR1 = 100

2

r2 = -50pcm

3

r3 = -5pcm

NE235 Nuclear Reactor Operations Training

15

Example: Reactor Behavior During Startup
Now, add +50pcm to ρ1 so ρ2 = -50 pcm & 𝑲𝟐 =
𝟏−𝑲

𝟏
= 𝟎. 𝟗𝟗𝟗𝟓
𝟏−(−𝟎.𝟎𝟎𝟎𝟓)

𝟏−𝟎.𝟗𝟗𝟗𝟎

Now CR2 = CR1 𝟏−𝑲𝟏 ; 𝟏𝟎𝟎 𝟏−𝟎.𝟗𝟗𝟗𝟓 = 𝟐𝟎𝟎
𝟐

Now, add +45 pcm to ρ2 so ρ3 = -5 pcm & 𝑲𝟑 =

Now CR3 = CR2

𝟏−𝑲𝟐
𝟏−𝑲𝟑

; 𝟐𝟎𝟎

𝟏−𝟎.𝟗𝟗𝟗𝟓
𝟏−𝟎.𝟗𝟗𝟗𝟗𝟓

𝟏
= 𝟎. 𝟗𝟗𝟗𝟗𝟓
𝟏−(−𝟎.𝟎𝟎𝟎𝟎𝟓)

= 𝟐𝟎𝟎𝟎

Time

ρnet

Keff

CR

0

r0 = -200pcm

K0 = 0.9980

CR0 = 50

1

r1 = -100pcm

K1 = 0.9990

CR1 = 100

2

r2 = -50pcm

K2 = 0.9995

CR2 = 200

3

r3 = -5pcm

K3 = 0.99995

CR3 = 2000

So, we can predict values for the SRM countrate and Keff during startup!
NE235 Nuclear Reactor Operations Training

16

Lab #4 – 1/M Approach to Criticality
Objective: Perform a conservative approach to criticality and start up
reactor.
Laboratory Procedure Snapshot:
Make conservative projections of critical rod position and pull control rods
halfway to projected critical positions, or until NFM counts double,
whichever happens first. Iterate and converge on criticality.
Reactor Theory concepts:
• Criticality –vs- Sub-criticality
• Subcritical Multiplication Factor (M)

Physical Plant Elements:
• Reactor Core
• Control Rods
• Startup Range Monitor Channel and chart recorder
17

PULSTAR Reactor: Instrumentation Used for 1/M Startup
Reactor Core

Neutron Flux
Monitor Channel
Schematic
Neutron Flux Monitor
(NFM) Count Rate Meter

NEUTRON
FLUX
MONITOR

Control Rod
Position Indicators

Control Rods

Control Rod Drive
Switches

Fission Chamber
Schematic

NFM Count
Rate Recorder

18

Subcritical Multiplication Factor ‘M’
Relationship between 𝑲𝒆𝒇𝒇 , NFM Countrate (𝑪𝑹), and ‘M’:
𝑴=

𝑵𝒇 + 𝑺
𝑪𝑹𝟐 (𝟏 − 𝑲𝟏 )
∝
=
𝑺
𝑪𝑹𝟏 (𝟏 − 𝑲𝟐 )

Where:
𝑵𝒇 = number of fission generated neutrons (increases during
startup).
𝑺
= number of source (non-fission) neutrons = constant!
𝑪𝑹𝟏,𝟐 = iterated neutron count rate from NFM
𝑲𝟏,𝟐 = iterated 𝑲𝒆𝒇𝒇 value
So, as thermal utilization (f) increases (e.g. by pulling control rods),
𝑲𝒆𝒇𝒇 increases (𝑲𝒆𝒇𝒇 → 1 = criticality!), so (𝟏 − 𝑲𝒆𝒇𝒇 ) → 0
NFM CR2 increases as number of fission generated neutrons Nf in core
increases, so as CR2 → ∞, M → ∞

∞ is hard to plot, but

𝟏

M

→ 𝟎 is easy to plot!

19

1/M Configuration: Conservative –vs- Non Conservative
Conservative measurements – 𝑵𝒇 term must predominate over 𝑺.
SO: don’t put neutron source next to the SRM detector!
Steps:
1. Withdraw rods until NFM counts (𝑪𝑹) double – make first
projection – extrapolating to x-axis.

𝟏

M

𝑪𝑹

= 𝑪𝑹𝒐
𝒊

2. Withdraw rods HALFWAY to
projected criticality, or until
NFM counts (𝑪𝑹) double –
whichever comes first!
𝟏

3. Make 2nd M projection to xaxis and pull control rods
conservatively.
𝟏

4. Repeat until → 𝟎 and
M
criticality is reached.

20

Typical 1/M Plot
Projected

Data:
Rod
Pull #

Gang Control
Rod Height (in)

0

SRM Count
Rate (CPS)

1/M Factor

8

1.000

Criticality
(from plot)
Gang Rods (in)

Next Step:
Pull Rods to:
double counts

1

9.8

16

0.500

20.00

double counts

2

12.7

40

0.200

14.70

13.7

3

13.7

54

0.148

16.60

15.2

4

15.2

140

0.057

16.10

15.6

5

15.6

290

0.028

16.10

15.9

6

16.0

2200

0.004

16.10

16.1

7

16.1

21

Summary
• Characteristics of Sub-Critical Multiplication apply to reactor
behavior when Keff < 1 and r < 0.
• To predict reactor behavior during startup, use these three
rules:
#1. Equal changes in Keff (or ρ) DO NOT result in equal
changes in equilibrium neutron population Neq.
#2. Each time the difference between Keff and 1 is cut in half,
Neq doubles.
#3. As Keff → 1, more generations are required to reach
equilibrium.
• 1/M Approach to Criticality Lab: Use conservative
arrangement so 𝑵𝒇 term predominates over 𝑺 on SRM. Pull
control rods until SRM countrate doubles, or halfway to
projected critical rod height, whichever happens first.
22



## Metadata
- Source file: junk_drawer/NE235 Lecture 6 (1).pdf
- Extracted: 2026-05-18
- Category: academic-lecture
