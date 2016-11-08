def do_math(a, b, z=None, kind=True):
  if (z==None):
    return a+b
  if (kind=="add"):
    return a+b
  else:
    return a-b

do_math(1, 2, 3)
do_math(1,2, kind="add")
do_math(1,4,5)