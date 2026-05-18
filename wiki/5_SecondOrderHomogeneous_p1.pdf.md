# 5_SecondOrderHomogeneous_p1.pdf

Source: junk_drawer/5_SecondOrderHomogeneous_p1.pdf

Category: [[academic-homework]]

## Summary
MA341 Applied ODE’s Lecture Notes 5 Second Order ODE A general form of second oOrder ODE is given by F (x, y, y 0 , y 0 ) = 0

## Full Content
MA341
Applied ODE’s
Lecture Notes

5

Second Order ODE

A general form of second oOrder ODE is given by
F (x, y, y 0 , y 0 ) = 0

or

y 00 = f (x, y, y 0 )

The number of initial conditions required for uniqueness of second order ODE is
two:
y(x0 ) = y0 , y 0 (x0 ) = y00
Example 5.1. Solve
y 00 = (y 0 )2 .
Denote v = y 0 , substitute into equation to get
v0 = v2
dv
= dx
v2
1
− = x + C1
v
1
v=−
x + C1
Thus
y0 = v = −

1
,
x + C1

and we integrate again to get
Z
y=−

1
= − ln x + C1 + C2 .
x + C1

M. Medvinsky

5.1

Applied Differential Equations

Linear Second Order ODE
y 00 + p (x) y 0 + q (x) y = g (x)

Example 5.2. Some famous second order ODEs:
1. Legender’s equation:

1 − x2 y 00 − 2xy 0 + α (α + 1) y = 0
2. Bessel equation:

x2 y 00 + xy 0 + x2 − v 2 y = 0
Theorem 5.3. Suppose p(x) q(x), g(x) are continuous function on (a, b). Let x0 ∈
(a, b), then there is a unique solution on (a, b) that satisfies the equation
y 00 + p (x) y 0 + q (x) y = g (x) ,
and the initial conditions
y (x0 ) = y0 , y 0 (x0 ) = y 00 ,
where y0 , y 00 are given constants.
5.1.1

Homogeneous second order linear equation

Homogeneous equation has g = 0, so consider
y 00 + p (x) y 0 + q (x) y = 0
Definition 5.4. Given functions f1 (x), f2 (x), . . . , fk (x) defined in I = [a, b]. A sum
of the form
k
X

ci fi (x) = c1 f1 (x) + c2 f2 (x) + · · · + c3 fk (x),

i=1

is called a linear combination of f1 (x), f2 (x), . . . , fk (x).

2

ci ∈ R

M. Medvinsky

Applied Differential Equations

Example 5.5. Consider ex , sin x, ln x. Example of linear combination:
3ex + 6 sin x + ln x.
Theorem 5.6. Superposition principle. Given y1 (x), y2 (x) solutions to the second
order linear homogeneous equation, then a linear combination of solutions y1 (x), y2 (x):
y (x) = c1 y1 (x) + c2 y2 (x)
is also solution to the equation.
Proof:
y (x) = c1 y1 (x) + c2 y2 (x)
y 0 (x) = c1 y 01 (x) + c2 y 02 (x)
y 00 (x) = c1 y 001 (x) + c2 y 002 (x) .
Hence
y 00 + p (x) y 0 + q (x) y = (c1 y 001 + c2 y 002 ) +p (x) (c1 y 01 + c2 y 02 ) +q (x) (c1 y1 + c2 y2 )
{z
}
|
{z
}
|
{z
}
|
y 00

y0

y

= c1 (y 001 + p (x) y 01 + q (x) y1 ) +c2 (y 002 + p (x) y 02 + q (x) y2 ) = 0
|
|
{z
}
{z
}
=0

=0

Example 5.7. Consider y 00 − y = 0.
1. Show that y1 = ex and 2 = e−x solves the equation.
x

−x

2. Show that cosh x = e +e
2

also solves the equation.

Solution: Substitute all the options into equation to see.
Example 5.8. Consider y 00 − y = x.
1. Show that y = xsolves the equation.
2. Show that y = −2x doesn’t solve the equation.
3. Explain why this is not a contradiction to the superposition principle (5.6).
3

M. Medvinsky

Applied Differential Equations

