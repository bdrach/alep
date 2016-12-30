.. meta::
  :description: A statistical sample models atomic processes to illustrate the half-life of a radioactive isotope. The steps described suggest the conservation of mass, charge, and energy in decay reactions.

H3-1: Radioactive Decay
=======================

Apparatus
---------

About 200 small cubes, marked :math:`\odot` and :math:`\otimes` on two
faces; two trays; 2 x :math:`500\text{ml}` beakers; periodic table of the elements; 2
sheets graph paper.

Introduction
------------

In this model of radioactive decay, the cubes represent atoms. They are
either parent (not decayed) atoms or daughter (decayed) atoms. When a cube
is thrown at random, if a marked face of the cube faces up, then the
atom has decayed.

Decay Model 1
-------------

(uses 1 tray and 1 beaker only)  

.. math::
   \text{Reaction: } & \qquad {^{12}_{5}B} \qquad \longrightarrow \qquad {^{A}_{Z}X + \beta^-} \\    
   &\widehat{\text{in the tray}} \qquad \qquad \quad \widehat{\text{discarded}}

1. Count the cubes. This is :math:`N_0`, the number of parent
   atoms of :math:`{^{12}_{5}B}` at time t=0.

2. Place all the cubes in a beaker and empty the beaker into a tray.
   Shake the tray until all the cubes lie flat (do not touch any cubes).

3. Each time you empty a beaker into a tray, 0.01s has elapsed. Record
   the time :math:`t=0.01`\ s. Discard cubes showing :math:`\odot` or
   :math:`\otimes` (these are atoms of :math:`{^{A}_{Z}X}` , the
   daughter atoms). Count and record :math:`N`, the number of cubes left
   in the tray.

4. Place the cubes now in the tray into the beaker. Empty the beaker
   into the tray and shake as before. Record :math:`t=0.02`\ s. Discard
   decayed atoms. Record the new number :math:`N` of cubes left in the
   tray.

5. Continue for :math:`t=0.03`, :math:`0.04`, :math:`0.05`, ...
   :math:`2.5`\ s, or until :math:`N=0`.

6. Tabulate your readings as follows:

   |H3-1.1|

Analysis
--------

1. Plot a graph of :math:`N` vs. :math:`t`. From the graph find the half
   life :math:`T_{\frac{1}{2}}`. The decay rate (lamda :math:`\lambda`) is 
   related to the half life as follows: :math:`\lambda = \ln{\frac{2}{T_{\frac{1}{2}}}}`

2. Using the formula: :math:`\frac{dN}{dt} = -\lambda N`, calculate the
   decay rate when :math:`t=0`. Find the graph's gradient at time :math:`t=0`;
   is this the same (approximately) as the calculated value?

3. On the same sheet of graph paper, plot another curve showing the
   number of daughter atoms.

4. Find :math:`A`, :math:`Z`, and :math:`X`. Is this atom stable?

Decay Model 2
-------------

(uses 2 trays and 2 beakers)

In this experiment, tray #1 contains :math:`{^{227}_{90}Th}` atoms and
tray #2 contains :math:`{^{A1}_{Z1}X}` daughter atoms. These daughter
atoms decay again and are discarded.

.. math::
   \text{Reactions: } \qquad {^{227}_{90}Th} \qquad & \longrightarrow \qquad {^{A1}_{Z1}X }+ \alpha \qquad \text{Half life } T_{\frac{1}{2}}\\    
   {^{A1}_{Z1}X } \qquad & \longrightarrow \qquad {^{A2}_{Z2}Y } + \alpha \qquad \text{Half life 11.7 days} 

1. Place all the cubes into tray #1, count them, and record number
   :math:`N_0` at time :math:`t=0`. Record for tray #2 that
   :math:`N_0 = 0` at :math:`t = 0`.

2. Place tray#1 cubes into beaker #1, return to tray #1 and shake tray
   to settle the cubes. Move cubes showing :math:`\otimes` into tray #2.
   Record :math:`N` for tray #1 and tray #2 at this time :math:`t=5`
   days.

3. FIRST: Place cubes from tray #2 into beaker #2. Return to tray #2
   and shake. Discard cubes showing :math:`\odot`.  

   SECOND: Place cubes from tray #1 into beaker #1. Return to tray #1
   and shake. Move cubes showing :math:`\otimes` to tray #2.  

   THEN: Count and record :math:`N` for trays #1 and #2 at
   :math:`t=10` days.

4. Continue repeating step 3, letting :math:`t =` 15, 20, 25, ... up to
   200 days. (Each time you perform step 3, :math:`t` advances by 5
   days).

5. Tabulate your readings as follows:

   |H3-1.2|

Analysis
--------

1. On the same piece of graph paper plot :math:`N` vs. :math:`t` for
   trays #1 and #2 to obtain two curves.

2. Using the #1 curve, find :math:`T_{\frac{1}{2}}` for
   :math:`{^{227}_{90}Th}`. Calculate :math:`\lambda` and thus find :math:`N`
   at :math:`t = 40` days (use :math:`N = N_0 e^{- \lambda t}`). Check
   that the value of :math:`N` at :math:`t = 40` days is about the same
   by using the graph, and note this value.

3. Explain carefully why the curve #2 has the shape that it does.

4. Use the reaction equations given above to determine :math:`A1`,
   :math:`Z1`, :math:`X` and also :math:`A2`, :math:`Z2`, and :math:`Y`.

Questions
---------

1. :math:`{^{A2}_{Z2}Y }` is unstable and decays. There follows a whole
   series of decays, ending with a stable atom, as follows:  

   .. math::
      {^{A2}_{Z2}Y} & \longrightarrow \text{?}+ \alpha & T_{\frac{1}{2}}&= 3.92 \text{s}\\    
      \text{?} & \longrightarrow \text{?}+ \alpha & T_{\frac{1}{2}} &= 1.8 \times 10^{-3} \text{s}\\ 
      \text{?} & \longrightarrow \text{?}+ \beta^{-} & T_{\frac{1}{2}}&= 36.1 \text{min}\\ 
      \text{?} & \longrightarrow \text{?}+ \alpha & T_{\frac{1}{2}}&= 2.15 \text{min}\\ 
      \text{?} & \longrightarrow \text{?}+ \beta^{-} & T_{\frac{1}{2}}&= 4.8 \text{min}

   Write down the above set of reactions, deducing each of the ?s,
   giving atomic mass, atomic number, and symbol in each case.

2. A sample of :math:`\ {^{227}_{90}Th}`, when left for 30 days, is found
   to contain a lot of :math:`{^{227}_{90}Th}`, :math:`{^{A1}_{Z1}X}`,
   and the final stable isotope.  There is very little of
   :math:`{^{A2}_{Z2}Y}` and the four intermediate isotopes. Why?

3. Draw a decay chain to map the complete series of seven decays from 
   :math:`{^{227}_{90}Th}` to the stable isotope.

.. |H3-1.1| image:: /images/65.png
.. |H3-1.2| image:: /images/66.png
