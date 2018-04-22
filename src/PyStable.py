
#
# Pystable.py, 22 Apr 18

import ctypes
import numpy


lib = ctypes.cdll.LoadLibrary('./libstable.so')
Py_stable_cdf = lib.c_stable_cdf
Py_stable_pdf = lib.c_stable_pdf
Py_stable_rnd = lib.c_stable_rnd

def stable_pdf(alpha, beta, sigma, mu, data):

   # print "stable_pdf"

   outdata = numpy.empty([1, data.size], dtype=numpy.double)
   Py_stable_pdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(data.ctypes.data), ctypes.c_int(data.size),
	ctypes.c_void_p(outdata.ctypes.data))

   return outdata

def stable_cdf(alpha, beta, sigma, mu, data):
   # print "stable_cdf"

   outdata = numpy.empty([1, data.size], dtype=numpy.double)
   Py_stable_cdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(data.ctypes.data), ctypes.c_int(data.size),
	ctypes.c_void_p(outdata.ctypes.data))

   return outdata


def stable_rnd(alpha, beta, sigma, mu, n):
   # print "stable_rnd"

   outdata = numpy.empty([1, n], dtype=numpy.double)
   Py_stable_rnd(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(outdata.ctypes.data), ctypes.c_int(outdata.size))

   return outdata


