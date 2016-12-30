.. meta::
  :description: Elastic materials under stress experience a measurable deformation (strain).  The ratio of stress to strain is a consistent physical property of the material -- the elastic modulus (or Young's modulus).

C3-1: Determining the Young's Modulus of Wood Along the Grain Using a Cantilever
================================================================================

Apparatus
---------

Wooden metre rule; :math:`100\text{g}` mass; elastic band; G-clamp; block of wood;
vernier calipers; stopwatch; graph paper  

|C3-1.1| 

Procedure
---------

1. Clamp the loaded metre rule firmly to the end of a bench with a
   definite length, :math:`L`, projecting from the edge of the bench.

2. Start the metre rule vibrating vertically and find the periodic time,
   :math:`T`, for one complete oscillation. Do this by timing :math:`20`
   oscillations and dividing by :math:`20`. Find :math:`T` for the following
   lengths :math:`L: 0.5, 0.6, 0.7, 0.75, 0.8, \text{ and } 0.9\text{m}`. Tabulate your
   readings of :math:`L` and :math:`T`.

3. Using the callipers, measure the dimensions :math:`b` and :math:`d`
   of the metre rule. Take six readings for each dimension at different
   positions along the rule. Record the readings, then calculate the
   mean values of :math:`b` and :math:`d`.

|C3-1.2| 

Observations
------------

:math:`M =` mass at end of the metre rule = ________ kg

6 readings for :math:`b`: ______, ______, ______, ______,
______, ______ 

  Average :math:`b` : ________ m

6 readings for :math:`d`: ______, ______, ______, ______,
______, ______ 

  Average :math:`d` : ________ m

Tabulate:

|C3-1.3| 

Theory
------

Bending theory gives :math:`s = \frac{4 F L^3}{b d^3 E}` where :math:`F`
is a force applied to the end of the metre rule and :math:`E` is known as
the Young's modulus(reference *Scholarship Physics* by Nelkon, fifth 
edition, p44). Thus if the rule is depressed a distance, :math:`s`, from 
equilibrium the restoring force is:

.. math::
    
   F=-\frac{b d^3 E s}{4 L^3}=-ks \text{ where: } k=\frac{b d^3 E}{4 L^3} 
   

This force acts on the mass at the end of the rule. Ignoring the mass of
the metre rule itself, the following is derived:

.. math::
   F = M a = - k s \quad \text{and therefore} \quad a = - \frac{k}{M} s

The solution to this equation comes from the theory of simple harmonic
motion. The equation describes an oscillation with
:math:`\omega ^2 = \frac{k}{M}`. In terms of the period this is:  

.. math::
    
   T=\frac{2 \pi}{\omega} = 2 \pi \sqrt{\frac{M}{k}}

Therefore:

.. math::
   T^2 =\frac{4 \pi ^2 M}{k}=\frac{16 \pi ^2 M}{b d^3 E}L^3 
   

Analysis
--------

1. Plot a graph of :math:`T^2` against :math:`L^3` and find the
   gradient.

2. From the equation :math:`T^2 =\frac{16 \pi ^2 M}{b d^3 E}L^3` and the
   gradient of your graph determine :math:`E`, the Young's modulus of
   the wood **along** the grain.

3. The Young's modulus **across** the grain is about :math:`0.5\text{GPa}`. Compare
   this with your value of :math:`E` from (2.) and give a reason for the
   difference.

4. Calculate the longitudinal tension that would stretch the metre rule
   by :math:`0.1\text{mm}`. Use the dimensions of the rule, your calculated value for
   :math:`E`, and the relation:
   :math:`E = \frac{\text{stress}}{\text{strain}}`

.. |C3-1.1| image:: /images/20.png
.. |C3-1.2| image:: /images/21.png
                :align: bottom
.. |C3-1.3| image:: /images/22.png
