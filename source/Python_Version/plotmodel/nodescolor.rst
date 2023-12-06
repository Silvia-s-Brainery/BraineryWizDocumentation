.. _plotmodelnodecolorpy:

Nodes_color_tag and Nodes_color Options
========================================================================
Using these options, user becomes able to change color of nodes. Nodes_color_tag is list of Nodes tag that user wants to assign a different color to them. Nodes_color is list of colors of corresponding nodes tag defined in Nodes_color_tag. 

Example
--------

.. code-block:: python
   :caption: Example for Nodes_color_tag and Nodes_color to set color of nodes with tag 1 to 10 equal to colors defined in following
   
   import BraineryWiz as bz
   colors=['black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',]
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command (Using :ref:`sizing options <plotmodelnodesizepy>` for better plot size of nodes increased)
   bz.PlotModel(plotmode=1, Nodes_color_tag=[i for i in range(1,11)], Nodes_color=[colors[i] for i in range(1,11)], Nodes_Size_tag=[i for i in range(1,11)], Nodes_Size=[15 for i in range(1,11)])
   
.. raw:: html
       :file: files/NodesColor.html
	   
.. tip::
   
   To assign one color to all nodes, do not fill **Nodes_color_tag** with anything and abandon it, then set **Nodes_color** equal to the desired color in string (str) format.
   
   .. code-block:: python
      :caption: Example for setting all nodes color to red
      
      import BraineryWiz as bz
      
      # ...
      # Create the OpenSees model
      # ...
      
      # Call PlotModel command 
      bz.PlotModel(plotmode=1, Nodes_color='red')  
	   
.. note::

   It is obvious that length of Nodes_color_tag and Nodes_color should be same, otherwise an error message will be appear and color of nodes won't change.
   
.. note::

   To get familiar with methods of defining colors, check :ref:`This Page <colorspy>`.