# Lecture 3.pdf

Source: junk_drawer/Lecture 3.pdf

Category: [[academic-lecture]]

## Summary
Lecture 3 ChE 467/596-012 Polymer Rheology Saad A Khan ChE 598K – Lecture ©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

## Full Content
Lecture 3

ChE 467/596-012
Polymer Rheology
Saad A Khan

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Last Class: Vectors and Tensors
Index Notation

a
2

2

a = a1 e1 + a 2 e2 + a3 e3

1
e2

3

e3

a = ai ei

e1

1

Kronecker delta
3

Dot Product

V. W = Vi ei . Wj ej

1

if i=j

dij =

= Vi Wj (ei . ej)

0
if ij
ei. ej = dij

= Vi Wj dij
= Vi Wi = V1W1 + V2W2 + V3W3
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Tensors
Scalar

a =a

Vector

V = Vi ei

Tensor

T = Tij ei ej

(Dyad)

= T11 e1 e1 + T12 e1 e2 + T13 e1 e3

+ T21 e2 e1 + T22 e2 e2 + T23 e2 e3
+ T31 e3 e1 + T32 e3 e2 + T33 e3 e3

T11 T12 T13 


T  T21 T22 T23 
T31 T32 T33 
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Food for Thought
Two vectors: a and b
Your thoughts on:

ab

ab

axb
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Vectors & Tensors (last class)
t ( n )  n T

Do not use same index

n T = ni ei . Tjk ej ek Take dot product of nearest vectors
n T = ni ei . Tjk ej ek
Nesting convention

= ni dij Tjk ek = ni Tik ek or nj Tjk ek (repeated indices)
= ni Ti1 e1 + ni Ti2 e2 + ni Ti3 e3
= ( n1 T11 + n2 T21 + n3 T31 ) e1

+ ( n1 T12 + n2 T22 + n3 T32) e2
+( n1 T13 + n2 T23 + n3 T33) e3
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Tensor : Tensor
A and B are tensors, What is A : B?
2

A : B = Aij ei ej : Bkl ek el
1
Nesting convention

= Aij ei . Bkl djk el
= Aij Bkl djk dil
= Aij Bji or Alk Bkl

(Scalar)

Sum over i=1,2 and 3; j=1, 2, and 3
(9 Components)
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Tensor : Tensor, cont’d
A and B are Tensors, What is A : B
 A11

 A21
 A31

A12
A22
A32

A13    B11 B12 B13 
A23    B21 B22 B23 
A33   B31 B32 B33 

 A ij B ji

= A11 B11 + A12 B21 + A13 B31
+ A21 B12 + A22 B22 + A23 B32
+ A31 B13 + A32 B23 + A33 B33
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Invariants of Tensor T
First Invariant

Second Invariant

IT  trace (T )
 T11 + T22 + T33

1
IIT  ( IT ) 2  trace (T  T ) 
2

Third Invariant
T11 T12 T13 


IIIT  det(T )  det T21 T22 T23


T31 T32 T33 
=T11 (T22 T33 -T23T32 )
- T12 (T21T33 -T31T23 ) + T13 (T21T32 -T31T22 )
All invariants –scalar & independent of coordinate system
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Gradient ()


ei
xi



=
e1 
e2 
e3
x1
x2
x3
For Example gradient of density r

r
 r
ei
xi
r
r
r
=
e1 
e2 
e3
x1
x2
x3
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Operational Order !

Examples:
A. A
Order =
A:A
Order =
ChE 598K – Lecture

Operation

Order

Vector
Tensor
Scalar
Dot Product
Double Dot Product
Cross Product

1
2
0
-2
-4
-1

V. A
Order =
VW
Order =

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Operational Order !

Examples:

Operation

Order

Vector
Tensor
Scalar
Dot Product
Double Dot Product
Cross Product

1
2
0
-2
-4
-1

V. A

A. A
Order = 2+2-2=2 (Tensor)

Order = 1+2-2=1 (Vector)
VW

