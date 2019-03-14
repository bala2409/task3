import numpy as np
import time, sys

size=1000000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

#python list
start=time.time()
result=[(x+y)for x,y in zip(l1,l2) ]
print("python list took:",(time.time()-start)*1000)

#numpy array addition
start=time.time()
res=a1+a2
print("Numpy Took:",(time.time()-start)*1000)
