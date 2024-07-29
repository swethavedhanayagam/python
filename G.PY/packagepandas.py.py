#PANDAS
'''import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)


import pandas as p
a=[1,7,2]
myvar=p.Series(a,index=["x","y","z"])
print(myvar)'''


'''import pandas as pd
mydataset={
    'cars':["BMW","VOLVO","FORD"],
    'passings':[3,7,2]
    }
print(mydataset)
myvar=pd.DataFrame(mydataset)
print(myvar)'''


#NUMPY

'''import numpy
arr=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[1])
print(arr[2]+arr[3])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:10:2])'''

'''import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
a=[]
print(type(a))
print(type(arr))'''


'''import numpy as np
print(np.__version__)
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print('2nd element on 1st row:',arr[0,1])'''


'''import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,2])
print("1.",arr[1,1:4])
print("2.",arr[0:2,2])
print("3.",arr[0:2,1:4])'''


'''import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("4.",arr)
print("5.",arr[0,1,2])'''



import numpy as np
i=np.array([[[0,1,2,3],[4,5,6,7]],[[8,9,10,11],[12,13,14,15]],[[9,8,7,6],[3,4,5,6]]])
for x in i:
    for y in x:
        print(y)
    
    
     














