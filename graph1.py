from smith import Smith

for traceFile in ['tests/traces/gcc_trace.txt','tests/traces/jpeg_trace.txt','tests/traces/perl_trace.txt']:
    missRates = []  
    for noOfBits in range(1, 7):    
        branchPredictor = Smith(noOfBits, 0,0)
        f = open(traceFile, "r")
        # Read each instruction from trace file
        for instruction in f:
            # reading each line and spliting instruction 
            branchPC,actualPrediction = instruction.strip().split(' ')
            # Predicting the outcome and updating the counter and prediction table 
            branchPredictor.predict(branchPredictor.getIndex(branchPC),actualPrediction,False)
            # Updating BHR (valid only for gshare and hybrid for rest its just dummy function call)
            branchPredictor.updateBranchRegistry(actualPrediction)
        f.close()
        missRates.append(branchPredictor.getMissRate())
    print(traceFile,missRates)

import math
import matplotlib.pyplot as plt

x = range(1,7)
plt.plot(x, [45.24135, 43.01095, 41.5714, 41.6764, 41.3327, 41.9382],marker = 'o')
plt.xlabel("number of counter bits")
plt.ylabel("MissPrediction Rate")
plt.title('gcc_trace.txt,smith')
plt.show()

x = range(1,7)
plt.plot(x, [50.02115, 30.9806, 29.1241, 28.14355, 27.99565, 27.94095],marker = 'o')
plt.xlabel("number of counter bits")
plt.ylabel("MissPrediction Rate")
plt.title('jpeg_trace.txt,smith')
plt.show()

x = range(1,7)
plt.plot(x, [47.66285, 47.97745, 48.6466, 46.73695, 47.55, 47.6947],marker = 'o')
plt.xlabel("number of counter bits")
plt.ylabel("MissPrediction Rate")
plt.title('perl_trace.txt,smith')
plt.show()
