.. meta::
  :description: The transistor acts as a current amplifier where the collector current depends on the size of the smaller base current.  This lab shows how transfer characteristics and output characteric changes with potential difference.

G2-1: Transistor Characteristics
================================

Apparatus
---------

:math:`3\text{V}` battery; :math:`9\text{V}` battery; 2 rheostats (high resistance); resistor :math:`\text{R}_2`
(approx. 50 k\ :math:`\Omega`); voltmeter (:math:`0-5\text{Vdc}`); ammeter
(:math:`\approx 50 \mu\text{A}` *fsd*); ammeter (:math:`\approx 3 \text{mA}` *fsd*);
transistor (pnp); connecting leads (12 short); 2 sheets graph paper.

    |G2-1.1| 

Instructions
------------

Set up the circuit as above, but do not connect the batteries until a
teacher has checked the circuit (to avoid damaging the ammeters or
transistor). In the experiment, when not taking readings, leave the
batteries disconnected.

EXPERIMENT 1
------------

**To investigate the 'transfer characteristics' of the transistor.**  
The transistor acts as a current amplifier: the size of the large
current :math:`I_C` depends on the size of the small current
:math:`I_B`. The circuit used above is called a 'common emitter'
circuit.

1: Procedure
-----------------------

1. Set :math:`V_{CE}` to :math:`4\text{V}` using rheostat :math:`\text{R}_3`. Ensure that this
   remains constant (adjust :math:`\text{R}_3` again later as necessary).

2. Set :math:`I_B` to 0 using :math:`\text{R}_1`. Read and note :math:`I_B` and
   :math:`I_C`.

3. Increase :math:`I_B` a little using :math:`\text{R}_1`, and read and note
   :math:`I_B` and :math:`I_C`. Continue increasing :math:`I_B` and
   reading the ammeters until :math:`I_C =` 3 mA.

4. Tabulate the readings of :math:`I_E`, :math:`I_C`, and the value of
   :math:`V_{CE}`.

1: Analysis
----------------------

1. Plot a graph of :math:`I_C` against :math:`I_B`, labelling the curve
   with the value of :math:`V_{CE}` used.

2. Find the gradient of the straight-line section of the curve. Then:  

   .. math::
      \text{Current gain } \beta = \frac{\Delta I_C}{\Delta I_B} = \text{gradient}

EXPERIMENT 2
------------

**To study how** :math:`I_C` **varies when** :math:`V_{CE}` **is changed, for certain
fixed values of** :math:`I_B`.  The graph obtained is called the ’output
characteristic' of the transistor.

2: Procedure
-----------------------

1. Set :math:`I_B = 0` using :math:`\text{R}_1`. Starting with
   :math:`V_{CE} = 0`, and little by little increasing :math:`V_{CE}` up
   to :math:`5\text{V}`, take a set of readings of :math:`I_C` and :math:`V_{CE}` and
   note the value of :math:`I_B = 0`.

2. Increase :math:`I_B` to :math:`10 \mu`\ A, and obtain another set
   of readings of :math:`I_C` and :math:`V_{CE}` as in step 1.

3. Repeat the procedure with :math:`I_B = 20 \mu`\ A then :math:`30 \mu`\ A.

4. Tabulate the sets of readings of :math:`I_C` and :math:`V_{CE}`,
   noting the value of :math:`I_B` for each set.

2: Analysis
----------------------

1. Plot a graph of :math:`I_C` vs. :math:`V_{CE}` to obtain four curves.
   Label each curve with the appropriate value of :math:`I_B` used.

Questions
---------

1. When :math:`I_B = 0`, :math:`I_C` should be zero for all
   :math:`V_{CE}`. However all transistors have some *leakage current*.
   What is the value of the leakage current :math:`I_C` when
   :math:`V_{CE} = 4`\ V?

2. What is the approximate minimum :math:`V_{CE}` so that a variation in
   :math:`I_B` between :math:`0` and :math:`30 \mu A` produces a large 
   change in :math:`I_C`? (In practice the supply voltage is usually set 
   between this value and a certain maximum. The maximum depends on 
   the 'breakdown voltage' of the junctions).

3. In use as an amplifier, an AC input voltage makes :math:`I_B` vary
   with time.  For example:  

   |G2-1.2| 

   a.  Use the value of :math:`\beta` to make a graph of :math:`I_C`
       against time.  

   b. If a resistor :math:`\text{R} = 1`\ k\ :math:`\Omega` is connected in
       series with the collector :math:`C`, so that :math:`I_C` flows
       through it; draw a graph of the potential difference (p.d.) across
       this resistor against time.  

   c. What is the frequency of these AC currents and p.d.?

4. Draw a diagram to show while the pnp transistor is conducting:  

   a.  Electron flows and conventional currents through the three
       terminals.  

   b. Electron & hole movements inside the transistor (may be simplified).

.. |G2-1.1| image:: /images/63.png
.. |G2-1.2| image:: /images/64.png
