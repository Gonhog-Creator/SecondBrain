# 2_DirectionFieldsAndPhaseLine (1).pdf

Source: junk_drawer/2_DirectionFieldsAndPhaseLine (1).pdf

Category: [[other]]

## Summary
MA341 Applied ODE’s Lecture Notes 2 Direction Field An equation of the type y ′ = f describes a slope of the solution y = y(t). This can be used to graphically study solutions behavior. The graphical representation

## Full Content
MA341
Applied ODE’s
Lecture Notes

2

Direction Field

An equation of the type y ′ = f describes a slope of the solution y = y(t). This
can be used to graphically study solutions behavior. The graphical representation
reminds the graph of Vector Field from Calc 3 course, although those things are very
different. Every trajectory on a direction field represents a solution to differential
equation. Direction fields become very useful when there no explicit solution do a
differential equation is available.
Example 2.1. Consider an equation
y′ = x − y
. Clearly, when x = y the slope is y ′ = 0, see Figure 1a blue arrows. If we fix x and
take various values of y the slope become negative at some moment, and it’s getting
steeper and steeper, see Figure 1a black arrows. Similarly, fixing y and taking various
values of x, the slope will turn positive and will get steeper as well, see Figure 1a red
arrows. In the end one arrive at Figure 1b.

2.1

The method of isoclines - level curves

Consider an ODE

dy
= f (x, y).
dx

Using different values of C draw a level curve f (x, y) = C. We usually use values of
C that are easier to calculate/represent.
Example 2.2. Consider
dy
= xy.
dx

M. Medvinsky

Applied Differential Equations

(a) Schematic.

(b) Direction Field

Figure 1: Direction Field: y ′ = x − y.
Choosing the value of C will give us a level curve xy = C. Solve it for y to get a
hyperbola
y=

C
.
x

Thus, on each hyperbola y = Cx we have a slope C, see Figure 2a. Figure 2b shows a
solution in case of y(0) = 1.

2.2

Phase Lines

Definition 2.3. An autonomous (or time-invariant) differential equation is an equation that does not explicitly depend on the independent variable, i. e. the case of
dy
= f (y).
dt
Definition 2.4. A solution to a differential equation is called an equilibrium solution
if it is constant and the slope of an equation is horizontal, i. e. if y = C (C = const)
and dy
= 0, those are the roots of f (C) = 0.
dt
We distinct 3 types of equilibria
1. A sink is a stable equilibrium, which is also its other name. Its attracting all
2

M. Medvinsky

Applied Differential Equations

(a) Direction Field

(b) Solution with IC y(0) = 1

Figure 2: Direction Field: y ′ = xy.
neighboring solutions to it as t → ∞. If y is a sink, then the solution y + ϵ,
where ϵ is a small value, will get close as t → ∞.
2. A source is an unstable equilibrium, that repel neighboring solutions.
3. A node is an unstable equilibrium, which is all the other cases.
Definition 2.5. Since an autonomous differential equation doesn’t depend on the
independent variable, its Direction Field looks the same for any value of t (or x).
Therefore, the same information can be represented in a compact form - on a y axis
only, which we call a Phase Line.
The equilibrium points are represented as circles on a phase line. The increasing
slope is represented as an arrow up, while the decreasing as an arrow down. As
such, a sink will be surrounded by arrows pointing inside a circle, while sources are
surrounded by arrow pointing out.
Example 2.6. Consider
y ′ = (y − 1)(y + 2).
The vector field has two equilibrium lines, the zeros of the slope y = 1 and y = −2.
When y > 1 the slope is clearly positive, when y < 1 the slope is negative. When
3

M. Medvinsky

Applied Differential Equations

y=1

y = −2

(a) Direction Field

(b) Phase Line

Figure 3: Direction Field and a Phase Line of y ′ = (y − 1)(y + 2)
y < −2 both y − 1 < 0 and y + 2 < 0, hence the slope is positive, see Figure 3a.
From the Figure 3a one can notice that y = 1 is a source and y = −2 is a sink. An
equivalent Phase Line representation is given in Figure 3b.

4



## Metadata
- Source file: junk_drawer/2_DirectionFieldsAndPhaseLine (1).pdf
- Extracted: 2026-05-18
- Category: other
