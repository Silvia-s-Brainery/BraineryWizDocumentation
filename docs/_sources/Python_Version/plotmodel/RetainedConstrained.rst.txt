.. _plotmodelretconspy:

show_constrained and not_show_retained_list and constrained_size Options
========================================================================
Setting show_constrained equal True will cause to plot the retained and constrained nodes connected to each other. constrained_size enable users to determine the size of lines and costrained and retained nodes. By defining list of retained nodes tag and assign to not_show_retained_list, the nodes that their tags are mentioned in the list and nodes that are constrained to them won't be shown using show_constrained. (Default: show_constrained=True,  not_show_retained_list=[], constrained_size=6)

Example
--------

.. code-block:: python
   :caption: Example for show_constrained=True, constrained_size=6
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, show_constrained=True, constrained_size=6)
   
.. raw:: html
       :file: files/retained.html