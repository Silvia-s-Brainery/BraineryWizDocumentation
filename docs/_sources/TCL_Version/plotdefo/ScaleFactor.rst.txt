.. _plotdefoscaleftcl:

ScaleFactor Option
====================================================
Determines the scale factor of deformations. (Default=1)

By calling this option, entered value after this option will be consider as the scale factor for plotting deformed shape of structure. (Default: 1)

Example
--------

.. code-block:: tcl
   :caption: Example with ScaleFactor equal to 10
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotDefo command 
   PlotDefo ScaleFactor 10

Watch resulted plot :ref:`here <plotdefoscalefpy>`.
