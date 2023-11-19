.. _plotanimeretconstcl:

ShowConstrained and ConstrainedSize Options
========================================================================
By calling ShowConstrained option retained and constrained nodes connected to each other will be shown on plot. ConstrainedSize option enable users to determine the size of lines and costrained and retained nodes. (Default size=6)

Example
--------

.. code-block:: tcl
   :caption: Example for ShowConstrained and ConstrainedSize (size=3)
   
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
   PlotAnime ShowConstrained ConstrainedSize 3
   
Watch resulted plot :ref:`here <plotmodelretconspy>`.