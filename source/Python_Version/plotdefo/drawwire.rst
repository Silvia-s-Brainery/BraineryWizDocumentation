.. _plotdefowirepy:

draw_wire_shadow Option
====================================================
A boolean that determines to draw the undeformed structe as a shadow or not. By setting this option equal to off the  (Default=True)

Examples
--------

.. code-block:: python
   :caption: Example with considering draw_wire_shadow=False
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, draw_wire_shadow=False)

.. raw:: html
       :file: files/wirefalse.html