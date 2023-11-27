.. _plotmodelelesizepy:

Elements_width Option
========================================================================
Using Elements_width option, user becomes able to define an integer that specifies the elements width.

Example
--------

.. code-block:: python
   :caption: Example for Elements_width to set size of all elements equal to 6
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, Elements_width=6)
   
.. raw:: html
       :file: files/EleSize.html
	   
.. note::

   Currently it is only possible to change width of all elemets and it is not possible yet to assign various width to various elements.