.. _installationTCL:

Installation
============

TCL BraineryWiz consist of two files as mentioned in **the following and should be download at first step:**

	* :download:`BraineryWiz.exe <http://www.bijansayyafzadeh.com/OpenSees/BraineryWizTCL/BraineryWiz.exe>`
	* :download:`BraineryWiz.tcl <http://www.bijansayyafzadeh.com/OpenSees/BraineryWizTCL/BraineryWiz.tcl>`
	
After downloading above files, now **the following steps should be done to install** it and make it ready to use:

   #. Move the downloaded BraineryWiz.exe to the folder that OpenSees.exe located (The folder should be in PATH of the system). BraineryWiz.exe should be located beside the OpenSees.exe But if you are using OpenSees.exe localy beside your .tcl files then you have you put BraineryWiz.exe beside the .tcl file.
   
      .. tip::
   
	        Attention: OpenSees.exe naturally is located in …/TCL/bin folder and this folder is located in the path of your system.
		 
   #. Copy BraineryWiz.tcl in the folder of your .tcl model (files) to source it.
   #. Using tcl source command source BraineryWiz and now it is ready to be used.


.. code-block:: tcl
   :caption: Example of how to call BraineryWiz.tcl 

   source BraineryWiz.tcl
	
   # ...
   # Modeling commands in TCL language
   # ...
	
   # Plotting commands of BraineryWiz to plot above created model
	
	
