# Topic 7 - Crystallographic Computations - 2023 - Notes - no solution (1).pdf

Source: junk_drawer/Topic 7 - Crystallographic Computations - 2023 - Notes - no solution (1).pdf

Category: [[academic-homework]]

## Summary
Topic 7: Crystallographic Computations in 3D Questions we will answer... • What is the distance between any two points in an arbitrary Bravais lattice? • What is the angle between two vectors? • What is a metric tensor and why is it useful to calculating the above? • What is the volume of a 3D Bravais unit cell?

## Full Content
Topic 7: Crystallographic Computations
in 3D
Questions we will answer...
• What is the distance between any two
points in an arbitrary Bravais lattice?
• What is the angle between two vectors?
• What is a metric tensor and why is it useful to
calculating the above?
• What is the volume of a 3D Bravais unit
cell?
Topic 7 -

1

Distance between any point and the
origin

Non-Cartesian

Cartesian

c

a

L
(0,0,0)

a

a

L

(1,1,1)

L

c

(0,0,0)
a

Cubic

(1,1,1)

(1,1,1)

c

Tetragonal

Pythagoras’ theorem works in Cartesian
(orthonormal) reference frames

a

b

(0,0,0)
a

a

b

g

Triclinic

Topic 7 -

2

In-Class Exercise 1
The unit cell of an oxide crystal with a cubic lattice parameter of 4.00 Å contains the following
atoms (the ordered sets are the coefficients of location that define rj):
A at (0,0,0) ; B at (1/2 , 1/2, 1/2);
O at (1/2, 1/2, 0); O at (0, 1/2, 1/2); O at (1/2, 0, 1/2).
(i)

Sketch projection and perspective views of the unit cell, including all atoms that are
within or partially within the cell

(ii) What is the formula unit of this compound?
(iii) Specify the lattice and the basis of this crystal
(iv) The compound is a cubic perovskite belonging to the m3m point group. What is the
space group of this perovskite?
(v) What are the coordination numbers of A and B?
(vi) Determine the A-O and B-O bond lengths
(vii) If A and B are not the same size, which is smaller?
(viii) Specify the sequence of atoms found along the <111> and <110> directions
(ix) Specify the contents of the (200) plane and the contents of the (110) plane
Topic 7 -

3

In-Class Exercise 1 (solution)
a
0,1

a

½

½

0,1
½

0,1
½

0,1

½

A at (0,0,0) ; B at
(1/2 , 1/2, 1/2);
O at (1/2, 1/2, 0);
O at (0, 1/2, 1/2);
O at (1/2, 0, 1/2).

0,1

OB A
A: 8x1/8 = 1
B: 1
O: 6x1/2 = 3

• Formula unit is ABO3 (perovskite)

(corner)
(center)
(face)

• One formula unit per unit cell
• Cubic P with ABO3 basis at
A: (0,0,0), B: (1/2,1/2,1/2), O:
(1/2,1/2,0) (1/2,0,1/2) (0,1/2,1/2)
•

Space group: Pm3m
Topic 7 -

In-Class Exercise 1 (solution)
0,1

½

½

0,1
½

0,1
½

0,1

OB A

½

0,1
https://www.xtal.iqfr.csic.es/Cristalografia/parte_03-en.html

Topic 7 -

5

In-Class Exercise 1 (solution)
(Crystal systems with
orthogonal axes)

O
a

B
A

B atoms have CN = 6 (octahedron)
A atoms have CN = 12 (cuboctahedron)

Topic 7 -

6

In-Class Exercise 1 (solution)
Plane (200)
O
a O

y

OB A

x
<111> = A-B-A
<110> = A-O-A

“A perovskite is any material with the same type of
crystal structure as calcium titanate (CaTiO3),
known as the perovskite structure, or A2+B4+(X2−)3
with the oxygen anion in the face centers.
Perovskites take their name from the mineral, which
was first discovered in the Ural mountains of Russia
by Gustav Rose in 1839 and is named after Russian
mineralogist L. A. Perovski (1792–1856).“
, in Wikipedia (retrieved 13 Sept 2017)

B

O

Plane (110)
A
A
O
a

B

