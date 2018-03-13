import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy
import time
from procTimer import tic, toc
# Start Timer
start = time.clock()
tic()

#### PLOTTING
app = QtGui.QApplication([])

pg.plot(numpy.random.random_integers(0,100,20))
#pylab.title("USING: "+matplotlib.get_backend())
#pylab.show()


##########
# End Timer
end = time.clock()
dtime = end - start
toc()
print ("Time to plot using pyqtgraph: " , dtime) 


# End
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