Solution: Substitute all the options into equation to see. This example doesn’t
contradict the superposition principle since the equation in this example is not homogeneous.
Theorem 5.9. Assume p(x), q(x) are continuous functions in an open interval I,
and y1 (x), y2 (x) are solutions of
y 00 + p (x) y 0 + q (x) y = 0.
If
y1 (x0 ) y 02 (x0 ) − y 01 (x0 ) y2 (x0 ) 6= 0,
then
y (x) = c1 y1 (x) + c2 y2 (x)
is a general solution of the equation.
Definition 5.10. Wronskian:
W (y1 , y2 , x) = [W (y1 , y2 )] (x) = W (y1 , y2 ) (x) = W1,2 (x)
!
y1 (x) y2 (x)
= det 0
y 1 (x) y 02 (x)
= y1 (x) y 02 (x) − y2 (x) y 01 (x)
Similarly,




f1 (x)

···

fk (x)

 0
 f 1 (x)
W (f1 , . . . , fk , x) = det 
 ..
 .

···


f 0k (x) 
.


(k)
fk (x)

(k)

f1 (x) · · ·

Theorem 5.11. Let p(x), q(x) be continuous functions in an open interval I, and
y1 (x), y2 (x) are solutions of
y 00 + p (x) y 0 + q (x) y = 0.
If
W (y1 , y2 , x) 6= 0,
4

M. Medvinsky

Applied Differential Equations

then
y (x) = c1 y1 (x) + c2 y2 (x)
is a general solution of the equation.
Example 5.12. Consider y 00 + y = 0. Show that y1 = sin x and y2 = cos x solves the
equation. Next, show that the Wronskian doesn’t vanish and write a general solution.
y 01 = cos x, y 001 = − sin x ⇒ y 001 + y1 = − sin x + sin x = 0.
Similarly,
y 02 = − sin x, y 002 = − cos x ⇒ y 002 + y2 = − cos x + cos x = 0.
Thus,

W (y1 , y2 , x) = y1 y 02 − y 01 y2 = − sin x sin x − cos x cos x = − cos2 x + sin2 x = −1 6= 0,
hence the general solution is
y (x) = c1 cos x + c2 sin x.
Definition 5.13. The solutions
y1 (x) , y2 (x)
that satisfies
W (y1 , y2 , x) 6= 0
called a fundamental set - a basis of the solution and any other solution can be
created by linear combination of them.
Theorem 5.14. Abel’s Formula. Let y1 (x), y2 (x) be solutions to
y 00 + p (x) y 0 + q (x) y = 0,

5

M. Medvinsky

Applied Differential Equations

where p(x), q(x) be continuous functions in an open interval I, then
W1,2 (x) = Ce−

R

p(t)dt

Furthermore,
• The constant C is independent of x, but depends on
y1 (x) , y2 (x) .
• Wronskian is vanishing if and only if C = 0.
Example 5.15. Consider
2x2 y 00 + 3xy 0 − y = 0.
Rewrite it as
y 00 +

3x 0
1
y
−
y = 0.
2
2
2x
2x
|{z}
p

• Show that y1 = x1/2 , y2 = x−1 solve the equation.
• Calculate Wronskian using determinant formula:
W1,2 = y 01 y2 − y1 y 02
 1
= |{z}
x1/2 −x−2 − x−1/2 |{z}
x−1
| {z } |2 {z } y
y1
2
0
y2


=− x

−1.5

y0 1

1
+ x−1.5
2

= −1.5x−1.5

6



M. Medvinsky

Applied Differential Equations

• Calculate Wronskian using Abel’s formula
W1,2 (x) = ce−

Rx

p(t)dt

R 1
3

= ce− 2

t

dt

3

= ce− 2 ln x = celn x

−3/2

= cx−1.5

for the given solution c = −1.5.
• Assume now that only y1 = x1/2 is known, find y2
cx−1.5 = W1,2 = y 01 y2 − y1 y 02
1
x1/2 y 02
= x−1/2 y2 − |{z}
|2 {z }
y1

y0 1

Solve it for y2 to get a first order ODE:
1
x1/2 y 02 = x−1/2 y2 − cx−1.5
2
1
y 02 − x−1 y2 = −cx−2 ,
2
which solution is of course y2 =−1 (verify!).
Definition 5.16. The functions
f1 (x) , f2 (x) , ..., fn (x)
are linearly dependent if there is a vanishing linear combination
c1 f1 (x) + c2 f2 (x) + ... + cn fn (x) = 0
where not all ci = 0. Otherwise, i. e. in the case the linear combination above is
vanishing only when all ci = 0, they are linearly independent dependent.

7

M. Medvinsky

Applied Differential Equations

