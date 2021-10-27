import numpy as np
liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
dtype=liste
arr=np.array(liste,dtype="object")
flatlist=list(arr.flat)
print(flatlist)

