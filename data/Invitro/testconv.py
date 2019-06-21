# To test the convolution function with the current file
import  numpy as np
import scipy.signal as sps
import pandas as pd
import matplotlib.pyplot as plt
#import time
import random

#then = time.time()

def deljitter(x_i,k,*noise1):

    nargin = (len(locals()))

    if (noise1==True):
        nargin = 3
    else:
        nargin = 2

   # print('after the if condition',nargin)

    if (nargin < 1):
        print('deljitter: notEnoughInputs', 'This function requires at least one input.')

    # user input: position 'k' missing
    if (nargin == 1):
        k = 1

    if (nargin == 2):
        noise1 = 80e-14

    x_i2 = x_i.ravel()

    h1 = np.zeros(shape=(5000))
    h1[k-1] = 1

    y1 = (np.convolve(x_i2,h1))
    y1np = np.array(y1.ravel())
    #print('values of y1', y1)
    #y1 = sps.fftconvolve(x_i, h1)
    y3init = np.array(noise1*(np.random.rand(len(y1np),1)))
    y3 = y1np + y3init.ravel()

    y4 = y3.ravel()

    return y4



# Summing areas of dendrites,soma, hillock and 3 compartments of axon
e4mfnorm2 = np.loadtxt('e4mfnorm.asc')
e3mfnorm2 = np.loadtxt('e3mfnorm.asc')
e2mfnorm2 = np.loadtxt('e2mfnorm.asc')
e1mfnorm2 = np.loadtxt('e1mfnorm.asc')

# No Nmda situ
e4mfnonmda2 = np.loadtxt('e4mfnonmda.asc')
e3mfnonmda2 = np.loadtxt('e3mfnonmda.asc')
e2mfnonmda2 = np.loadtxt('e2mfnonmda.asc')
e1mfnonmda2 = np.loadtxt('e1mfnonmda.asc')

# Summing areas of dendrites,soma, hillock and 3 compartments of axon
# -Inhibitory cases
e4i42 = np.loadtxt('e4i4.asc')
e3i32 = np.loadtxt('e3i3.asc')
e2i22 = np.loadtxt('e2i2.asc')
e1i12 = np.loadtxt('e1i1.asc')

# initialize weights - comparitive index
w1=0.2150# w1 percent of cells fire 1 synapse
w2=0.3310# w2 perc of cells fire 2 synapses
w3=0.2535# w3 perc of cells fire 3 synapses
w4=0.2004# w4 perc of cells fire 4 synapses


# initialize weights - for the fields
#wn1=w1
#wn2=w2
#wn3=w3
#wn4=w4

nX1mf0in=deljitter(e1mfnorm2[:,[1]],300)
#nX1mf0in = nX1mf0in0.ravle()
#nX1mf0in=deljitter(e1mfnorm2[:,[2]],300)
nX2mf0in=deljitter(e2mfnorm2[:,[1]],300)
nX3mf0if=deljitter(e3mfnorm2[:,[1]],1)
nX4mf0in=deljitter(e4mfnorm2[:,[1]],1)

Xnew = []
X2new = []

nei1 = deljitter(e1i12[:,[1]],300)
nei2 = deljitter(e2i22[:,[1]],300)
nei3 = deljitter(e3i32[:,[1]],1)
nei4 = deljitter(e4i42[:,[1]],1)



# Plot cases
X1new = deljitter(e4mfnorm2[:,[0]],2)
X2new = ((w1*nX1mf0in)+(w2*nX2mf0in)+(w3*nX3mf0if)+(w4*nX4mf0in))
plt.figure(0)
plt.plot(X1new,X2new,linewidth=1.3)
plt.title('Weighted measure(ctrl,nonmda,inhib)-SomaHillDend regions')
V1new = []# Neeed to modify for the plotting...........
V2new = []
V1new = deljitter(e4i42[:,[0]],2)
V2new = ((w1*nei1)+(w2*nei2)+(w3*nei3)+(w4*nei4))
#plt.plot(V1new,V2new)
#plt.show()

nN1mf0in=deljitter(e1mfnonmda2[:,[1]],300)
nN2mf0in=deljitter(e2mfnonmda2[:,[1]],300)
nN3mf0if=deljitter(e3mfnonmda2[:,[1]],1)
nN4mf0in=deljitter(e4mfnonmda2[:,[1]],1)

N1mdanew = [] # Neeed to modify for the plotting..........title need to add
N2mdanew = []
N1mdanew = deljitter(e4mfnonmda2[:,[1]],2)
N2mdanew = ((w1*nN1mf0in)+(w2*nN2mf0in)+(w3*nN3mf0if)+(w4*nN4mf0in))
#title('Weighted measure(ctrl,nonmda,inhib)-SomaHillDend regions')

# new Vectors for fields
noX1 = X1new
noX2 = X2new
noV1 = V1new
noV2 = V2new
noNM1 = N1mdanew
noNM2 = N2mdanew

Y1new = []
Y2new = []

# Going in for the field calculations
ytst = np.zeros(shape=(len(X1new)))
Y1new = deljitter(ytst,1)
Y2new = deljitter(ytst,1)
savscram=[]

for i in range(700):
    scram=round((np.random.normal(300,81))) #(mod(k1,105))*
    savscram.append(scram)
    y_i=np.array(deljitter(noX2,scram))
    Y2new =Y2new+y_i
Y1new = deljitter(X1new,1,0)
#8888888888888888888888888888888888888888888888888888888888888888
seed=123456789

# Going in for the non-NMDA field calculations
Z1new = []
Z2new = []
ztst1 = np.zeros(shape=(len(X1new)))
ztst2 = np.zeros(shape=(len(X1new)))
savscram1=[]
Z1new = deljitter(ztst1,1)
Z2new = deljitter(ztst2,1)

for i in range(700):
    scram1=round((np.random.normal(300,81))) #
    savscram1.append(scram1)
    z_i=np.array(deljitter(noNM2,scram1))
    Z2new = Z2new+z_i
Z1new = deljitter(X1new,1,0)

seed=1234556789
# Going in for the inhibitory included field calculations
U1new = []
U2new = []
vtst1 = np.zeros(shape=(len(V1new)))
vtst2 = np.zeros(shape=(len(V1new)))
savscram2=[]
U1new = deljitter(vtst1,1)
U2new = deljitter(vtst2,1)

for i in range(700):
    scram2=round((np.random.normal(300,81))) #
    savscram2.append(scram2)
#   print('scram2 value is')
#   print(i)
#   print(scram2)
    u_i=np.array(deljitter(noV2,scram2))
    U2new = U2new+u_i

U1new = deljitter(noV1,1,0)

seed=123456789

#for new field related x-axis
#disp=1:(1/40):((length(Ynew))/40);
disp = np.arange(1,(len(Y1new)/40),(1/40))
disp1=disp[:4496]
dispvar=(disp1/4)

#plot fields
plt.figure(1)
plt.plot(dispvar,Y2new[4:4500],label ='Ctrl- Without inhibition',linewidth=1.0)

plt.plot(dispvar,Y2new[4:4500],'b',linewidth=1.0)

plt.plot(dispvar,Z2new[4:4500],'r', label = 'no NMDA',linewidth=1.0)

plt.plot(dispvar,U2new[4:4500],'g', label = 'with inhibition',linewidth=1.0)
plt.title('Extracellular field reconstruction-ctrl(B), Inhib-on(G) & no-nmda(R)')
plt.legend()
#print('\n\n')
#now = time.time() #Time after it finished
#print("It took: ", now-then, " seconds")
plt.show()
