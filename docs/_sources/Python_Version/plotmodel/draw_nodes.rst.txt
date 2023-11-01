.. _plotmodeldrawnodespy:

draw_nodes Option
====================================================
A boolean that determines to draw nodes connected to the elements or do not draw the nodes that are connected to the elements. (Default=True)

Examples
--------

.. code-block:: python
   :caption: Example with considering draw_Nodes
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command with 
   bz.PlotModel(plotmode=6, draw_nodes=True)

.. raw:: html
       :file: files/DrawNodesTrue.html
	   
.. code-block:: python
   :caption: Example without considering draw_Nodes
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command with 
   bz.PlotModel(plotmode=6, draw_nodes=True)

.. raw:: html
       :file: files/DrawNodesFalse.html
	   
.. hint::
   Attention that this option only affects on the nodes that are connected to the elements and has no effect on the free nodes (not connectoed to any element) and free nodes always will be drawn or plotted.