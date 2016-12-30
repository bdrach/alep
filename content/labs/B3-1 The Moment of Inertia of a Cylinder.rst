.. meta::
  :description: A cylinder rolling down and incline plane trades potential energy for a combination of linear and rotational kinetic energy.  Thisconservation of energy creates a basis for testing principles of rotational dynamics.

B3-1: The Moment of Inertia of a Cylinder
=========================================

|B3-1.1| 

Apparatus
---------

2 mounted rails; 2 different cylinders with axles; metre rule;
micrometer screw gauge; stack of books; stop watch; piece of chalk;
triple beam balance; graph paper

Procedure
---------

1. Set up the apparatus as shown above with :math:`PR` less than 4 cm. Measure
   :math:`s=AB` and measure :math:`PQ`. Record :math:`s` and :math:`PQ`.

2. Measure and record :math:`PR`. Calculate
   :math:`\sin\theta = \frac{PR}{PQ}`.

3. Place a cylinder at :math:`A`. Record the time, :math:`t`, for the
   cylinder, starting from rest, to roll from :math:`A` to :math:`B`.

4. Determine the linear acceleration, :math:`a`, of the cylinder using
   your readings of :math:`s` and :math:`t`.

5. Increase :math:`PR` and repeat steps 2, 3, and 4. Increase :math:`PR`
   three more times, repeating steps 2, 3, and 4 to obtain five sets of
   readings.

6. Measure the axle diameter and find the axle radius, :math:`r_a`.
   Find the cylinder radius, :math:`r`.  Measure the mass, :math:`M`, of the 
   cylinder and axle.

7. Repeat steps 2 to 6 for the second cylinder.

Observations
------------

For each cylinder:

:math:`M` =________kg 

:math:`r_a` =________m 

:math:`r` =________m 
      
Tabulate:

|B3-1.2| 

Theory
------

The cylinder loses potential energy (:math:`PE`) and gains kinetic
energy (:math:`KE`) as it moves from A to B. Conservation of energy
requires:

.. math::
  \text{PE lost} &= \text{KE gained} \\ 
   Mgh &= Mgs\ (\sin\theta) \\ 

Ignoring friction this becomes the :math:`KE` of the cylinder where the total :math:`KE` is: 

.. math::
   KE = \text{KE (linear) }+\text{ KE (rotational)} \\ 

Therefore:

.. math::
   Mgs\ (\sin\theta) &=  \frac{1}{2}Mv^2+\frac{1}{2}I\omega ^2 \\ 

Substitute :math:`v^2 = 2as` and :math:`\omega = \frac{v}{r_a}` :

.. math::
   a = \left(\frac{Mgr_a^2}{Mr_a^2 + I}\right) (\sin\theta) \tag{check this yourself!} 

Analysis
--------

1. Plot a graph of :math:`a` against :math:`\sin\theta` for each
   cylinder on the same sheet of graph paper. Find the gradient of each
   line.

2. Given that :math:`a=(\frac{Mgr_a^2}{Mr_a^2 + I})\sin\theta` find
   :math:`I` for each cylinder.

3. From theory :math:`I = \frac{1}{2}Mr^2` where
   :math:`r = \text{cylinder radius}`. Calculate :math:`I` using this
   to check your value from 2 above. Give the % error for your value
   from 2.

4. If :math:`I = Mk`, find the radius of gyration, :math:`k`, for each
   cylinder.

5. Calculate the torque necessary to steadily accelerate each cylinder
   from rest to an angular velocity of 30 radians/s in 2s.

.. |B3-1.1| image:: /images/9.png
.. |B3-1.2| image:: /images/10.png
