# Topic 6 - 3D Symmetry  Space groups - 2023 - Notes - no solution (2).pdf

Source: junk_drawer/Topic 6 - 3D Symmetry  Space groups - 2023 - Notes - no solution (2).pdf

Category: [[academic-homework]]

## Summary
Topic 6: 3D Crystal Symmetries, Point Groups and Space Groups Questions we will answer... • What symmetry elements are found in 3D? • What are the 32 point groups in 3D? • What properties do point groups relate to? • What information does a point group encode? • What are general equivalent positions and how are they calculated from a point group? • What are the 230 space groups?

## Full Content
Topic 6: 3D Crystal Symmetries, Point
Groups and Space Groups
Questions we will answer...
• What symmetry elements are found in 3D?
• What are the 32 point groups in 3D?
• What properties do point groups relate to?
• What information does a point group encode?
• What are general equivalent positions and
how are they calculated from a point group?
• What are the 230 space groups?
• What information does a space group encode?
• How to read and interpret the International
Tables for Crystallography?
Topic 6 -

1

From 1D and 2D to 3D Lattices
•
•

Definition of basis and lattice hold true in 3D exactly as
they do in 2D and 1D
Additional symmetry elements in 3D:
– Point symmetry elements = centers of symmetry, mirror
planes (instead of lines) and inversion axes
– Translational symmetry elements = are glide planes
(instead of lines) and screw axes

•

•

•

 14 3D lattices
(recall: 5 2D plane lattices and 1 1D line lattice)
 32 3D point groups
(recall: 10 2D point groups and 4 1D point groups)

2D example:
Lattice
+
Pt
group

point group = combination of symmetry operations + single point

=

 230 space groups
(recall: 17 2D plane groups and 6 1D line groups)

Plaine
group

space group = combination of point group + lattice translation

Topic 6 -

2

Space Group of Real Materials
-quartz  P3121 (trigonal)
-quartz  P6222 (hexagonal)
Cu, Ag, Au  Fm3m
Cubic perovskites, e.g., BaTiO3, MAPbBr3 Pm3m
Martensitic steel: P42/n
Graphite: P63mc or P63/mmc
Silicon: Fd3m
GaN & SiC: P63mc
Topic 6 -

3

Symmetry Elements in 3D
Symmetry elements in 3D are imaginary objects that can perform symmetry
operations (just like in 1D and 2D). They become symmetry operators when
positioned and oriented.
The primary function of a symmetry element is to provide a reference point about which to
perform the operation

Inversion
Rotations

Side view

Plan view
Mirror plane Mirror plane
Glide plane

Screws

Symmetry elements
positioned on a 3D
unit cell

Rotoinversion
Topic 6 -

Glide plane

Symmetry Operators in 3D
A symmetry operator describes an imaginary action that can be used to
develop a pattern (e.g. lattice point + translation; lattice + diad)
Operators change the position/orientation of an object in space; each operator can be
described mathematically

Seven symmetry operators in crystallography:

Element

– Translation (1D, 2D, 3D)
– Rotation (1D, 2D, 3D)
– Reflection (mirror) (1D, 2D, 3D)
– Inversion (center of symmetry) (2D, 3D)
– Roto-inversion (inversion axis) (3D)
– Glide (translation + reflection) (1D, 2D, 3D)
– Screw (rotation + translation) (3D)
International notation:
O indicates the object
+ indicates O is above page plane
- indicates O is below page plane
 Indicates change of handedness

z

x

x

y
(-x,-y,z)

Operation

+
+

(x,y,z)

+(x,-y,z)
m
 + (x,y,z)
m

- +

(x,y,-z)

(x,y,z)

Topic 6 -

5

m
z=0

Rotation Operators
International notation:
No graphic symbol for n=1 (monad)

diad
triad

tetrad

Rotation takes place around an axis.
Points on axis do not change their
position (aka, special coordinates).
Rotations are proper symmetry operations

hexad
Topic 6 -

6

Reflection/Mirror Plane Operator
Symmetry element: mirror (m)
Operation of a mirror  reflection

y-z mirror plane at x = 0
(x,y,z)  (-x,y,z)
Coma refers to a left-handed
replica for generality

x

Right-handed  left-handed

Reflection is an improper symmetry operation
Topic 6 -

7

Inversion Operator
Symmetry element: center of symmetry at the origin (symbol: i, , o)
Operation: inversion at origin transforms an object at (x,y,z) to (-x,-y,-z)

