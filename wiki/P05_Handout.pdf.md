# P05_Handout.pdf

Source: junk_drawer/P05_Handout.pdf

Category: [[academic-lecture]]

## Summary
Prof. V. Amendola Physical Chemistry of Materials LM in Materials Science Physical Chemistry of Materials P05: Magnetic properties of materials

## Full Content
Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Physical Chemistry of Materials
P05:
Magnetic properties of materials

Magnetic terms.[Mazzoldi, Strobl]
In the treatment of magnetism in a material three main quantities can be identified:1
H : the magnetizing field, i.e. applied from the outside
B : magnetic induction, i.e. the magnetic field present inside the material
M : magnetization.
Magnetization M represents the density of magnetic moments per unit volume in a material. In
analogy to polarization P, which in general (but not always) develops by application of an external
electric field, magnetization in general (but not always) also results from the application of an
external magnetic field H. Therefore, M will be proportional to the applied field with a coefficient
of proportionality equal to the magnetic susceptibility m.

M = mH
Since M and H are two tensors of 1st rank, m will be a symmetric 2nd rank tensor.2
By analogy to the relative dielectric constant r = /0 for dielectric properties, relative magnetic
permeability (r) is used to describe the magnetic properties of a material.

B =  H = 0  r H
where3

r =


0

The relationship between r and m is

r = 1 + m
whereby

(

(S.I.)

)

B = 1 +  m 0 H

(S.I.)

1

In analogy to what will be seen in P06 for dielectric properties by introducing E, D and P.
Again, m symmetry derives for the same reasons that will be shown in P06 about electrical susceptibility e and .
3
The unit of measurement of magnetic permeability is H/m, where it is recalled that the Henry H = V.s/A is the unit of
measurement used for electrical inductance.
2

vincenzo.amendola@unipd.it
www.chimica.unipd.it/LASP

15/11/2025

P05

So there are four ways in which the resulting magnetic induction B in a material can be defined:4

B = H
B =  r 0 H
B = 0 H + 0 M

(

)

B = 1 +  m 0 H

The units of measurement of the physical quantities of interest for magnetism are shown in the
following table:

4

Sometimes, the units of measurement in the S.I. system are preferred to those c.g.s., which, however, are still found in
old texts and in scientific works not harmonized with the trend most shared internationally.

2

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Note: units named after people should be capitalized, although this is not the case in this table.

Angular momentum and magnetic momentum.[Atkins]
3

P05

Magnetism is a phenomenon that requires quantum mechanics to be described, as a classical system
would have no magnetic properties, even if immersed in a magnetizing field.
At the atomic or molecular level, the magnetic properties of a material can be traced back to three
sources:5
-

spin (electronic or nuclear)

-

the electron orbital angular momentum

-

the variation of the electronic orbital angular momentum due to the effect of the magnetizing
field.

Each angular momentum is associated with a magnetic moment  proportional to it. For example,
given the spin angular momentum ( s ) for an isolated electron, the orbital angular momentum ( l )
for an isolated electron6, and the spin angular momentum ( I ) for a nucleus, one can write:

s  s
l  l
I  I
The constant of proportionality is called the gyromagnetic ratio () and is proportional to the inverse
of the mass of the object with angular momentum:

 electronic (e):
e = −

e
2me

 nuclear:

 = gI

e
2M p

where the nuclear g factor (gI) ranges from about 6 to about –6 and is tabulated for each nucleus.
So for an isolated electron you have  e  1 me and for a proton you have   1 M p . In the case of
the magnetic moment associated with the spin angular momentum, a corrective factor g (called "gfactor"7) is required with respect to the case of orbital angular momentum:

 spin = g e s
 orbital =  e l
 atomico =  I
In matter, these three sources of magnetism mean that the magnetic behavior of materials can be
divided into the following 5 categories:
5

Nuclear magnetic moments are about 10-3 times less intense than electronic ones.
For electrons in atoms, capital letters (S, L) will be used instead.
7
g is 2 for a free electron and 1 for an electron with zero spin and nonzero orbital angular moment, see Landè eq. later.
6

4

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Diamagnetism[Strobl]
Materials defined as diamagnetic are essentially "nonmagnetic", in the sense that they do not exhibit
magnetic behavior relevant for practical applications,
and diamagnetism takes place only in the presence of
an

external

magnetic

field.

In

addition,

the

diamagnetic response in nature is extremely weak in
intensity, compared to the magnitude of the magnetizing field.
In general, magnetism originates from electric currents (from electric charges subject to
acceleration), and this applies both to "macroscopic" currents within conducting materials, and to
"microscopic" currents associated with electron motion in individual atoms. In most cases, the
magnetism due to "microscopic" currents is self-compensating and does not generate any effect
outside the atom. However, this situation changes if a magnetic field is applied from the outside,
because it induces a distortion of the electronic distribution at the atomic level, such that a magnetic

5

P05

response is observed by the material even at the macroscopic level, due to the spontaneous tendency
of the materials to oppose the external magnetizing field.
This phenomenon, known as diamagnetism, therefore consists in the appearance of an atomic
magnetic moment in the opposite direction to the external field, and only in the presence of it.
Quantitatively, in diamagnets the relative magnetic permeability is just below 1

r =


 0.99999 →  m =  r − 1  −10 −5
0

It should be noted that any material generates a diamagnetic response in the presence of a
magnetizing field, however this response is relevant only when other forms of magnetism
(paramagnetism, ferromagnetism, etc.) are not present, given its weak intensity.
This condition occurs in particular when the atoms that make up the material have completely full
orbitals (that is, they are devoid of unpaired electrons to which it is possible to associate a net spin
moment). Typical examples of these materials are:
-

inert gases

-

certain molecules (H2O, organic molecules)

-

Certain oxides and ionic solids (Al2O3)

-

Noble metals (Au, Cu, Ag) and some transition metals (Hg, Cd, Zn, etc.)8

-

graphite

-

frogs...

Langevin's model for diamagnetism.[Kittel, Strobl]
Although diamagnetism is a purely quantum mechanical effect, it can
also be explained quantitatively by Langevin's semiclassical model.
According to Larmor's theorem, the electrons of an atom immersed in
a magnetic field B are subject to a precession with frequency
L =

eB
(S.I.)
2m

which, according to the principle of magnetic induction9, involves the
existence of a current called the Larmor precession current
 1 eB 
I = (− Ze )
 (S.I.)
 2 2 m 

which is equivalent to the product of the charges concerned for the frequency of revolution.

8

The electronic configurations are [Hg] = [Xe] 4f 14 5d10 6s2, [Cd] = [Kr] 4d10 5s2 and [Zn] = [Ar] 3d10 4s2.
The principle of magnetic induction states that, if a magnetic field is applied to a conducting circuit, a "transient"
electric current develops with a direction determined by Lenz's law, so as to oppose the external magnetic field.
9

6

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

In this case of an electron orbiting the nucleus, the current is not transient as predicted by the
principle of magnetic induction according to classical electromagnetism, but persists as long as the
field is present.
The magnetic moment associated with this current is obtained by multiplying the current itself by
the area of the circuit on which the motion occurs. Assuming that the circuit has radius  (area A
=   2 ):
Ze 2 B 2
 a = IA = −
 (S.I.)
4m

where me is the mass of the electrons, Z is the number of electrons in the atom, which are assumed
to orbit all in the same circuit (hence why the average value of the circuit radius is used  ) and at
the same Larmor frequency.
By the effect of Lenz's law, the direction of the magnetic moment will be such as to oppose the
external field.
By convention the axis along which the magnetic field is located is identified with the z-axis, which
will be the axis perpendicular to the surface A. So  it coincides with the average distance of the
electrons from the axis of rotation:

 = r⊥
Since atoms with complete electron shells, as is the case with diamagnetic elements, have charge
distribution with spherical symmetry,
x2 = y2 = z 2

which allows you to write the average position of the electrons as
r 2 = x2 + y2 + z 2 = 3 x2 = 3 y2 = 3 z 2

and the average distance of the electrons from the axis of rotation as
 2 = r⊥ 2 = x 2 + y 2 =

2 2
r
3

from which

a = −

Ze 2 B 2
r (S.I.)
6m

This leads to Langevin's law for magnetic susceptibility in diamagnetism:

M = N a

N a
NZe 2 2

→

=

=
−

r
M
M
dia
0
0
 m =  0 
B
6m
H
B

(S.I.)

7

P05

where N is the number of atoms per unit volume, and use has been made of

B = 0 H + 0 M  0 H
since m << 1 → r  1 and M is very small.
The quantum mechanical theory introduces the interaction of the magnetizing field with the
electrons as a small perturbation to the Hamiltonian of the system and, solving the problem with
perturbation theory, arrives at the same result as Langevin's law.
The main limits of this model are related to the existence of closed electron shells, so in the case of
metallic materials in which free electrons are present it is no longer valid, and to the hypothesis of
spherical symmetry of the electron shell, for which in the case of molecules it is necessary to resort
to an expression of dia taking into account both the contribution of the electrons of the inner shells
(inner) and that of the valence shell participating in molecular bonds with non-spherical symmetry
(bond)

 dia =  inner +  bond
Paramagnetism.[Kittel]
For what has been said in the previous paragraphs, if at the atomic level, the electron orbitals are not
completely full or the spins are not balanced, the result is a total non-zero angular momentum J ,
or for which
J

2

=  2 J ( J + 1)  0 → J  0

then there will be a permanent magnetic moment proportional to J :
a  J

If it is assumed that there is no interaction between the microscopic magnetic moments, in the
absence of an external magnetizing field the
magnetic moments are randomly oriented, that is,
the material has zero net magnetization and is "nonmagnetic".
However, in an external field, the magnetic
moments align with the field, amplifying it (albeit
by a small amount compared to the magnetizing field itself).
Thus, the magnetic susceptibility of paramagnetic materials is positive ( > 0, r > 1) and the
relative magnetic permeability typically varies between 1.00001 and 1.01.

8

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Typically, molecules consist of atoms with closed electron shells, so J is zero, but there are
exceptions where paramagnetic behavior is found:
-

materials that contain atoms, molecules or point defects associated with the presence of an odd
number of electrons;

-

molecules with ground state of triplet (e.g. oxygen molecules, biradicals);

-

materials containing atoms or ions with partially filled 10inner electron shells (e.g. some
transition metals and related compounds such as Cr, Cr2Cl3, MnSO4, Al), rare earths;

-

some materials with conduction electrons such as metals.

Paramagnetism associated with spin and orbital angular momentums.
The magnetic moment of an atom or ion can be written as:

 a = g e J = −

g B
J


where
-e is the gyromagnetic ratio
- The total angular momentum operator is given by:

J = L + S
-  is the Bohr magneton (m is the mass of the electron):

 B = − e  =

e
= 9.274 10 −24 J T
2me

whose value is close to the magnetic spin moment of a free electron, for which J = 1/2 and g =
2.0023.
- g is the g-factor defined by the Landé equation:
g = 1+

J (J + 1) + S (S + 1) − L(L + 1)
2 J (J + 1)

