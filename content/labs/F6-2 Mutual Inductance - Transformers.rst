.. meta::
  :description: This exercise gives hands-on experience about the behavior of transformers relative to voltage, current, and energy loss when the electromagnetic flux from one coil induces a current in an adjacent coil.

F6-2: Mutual Inductance - Transformers
======================================

*NB: Students are advised to perform experiment F6-1 Self Inductance before 
attempting F6-2.*

Apparatus
---------

Coils 300 turns & 150 turns; wire for 20 turn & 10 turn coils; 2 iron
C-cores; C-core clip; 10\ :math:`\Omega` and 5\ :math:`\Omega`
resistors; CRO (oscilloscope); AC power supply; connecting leads (5
short).

*NB: This experiment requires mains electricity.*

Procedure
---------

1. Construct the following:  

   |F6-2.1| 

a) Using :math:`N_p` = 150 turns, :math:`N_s` = 10 turns. Measure and
   set :math:`V_{in} = V_p = 4`\ V peak. Measure :math:`V_s` peak.
   Calculate :math:`\frac{V_p}{V_s}` and :math:`\frac{N_p}{N_s}` and
   compare their values.  

b) Repeat a) with the following numbers of turns:  

   |F6-2.2| 

c) Keeping :math:`N_p = 150` turns and :math:`N_s = 300` turns, reduce
   :math:`V_{in} = V_p` to 2V peak. Measure :math:`V_s` peak, and
   calculate and compare :math:`\frac{V_p}{V_s}` and
   :math:`\frac{N_p}{N_s}`.  

d) Remove the clip from the iron cores, and remove one C-core. Place two coils, 
   one on each arm of a single C-core. Again use :math:`N_p = 150` turns and 
   :math:`N_s = 300` turns. Set :math:`V_{in} = V_p = 4`\ V peak. 
   Measure :math:`V_s`.

2. Construct the following with :math:`N_p = 300` turns,
   :math:`N_s = 150` turns, and an extra test coil of 10 turns as shown:
    
   |F6-2.3| 

a) Connect the CRO to measure :math:`V_p` peak, and set :math:`V_{in}`
   so that :math:`V_p = 4`\ V peak.  

b) Measure :math:`V_R` peak, and thus calculate :math:`I_p` peak, the
   current in the primary circuit.  

c) Measure :math:`V_T` peak, across the 10 turn test coil.  

d) Connect a 5\ :math:`\Omega` resistor between **A** and **B**, across
   the 150 turn secondary coil. Connect the CRO to measure :math:`V_p`
   and adjust :math:`V_{in}` so that :math:`V_p = 4`\ V peak.  

e) Measure :math:`V_R` peak, and thus calculate :math:`I_p` peak.  

f) Measure :math:`V_T` peak again. This should be about the same size as
   the value measured in procedure 2 c) above.

Theory
------

1. Flux :math:`\Phi` and induced emf :math:`E` are related by the
   following:  

   .. math::
      E_p = -N_p \frac{d \Phi_s}{dt} \label{eqnA} \tag{equation A}

   .. math::
      E_s = -N_s \frac{d \Phi_p}{dt}  \label{eqnB} \tag{equation B}

   The unit of flux is the weber - Wb.  When :math:`\Phi_s` (the flux through the secondary coil)
   :math:`=\Phi_p` (the flux through the primary coil), then:

     .. math::
         \frac{d \Phi_s}{dt} = \frac{d \Phi_p}{dt} 

   therefore:

   .. math::
      \frac{E_s}{N_s} = \frac{E_p}{N_p}

   thus:

   .. math::
      \frac{E_p}{E_s} = \frac{N_p}{N_s} 

   If the resistances of the primary coil and the secondary coil are
   both low and the currents flowing through them are not too large,
   then:  

   .. math::
      V_p \approx E_p \quad \text{and} \quad V_s \approx E_s 

2. The 10 turn coil is used to detect if the flux :math:`\Phi` in the
   iron core changes in the experiment. If
   :math:`\Phi = \Phi_{peak} \sin \omega t`, then :math:`\ref{eqnB}` can be
   used to show that :math:`V_T` peak :math:`\propto \Phi_{peak}`,
   provided that :math:`\omega` is constant.

Analysis
--------

1. Why, in experiment 1a) to 1c), are the two calculated ratios not
   exactly equal (hint: use the theory, and the fact that the primary
   coil has some resistance)?

2. Use the theory to explain the result of procedure 1 d).

3. According to Lenz's Law, the induced current in the secondary coil in
   the procedure 2 d) is in such a direction so as to **reduce**
   the flux in the core. However procedure 2 f) shows that the flux remains
   approximately constant. How is this possible (hint: consider the
   primary coil)?

4. Give an explanation in terms of power flow for the change in
   :math:`I_p` produced as a result of connecting the 5\ :math:`\Omega`
   resistor to the secondary coil.

5. 

   a) These coils are simple electrical transformers.  What are the causes of 
      power loss in a transformer, and how can they be minimised?  

   b) All electricity supply companies use transformers in their power
      distribution systems. Explain, giving reasons, how they are used.

.. |F6-2.1| image:: /images/55.png
.. |F6-2.2| image:: /images/57.png
.. |F6-2.3| image:: /images/58.png
