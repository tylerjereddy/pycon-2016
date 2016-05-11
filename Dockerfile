FROM jupyter/minimal-notebook

#include the necessary files in the image at the default working path set by the Jupyter team
ADD shapefiles/ /home/jovyan/work/shapefiles/
ADD images/ /home/jovyan/work/images/
ADD *.p *.py *ipynb /home/jovyan/work/

#custom conda installation of dependencies for tutorial
#conda install of scipy master branch so that scipy.spatial.SphericalVoronoi may be used during tutorial
RUN conda create --name py27 python=2.7 numpy=1.11.0 matplotlib=1.5.1 ipywidgets=4.1.1
RUN /bin/sh -c 'source activate py27' && \
   conda install -c https://conda.anaconda.org/treddy scipy && \
   pip install triangle pyshp
