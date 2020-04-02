#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:29:23 2020

@author: anita
"""

import numpy as np
import matplotlib.pyplot as plt

def edo_discret(S, I, D, C, beta, gamma, delta, N):
    '''
    :param: S = S(t)
            I = I(t)
            R = R(t)
            beta, gamma, N the model's parameters
    :return: S(t+1), I(t+1), R(t+1) with the finite difference approximation
    '''
    St = - beta * S * I / N + S
    It = beta * S * I / N - I * (gamma - 1)
    R = D + C
    Rt = gamma * I + R
    Dt = delta * Rt
    Ct = Rt - Dt
#    Rt = N - St - It
    return St, It, Dt, Ct

def edo_continue(S, I, R, beta, gamma, N):
    '''
    :param: S = S(t)
            I = I(t)
            R = R(t)
            beta, gamma, N the model's parameters
    :return: S(t+1), I(t+1), R(t+1) with the continuous resolution of the edo
    '''
    St, It, Rt = 0
    return St, It, Rt


def SIR(S0, I0, D0, C0, beta, gamma, delta, N, end, betaconf,deltaSaturation):
    Ls, Li, Ld, Lc = np.empty(end), np.empty(end), np.empty(end), np.empty(end)
    St, It, Dt, Ct = S0, I0, D0, C0
    for t in range(end):
        Ls[t], Li[t], Ld[t], Lc[t] = St, It, Dt, Ct
        if It >= 0.1 * N :
            beta = betaconf
        if It >= 0.3*N:
            delta=deltaSaturation
            
        St, It, Dt, Ct = edo_discret(St, It, Dt, Ct, beta, gamma, delta, N)
    return Ls, Li, Ld, Lc



# =============================================================================
# INITIALISATION
# =============================================================================

# total population
N = 1000
# initialisation
I0 = 1
D0 = 0
C0 = 0
S0 = N - I0 - D0 - C0

p1 = 1/100 # probabilité de transmission lors d'un contact entre un I et un S
c1 = 30 # nombre de contact par unité de temps

p2 = 1/50
c2 = 10

beta = p1 * c1
betaconf = p2 * c2
gamma = 1/20
delta = 1/10
deltaSaturation=2/3


#Rnutch = beta/gamma    #/!\ attention  pas le même R0 que l'initialisation de removed population

# print('Rnutch :', Rnutch)
# =============================================================================
# SIMULATION AND PLOT
# =============================================================================

end = 200
t = np.linspace(0, end, end)
Ls, Li, Ld, Lc = SIR(S0, I0, D0, C0, beta, gamma, delta, N, end, betaconf,deltaSaturation)

#normaliser
Ls = Ls / N
Li = Li / N
Ld = Ld / N
Lc = Lc / N

plt.plot(t, Li, marker='.', color='orange', label='I(t)')
plt.plot(t, Ls, marker='.', color='skyblue', label='S(t)')
plt.plot(t, Ld, marker='.', color='purple', label='D(t)')
plt.plot(t, Lc, marker='.', color='green', label='C(t)')
plt.legend()
plt.show()

plt.stackplot(t, Li, Ls, Ld, Lc, labels=['I(t)', 'S(t)', 'D(t)', 'C(t)'], colors=['orange', 'skyblue', 'purple', 'green'])
plt.legend(loc='upper left')
plt.margins(0,0)
plt.show()
