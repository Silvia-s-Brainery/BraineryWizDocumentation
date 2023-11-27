.. _plotmodelfiberspy:

plot_fibers Option
====================================================
A boolean that determines to show fibers or not. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example for plot_fibers=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, plot_fibers=True)

.. raw:: html
       :file: files/fibers.html
	   
.. hint::

    For each different material, BraineryWiz considers different color.