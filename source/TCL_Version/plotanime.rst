.. _plotanimetcl:

PlotAnime Command (Plot Animation)
====================================

PlotAnime is a command to create an animation from the desired analyed steps of OpenSees model. There are two commands beside PlotAnime command that provides required data for creating animation. The first command is **Record** command that is resposible to record data related to current analyed step of OpenSees model and **RecorderReset** to clear recorded data that stored using **Record** command.

.. code-block:: tcl
   :caption: The structure of the command
   
   source BraineryWiz.tcl
   
   #...
   #Lines related to creating model
   #...
   
   #Reset the recorder file if any recorded data exist in
   RecorderReset
   
   #Record desired steps
   {Loop of model analyze steps} {
      Record
   }
   
   #Creating animation from redorded steps
   PlotAnime
	
In the following the existing options for this command are described. User can use one or multiple of the following options after the command.

.. toctree::
   :maxdepth: 1
   :caption: PlotAnime Command Options

   plotanime/ScaleFactor
   plotanime/NotDrawWireShadow
   plotanime/PlotLegend
   plotanime/DrawNodesOff
   plotanime/ShowNodeTag
   plotanime/ShowEleTag
   plotanime/OnHover
   plotanime/title
   plotanime/VerticalAxis_i
   plotanime/RetainedConstrained
   plotanime/FigWidthHeight
