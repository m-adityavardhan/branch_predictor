from bimodal import Bimodal

for traceFile in ['tests/traces/gcc_trace.txt','tests/traces/jpeg_trace.txt','tests/traces/perl_trace.txt']:
    missRates = []  
    for noOfBits in range(7, 13):    
        branchPredictor = Bimodal(3,noOfBits,0)
        f = open(traceFile, "r")
        for instruction in f:
            branchPC,actualPrediction = instruction.strip().split(' ')
            branchPredictor.predict(branchPredictor.getIndex(branchPC),actualPrediction,False)
            branchPredictor.updateBranchRegistry(actualPrediction)
        f.close()
        missRates.append(branchPredictor.getMissRate())
    print(traceFile,missRates)

import math
import matplotlib.pyplot as plt

x = range(7,13)
plt.plot(x, [25.71735, 21.65705, 17.99665, 15.33165, 13.4648, 12.3029],marker = 'o')
plt.xlabel("number of PC bits")
plt.ylabel("MissPrediction Rate")
plt.title('gcc_trace.txt,bimodal')
plt.show()

x = range(7,13)
plt.plot(x, [7.84725, 7.7476, 7.69205, 7.6523, 7.51485, 7.48835],marker = 'o')
plt.xlabel("number of PC bits")
plt.ylabel("MissPrediction Rate")
plt.title('jpeg_trace.txt,bimodal')
plt.show()

x = range(7,13)
plt.plot(x, [20.60495, 16.1651, 13.7866, 11.6217, 10.59145, 8.94415],marker = 'o')
plt.xlabel("number of PC bits")
plt.ylabel("MissPrediction Rate")
plt.title('perl_trace.txt,bimodal')
plt.show()
