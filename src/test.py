
import ctypes
import numpy
import matplotlib.pyplot as plt

num_elems=200
indata  = numpy.empty(num_elems, dtype=numpy.double)
outpdf  = numpy.empty(num_elems, dtype=numpy.double)
outcdf  = numpy.empty(num_elems, dtype=numpy.double)
outrnd  = numpy.empty(num_elems, dtype=numpy.double)

indata=numpy.linspace(-5.0, 30.0, 200, dtype=numpy.double)

lib = ctypes.cdll.LoadLibrary('./libstable.so')
stable_cdf = lib.c_stable_cdf
stable_pdf = lib.c_stable_pdf
stable_rnd = lib.c_stable_rnd

# print indata.size

alpha = 1.5
beta  = 0.75
sigma = 1.0
mu    = 0.0

print("stable_pdf")

stable_pdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(indata.ctypes.data), ctypes.c_int(indata.size),
	ctypes.c_void_p(outpdf.ctypes.data))

print('indata:')
print(indata)
print('outpdf:')
print(outpdf)

print("stable_cdf")

stable_cdf(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(indata.ctypes.data), ctypes.c_int(indata.size),
	ctypes.c_void_p(outcdf.ctypes.data))

print('indata:')
print(indata)
print('outcdf:')
print(outcdf)

print("stable_rnd")

stable_rnd(ctypes.c_double(alpha), ctypes.c_double(beta), 
	ctypes.c_double(sigma), ctypes.c_double(mu), 
	ctypes.c_void_p(outrnd.ctypes.data), ctypes.c_int(outrnd.size))

print('outrnd:')
print(outrnd)


fig,ax = plt.subplots(1,3)
plt.sca(ax[0])
plt.plot(indata,outpdf)
plt.sca(ax[1])
plt.plot(indata,outcdf)
plt.sca(ax[2])
plt.hist(outrnd)
plt.show()
