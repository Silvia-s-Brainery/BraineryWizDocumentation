.. _plotmodelonhoverpy:

onhover_message Option
====================================================
A boolean that determines nodes and element data hover on the plot. After activating this option, move mouse on the nodes or element to watch data on plot. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example with onhover_message=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, onhover_message=True)

.. raw:: html
       :file: files/OnHover.html
	   
