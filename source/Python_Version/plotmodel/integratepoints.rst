.. _plotmodelintpointspy:

plot_integration_points Option
====================================================
A boolean that determines to show integration points or not. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example for plot_integration_points=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, plot_integration_points=True)

.. raw:: html
       :file: files/IntegratePoints.html
	   