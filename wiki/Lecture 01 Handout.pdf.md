# Lecture 01 Handout.pdf

Source: junk_drawer/Lecture 01 Handout.pdf

Category: [[academic-lecture]]

## Summary
CHE 435/525 Process Systems Analysis and Control Lecture 1: Introduction to Process Control Wentao Tang Assistant Professor, Chemical & Biomolecular Engineering North Carolina State University

## Full Content
CHE 435/525

Process Systems Analysis and Control

Lecture 1: Introduction to Process Control

Wentao Tang
Assistant Professor, Chemical & Biomolecular Engineering
North Carolina State University

January 7, 2025

Wentao Tang (NCSU)

Introduction

January 7, 2025

0 / 14

Introduction of myself

B.S. Chemical Engineering, Tsinghua University (2015)
▶

B.S. Mathematics, Tsinghua University (2015)

Ph.D., Chemical Engineering, Univ. of Minnesota (2020)
Process Control Engineer, Shell Global Solutions (2020–2022)
Assistant Professor, Chemical Engineering, NC State (2022–)
▶

Affiliate Faculty, Operations Research, NC State (2024–)

Wentao Tang (NCSU)

Introduction

January 7, 2025

1 / 14

A “Person in Control” for about a decade
Past: R&D Engineer in industry, focusing on practice

Now: Academic investigator, focusing on theory
“Data-driven control theory” (≈ control + machine learning)
Supported by grants from NSF, ACS, and UNC System
▶ 1 postdoc + 4 Ph.D. students
▶

▶

Active in the process control research community
American Control Conference – Associate Editor, 2025
AIChE Annual Meeting – Program Coordinator, 2026
▶ Journal Digital Chemical Engineering – Associate Editor
▶
▶

Wentao Tang (NCSU)

Introduction

January 7, 2025

2 / 14

Control: An interdisciplinary field of study
Who studies control?
▶

Electrical engineers – generators, rotors, power grids
⋆

They created this field of study first and still leads the advances

Chemical engineers – “process control”
▶ Mechanical engineers – robotics, autonomous driving, etc.
▶ Biomedical engineers & biologists – metabolism, gene regulation
▶ Mathematicians & computer scientists – “control theory”
▶

⋆

... can be applied to physics, chemistry, epidemics, social networks,
stock markets, etc.

Control is indispensable in all industries!
Wentao Tang (NCSU)

Introduction

January 7, 2025

3 / 14

Illustrative example: Blending process
Notation: x – mass fraction, w – mass flow rate

Assumptions
w1 = const., but x1 may fluctuate (a salty water stream to be diluted,
whose saltiness is uncertain)
2 x2 = const. = 1 (a water stream to dilute the salty water)
3 Perfect mixing in the tank
1

Wentao Tang (NCSU)

Introduction

January 7, 2025

4 / 14

Control objective & Controlled variabled
Control objective is specified on some controlled variables (CV).
Typical control objectives:
▶
▶

“Regulation”: Keep CVs near their setpoints or within some range.
“Tracking”: Make CVs follow some desirable trajectories.

This example: Regulate product composition (x).
Discuss: What are the control objectives when you drive a car?

Wentao Tang (NCSU)

Introduction

January 7, 2025

5 / 14

Disturbance variables & Manipulated variables

Disturbance Variables (DVs): affect CVs and cause them to deviate
▶

Here: x1 (composition of the stream to be treated)

Manipulated Variables (MVs): can be adjusted to shape the CVs
▶

Here: w2 (flow rate of the other stream)

This Example: Keep x (CV) at a setpoint xsp , despite variations in
x1 (t) (DV), by adjusting flow rate w2 (MV).
So, how?

Wentao Tang (NCSU)

Introduction

January 7, 2025

6 / 14

From process design to process control
Process design: Assuming all process variables are constants (i.e., x1
is at steady state, no disturbance)
▶

