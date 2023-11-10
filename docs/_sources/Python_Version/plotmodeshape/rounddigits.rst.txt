.. _plotmoderoundpy:

round_digit Option
====================================================
Determines the number of digits after dot to round and prevent of showing long numbers.

.. code-block:: python
   :caption: Example with round_digit=3
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModeShape command 
   bz.PlotModeShape(plotmode=3, round_digit=3)