A:A
Order = 2+2-4=0 (scalar)

Order = 1+1=2 (Tensor)
= Vi Wj ei ej

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

So far…..
• Concepts of Vectors & Tensors
Index notation
Dot and double dot products
Orders of vector, tensor & various operation

 Properties of Stress Tensor T
Symmetric
Normal stress – diagonal elements

Shear stress – off-diagonal elements
Scalar invariants of tensor
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Class Exercise
A●B = ? (write simplified version in index notation)
A●B = Aij ei ej● Bkl ek el
1

= Aij ei Bkldjk el
= Aij Bjl ei el
Now this is a tensor of the form
1 2

 4 5
7 8
ChE 598K – Lecture

3
6 
9 

What is term 2?

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Class Exercise
A●B = Aij Bjl ei el
this is the term with e1e2 in it

= A1j Bj2 e1 e2

Now this is a tensor of the form
1 2

 4 5
7 8

3 What is term 2?
6 
9 

= [A11 B12 + A12 B22 + A13 B32 ] e1 e2

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Stress Tensor
Consider sample
• under pressure or at ambient
condition
• no flow

Static condition
p

p
Can support only normal stresses

0
 p 0
T   0 p 0 
 0
0 p 

p

T  pI,

1 0 0 
I  0 1 0 
0 0 1 

Identity or Unit tensor
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Stress tensor & flow
T  pI  
Total stress tensor

Viscous stress tensor

  0 (when no flow)

Advantage –isolate isotropic or hydrostatic pressure effects
For normal stress measurements, want to subract “p” effect
Use normal stress difference, not normal stress:

T11  T22   11   22
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Deformation description
2

Shear Flow:
1

F
 21
A
 vo 
21    
 h 

Stress 

V0
Force, F

A= area

h

  vis cosity
 vo 
  = shear rate = 
 h 

How do we get shear rate? Form of shear rate?
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Deformation description (kinematics)
Stress  vis cosity * rate of change of strain
 ds 
 
 dt   Rate of change of strain
s
h
ds
 vo
2
dt
v
Rate of change of strain  o
1
h

V0

Force, F
h

3

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Deformation description (kinematics)

V0

s

v
Rate of change of strain  o
h
In general:
v1
12  
3
x 2
in TENSORIAL form
    = 2 D
ChE 598K – Lecture

Force, F
h

2

1

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Stress Tensor, cont’d
  = 2 D
2D    Rate of stra in t ensor
 ij

 v j vi 
 

 x x 
j 
 i

v  (v1 ,0,0)
Vo
v1 =
x2
h
ChE 598K – Lecture

V0

s

Force, F

h

2
1

3

0

 21
 0

12
0
0


 0

0
 v1

0  

x 2

0 
 0


v1
x 2
0
0

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved


0


0

0

of

Rate of Strain Tensor
 ij

 v j vi 
 

 x x 
j 
 i

11  ?
 32  ?

Vo
v1 =
x2
h

12  ?
 21  ?

Find the different
components of the rate of
strain tensor.
ChE 598K – Lecture

 21  ?

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Rate of Strain Tensor
 ij

 v j vi 
 

 x x 
j 
 i

Vo
v1 =
x2
h

Shear rate not a function of
position –
homogeneous flow
ChE 598K – Lecture

11 

v1 v1
v

2 1 0
x1 x1
x1

v 2 v3
 32 

0
x 3 x 2

12 

v 2 v1 v1


x1 x 2 x 2

 21 

v1 v 2 v1


x 2 x1 x 2

 21  12 

v1 V0


x 2
h

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Transition to new topic
•

End of Quick Overview

•

Start on Chap 3 of Dynamics of Polymeric Liquids

•

Flow types & Material Functions

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Material Functions
Inherent properties of materials
Serves to classify material

Used in developing constitution equations
Provides information – microstructural or molecular level

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Material Functions, cont’d
Newtonian Fluids
•
•

(oil, water, ….)
r, (constant)
• Independent of flow type and shear rate
 characterizes Newtonian fluids

