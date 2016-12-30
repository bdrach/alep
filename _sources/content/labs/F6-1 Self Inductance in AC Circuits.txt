.. meta::
  :description: An inductor in a simple LR circuit reveals relationships between resistance, current, peak voltage, and the influence of a magnetic core.  Withan AC current applied, the system acts as an electronic harmonic oscillator. 

F6-1: Self Inductance in AC Circuits
====================================

Apparatus
---------

300 turn coil; 2 iron C-cores; C-core clip; ammeter (0 - 1 Adc);
voltmeter (O - 5 Vdc); 3 batteries (3V); 2 x 100\ :math:`\Omega`
resistors; CRO (oscilloscope); AC power supply; 0.5m ruler; connecting
leads (5 short); 1 sheet graph paper.

*NB: This experiment requires mains electricity.*

Procedure
---------

1. To find the resistance :math:`r` of the coil, connect the following
   circuit and use the readings of the ammeter and voltmeter to calculate
   :math:`r`:

|F6-1.1| 

2. To find the inductance :math:`L` of the coil with an iron core,
   connect the following circuit:  
   |F6-1.2| 

   a) Connect the CRO input to :math:`V_1`. Adjust the CRO so that
      :math:`V_1` is about 4V, the supply being switched to AC. Adjust the
      CRO so that the AC waveform is seen clearly:  

      |F6-1.3| 

      Carefully adjust the power supply so that the peak value of
      :math:`V_1` as seen on the screen is 4V peak.  

   b. Now connect the CRO to measure :math:`V_R` peak. Use this, and the
      value of **R** to calculate the value of :math:`I` peak for the
      circuit.  

   c. Use the CRO to measure :math:`V_2` peak.  

   d. Repeat a), b), and c), but using :math:`V_1` of 3.5, 3, 2.5, 2, 1.5,
      1, 0.5, and 0 volt peak each time.  

   e) Tabulate the values of :math:`V_R` peak, :math:`V_2` peak, and
      :math:`I` peak.  

   f) Measure the cross-sectional area of the iron core and the distance
      :math:`l` around the centre of the pair of cores as shown below:  

     |F6-1.4| 

Theory
------

The coil with its iron core has an inductance :math:`L`, and the copper
wire of the coil has a resistance :math:`r`. An equivalent circuit for
the coil is:

|F6-1.5| 

The impedance of this combination of :math:`r` and :math:`L` is given
by:

.. math::
   Z = \sqrt{r^2 + \omega ^2 L^2} \label{eqn1} \tag{equation 1}

where:

.. math::
   \qquad Z = \frac{V_2 \text{ rms}}{I \text{ rms}} = \frac{V_2 \text{ peak}}{I \text{ peak}} \label{eqn2} \tag{equation 2}

and: 

.. math::
   \qquad \omega = 2 \pi f

It is also possible to calculate :math:`L` using data about the coil and
its core:

.. math::
   L = \frac{ \mu_0 \mu_r N^2 A}{l}  \label{eqn3} \tag{equation 3}

where:

.. math::
   \mu_0 &= 4 \pi \times 10^{-7} \text{Hm} ^{-1} \\
   \mu_r &= \text{relative permeability of the iron} \\
   N &= \text{number of coil turns} \\
   A &= \text{core cross-sectional area} \\
   l &= \text{distance around core}

Analysis
--------

1. Plot a graph of :math:`V_2` peak against :math:`I` peak, and find the
   gradient.

2. Use the gradient and :math:`\ref{eqn2}` to find the value of :math:`Z`.

3. Use :math:`\ref{eqn1}` to find the inductance of the coil, :math:`L`.

4. Use this value of :math:`L`, together with the other measured values,
   and :math:`\ref{eqn3}`, to find the relative permeability of this type of
   iron, :math:`\mu_r`.

5. Look up values of :math:`\mu_r` for different types of iron in a reference
   table and try to deduce the type of iron alloy used in your iron cores.

Questions
---------

1. Use the values of :math:`R`, :math:`r`, and :math:`L` above to
   calculate the current :math:`I` peak when :math:`V_1 = 8`\ V peak and
   :math:`f = 1`\ kHz.

2. Use :math:`\ref{eqn3}` to estimate :math:`L` if the iron core is removed.
   Show that in this case :math:`Z \approx r`. Repeat Q1 using :math:`L`
   for the coil without an iron core.

3. Briefly explain the energy changes in :math:`r` and :math:`L` when:  

   a)   The current is + and rising  

   b)  The current is a maximum +, and constant  

   c) the current is + and falling

4. How can an inductor be constructed so that power losses are kept to a
   minimum (consider both the design of the coil and the core)?

5. Why is it desirable to keep power losses to a minimum in an inductor
   used in the tuning circuit of a radio receiver?

6. Prove that:

   .. math::
      \qquad \frac {V_2 \text{ rms}}{I \text{ rms}} =
      \frac{V_2 \text{ peak}}{I \text{ peak}} \tag{from equation 2}

   Why in the experiment is :math:`V` peak measured rather than :math:`V` rms?

7. Sketch on the same graph curves of :math:`V` and :math:`I` for an
   inductor (with :math:`r = 0`) which is connected to an AC power
   supply.

8. Explain carefully why
   :math:`V_1 \text{ peak} \neq V_R \text{ peak} + V_2 \text{ peak.}`

.. |F6-1.1| image:: /images/49.png
.. |F6-1.2| image:: /images/50.png
.. |F6-1.3| image:: /images/52.png
.. |F6-1.4| image:: /images/53.png
.. |F6-1.5| image:: /images/54.png
