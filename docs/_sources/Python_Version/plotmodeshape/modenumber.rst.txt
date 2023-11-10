.. _plotmodenumberpy:

mode_number Option
====================================================
A digit the determines the number of desired mode to be plotted.

.. code-block:: python
   :caption: Example with mode_number=3
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModeShape command for plotting mode number 3
   bz.PlotModeShape(plotmode=3, mode_number=3)