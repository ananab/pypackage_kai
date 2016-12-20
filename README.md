# pypackage_kai
dsci 524 lab 2
[![Build Status](https://travis-ci.org/ananab/pypackage_kai.svg?branch=master)](https://travis-ci.org/ananab/pypackage_kai)

The structure of this repository is summarized in the table below:

|directory|file|nature|usage|
|---------|----|------|-----|
|[pypackage_kai](https://github.com/ananab/pypackage_kai)|[setup.py](https://github.com/ananab/pypackage_kai/blob/master/setup.py)|setup file for creating [sdiv-0.1dev.tar.gz](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/dist/sdiv-0.1dev.tar.gz)|`python setup.py sdist`|
|[pypackage_kai](https://github.com/ananab/pypackage_kai/tree/master/sd)|[__init__.py](https://github.com/ananab/pypackage_kai/blob/master/sd/__init__.py)|python script for importing the package|NA|
|[sd](https://github.com/ananab/pypackage_kai/tree/master/sd)|[sdse.py](https://github.com/ananab/pypackage_kai/blob/master/sd/sdse.py)|python script including the sd and se functions|NA|
|[dist](https://github.com/ananab/pypackage_kai/tree/master/dist)|[sdiv-0.1dev.tar.gz](https://github.com/ananab/pypackage_kai/blob/master/dist/sdiv-0.1dev.tar.gz)|compressed python package|`pip install dist/sdiv-0.1dev.tar.gz`|
|[test](https://github.com/ananab/pypackage_kai/tree/master/test)|[test.py](https://github.com/ananab/pypackage_kai/blob/master/test/test.py)|test file for package|`pytest test/test.py`|
|[pypackage_kai](https://github.com/ananab/pypackage_kai)|[.travis.yml](https://github.com/ananab/pypackage_kai/blob/master/.travis.yml)|.yml file for travis ci|NA|

### installation:

Use `cd pypackage_kai` to go into the root directory of the cloned, use `pip install dist/sdiv-0.1dev.tar.gz` to install the package.

### usage:

Once the package is installed, open python. Import the package with `import sd`, then call the functions with `sd.standard_deviatoin()`, and `sd.standard_error()`.

### Update:

If changes are made to the `sd.py` script (added a function for example), update the `__init__.py` accordingly. 

Update the compressed package with `python setup.py sdist` in the sdiv directory. In Mac and Linux, a tar.gz file will be created in the dist directory. In windows, the compressed package will be created as a separate rar file. 

To install this package, do `pip install dist/sdiv-0.1dev.rar`.

### Uninstallation:

Uninstall with `pip uninstall sdiv`

# New function suggestion
Standard error function has been added to the code. 

`sd/sdse.py` has been amended with the following function

```
def standard_error(x):

    se = standard_deviation(x)/(len(x) ** 0.5)

    return(se)

```

Since `__init__.py` adds everything in sd, it is not modified.

# Quick Demo

```
standard_deviation([1,1,1])
```

```
0.0
```


```
standard_error([8,3,5])
```


```
1.186342028003479

```

# test

pytest test/test.py

