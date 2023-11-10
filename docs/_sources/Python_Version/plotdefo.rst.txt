.. _plotdefopy:

PlotDefo Command (Plot Deformation)
====================================

PlotDefo is the command that should be used to plot the deformed model (At the current step).

.. code-block:: python
   :caption: The structure of the command
   
   PlotDefo (plotmode=3, **kwargs)
	
* plotmode
   For different python editors there is a need to consider some settings to plot the figure. There are different modes to plot figures and if your editor does not show the figure change the number of the mode! (1,2,3,4,5,6)
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: PlotDefo Command Options

   plotdefo/scalefactor
   plotdefo/drawwire
   plotdefo/draw_nodes
   plotdefo/show_nodes_tag
   plotdefo/show_elemens_tag
   plotdefo/onhover
   plotdefo/title
   plotdefo/widthheight
   plotdefo/eledata
   plotdefo/nodedata
   plotdefo/imagetypename
   plotdefo/legends
   plotdefo/verticalaxis
   plotdefo/RetainedConstrained