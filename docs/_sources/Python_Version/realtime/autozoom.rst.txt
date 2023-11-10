.. _plotrealzoompy:

auto_zoom Option
====================================================
A boolean that determines does the plot automaticaly change the zoom of plot or not. Versus plot animation that user by pausing button can set the desired zoom, in RealTimeObj it is not possible during the analysis change the initial zoom. So, for large displacements, the figure zoom will changes if this option was set to True. (Default=True)
	   
.. code-block:: python
   :caption: Example for auto_zoom=False
   
   import openseespy.opensees as ops
   import BraineryWiz as bz
   
   #...
   #codes of creating OpenSees model
   #...
   
   numberOfSteps=100    #Imagine the number of steps that want to be recorded are 100 steps
   
   bz.RecorderReset()   #Reset the recorder to prevent adding new steps (slides) to previous recorded slides
   
   for i in range(numberOfSteps):
      
	ops.analyze(1,0.01) #One step analysis
	bz.Record(auto_zoom=False)         #Record the analyzed step