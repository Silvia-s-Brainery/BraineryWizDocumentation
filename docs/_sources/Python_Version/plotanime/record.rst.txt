.. _plotanimerecordpy:

Record() Command
====================================================

This command is for recording the current step analyzed data and add them as a slide to previous recoded data. The structure of the command is in this way:

.. code-block:: python
   
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
	
* recorderfilename option [Record(recorderfilename='BrainRecorder.txt')]
   using recorderfilename option the filename of the recoding data can be changed. User should know that if except of default filename, another name be selected, then the selected filename also should be define for PlotAnime command using :ref:`recorderfilename <plotanimerecordfnamepy>`, option. (Default='BrainRecorder.txt')