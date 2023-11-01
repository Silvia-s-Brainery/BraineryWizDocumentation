.. _plotmodelimgtypnamepy:

image_type and image_filename Options
====================================================
`Users can take a pricture of the plot by clicking on the camera sign on the up right corner of the plot. Using image_type the type of image can be determined (Types: 'png' |'jpeg' |'svg' |'webp'). Using image_filename the name of the image file can be determined. (Defaults: image_type='png' and image_filename='BraneryWiz')`

Example
--------

.. code-block:: python
   :caption: Example with image_type='jpeg' and image_filename='NewFile' 
   
   import BraineryWiz as bz
   
   # ...
   # Create the OpenSees model
   # ...
   
   # Call PlotModel command 
   bz.PlotModel(plotmode=3, image_type='jpeg', image_filename='NewFile' )

.. raw:: html
       :file: files/image.html
	   
