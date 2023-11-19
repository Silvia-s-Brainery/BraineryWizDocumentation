.. _plotanimescaleftcl:

ScaleFactor Option
====================================================
Determines the scale factor of deformations. (Default=1)

By calling this option, entered value after this option will be consider as the scale factor for plotting deformed shape of structure. (Default: 1)

Example
--------

.. code-block:: tcl
   :caption: Example with ScaleFactor equal to 10
   
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
   PlotAnime ScaleFactor 10

Watch resulted plot :ref:`here <plotdefoscalefpy>`.