+

+ and – signs next to the object O refer to
small displacements above and below the
plane of the screen, respectively

Like the reflection, the inversion is an improper operation
and creates a left-handed replica
Topic 6 -

8

Roto-inversion Operators
•
•

Roto-inversion operation rotates an object about its axis, then inverts
the object through a center of symmetry on the axis of rotation
Symbol is the same as rotation, but with a bar above.
Mirror in the plane of the screen

= 3/m
Two objects

3
m

N/m  Mirror plane
3/m normal is || to rotation axis
Topic 6 -

9

Roto-inversion Operators

Note that:
-The direction of the 1 axis is irrelevant (symbol i)
-The axis is equivalent to a reflection plane perpendicular to it
-The axis is equivalent to the product of a threefold rotation by
an inversion:
-The
axis also contains a diad
-The
axis is equivalent to a threefold rotation and a reflection
plane perpendicular to it:
(normal of mirror plane is parallel to triad)
Topic 6 - 10

Point Groups: 32 in 3D
Point Groups arise from the combination of symmetry operators which do
not imply translations.
This means combination of proper and improper axes & planes
intersecting at a single point (Note: intersection point does not move
upon application of the symmetry operation(s)).
Intersecting symmetry operators allow for use of multiple matrix
operations around a common reference frame.
Important: Screws and glides are excluded from point groups because
they imply a translation (Bravais lattice).
The set of crystals belonging to the same point group is called a Crystal
Class and its symbol is that of the point group.
Crystallographic point groups provide a set of math
instructions (symmetry operations) that allow a pattern to
be generated based on a single general coordinate (x, y, z)

A point group is a concise way of listing symmetries of
an object in a pattern.

Topic 6 -

11

Single-Axis Point Groups: 10
Simplest case: presence of one proper or inversion axis
or a combination of these.

10 unique point groups
1,2,3,4,6,

,m, , ,

Hermann-Mauguin
notation of point groups

Which of the 7 crystal systems are these point groups associated to?
Answer: think about the highest symmetry supported by a crystal system
Topic 6 -

12

Proper Rotation Point Groups: 6
Operators that form a group and intersect at
an unchanged point (e.g., center of cube) can
be written as a product (matrix multiplication)
– E.g., the group formed by A, B, and C, can be
written as ABC, where each one is an operation
– Only 6 point groups meet these conditions:
• 222, 223, 224, 226, 233, 234
• 222, 32, 422, 622, 23, 432 (conventional names)

Which of the 7 crystal systems are these point groups associated to?
Answer: think about the highest symmetry and lattice of a crystal system
Topic 6 -

13

Decoding the Crystal System from the
Point Group
1 and 1  Triclinic
2, m and 2/m  Monoclinic
“2” or “m” in first position and three symbols Orthorhombic (e.g. 222, mm2)
“3” in first position  Trigonal (e.g. 3m)
“4” in first position (3 NOT in second position)  Tetragonal (e.g. 4/mmm)
“6” in first position  Hexagonal (e.g. 622)
“3” in second position Cubic (e.g. m3m)

Topic 6 -

14

Combination of Rotations
•

•

Compatibility of rotations & translations is crucial and must be
maintained as we are only interested in operators that can be
combined with one of the 14 Bravais lattice vectors to build a crystal
Point groups can be obtained by combining the five proper rotations.
Defining characteristic:
–
–

The effect of any two operators can be reproduced by a third single operator.
Why? Because any rotation operation will always keep you on a Bravais lattice
E.g., three operations on a cube; A, B and C

A & B are
rotation triads
about body
diagonals
C is a rotation
diad about a line
through the
cube’s face

 AB = C
Important: all three operator axes
intersect at the same point (body center)

Topic 6 -

15

Combination of Improper Operations (1/2):
16 Point Groups
•
•
•

Condition to combining improper operations: final object must
not change handedness  16 point groups
Derived from groups containing proper rotations, assuming that
each proper axis has a perpendicular or parallel inversion axis,
If n-fold rotation || , then
Also:
– When n is even,

where m is a mirror operator

– If n is odd, then

•

E.g., take the group 222 of proper rotations. If two of the three
diads are inversion diads, then it becomes
which has the
conventional name mm2

16 distinct point
groups containing
improper operators

1, 2, 3, 4,
6, 222, 32,
422, 622,
23, 432
Topic 6 -

