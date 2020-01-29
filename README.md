# Joystick Control System
The rep has the control system for the 2-axis joystick used in [Mathis et al, 2017](https://www.sciencedirect.com/science/article/pii/S0896627317301575?via%3Dihub#abs0015) Somatosensory Cortex Plays an Essential Role in Forelimb Motor Adaptation in Mice. https://doi.org/10.1016/j.neuron.2017.02.049

# Essential Hardware:

- Joystick base, Digi-Key, Cat #679-2501-ND
- Joystick handle; replace d-pad (removed by screw) with any handle you prefer
- Joystick spring; you may need to exchange the base spring with a lower stiffness spring (should be independently verified)
- NI-DAQ card, PCI-e6251 National Instruments, Cat # NI PCIe-6251 – 779512-01
- LabView 2013 or newer, National Instruments  http://www.ni.com

# Essential Software:

- our custom LabView VIs

The main file is "Pull Behavior...". The other vi's are for grabbing frames from another source, i.e. 2-photon.  There are three output files (reward TTLs, a "trial start" TTL, and the full X and Y joystick trajectory + lick signal + frame count).You will see I utilize the NI-DAQmx Tasks for this code; screenshots in the media folder. 

# Experimental Settings File:

The experimental parameters is a text file that you load, so you can customize this to your system/needs. You specify a resting home box, start "box - i.e. when it crosses a point in Y space it will trigger a trial start", end box, delay times, water value open times, magnet on time, and magnet force. It's easy to customize too, if you want to make changes. Each line in the text file is a trial. i.e.;

<p align="left">
<img src="https://images.squarespace-cdn.com/content/v1/57f6d51c9f74566f55ecf271/1580332353354-LVVT5YLXTGMRPQBVZIXX/ke17ZwdGBToddI8pDm48kHzsiv5yD4n7p_B9esjyrWJZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpy3Qf9vIQl4yoc5X6lDN1caHTGO4yrB4-uwOSTmPq_v1_QBLjygwGx4qYPs2cMZwac/joystick.png?format=750w" width="75%">
</p>

# Getting Started:

Based on how you build the joystick, your resting voltage may differ. Each rig should be measured and calibarated (i.e. what voltage delta = X mm distance). 

The above values are a good starting point, assuming the voltage rests at 2.55.  Set for your rig as needed. There is a exp array that is on the front screen of the vi so you can figure out which values are which, etc, but it doesn't match the orde rin the text file, thus I highlighted important variables. To note, this demo assumes the joystick rests at 2.55; and every .05 is 1 mm. 

# Citation:

If you use this code please cite: 

- [Mathis et al, 2017](https://www.sciencedirect.com/science/article/pii/S0896627317301575?via%3Dihub#abs0015) Somatosensory Cortex Plays an Essential Role in Forelimb Motor Adaptation in Mice. https://doi.org/10.1016/j.neuron.2017.02.049

We greatly thank Dr. Ed Soucy at the Harvard CBS Center for Neuroengineering with LabView code and expert advice throughout the development of this joystick system! 
