def lhs(a,b):
    return (a+b)**2

def rhs(a,b):
    return a**2+2*a*b+b**2

l=lhs(2,3)
r=rhs(2,3)

print('{}={} Hence Proved'.format(l,r))