16

Combination of Improper Operations (2/2):
Details
Now consider that l1 is a proper rotation while l2 is an inversion axis
 l3 has to be an inversion axis

l1

Q

l3

l2
R

P

O
+4

+6
+3
Do not count
redundant pt groups

=mmm
=6/mmm

=3mm

=4/mmm
=43m

+3

Which of the 7 crystal systems are these point groups associated to?
Answer: think about the highest symmetry and lattice of a crystal system
Topic 6 -

17

3D Point Groups
Hermann-Mauguin notation of point groups
10 unique point symmetry groups
6 combinations of symmetry groups
containing only proper operations

16 combinations of symmetry groups
containing improper operations

Total: 32 point groups!
= 32 crystal classes
Topic 6 -

18

32 Point Groups Associated to 7 Crystal
Systems

21

11

(2)
(3)
(3)
(7)
(5)
(7)
(5)
(=32 crystal classes)

A point group which contains an inversion center is centrosymmetric. Crystals with an inversion center cannot
display certain properties such as the piezoelectric effect. Point groups lacking an inversion center (noncentrosymmetric) are divided into polar and chiral types. Chirals only contain (purely) rotational symmetry.
Topic 6 -

19

Non-Centrosymmetric crystals
21 lack center of
symmetry, but only 10 are
polar point groups

BaTiO3 (ABO3) perovskite
Tetragonal 4mm point group

– 1, 2, m, mm2, 3, 3m, 4,
4mm, 6, 6mm
–

–

In a polar crystal there is a direction that
is not transformed in the opposite
direction by any symmetry operation of
the crystal class. That direction is called
the polar axis of the crystal.
There is a general interest in polar and/or
chiral crystals, because some physical
properties of materials, highly desired for
advanced applications:
•
•
•
•
•

Tetragonal P with basis of ABO3
A: (0,0,0), B: (1/2,1/2,1/2+),
O: (1/2,0,0), (0,1/2,0), (0,0,1/2)

Pyroelectricity
Piezoelectricity
Ferroelectricity
Second harmonic generation
Electrooptic effect

Topic 6 -

20

Properties of Non-Centrosymmetric
Crystals
•

•

•

•

Second harmonic generation – a
crystal that produces light with twice
the frequency at that of the incident
light (e.g., green laser pointer)
Piezoelectricity – a crystal that
develops electric charges on
opposite faces when a mechanical
stress is applied (sonar,
microphone)
Pyroelectricity – Crystals that have
a net electric field in the absence of
an electric field. If we can reverse
the direction of polarization with an
external field, then it is also
ferroelectric.
Optical activity – a crystal that
rotates linearly polarized light.

•

Crystals are centrosymmetric
when:
– Inversion center
– Odd rotoinversions (1, 3)
– Even rotation (2, 4, 6) +  m

Topic 6 -

21

Non-Centrosymmetric Crystal Classes

 improper operations
(same handedness)

 multiple rotations
 rotoinversions

All but 432

Halasyamani & Poeppelmeier, Chem. Mater. 1998, 10, 2753. Topic 6 -

22

Decoding the Crystal System from the
Point Group
1 and 1  Triclinic
2, m and 2/m  Monoclinic
“2” or “m” in first position and three symbols Orthorhombic (e.g. 222, mm2)
“3” in first position  Trigonal (e.g. 3m)
“4” in first position (3 NOT in second position)  Tetragonal (e.g. 4/mmm)
“6” in first position  Hexagonal (e.g. 622)
“3” in second position Cubic (e.g. m3m)

Topic 6 -

23

In-Class Exercise 1
Specify the crystal system associated to the following point
groups…
3m

1

m3

2mm

2/m

23

422

43m

222

622

32
Topic 6 -

24

Decoding the Symmetry
Operations from the Point Group

c [001]
90º 90º

a [100]

b [010]

90º

1) Each component in the name refers to a different direction
e.g. 222 refers to an orthorhombic crystal.
Convention: the 1st, 2nd and 3rd positions of the diad indicate
rotations along [100], [010] and [001], respectively (or x, y, z).

222

All diads intercept in the center of the unit cell (point group!)
2) The position of the symbol m indicates the direction to
which the mirror is normal to (x, y, z in case of orthorhombic)

mm2

3) Fractional symbol means mirror plane is normal to rotation
axis (or mirror plane normal is || to rotation axis)

2/m

