#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:29:23 2020

@author: anita
"""

import numpy as np
import matplotlib.pyplot as plt

def edo(S, I, R, beta, gamma, N):
    '''
    :param: S = S(t)
            I = I(t)
            R = R(t)
            beta, gamma, N the model's parameters
    :return: S(t+1), I(t+1), R(t+1) with the finite difference approximation
    '''
    St = - beta * S * I / N + S
    It = beta * S * I / N - I * (gamma - 1)
    Rt = gamma * I + R
#    Rt = N - St - It
    return St, It, Rt
# maybe compute Rt as N - St - It to be sure that N = sum(S, I, R) ?


def SIR(S0, I0, R0, beta, gamma, N, end):
    Ls, Li, Lr = np.empty(end), np.empty(end), np.empty(end)
    St, It, Rt = S0, I0, R0
    for i in range(end):
        Ls[i], Li[i], Lr[i] = St, It, Rt
        St, It, Rt = edo(St, It, Rt, beta, gamma, N)
    return Ls, Li, Lr



# =============================================================================
# INITIALISATION
# =============================================================================

# total population
N = 1000
# initialisation
I0 = 10
R0 = 0
S0 = N - I0 - R0
beta = 0.2
gamma = 0.1
# R0 = beta/gamma    /!\ attention  pas le même R0 que l'initialisation de removed population

# =============================================================================
# SIMULATION AND PLOT
# =============================================================================

end = 200
t = np.linspace(0, 200, 200)
Ls, Li, Lr = SIR(S0, I0, R0, beta, gamma, N, end)

#normaliser
Ls = Ls / N
Li = Li / N
Lr = Lr / N

plt.plot(t, Li, marker='.', color='orange', label='I(t)')
plt.plot(t, Ls, marker='.', color='skyblue', label='S(t)')
plt.plot(t, Lr, marker='.', color='grey', label='R(t)')
plt.legend()
plt.show()

plt.stackplot(t, Li, Ls, Lr, labels=['I(t)', 'S(t)', 'R(t)'], colors=['orange', 'skyblue', 'grey'])
plt.legend(loc='upper left')
plt.margins(0,0)
plt.show()
