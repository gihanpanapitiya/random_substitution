from itertools import combinations
import numpy as np
from random import randint
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

xyzname = "input.xyz"
for i in range(0,numruns):
  filedir = str(i)  
  os.system("mkdir"+" "+filedir)
  g = open(filedir+"/"+xyzname,"w")
  

  g.write(str(natoms)+'\n') 
  for j in range(0,int(natoms)):
    
    if any(j in positions[i,:]):
      g.write("%d \t %f \t %f \t %f  \n" % (47 , data[j][1],  data[j][2],  data[j][3]))
    else:
      g.write("%d \t %f \t %f \t %f  \n" % (data[j][0] , data[j][1],  data[j][2],  data[j][3]))
      
  g.close

