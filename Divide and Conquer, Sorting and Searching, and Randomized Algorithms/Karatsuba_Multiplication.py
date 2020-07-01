#!/usr/bin/env python
# coding: utf-8

def karatsuba(x,y):
    x_str = str(x)
    y_str = str(y)
    if (x < 10) or (y < 10):
        return x*y
    else:
        n = max(len(x_str),len(y_str))
        center = int(n/2)
        a,b = int(x_str[:center]), int(x_str[center:])
        c,d = int(y_str[:center]), int(y_str[center:])
        p,q = a+b,c+d
        ac, bd, pq = karatsuba(a,c), karatsuba(b,d), karatsuba(p,q)
        adbc = pq - (ac+bd)
        return (10**(2*center)*(ac))+(10**(center)*(adbc))+bd


