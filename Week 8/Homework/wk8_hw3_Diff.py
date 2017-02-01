# -*- coding: utf-8 -*-
class Diff:
    def __init__(self, effex, h=1E-2):
        self.effex = effex
        self.haich = h

    def __call__(self, x):
        differential = (self.effex(x + self.haich) - self.effex(x)) / self.haich
        return differential
#======================================#
def f(x): 
    return 0.25*x**4

df = Diff(f) # make function -like object df
# df(x) computes the derivative of f(x) approximately: 
for x in (1, 5, 10):
    df_value = df(x) # approx value of derivative of f at point x 
    exact = x**3 # exact value of derivative 
    print "f’(%d)=%g (error=%.2E)" % (x, df_value , exact -df_value)