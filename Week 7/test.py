import numpy as np
aa = np.array([[1,2,3,4], [2,3,4,5], [5,6,7,8], [9,10,11,12]])
bb = np.array([[100,200,300,400], [100,200,300,400], [100,200,300,400], [100,200,300,400]])
#print aa[:,1]
#print bb
#print bb[:,1]
def vec2(a, b):
    return a * b

func2 = np.vectorize(vec2)
print func2(bb, aa)