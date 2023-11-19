.. _plotanimeonhovertcl:

OnHover Option
====================================================
By calling this option, nodes and element data hover on the plot. After calling this option, move mouse on the nodes or element to watch data on plot.

Example
--------

.. code-block:: tcl
   :caption: Example with OnHover
   
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
   PlotAnime OnHover

Watch resulted plot :ref:`here <plotmodelonhoverpy>`.
