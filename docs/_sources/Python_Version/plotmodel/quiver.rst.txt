.. _plotmodelquiverpy:

quivers_size Option
====================================================
Using this option user can define a size for arrows of elements section local axis. (Default=None)

Example
--------

.. code-block:: python
   :caption: Example for quivers_size=0.002
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, quivers_size=0.002)

.. raw:: html
       :file: files/quiver.html
	   
.. hint::

    the range of the quivers_size is around 0.002 value. But currently it strongly depends on the dimension of the model and to find the proper size of quivers user may needs try and error.