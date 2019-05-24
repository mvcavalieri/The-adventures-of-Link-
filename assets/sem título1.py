import matplotlib.pyplot as plt

from scipy.integrate import odeint
import math
from numpy import arange

l= 1.496* 10**11
p= 3.1558464 * 10**7
Voy= 2*math.pi
def trajetoria(listasol,t):
    x= listasol[0]
    y= listasol[1]
    vx= listasol[2]
    vy= listasol[3]
    dxdt= vx
    dydt= vy
    dvxdt= -4* math.pi **2* x/ (x**2+ y**2)**3/2
    dvydt= -4* math.pi**2* y/ ( x**2 + y**2)**3/2
    return dxdt, dydt, dvxdt, dvydt
  
tp= arange(0,3,0.5)
c0= [1,0,0,Voy]
Solucao= odeint(trajetoria,c0,tp)

plt.plot( Solucao[:,0]) ,Solucao[:,1])
plt.grid(True)
plt.grid("equal")
plt.show()