It is observed that g = 1 if J = L and g = 2 if J = S.
The Landè equation holds in cases of only "LS coupling" between L and S in an atom, i.e. when
there are no external factors that influence the interaction between the two angular momentums,
such as the presence of a "crystalline field" (see below) that cancels the contribution of orbital
angular momentum, or the interaction with angular momentum. of other neighboring atoms. For
example, the Landè equation applies very well to rare earths, whose paramagnetism is due to the
presence of unpaired electrons in the f-shells, which are too internal to participate in the molecular
bond and be affected by crystal field effects.
10

"Internal" means that they are not necessarily involved in the formation of molecular bonds leading to the formation
of closed electron shells (S = 0, L = 0).

9

P05

Curie's Law for Paramagnetism.[Kittel]
In the presence of an external magnetic field B0 , the "classical" energy of a magnetic moment is
given by:
E = −   B0

Similarly, the Hamiltonian of the quantum mechanical problem is:

Hˆ = − ̂  B0
I can therefore calculate the magnetic moment energy of the three examples seen above for isolated
electron or generic nucleus in the presence of the magnetic field:

s : E = − g e s  B0 = − g ems B0

l : E = − e l  B0 = − e mz B0

I : E = −I  B0 = −mI B0
To simplify writing, the energy associated with electronic magnetic moments can be expressed as a
function of the Bohr magneton  B :

s : E = − g e s  B0 = g B ms B0

l : E = − el  B0 =  B mz B0
Similarly, the energy associated with the magnetic moments of the nuclei can be expressed as a
function of the nuclear magneton  N :

N =

 
gI

=

e
= 5.051  10 − 27 J T
2M p

I : E = −I  B0 = − g I  mI B0
In general, the energy associated with a magnetic moment in the presence of a magnetic field is
g B
 g B 
U = −  a  B = − −
J  B =
m J B = g B m J B





where the projection of J along the axis of the magnetic field will be given by

J z = mJ
with

mJ = J ,(J − 1),...,−(J − 1),− J
Then the initially degenerate 2J+1 levels are separated into energy by the magnetic field.

10

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

In the simple case where we have J = 1/2 (for example for a free electron with S = 1/2 and L = 0),
we can identify only two states with populations N1 (mJ = -1/2) and N2 (mJ = +1/2) given by
Boltzmann's statistics:
−

Ui

e kT

Ni =
e

U
− 1
kT

+e

U
− 2
kT

N

with
U 1 = −1  B = −

1
g B B = −U 2
2

So, having
a = − g

B


m J =

1

1
g B B
2
mJ = 1 / 2

U2 =

1
g B
2

 1  1 
E =  −  −   g B B = g B
 2  2 
1
U1 = − g B B
2
mJ = −1 / 2

B

−1

One can express magnetization as
M = (N 1 − N 2 ) a = N a
x=

a B
k BT

2

e x − e−x 

e x + e−x 
 → M = N a tanh(x )




When x << 1 (i.e. at high temperature and/or for low external magnetic fields, since a is always
small), we have
tanh(x) ≈ x
therefore

N a2 B
M
k BT
As shown in the figure, the separation of the energy
levels of an electron in the presence of an external
magnetic field B increases with the modulus of B (by
convention, the z axis is assumed parallel to B and with
the same direction).
For an isolated electron, the magnetic moment a has
opposite sign to the spin J (= S). Thus, in the lower energy state, the magnetic moment is parallel to
the external field.
Such a separation in energy will correspond to a different population of the two levels, in thermal
equilibrium at the temperature of the system. Macroscopically, the magnetization is proportional to
the difference between the two curves.
11

2

P05

In the case of a generic atom with a total angular momentum J, in the presence of an external
magnetic field it will have (2J + 1) equally spaced energy levels. One can then express the average
magnetic

moment

using

Boltzmann

statistics:
 gmJ  B B 

k BT 
mJ = J

a =
−J
 gmJ  B B 

exp −

k BT 
mJ = J

−J

 − m g exp −
J

B

This summation can be calculated exactly
and leads to the Brillouin function BJ(x):
BJ ( x ) =

2J + 1
 (2 J + 1)x  1
 x 
coth
coth
−

2J
2J

 2J
 2J 

such that

 a = gJ B BJ (x )
x=

gJ B B
k BT

So what
M = NgJ B B j (x )

In fact, for S = 1/2 we have

B

1
J=
2

(x ) = 1 + 1 coth (1 + 1)x  − 1 coth x  = 2 coth(2 x ) − coth(x )
1



1

 1

1

and being
1
1 + tanh(x )tanh(x )
= coth(x + x ) =
tanh(x + x )
tanh(x ) + tanh(x )

you have

1 + tanh(x ) tanh(x )
1 + tanh(x )
1
1 + tanh(x ) − 1
B 1 (x ) = 2
− coth(x ) = 2
−
=
= tanh(x )
J=
tanh(x ) + tanh(x )
2 tanh(x )
tanh(x )
tanh(x )
2
2

Under ordinary conditions x<<1, and one can expand the coth in power series:
coth(a ) =

1 a a3
+ −
+ ...
a 3 45

Truncating the series expansion at the 2nd term, one arrives at:

12

2

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

 2J + 1
 (2 J + 1)x  1
 x 
coth
coth
−
 
 2J
 2J
 2 J 
 2J

 a = gJ B 

 2J + 1  2J
 1  2 J  2 J + 1  1 (2 J + 1)x  1  1 x 

 −
 gJ B 

+

−

 =
(
)
2
J
2
J
+
1
x
2
J
x
2
J
3
2
J
2
J
3
2
J









 1 (2 J + 1)2

1 4J 2 + 4J + 1− 1 
1 1
J + 1 gJ B B
= gJ B 
x
−
x
=
gJ

x  = gJ B
B
2
2 
2
3 (2 J ) 
3 J k BT
4J
3

 3 (2 J )
g 2  B2 B
= J (J + 1)
3k B T
which corresponds to a magnetization (N is always understood as the number of paramagnetic
centers per unit volume):

M = N  a = NJ (J + 1)

g 2  B2 B
3k B T

If we consider that

B = 0 H + 0 M  0 H
since m << 1 → r  1 and M is very small, then one can write Curie's
law for paramagnetism

 Curie =  0

g 2  B2
Np 2  B2 C
M
  0 NJ (J + 1)
= 0
=
B
3k B T
3k B T
T

where p is called the effective number of Bohr magnetons:
p = g J (J + 1)

1/ 2

Since  corresponds to the magnetic moment of a free electron, the
meaning of p is to indicate the magnitude of the actual atomic magnetic
moment in units .
C is Curie 's constant of the material:

C = 0

C=

Np 2  B2
3k B

Np 2  B2
3k B

(S.I.)

(C.G.S.)

and determines the magnitude of the paramagnetic response, depending on the density of
paramagnetic centers for the square of their effective number of Bohr magnetons.

13

P05

Effective Magneton Numbers p for Trivalent Lanthanide Group Ions
(Near room temperature)
Ion

Configuration

Ground level

