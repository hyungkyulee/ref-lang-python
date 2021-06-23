# ref-lang-python
Reference Code examples - Python 


## tensorflow

### mac osx
 - miniconda installation : https://docs.conda.io/en/latest/miniconda.html#macosx-installers
 - conda --version
 - conda install jupyter
 - conda env create -v -f tensorflow.yml
 ```yml
 name: tensorflow
 
dependencies:
    - python=3.8
    - pip>=19.0
    - jupyter
    - scikit-learn
    - scipy
    - pandas
    - pandas-datareader
    - matplotlib
    - pillow
    - tqdm
    - requests
    - h5py
    - pyyaml
    - flask
    - boto3
    - pip:
        - tensorflow==2.4
        - bayesian-optimization
        - gym
        - kaggle
 ```

 - conda activate tensorflow (enter to tensorflow mode) 
   * import tensorflow will show error without activating tensorflow
(base) ➜  ~ conda activate tensorflow
(tensorflow) ➜  ~ python
 ```python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> print(tf.__version__)
2.4.0
>>> 
KeyboardInterrupt
>>> q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'q' is not defined
>>> quit()
 ```
 
 - embedd tensorflow to kernel for jupyter to use tensorflow
 ```sh
(base) ➜  ~ conda activate tensorflow
(tensorflow) ➜  ~ python -m ipykernel install --user --name tensorflow --display-name "Python 3.8 (tensorflow)"
Installed kernelspec tensorflow in /Users/albert/Library/Jupyter/kernels/tensorflow
(tensorflow) ➜  ~ 
(tensorflow) ➜  ~ jupyter notebook
[I 00:39:54.191 NotebookApp] Serving notebooks from local directory: /Users/albert
[I 00:39:54.191 NotebookApp] Jupyter Notebook 6.2.0 is running at:
[I 00:39:54.191 NotebookApp] http://localhost:8888/?token=cb9d532069252ca9222409941c5ecd3df19df5ea891ad8ae
[I 00:39:54.191 NotebookApp]  or http://127.0.0.1:8888/?token=cb9d532069252ca9222409941c5ecd3df19df5ea891ad8ae
[I 00:39:54.191 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 00:39:54.205 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///Users/albert/Library/Jupyter/runtime/nbserver-41282-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=cb9d532069252ca9222409941c5ecd3df19df5ea891ad8ae
     or http://127.0.0.1:8888/?token=cb9d532069252ca9222409941c5ecd3df19df5ea891ad8ae
[I 00:40:51.126 NotebookApp] Creating new notebook in 
[I 00:40:52.113 NotebookApp] Kernel started: 889dda01-bed7-4fba-af6f-c1608c499fb7, name: tensorflow
 ```
 * a new jupyter notebook file should be created with 'python 3.x (tensorflow)' option on the new's dropdown menuto use tensorflow