O
A
A
O
a
a2
Q: What is the angle between
<111> and <110?
Q: What is the angle between
(200) and (110)?
Q: What changes if crystal
system is orthorhombic?
Q: What changes if crystal
Topic 7 system is NOT orthogonal?

(Length of a
vector)

Vector Operations

si and ti are expressed
in terms of Miller
indices:
- distance (x, y, z)
- Direction [h k l]

(angle between
two vectors)

Metric tensor,
contains ALL
unit cell info
and units

We need unit cell info
(a,b,c, a,b,g) to compute
actual distances

Non-orthogonal:
Orthogonal:
Cubic:

diagonal matrix
identity matrix a2
Topic 7 -

8

Metric tensor in 3D
c

The metric tensor
allows a wide range
of calculations* to be
performed correctly in
orthogonal and nonorthogonal crystal
systems

L
b
a

a

Most general
case:
triclinic

b

g

The metric tensor contains
all the lattice parameters

*We can compute:
•
•

Define vector
R and metric
tensor

•

Distance between atoms
and bond lengths
(nearest neighbors)
Angle of a bond and
between two directions
Volume of a unit cell

Result is
a scalar
Topic 7 - 9

Metric tensor for all Bravais lattices

Identity matrix  a2

(Crystal systems with
orthogonal axes)

(Crystal systems with
non-orthogonal axes)
Topic 7 - 10

Metric tensor in 3D

c

(1,1,1)

L
b

a

(0,0,0)
a

Length of Triclinic unit cell along [111]:
b

x y z

x
y
z

g

Triclinic

Topic 7 -

11

In-Class Exercise 2
Compute the distance between two atoms
Given: Crystal with lattice parameters {2, 2, 3, 90, 90, 90} contains
atoms at points (1/2, 1/3, 1/4) and (1/3, 1/2, 3/4).
Compute the distance between these two atoms

Topic 7 -

12

In-Class Exercise 3
Compute the angle between atomic bonds
Given: In a cubic crystal with lattice parameter a, an oxygen atom is
present at the position (0, 0, 0); this atom is bonded with two titanium
atoms, located at the positions (1/2, 1/2, 0), and (1/2, 0, 1/2).
Compute the angle between these two bonds

Topic 7 -

15

Metric tensor and dot product

{1, 2, 3} = {x, y, z}

Summation implied

(mixed products = 0)
Topic 7 -

18

c

In-Class Exercise 4
Compute the length of a vector

b

Given: Crystal with lattice parameters {3, 4, 6, 90, 120, 90}.
Compute the length of the main body diagonal

a

a

b

g

{a, b, c, α, b, g}

Topic 7 -

21

In-Class Exercise 5

Topic 7 -

24

Volume of a Unit Cell

c

Mixed vector product

b
a

a
g

Topic 7 - 28

b

Volume of a Unit Cell

Non-Cartesian
Triclinic

Determinant of
a 3x3 matrix
b

a
g

Vertical lines
symbolize
determinant
operation

Tetragonal example:
a=bc; α=b=g=90

c

a

a
Topic 7 -

29

Additional considerations
This is bonus material showing the
necessity for the need for a metric tensor
approach when computing distances in
Cartesian and non-cartesian references
frames:
– Conversion between Cartesian & nonCartesian reference frames
– Example of 2D metric tensor

Topic 7 -

30

Distance between two points in a nonCartesian frame in 2D
P
p/4

L
Q

Pythagoras’ theorem

incorrect
Topic 7 - 31

Distance between two points in a nonCartesian frame in 2D
P
p/4

L
Express the old basis vectors
in terms of the new ones…

Q

Needs to be generalized…

g
Topic 7 - 32

Distance between two points in a nonCartesian frame in 2D
P
p/4

L
Q

Pythagoras’ theorem
Topic 7 - 33

Distance between two points in a nonCartesian frame in 2D
P
p/4

L
Q

Correct

Topic 7 - 34

Metric tensor in 2D

Dot product between basis vectors

Result is
a scalar

Distance between two points, valid in all
non-orthonormal reference frames!

Topic 7 - 35



## Metadata
- Source file: junk_drawer/Topic 7 - Crystallographic Computations - 2023 - Notes - no solution (1).pdf
- Extracted: 2026-05-18
- Category: academic-homework
