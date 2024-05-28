.. _plotmodetcl:

PlotModeShape Command (Plot ModeShape)
========================================

PlotModeShape is the command for plotting requested mode shape.

.. code-block:: tcl
   :caption: The structure of the command
   
   source BraineryWiz.tcl
   
   PlotModeShape ModeNumber

.. note::
   
   IT IS VERY IMPORTANT THAT USER ENTER THE “ModeNumber” VALUE EXACTLY AFTER “PlotModeShape” COMMAND LIKE WHAT HAS SHOWN IN ABOVE. ModeNumber is an integer that detemines the requested mode number to plot.
   
In the following the existing options for this command are described. User can use one or multiple of the following options after the command.

.. toctree::
   :maxdepth: 1
   :caption: PlotModeShape Command Options

   plotmodeshape/ScaleFactor
   plotmodeshape/NotDrawWireShadow
   plotmodeshape/PlotLegend
   plotmodeshape/DrawNodesOff
   plotmodeshape/ShowNodeTag
   plotmodeshape/ShowEleTag
   plotmodeshape/OnHover
   plotmodeshape/title
   plotmodeshape/VerticalAxis_i
   plotmodeshape/RetainedConstrained
   plotmodeshape/FigWidthHeight
   plotmodeshape/SupportSize