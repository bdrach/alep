.. meta::
  :description: Kinetic energy is transferred when one material collides into another.  The efficiency of kinetic energy transfer is a property of the material and can be measured with this experimental technique.

B1-1: Coefficient of Restitution
================================

Apparatus
---------

2 wooden rods (about :math:`200\text{m}` long); wooden lath (about
:math:`25\text{cm}` long); 2 elastic bands; 2 pendulum bobs (1 large,
1 small); thin Cu wire; 2 :math:`0.5\text{m}` rulers; stand; 2 bosses
& clamps; G-clamp; triple beam balance.

|B1-1.1| 

Procedure
---------

1. Assemble the apparatus as above, ensuring that the lath and
   :math:`0.5\text{m}` ruler are horizontal. Make sure that the centres of
   the pendulum bobs are on the same level, and that the bobs just touch.

2. Pull bob A to the left and let it swing to collide with bob B to
   check the operation of the apparatus.

3. With the bobs at rest, read values :math:`a_2` and :math:`b_1` on the
   :math:`0.5\text{m}` ruler. (Position your eye carefully to avoid parallax). Measure
   length :math:`d`.

4. Move bob A to the left until it touches the :math:`0.5\text{m}` ruler.
   Read value :math:`a_1`.

5. Release bob A, and note the furthest position that it reaches on the
   right *after* the collision (this is :math:`a_3`).

6. Repeat 4 and 5 to get five readings of :math:`a_3` to average.

7. Repeat 4, then release bob A, and note the furthest position that
   *bob B* reaches to the right after the collision (this is
   :math:`b_2`).

8. Repeat 7 to get five readings of :math:`b_2` to average.

9. Measure the masses of bob A (:math:`m_A`) and bob B (:math:`m_B`)
   using the beam balance.

Observations
------------

|B1-1.2| 

Theory
------

It can be shown that a pendulum, length :math:`L`, moving through an
angle :math:`\theta` has a velocity change of:

.. math::
   v = \sqrt{2gL(1-\cos\theta)} \label{eqn1} \tag{equation 1}

1. In the experiment there is a collision, and momentum is conserved:

   .. math::
     \sum\big(\text{momentum before collision}\big) &= \sum\big(\text{momentum after collision}\big)\\
     m_A v_A + m_B v_B &= m_A v_A' + m_B v_B'

   where :math:`v_A`, :math:`v_B`, :math:`v_{A^{'}}`, :math:`v_{B^{'}}` are
   the velocities of bobs A and B before and after the collision
   respectively. However in the experiment :math:`v_B = 0`. Thus:

   .. math::
     \frac{m_A}{m_B} = \frac{v_{B^{'}}}{v_A - v_{A^{'}}}

   Calculating velocities using :math:`\ref{eqn1}`, and substituting:

   .. math::
     \frac{m_A}{m_B} = \frac{\sqrt{2gL(1-\cos\theta_{B^{'}})}}{\sqrt{2gL(1-\cos\theta_A)}-\sqrt{2gL(1-\cos\theta_{A^{'}})}}

   Thus:

   .. math::
     \frac{m_A}{m_B} = \frac{\sqrt{(1-\cos\theta_{B^{'}})}}{\sqrt{(1-\cos\theta_A)}-\sqrt{(1-\cos\theta_{A^{'}})}} \label{eqn2} \tag{equation 2}

   This equation can be used to calculate the ratio of the masses of the bobs.

2. To find the coefficient of restitution, :math:`e` :

  By definition:

   .. math::
     \qquad e = - \frac{\big(\text{relative velocity after the collision}\big)}{\big(\text{relative velocity before the collision}\big)}


  Using :math:`\ref{eqn1}` for these velocities:

   .. math::
     e = \frac{\sqrt{1-\cos\theta_{B'}}-\sqrt{1-\cos\theta_{A'}}}{\sqrt{1-\cos\theta_{A}}} \label{eqn3} \tag{equation 3}


Analysis
--------

1. Complete the following table to obtain values of :math:`\theta_A`,
   :math:`\theta_{A}'`, :math:`\theta_{B}'`.

   |B1-1.3|

2. Substitute the values of :math:`\theta_A`, :math:`\theta_{A}'`,
   :math:`\theta_{B}'` calculated in the above table into
   :math:`\ref{eqn2}` to calculate the ratio of the masses of the two
   pendulum bobs. Check the accuracy of the method using the readings of
   mass obtained directly using the beam balance. Comment on the
   differences in these ways of measuring mass, using either the ballistic
   balance (collision method), or the beam balance.

3. Substitute the values of :math:`\theta_A`, :math:`\theta_{A}'`,
   :math:`\theta_{B}'` from the above table into :math:`\ref{eqn3}` to calculate
   the coefficient of restitution for these pendulum bobs. Comment on
   the elasticity of the collision in your experiment if:

   .. math::
     e &= 1 \qquad \text{collision is perfectly elastic} \\
     e &= 0 \qquad \text{collision is completely inelastic}

   Give simple examples to illustrate the energy changes that occur in collisions where:

    i)   :math:`e = 1`

    ii)  :math:`e = 0`

    iii) :math:`e = \big(\text{the value in your experiment}\big)`

.. |B1-1.1| image:: /images/4.png
.. |B1-1.2| image:: /images/5.png
.. |B1-1.3| image:: /images/6.png
