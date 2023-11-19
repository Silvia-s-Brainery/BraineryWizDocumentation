.. _plotanimeverticaltcl:

VerticalAxis_i Option
====================================================
By calling this option, direction of vertical axis can be set. 3 or 2 or 1 can sit instead of i, that shows which directional value stands for vertical direction. Mostly it is 3 for everyone but sometimes someone need to set it equal 2 or 1. So, the option can be called in these ways: VerticalAxis_3 , VerticalAxis_2, VerticalAxis_1 (Default= VerticalAxis_3).

Example
--------

.. code-block:: tcl
   :caption: Example with VerticalAxis_2
   
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
   PlotAnime VerticalAxis_2

Watch resulted plot :ref:`here <plotmodelverticalpy>`.
	   