import pyqtgraph as pg
import numpy as np
import sys
sys.path.append('/usr/local/Cellar/pyqt/')
from PyQt4 import QtGui

app = QtGui.QApplication([])
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
pg.plot(x, y, pen=None, symbol='o')

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
