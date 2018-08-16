from numpy import *
import numpy
from itertools import combinations
import pickle
import json as simplejson
import numpy as np
from array import *
from random import randint
from subprocess import call
import subprocess
import os


numofsubs = raw_input('Enter the number of substitutions: ')
numsubs = int(numofsubs)
numofruns = raw_input('Enter the number of runs: ')
numruns = int(numofruns)

nauatoms = int(25)


os.system("pwd > pwd.dat")
workdir = np.genfromtxt('pwd.dat',dtype='str')
workdir = str(workdir)

numcombs = math.factorial(nauatoms)/math.factorial(nauatoms-numsubs)
numcombs = numcombs/math.factorial(numsubs)
print "number of combinations ="+str(numcombs)

print numcombs

f = open('au'+str(nauatoms)+'.dat','rb')
#h= open('array.dat','w')

data = loadtxt("au"+str(nauatoms)+".dat", skiprows=1)  
natoms=f.readline()
natoms=int(natoms)
goldpositions=numpy.zeros((nauatoms,2))
positions=numpy.zeros((numcombs,numsubs))

catom = 79
j=0
atoms=data[:,0]
for i in range(0,int(natoms)):
  if atoms[i] == catom:
    goldpositions[j][0]=int(i)
    goldpositions[j][1]=int(catom)
    j=j+1
    
new=list(combinations(goldpositions[:,0], numsubs))

positions = np.array(new)

	
for i in range(0,numruns):
  g = open("input.bas","w")
  basname = "input.bas"
  filedir = str(i)

  g.write(str(natoms)+'\n') 
  for j in range(0,int(natoms)):
    
    if any(j in positions[i,:]):
      g.write("%d \t %f \t %f \t %f  \n" % (47 , data[j][1],  data[j][2],  data[j][3]))
    else:
      g.write("%d \t %f \t %f \t %f  \n" % (data[j][0] , data[j][1],  data[j][2],  data[j][3]))
      
  g.close

  os.system("mkdir"+" "+str(i))
  os.system("mv"+" "+basname+" "+str(i))
  os.system("cd"+" "+filedir)

  os.system("ln -s ../fireball.x"+" "+filedir)
  os.system("ln -s ../Fdata"+" "+filedir)
  os.system("ln -s ../rms.input"+" "+filedir)
  os.system("ln -s ../fireball.in"+" "+filedir)

jobfile = open("gold.job","w")
jobfile.write("#!/bin/bash\n")
jobfile.write("#PBS -q standby\n")
jobfile.write("#PBS -l nodes=1:ppn=1\n")
jobfile.write("#PBS -l walltime=4:00:00\n")
jobfile.write("#PBS -t 0-"+str(numruns-1)+"\n")
jobfile.write("#PBS -m ae\n")
jobfile.write("#PBS -l pvmem=4gb\n")
jobfile.write("#PBS -e pathToErrorFile\n")
jobfile.write("#PBS -M gihansflying@gmail.com\n")
jobfile.write("#PBS -N au"+str(nauatoms)+"-"+str(numsubs)+"-${PBS_ARRAYID}\n")
jobfile.write("\n")
jobfile.write("source ~/.bashrc\n")
jobfile.write("\n")
jobfile.write(" cd "+workdir+"/"+"${PBS_ARRAYID}"+"\n")

jobfile.write("    ./fireball.x > output.log\n")

jobfile.close()

#CREATING FIREBALL.IN   
fireinfile = open("fireball.in","w")
fireinfile.write("&OPTION\n")
fireinfile.write("basisfile = "+basname+"\n") 
fireinfile.write("ihorsfield = 1\n")
fireinfile.write("imcweda = 0\n")
fireinfile.write("iquench = -3\n")
fireinfile.write("icluster = 1\n")
fireinfile.write("nstepf = 5000\n")
fireinfile.write("qstate = 1.0\n")
fireinfile.write("dt = 0.5\n")
fireinfile.write("&END\n")
fireinfile.write("&OUTPUT\n")
fireinfile.write("iwrtxyz = 1\n")
fireinfile.write("iwrtcharges = 1\n")
fireinfile.write("iwrteigen = 1\n")
fireinfile.write("&END\n")
   
fireinfile.close()



