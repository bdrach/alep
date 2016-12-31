.. meta::
  :description: An electrical circuit having a resistor, a capacitor, and a power supply (RC circuit) is used to observe current and potential differencefor capacitors wired alone, in series, and in parallel. 

F1-2: Charging Capacitors
=========================

Apparatus
---------

Capacitors (2 :math:`\times 1000\mu\text{F}`, electrolytic); voltmeter (high
resistance, :math:`0-5\text{Vdc}` eg multimeter); ammeter (:math:`0.5\text{mA}` fsd); resistor
(:math:`10\text{k}\Omega`); :math:`4.5\text{V}` battery; 2 switches; stopclock; 9 connecting
leads; 2 blocks with crocodile clips; 2 sheets of graph paper.

**IMPORTANT:** The battery must not be connected until your circuit has been checked by
a teacher (an error could seriously damage the ammeter).

|F1-2.1| 

Procedure
---------

1. Construct the circuit as above using one capacitor. Connect the
   battery after the circuit has been checked.

2. Leave :math:`SW2` open. Close :math:`SW1` and notice how :math:`V`
   and :math:`I` change as the capacitor charges. Open :math:`SW1`, then
   close :math:`SW2` briefly to discharge the capacitor again.

3. Close :math:`SW1` and start the stopclock at the same moment. Note readings
   of :math:`V` at :math:`t = 0, 10, 20, ...` up to :math:`100\text{s}` .
   Open :math:`SW1`, then discharge the capacitor by closing :math:`SW2`
   briefly.

4. Close both :math:`SW1` & :math:`SW2`, and note the value of :math:`I`
   at :math:`t = 0`. Open :math:`SW2` (to allow charging to start),
   starting the stopclock at the same moment. Note readings of :math:`I`
   at time :math:`t = 10, 20, 30 ...` up to :math:`100\text{s}`.

5. Tabulate your readings of :math:`V`, :math:`I`, and :math:`t`.

6. Replace the single capacitor by two capacitors in series:

   |F1-2.2| 

7. Repeat steps 2 to 5.

8. Replace the series capacitors by two in parallel:

   |F1-2.3| 

9. Repeat steps 2 to 5.

Analysis
--------

1.  Plot a graph of :math:`V` vs. :math:`t` for all three arrangements
    of capacitors on the same sheet of graph paper. Label each line
    clearly.

2.  Plot a graph of :math:`I` vs. :math:`t` on another sheet, labelling
    the three lines clearly.

3.  Find the area under the :math:`I` vs. :math:`t` curve for the single
    capacitor, using the axes scales. This is the total charge stored in
    coulombs (ask for help if you have not done this before).

4.  From the :math:`V` curve for the single capacitor read the maximum
    value :math:`V_{MAX}`.

5.  Calculate the capacitance using:

    .. math::
       C = \frac{Q}{V} \quad = \quad \frac{\big(\text{Total charge stored}\big)}{V_{MAX}}

6.  Repeat analysis steps 3, 4, and 5 for the capacitors in series and in parallel.

7.  Assuming that each capacitor has value
    1000\ :math:`\mu`\ F\ :math:`\pm 10 \%`, and using the formulae
    for capacitors in series or in parallel, calculate the range of
    possible values for each of the three arrangements in the
    experiment. If your values from step 5 lie outside these ranges,
    suggest possible reasons for error.

8.  Draw a line on the :math:`V` graph, parallel to the :math:`x`-axis,
    at :math:`V = \frac{5}{8} V_{MAX}`. For each of the three
    curves read the time when :math:`V = \frac{5}{8} V_{MAX}`.

9.  :math:`\tau = RC` is called the **time constant** of the circuit.
    (:math:`\tau` is Greek "tau"). This is the time taken for the
    potential difference (p.d.) to rise to :math:`\frac{5}{8}` of its
    final value (approximately). 

    a) Calculate the values of :math:`RC` using the values of capacitance
    found in step 5. 

    b) Compare these calculated times with times obtained experimentally 
    (analysis step 8).

10. :math:`V_{MAX}` should equal the battery voltage, but in the
    experiment it is lower. Why? 
    
    (Hint: take into account the resistance of the voltmeter).

.. |F1-2.1| image:: /images/34.png
.. |F1-2.2| image:: /images/35.png
.. |F1-2.3| image:: /images/36.png
