import numpy as np
import pandas as pd
import math
import time

def baseline():
    mat = np.load('../train.npy')
    iBias = np.apply_along_axis(average, 0, mat)#0:col; 1:lin
    uBias = np.apply_along_axis(average, 1, mat)#0:col; 1:lin
    np.save('movieBaseline.npy',iBias) 
    np.save('userBaseline.npy',uBias) 


def average(index):
    mat = np.load('../train.npy')
    globalMean = np.nanmean(mat)
    total = 0
    cont = 0
    for i in index:
        if math.isnan(i):
            continue
        else:
            total += i-globalMean
            cont += 1
    if cont == 0:
        mean = np.NaN
    else:
        mean = total/cont
    return mean

if __name__=='__main__':
    start_time = time.time()
    baseline()
    print(time.time() - start_time)
