.. _plotmodelelecolorpy:

Element_color_tag and Elements_color Options
========================================================================
Using these options, user becomes able to change the color of elements. Element_color_tag is list of Elements tag that user wants to assign a different color to them. Elements_color is list of colors of corresponding elements tag defined in Element_color_tag. 

Example
--------

.. code-block:: python
   :caption: Example for Element_color_tag and Elements_color to set color of element with tag 1 to 10 equal to defined colors in following
   
   import BraineryWiz as bz
   
   colors=['black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',]

   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, Element_color_tag=[i for i in range(1,11)], Elements_color=[colors[i] for i in range(1,11)])
   
.. raw:: html
       :file: files/ElementsColor.html
	   
.. note::

   It is obvious that length of Element_color_tag and Elements_color should be same, otherwise an error message will be appear and size of nodes won't change.
   
.. note::

   To get familiar with methods of defining colors, check :ref:`This Page <colorspy>`.