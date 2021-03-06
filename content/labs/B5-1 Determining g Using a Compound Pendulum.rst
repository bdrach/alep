.. meta::
  :description: Simple to construct and conduct, this experiment finds the acceleration due to local gravity and centrifugal acceleration while also showing the moment of inertia of the compound pendulum about its axis of rotation.

B5-1: Determining :math:`g` Using a Compound Pendulum
=====================================================

Apparatus
---------

|B5-1.1| 

Long uniform stick with holes at regular intervals; stiff :math:`25\text{cm}` long
wire; 2 razor edges mounted on blocks; 4 lab stools; stopwatch; graph
paper; triple beam balance

Procedure
---------

1. Suspend the stick as shown starting with the wire in the hole nearest
   the end of the stick. Record the time required for 20 oscillations of
   small amplitude.  Find the periodic time, :math:`T`, where 
   :math:`T = \frac{(\text{time for 20 oscillations})}{20}`.  Record the 
   distance, :math:`d`, from each hole to the end of the stick you started 
   near.  Repeat for every hole from one end of the stick to the other. 

2. Measure and record the mass, M, of the stick.

3. Graph :math:`T` against :math:`d`. This graph will be a pair of
   roughly parabolic curves symmetric about a line parallel to the y-axis.

4. Select 6 values of :math:`T` and draw lines parallel to the x-axis
   through those values. These lines should cross each curve two times.
   Find the distance along the x-axis from left to right between the
   first point of intersection with the left hand curve and the first
   point of intersection with the curve on the right. Call this value L
   and tabulate it with the corresponding values of :math:`T` and
   :math:`T^2`.

Observations
------------

:math:`M=\big(\text{mass of the stick}\big)=` ________ kg 

Tabulate:

|B5-1.2| 

Average value of :math:`\frac{L}{T^2}=` ________ :math:`\text{ms}{^-}{^2}`

Theory
------

For a small displacement :math:`\theta`, the equation of motion of the
stick executing simple harmonic motion is:

.. math::
   \text{Torque} = I\alpha = -Mgh\theta \quad \text{or} \quad \alpha = - \frac{Mgh}{I}\theta 
   

.. math::
   M &= \text{mass of the stick}\\
   h &= \text{distance from the axis of rotation to the center of mass}\\
   \theta &= \text{angular displacement in radians}\\
   I &= \text{the moment of inertia of the stick about the axis of rotation}\\
   \alpha &= \text{angular acceleration} = \frac{d^2\theta}{dt^2}\\

From the theory of simple harmonic motion the angular frequency,
:math:`\omega`, is:

.. math::
   \omega = \sqrt{\frac{Mgh}{I}} \quad \text{ and the period, } T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{I}{Mgh}} 
   

By the parallel axis theorum and definition of radius of gyration, :math:`k`:

.. math::
   I = Mk^2 + Mh^2
   
and therefore:

.. math::
   T = 2\pi\sqrt{\frac{Mk^2 + Mh^2}{Mgh}} = 2\pi\sqrt{\frac{k^2 + h^2}{gh}} 
   

The period of a simple pendulum is :math:`T = 2\pi\sqrt{\frac{L}{g}}`. L
is equivalent to the expression :math:`\frac{1}{h}\sqrt{k^2 + h^2}`,
which has a value found graphically as explained in procedure 4 
(above). Using this value for :math:`L` compute :math:`\frac{L}{T^2}`, and find :math:`g`
from the expression:

.. math::
   g = 4\pi^2\frac{L}{T^2} 
   

Analysis
--------

1. What is the value of :math:`g` which you obtain using the average
   value of :math:`\frac{L}{T^2}`?

2. The moment of inertia of the bar can be found from the graph
   :math:`T` against :math:`d`. The radius of gyration, :math:`k`, is
   one half the distance along the x-axis from the point where the
   slope of the left curve is zero to the point where the slope of the
   right curve is zero. Use this value of :math:`k` and the mass of the
   stick to determine the moment of inertia of the stick.

.. |B5-1.1| image:: /images/11.png
.. |B5-1.2| image:: /images/12.png