e.g. 2/m is a mirror plane normal to a diad
4) All tetragonal groups have only one 4 or 4 rotation axis in
the z-direction, listed 1st.
The 2nd symbol/number: symmetry around x, y;
The 3rd: axis in the x-y plane that bisects x and y axes.
Topic 6 -

26

Decoding the Symmetry Operations from the
Point Group
4) In trigonal (3 and 3) and hexagonal systems (6 and 6), the 2nd
symbol refers to the symmetry around the equivalent directions (either
120 or 60 apart) in the plane perpendicular to the 3, 3, 6 or 6 axes.
5) A 3rd component in the hexagonal system refers to directions that
bisect the angles between the axes specified by the 2nd symbol.
6) If there is a 3 in the second position, it is a cubic point group! Rotation
triads along the four body diagonals of the cube; the 1st symbol refers
to the cube axis and the 3rd to the face diagonals.

Topic 6 -

27

Symmetry Directions Encoded based on
Point Group & Crystal System
(2)

,

(3)

,

(3)

,
, ,
,

,

,

,

, ,

,

,

,

(7)
(7)

,
,

,

(5)

, ,

(5)

,

,

,

,

,

Topic 6 -

28

(=32 crystal classes)

,

Point Group Interpretation by Bravais Lattice
Hermann-Mauguin notation:
(used in crystallography, Schoenflies for spectroscopy)
Each component in the point group refers to a different
direction (e.g. 222  diads around x, y, and z)

Crystal system (Bravais):
Orthorhombic
H-M Symbol (point group):

222
mmm

Position of m indicates the direction  to mirror plane
(e.g. mm2  mirror planes  to x and y)
Fractional symbols: the axes of the operators in
numerator and denominator are parallel (e.g. 2/m 
mirror plane normal || to rotation diad)
Topic 6 -

29

Point Group Interpretation by Bravais Lattice
•

Orthorhombic:
3 symbols refer to mutually  x, y, z

c≠a
90º 90º

a

•

b≠a

90º

Tetragonal:
4 or 4 in the z direction (listed 1st for convenience)
2nd symbol refers to mutually  x and y axes
3rd symbol refers to directions in x-y plane that
bisect the x and y axes

c≠a
90º 90º

a

b=a

90º
Topic 6 -

30

Point Group Interpretation by Bravais Lattice
•

Trigonal:
3 or 3 axis as 1st symbol (body diagonal)
2nd symbol refers to symmetry around
equivalent directions 60 apart in the plane 
to 3 or 3

c=a

a

 


b= a

< 120
Topic 6 -

31

Point Group Interpretation by Bravais Lattice
•

Hexagonal:
6 or 6 axis as 1st symbol
2nd symbol refers to symmetry around
equivalent directions 120 apart in the plane
 to 6, 6
3rd component in hexagonal system refers to
directions that bisect the angles between the
axes specified by the 2nd symbol

c≠a
90 90

a

b=a

120

Topic 6 -

32

Point Group Interpretation by Bravais Lattice
•

Cubic:
There is always a 3 or 3 in the 2nd position,
referring to the rotation triad along four body
diagonals
1st symbol refers to the cube axis <100> and
the 3rd to the face diagonals <110>

Topic 6 -

33

In-Class Exercise 2
Draw the following point group symmetries
2/m

mm2

4/mmm

422

622

23

Topic 6 -

34

Identifying the Point Group from the
Crystal and its Symmetries
How to determine a crystallographic point group?
Start by checking where is the highest symmetry:
If no rotational symmetry, then it must be 1, 1 or m (triclinic or monoclinic)
If four triads are present, then it must be a cubic point group
Systematic search of other symmetries  specify which of 5 cubic point groups
(outside scope of MSE 300!)

If neither cubic nor triclinic, then find axis of highest rotational symmetry
If hexad  hexagonal
If single triad  trigonal
If single tetrad  tetragonal
If triad and tetrad  cubic!!
If diad and two are mutually   orthorhombic
If diad  monoclinic

After the crystal system is identified, the presence/absence of  diads
and mirrors specifies which point group it belongs to
e.g.:

M: ,

,

O:

,

,

T: , ,

,

,

,

Topic, 6 -

36

