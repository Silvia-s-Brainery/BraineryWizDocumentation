.. _plotmodepy:

PlotModeShape Command (Plot mode shape)
=======================================

PlotModeShape command is for plotting one of the modeshapes of the model. This command initially using eigen command execute a eigen analysis and according results of the eigen analysis plots the requested mode shape. 

.. code-block:: python
   :caption: The structure of the command
   
   PlotModeShape (plotmode=3, **kwargs)
   
* plotmode
   For different python editors there is a need to consider some settings to plot the figure. There are different modes to plot figures and if your editor does not show the figure change the number of the mode! (1,2,3,4,5,6)
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: PlotModeShape Command Options

   plotmodeshape/modenumber
   plotmodeshape/rounddigits
   plotmodeshape/scalefactor
   plotmodeshape/drawwire
   plotmodeshape/draw_nodes
   plotmodeshape/show_nodes_tag
   plotmodeshape/show_elemens_tag
   plotmodeshape/onhover
   plotmodeshape/title
   plotmodeshape/widthheight
   plotmodeshape/eledata
   plotmodeshape/nodedata
   plotmodeshape/imagetypename
   plotmodeshape/legends
   plotmodeshape/verticalaxis
   plotmodeshape/RetainedConstrained