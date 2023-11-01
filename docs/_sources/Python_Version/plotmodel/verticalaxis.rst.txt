.. _plotmodelverticalpy:

vertical_axis Option
====================================================
Using this option user can define the dimension related to vertical axis. BraineryWiz considers the 3rd value of the enetered points as the values related to the vertical axis. For other cases using this option users can determine the vertical axis dimension. (Default=3)

Example
--------

.. code-block:: python
   :caption: Example for vertical_axis=2
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, vertical_axis=2)

.. raw:: html
       :file: files/vertical.html
	   