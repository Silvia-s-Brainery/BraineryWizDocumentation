.. _plotmodelpy:

PlotModel Command (Plot Model)
==============================

PlotModel is the command that should be used to plot the model. The structure of the command is in this way:

.. code-block:: python

   PlotModel (plotmode=3, **kwargs)
	
* plotmode
   For different python editors there is a need to consider some settings to plot the figure. There are different modes to plot figures and if your editor does not show the figure change the number of the mode! (1,2,3,4,5,6)
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: PlotModel Command Options

   plotmodel/draw_nodes
   plotmodel/show_nodes_tag
   plotmodel/show_elemens_tag
   plotmodel/onhover
   plotmodel/title
   plotmodel/widthheight
   plotmodel/eledata
   plotmodel/nodedata
   plotmodel/imagetypename
   plotmodel/quiver
   plotmodel/fibers
   plotmodel/integratepoints
   plotmodel/legends
   plotmodel/verticalaxis
   plotmodel/RetainedConstrained