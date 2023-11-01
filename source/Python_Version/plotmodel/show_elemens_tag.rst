.. _plotmodelshowelementstagpy:

show_elemens_tag Option
====================================================
A boolean that determines to show elements tag or not. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example with show_elemens_tag=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, show_elemens_tag=True)

.. raw:: html
       :file: files/ShowElementsTag.html
	   
