import numpy as np

s=np.loadtxt('S0.txt',unpack=True)
s = s.T
print(s)
print(s.shape)

# 1) Setting floating point precision:
np.savetxt('S1.txt',s,fmt='%1.3f')

# 2) Adding characters to right-justify:
# With spaces:
np.savetxt('S2a.txt',s, fmt='% 4d')

# With zeros:
np.savetxt('S2b.txt',s, fmt='%04d')

# 3) Adding characters to left-justify (use of "-")
#With spaces:
np.savetxt('S3.txt',s, fmt='%-4d')

# 4) General example:
np.savetxt('S4.txt',s, fmt='%1.1f + %1.1f / (%1.1f * %1.1f)')