pcalc=
g[J(J+1]1/2

pexp

Ce3+

4f15s2p6

3F
5/2

2.54

2.4

Pr3+

4f25s2p6

3H
4

3.58

3.5

Nd3+

4f35s2p6

4I

9/2

3.62

3.5

Pm3+

4f45s2p6

5I

4

2.68

-

Sm3+

4f55s2p6

6H
5/2

0.84

1.5

Eu3+

4f65s2p6

7F
0

0

3.4

Gd3+

4f75s2p6

8S

7/2

7.94

8.0

Tb3+

4f85s2p6

7F
6

9.72

9.5

Dy3+

4f95s2p6

6H
15/2

10.63

10.6

Ho3+

4f105s2p6

5I

8

10.60

10.4

Er3+

4f115s2p6

4I

15/2

9.59

9.5

Tm3+

4f125s2p6

3H
6

7.57

7.3

Yb3+

4f135s2p6

2F
7/2

4.54

4.5

The trivalent ions of the lanthanides11 are distinguished by an electron configuration equivalent to
that of [Xe] plus a variable number of electrons in the 4f orbitals. The ionic radius varies very little,
having a maximum for Ce3+ at 1.11 Å and a minimum at 0.94 Å for Yb3+ (known as "lanthanide
contraction"), due to the fact that the 4f shell is quite internal and generally not affected by the
formation of chemical bonds.
Dy3+, Ho3+ and Er3+ are the lanthanides with the most intense paramagnetic response, but the order
of magnitude is the same for everyone.
At room temperature, for all lanthanides, except Eu3+ and Sm3+, the agreement between the p
obtained experimentally by applying Curie's law and the theoretical one is very good. For Eu3+ and
Sm3+ the disagreement is due to the population of states with spin J at higher energy than the
ground state, which is possible because the difference in energy with the ground state is comparable
with the thermal energy at room temperature (to which the measurements refer).12

11

According to IUPAC, lanthanides, along with Sc and Y, make up the "rare earths" group. In the table, promethium
lacks the experimental result as it is not found in nature on Earth (its spectral lines have been detected in the light of
some stars).
12
The presence of multiple spin configurations is due to the spin orbit coupling effects between L and S, which lead to a
multiplet of J states. In Eu3+ and Sm3+ at room temperature, other states with J other different from that of the ground
state are also populated.

14

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

The value of p in the case of transition metals of the 4th period is very different from the
lanthanides: 13 the theory fails to predict the correct value, except in the case in which it is assumed
that the orbital angular momentum L is zero, so that only the spin contribution to the total atomic
angular momentum remains. For the rest, the values of p are of the same order of magnitude as that
of the lanthanides.

Effective Magneton Numbers for Iron Period Ions
Ion

Configuration

Ground
level

pcalc=
g[J(J+1]1/2

pcalc=
2[S(S+1]1/2

pexp

Ti3+, V4+

3d1

2D
3/2

1.55

1.73

1.8

V3+

3d2

2F
2

1.63

2.83

2.8

Cr3+, V2+

3d3

4F
3/2

0.77

3.87

3.8

Mn3+, Cr2+

3d4

5D
0

0

4.90

4.9

Fe3+, Mn2+

3d5

6S

5/2

5.92

5.92

5.9

Fe2+

3d6

5D
4

6.70

4.90

5.4

Co2+

3d7

4F
9/2

6.63

3.87

4.8

Ni2+

3d8

3F
4

5.59

2.83

3.2

Cu2+

3d9

2D
5/2

3.55

1.73

1.9

Because of ions close to atoms, shell d is polarized and J is no longer a good quantum number. In
fact, the 3d shell in the metals of the 4th group is not internal like the 4f in the lanthanides, and this
causes the d orbitals to suffer from the intense electric field due to the surrounding ions in the
crystal. This spatially inhomogeneous electric field is called the "crystalline field".
For example, in the case of an ionic crystal with orthorhombic symmetry, the solution of the
Laplace equation

 2 = 0
where  is the electrostatic potential, leads to a variable electric field with the position in the cell as

Ecf (x , y , z ) = e (x , y , z ) = Ax 2 + By 2 − ( A + B )z 2
where A and B are two constants.
The crystalline electric field has two effects:
-

the L-S coupling fails, so J is no longer a valid quantum number;

-

the 2L+1 levels associated with each L are no longer degenerate, but there is a splitting in
energy. In fact, the interaction of the electron charge distribution of the 2L + 1 levels with the

13

The elements of the periodic table can be grouped by "period" or by "group". The 4th period is also called the iron
period.

15

P05

charges of the crystalline field (for example with cations or anions arranged along some specific
directions), can be energetically more favorable or less favorable. The figure shows the
hypothetical (simple) case of a shell with L = 1 in a uniaxial crystalline field due to the presence
of two cations arranged along the z axis, so the pz orbital will be energetically favored due to
the greater proximity of the electric charge to the cations.

This splitting leads to a lower contribution of the orbital angular momentum to the overall magnetic
moment of the atom, because inside a crystal the electric field is non-central, that is, it is not
directed towards the center of the atom where the positive nucleus is located, and in this situation
the projection of L along a certain direction z (Lz) is on average zero, that is, there is the
"quenching" of angular momentum. In the presence of an external magnetic field along the z
direction, the Lz component is zero and will remain the only spin angular momentum, if any, to
contribute to the atomic magnetic moment a.
The presence of spin orbit interactions between S and
L leads to a slight modification of the g-factor
compared to the case in which L is completely
neglected, so g > 2 for full 3d shell over half, g = 2
for half-filled 3d shell, and g < 2 for 3d shell less than
half full.
The comparison of the theoretical magnetization
calculated by the expression leading to Curie's law,
and the experimental results for lanthanide salts or
transition metals indicates the validity of the theory,
once the quenching of the orbital angular momentum
is taken into account.14
14

The trend of the magnetic moment per magnetic center in the figure is linear for B/T small as per Curie's law, and
then saturates when the ratio B/T increases, as expected by the complete expression as a function of the coth, expected
when the alignment of all the spins of the system is reached.

16

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Pauli's paramagnetism.[Kittel, Ziman]
Conduction electrons in metals are, to a first
approximation, modelable as free electrons, each
of which can be associated with a magnetic
moment but = B. From this it could be assumed
that metals have paramagnetic behavior, but
experimentally it is verified that Curie's law is
not applicable, as the magnetization of nonferromagnetic

metals

is

independent

of

temperature (see figure).
Pauli's

theory

describes

the

paramagnetic

response of conduction electrons in a material
and relies

on the Fermi-Dirac distribution to

correct Curie's theory, based on the fact that, in
the conduction band of metals, the orientation of
electronic magnetic moments along the magnetic field is not always possible because this would
correspond to the occupation of already filled electronic levels. from other electrons of the same
band. Only electrons in the levels near the Fermi EF energy, within an energy range of the order of
thermal quantum kBT, will have the ability to switch from a more energetic to a less energetic spin
configuration, aligned with the external magnetic field.
On the basis of this consideration, it can be inferred that only a fraction equal to T/TF of the total
number of conduction electrons N will contribute to susceptceptibility
N '

k BT
N
k BTF

where
TF =

EF
kB

kBT

so the magnetization can be written as
M = N '  a = N ' J ( J + 1)
1  1  22  B2 B
= N '  + 1
=
2  2  3k BT

g 2  B2 B
=
3k BT

kBTF

EF

17

P05

N ' a2 B
a2 B T Na2 B
=
N
=
k BT
k BT TF
k BTF
which actually turns out to be independent of temperature.
A more rigorous expression of the Pauli magnetization can be derived if one assumes to be at
absolute 0, and expresses the concentration of electrons with magnetic moment parallel to the
magnetic field by the integral of the Fermi-Dirac distribution D:
E

N =

1 F
D(E +  a B )dE
2 − a B

where the argument of the density of states D is increased by the energy of the magnetic moment in
the presence of B, since at absolute 0 the occupation of the conduction band extends beyond EF by a
quantity +aB. In fact, as shown in the figure below, the electronic states with magnetic moment
parallel to B will be energetically stabilized by a factor
U  = −a  B = −

1
g B B = −  a B
2

while those with magnetic moment antiparallel to the field B will experience an increase in energy
by a factor
U  = −a  B = +

1
g B B = +  a B
2

although the Fermi level for the two electron subpopulations remains the same.
The factor 1/2 takes into account the fact that only half of the states at a given energy, those with
magnetic moment parallel to the field, must be considered in the integral.
If one assumes that, in the vicinity of EF, the density of the states is approximately uniform for an
interval a, then one can approximate N↑ as
E

N 

1 F
1
D(E )dE + D(EF ) a B

2 0
2

The calculation of N↓ will be in analogy
E

E

1 F
1
1 F
N  =  D(E − a B )dE   D(E )dE − D(E F ) a B
2 0
2
2 + a B
so one can express the magnetization as
E
 1 EF

1
1 F
1
M = (N  − N  ) a =   D(E )dE + a BD(EF ) −  D(E )dE + a BD(EF )  a
2

2
2 0
2
 0

2
=  a D(EF )B

The density of states at the Fermi energy for a gas of free electrons is

18

Prof. V. Amendola

D (E F ) =

Physical Chemistry of Materials

LM in Materials Science

3N
3N
=
2 E F 2 k BTF

from which

M para =

3 N a2
B
2k BTF

known as Pauli spin magnetization.

E

1/2D(EF)
2aB

½ D(E)
(a //)

½ D(E)
(a anti //)

To the magnetization due to Pauli paramagnetism, in metals must also be added the magnetization
due to the diamagnetic response of the conduction electrons, which, for a gas of free electrons,
Landau has shown to be equal to –1/3 of the paramagnetic contribution:

1 3 N a2
M dia = −
B
3 2k BTF
for which it turns out

N a2
M = M dia + M para =
B
k BTF
There are also additional contributions due to the
- diamagnetism of atomic cores
- the structure of the conduction band
- some effects related to electron-electron interaction.
These effects can increase the resulting magnetization by up to 75% (case of Na).

19

P05

Ferromagnetism.[Kittel]
Atoms of ferromagnetic materials, such as paramagnetic materials, possess a permanent magnetic
moment.
In contrast to paramagnetic materials, in which spin moments or net orbital moments are aligned in
random directions in the absence of an external magnetic field, in ferromagnetic materials the
presence of unbalanced spin moments leads to the formation of permanent magnetization even in
the absence of an external magnetic field .
Typical examples of these materials are Fe in its phase  (BCC), Co, Ni, and Gd.

H=0

The table above refers to the magnetic properties of materials in the form of a single element and in
their thermodynamically stable phase. In particular, only three elements are ferromagnetic at room
temperature (Fe, Co and Ni), while Gd has a Curie temperature of 293 K. However, the formation
of new compounds (such as metal alloys or the formation of oxides) in some cases leads to
magnetic properties of a different type.
It is interesting the case of Ru, paramagnetic in the HCP phase, but which can become
ferromagnetic if forced into a metastable tetragonal phase with a body centered, as in the case
shown in the figure, where a nanometric film of Ru has grown epitaxially15, in order to induce the
strain necessary to stabilize the tetragonal phase (as indicated by the XRD and TEM / STEM
measurements).
This film has a saturation magnetization of 148 emu/cm3 at room temperature and 160 emu/cm3 at
10 K. By increasing the thickness of the film, there is relaxation of the strain and a consequent
dilution of the magnetization. The figures below show the characterization of the tetragonal Ru
structure by STEM analysis of a sample dissected along the direction [001] of the Al 2O3 substrate:
15

Nature Communications, volume 9, Article number: 2058 (2018).

20

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

(a) STEM image annular bright field (ABF) of the multilayer. The bar scale is 10 nm. (b) Highangle annular dark field (HAADF) STEM at the Mo–Ru interface, with the inset showing the
HADDF STEM for the direction [111] of the Ru. The distortion of the lattice is evidenced by the
dashed black line. The bar scale is 2 nm. (c) HAAADF STEM zoom of a Ru grain edge. The bar
scale is 1 nm.

The maximum possible magnetization for these materials is saturation magnetization (Ms), usually
reported per unit volume (in A/m):

M s  =  a N  = Am 2 13

M s = a N

m

or per unit mass of the material or magnetic centres only (in A m2/kg)16:
M s' = a N

1



M s ' =  a N  1  = Am 2 13 m
 

3

m kg

It corresponds to a magnetic field of saturation Bs present inside the material even if the external
magnetizing field is zero.
Some typical magnetization values for single magnetic center in

a

Fe

Co

Ni

B

2.22

1.72

0.6

metallic Fe, Co and Ni are:
The exchange interaction.[Ziman]
At the level of classical electromagnetism, the interaction energy between two magnetic dipoles m1
and m2 placed at a distance r is
16

In a generic magnetic material, composed of several elements, the magnetic centers are only the elements responsible
for the magnetic response. For example, in a FeZn alloy, the magnetic centers are the atoms of Fe.

21

P05

UD 

m1  m2
r3

However, classical interaction energy is not sufficient to
account for ferromagnetism, i.e. the fact that in
ferromagnetic

solids

the

magnetic

moments

of

individual atoms spontaneously align with each other.
For example, if we assume a typical magnitude for the
atomic magnetic moment m ~ 10-29 Wb m (the Weber symbol Wb - is the S.I. unit of the magnetic flux, with 1 Wb/m2 = 1 T) and r ~ 1 Å, we get UD ~ 1023

J which corresponds to the thermal quantum at a temperature of ~1.3 K: above this temperature

the thermal agitation would prevent any magnetic ordering.
Heisenberg and Dirac have shown that ferromagnetism, or the tendency of atomic magnetic
moments to order spontaneously even in the absence of a magnetizing field, is the consequence of a
quantum mechanical process attributable to the minimization of Coulomb interactions between the
electric charges to which the spins responsible for the magnetic moment are associated.
Through this quantum theory, it is possible to arrive at an exchange energy between magnetic
moments that is comparable with the Coulomb energy of interaction between two electric charges
placed at the same distance:

UC =

e2
4 0 r 2

If one assumes r ~ 1 Å as done above, gets U C  10 −18 J , which corresponds to the thermal
quantum at a temperature of 105 K.
Qualitatively, the theory is explained by the advantage that one has from the point of view of the
Coulomb repulsion to have electrons with spins aligned instead of paired: in the first case, in fact,
the electrostatic repulsion is lower.
Heisenberg model[Ziman]
According to Heisenberg's model, the Hamiltonian of interaction (or Hamiltonian of exchange
energy) between the Si and Sj spins of two atoms (to which the angular momenta S i and S j )
correspond can be written as:

H ex = −2 JS i  S j

22

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

where J is the exchange integral, a quantity related to the overlap of the charge distribution of atoms
i and j, and usually negligible when the interaction occurs at the level of thirds or sometimes even
close primes.
If we consider the simple case of a system with
two spins (such as a hydrogen atom with two
electrons), the eigenfunction of the system will
have a different structure depending on whether
the spins are oriented in an antiparallel (singlet) or
parallel (triplet) way. In fact, by Pauli's principle,
for electrons (fermions) an antisymmetric spin

Energy of Coulomb
repulsion higher

Energy of Coulomb
repulsion lower

function (singlet) must correspond to a symmetric orbital wave function of the type

 s (r1 , r2 ) =







1
1 (r1 )2 (r2 ) + 2 (r1 )1 (r2 )  (1)  (2 ) −  (2 )  (1)
2

while a symmetric spin function (triplet) corresponds to an antisymmetric orbital wave function, of
the type



 (1) (2 )
1


 as (r1 , r2 ) =
1 (r1 )2 (r2 ) − 2 (r1 )1 (r2 )   (1)  (2 ) +  (2 )  (1)
2


  (1)  (2 )







Where i are the single-electron orbital wave functions, and  and  the spin functions "up" and
"down" for electrons 1 and 2 with coordinates r1 and r2.
A wave function is antisymmetric if the exchange of coordinates r1 of 1 with coordinates r2 of 2
leads to a sign change of the function itself, and if r1 = r2 is posed, the wave function is zero. This
means that there is no probability of finding the two electrons with the same spin in the same
position at the same time (which represents the statement of Pauli's principle), while this does not
apply to the two electrons with antiparallel spin.
It follows that the electrostatic energy of the system depends on the orientation of the spins, and the
difference in energy between the two different orientations is precisely the exchange energy.
One can write the energy associated with the two electrons in the parallel or antiparallel spin
configuration as

E = I 1 + I 2 + K12  J 12
Where you have +J12 for the singlet and –J12 for the triplet. Therefore, if J12 is positive, the lower
energy level is for the triplet configuration:

E = I 1 + I 2 + K12 − J 12
23

P05

The shape of J12 is such that the parallel alignment of the spins lowers the energy of:
J 12 =

e2

1

 (r ) (r )
 (r ) (r )d r d r
4 
r −r
*
1

1

*
2

0

3

2

2

1

1

1

2

3

1

2

2

where there is a ~1/r dependence which, integrated, leads to the ~1/R2 dependence mentioned above
about the classical Coulomb repulsion energy.
The Weiss model.
In 1907, Weiss developed a theory in which the presence of an effective field within ferromagnetic
materials is assumed, such as to generate spontaneous spin ordering.
On the atomic scale, the magnetic moments of ferromagnets are assumed to be due to spin angular
momentum alone, due to the quenching of orbital angular momentum from the crystalline field. In
fact, Fe-period elements or Gd in its metallic form exhibit ferromagnetism, thus external shells
electrons are involved, which are subjected to the crystalline field effects.
Assume therefore to have a paramagnet with an N concentration of spins S: if the spins tend to
align, then in ferromagnetic materials we can postulate the presence of an interaction between spin,
which can be treated as a real magnetic field called BE exchange field (or Weiss field or molecular
field). Since thermal agitation is opposed to spin ordering, the exchange field must be quite intense,
with values close to 103 T, or about 104 times higher than the fields associated with naturally
occurring magnetic moments.
The "classical" energy of atomic magnetic moments  a = p B will be affected by an overall field
U m = − a  (Ba + BE )

and the MT torque felt by the dipole (favorable to its
orientation in the direction of the field) will be
M T =  a  (Ba + BE )

where Ba is the magnetic field in the material net of BE,
which is not a true magnetic field that obeys Maxwell's
equations.
The resulting magnetization in the material, on the dimensional scale where all magnetic moments
are aligned,17 will clearly depend on the intensity of BE, and in Weiss' theory it is assumed that the
two quantities are directly proportional:

BE = M
where  is called the molecular field coefficient or Weiss coefficient, and is independent of T.
17

As will be seen below, this happens within the individual magnetic domains.

24

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

At the phenomenological level, ferromagnetism can be explained very well by Weiss theory,
although the origin of a high Weiss field is not accessible by the theory itself.
In the paramagnetic phase, the magnetization can be written as18
M =  p (Ba + BE ) (c.g.s.)

0 M =  p (Ba + BE ) (S.I.)
that is, the applied field will induce a magnetization which in turn will induce a Weiss field that will
help induce a certain magnetization.
At

the microscopic level,

the self-consistent relationship between the Weiss field and

magnetization is:19

  a ( Ba +  M ) 
exp
0  k BT  cos sind
M = N  a = N a

  a ( Ba +  M ) 
0 exp k BT  sind


If one assumes that the material in the paramagnetic phase can be described by Curie's law, then the
susceptibility is
p =

C
T

Substituting in M yields

C 

C
M C T
=
→
T  → M = ( Ba +  M ) →
T
B
T
T
−

C
a
BE = M 

p =

=

M
C
=
(c.g.s.)
Ba (T − C )

From this relation it is observed that the susceptibility diverges to TC = C, so one can write the
Curie-Weiss law in the following form

=

C
T − Tc

where

Tc = C
from which

=

Tc k BTc
1
=
per S =
2
C N B
2

18

It is also assumed in this case that B =  0 H +  0 M   0 H since m << 1 → r  1 and M is very small.

19

See the derivation of the Debye equation in P07.

25

P05

and for a generic S you get

=

Tc
3k BTc
=
2
C Ng S (S + 1) B2

Below Tc there is ferromagnetic behavior.
For Fe, Tc = 1063 K (experimental), a = 2.2 B (experimental), and N = 8.54 1028 m-3 from which
is ~ and a Weiss field of 103 T.
The exchange integral J is directly related to Tc, since it determines the intensity of the interaction
between atomic magnetic moments and thus establishes the threshold beyond which thermal
agitation prevails over the spontaneous tendency to order. Assuming that the magnetic center
interacts only with its first neighbor z in a crystal, it is possible to write
J

3k BTc
2 zS (S + 1)

The susceptibility for temperatures above the Curie temperature.
The figure on the side shows the reciprocal of susceptibility per gram of Ni ( is the density)20 near
the Curie temperature of the metal (358 °C), measured experimentally (white circles). The dashed
line is a linear extrapolation of the high-temperature
section, where it is seen that the intercept corresponds

1

to a higher value of Tc.



=

T − Tc
C

As a first approximation, for T >> Tc the Curie-Weiss
law can be corrected in the form
=

C
T −

where  > Tc.
At temperatures close to Tc, however, the Curie-Weiss law satisfactorily describes the behavior of
ferromagnetic materials, but the detailed calculation provides a dependency such as:



C
(T − Tc )

With a "critical" exponent  ~ 1.2 – 1.6,21 as indicated in the table:
20

Being  m = M / H , if we use magnetization per unit ("mass magnetization") [M] = Am 2/kg and [H] = A/m, derive

[] = m3/kg, which is the "mass susceptivity" (see table at the beginning of the chapter).
21
See the meaning of the critical exponent in the 2nd order phase transitions described by the Ginzburg-Landau theory
in P07.

26

Prof. V. Amendola

Physical Chemistry of Materials

Metal



Tc (K)

Fe

1.330.015

1043

Co

1.210.04

1388

Ni

1.350.02

627.2

Gd

1.30.1

292.5

2

1.630.02

386.5

CrBr

1.2150:02

32.56

CrO

3

LM in Materials Science

Magnetization at temperatures below Curie temperature.
The Weiss model also allows to derive the dependence of spontaneous magnetization in a
ferromagnet at varying temperature between 0 K and TC.
Curie's law was obtained by assuming that the argument of the hyperbolic cotangent in Brillouin's
expression was x << 1, and truncating the power series expansion of the coth at the second-order
term.
Using instead, the complete Brillouin expression for the magnetization of atoms with S = 1/2, and
replacing B with only the exchange field BE =  (i.e., omitting the applied magnetic field, so as to
consider the spontaneous ordering of magnetic moments), we have
M = N a tanh(x )

  a M 
 B


x= a
M = N a tanh
k BT
 k BT 

B = BE =  M 


Using small sizes as follows:

M

N a 
m
→ m = tanh 

k T
T
t 
t = = B2 
Tc N a  
m=

we arrive at an expression for reduced magnetization that can be solved graphically by reporting m,
which is independent of T, and tanh(m/t), which obviously varies with reduced temperature. For t <
1, i.e. T < Tc, solutions are possible, from which the theoretical value of M is derived.
In this way we derive the theoretical curve of M vs T shown in the figure on the side (solid line) for
the Ni (S = 1/2). The experimental data (white circles) are discreetly reproduced from the
experimental trend.

27

P05

Theoric
Experimental

It is clearly observed that M  0 for Tc  T as expected for a continuous phase transition of the
2nd order in which the order parameter is M. [Strobl]
As the temperature decreases, there will be an increasing number of magnetic moments aligned
with each other, according to
  a M 



M = N  a = N a

 exp k T  cos  sin d
0

B

  a M 
exp
0  kBT  sin d


The above expression can be written in a more
compact way if we introduce the Langevin function
L, in analogy to what we will see in P07 for the
Debye equation (orientation of polar molecules in an
external electric field), for which we arrive at
  M 
 = N a L( )
M = N a L a
 k BT 
 M
= a
k BT

At 0 K, the saturation magnetization coincides with the density of atomic magnetic moments for the
magnetic moment itself:

M (T = 0 ) = N a = NnB  B
with the magnetic moment nBB which should correspond to an integer number of Bohr magnetons,
since g ~ 2 for an electron, and dependent only on the spin angular momentum which is responsible
for the atomic magnetic moment. 22

22

Since  a = − g

28

B


J , if J = S then along the axis of application of B we have  a = − g  B ms − g B ms


Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

However, experimental values show non-integer numbers.

This is due to several causes:
-

The spin orbit coupling carries a small contribution of orbital angular momentum (sometimes
positive and sometimes negative), even where there is quenching for the crystal field.

-

The interaction between atomic magnetic moments and conduction electrons (in conducting
ferromagnetic materials), which induces a small magnetic moment in the latter.

-

The distribution of electrons in the band structure can lead to a non-integer average number of
electrons per atom in a ferromagnetic material.

The comparison of Cu (diamagnetic as it does not have d orbitals with unpaired electrons) and Ni
(ferromagnetic) allows to clarify this phenomenon. The figure above shows the diagram of the 4s
and 3d band structure in copper. Since the Fermi energy is above the 3d band, it contains 10
electrons per atom and is full, while the 4s contains 1 electron per atom, and is half-full. The 3d
band can be divided into two subbands corresponding to electrons with opposite spin, each with 5
electrons, so the contribution to net magnetization is 0.

29

P05

The figure shows the diagram of the 4s and 3d band structure of Ni above Tc (a) and 0 K (b). The
Fermi energy is lower than the 3d band, so above the Tc, the 4s band contains 0.54 electrons/atom,
and the 3d band contains 4.73/atom. Since above Tc the Ni is paramagnetic, in the 3d band there is
the same number of electrons with spin up and down. At 0 K, on the other hand, the exchange
interaction between the electrons prevails over the thermal motions, so one of the two sub-bands
will be energetically favored in having the maximum number of iso-aligned spins, compatibly with
the number of available orbitals, which coincides with 1/2 of the total or with 5 electrons per atom.
In the other band will remain 4.73 - (5 - 4.73) = 4.46 electrons. The result is a net magnetic moment
of 5 – 4.46 = 0.54 electrons, or 0.54  (close to what is indicated in the table above). This value
coincides with the gaps in the 3d band, so we often refer to the magnetic moment associated with
the presence of the gaps.

Magnoni.
Weiss's mean field theory does not reproduce
well the pattern of magnetization at low
temperatures, as the experimental trend shows
a faster decrease of M with T in that region, of
the type

M

M (T = 0 K )

= AT 3 / 2

Known as Bloch's law of T3/2 where A is a
constant that depends on the material. The
30

Theoric
Experimental

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

explanation for this dependence lies in the presence of spin waves that lead to a more rapid
misalignment of low-T spins, called magnons.
Magnons are spin waves with quantized energy. A spin wave is an oscillation of the spin direction
(parallel to each other) of a ferromagnet, which propagates undulating in the material, to which is
associated a characteristic energy for the system under examination or a multiple of it. Magnon
physics has many similarities with that of phonons, with the difference that they are not oscillations
in the relative position of crystal atoms but the relative orientation of their spins.
In the ground state (and at 0 K), spins in a ferromagnetic domain are all parallel. If one considers N
spin S, then with spin angular momentum S arranged along a line, and assumes that the coupling
constant J is different from 0 only for the first neighbors, then one can write the overall Heisenberg
coupling energy as
N

U = −2 J  S p  S p +1
p =1

Being all parallel, at 0 K (ground state of the magnone), treating for simplicity S as a classical
vector, we have
U 0 = −2 JNS 2

An excitation of the system could correspond to the reversal of a spin in the row (see figure), so for
two spin pairs the exchange interaction would change sign and there would be an energy

(

)

U 1 = −2 JNS 2 − 2( −2 JS 2 ) + 2 2 JS 2 = U 0 + 8 JS 2

It is not said that this energy cost is sustainable at low temperatures, where the experimental trend
of T-3/2 is observed. On the other hand, an excitation with a lower energy cost can be obtained if the
"overturning" of a spin is distributed over all the spins in the row by a precession motion:

To find the energy associated with this precession motion, first consider the p-th Sp spin, to which
a magnetic moment will be associated.

 p = − g B S p
which allows the contribution of the p-th term to be rewritten to U as

31

P05

− 2 JS p  (S p −1 + S p +1 ) = 2

J
g B

 p  (S p −1 + S p +1 ) =


J 
(S p −1 + S p +1 ) = −  p  B p
= −  p   − 2
g B 


where the last member shows how the whole can be expressed in the form of the interaction energy
between the magnetic moment associated with the spin and an effective magnetic field (exchange)
Bp acting on it:


J 
(S p −1 + S p +1 )
B p =  − 2
g B 

From the laws of classical mechanics, the variation of angular momentum S p in time is given by
the torque due to Bp:


dS p
dt

=  p  Bp



J 
J 
(S p −1 + S p +1 ) = − g B S p   − 2
(S p −1 + S p +1 ) =
=  p   − 2
dt

g


g

B 
B 


2J
(S p  S p−1 + S p  S p+1 )
=


→

dS p

So a misalignment between Sp and Bp leads to a non-zero torque that propagates along the entire
chain triggering the magnonic oscillation.
Reporting everything in Cartesian components we have
 dS px 2 J y z
=
S p S p −1 + S pz +1 − S pz S py−1 + S py+1


 dt
y

 dS p 2 J
=
− S px S pz −1 + S pz +1 + S pz S px −1 + S px +1


 dt
z
 dS p 2 J x y
=
S p S p −1 + S py+1 − S py S px −1 + S px +1

dt




 (


)

(

 (

)

(

)

(

)

(

)

)

If the oscillation of Sp is small, then Sx, Sy << S23 and one can simplify the system by assuming Sz
~S and neglecting the terms of order SxSy:

 dS px 2 J

S 2S py − S py−1 − S py+1


 dt
y
 dS p
2J
−
S 2 S px − S px −1 − S px +1


 dt
z
 dS p 2 J
0 − 0



 dt







23



By convention, z is assumed as the direction of spin alignment.

32

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

This system of equations can have solutions such as
x

S p = u expi ( pka − t )
 y

S p = v expi ( pka − t )

where u and v are constants, p is the index that identifies the spin in the row, and a is the spacing
between the spins.
Substituting the test functions in the system of equations gives
2J

− iu expi ( pka − t ) =
S 2v expi ( pka − t ) − v expi (( p − 1)ka − t ) − v expi (( p + 1)ka − t )




− iv expi ( pka − t ) = − 2 J S 2u expi ( pka − t ) − u expi (( p − 1)ka − t ) − u expi (( p + 1)ka − t )



2J

− iu expi ( pka ) =
S 2v expi ( pka ) − v expi (( p − 1)ka ) − v expi (( p + 1)ka )



→
− iv expi ( pka ) = − 2 J S 2u expi ( pka ) − u expi (( p − 1)ka ) − u expi (( p + 1)ka )





2J
2J 
exp− i (ka ) + expi (ka )
− iu =  S 2v − v exp− i (ka ) − v expi (ka ) =  S 2v − 2v

2


→
− iv = − 2 J S 2u − u exp− i (ka ) − u expi (ka ) = − 2 J S 2u − 2u exp− i (ka ) + expi (ka )



 
2

J

− iu = 4 Sv(1 − cos ka )



→
− iv = −4 J Su(1 − cos ka )



J

iu + 4 S (1 − cos ka )v = 0



→
J
iv − 4 S (1 − cos ka )u = 0




To this system corresponds the secular determinant
i
−4

J
S (1 − cos ka )


4

J
S (1 − cos ka )

=0
i
2

 J

→ − 2 +  4 S (1 − cos ka ) = 0
 

→  = 4 JS (1 − cos ka )
However, the dispersion relation shown in the figure on the side is valid only for the ideal case
treated in this example, of a spin linear chain with exchange interaction limited to its first neighbors.
Even in realistic cases of spins arranged along a three-dimensional lattice, if the exchange
33

P05

interaction is limited to the first neighbors, the dispersion relation has a similar pattern to what was
found in this simplified case.
Replacing  in the system leads to the following solution

v = −iu
i 4 JS (1 − cos ka )u + 4 JS (1 − cos ka )v = 0 iu + v = 0 
→
→ u

(
)
(
)
i
4
JS
1
−
cos
ka
v
−
4
JS
1
−
cos
ka
u
=
0
iv
−
u
=
0


v = i = −iu
and test solutions
S px = u expi ( pka − t )
 y
S p = −iu expi ( pka − t )

This result corresponds to a precession with circular orbit about the z-axis.

 x
 e ix e ix e −ix e − ix 
i  e ix e −ix 
ix
 = u cos x + u  −
 = u cos x + iusenx
+
−
S p = ue = u +
2
2
2 
i 2
2 

 2
x = ( pka − t ) → 
ix
ix
−ix
−ix
ix
−ix
S y = −iueix = −iu e + e + e − e  = −iu cos x − iu i  e − e  = −iu cos x + usenx
 2
 p
2
2
2 
i  2
2 


whose real components are

 
 

 Re S px = u cos( pka − t )




y
 Re S p = usen( pka − t ) = u cos pka − t − 
2



where the phase relationship /2 between the two components is evident.

The solution coincides with what would be obtained through the complete quantum mechanical
treatment.
If the wavelength of the magnon is very large compared to the periodicity of the spins, or
ka =

2



a  1

Then one can expand the cosine in truncated power series to the first term for which
1

2
 = 4 JS (1 − cos ka )  4 JS  1 − 1 + (ka )  = 2 JSa 2 k 2
2



Magnon energy is quantized in the same way as photons and phonons.

34

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

1

E k =  nk +  k
2


where nk is the Magnone number with wave vector k.
Like photons and phonons, the number of excited magnons at a certain temperature is given by the
Planck distribution, which applies to all physical problems in which the potential is harmonious:

nk =

1
  
exp k  − 1
 k BT 

Each nk = 1 corresponds to the reversal of a spin, so the variation in magnetization with respect to
magnetization at 0 K is proportional to the ratio

k nk 3 / 2
M

T
M (0 )
N
which in turn can be calculated to be proportional to T3/2, in accordance with experiments. This
relation is called Bloch's law of T3/2.
The ferromagnetic domain structure.
A "macroscopic" ferromagnetic material, also monocrystalline, can have zero initial magnetization,
if cooling below the Curie temperature occurs in the absence of an external magnetic field. This
depends on the spontaneous division of the material into magnetic domains, i.e. small regions
within which the magnetization is different from 0, but has no direction parallel to that of
magnetization in neighboring domains. These magnetic domains are called Weiss domains.
The magnetization that develops in magnetic domains in the absence of an external field is directed
along some preferential directions, established by the symmetry of the crystal, and called
"directions of easy magnetization". This means that, at distances much greater than atomic, the
advantage in having parallel alignment of magnetic moments, due to the exchange energy, is
outweighed by the tendency of the dipoles to align in an antiparallel direction with each other, as
predicted by the classical model of magnetism.
The boundary between two magnetic domains, or the
area in which the magnetization changes direction, is
called the domain wall or Bloch wall. It consists of a
gradual rotation of the direction of magnetic moments,
over distances of the order of a few hundred atoms
(about 300 in the case of Fe).
The domains are present both in a single crystal and in a
35

P05

polycrystalline material, since there is no correlation between the crystallographic and magnetic
domains, on a scale higher than that of the single crystallographic cell. The figure shows the
arrangement of ferromagnetic domains in a monocrystalline nickel foil. Thus, it is evident that there
is no relationship between the dimension of the Bloch domains and that of the crystalline domains
in the material. The direction of magnetization in each
domain, indicated by the arrow, is identified by monitoring
the growth or contraction of each domain by application of an
external magnetizing field. The white lines indicate the walls
of the magnetic domains, and are obtained by spreading an
oil containing fine iron powder on the crystal.
In general, magnetic domains that form spontaneously
(without application of external field) and crystalline domains
do not coincide, but this is true only above a critical
dimension, as schematized in the figure on the side, which shows a qualitative representation of
magnetic domains in a polycrystalline material (Bloch walls are indicated as dotted lines while
wheat edges are indicated in blue). In addition, magnetic domains usually do not extend beyond
crystallographic domains, except randomly as shown in the figure, because crystallographic
directions in polycrystalline materials are random, and magnetization within each crystalline
domain will always follow directions of easy magnetization.
Directions of easy magnetization and anisotropy
energy.
The magnetization curves for Fe are anisotropic,
in fact magnetization is facilitated when the
directions [100] are aligned with the field and is
more difficult along the direction [111].
The difference in energy for magnetization along
two

different

directions

is

called

magnetic

anisotropy energy. Since the exchange interaction
leading to magnetic ordering is an isotropic
phenomenon,24 anisotropy energy originates in the
crystal structure of the ferromagnet and in the spin
24

Changing the direction of magnetization is equivalent to changing the orientation of the spins in the material, but this
does not involve any change in the position of the atoms in the crystalline cell, so it is an isotropic process except for a
secondary effect due to the asymmetry of the orbitals due to the spin-orbit interaction.

36

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

orbit coupling between S and L. The spin-orbit interaction leads to a slight asymmetry in the charge
distribution, which moves with the spin in its orientation motion along the magnetizing field (see
figure on the side). Since atomic distances vary depending on the crystallographic direction, some
orientations will be less favored due to a higher electrostatic repulsion contribution, and vice versa,
so not all magnetization directions have the same energy cost in a ferromagnetic crystal.

For example, in Co, which has H.C.P. structure, the direction of easy
magnetization is that of the main axis C6 and the anisotropy energy is

M



expressible as a function of the angle  between the magnetization and
the main axis of symmetry:
U kCo = K 1' sin 2  + K 2' sin4 

with K1' and K2' two temperature-dependent constants. When the
direction of magnetization is parallel to the C6 axis, the sine cancels out
l3=cos3

and, with it, the anisotropy energy is zero.
As shown in the figure, in the -Fe, the directions of easy magnetization
coincide with the edges of the cubic cell, and the anisotropy energy is
given by

(

)

l1=cos1

U k − Fe = K 1' l12 l 22 + l 22 l32 + l32 l12 + K 2' l12 l 22 l32

where are the directing cosines the magnetization with respect to the three axes of the cubic cell. In
this case, when the direction is parallel to one of the edges of the cell, one of the directing cosines is
1 while the other two are 0, so the anisotropy energy cancels out.
The constants K' are called anisotropy constants and are usually measured in energy per unit
volume.
The transition region between domains.
The magnetic moments of the cells in the Bloch walls change direction continuously from one
domain to another. The change in direction of spins at the boundary between two magnetic domains
37

P05

does not occur within a single atomic plane, but can involve
a layer hundreds of atomic planes thick. The reason lies in
the fact that

the exchange energy is lower if the spin

rotation occurs gradually.
The transition region that separates two domains with
different direction of magnetization in a magnetic material is
called the Bloch wall.
The thickness of the Bloch wall can be obtained using a
classical interpretation of the Heisenberg model,

H ex = −2 JS i  S j
For example, if we consider two spins S between which there is an angle 
U ex = −2 JS 2 cos 

If  is small, then
1
1 

cos   1 −  2 → U ex  −2 JS 2  1 −  2 
2
2 


where it is seen that the presence of an angle  between the two spins corresponds to an additional
energy cost equal to
U ex = JS 2 2

If the rotation of 180° in the direction between the spins is distributed over N + 1 atomic planes,
the angle  between two spins will be
=


N

→ U ex = JS 2

2
N2

and the total energy for a spin row will be
NU ex = JS 2

2
N

So the energy tends to 0 per N , but the increase in thickness of the Bloch wall is balanced by
the anisotropy energy, which is higher for spins that deviate from directions of easy magnetization.
The energy of total anisotropy Uanis will be proportional to the number of spins N in the row:

U anis  N
To derive the value of N at which there is equilibrium between the gain in exchange energy and the
loss in anisotropy energy, we can consider the simple case of a Bloch wall that separates two
domains with magnetization in opposite directions due to spins arranged in a simple cubic crystal.
The total energy tot associated with the formation of a Bloch wall with unit area section will be
38

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

 tot =  ex +  anis
where the exchange term ex will be proportional to the number of atomic plans
involved and the number of spins per unit area.
Since in a simple cubic lattice we have 1 spin for each face of the cell of side a,
the spin density per unit area will be 1/a2, so the exchange energy density per
unit area will be equal to the exchange energy for the single spin (Uex) for the spin density per unit
area (a2) for the number of atomic planes in the Bloch wall (N):
2
NU ex
1
2 
 ex =
= JS
2
N a2
a

The total anisotropy energy will be proportional to the wall thickness (Na), with proportionality
constant approximately equal to the "average" anisotropy constant expressed per unit volume (K):25

 anis  NaK
whereby

 tot = JS 2

2 1
N a

2

Number of atomic planes
in the Bloch wall

 ex = NU ex

+ KNa

Exchange energy
for 1 spin

Minimizing with respect to N is

→ JS 2

2
a2

1
1
2 
=
JS
a2
N a2

 anis  NaK

d tot
2 1
= − JS 2 2 2 + Ka = 0
dN
N a

Number of
spins per
2
unit area

Thickness of
The Bloch wall

Average
anisotropy
constant
(energy per
unit volume)

= KaN 2

 2 2 
→ N =  JS 3 
a K


1/ 2

which is proportional to the root of the exchange integral J and inversely proportional to the root of
the anisotropy constant K.
The energy per unit area is

2

 2 2 
1
 tot = JS
+ K  JS 3 
1/ 2
a2
a K
 2 2 

 JS 3 
a K

2

= J 1/ 2S

K 1 / 2
a1 / 2

+ J 1/ 2S

K 1 / 2
a1 / 2

1/ 2

a=

=

25

The anisotropy energy depends on the angle between the spins and the direction of easy magnetization, so in case of
rotation of 180° along the row of N spin it would be necessary to perform the average on this angle. Multiplying K
(expressed in energy per unit volume) by the length of part Na gives an energy anis per wall of unit area.

39

P05

 KJS 2 

= 2 
 a 

1/ 2

The energy per unit area per single floor is
2
1
 tot  2  2 1
1
2
1
2 
2
=  JS
+ KNa  = JS
+ Ka = JS
+ Ka =
2
2
2
2
N 
N a
N a
 2   a2
N
 JS 3 
a K

 2a3K 1
= JS 2
+ Ka = 2 aK
JS 2 2 a 2

Performing the same calculation in the case of Fe (B.C.C.) for a 180° rotation of the spin in a
direction perpendicular to the plane (100), we obtain a total energy equal to
 − Fe

 tot

 2 K 1 JS 2 

= 2
a



1/ 2

and a number of atomic plans N  300.
In physics, the rotation of the spin that is observed in a Bloch wall represents an example of a
"soliton", or a physical quantity that can be described as a localized wave, unless there is a
magnetizing field that stimulates its propagation, and in this case the encounter with another Bloch
wall (another soliton) does not change its amplitude or frequency but only the phase. Solitons are
observable phenomena, under appropriate conditions, in optics and mechanics and, together with
skirmioni, are gaining relevance in the field of quantum technologies.
Spin in materials subject to spontaneous magnetic ordering (ferromagnets, antiferromagnets and
ferrimagnets) can also be organized in local energy minimums with a "topologically" anomalous
configuration, such as to be different from a soliton. These energy minimums are
defined "skyrmions" and are quasiparticles corresponding to a topologically non-trivial magnetic
configuration confined to a finite and localized region of the materials, generally
stable or metastable with respect to its transformation into a homogeneously magnetized ground
state that is equivalent to the magnetic soliton state.

40

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

The origin of magnetic domains.
The previous calculation shows that the formation of Bloch walls has a non-zero energy cost.
Therefore, if the ferromagnetic material spontaneously organizes itself into domains, there must be
an energy advantage of different origin. Landau and Lishfitz have shown that the presence of
magnetic domains results from the balance between the different contributions of exchange energy,
anisotropy energy and magnetic energy.
In particular, the magnetic energy UM associated with the presence of a magnetic field B in a certain
volume of space V is given by:
UM =

1
B 2 dV
8 

It is verified that, for a ferromagnet, the configuration with the lowest energy cost will tend to be the
one in which the B field has the least possible spatial extension.
The figure qualitatively schematizes the
field lines in a hypothetical uniaxial
magnetic material26 in the case of (a)
single magnetic domain, (b) two and (c)
four domains. It is observed
magnetic

flux

density

that the

outside

the

material is progressively reduced as the
number of nd domains increases, with a dependence that proves to be
UM 

26

1
nd

In uniaxial materials, the direction of easy magnetization coincides with the main axis of symmetry.

41

P05

But it never cancels, while inside the material the magnetic energy remains practically unchanged.
(d) In the case of uniaxial materials, inverted wedge domains may be formed to further reduce the
flow density outside. (e) The domains that allow the total concatenation of the magnetic field flux,
without magnetic flux permeation outside the sample, are those with wedge structure and direction
of magnetization orthogonal to that of adjacent domains. These domains are called closure domains,
because they complete the magnetic flux circuit entirely within the material.
Magnetization curves and hysteresis.
The increase in magnetization takes place by two independent processes:
1. At moderate fields, the volume of favorably oriented domains increases at the expense of those
oriented in an unfavorable way, by migration of Bloch walls.
The figures below show a diagram of the process and an experimental measurement performed on a
small iron monocrystal.

2. At very strong fields, the magnetization rotates in the direction of the external field.
In hysteresis curves, this process begins at the inflection point of the last stroke (see figure).
Another inflection point can be identified in the low-field zone, corresponding to the initial phase
in which the expansion of magnetic domains is reversible.
42

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

It is therefore possible to measure a hysteresis characteristic for a certain ferromagnetic (or
ferrimagnetic, see below) material, i.e. the profile traced by magnetization during a cycle of
variation of the intensity of the magnetizing field applied to the material itself according to H = 0

+Hmax  0  -Hmax  0.
In such a cycle the following characteristic quantities can be identified:
-

Ms - saturation magnetization: the maximum
possible magnetization in a material, observed when
all dipoles have been aligned by the magnetizing
field.

-

Mrs magnetic remanence: The magnetization that
remains in a material after removal of the external
field.

-

Coercive field Hc: also called coercivity, the field
that must be applied to the material to cancel the
magnetization.

As can be seen from the figure, a ferromagnetic material can initially have a zero magnetization, or
different from 0 depending on its "history" of exposure to external magnetizing fields.
Hysteresis M – H corresponds to hysteresis B-H, which however is of less practical interest because
the value of B never saturates being B = 0H + .

43

P05

Coercivity.
The coercivity can vary by as many as 7 orders of magnitude depending on the type and structure
(understood as the size and dispersion of crystalline grains in other magnetic and non-magnetic
dispersing phases) of the magnetic material, and its value can be modified by acting on the structure
of the material.
As shown by the hysteresis cycle, magnetic permeability has a variable value depending on the
strength of the applied field H, but also on the "history" of the material, since the same value of H
can correspond to different values of M and different slopes. Therefore, the magnetic susceptibility
for ferromagnetic materials cannot be uniquely identified, but depends on the state of spin ordering
in the material. In general, one can define as the derivative of M with respect to H valued at the
value of the applied field Hi:

 ferrom =

dM
dM
→ r = 1 +
dH H i
dH H i

In materials with high coercive field, the variation of M with H will be slower, which will
correspond to a low magnetic permeability, and vice versa for materials with low coercive field.
The coercive field can be decreased (and magnetic permeability increased) minimizing material
defects.
Instead, a high coercive field can be achieved by structuring the material into particles the size of a
single magnetic domain, but assembled so that
there are no crystalline connections between
them. This can occur in a heterogeneous
structure in which the magnetic particles are
dispersed in a second metallic phase, as in the
figure on the side referring to a section of the
width of 1100 nm of the system Al(8wt%)Ni(14wt%)-Co(24wt%)-Cu(3wt%)-Fe(51wt%), called Alnico V. The precipitation is performed in
the presence of a magnetic field, so that the nanoparticles are oriented with their major axis all in
the same direction, so as to obtain an anisotropic structure.
Crystals with dimensions close to 10-7 - 10-8 m are generally single-domain, because the division
into subdomains becomes energetically expensive. Therefore, in the individual domains, the
rotation of the magnetization cannot occur by moving the Bloch walls, but must rotate all together,
which requires more energy. In single-domain Fe particles, Hc  500 Gauss.

44

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Ferrimagnetism.
At the macroscopic level, the magnetic behavior of ferrimagnetic materials is similar to that of
ferromagnetics.
At the microscopic level, as in ferromagnetics, the cell has a net magnetic moment, but not as large
as if all magnetic centers were aligned in the same direction.
In fact, in ferrimagnetism some magnetic centers are constructively coupled, and others
destructively.
Examples of ferrimagnets are Fe3O4, NiFe2O4, ZnFe2O4.
A common feature of ferrimagnets is that they are insulators, while many ferromagnets are
conductive metals. This is useful for all applications where non-conductive magnetic materials are
required, as described below.
The case of ferrites.
Fe3O4 magnetite has a FeO.Fe2O3 reverse spinel
structure.
The normal structure of spinels (F.C.C. lattice) is
that of MgAl2O4, with divalent ions (Mg2+) in

Tetrahedral sites
(1/2,0,0)
Octahedral sites
(1/4,1/4,1/4)

tetrahedral sites and trivalent ions (Al3+) in
octahedral sites.
In inverse spinels, the divalent ions swap position
with the trivalent ones, so that the former occupy only the octahedral sites and the latter also the
tetrahedral ones. In random spinels, divalent and trivalent ions are divided into proportions 2:1 and
1:2 as shown in the figure.
½ of Fe3+ cations
(tetrahedral sites)

8 Fe3+: 5  B
(S = 5/2)

½ of Fe3+ cations and all Fe2+
cations (octahedral sites)

8 Fe3+: 5  B
(S = 5/2)

8 Fe2+: 4  B
(S = 2)

The arrangement of spins in magnetite is such that the magnetic moments of Fe3+ ions, whose spin
is 5/2, cancel each other, leaving only the contribution of Fe2+ ions, whose spin is 2.
Magnetite is the progenitor of ferrites, with MO.Fe2O3 structure, where M is a divalent cation
between Fe, Zn, Cd, Ni, Cu, Co, Mg.

45

P05

Exchange interactions in ferrimagnetic materials.
In ferrites, all exchange interactions favor antiparallel spin alignment . Since we have two magnetic
centers A and B, it means that
JAA, JAB, JBB < 0
However, if spins A are parallel to each other, same are spins B, then

J AB  J AA + J BB
The condition for the stability of the spin arrangement in a ferrimagnet with permanent
magnetization can be derived by the Weiss model.
Identify three types of exchange interactions, corresponding to interactions AA, BB and AB,
characterized respectively by the molecular field coefficients -, - and - with a negative sign for
what has just been said about the exchange integrals in ferrimagnets. According to Weiss' theory,
spin A will be affected by exchange interactions with other spins A (with molecular field constant

) but also with spin B (with molecular field constant ), and vice versa for B (with molecular field
constants  and ). Then the Weiss field heard by spins A and B will be:

B A = −M A − M B
BB = −M B − M A
They will correspond to an interaction energy density 27:
U =−

1
(B A  M A + BB  M B ) = 1 M A2 + M A  M B + 1 M B2
2
2
2

which is less than 0 when M A it is antiparallel to M B and the interaction AB prevails over the sum
of the interactions AA and BB:

MA MB  0
M A M B 

(

1
M A2 + M B2
2

)

as in the case of ferrites, where the ground state has MA antiparallel to MB and the material is
ferrimagnetic.
Susceptibility of ferrimagnetic materials.
To derive the susceptibility of ferrimagnets, two Curie constants can be defined for spins A and B.
For simplicity, consider only the interaction AB (which has just been seen to be the prevailing one):

BA = − M B
BB = − M A
27

If magnetization per unit volume is used, the energy will be per unit volume.

46

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

According to the Weiss model one can write28

MA
C 
= A = A 
B
T
CA
(Ba − M B )
BA = − M B  M A =
T
→

MB
CB 
C

= B =
M B = B (Ba − M A )
B
T 
T

BB = − M A 
To find the Curie temperature I can solve the system of two equations in case Ba = 0:

TM A + C A M B = 0 
T
CA
= 0 → T 2 − C AC B  2 = 0
→
TM B + C B M A = 0  C B  T
from which one derives Tc:

Tc =  (C AC B )

1/ 2

which is the only temperature at which you can have MA and MB other than 0 even in the absence of
Ba (for T>Tc and Ba = 0, the system admits only the trivial solution MA = MB = 0).
Solving the system for Ba  0 one gets MA and MB:
C

C

M A = A (Ba − M B )
M A = A (Ba − M B )



T
T
→

→
CB 
CA
C B Ba
CBC A

2 CBC A

(
)
MB =
B
−

B
−

M
MB =
−
Ba + 
MB
 a
a
B 
T 
T
T
T2
T2


C BTBa − C B C A Ba 
CA 
CA



M
=
B
−

(Ba − M B )
A
A

T 
T 2 −  2 C B C A 
T
→
→
C T − C B C A
T2
C BTBa − C B C A Ba


MB = B
B
MB =
a
T2
T 2 −  2 C B C A 

T 2 −  2CBC A
MA =

C ATBa − C B C A Ba 
T 2 −  2 C B C A 
C BTBa − C B C A Ba 

MB =
T 2 −  2 C B C A 

MA =

that substituting in susceptibility leads to

=

M A + M B (C A + C B )T − 2 C AC B
=
(c.g.s.)
Ba
T 2 − Tc2





=

T 2 − Tc2
(C A + CB )T − 2C ACB

The figure on the side shows the reciprocal
susceptibility of magnetite as a function of
temperature. We observe the typical trend of

28

It is also assumed in this case that B =  0 H +  0 M   0 H since m << 1 → r  1 and M is very small.

47

P05

ferrimagnets, which is different from that of the Curie-Weiss law (for T > Tc is



C
C
, and for T ~ Tc is  
) followed by ferromagnets.
T − Tc
(T − Tc )

Anti-ferromagnetism.
The coupling of atomic magnetic moments does not always lead to a "constructive" alignment as in
ferromagnetism.
For some materials, the alignment of the spin moments of
adjacent atoms occurs in opposite directions.
For example, in MnO, O2- has no net magnetic moment,
while Mn2+ has a net moment due to the spin of electrons in
the d orbitals. However, below a certain temperature, there
is no net magnetization in the material, so MnO is called
antiferromagnetic.
In an antiferromagnetic material, below a magnetic ordering
temperature called the Néel TN temperature, the spins are
arranged in an antiparallel manner.
Antiferromagnetism

represents

a

special

case

of

ferrimagnetism in which there are two spin sub-crystals with
equal and opposite magnetization. Thus, it is equivalent to placing CA = CB in the susceptibility in
the paramagnetic range:29

M A + M B (C A + C B )T − 2 C AC B 2CT − 2C 2 
=
=
=
(c.g.s.)
Ba
T 2 − Tc2
T 2 − Tc2
with

Tc =  (C AC B )

1/ 2

= C = TN

whereby
2CT − 2C 2 
T − C
2C
= 2C
=
=
2
2 2
(T + C )(T − C ) T + C
T − C
2C
=
T + TN

=

In fact, experimentally we find a trend of the type

29

It is also assumed in this case that B =  0 H +  0 M   0 H since m << 1 → r  1 and M is very small.

48

Prof. V. Amendola

=

Physical Chemistry of Materials

LM in Materials Science

2C
T +

where  is a fictitious temperature not coinciding with TN at which the transition from para to
antiferromagnet is actually observed, in fact /TN varies from ~ 5 to ~ 1. The discrepancy is due to
the need to also consider the exchange interactions with the second closest primes and the possible
arrangement in sublattices other than the crystalline one.

1



=

T +
2C

AFM: antiferromagnetic
PM: paramagnetic

43

Susceptibility of antiferromagnets.
While above TN (in the paramagnetic phase) the susceptibility is independent of the direction of
application of the magnetizing field, below TN there are two possible "limit" orientations: parallel to
the spins or perpendicular to them.
In general, the energy density in the presence of a magnetic field will be given by the balance
between two contributions, the one due to the tendency of the two magnetizations to arrange

49

P05

themselves in an antiparallel direction, and the opposite one due to the tendency of the
magnetizations to align in the direction of the magnetizing field:
U = M A  M B − Ba  M A − Ba  M B = M A  M B − Ba M A cos A − Ba M B cos B

where i is the angle between the field and the magnetization.
When the field is perpendicular to the direction of magnetization, you will have
A = B = 

So what
M A = −M B → M A = M B = M

and the two magnetizations will be distorted in the
direction of the field itself due to the tendency of
the spins to align with the magnetizing field (see
figure), so an angle 2 will be formed between them
2 + 2 =  →  =

 − 2
2

so you can write
  − 2 
U = M 2 cos( − 2 ) − 2 Ba M cos

 2 

Since

cos(x − y ) = cos(x )cos( y ) + sin( y ) sin(x )
one has
cos = cos

 − 2
2

= cos


2

cos  + sin


2

sin = 0 + sin

cos( − 2 ) = cos  cos 2 + sin  sin 2 = − cos 2 + 0
Being 2 very small, it can expand in power series truncating to first order in 

1
(2 )2 + ...
2
sin   + ...

cos 2  1 −

so one rewrites U as
1

2
U  M 2  − 1 + (2 )  − 2 Ba M
2



Then it was possible to express the magnetic energy as a function of the angle 2 and its value
corresponding to the minimum of U can be identified:
B
dU
= 4 M 2 − 2 Ba M = 0 →  = a
d
2 M

50

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

So the resulting magnetization in the material will be

M tot = 2 M cos = 2 M sin  2 M =
= 2M

Ba
B
= a
2 M


and susceptibility is by definition

=

M tot
Ba

and the magnetic susceptibility is obtained by field oriented perpendicular to the direction of the
two magnetizations:

⊥ =

1 Ba
1
=
Ba 


In the other extreme case of Ba parallel to the direction of the magnetizations, if all
spins are aligned and equally distributed between MA and MB (i.e. at 0 K), then
Mtot = MA – MB = 0
and

 // =

M tot
=0.
Ba

La  // will progressively tend to the value of TN
susceptibility due to spin misalignment due to
thermal agitation.
Overall, a material will have a series of domains
with

various

orientations

and

the

resulting

susceptibility at the macroscopic level will be the
average of the two.
=

1
2
 ⊥ +  //
3
3

so, we see that at TN susceptibility has a cusp, instead of diverging
as in ferromagnetic materials.
The magnetic structure of MnO is shown in the figure on the side,
where Mn2+ ions are indicated in purple and O2- ions in red. It is
observed that, along the side of the cell, the distance between the
Mn2+ ions is greater than that which usually admits an intense
51

P05

exchange interaction. In this case, antiferromagnetism takes place due to the mediation of the
oxygen atom placed between the two ions of Mn2+, based on a mechanism called "super exchange".
In the "super exchange", the d electrons of Mn are coupled with the electrons of O, which in turn
interact with the d electrons of the other ion of Mn.
The dashed line corresponds to the direct exchange interaction J1 between adjacent Mn ions (near
primes), while the dashed line J2 shows a "super-exchange" interaction with the second closest
primes, through an intermediate O ion. The result is that, below TN, the spins arranged in the single
plane (111) are parallel to each other, but the direction of the spins of two adjacent planes (111) is
antiparallel.
Neutron scattering.
The phase transition from paramagnetic to antiferromagnetic can be measured through neutron
scattering. In fact, neutrons, despite having no charge, have spin, which allows them to interact with
the spin "lattice" of the material, be it electronic or nuclear. The magnetic moment of neutrons
interacts with those present in the material, and the neutron scattering cross section is of the same
order of magnitude whether the scattering occurs with electronic magnetic moments, or with
nuclear ones (~103 times smaller), indicating that the interaction with nuclei is ~103 times more
intense than with electrons. Neutrons interact with magnetic moments in all their forms, and in fact
can lead to annihilation or excitation of a magnon, through an inelastic scattering process. In this
way it is possible to measure the characteristic frequency of magnons m according to the principle
of conservation of energy:
 2 k n2,i  2 k n2,s
=
+  m
2M n
2M n

where kn,i and kn,s are respectively the wave
vector of the incident and scattered neutron,
whose mass is MN.
The

neutron

scattering

measurement

performed on MnO, at T > TN = 120 K
shows

peaks

of

scattering

intensity

coinciding with those of a cubic cell F.C.C.
with cell parameter a = 4.43 Å, while for T <
TN the spin cell is cubic with cell parameter a
= 8.85 Å. Since no structural phase transition
occurs in the material, both at T < TN and at
52

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

T > TN the crystalline cell always remains the cubic F.C.C. with cell parameter a = 4.43 Å.
Dependence of susceptibility on temperature.
Above the critical (or Curie) temperature, ferro- and ferrimagnetic materials no longer possess
spontaneous magnetization, becoming paramagnetic. The same thing happens for antiferromagnets.

Applications of iron and ferrimagnetic materials.
The shape of the hysteresis cycle reflects the
magnetic anisotropy of the material and determines
the applications of the ferromagnet.
In fact, the energy expended during the hysteresis
cycle is proportional to the area of the hysteresis
cycle itself, and for a material of volume V is given
by
E = V  HdB

As shown in the figure, sections 1-2 and 3-5 make a
positive

contribution

to

the

work

done

for

magnetization (in 1-2 H > 0 and dB > 0, in 3-5 H < 0
and dB < 0), while sections 2-3 and 5-6 give a
53

P05

negative contribution (in 2-3 H > 0 and dB < 0, in 5-6 H < 0 and dB > 0).
The

figure

shows

the

comparison

between

hysteresis cycles for three different applications of
magnetic materials:
-

"Soft" magnets, in which the coercive field is
relatively low compared to magnetization.

-

"Hard" magnets, in which the coercive field is
high.

-

Magnets with "square" cycle, in which the
residual magnetization is comparable to that of
saturation and the coercive field is relatively high.

Types of magnetic materials.
The graph below represents the saturation magnetization and coercive field for a range of magnetic
materials.

54

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Soft Ferromagnets:
- so-called "electric" steels for applications in electronic devices. They are bonded with Si to
increase resistivity and decrease magnetic anisotropy
-

Fe-Co-Mn

-

permalloys (Ni78Fe22) with almost zero anisotropy and magnetostriction

-

vitreous metals (e.g. Fe79B13Si9 based)

Hard Ferromagnets:
- Rare earth alloys with Mn, Fe, Co and Ni, such as SmCo5, Nd2Fe14B.
Type of ferromagnet

Hc

Application

Alnico V

600 g

Speakers

SmCo5

10000 g

Special magnets with high stability

Fe 4wt% in Si

0.5 g

Transformers

Supermalloy

0.002 g

Pulsed transformers

Classification of magnets
In the industrial or application field, magnets can be evaluated according to different parameters
such as:
- the tensile force, i.e. the force to be exerted to separate a magnet from an iron surface (with
standard characteristics). It can be expressed in N or Kg.
- the strength of the magnetic field, measured at a certain distance and direction from the surface of
the magnet. Expressed in Gauss or T.
- the maximum "energy product", which corresponds to the maximum value of the product H*B in
the hysteresis cycle H vs B. This value, measured in Mega Gauss Oersted (MGOe) is typically
anticipated by the letter N and can be followed by other letters (M, H, SH, UH, EH, AH) that
indicate the maximum operating temperature without loss of magnetization (for example N45M
means 45 MGOe and maximum operating temperature of 100 °C).

55

P05

As for applications:
- Soft magnetic materials are often used to amplify the magnetic flux density produced by a coil
through which electric current passes. This series includes electromagnets, electric motors,
transformers, generators, and other electrical equipment. In these electrical devices it must be easy
to cancel the induced magnetization without dissipating an excessive amount of heat. For the core
of a transformer you want a ferromagnet with low coercive field, because this corresponds to low
dissipation of magnetic energy into thermal energy at each hysteresis cycle.
In the particular case of ferrites, they are oxides and, therefore, are not electrical conductors, which
allows them to be used as dielectric magnetic components, in high-frequency applications such as
microwave devices (e.g. circulators and phase modulators).
- Hard magnetic materials are used as permanent magnets. Permanent magnets can be classified
according to the "power" of the magnet, i.e. the maximum value reached by the product of magnetic
induction for the magnetizing field inside the hysteresis (rectangle of greater area inscribable in
hysteresis), for which high coercivity is needed.
- Square hysteresis materials are used for data storage such as hard drives and magnetic tape devices
such as cassette tapes or advanced tape storage systems. In fact, they maintain a high magnetic field
even after the removal of the magnetizing field.

56

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Permanent magnet and induction motors.
Induction motors use ferromagnetic materials, mainly silicon-steel laminations, in both stator and
rotor cores. These materials have high magnetic permeability, which channels and strengthens the
magnetic flux. The laminations reduce eddy current losses, improving efficiency. Copper or
aluminum conductors are embedded in the rotor to carry induced currents. The interaction between
the magnetic core fields and rotor currents produces torque. Thus, magnetic materials are essential
for flux concentration, efficiency, and torque generation.
The reverse mechanism is exploited for electricity generation. Here, rotation due to a mechanical
force drives the rotor. This changing magnetic flux induces voltage in the stator windings. Thus,
mechanical energy is converted into electrical energy by the same principles.
In permanent magnet motors, the rotor carries magnets that establish a steady magnetic field. This
field interacts with the stator’s current-carrying windings to produce torque. Since no field windings
are required, copper losses in excitation are avoided. The design offers high efficiency and power
density compared to induction motors. Stronger magnets, such as NdFeB, allow compact machines
with high torque output. Precise control is achieved with modern power electronics and sensors.
These motors are widely used in electric vehicles, wind turbines, and robotics. Their combination of
efficiency, compactness, and reliability makes them vital in advanced systems.

57

P05

Magnetostriction.
Magnetostriction is

the variation in the size of a

material, usually ferromagnetic metallic, due to its
magnetization. This phenomenon is due to the
reorientation of atomic dipoles. Since the process is
isochoric and takes place in the direction of
magnetization, it actually consists in the elongation of
the material in the direction of the magnetizing field. This effect is in some ways equivalent to the
piezoelectric effect, and in the past it was used to generate sound waves (e.g. sonar during World
War 2).
Giant magnetoresistance.
Giant magnetoresistance (GMR) is a quantum effect of electrical resistance dependent on the
magnetization of the material, observed in thin-film structures composed of alternating layers of
ferromagnetic and non-magnetic type. The 2007 Nobel Prize in Physics was awarded to Albert Fert
and Peter Grünberg for the discovery of GMR.
The effect is observed as a significant change in electrical resistance depending on whether the
magnetization of adjacent ferromagnetic layers is in parallel or antiparallel alignment. The overall
resistance is relatively low for parallel alignment and relatively high for antiparallel alignment.
The typical GMR-based device is the spin-valve. The figure below shows a multilayer composed of
a non-magnetic conducting film (NM) coupled to two ferromagnetic (FM) conducting films. You
can have the configuration with antiparallel (right) and parallel (left) magnetizations. The vertical
black arrows in the ferromagnetic layers show the direction of magnetization, while the arrows
through the spin valve schematize the path of the electron, where a deviation from the straight path
indicates that the electron has been scattered. In the spin valve, an electron passing through the FM
layer will suffer a higher probability of scattering if it has spin opposite to the direction of
magnetization. This principle allows the two FM layers to be represented as two electrical circuits
in parallel, one for each spin orientation of the conduction electrons, where the resistance is
different depending on the orientation of the spin. The calculation of the equivalent resistance for
the spin valve in antiparallel and parallel configuration shows that parallel alignment has the lowest
resistance.
GMR is used in hard drives to read stored data.

58

Prof. V. Amendola

Physical Chemistry of Materials

LM in Materials Science

Magnetocaloric effect and magnetic refrigeration.
The magnetocaloric effect consists of heating a
magnetic material following its exposure to an
external magnetic field. The increase in temperature
is due to the heat released into the material as a result
of the spin being sorted along the direction of the
external field. The magnetocaloric effect is more
intense close to the Curie temperature of the material.
In some cases, magnetic sorting also involves a
structural change, which corresponds to an additional heat release.
The magnetocaloric effect is used in magnetic refrigeration, which allows to obtain extremely low
temperatures, useful for scientific purposes, but above all as a refrigeration technology for common
refrigerators.
The principle of magnetic refrigeration is that, after the magnetic ordering, the ferromagnet will
return to thermal equilibrium with the environment. At this point, if the magnetizing field is
removed, the ferromagnet will be able to absorb heat from the outside, which it will use to return
the magnetization to its original value. During this process, the ferromagnet acts as a chiller. By
coupling the ferromagnet with a fluid heat exchange system (e.g. water), the heat released during
the magnetization cycle can be dissipated outwards, and the heat inside the luminaire can be
absorbed during the demagnetization cycle.
Compared to traditional gas compression refrigeration, magnetic refrigeration is quieter, more
compact, has superior cooling efficiency and does not use harmful gases for the Earth's ozone layer.

59



## Metadata
- Source file: junk_drawer/P05_Handout.pdf
- Extracted: 2026-05-18
- Category: academic-lecture
