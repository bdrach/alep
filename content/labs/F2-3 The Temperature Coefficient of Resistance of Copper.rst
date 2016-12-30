:title: The Temperature Coefficient of Resistance of Copper
:id: F2-3
:description: The Wheatstone Bridge, in this case using a 100 cm wire ofconsistant resistivity, is a good tool for measuring the changing resistancein a wire as its temperature increases.
:type: lab

F2-3: The Temperature Coefficient of Resistance of Copper
=========================================================

Apparatus
---------

Metre bridge board; clamp and stand; 1.5V cell; galvanometer; jockey;
standard resistor 10\ :math:`\Omega`; copper wire & thermometer in a
test tube; 1L beaker of water; bunsen burner (or other heat source); 8
connecting leads (5 long, 3 short); 1 sheet of graph paper.

|F2-3.1| 

Procedure
---------

1. Set up the apparatus as above, connecting the battery last. Check
   carefully that all connections are secure. Do not begin heating yet. Find 
   the balance point length :math:`L` where the galvanometer reads zero. 
   Disconnect the battery. Read the temperature :math:`\theta`.

2. Begin heating the water. At temperatures approximately 30, 35, 40,
   45,... up to 90°C, reconnect the battery, find :math:`L`, and read
   :math:`\theta` (to the nearest 0.1°C). Disconnect the battery between
   readings.

3. Tabulate the readings of :math:`L` and :math:`\theta`.

Theory
------

1. Resistivity (the Greek :math:`\rho` ) at a given temperature is:

    .. math:: 
    
      \rho = \text{Resistance} \left( \frac{ \text{Area}}{ \text{length}} \right)
    
   Therefore the resistance of a given sample varies with temperature. 
   This is given by:

   .. math::
      
      R_{\theta} &= R_0 (1+ \alpha \theta + \beta \theta^2) \\ 
      \\  
      \text{Where: } R_{\theta} &= R \text{ at } \theta \text{°C} \\  
      R_0 &= R \text{ at } 0 \text{°C} \\ 
      \alpha \text{ } & \text{and } \beta \text{ are constants}
      

   :math:`\beta` is very small, and is usually neglected. In this
   experiment, assume that :math:`\beta =0`. 
    
2. The circuit is a Wheatstone Bridge:  

   |F2-3.2| 

   When the galvanometer reads zero:  

   .. math::
      \frac{R_1}{R_2} = \frac{R_3}{R_4} \qquad \qquad \textbf{---- equation 1}
      

   And therefore in this experiment when the units of L are cm: 

   .. math::
      R_{\theta} = 10 \left( \frac{L}{100-L} \right) \qquad \qquad \textbf{---- equation 2}
      

Analysis
--------

1. For each value of :math:`L`, calculate a value of :math:`R_\theta`
   using the above formula (equation 2).

2. Plot a graph of :math:`R_\theta` vs. :math:`\theta`\ °C. Find the
   gradient and the y-intercept. NB: it is not necessary for the
   :math:`R_\theta` axis to extend down to zero).

3. Use the formula given in 1 of the theory, together with the gradient
   and y-intercept only, to calculate :math:`\alpha`, the temperature
   coefficient of resistance of copper.

Questions
---------

1. Use equation 1 above to prove equation 2.

2. Calculate the expected resistance of the copper wire when its
   temperature is 300°C.

3. If copper has a **resistivity** of
   :math:`1.7 \times 10^{-8}\Omega\text{m}` at 293K, find the
   **resistance** of a sample of copper length 5cm, uniform
   cross-sectional area :math:`10^{-6} \text{m}^2`, at: 

   a) 0°C

   b) 100°C.

.. |F2-3.1| image:: /images/41.png
.. |F2-3.2| image:: /images/42.png