General Positions and Order of Point Group
General Positions
For point group 222 (orthorhombic):
coordinates of initial point (x,y,z)
1 General
that does not lie on a symmetry element
2 Diad along z-axis produces a replica of
initial point at (-x,-y,z)
of
3 Diad along x-axis produces a replica
initial point at (x,-y,-z) and of 2nd point at
(-x,y,-z)
Diad along y-axis produces a replica of
initial point at (-x,y,-z), which is redundant
Thus, general coordinates for 222 are
(x,y,z), (-x,-y,z), (x,-y,-z) and (-x,y,-z)
Because there are 4 general
coordinates, we say the order of the
group is 4

2

3

3

1

y
(x,y,z)

x
The general coordinates
always have the lowest
symmetry and highest
multiplicity

A point group is a
concise way to list
the coordinates of
a pattern

Order: The number of equivalent positions a point group can generate.

Topic 6 -

37

Special Positions
To produce the general positions of the object (i.e. with maximum multiplicity),
the initial coordinate must not lie on a symmetry element
If the initial point lies on a symmetry element  list of coordinates is restrictive
 special positions
Take point group 222 and assume initial point is (0,y,0):
The initial point lies on the diad along y (pattern b)
Diads along x and z produce the same replica (0,-y,0) but the diad along y does
not produce points
Pattern (b) has 2 points instead of 4
Coordinates (0,y,0) and (0,-y,0) represent special positions in the point group 222

General

Special

Can you think of other special positions?

Topic 6 -

38

Planar Projections of Point Groups
Crystallographic point groups provide a set of instructions (symmetry
operations) that allow a pattern to be generated based on a single
general coordinate (x, y, z) as well as special coordinates
A point group is a concise way to list coordinates of the objects in a pattern.
By translating this pattern (or basis) to all points of the Bravais lattice, the
crystal structure can be formed!

We use 2D projections of point groups
Non-cubic point groups: projection along the unique axis of highest
symmetry of 27 non-cubic point groups, with operations carried out in the
plane of the screen
Cubic point groups: axes are inclined to the plane of the screen (more
difficult to depict)

Topic 6 -

39

Planar Projections: Triclinic & Monoclinic
Triclinic

Construction guide

Monoclinic
Order: 1

Order: 2

Inversion

Order: 2

Order: 2

Order: 4

mirror plane normal
to rotation axis Topic 6 -

40

Planar Projections: Orthorhombic

3 symbols refer to mutually  x, y, z

Order: 4

Order: 4

Order: 8
Topic 6 -

41

Planar Projections: Tetragonal

Order: 8
•
•
•

Order: 8

Order: 4

Order: 4

Order: 8

4 (or 4) in the z direction (listed 1st for
convenience)
2nd symbol refers to mutually  x and y axes
3rd symbol refers to directions in x-y plane that
bisect the x and y axes
Order: 8

Order: 16
Topic 6 -

42

Planar Projections: Trigonal

Order: 6

Order: 3
•
•

Order: 6

3 (or 3) axis as 1st symbol
2nd symbol refers to symmetry
around equivalent directions 60
apart in the plane  to 3 (or 3)
Order: 6

Order: 12
Topic 6 -

43

Planar Projections: Hexagonal

Order: 6

Order: 12
•
•
•

6 (or 6) axis as 1st symbol
2nd symbol refers to symmetry around equivalent
directions 120 apart in the plane  to 6 (or 6)
3rd component refers to directions that bisect the
angles between the axes specified by the second
Order: 12
symbol

Order: 6

Order: 12

Order: 12

Order: 24
Topic 6 -

44

Planar
PlanarProjections
Projections: Cubic

•

•

•
•
•

5 groups have multiple triads and tetrads, so no
unique axis of highest symmetry  challenge to
visualize in 2D
Lowest symmetry is the group 23: includes 3
mutually  diads forming a convenient set of axes
for reference
3 diads join at the midpoint of opposite edges of a
tetrahedron
The triads are directed from the 4 vertices of the
tetrahedron to the centers of the opposite faces
Note: 3 elements refer to operations along cube
axes, body diagonals and face diagonals

Order: 12

Order: 24
Topic 6 -

45

In-Class Exercise 3
Indicate visually how the point group below
changes upon addition of an inversion center
2

2/m
zx

x mm2

y
422
Topic 6 -

46

Rotation Operator in 3D
e.g. Tetrad rotation axis || z (i.e. in x-y plane)
 = /2, , 3/2

R

General coordinate: (x, y, z)
Rotation operator:

x
R

z
·

R

R

y

Rotation #1 ( = /2):

