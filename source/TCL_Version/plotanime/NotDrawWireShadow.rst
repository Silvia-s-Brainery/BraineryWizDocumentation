.. _plotanimewiretcl:

NotDrawWireShadow Option
====================================================
By calling this option, the wire shadow on nondeformed structure won't be shown.

Example
--------

.. code-block:: tcl
   :caption: Example with NotDrawWireShadow
   
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
   PlotAnime NotDrawWireShadow

Watch resulted plot :ref:`here <plotdefowirepy>`.