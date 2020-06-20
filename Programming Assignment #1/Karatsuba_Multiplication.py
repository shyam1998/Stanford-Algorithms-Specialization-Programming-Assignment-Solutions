#!/usr/bin/env python
# coding: utf-8

def karatsuba(x,y):
    x_str = str(x)
    y_str = str(y)
    if (x < 10) or (y < 10):
        return x*y
    else:
        n = max(len(x_str),len(y_str))
        splitpos = int(n/2)
        a,b = int(x_str[:splitpos]), int(x_str[splitpos:])
        c,d = int(y_str[:splitpos]), int(y_str[splitpos:])
        p,q = a+b,c+d
        ac, bd, pq = karatsuba(a,c), karatsuba(b,d), karatsuba(p,q)
        adbc = pq - (ac+bd)
        return (10**(2*splitpos)*(ac))+(10**(splitpos)*(adbc))+bd


