.. _plotmodelnodesizepy:

Nodes_Size_tag and Nodes_Size Options
========================================================================
Using these options, user becomes able to change the size of nodes. Nodes_Size_tag is list of Nodes tag that user wants to assign a different size to them. Nodes_Size is list of size values of corresponding nodes tag defined in Nodes_Size_tag. 

Example
--------

.. code-block:: python
   :caption: Example for Nodes_Size_tag and Nodes_Size to set size of nodes with tag 1 to 10 equal to 15
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, Nodes_Size_tag=[i for i in range(1,11)], Nodes_Size=[15 for i in range(1,11)])
   
.. raw:: html
       :file: files/NodesSize.html
	   
.. note::

   It is obvious that length of Nodes_Size_tag and Nodes_Size should be same, otherwise an error message will be appear and size of nodes won't change.