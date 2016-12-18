from sd import sd
import pytest as pt
import numpy as np

def testEmptyLst():
    with pt.raises(ZeroDivisionError):
        sd.standard_deviation([])

def testInt():
	with pt.raises(TypeError):
		sd.standard_deviation(1)

def testStr():
	with pt.raises(TypeError):
		sd.standard_deviation("1")

def testInt():
	with pt.raises(TypeError):
		sd.standard_deviation(1)

def testMixedLst():
	with pt.raises(TypeError):
		sd.standard_deviation([1,2.0,"1"])

def testNeg():
	assert sd.standard_deviation([1,2,-5]) == 3.0912061651652345

def testNestLst():
	with pt.raises(TypeError):
		sd.standard_deviation([1,2,[1]])

def test0Var():
	assert sd.standard_deviation([1,1,1,1,1]) == 0

def testNa():
	assert sd.standard_deviation([1,1,1,np.nan]) == 0

def testEmptyLstSE():
    with pt.raises(ZeroDivisionError):
        sd.standard_error([])

def testIntSE():
	with pt.raises(TypeError):
		sd.standard_error(1)

def testStrSE():
	with pt.raises(TypeError):
		sd.standard_error("1")

def testIntSE():
	with pt.raises(TypeError):
		sd.standard_error(1)

def testMixedLstSE():
	with pt.raises(TypeError):
		sd.standard_error([1,2.0,"1"])

def testNegSE():
	assert sd.standard_error([1,2,-5]) == 1.784708711578779

def testNestLstSE():
	with pt.raises(TypeError):
		sd.standard_error([1,2,[1]])

def test0VarSE():
	assert sd.standard_error([1,1,1,1,1]) == 0

def testNaSE():
	assert sd.standard_error([1,1,1,np.nan]) == 0

def testSD_SE():
	assert sd.standard_deviation([1,2,3,4,5]) >= sd.standard_error([1,2,3,4,5])

