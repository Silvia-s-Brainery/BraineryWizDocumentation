.. _realtimepy:

RealTimeObj Command (Plot at Each desired Time Step)
====================================================

Using this command users be able to plot the model and watch the deformation of the model during the analysis (:ref:`PlotAnime <plotanimepy>` creates animation at the end of analysis But this command shows the deformation at each time step). To use this command :

* User befor start of analysis should create the plot using RealTimeObj command.
* After creating the mentioned plot, by calling RealTimeUpdate command at each desired step the created plot (using RealTimeObj) will be updated.

**Attention: This command currently availables only on Jupyter Notebook Editors**

.. code-block:: python
   :caption: The structure of the command
   
   import openseespy.opensees as ops
   import BraineryWiz as bz
   
   #...
   #codes of creating OpenSees model
   #...
   
   numberOfSteps=100                       #Imagine the number of steps that want to be recorded are 100 steps
   
   bz.RealTimeObj(plotmode=1, **kwargs)    #Create the Plot
   
   for i in range(numberOfSteps):
      
	ops.analyze(1,0.01) #One step analysis
	bz.RealTimeUpdate(**RUkwargs)          #Update the created plot


RealTimeObj command options
----------------------------

* plotmode
   For different python editors there is a need to consider some settings to plot the figure. There are different modes to plot figures and if your editor does not show the figure change the number of the mode! (1,2,3,4,5,6)
   
* `**kwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: RealTimeObj **kwargs Options

   realtime/drawwire
   realtime/draw_nodes
   realtime/show_nodes_tag
   realtime/show_elemens_tag
   realtime/onhover
   realtime/title
   realtime/widthheight
   realtime/imagetypename
   realtime/legends
   realtime/verticalaxis
   realtime/RetainedConstrained
   realtime/nodessize
   realtime/nodescolor
   realtime/elecolor
   realtime/elesize
   realtime/supports_size
   
RealTimeUpdate command options
------------------------------
   
* `**RUkwargs`
    Stands for other options that user can use to provide desired changes in the plot. In the following the existing options are described.

.. toctree::
   :maxdepth: 1
   :caption: RealTimeUpdate **RUkwargs Options

   realtime/scalefactor
   realtime/autozoom