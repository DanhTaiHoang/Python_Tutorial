import numpy as np

def test_xy(x,y):
    return x*10,y+10

res = [test_xy(x,y) for x in range(2) for y in range(2)]
print(res)
print(len(res))
print(res[1])

np.savetxt('list_comprehension.dat',(res[1]))
