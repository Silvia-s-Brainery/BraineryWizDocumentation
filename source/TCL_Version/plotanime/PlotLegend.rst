.. _plotanimelegendtcl:

PlotLegend Option
====================================================
By calling this option, a legend of elements type appears on the top right corner of the polt and each element type can be turned on or off.

Example
--------

.. code-block:: tcl
   :caption: Example with PlotLegend
   
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
   PlotAnime PlotLegend

Watch resulted plot :ref:`here <plotmodellegendpy>`.


	   