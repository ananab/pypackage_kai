# pypackage_kai
dsci 524 lab 2
[![Build Status](https://travis-ci.org/ananab/pypackage_kai.svg?branch=master)](https://travis-ci.org/ananab/pypackage_kai)

The structure of this repository is summarized in the table below:

|directory|file|nature|usage|
|---------|----|------|-----|
|[sdiv](https://github.ubc.ca/hknaicha/pypackage_kai/tree/master/sdiv)|[setup.py](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/setup.py)|setup file for creating [sdiv-0.1dev.tar.gz](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/dist/sdiv-0.1dev.tar.gz)|`python setup.py sdist`|
|[sdiv/sd](https://github.ubc.ca/hknaicha/pypackage_kai/tree/master/sdiv/sd)|[__init__.py](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/sd/__init__.py)|python script for importing the package|NA|
|[sdiv/sd](https://github.ubc.ca/hknaicha/pypackage_kai/tree/master/sdiv/sd)|[sd.py](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/sd/sd.py)|python script including the sd and se functions|NA|
|[sdiv/dist](https://github.ubc.ca/hknaicha/pypackage_kai/tree/master/sdiv/dist)|[sdiv-0.1dev.tar.gz](https://github.ubc.ca/hknaicha/pypackage_kai/blob/master/sdiv/dist/sdiv-0.1dev.tar.gz)|compressed python package|`pip install sdiv/dist/sdiv-0.1dev.tar.gz`|

### installation:

Use `cd pypackage_kai` to go into the root directory of the cloned, use `pip install sdiv/dist/sdiv-0.1dev.tar.gz` to install the package.

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

`sdiv/sd/sd.py` has been amended with the following function

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

