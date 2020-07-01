#!/usr/bin/env python
# coding: utf-8

def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        mid = int(length/2)
        L, R = arr[:mid], arr[mid:]
        L, R = merge_sort(L), merge_sort(R)
        return merge(L,R)
       

def merge(L,R):
    result = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    result += L[i:]
    result += R[j:]
    return result