.. _plotmodelquivertcl:

QuiversSize Option
====================================================
Using this option user can define a size for arrows of elements section local axis. Attention that the size number should be mentioned just after the option. 

Example
--------

.. code-block:: tcl
   :caption: Example for QuiversSize equal to 0.002
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModel command 
   PlotModel QuiversSize 0.002

Watch resulted plot :ref:`here <plotmodelquiverpy>`.
	   
.. hint::

    the range of the quivers_size is around 0.002 value. But currently it strongly depends on the dimension of the model and to find the proper size of quivers user may needs try and error.