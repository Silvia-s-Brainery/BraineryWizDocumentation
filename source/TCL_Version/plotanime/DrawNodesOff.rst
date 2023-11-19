.. _plotanimedrawnodestcl:

DrawNodesOff Option
====================================================
By calling this option, nodes that are connected to at least an element won't be shown.

Examples
--------

.. code-block:: tcl
   :caption: Example with considering DrawNodesOff
   
   source BraineryWiz.tcl
   
   #...
   #Lines related to creating model
   #...
   
   #Reset the recorder file if any recorded data exist in
   RecorderReset
   
   #Record desired steps
   {Loop of model analyze steps} {
      Record
   }
   
   #Creating animation from redorded steps
   PlotAnime DrawNodesOff

Watch resulted plot :ref:`here <plotmodeldrawnodespy>`.
	   
.. hint::
   Attention that this option only affects on the nodes that are connected to the elements and has no effect on the free nodes (not connectoed to any element) and free nodes always will be drawn or plotted.