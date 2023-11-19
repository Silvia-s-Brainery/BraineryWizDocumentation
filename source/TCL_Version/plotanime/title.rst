.. _plotanimetitletcl:

title Option
====================================================
By calling this option, defined word after the title command will be consider as the title of plot. (Default: BraineryWiz)

Example
--------

.. code-block:: tcl
   :caption: Example with title equal to NewTitle
   
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
   PlotAnime title NewTitle

Watch resulted plot :ref:`here <plotmodeltitlepy>`.
	   
