.. _plotmodellegendpy:

plot_legends Option
====================================================
A boolean that determines to show legends of various element on the up right corner of the plot. Users are able to turn of some elements by clicking on their corresponding legend. It helps some times in crowded models to investigate some other elements in details. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example for plot_legends=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, plot_legends=True)

.. raw:: html
       :file: files/legends.html
	   