.. _plotanimepy:

PlotAnime Command (Plot Animation)
====================================================

PlotAnime is the command that should be used to show **an animation** of **recorded steps**. Users initially should record the desired steps using :ref:`Record() <plotanimerecordpy>` command. The :ref:`Record() <plotanimerecordpy>` command records the required data for creating animation and in each desired step user should call the :ref:`Record() <plotanimerecordpy>` command. Finally, when all desired steps recording finished, by calling PlotAnime command, the animation of the plot will be shown. Using :ref:`RecordReset() <plotanimerecorderrestpy>` command the recorded steps will be reset.

.. code-block:: python
   :caption: The structure of the command
   
   import openseespy.opensees as ops
   import BraineryWiz as bz
   
   #...
   #codes of creating OpenSees model
   #...
   
   numberOfSteps=100    #Imagine the number of steps that want to be recorded are 100 steps
   
   bz.RecorderReset()   #Reset the recorder to prevent adding new steps (slides) to previous recorded slides
   
   for i in range(numberOfSteps):
      
	ops.analyze(1,0.01) #One step analysis
	bz.Record()         #Record the analyzed step
   
   
   bz.PlotAnime (plotmode=3, dt=0.01, **kwargs) #Show animation of the recorded steps

   
Click on **Pause** botton and then click on **Play** button on the below animation to watch the created animation as a sample.

   
.. raw:: html
       :file: plotanime/files/anime.html

   
PlotAnime command options
-------------------------

* plotmode
   For different python editors there is a need to consider some settings to plot the figure. There are different modes to plot figures and if your editor does not show the figure change the number of the mode! (1,2,3,4,5,6)

* dt
   Determines the time distance between steps. (Default=0.01)
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: PlotAnime **kwargs Options

   plotanime/scalefactor
   plotanime/drawwire
   plotanime/draw_nodes
   plotanime/show_nodes_tag
   plotanime/show_elemens_tag
   plotanime/onhover
   plotanime/title
   plotanime/widthheight
   plotanime/eledata
   plotanime/nodedata
   plotanime/imagetypename
   plotanime/legends
   plotanime/verticalaxis
   plotanime/RetainedConstrained
   plotanime/recorderfilename

.. toctree::
   :maxdepth: 1
   :caption: PlotAnime Related Commands

   plotanime/recorderreset
   plotanime/record