.. _plotanimerecorderrestpy:

RecorderReset() Command
====================================================
  
This command is for reseting the recording the recoded steps from the file.

.. code-block:: python
   :caption: The structure of the command
   
   import openseespy.opensees as ops
   import BraineryWiz as bz
   
   #...
   #codes of creating OpenSees model
   #...
   
   bz.RecorderReset()   #Reset the recorder to prevent adding new steps (slides) to previous recorded slides

* recorderfilename option [RecorderReset(recorderfilename='BrainRecorder.txt')]
   using recorderfilename option the filename of that defined for the recorder will be reset. If user deined a filename except the default filename for recorder (as explained in :ref:`Record <plotanimerecordpy>` command), Then to reset the defined filename, it should be defined for RecorderReset to reset it. (Default='BrainRecorder.txt')