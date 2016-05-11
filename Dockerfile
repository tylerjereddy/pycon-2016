FROM jupyter/datascience-notebook

#conda install of scipy master branch so that scipy.spatial.SphericalVoronoi may be used during tutorial
RUN conda install -c https://conda.anaconda.org/treddy scipy

#include the necessary files in the image at the default working path set by the Jupyter team
ADD shapefiles/ /home/jovyan/work/shapefiles/
ADD images/ /home/jovyan/work/images/
ADD *.p *.py *ipynb /home/jovyan/work/
