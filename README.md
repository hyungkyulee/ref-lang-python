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
