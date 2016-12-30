.. meta::
  :description: Hooke's Law forms the basis for this set of observations on elastic deformation, the transfer of potential energy to kinetic energy, and vice versa.

B5-2: Experiments Using a Spiral Spring
=======================================

Apparatus
---------

2 stands with clamps; metre rule; spiral spring; scale pan with attached
pointer; stopwatch; assorted masses 5g to 100g; 2 sheets of graph paper;
triple beam balance

|B5-2.1| 


Procedure
---------

1. Measure and record the mass of the scale pan and attached pointer.
   Attach the pan and pointer to one stand and place the metre rule in
   the other stand such that the end of the pointer moves lightly over
   it. Read and record the pointer position. This is the zero position.

2. Put 5g in the pan and record the total load (including the mass of
   the pan and pointer) and the pointer position.

3. Put 10g more into the pan and record the position of the pointer and
   the total load on the spring. Continue adding 10g increments of mass
   until 95g has been added. Record the total load and pointer position
   each time.

4. Once you have reached 95g remove 10g at a time and record the total
   load and the pointer position each time. This will give you two
   readings for every load except at 95g.

5. Use the readings in your data table to find the total mean extension
   for each load by subtracting the zero position pointer reading (from
   1.) from the average pointer reading for each load. Write this in
   your table.

6. Put 50g into the scale pan then set it in vertical oscillations by
   lifting it slightly above the equilibrium position then quickly
   letting go. Time 20 complete oscillations to find the periodic time,
   :math:`T`, where :math:`T = \frac{\text{time for 20 oscillations}}{20}`.

7. Repeat procedure (6.) with 100, 150, 200, and 250g. Be certain to
   include the mass of the pan and pointer in your tabulation of total
   load on the spring.

Observations
------------

Mass of scale pan and pointer = \_\_\_\_\_ g 

Zero position of pointer = \_\_\_\_\_ cm (also record in data table)

Tabulate:

|B5-2.2| 

Theory
------

Hooke's Law predicts that when the spring experiences elastic
deformation due to a load the extension is linearly proportional to the
load: :math:`F = -kx`. When a mass, :math:`M`, attached to the spring
extends the spring by a distance, :math:`x`, there is a restoring
force :math:`Mg = \frac{x}{n}g`, where
:math:`n = \frac{\text{extension}}{\text{load}}` (n is the slope of
the first graph you will draw), and :math:`g` is the acceleration due to
gravity.

The oscillations of the spring are simple harmonic and obey the equation
of motion :math:`Ma = -\frac{x}{n}g` or, :math:`a = -\frac{g}{Mn}x`.
Using calculus, :math:`-\frac{a}{x}` can be expressed in terms of the angular
frequency :math:`\omega` such that:

.. math::
   \omega^2 = \frac{g}{Mn} \mbox{ and, } T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{Mn}{g}} 

The above assumes that the spring is weightless. In reality the spring
has an effective mass, :math:`m`, which changes the equation for T:

.. math::
   T = 2\pi\sqrt{\frac{(M+m)n}{g}} 

 
From a graph (you will draw) of :math:`T^2` vs. :math:`\text{load}`,
:math:`g` and :math:`m` can be found:

.. math::
   \frac{T^2}{\text{load}}=\frac{4\pi^2 n}{g}&=\text{(}\text{slope of the second graph} \text{)}\\  
   g &= 4\pi^2 n \frac{1}{\text{(} \text{slope of the second graph} \text{)}} 

The :math:`x`-intercept of the :math:`T^2` vs. load graph gives the
effective mass, :math:`m`, of the spring.

Analysis
--------

1. Plot a graph of total mean extension vs. load. Find the slope,
   :math:`n`, of the graph and the :math:`x` - intercept. Use SI units.

2. Does this first graph verify Hooke's Law?

3. Plot a graph of :math:`T^2` vs. load. Fine the slope and the
   :math:`x` - intercept.

4. Use the slope of your graph to solve for :math:`g`. Does the value
   you obtain for :math:`g` agree with your expected value of nearly 9.8
   ms\ :math:`^2`? If there are differences try to explain them.

5. What is the value you predict for the effective mass, :math:`m`, of the 
   spring? 

.. |B5-2.1| image:: /images/13.png
.. |B5-2.2| image:: /images/14.png
