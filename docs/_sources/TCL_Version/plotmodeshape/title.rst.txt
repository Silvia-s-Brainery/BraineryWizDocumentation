.. _plotmodetitletcl:

title Option
====================================================
By calling this option, defined word after the title command will be consider as the title of plot. (Default: BraineryWiz)

Example
--------

.. code-block:: tcl
   :caption: Example with title equal to NewTitle for ModeNumber 3
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModeShape command 
   PlotModeShape 3 title NewTitle

Watch resulted plot :ref:`here <plotmodeltitlepy>`.
	   
