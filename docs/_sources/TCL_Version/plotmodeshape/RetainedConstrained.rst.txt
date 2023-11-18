.. _plotmoderetconstcl:

ShowConstrained and ConstrainedSize Options
========================================================================
By calling ShowConstrained option retained and constrained nodes connected to each other will be shown on plot. ConstrainedSize option enable users to determine the size of lines and costrained and retained nodes. (Default size=6)

Example
--------

.. code-block:: tcl
   :caption: Example for ShowConstrained and ConstrainedSize (size=3) for ModeNumber 3
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModeShape command 
   PlotModeShape 3 ShowConstrained ConstrainedSize 3
   
Watch resulted plot :ref:`here <plotmodelretconspy>`.