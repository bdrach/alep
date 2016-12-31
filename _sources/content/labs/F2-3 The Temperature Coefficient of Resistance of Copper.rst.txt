.. meta::
  :description: The Wheatstone Bridge, in this case using a 100 cm wire of consistant resistivity, is a good tool for measuring the changing resistance in a wire as its temperature increases.

F2-3: The Temperature Coefficient of Resistance of Copper
=========================================================

Apparatus
---------

Metre bridge board; clamp and stand; :math:`1.5\text{V}` cell; galvanometer; jockey;
standard resistor :math:`10\Omega`; copper wire & thermometer in a
test tube; :math:`1\text{L}` beaker of water; bunsen burner (or other heat source); 8
connecting leads (5 long, 3 short); 1 sheet of graph paper.

|F2-3.1| 

Procedure
---------

1. Set up the apparatus as above, connecting the battery last. Check
   carefully that all connections are secure. Do not begin heating yet. Find 
   the balance point length :math:`L` where the galvanometer reads zero. 
   Disconnect the battery. Read the temperature :math:`\Theta`.

2. Begin heating the water. At temperatures approximately :math:`30, 35, 40,
   45,... \text{ up to } 90\text{°C}`, reconnect the battery, find :math:`L`, and read
   :math:`\Theta` (to the nearest :math:`0.1\text{°C}`). Disconnect the battery between
   readings.

3. Tabulate the readings of :math:`L` and :math:`\Theta`.

Theory
------

1. Resistivity (the Greek :math:`\rho` ) at a given temperature is:

    .. math:: 
    
      \rho = \text{Resistance} \left( \frac{ \text{Area}}{ \text{length}} \right)
    
   Therefore the resistance of a given sample varies with temperature. 
   This is given by:

   .. math::

      R_{\Theta} = R_0 (1+ \alpha \Theta + \beta \Theta^2)

   where:

   .. math::

      R_{\Theta} &= R \quad \text{ at } \Theta \text{°C} \\  
      R_0 &= R \quad \text{ at } 0 \text{°C} \\ 
      \alpha \text{ } & \text{and } \beta \text{ are constants}
      

   :math:`\beta` is very small, and is usually neglected. In this
   experiment, assume that :math:`\beta =0`. 
    
2. The circuit is a Wheatstone Bridge:  

   |F2-3.2| 

   When the galvanometer reads zero:  

   .. math::
      \frac{R_1}{R_2} = \frac{R_3}{R_4}  \label{eqn1} \tag{equation 1}
      

   And therefore in this experiment when the units of L are cm: 

   .. math::
      R_{\Theta} = 10 \left( \frac{L}{100-L} \right) \label{eqn2} \tag{equation 2}
      

Analysis
--------

1. For each value of :math:`L`, calculate a value of :math:`R_\Theta`
   using the above formula :math:`(\ref{eqn2})`.

2. Plot a graph of :math:`R_\Theta` vs. :math:`\Theta`\ °C. Find the
   gradient and the y-intercept. 
   
   *NB: it is not necessary for the* :math:`R_\Theta` *axis to extend down to
   zero.*

3. Use the formula given in 1 of the theory, together with the gradient
   and y-intercept only, to calculate :math:`\alpha`, the temperature
   coefficient of resistance of copper.

Questions
---------

1. Use :math:`\ref{eqn1}` above to prove :math:`\ref{eqn2}`.

2. Calculate the expected resistance of the copper wire when its
   temperature is :math:`300\text{°C}`.

3. If copper has a **resistivity** of
   :math:`1.7 \times 10^{-8}\Omega\text{m}` at 293K, find the
   **resistance** of a sample of copper length :math:`5\text{cm}`, uniform
   cross-sectional area :math:`10^{-6} \text{m}^2`, at: 

   a) :math:`0\text{°C}`

   b) :math:`100\text{°C}`

.. |F2-3.1| image:: /images/41.png
.. |F2-3.2| image:: /images/42.png
