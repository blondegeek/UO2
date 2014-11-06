import pymatgen 
from pymatgen.io.vaspio.vasp_output import Outcar
import os
import pickle
import numpy as np

outcar = Outcar('OUTCAR')

magarray = []

magx = outcar.magnetizationx
magy = outcar.magnetizationy
magz = outcar.magnetizationz

magxlist = [x["tot"] for x in magx]
magylist = [y["tot"] for y in magy]
magzlist = [z["tot"] for z in magz]

strlist = []

for i in range(0,len(magxlist)):
# change this if loop to select only the magnetic species of interest
# this example was used for a 48 atom unit cell where atoms 41-48 were magnetic
	if i == 0:
		strlist.append(str(magxlist[i])+" "+str(magylist[i])+" "+str(magzlist[i]))

magstr = " ".join(strlist)

print magstr
