.. _plotmodelshownodestagpy:

show_nodes_tag Option
====================================================
A boolean that determines to show nodes tag or not. (Default=False)

Example
--------

.. code-block:: python
   :caption: Example with show_nodes_tag=True
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, show_nodes_tag=True)

.. raw:: html
       :file: files/ShowNodesTag.html
	   
