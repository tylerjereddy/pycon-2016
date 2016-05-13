FROM jupyter/minimal-notebook

#include the necessary files in the image at the default working path set by the Jupyter team
ADD shapefiles/ /home/jovyan/work/shapefiles/
ADD images/ /home/jovyan/work/images/
ADD *.p *.py *ipynb /home/jovyan/work/

USER root

#custom conda installation of dependencies for tutorial
#conda install of scipy master branch so that scipy.spatial.SphericalVoronoi may be used during tutorial
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
	'ipykernel' \
	'numpy=1.11.0' \ 
	'matplotlib=1.5.1' \
	'openblas' \
	&& /bin/bash -c "source activate /opt/conda/envs/python2 && conda install -c https://conda.anaconda.org/treddy scipy && conda clean -tipsy && pip install triangle pyshp ipywidgets && jupyter nbextension install --py widgetsnbextension && jupyter nbextension enable widgetsnbextension --py"

RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install
