#lambdas

import math

def square_root(x): return math.sqrt(x)

print(square_root(64));


square_root1 = lambda x: math.sqrt(x)

print(square_root1(81));

sum = lambda x, y: x + y;
print(sum(4,5)) # prints 9

out = lambda *x: sys.stdout.write(" ".join(map(str,x)))

print(4) # prints 4

"""
#pickling is the process whereby a Pyton object hierarchy is converted into a byte stream and unpickling is the inverse operation, whereby a bytestream (from a bin file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively know as serialization, marshalling or flattening
"""