Vector-matrix
multiplication:
Tetrad replicates an object at four locations:
(x,y,z), (-y,x,z), (y,-x,z), (-x,-y,z)

Topic 6 -

48

In-Class Exercise 4
Apply a tetrad || z-axis to (1/2,1/4,0):

½

¼
y
(x,y,0)

R

x

Wikibooks

Topic 6 -

49

In-Class Exercise 5
Specify the coordinates of the general equivalent position in the 422 point
group and draw its plane projection.
Given:

1 +

z

x

(x,y,z)

y

x

Topic 6 -

51

Equivalent Positions
In-Class Exercise 6
What point group is created if a center of symmetry is added to 422?
Specify the general equivalent positions in this new group.

Topic 6 -

55

Screw Operators
Combination of rotation or reflection and translation leads to two
additional operators known as the screw and the glide, respectively
•
•
•
•

Combination of rotation + translation ||
Only diad, triad, tetrad and hexad axes can be used
Translation on each rotation must be a rational
fraction of the entire translation
Symbol: Nq, where N is the rotational operator by
2/N and q refers to translation by q/N and q < N

11 possible screw axes:

42

61

Screw operator can be clockwise or counterclockwise.
It is always a proper operation
Topic 6 -

57

Screw Operators
Oblique projections

Plane projections

Topic 6 -

58

Glide Operators
•
•
•
•

•
•

•

Combination of translation + mirror
Must be compatible with translations of Bravais lattice!
Translation components of glide operators must be a
rational fraction of a lattice vector (1/2 or 1/4)
If axis (a, b or c) is || to the translation, it is called an axial
glide; glide planes with translations a/2, b/2, and c/2 are
designated by the symbol a, b and c (according to the axis
of glide)
Diagonal glides are indicated by the symbol n; they have
the translation components a/2+b/2, b/2+c/2 or a/2+c/2
Diamond glides are indicated by the symbol d; they have
the translation components (a+b)/4, (a+c)/4, (b+c)/4.
A d-glide in 3D (a+b+c)/4 is possible in cubic and tetragonal
systems
Translation in a glide is always in the plane of the mirror (g)

Glide is an improper symmetry
operation (opposite congruence)
Axial glide: a, b, c
Diagonal glide: n
Diamond glide: d

Example: m + translation  n or a, etc.
Topic 6 -

59

How do we Get 230 Space Groups?
Step 1: consider one of the 14 Bravais lattices (7 systems + centering operations)
Step 2: combine the point groups consistent with the Bravais lattice type
Step 3: where possible, replace rotations with screws and mirrors with glides
Step 4: remove duplicates and chose conventional names
Not all screws and glides are
consistent with Bravais lattice,
but below are some examples!
P
P, C
P, A, C, I, F
P, I
P

P1

P

P6/m

P63/m

Pm3m

Pn3n

P, I, F

I41, I42, I43

I4

Rotation  screw

Mirror  glide

Point Group + Bravais Lattice

=

Space Group
Topic 6 -

60

How do we Get 230 Space Groups?
Step 1: consider one of the 14 Bravais lattices (7 systems + centering operations)
Step 2: combine the point groups consistent with the Bravais lattice type
Step 3: where possible, replace rotations with screws and mirrors with glides
Step 4: remove duplicates and chose conventional names

For instance, for monoclinic space
groups, the operators compatible are
a diad and a mirror:

Understanding orientation of mirror planes
and glide symmetry is important to
choosing correct glide plane (a, b, c, n, d) Replaced rotation Replaced mirror Topic 6 with screw

with glide

61

How do we Get 230 Space Groups?
When this process is repeated for the seven crystal systems (i.e. triclinic,
tetragonal…), then 230 space groups are generated

These are the standard, internationally recognized Hermann-Mauguin
symbols for space groups
They do not show all symmetries, but a sufficient number to generate all
of the equivalent positions that need to be specified
Remember, space group symbols always begin with a capital letter
indicating the type of lattice centering
Topic 6 -

62

Glides in Space Groups
Pna21

 mm2

n in 1st position
n: diagonal glide
Glide normal || x  plane || to y-z
Or glide plane  x
Translation: +b/2 +c/2

Orthorhombic
z
y

Axial glide: a, b, c
Diagonal glide: n
Diamond glide: d

x

Compatible glides with m in 1st position: b, c, n, d (a)

