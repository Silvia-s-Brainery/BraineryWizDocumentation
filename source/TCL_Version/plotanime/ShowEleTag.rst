.. _plotanimeshowelementstagtcl:

ShowEleTag Option
====================================================
By calling this option, tag of elements will be shown on plot.

Example
--------

.. code-block:: tcl
   :caption: Example with ShowEleTag
   
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
   PlotAnime ShowEleTag

Watch resulted plot :ref:`here <plotmodelshowelementstagpy>`.
	   
