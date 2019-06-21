# To test the convolution function with the current file
import  numpy as np
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
t4mfnorm2 = np.loadtxt('t4mfnorm.asc')
t3mfnorm2 = np.loadtxt('t3mfnorm.asc')
t2mfnorm2 = np.loadtxt('t2mfnorm.asc')
t1mfnorm2 = np.loadtxt('t1mfnorm.asc')

c4mfnorm2 = np.loadtxt('c4mfnorm.asc')
c3mfnorm2 = np.loadtxt('c3mfnorm.asc')
c2mfnorm2 = np.loadtxt('c2mfnorm.asc')
c1mfnorm2 = np.loadtxt('c1mfnorm.asc')

seed=123456789

# initialize weights - comparitive index
w1=0.15; # w1 percent of cells fire 1 synapse
w2=0.35; # w2 perc of cells fire 2 synapses
w3=0.35; # w3 perc of cells fire 3 synapses
w4=0.15; # w4 perc of cells fire 4 synapses

# initialize weights - for the fields
wn1=w1
wn2=w2
wn3=w3 #1
wn4=w4 #1

nX1mf0in=deljitter(t1mfnorm2[:,1],1300)
nX2mf0in=deljitter(t2mfnorm2[:,1],130)
nX3mf0if=deljitter(t3mfnorm2[:,1],1)
nX4mf0in=deljitter(t4mfnorm2[:,1],1)

nC1mf0in=deljitter(c1mfnorm2[:,1],2600)
nC2mf0in=deljitter(c2mfnorm2[:,1],2600)
nC3mf0if=deljitter(c3mfnorm2[:,1],1)
nC4mf0in=deljitter(c4mfnorm2[:,1],1)

Xanew = []
Xbnew = []
X1anew = []
X1bnew = []

# Plot cases
Xanew = deljitter(t4mfnorm2[:,0],1)
Xbnew = ((w1*nX1mf0in)+(w2*nX2mf0in)+(w3*nX3mf0if)+(w4*nX4mf0in))
X1anew = deljitter(c4mfnorm2[:,0],1)
X1bnew = ((w1*nC1mf0in)+(w2*nC2mf0in)+(w3*nC3mf0if)+(w4*nC4mf0in))

#figure
#plot(Xnew(:,1),Xnew(:,2));
#hold on;
#plot(X1new(:,1),X1new(:,2));
#title('Weighted measure-SomaHillDend regions');

# new Vectors for fields
noX1 = Xanew
noX2 = Xbnew
noC1 = X1anew
noC2 = X1bnew

seed=3e7
Y1new = []
Y2new = []

# Going in for the field calculations
ytst1 = np.zeros(shape=(len(Xanew)))
ytst2 = np.zeros(shape=(len(Xanew)))
Y1new = deljitter(ytst1,1);
Y2new = deljitter(ytst2,1);

#Make copies for averaging
A1new = deljitter(ytst1,1);
A2new = deljitter(ytst2,1)
B1new = deljitter(ytst1,1)
B2new = deljitter(ytst2,1)
C1new = deljitter(ytst1,1)
C2new = deljitter(ytst2,1)
D1new = deljitter(ytst1,1)
D2new = deljitter(ytst2,1)
E1new = deljitter(ytst1,1)
E2new = deljitter(ytst2,1)
F1new = deljitter(ytst1,1)
F2new = deljitter(ytst2,1)
G1new = deljitter(ytst1,1)
G2new = deljitter(ytst2,1)
H1new = deljitter(ytst1,1)
H2new = deljitter(ytst2,1)
I1new = deljitter(ytst1,1)
I2new = deljitter(ytst2,1)

savscram=[]
savscrami1=[]

#For the separate T,C
#Tw(:,1) = deljitter(ytst(:,1),340);
#Cw(:,1) = deljitter(ytst(:,1),300);

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    Y2new = Y2new+y_i+y1_i
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
Y1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    A2new = A2new+y_i+y1_i
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
A1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    B2new = B2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
B1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    C2new = C2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
C1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    D2new = D2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
D1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    E2new = E2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
E1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    F2new = F2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
F1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    G2new = G2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
G1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    H2new = H2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
H1new = deljitter(Xanew,1,0)

del scram
del scrami1
savscram = []
savscrami1 = []
del y_i
del y1_i

for i in range(110):
    scram=abs(round((np.random.normal(1300,340))));
    savscram.append(scram)
    scrami1=abs(round((np.random.normal(2600,340))));
    savscrami1.append(scrami1)
    y_i = np.array(deljitter(noX2,scram))
    y1_i = np.array(deljitter(noC2,scrami1))
    I2new = I2new+y_i+y1_i;
#    Tw=Tw+y_i;
#    Cw=Cw+y1_i;
I1new = deljitter(Xanew,1,0)

S1new = deljitter(Xanew,1,0);
S2new = ((Y2new+A2new+B2new+C2new+D2new+E2new+F2new+G2new+H2new+I2new)/10)

#for new field related x-axis (check this for other lengths of simulations - assumed here tstop=200ms with 40 points
disp0 = np.arange(0,((len(Y1new)+340)/40),(1/40))
disp1 = disp0[:17998]
dispvar = (disp1/4)

yindex = np.arange(len(Y1new))
#plot fields
plt.figure(0)
plt.plot(dispvar,S2new,linewidth=1.0)
plt.title('In vivo evoked LFP reconstruction')
#print('\n\n')
#now = time.time() #Time after it finished
#print("It took: ", now-then, " seconds")
plt.show()
