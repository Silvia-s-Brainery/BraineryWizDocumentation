.. _plotanimewidthheighttcl:

FigWidth and FigHeight Options
====================================================
Using these options the dimension of the plot can be determined. (Default: FigWidth=1000 and FigHeight=800)

Example
--------

.. code-block:: tcl
   :caption: Example with FigWidth=600 and FigHeight=600
   
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
   PlotAnime FigWidth 600 FigHeight 600

Watch resulted plot :ref:`here <plotmodelwidthheightpy>`.
