.. _plotmodedrawnodestcl:

DrawNodesOff Option
====================================================
By calling this option, nodes that are connected to at least an element won't be shown.

Examples
--------

.. code-block:: tcl
   :caption: Example with considering DrawNodesOff for ModeNumber 3
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModeShape command 
   PlotModeShape 3 DrawNodesOff

Watch resulted plot :ref:`here <plotmodeldrawnodespy>`.
	   
.. hint::
   Attention that this option only affects on the nodes that are connected to the elements and has no effect on the free nodes (not connectoed to any element) and free nodes always will be drawn or plotted.