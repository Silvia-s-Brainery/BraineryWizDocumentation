.. _plotdefoscalefpy:

scale_factor Option
====================================================
Determines the scale factor of deformations. (Default=1)

Examples
--------

.. code-block:: python
   :caption: Example with scale_factor=2
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotDefo(plotmode=1,scale_factor=2)

.. raw:: html
       :file: files/scf2.html
	   
.. code-block:: python
   :caption: Example with scale_factor=10
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotDefo(plotmode=1,scale_factor=10)

.. raw:: html
       :file: files/scf10.html
