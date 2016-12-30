:title: Determination of the Internal Resistance of a Cell Using a Potentiometer
:id: F2-1
:description: The LeClanché cell creates an electromotive force that drivescurrent through a circuit.  Internal to the cell there is a resistence tocurrent, which is measured by applying a special case of Ohm's law.
:type: lab

F2-1: Determination of the Internal Resistance of a Cell Using a Potentiometer
==============================================================================

Apparatus
---------

Leclanché Cell (filled to bottom of paint line with
saturated Ammonium Chloride solution); metre bridge board; 3V battery
(fresh cells); jockey; switch; galvanometer with 100\ :math:`\Omega`
series resistor; rheostat (:math:`\sim` 15\ :math:`\Omega` resistance);
resistors values: 5\ :math:`\Omega`, 10\ :math:`\Omega`, and
20\ :math:`\Omega`; block with crocodile clips (for resistor);
connecting leads (3 long, 7 short); 1 sheet graph paper.

|F2-1.1| 

Procedure
---------

1. Construct the above circuit, with :math:`R =\infty\Omega`. Close the
   switch **S**. After placing **J** 5cm from **B**, adjust the rheostat
   until the galvanometer reads zero (balance point). Note the length
   :math:`l_{\infty} = \overline{AJ}`. Open **S**.

2. Connect :math:`R = 30\Omega`, Close **S**, and find the balance
   point. Read :math:`l = \overline{AJ}`. Repeat with :math:`R =` 25,
   20, 15, 10, and 5\ :math:`\Omega`. Tabulate :math:`R` and :math:`l`.
   Open **S**.

NOTE: After the experiment, empty the Ammonium Sulphate solution out of
the Cell again, to ensure a maximum lifetime for the solution.

Theory
------

Consider the lower branch of the circuit when the galvanometer reads
zero. It is effectively disconnected from the top branch of the circuit:

|F2-1.2| 

.. math::
   I=\frac{E}{r+R}=\frac{V}{R}\\

Therefore:

.. math::
   ER = Vr+VR

And therefore:  

.. math::
   r = \frac{R(E-V)}{V} 

However the length :math:`l` is proportional to the potential difference 
:math:`V`, and when :math:`R=\infty\Omega`, :math:`V = E`. Thus let 
:math:`V = kl` and :math:`E = kl_{\infty}`,where :math:`k` is a constant.  
Therefore:

.. math::
   r = \frac{R(kl_{\infty}-kl)}{kl} = \frac{R(l_{\infty}-l)}{l}

And therefore:

.. math::
   \frac{1}{R} = \frac{l_{\infty}}{r} \times \frac{1}{l} - \frac{1}{r}

Analysis
--------

1. Plot a graph of :math:`\frac{1}{R}` vs. :math:`\frac{1}{l}` and find
   the gradient.

2. Use the gradient, the value of :math:`l_{\infty}`, and the last
   equation in the theory only to find the internal resistance of the
   cell, :math:`r`.

Questions
---------

1. 

   a) In the theory why can we say that the lower branch is 'effectively 
      disconnected' from the top branch of the circuit? 

   b) If the resistance of wire **AB** is 2\ :math:`\Omega` and its length
      is 100cm, find an expression for :math:`k` in terms of :math:`V_{AB}`
      only.

2. Compare the Leclancé Cell and the modern Dry Cell.  List
   a) the similarities and 
   b) the differences.

3. Define 
   a) internal resistance and 
   b) electromotive force. 
   Thus explain carefully why in the theory, when :math:`R =\infty \Omega`,
   then :math:`V = E`.

.. |F2-1.1| image:: /images/37.png
.. |F2-1.2| image:: /images/38.png
