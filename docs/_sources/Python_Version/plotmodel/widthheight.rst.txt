.. _plotmodelwidthheightpy:

fig_width and fig_height Options
====================================================
Using these options the dimension of the plot can be determined. (Default: fig_width=1000 and fig_height=800)

Example
--------

.. code-block:: python
   :caption: Example fig_width=600 and fig_height=600
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, fig_width=600, fig_height=600)

.. raw:: html
       :file: files/widthheight.html
	   