Intuition: If we can express one of the functions as linear combination of the others
fj (x) = c1 f1 (x) + ... + cj−1 f2 (x) + cj+1 f2 (x) + ... + cn fn (x)
then this set is linearly dependent.
Example 5.17.

• {2x, 4x} is linearly dependent.

• ex , e2x is linearly independent.
Theorem 5.18. If
f1 (x) , f2 (x) , ..., fn (x)
are linearly dependent then
W1,2...,n (x) = 0, ∀x ∈ I,
but,
W1,2...,n (x) = 0, ∀x ∈ I
it is insufficient condition to conclude that
f1 (x) , f2 (x) , ..., fn (x)
are linearly dependent. However, if y1 (x), y2 (x) are solutions to second order linear
homogeneous equation, and
W1,2...,n (x) 6= 0, ∀x ∈ I
then y1 (x), y2 (x) are linearly independent.
Example 5.19. Consider the following functions

f1 (x) =

f2 (x) =


1 + x 3

x≤0

1

x>9


1

x≤0

1 + x 3

x>9

8

M. Medvinsky

Applied Differential Equations
f3 (x) = 3 + x3

• The functions f1 ,f2 ,f3 are linearly independent in (−1, 1):
If −1 < x ≤ 0, assuming there are c1 , c2 , c3 that are not all zeros and satisfies
c1 f1 (x) + c2 f2 (x) + c3 f3 (x) = c1 (1 + x3 ) + c2 + c3 (3 + x3 ) = 0
gives
c1 + c3 = 0
c1 + c2 + 3c3 = 0.
If 0 < x < 1, the same coefficients c1 , c2 , c3 should also satisfy
c1 f1 (x) + c2 f2 (x) + c3 f3 (x) = c1 + c2 (1 + x3 ) + c3 (3 + x3 ) = 0,
which gives
c2 + c3 = 0
c1 + c2 + 3c3 = 0.
All together we got
c1 + c3 = 0
c2 + c3 = 0
c1 + c2 + 3c3 = 0.
The only solution to this system is c1 = c2 = c3 = 0, hence the functions are
linearly independent.
• However, W (f1 , f2 , f3 )(x) = 0:
1 + x3 1 3 + x3
W (f1 , f2 , f3 )(x) =

x≤0

3x

2

6x
9

2

0

3x

0

6x

=−

3x2 3x2
6x

6x

=0

M. Medvinsky

Applied Differential Equations

Similarly,
1 1 + x3 3 + x3
2

W (f1 , f2 , f3 )(x) = 0

3x

0

6x

x>0

3x

2

=

3x2 3x2

6x

6x

6x

= 0.

Hence,
W (f1 , f2 , f3 )(x) = 0, ∀x ∈ R.
5.1.2

D’Alembert’s Order Reduction Method

Consider
y 000 + 2y 00 − 3y 0 + y = 0.
Assume y1 is a know solution to this equation. Consider solution in the form
y = v (x) y1 (x) .
Differentiate it twice to get
y 0 = v 0 y1 + vy 01
y 00 = v 00 y1 + v 0 y 01 + v 0 y 01 + vy 001 = v 00 y1 + 2v 0 y 01 + vy 001
y 000 = v 000 y1 + v 00 y 01 + 2v 00 y 01 + 2v 0 y 001 + v 0 y 001 + vy1000
(3)

= v 000 y1 + 3v 00 y 01 + 3v 0 y 001 + vy1
Substitute into equation:
0 = y 000 + 2y 00 − 3y 0 + y

= (v 000 y1 + 3v 00 y 01 + 3v 0 y 001 + vy1000 ) + 2 (v 00 y1 + 2v 0 y 01 + vy 001 ) − 3 (v 0 y1 + vy 01 ) + v (x) y1 (x)
= v 000 y1 + (3y 01 + 2y1 ) v 00 + (4y 01 − 3y1 + 3y 001 ) v 0 + (y1000 + 2y 001 − 3y 01 + y1 ) v
|
{z
}
=0

10

M. Medvinsky

Applied Differential Equations

Substitute now u = v 0 to get a second order ODE
0 = u00 y1 + (3y 01 + 2y1 ) u0 + (4y 01 − 3y1 + 3y 001 ) u
or
u00 = −

3y 01 + 2y1 0 4y 01 − 3y1 + 3y 001
u −
u
y1
y1

11



## Metadata
- Source file: junk_drawer/5_SecondOrderHomogeneous_p1.pdf
- Extracted: 2026-05-18
- Category: academic-homework
