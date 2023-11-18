.. _plotmodewiretcl:

NotDrawWireShadow Option
====================================================
By calling this option, the wire shadow on nondeformed structure won't be shown.

Example
--------

.. code-block:: tcl
   :caption: Example with NotDrawWireShadow for ModeNumber 3
   
   source BraineryWiz.tcl
   
   # ...
   # lines of Creating OpenSees model
   # ...
   
   # Call PlotModeShape command 
   PlotModeShape 3 NotDrawWireShadow

Watch resulted plot :ref:`here <plotdefowirepy>`.