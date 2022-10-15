#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/megha/Desktop/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if


I =  np.eye(2)
e1 =  I[:,0]
#Input parameters

#Circle parameters
r = 1
O =  np.array(([1.25,0])) #normal vector
Q =  np.array(([-1,0])) #normal vector
P =  np.array(([1,0])) #normal vector
theta1=45
theta2=50
theta3=85
A=r*np.array([np.cos(theta1),np.sin(theta1)])+O
B=r*np.array([np.cos(theta2),np.sin(theta2)])+O
C=r*np.array([np.cos(theta3),np.sin(theta3)])+O
print(A,B,C)
print("||A-P||=||B-P||=||C-P||=1")
print("||A-Q||=||B-Q||=||C-Q||=1")
c=[9*P-Q]
h,k=c[0]*1/8
centre=[h,k]
print("the circumcentre of a triangle is ",centre)
##Generating the line 
m = e1
k1 = -10
k2 = 10
#xline = line_dir_pt(m,B,k1,k2)
xAB = line_gen(A,B)
xOB = line_gen(B,C)
xOA = line_gen(A,C)

##Generating the circle
x_circ= circ_gen(O,r)

#Plotting all lines
#plt.plot(xline[0,:],xline[1,:])
plt.plot(xAB[0,:],xAB[1,:])
plt.plot(xOA[0,:],xOA[1,:])
plt.plot(xOB[0,:],xOB[1,:])

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')


#Labeling the coordinates
tri_coords = np.vstack((Q,A,B,P,C,O)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['Q','A','B','P','C','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-20.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
plt.show()
