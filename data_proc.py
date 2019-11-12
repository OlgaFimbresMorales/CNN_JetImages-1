import h5py as h
import numpy as np


with h.File("qcd.h5", 'r') as qcd:
    with h.File("wprime.h5", 'r') as w:
        with h.File("new.h5", 'w') as new:
            xt = qcd["images"][:]
            xw = w["images"][:]
#            xt /= np.max(xt)
#            xw /= np.max(xw)
            yt = np.zeros(qcd['images'].shape[0])
            yw = np.ones(w['images'].shape[0])
            new.create_dataset("qcd/images", data=xt) 
            new.create_dataset("qcd/labels", data=yt, dtype='i')
            new.create_dataset("wprime/images", data=xw) 
            new.create_dataset("wprime/labels", data=yw, dtype='i') 
