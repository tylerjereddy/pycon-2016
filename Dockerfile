FROM jupyter/datascience-notebook

#conda install of scipy master branch so that scipy.spatial.SphericalVoronoi may be used during tutorial
RUN conda install -c https://conda.anaconda.org/treddy scipy
