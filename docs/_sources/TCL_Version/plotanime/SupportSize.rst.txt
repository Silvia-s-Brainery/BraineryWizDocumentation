.. _plotanimesupportsftcl:

SupportSize and SupportsDescOff Options
====================================================
Using this option user can define a size supports size. Attention that the size number should be mentioned just after the option. By assigning a value to SupportSize option, supports will be plotted. Supports types are shown based on colors and decription of colors are also plotted in the bottom of the plot. By mentioning SupportsDescOff in options, supports description will be hidden.

Example
--------

.. code-block:: tcl
   :caption: Example for SupportSize equal to 0.2
   
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
   PlotAnime SupportSize 0.2

Watch resulted plot :ref:`here <plotmodelsupportssizepy>`.
