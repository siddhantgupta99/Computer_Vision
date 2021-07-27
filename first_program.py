import torch
import numpy as np

b = np.ones(2)
c = np.ones(4)
d = np.ones(5)
'''
# Convert numpy to tensor

a = np.ones(5)
print(a)

b = torch.from_numpy(a)
print(b)

a += 1
print(a)
print(b)
'''

'''
# Convert tensor to numpy 
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)

a.add_(1) # in place addition
print(a) # Both elements point to the same location in the memory
print(b)

'''


'''
# 
x=torch.rand(4,4)
print(x)
y = x.view(-1,8)
print(y)
'''



'''
In place addition to y
y=torch.rand(2,2)
print("x = ", x)
print("y  =  ", y)
y = y.add_(x) 'In place addition _ to y '
print(y)
'''

"""
Some basic operations
z=x+y
z=torch.add(x,y)
"""