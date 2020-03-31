#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:29:23 2020

@author: anita
"""

import numpy as np
import matplotlib.pyplot as plt

# total population
N = 1000
# initialisation
I0 = 10
C0 = 0
D0 = 0
S0 = N - I0 - C0 - D0
y0 = S0, I0, C0, D0
beta = 0.5
gamma = 0.2
R0 = beta/gamma

def edo(y, N, beta, gamma):
    S, I, R = y
    dSdt = - beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

