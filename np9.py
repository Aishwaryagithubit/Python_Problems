#assignment and slicing
import numpy as np
a = np.arange(10)
print(a)
a[5:]=7
print(a)

b=a[5:]
a[5:]=b[::-1]
print(a)

print(np.may_share_memory(a,b))

c=a[::2].copy()
c[0]=12
print(a)
print(np.may_share_memory(a,c))
