import random
from itertools import combinations
import numpy as np
import subprocess
import os

# Number of substitutions
numofsubs = raw_input('Enter the number of substitutions: ')
numsubs=int(numofsubs)

# Number of different isomers
numofruns = raw_input('Enter the number of runs: ')
numruns=int(numofruns)

# Number of atoms in the system
nautoms = int(25)
ngap = int(0)

os.system("pwd > pwd.dat")
workdir = np.genfromtxt('pwd.dat',dtype='str')
workdir = str(workdir)



numcombs = math.factorial(nautoms)/math.factorial(nautoms-numsubs)
numcombs = numcombs/math.factorial(numsubs)
print "number of combinations ="+str(numcombs)

f = open('au'+str(nautoms)+'.dat','rb')

data = loadtxt("au"+str(nautoms)+".dat", skiprows=1)  
natoms = f.readline()
natoms = int(natoms)
goldpositions = numpy.zeros((nautoms,2))

# Atom needs to be substituted
catom = 79
j = 0
atoms = data[:,0]
for i in range(0,int(natoms)):
  if atoms[i] == catom:
    goldpositions[j][0]=int(i)
    goldpositions[j][1]=int(catom)
    j = j + 1



#print goldpositions

for i in range(0,numruns):
  
  positions = random.sample(goldpositions[:,0], numsubs)
 
  for item in positions:
    h.write("%s\n" % item)
  h.write("%s\n" % " ")
  
  os.system("mkdir"+" "+str(strnum))
  
  g = open(str(strnum) + "/input.bas","w")  
  strnum = i + ngap
  filedir = str(strnum)
  g.write(str(natoms)+'\n') 
  for j in range(0,int(natoms)):

      if any(j in positions):
        g.write("%d \t %f \t %f \t %f  \n" % (47 , data[j][1],  data[j][2],  data[j][3]))
      else:
        g.write("%d \t %f \t %f \t %f  \n" % (data[j][0] , data[j][1],  data[j][2],  data[j][3]))
      
  g.close
