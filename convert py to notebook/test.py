#>
import numpy as np

'''
### parameters
'''

#>
a = 2
c = 6

#>
b = 10*a + c
print('b =',b)
np.savetxt('result_%s.txt'%a,np.array([a,b]),fmt='%f')

'''
Results: we will print c and b here
'''

#>
print(c,b)
