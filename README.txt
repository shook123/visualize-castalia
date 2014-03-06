visualize-castalia
==================

Version 1.0

Python script for parsing trace files produced by castalia and visualizing the results.
The script needs python 2.7 and the latest version of pygame. Put it  in your castalia folder and run it with:
python visualize_castalia.py Simulations/radioTest
to show the movements of the radioTest simulation. Make sure you have actually run the simulation before, with 
SN.node[*].MobilityManager.collectTraceInfo = true
being uncommented in the omnetpp.ini file. You should also delete the Castalia-Trace.txt file before each simulation run, or you will probably get weird results.

Hitting Escape will stop the Simulation. 


See https://groups.google.com/forum/#!topic/castalia-simulator/0XSdLAUvRoU for initial description and discussion. Future discussion should probably be held on the github site though.

Todo:
- check if omnetpp.ini is in folder
- check if Castalia-Trace.txt in in folder
- check Castalia-Trace.txt holds more than one run. If so, abort after first run and give a warning

possible features:
- add a help section
- show node numbers (they are already saved in nodes)
- different colors
- show/hide a grid
- show simulation time
- add play/pause and speed control
- show parsed messages in a textfield
- show messages being sent (this is probably a lot of work)
- "Zoom out" a bit, so nodes being on the edges of the field are fully visible. This can be done via coordinate transformation