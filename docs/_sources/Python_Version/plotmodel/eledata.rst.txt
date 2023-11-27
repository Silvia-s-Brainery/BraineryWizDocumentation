.. _plotmodeleledatapy:

elements_data_tag and elements_data Options
====================================================
These options should be called together. Using these options any data that user wants, can be added to any elements and by plotting model, the desired data will be shown on element hover!. In elements_data_tag the tag of target elements should be enter as a list and in elements_data, any desired data corresponding to the entered tags should be enter as a list. By plotting the model the data will be shown on the element hover. (Default=[])

Example
--------

.. code-block:: python
   :caption: Example with considering a text for elements with tag from 1 to 101
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=1, elements_data_tag=[i+1 for i in range(100)], elements_data=[f'My data on the element {i+1}' for i in range(100)], onhover_message=True)

.. raw:: html
       :file: files/Eledata.html
	   
.. hint::
   This is obvious that the :ref:`onhover_message <plotmodelonhoverpy>` option should be activate till the defined data be plotted.

.. hint::
   This option helps users to investigate element values on the plot. By adding desired values to each element user can check the values on the plot!
  
   