import numpy as np
import scipy.constants as c
a = c.physical_constants['Bohr radius'][0]

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        start = 1
        for i in range(1,n+1):
            start *= i
        return start

def cartesianToSpherical(x,y,z):
    r = np.sqrt(x**2+y**2+z**2)
    if x == 0:
        t = np.pi/2
    else:
        t = np.arctan(y/x)
    p = np.arccos(z/np.sqrt(x**2+y**2+z**2))
    return round(r,5),round(p,5),round(t,5)

def assocLaguerre(p,qmp):
    def Lpoly(x):
        masterlist = [[1,-x+1,x**2-4*x+2,-x**3+9*x**2-18*x+6],[1,-2*x+4,3*x**2-18*x+18,-4*x**3+48*x**2-144*x+96],[2,-6*x+18,12*x**2-96*x+144,-20*x**3+300*x**2-1200*x+1200],[6,-24*x+96,60*x**2-600*x+1200,-120*x**3+2160*x**2-10800*x+14400]]
        ans = masterlist[p][qmp]
        return ans
    return Lpoly

def radial_wave_func(n,l,r):
    p = 2*l+1
    qmp = n-l-1
    #print p,qmp
    lfunc = assocLaguerre(p,qmp)
    #print lfunc
    y = lfunc(2*r/(n*a))
    #print y
    radsol = np.sqrt((2/(n*a))**3*fact(n-l-1)/(2*n*(fact(n+l))**3))*np.exp(-r/(n*a))*((2*r/(n*a))**l)*y
    ans = radsol/(a**-1.5)
    return np.round(ans,5)

def assocLegendre(m,l):
    def Lpoly(theta):
        x = np.cos(theta)
        masterlist = [[1],[x,np.sqrt(1-x**2)],[0.5*(3*x**2-1),3*x*np.sqrt(1-x**2),3*(1-x**2)],[0.5*(5*x**3-3*x),1.5*(5*x**2-1)*np.sqrt(1-x**2),15*x*(1-x**2),15*(np.sqrt(1-x**2))**3]]
        ans = masterlist[l][m]
        return (ans)
    return Lpoly 
       
def angular_wave_func(m,l,theta,phi):
    pfunc = assocLegendre(m,l)
    y = pfunc(theta)
    #print y
    angsol = (-1)**m*np.sqrt(((2*l+1)*fact(l-np.abs(m)))/(4*np.pi*fact(l+np.abs(m))))*np.exp(1j*(m*phi))*y
    return np.round(angsol,5)

def XX(roa,Nx,Ny,Nz):
    #create x,y,z coordinates
    alllist = []
    N = [Nx,Ny,Nz]
    for i in N:
        alist = []
        if i%2 == 0:
            if i ==Ny:
                i = i-1
            for j in range(-i,i+1,2):
                if j !=0:
                    alist += [roa*float(j)/i]
                    #print alist
        else:
            i = i-1
            for j in range(-i,i+1,2):
                alist += [roa*float(j)/i]
                #print alist
        alllist += [alist]
        #print alllist
    
    x = alllist[0]
    y = alllist[1]
    z = alllist[2]
    xx,yy,zz = np.meshgrid(x,y,z)
    return np.round(xx,5),np.round(yy,5),np.round(zz,5)
    
def magn(n,m,l,r,t,p):
    R = radial_wave_func(n,l,r)
    Y = angular_wave_func(m,l,t,p)
    mag = np.abs((R*Y)**2)
    return mag

def hydrogen_wave_func(n, m, l, roa, Nx, Ny, Nz):
    a = c.physical_constants['Bohr radius'][0]
    xx,yy,zz = XX(roa,Nx,Ny,Nz)
    fvec = np.vectorize(cartesianToSpherical)
    rr,tt,pp = fvec(xx,yy,zz)
    magvec = np.vectorize(magn)
    mag = magvec(n,m,l,rr*a, tt, pp)       
    return xx,yy,zz, np.round(mag,5)
    
x,y,z,mag = hydrogen_wave_func(2,0,0,10,20,20,20)
x.dump('xdata200.dat')
y.dump('ydata200.dat')
z.dump('zdata200.dat')
mag.dump('density200.dat')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.load('xdata200.dat')
y = np.load('ydata200.dat')
z = np.load('zdata200.dat')

mag = np.load('density200.dat')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

for a in range(0,len(mag)):
    for b in range(0,len(mag)):
        for c in range(0, len(mag)):
            ax.scatter(x[a][b][c],y[a][b][c],z[a][b][c],marker='o',alpha=(mag[a][b][c]/np.amax(mag)))
            
plt.show()

