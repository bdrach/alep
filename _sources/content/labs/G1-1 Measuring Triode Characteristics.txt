.. meta::
  :description: A triode with a small potential difference (p.d.) between the grid and cathode can amplify current flowing between the cathode and anode ata much higher p.d.  This discovery was the basis for radio and electronics.

G1-1: Measuring Triode Characteristics
======================================

Apparatus
---------

DC power supply :math:`0-800\text{V}`; voltmeter :math:`0-800\text{V}`; cathode heater circuit (in
power supply); planar triode (e.g.: TEL 521); 6 dry cells as grid voltage
source; sensitive ammeter :math:`0.01-0.8\text{m}`.; 9 connecting wires; 2 sheets of
graph paper.

|G1-1.1| 

Procedure
---------

1. Check the circuit to see it agrees with the drawing above. The power
   supply is off. Always be certain the power supply is off before you
   change circuit connections. Failure to do this may cause injury or
   damage to the equipment.

2. Set the grid voltage at :math:`-9\text{V}` (six dry cells in series). Set the
   power supply dial at zero. Turn on the power supply and slowly
   increase the anode potential by turning the power supply dial until
   the voltmeter shows 100\text{V}`. Record anode potential, :math:`V_a`, and
   anode current, :math:`I_a`, for :math:`V_a = 100, 200, 300, 400,
   500, \text{ and } 600\text{V}`.  

   NOTE the ammeter while you increase the anode potential. If the
   ammeter goes off scale, STOP increasing the potential difference and
   go on to the next step.  

   Turn the power supply off.

3. Change the grid potential, :math:`V_g`, to :math:`-6\text{V}` then repeat procedure (2).

4. Change :math:`V_g` to :math:`-4.5\text{V}` and repeat procedure 2.

5. change :math:`V_g` to :math:`-3\text{V}` and repeat procedure 2.

6. Change :math:`V_g` to :math:`-1.5\text{V}` and repeat procedure 2.

7. Make 5 more data tables of :math:`V_g` and :math:`I_a`, with
   :math:`V_a` constant. Use the data from the procedure above for
   :math:`V_a = 100, 200, 300, 400, \text{ and } 500\text{V}`.

Observations
------------

Tabulate:
 
:math:`I_a` and :math:`V_a` for each of the 5 values of :math:`V_g` constant: 

:math:`V_g` = ______ V

|G1-1.2| 

:math:`I_a` and :math:`V_g` for the first 5 values of :math:`V_a` constant:  

:math:`V_a` = ______ V

|G1-1.3| 

Theory
------

|G1-1.4| 

From the slope of the linear part of graph (a) the anode resistance is:

.. math::
   R_a = \frac{\delta V_a}{\delta I_a} \text{ when } V_g \text{ is constant} 

 
From the linear part of graph (b), the mutual conductance, :math:`g_m`,
is:

.. math::
   g_m = \frac{\delta I_a}{\delta V_g} \text{ when } V_a \text{ is constant}

The amplification factor, :math:`\mu`, can be found by comparing
:math:`V_a` and :math:`V_g` over similar intervals of :math:`I_a` on the
graphs:  

.. math::
   \mu = \frac{\delta V_a}{\delta V_g} \tag{  over the same interval $I_a$ }

or:

.. math::
   \mu = g_m R_a

Analysis
--------

1. Plot :math:`I_a` vs. :math:`V_a` for all values of :math:`V_g` on the
   same axes.

2. Plot :math:`I_a` vs. :math:`V_g` for all values of :math:`V_a` on the
   same axes.

3. From your graphs find :math:`R_a`, :math:`g_m`, and :math:`\mu`.

.. |G1-1.1| image:: /images/59.png
.. |G1-1.2| image:: /images/60.png
.. |G1-1.3| image:: /images/61.png
.. |G1-1.4| image:: /images/62.png