a in 2nd position
a: axial glide
Glide normal || y  plane || to x-z
Or glide plane  y
Translation: +a/2

Compatible glides with m in 2nd position: a, c, n, d (b)

z

y

a 21

n

x
Pt group

Space group

Topic 6 -

63

Space Groups

2

2
3

13

3
59

Topic 6 -

64

Space Groups

7

68

Topic 6 - 65

Space Groups

5

7

52

5
Total = 32

36
Total = 230

Topic 6 -

66

In-Class Exercise 7
Complete the tables
Space
Group

Crystal
System

Bravais Lattice

Point
Group

Space
Group

P1

Ccc2

P2/m

Ibca

C222

I41cd

Immm

I41/acd

P4/mmm

P322

I42m

R3c

P3m1

P63/mmc

P6m2

Fd3

P432

C2/c

I43m

Iba2

Fm3m

P63mc

P21/m

I213

Crystal
System

Bravais Lattice

Topic 6 -

Point
Group

67

Space Group Diagrams
Triclinic
Diagrams include two parallelograms
Origin is at the top left corner
z-axis is normal to the screen

For instance, consider the diagrams of space group
•
•
•
•
•
•
•

:

Parallelogram on the left shows equivalent positions
Parallelogram to the right shows the relative positions of symmetry elements
In , the primary symmetry element is the inversion center at the origin
The other inversion centers at the edges, corners and center are a consequence
of the translation symmetry
Point 2 is generated by performing an inversion operation at the origin
Unit cell translations of points 1 and 2 generate additional coordinates
Conventionally, only equivalent positions in the same unit cell are reported; in
, there are two only: (x, y, z) and (-x,-y,-z); the latter can be translated into the unit
cell by the vector a+b+c to become (1-x,1-y,1-z), which we write (
) Topic 6 - 69

Space Group Diagrams
Monoclinic
Space group C2
End-centered monoclinic
“C”  lattice point in a-b plane at (1/2,1/2, 0)

Upper diagrams show projection along caxis (rectangular a-b base) and lower
diagrams show view along b-axis

b
“C”

a
a

Equivalent positions for C2:
•

Start with (x,y,z), #1

•

Diad || b  (-x,y,-z), #2  (𝑥̅ , 𝑦, 𝑧̅)

•

C-centering operation (x+1/2, y+1/2, 0) applies to
points 1 and 2  #3 and #4

•

(x,y,z), (𝒙, 𝒚, 𝒛), (x+1/2, y+1/2, z), (1/2-x, y+1/2, 𝒛)

•

Note: It is customary to only note the basis
(points 1 and 2), as C-centering is implicit

c

Topic 6 -

70

Space Group Diagrams
b

Orthorhombic
a
Ambiguity: all 3 symmetry axes do not always
intersect; for instance:
Consider P222  primitive
•
•

•
•
•

(x,y,z), (𝑥̅ , 𝑦, 𝑧), (𝑥̅ , 𝑦, 𝑧̅), (𝑥, 𝑦, 𝑧̅)

We use 2 intersecting diads to generate points 2, 3 and
4 from point 1
The 3rd diad is redundant  3 diads intersect for sake
of internal consistency

Consider P2221
•

General equivalent positions (P222):

Presence of screw diad means the x and y diads do not
intersect at z = 0; diad along y is displaced by z = 1/4
Using screw diad, point 2 is generated from point 1
Using diad along a-axis (at z = 0), point 1 generates
point 3 and point 2 generates point 4
The diad along b-axis must be at z = 1/4 and 3 diads do
not intersect

b
a
General equivalent positions (P2221):
Topic 6 -

71

Space Group Diagrams
Orthorhombic

Pna21 has two types of glide operators (n and a):
•
•
•
•
•

Position of symbols indicates the orientation of the mirrors and screw
The normal of the mirror associated with the diagonal glide plane is along the a axis (in b-c plane); the
translation is || to the b-c plane and has a magnitude b/2+c/2
The axial glide has a mirror whose normal is along b and a translation of a/2
Screw diad does not intersect the glide planes
General equivalent positions: (x,y,z), (𝑥̅ , 𝑦, z+1/2), (x+1/2, 𝑦+1/2, z) and (𝑥̅ +1/2, y+1/2, z+1/2)

Topic 6 -

72

International Tables
Hermann-Mauguin:
•

First, one letter: P, I, F, R, C, B or A
(i.e. Bravais lattices)

•

