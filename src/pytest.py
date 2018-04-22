
import numpy
import PyStable as ps


num_elems=20

indata=numpy.arange(-1.0, 1.0, 0.1, dtype=numpy.double)

alpha=1.5
beta=0.1
sigma=1.0
mu=0.0

spdf=ps.stable_pdf(alpha, beta, sigma, mu, indata)

print "stable_pdf"
print 'indata: %s' % indata
print 'spdf: %s' % spdf

scdf=ps.stable_cdf(alpha, beta, sigma, mu, indata)

print "stable_cdf"
print 'indata: %s' % indata
print 'scdf: %s' % scdf


srnd=ps.stable_rnd(alpha, beta, sigma, mu, 20)

print "stable_rnd"
print 'indata: %s' % indata
print 'rnd: %s' % srnd



