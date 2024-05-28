.. _plotmodelsupportssizepy:

supports_size and show_supports_desc Options
========================================================================
Using these options, user ables to plots supports. supports_size is for assigning size of supports and by assigning a value, supports will be plotted. Supports types are shown based on colors and decription of colors are also plotted in the bottom of the plot. By assigning False to show_supports_desc, supports description will be hidden.

Example
--------

.. code-block:: python
   :caption: Example for plotting supports with supports_size equal to 0.2
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, supports_size=0.2)
   
.. raw:: html
       :file: files/supports_size.html

.. tip::
   
   Because of some technical problems, size of cones could change!. Currently to handle this issue, user can assign various size for **each type of supports**. By assigning a list with 3 values to supports_size, the first value will be consider as size of Transitional supports (Green), second value will be consider and rotational supports (Blue) and third will be consider for fixed supports (Red).
   
   .. code-block:: python
      :caption: Example for setting 3 different values for supports_size.
      
      import BraineryWiz as bz
      
      # ...
      # Create the OpenSees model
      # ...
	  
	  Transitional_size=0.2
	  Rotational_size=0.1
	  Fixed_size=0.3
      
      # Call PlotModel command 
      bz.PlotModel(plotmode=1, supports_size=[Transitional_size,Rotational_size,Fixed_size])  
