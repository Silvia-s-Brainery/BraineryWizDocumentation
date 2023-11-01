.. _plotmodelnodedatapy:

nodes_data_tag and nodes_data Options
====================================================
These options should be called together. Using these options any data that user wants, can be added to any node and by plotting model, the desired data will be shown on nodes hover!. In nodes_data_tag the tag of target nodes should be enter as a list and in nodes_data, any desired data corresponding to the entered tags should be enter as a list. By plotting the model the data will be shown on the nodes hover. (Default=[])

Example
--------

.. code-block:: python
   :caption: Example with considering a text for nodes with tag from 1 to 101
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, nodes_data_tag=[i+1 for i in range(100)], nodes_data=[f'My data on the element {i+1}' for i in range(100)], onhover_message=True)

.. raw:: html
       :file: files/Nodesdata.html
	   
.. hint::
   This is obvious that the :ref:`onhover_message <plotmodelonhoverpy>` option should be activate till the defined data be plotted.

.. hint::
   This option helps users by adding desired values to each node, user can check the values on the plot!
  
   