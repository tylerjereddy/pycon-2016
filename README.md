# pycon-2016
PyCon 2016 Computational Geometry Tutorial

This tutorial is available as a github repository that you may clone and run locally / interactively on your machine with the prerequisite [Jupyter / IPython kernel](http://jupyter.readthedocs.io/en/latest/install.html) installed. I have used `Python 2.7.11` in this tutorial and have not tested with `Python 3.x`. I encourage you to `git clone` and run `ipython notebook`, and execute all the cells in the `computational_geometry_tutorial.ipynb` *before* the tutorial as it will help us get through more material if we can minimize technical issues (please do feel free to contact me ahead of the tutorial for assistance with the installation, etc.).

It may be a good idea to use something like [`conda`](http://conda.pydata.org/docs/intro.html) to manage your python libraries if you have difficulties with installation. Here is a summary of the python libraries (beyond the standard library) and versions imported in the notebook at present, along with some notes:

library name | version used | notes
-------------|--------------|------
`circumcircle` | N/A | a small library included in the git repo
`triangle` | `20160203` | [PyPI page](https://pypi.python.org/pypi/triangle/)
`numpy` | `1.11.0` | http://www.numpy.org
`scipy` | `0.18.0.dev0+339c771` | https://www.scipy.org ; I built from master branch for use of `scipy.spatial.SphericalVoronoi` -- can use an older version if you don't mind skipping that example in tutorial
`matplotlib` | `1.5.1` | http://matplotlib.org
`ipywidgets` | `4.1.1` | https://github.com/ipython/ipywidgets
`pyshp` | `1.2.3` | [PyPI page](https://pypi.python.org/pypi/pyshp) ; use `import shapefile`
