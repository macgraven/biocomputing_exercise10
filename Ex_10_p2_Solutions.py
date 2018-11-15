#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:04:00 2018

@author: Mac
"""

import pandas
import scipy
import scipy.integrate as spint
from plotnine import *

def compSim(y,t0,R1,a11,a12,R2,a22,a21):
    N1=y[0]
    N2=y[1]
    
    dN1dt = R1 * (1 - N1 * a11 - N2 * a12) * N1
    dN2dt = R2 * (1 - N2 * a22 - N1 * a21) * N2
    
    return [dN1dt,dN2dt]

#Trial One - Should Coexist
#a12 = .01, a11 = .05; a21 = .01, a22 = .05
times = range(0,100) #Passed as t0
y0=[10,20]
params = (.05,.05,.01,.05,.05,.01) #(R1,a11,a12,R2,a22,a21)
sim=spint.odeint(func=compSim,y0=y0,t=times,args=params)
simdf=pandas.DataFrame({"t":times,"N1":sim[:,0],"N2":sim[:,1]})
a=ggplot(simdf,aes(x="t",y="N1"))+geom_point()+geom_line()+ylab("population")+geom_line(simdf,aes(x="t",y="N2"),color="red")+theme_classic()
print(a)

#Trial Two - Should Not Coexist
#a12 = .05, a11 = .01; a21 = .05, a22 = .01
times = range(0,100) #Passed as t0
y0=[10,20]
params = (.05,.01,.05,.05,.01,.05) #(R1,a11,a12,R2,a22,a21)
sim=spint.odeint(func=compSim,y0=y0,t=times,args=params)
simdf=pandas.DataFrame({"t":times,"N1":sim[:,0],"N2":sim[:,1]})
b=ggplot(simdf,aes(x="t",y="N1"))+geom_point()+geom_line()+ylab("population")+geom_line(simdf,aes(x="t",y="N2"),color="red")+theme_classic()
print(b)

#Trial Three - Should Not Coexist
#a12 = .05, a11 = .05; a21 = .05, a22 = .05
times = range(0,100) #Passed as t0
y0=[20,15]
params = (.05,.05,.05,.05,.05,.05) #(R1,a11,a12,R2,a22,a21)
sim=spint.odeint(func=compSim,y0=y0,t=times,args=params)
simdf=pandas.DataFrame({"t":times,"N1":sim[:,0],"N2":sim[:,1]})
b=ggplot(simdf,aes(x="t",y="N1"))+geom_point()+geom_line()+ylab("population")+geom_line(simdf,aes(x="t",y="N2"),color="red")+theme_classic()
print(b)