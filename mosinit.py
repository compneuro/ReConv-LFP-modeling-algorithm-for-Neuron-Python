# ReConv algorithm for reconstructing evoked LFP in cerebellar granular layer
# Uses Multicompartmental GrC model (see http://senselab.med.yale.edu/ModelDb/showmodel.asp?model=116835)
# Last updated 11-June-2011
# Model developer: Shyam Diwakar
# Model contributors and Python re-implementation: Anandhu Presannan
# Developed at Amrita School of Biotechnology (India)
# Amrita School of Biotechnology, Amritapuri campus
# Clappana P.O., Kollam, 690 525, Kerala, India.
# http:/www.amrita.edu/compneuro
# Email:shyam@amrita.edu


# Model published as [Diwakar et al., 2011, PLoS ONE]
#Shyam Diwakar, Paola Lombardo, Sergio Solinas, Giovanni Naldi, Egidio D'Angelo. "Local field potential modeling predicts dense activation in cerebellar granule cells clusters under LTP and LTD control", PLoS ONE, 2011.


from neuron import h
import os
import subprocess
from tkinter import *


h.load_file("nrngui.hoc")
h.load_file("Start.hoc")
h.xopen("Record_vext.hoc")

print("For run the Invitro LFP simulation click on the Invitro button in the panel\n")
print("For run the Invivo LFP simulation click on the Invivo button in the panel\n")

def invitroplot():
    h.Invitro()
    print('\n\n\n')
    print('Plotting invitro......')
    print('Please wait few minutes......... :)')
    os.chdir("data/Invitro/")
    return_value = subprocess.check_output('python3 testconv.py', shell=True)
    print(return_value.decode('utf-8'))
    print("Quit and restart before running for in vivo traces... ")



def invivoplot():
    h.Invivo()
    print('\n\n\n')
    print('Plotting invivo.....')
    print('Please wait few minutes......... :)')
    os.chdir("data/Invivo/")
    return_value = subprocess.check_output('python3 testconv.py', shell=True)
    print(return_value.decode('utf-8'))
    print("Quit and restart before running for in vitro traces... ")

top = Tk()
top.geometry("350x230")
top.title("Control")

label1 = Label(text="ReConv Algoritham")
label1.place(x=5, y= 10)
label2 = Label(text="============")
label2.place(x=5, y= 30)

label3 = Label(text="Run Control")
label3.place(x=5, y= 70)

B1 = Button(top, text = "In-Vitro", command = invitroplot, bd = 3, fg = "red")
B1.place(x=5, y= 95)

B2 = Button(top, text = "In-Vivo", command = invivoplot, bd = 3, fg = "green")
B2.place(x=5, y= 135)

label2 = Label(text="Reconstructing evoked LFP in cerebellar granule\nRef.Diwakar et al, PloS ONE, 2011.")
label2.place(x=5, y= 180)

top.mainloop()
