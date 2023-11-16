from gshare import GShare

for traceFile in ['tests/traces/gcc_trace.txt','tests/traces/jpeg_trace.txt','tests/traces/perl_trace.txt']:
    matrix = []
    for noOfPCBits in range(7, 13):
        missRates = []
        for bhrBits in range(2,noOfPCBits+1,2):
            branchPredictor = GShare(3, noOfPCBits,bhrBits)
            f = open(traceFile, "r")
            for instruction in f:
                branchPC,actualPrediction = instruction.strip().split(' ')
                branchPredictor.predict(branchPredictor.getIndex(branchPC),actualPrediction,False)
                branchPredictor.updateBranchRegistry(actualPrediction)
            f.close()
            missRates.append(branchPredictor.getMissRate())
        matrix.append(missRates)
    print("------")
    print(traceFile,matrix)

import math
import matplotlib.pyplot as plt

mat = [[27.81005, 28.9513, 31.10055], [23.5597, 24.95595, 27.52895, 29.5263], [19.9386, 20.8434, 23.46815, 25.48915], [16.95135, 17.9959, 19.87585, 21.22135, 22.52295], [14.45825, 15.05465, 17.05725, 17.7534, 18.835], [12.52625, 13.3966, 14.4659, 15.16175, 15.68515, 16.28485]]
mr = []
for j in range(6):
  l = []
  for arr in mat:
    try:
      l.append(arr[j])
    except:
      pass
  mr.append(l)

n = [2, 4, 6, 8, 10, 12]
x = [range(7,13),range(7,13),range(7,13),range(8,13),range(10,13),range(12,13)]

for index,res in enumerate(mr):
  plt.plot(x[index], res, label=f"n = {n[index]}",marker='o')

plt.legend()
plt.xlabel("number of PC Bits")
plt.ylabel("MissPrediction Rate")
plt.title('gcc_trace.txt,gshare')
plt.show()

mat2 = [[8.40565, 8.6508, 9.4931], [8.04015, 8.19905, 8.81755, 9.06885], [7.93985, 8.0386, 8.45795, 8.3202], [7.8712, 7.9655, 8.3735, 8.05435, 7.98465], [7.4533, 7.6174, 7.89915, 7.49785, 7.46845], [7.4334, 7.5997, 7.8434, 7.2759, 7.29705, 7.35275]]
mr = []
for j in range(6):
  l = []
  for arr in mat2:
    try:
      l.append(arr[j])
    except:
      pass
  mr.append(l)

n = [2, 4, 6, 8, 10, 12]
x = [range(7,13),range(7,13),range(7,13),range(8,13),range(10,13),range(12,13)]

for index,res in enumerate(mr):
  plt.plot(x[index], res, label=f"n = {n[index]}",marker='o')

plt.legend()
plt.xlabel("number of PC Bits")
plt.ylabel("MissPrediction Rate")
plt.title('jpeg_trace.txt,gshare')
plt.show()

mat3= [[21.2804, 24.77935, 28.71915], [17.472, 19.00345, 22.6337, 23.39055], [14.58355, 16.11355, 18.18805, 17.694], [11.51585, 13.19145, 13.7806, 12.6354, 13.65635], [9.9086, 11.03335, 12.0301, 9.28715, 8.90895], [8.82685, 9.42265, 9.9987, 6.96805, 6.42245, 6.8837]]
mr = []
for j in range(6):
  l = []
  for arr in mat3:
    try:
      l.append(arr[j])
    except:
      pass
  mr.append(l)

n = [2, 4, 6, 8, 10, 12]
x = [range(7,13),range(7,13),range(7,13),range(8,13),range(10,13),range(12,13)]

for index,res in enumerate(mr):
  plt.plot(x[index], res, label=f"n = {n[index]}",marker='o')

plt.legend()
plt.xlabel("number of PC Bits")
plt.ylabel("MissPrediction Rate")
plt.title('perl_trace.txt,gshare')
plt.show()
