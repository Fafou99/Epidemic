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
    St = - beta * S * I / N - S
    It = beta * S * I / N - I * (1 + gamma)
    Rt = beta * I - R
    return St, It, Rt
# maybe compute Rt as N - St - It to be sure that N = sum(S, I, R) ?


def SIR(S0, I0, R0, beta, gamma, N, end):
    Ls, Li, Lr = [S0], [I0], [R0]
    for _ in range(end):
        St, It, Rt = edo(Ls[-1], Li[-1], Lr[-1], beta, gamma, N)
        Ls.append(St)
        Li.append(It)
        Lr.append(Rt)
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
beta = 0.5
gamma = 0.2
# R0 = beta/gamma    /!\ attention  pas le même R0 que l'initialisation de removed population

# =============================================================================
# SIMULATION AND PLOT
# =============================================================================

end = 200
t = np.linspace(0, 200, 200)
Ls, Li, Lr = SIR(S0, I0, R0, beta, gamma, N, end)
