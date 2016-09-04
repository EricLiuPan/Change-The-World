# -*- coding: utf-8 -*-
def is_palindrome(n):
    I,m=n,0
    while I:
        m=m*10+I%10
        I=I//10
    return(n==m)
