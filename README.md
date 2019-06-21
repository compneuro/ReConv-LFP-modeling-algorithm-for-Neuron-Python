ReConv
======

Working version of Repetitive Convolution Code (works on NEURON+Python simulator)


Reconstructing evoked LFP in cerebellar granular layer using jittered
repetitive convolution (ReConv)

This is the README for ReConv model for the paper 

Shyam Diwakar, Paola Lombardo, Sergio Solinas, Giovanni Naldi, Egidio
D'Angelo.  "Local field potential modeling predicts dense activation
in cerebellar granule cells clusters under LTP and LTD control", PLoS
ONE, 2011 6(7):e21928
 
Original implementation was done by Shyam Diwakar in Neuron and Matlab. This is the Python version for Neuron-Python and was implemented by Anandhu Presannan & Shyam Diwakar, Amrita School of Biotechnology, Amrita University, Kollam, Kerala, India.  


Usage instructions:

Attention: For running the model using python3, "tkinter" package is required. 

The code, here, was originally meant for GNU/Linux systems. 

Auto-launch from ModelDB or download and extract the archive.  Then
under:

----
MSWIN

run mknrndll, cd to the archive and make the nrnmech.dll.  Then double
click on the mosinit.py file.

When the "Control Panel" menu pops, click on in vitro for invitro behaviour and after finish the simulation quit and restart before running for in vivo.

----
MAC OS X

Drag and drop the GrC folder onto the mknrndll icon.  Drag and drop
the mosinit.py file onto the nrngui icon.

When the "Control Panel" menu pops, click on "in vitro" for invitro to generate evoked LFP signal and after completing the simulation, quit and restart before running for "in vivo" simulations.
----
Linux/Unix

Change directory to the GrC folder. run "nrnivmodl". Then execute "python3 mosinit.py"

When the "Control Panel" menu pops, click on "in vitro" for invitro to generate evoked LFP signal and after completing the simulation, quit and restart before running for "in vivo" simulations.
----


The GrC model used here was published as (Diwakar et al., 2009)

Shyam Diwakar, Jacopo Magistretti, Mitchell Goldfarb, Giovanni Naldi,
and Egidio D'Angelo. Axonal Na+ channels ensure fast spike activation
and back-propagation in cerebellar granule cells. J Neurophysiol
(December 10, 2008).  doi:10.1152/jn.90382.2008

Also available at
http://senselab.med.yale.edu/ModelDb/showmodel.asp?model=116835