Steady-state relations for design:
0 = w̄1 + w̄2 − w̄
0 = w̄1 x̄1 + w̄2 x̄2 − w̄x̄

▶

To achieve desired composition (“setpoint”) x̄ = xsp , we need to design
w2 as
xsp − x̄1
w̄2 = w̄1
.
1 − xsp

Process control: Adjust w2 (t) against the disturbance in x1 (t) (no
longer const.) in order to regulate x(t).

Wentao Tang (NCSU)

Introduction

January 7, 2025

7 / 14

Strategy 1: Feedback control
Feedback control: Measure CV and take corrective action in MV.
▶

For example, w2 (t) = w̄2 + Kc [xsp (t) − x(t)]

Very natural idea ... Think about driving a car
Wentao Tang (NCSU)

Introduction

January 7, 2025

8 / 14

Strategy 2: Feedforward Control
Feedback control: Measure DV and take preventive action in MV.
▶

x −x (t)

For example, w2 (t) = w̄1 (t) sp1−x1sp

Discuss: Isn’t this actually a better idea?
Wentao Tang (NCSU)

Introduction

January 7, 2025

9 / 14

Feedback v.s. Feedforward

Feedforward control is idealistic, which requires
▶
▶

accurate measurement of DV;
accurate modoel (knowledge of how DV and MV affect the CV).

Feedback control is realistic.
▶
▶

Its performance/quality, however, can be restrictive
Goal of this course: Optimal feedback controller design

If possible, combined FB/FF control will be preferred.
Principle: To design a controller, we need the process model!

Wentao Tang (NCSU)

Introduction

January 7, 2025

10 / 14

Roadmap

1

Dynamic modeling of processes
▶

2

▶
▶

3

How does the output respond to the input?
How to calculate analytically and simulate numerically?

Simple controller design & synthesis
▶
▶

4

How to describe a process as ODEs?

Analysis of dynamical systems

How to achieve stability, robustness, and performance?
How to obtain the controller systematically?

Multivariable systems
▶
▶

How to deal with multi-input-multi-output?
How to operate the plant optimally?

Wentao Tang (NCSU)

Introduction

January 7, 2025

11 / 14

“Personality” of process control

One has to know some theory to do process control correctly!
▶

I mean ... some mathematics is necessary

“A fundamental characteristic of the field of systems and control research
is its rich intersection of engineering and mathematics – while the problem
formulations stem from engineering systems, the tools and techniques
employed are grounded in mathematics and computer science... It is this
abstract feature that enables the broad applicability of the field.”
[F. Lamnabhi-Lagarrigue et al. (2017). Annual Reviews in Control, 43, 1–64.]

“An engineer who does not know mathematics never needs it. But if he
knows it, he uses it frequently.” [J. Plemelj (1873–1967), mathematician]

Wentao Tang (NCSU)

Introduction

January 7, 2025

12 / 14

How to get along with process control?
1

Meet the basic expectations.
▶
▶

2

Attend the classes, do homeworks, and pass exams.
You are pursuing a degree. Minimize your distractions.

Practice, practice, practice!
Consent with what I write ̸= Ability to do it yourself.
Fill in the “gaps” that I left on the slides (if you feel there exist).
▶ True understanding comes from your practice.

▶

▶

3

Accept the challenges.
You will likely encounter comprehensive/complex problems in your
future jobs or advanced studies.
▶ Maybe – you don’t know the answer, you have never learned it, or your
math/coding skills are not yet sufficient.
▶ Blame whomever that makes your life so hard, or ask for help and help
yourself proactively
⋆ ... probably why process control takes place in your final semester
▶

Wentao Tang (NCSU)

Introduction

January 7, 2025

13 / 14

Growth mindset: What makes a good engineer

Wentao Tang (NCSU)

Introduction

January 7, 2025

14 / 14



## Metadata
- Source file: junk_drawer/Lecture 01 Handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
