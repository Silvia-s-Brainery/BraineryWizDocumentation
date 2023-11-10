.. _plotanimegifpy:

PlotAnimeGif command (Create Animation in gif format)
======================================================

The structure of this command is completely compatible with :ref:`PlotAnime <plotanimepy>` command but this command creates a gif file from the recorded steps. Just use PlotAnimeGif instead of PlotAnime. To create an animation or gif of animation:

* Using :ref:`Record() <plotanimerecordpy>` command record each step that are desired to animate.
* Using :ref:`PlotAnime <plotanimepy>` or PlotAnimeGif create the animation. 

**Attention:** The :ref:`Record() <plotanimerecordpy>` command add the current analyzed step to all previously recorded steps. It is important to remember to use :ref:`RecordReset() <plotanimerecorderrestpy>` command to reset the recorder and delete the recorded steps for a new animation. Also remeber that generating gif file usually **takes long time!**


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
   
   
   bz.PlotAnimeGif (**kwargs) #Show animation of the recorded steps

   
Click :download:`here <plotanimegif/files/Anime.gif>` to downlad the created gif file as a sample.

   
PlotAnimeGif command options
----------------------------
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: PlotAnimeGif **kwargs Options

   plotanimegif/scalefactor
   plotanimegif/drawwire
   plotanimegif/draw_nodes
   plotanimegif/show_nodes_tag
   plotanimegif/show_elemens_tag
   plotanimegif/onhover
   plotanimegif/title
   plotanimegif/widthheight
   plotanimegif/verticalaxis
   plotanimegif/RetainedConstrained
   plotanimegif/recorderfilename

.. toctree::
   :maxdepth: 1
   :caption: PlotAnimeGif Related Commands

   plotanimegif/recorderreset
   plotanimegif/record