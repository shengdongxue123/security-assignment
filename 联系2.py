# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:03:02 2021

@author: Littlebox
"""

import matplotlib.pyplot as plt

class m:
    def __init__(self, x, m, v, dt, F=0):
        self.m = m
        self.x = x
        self.v = v
        self.F = F
        self.a = F/m
        self.dt = dt
        
    def step(self, f):
        self.a = (self.F+f)/self.m
        self.v += self.a*self.dt
        self.x += self.v*self.dt
        return self.x, self.v

        
def elstic(x1, x2, k):
    return k*(x1-x2-5)

dt = 0.001
k = 10
m1 = m(0, 1, 3, dt)
m2 = m(5, 2, 0, dt)
m3 = m(10, 3, 0, dt)
t = 0
x_out = [[m1.x, m2.x, m3.x]]
v_out = [[m1.v, m2.v, m3.v]]
a_out = [[m1.a, m2.a, m3.a]]
p = [m1.m*m1.v+m2.m*m2.v+m3.m*m3.v]
t_out = [0]
m1.step(0)
m2.step(0)
m3.step(0)
while t<=10:
    x = [m1.x, m2.x, m3.x]
    v = [m1.v, m2.v, m3.v]
    a = [m1.a, m2.a, m3.a]
    f = [elstic(x[1],x[0],k), -elstic(x[1],x[0],k)+elstic(x[2],x[1],k), -elstic(x[2],x[1],k)]
    m1.step(f[0])
    m2.step(f[1])
    m3.step(f[2])
    t += dt
    p.append(m1.m*m1.v+m2.m*m2.v+m3.m*m3.v)
    x_out.append(x)
    v_out.append(v)
    a_out.append(a)
    t_out.append(t)
plt.subplot(2,2,1)
plt.plot(t_out, x_out)
plt.subplot(2,2,2)
plt.plot(t_out, v_out)
plt.subplot(2,2,3)
plt.plot(t_out, a_out)
plt.subplot(2,2,4)
plt.plot(t_out, p)
plt.show()

