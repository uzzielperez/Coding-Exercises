import numpy
import matplotlib
import pylab
import time
from procTimer import tic, toc
# Start Timer
start = time.clock()
tic()

pylab.plot(numpy.random.random_integers(0,100,20))
pylab.title("USING: "+matplotlib.get_backend())
pylab.show()

# End Timer
end = time.clock()
dtime = end - start
toc()
print ("Time to plot using "+matplotlib.get_backend(),": ", dtime) 