Complex Fluids
•
•

ChE 598K – Lecture

Need many material properties to be fully
characterized
Material properties are functions of flow type or
flow rate
©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Flow Type
Shear Flow

Steady

Dynamic

Extensional Flow

Unsteady

Biaxial

Uniaxial

Transient
Steady

ChE 598K – Lecture

Planar

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

Unsteady

of

Features of Shear Flow
• Family of surfaces that slide past each
other

h

2
2’

2

lo

l

V0

s

Force, F

1
3

Vo   lo

1

=


.
2  2 2 t2
o
o
.

o t

(for larger times)

• Distance between neighboring fluid
particles change linearly with time
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Extensional Flow
Uniaxial

Planar

Biaxial

lo

lo

lo

lo

lo

lo
l

1
l

ChE 598K – Lecture

lo

lo
lo
l
1
l

l

lo2
l

l
lo

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Extensional Flow
vx  x,

 is the extension rate

vx  
d

dt
ln  t ,

t 0



o

o

exp(t )

• Neighboring particles move relative to each
other at an exponential rate  “strong” flow
• Extensional Flows are volume preserving
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

What kind of flow are these?

Flow through pipe

Flow through tapered pipe

END OF CLASS
Flow between concentric cylinders
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Stress tensors in different flows
Extension :
  p   xx
T = 0

 0

0
 p   yy
0


0 

 p  zz 
0

normal stresses of interest

Txx  Tyy   xx   yy

Shear:
  p   xx
T =   xy

 0

For either flow,

 yx
 p   yy
0


0 

 p  zz 
0

Tyy  Tzz   yy   zz

 xz   yz  0
i.e., only one shear component non-zero
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Material function- steady shear flow
3 material functions characterize a material
(  ) =

1 (  ) =

 2 () =

ChE 598K – Lecture

 xx   yy


2

yy  zz


2

=

 yx


Viscosity

N1
= 2


First Normal Stress Coefficent

N2
2

Second Normal Stress Coefficent

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Steady Shear Flow
• x(1) Flow Direction

• y(2) Direction of Velocity Gradient

V0

dxs

• Z(3) Neutral Direction

h

2

Force, F

1
3

3 Stresses of Interest in Steady Shear Flow


 yx

Shear Stress



N1   xx   yy

First Normal Stress Difference



N 2  yy  zz

Second Normal Stress Difference

ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Shear Viscosity
Viscosity (), poise

10

1

o
10

0

(power-law)

Zero shear viscosity

Slope (0.4-0.9)
10

-1

10

-2

( cc )
10

-3

10

ChE 598K – Lecture

Shear-Thinning region
Industrially relevant

-1

10

0

10

1

Shear Rate (  ) , s

-1

10

2

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

10

3

of

Viscosity (), poise

Temperature effect
10

1

10

0

T

1

T >T
10

-1

10

-2

10

-3

10

-4

2

1

( c )1
10

-1

10

0

( c ) 2
10

1

Shear Rate

( ) , s

10
-1

2

10

3

As Temperature 
o  and ( c )
l  (Longest relaxation time of material  1/( c ) )
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Molecular Weight Distribution
Viscosity (), poise

10

1

Sharp transition ~ narrow Mw distribution
10

10

0

-1

Broader transition ~ larger Mw distribution
10

-2

10

-1

10

0

10

1

Shear Rate
ChE 598K – Lecture

.
()

10
-1

2

10

3

,s

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of

Shear Viscosity ()

 versus Normal Stress Coefficient
10

1

10

1

10

0

10

0

10

-1

10

-1

10

-2

10

-2

10

-3

10

-3

10

-1

10

0

10

1

10
.
-1
Shear rate () ,(s )

2

10



1

3

Slope of normal Stress Coefficient is steeper
than that of viscosity
ChE 598K – Lecture

©2002 Professor Saad A Khan, North Carolina State University, All Rights Reserved

of



## Metadata
- Source file: junk_drawer/Lecture 3.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
