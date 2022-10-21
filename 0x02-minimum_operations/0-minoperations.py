#!/usr/bin/python3
'''
Given a number n, write a method that calculates
'''


def findIterations(n, result, index):
    '''
    returns min operations to get n Hs
    '''
    if n % index == 0:
        n, result = findIterations(n / index, result + index, index)
    return (n, result)


def minOperations(n, result=0, index=2):
    '''
    returns min operations to get n Hs
    '''

    if n < 2 and result == 0:
        return 0

    while (index < n + 1):
        n, result = findIterations(n, result, index)
        index += 1
    return result
