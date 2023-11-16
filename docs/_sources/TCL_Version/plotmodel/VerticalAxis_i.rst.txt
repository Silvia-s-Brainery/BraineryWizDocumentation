.. _plotmodelverticaltcl:

VerticalAxis_i Option
====================================================
By calling this option, direction of vertical axis can be set. 3 or 2 or 1 can sit instead of i, that shows which directional value stands for vertical direction. Mostly it is 3 for everyone but sometimes someone need to set it equal 2 or 1. So, the option can be called in these ways: VerticalAxis_3 , VerticalAxis_2, VerticalAxis_1 (Default= VerticalAxis_3).

Example
--------

.. code-block:: tcl
   :caption: Example with VerticalAxis_2
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModel command 
   PlotModel VerticalAxis_2

Watch resulted plot :ref:`here <plotmodelverticalpy>`.
	   