Second, statement of the essential symmetry
elements of the point group also helps
identify crystal system

•

Reducing the screw and glide leads to point
group

Topic 6 -

73

International Tables
Two particularly useful pieces of
information are projections of the operators
in different orientations (i.e., diagrams) and
tabulated lists of all general and special
positions.

For P2221, the listed positions are:

b
a
General equivalent positions (P2221):

Order of 222
pt group
General positions
Special positions

Name of the different possible sites in each group: Point symmetry of each site
‘a’ is most symmetric site (special position); least
symmetric site (general position) is ‘e’

general positions are left
invariant only for the identity
operation - each space
group has only one general
position;
special positions are left
invariant by the identity
operation and at least one
other operation of the space
group.
Topic 6 -

74

Data Interpretation
Cu
O
La

What you can find in the literature
Qualitative picture

Topic 6 -

75

Data Interpretation

Formula
Space Group
Minimum
parameters

Standard type
of crystal
Number of
molecules
per unit cell
Experimentally
determined
Coordinates of the atoms in one cell (+ multiplicity & Wyckoff)

Topic 6 -

76

Cu

Data Interpretation

4/mmm

O
La

I4/mmm

•
•
•

4 (or 4) in the z direction (listed 1st for convenience)
2nd symbol refers to mutually  x and y axes
3rd symbol refers to directions in x-y plane that
bisect the x and y axes

Space group I4/mmm:
I4, i.e. body centered tetragonal (“4” is in 1st position and “3” is
absent)
‘I’ implies that (1/2,1/2,1/2) must be added to each coordinate 
second half of sites “/m”: mirror plane normal to c-direction

2 x La2CuO4 formula per unit cell = 14 atoms per unit cell
 density = (4MLa + 2MCu + 8MO) / (a2c)

Topic 6 -

77

Data Interpretation Coordinates:

Order:

General

•

a, c, e are the Wyckoff letters (see example on P2221);
a, b, c, d ,e, etc. are all the possible sites; a is for the
most symmetric one (special coordinate 0,0,0); higher
order letters refer to increasingly general coordinates

•

To indicate a position, use Wyckoff letter + multiplicity
(e.g. La in (4e))

•

By convention, positions generated by centering are
not listed, because they are not part of basis.

•

La2CuO4 atoms are clearly in special positions

Topic 6 -

78

Data Interpretation
Step 1: Determine atomic coordinates for all
atoms in the cell and on the borders of the cell

Recall:

4xLa atoms (given X 2) due to centering, I):
(0,0,0.36), (0,0,0.64), (1/2,1/2, 0.86), (1/2,1/2, 0.14)
The sketch is easier with approximate fractions
(0,0,1/3), (0,0,2/3), (1/2,1/2,5/6), (1/2,1/2,1/6)
O(2) coordinates:
(0,0,0.2), (0,0,0.8), (1/2,1/2, 0.7), (1/2,1/2,0.3)
O(1) coordinates:
(0,1/2,0), (1/2,0,0), (1/2,0,1/2), (0,1/2,1/2)
Cu coordinates:
(0,0,0), (1/2,1/2,1/2)

Step 2: Include translation repeats
Cell corners (8x), edges (4x), faces (2x)

Step 3: Draw the unit cell projection, e.g., down
the a axis [100]
Topic 6 -

79

Data Interpretation

4/mmm

Projection 1/2 0,1
down the a
axis

b

0,1
1/2

1/2

0,1
La: (0,0,1/3), (0,0,2/3) +I: (1/2,1/2,5/6), (1/2,1/2,1/6)

0,1
1/2

Cu: (0,0,0) + I: (1/2,1/2,1/2)
O(1): (1/2,0,0), (0,1/2,0) + I: (1/2,1/2, 0.7), (1/2,1/2,0.3)
O(2): (0,0,1/5), (0,0,4/5) + I: (1/2,0,1/2), (0,1/2,1/2)
There are 14 atoms in one unit cell 
42 coordinates + 6 lattice parameters
But these were reduced to four parameters:
2 lattice constants + 2 positions

0,1
c
1/2

0,1

0,1
1/2

0,1

1/2

Topic 6 -

80

In-Class Exercise 8

Topic 6 -

81



## Metadata
- Source file: junk_drawer/Topic 6 - 3D Symmetry  Space groups - 2023 - Notes - no solution (2).pdf
- Extracted: 2026-05-18
- Category: academic-homework
