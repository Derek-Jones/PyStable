
import ctypes
import numpy

num_elems=20
indata = numpy.empty([1, num_elems], dtype=numpy.double)
outdata = numpy.empty([1, num_elems], dtype=numpy.double)

indata=numpy.arange(-1.0, 1.0, 0.1, dtype=numpy.double)

lib = ctypes.cdll.LoadLibrary('./libstable.so')
stable_cdf = lib.c_stable_cdf
stable_pdf = lib.c_stable_pdf
stable_rnd = lib.c_stable_rnd

# print indata.size

alpha=1.5
beta=0.1
sigma=1.0
mu=0.0

print "stable_pdf"

stable_pdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(indata.ctypes.data), ctypes.c_int(indata.size),
	ctypes.c_void_p(outdata.ctypes.data))

print 'indata: %s' % indata
print 'outdata: %s' % outdata

print "stable_cdf"

stable_cdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(indata.ctypes.data), ctypes.c_int(indata.size),
	ctypes.c_void_p(outdata.ctypes.data))

print 'indata: %s' % indata
print 'outdata: %s' % outdata

print "stable_rnd"

stable_rnd(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(outdata.ctypes.data), ctypes.c_int(outdata.size))

print 'outdata: %s' % indata

