import sys
import time
from smith import  Smith
from bimodal import Bimodal
from gshare import GShare
from hybrid import Hybrid

if __name__=='__main__':
    predictorName = sys.argv[1]
    noOfBits = int(sys.argv[2])
    traceFile = sys.argv[3]
        
    branchPredictor = None 
    if predictorName == 'smith':
            branchPredictor = Smith(noOfBits,0,0)            
    elif predictorName == 'bimodal':
            branchPredictor = Bimodal(3,noOfBits,0)                        
    elif predictorName == 'gshare':
            registerBits = int(sys.argv[3])
            traceFile = sys.argv[4]
            branchPredictor = GShare(3,noOfBits,registerBits) 
    else:
          chooserBits = int(sys.argv[2])
          gShareNoOfBits = int(sys.argv[3])
          registerBits = int(sys.argv[4])
          bimodalNoOfBits = int(sys.argv[5])
          traceFile = sys.argv[6]
          gsharePredictor = GShare(3,gShareNoOfBits,registerBits) 
          bimodalPredictor = Bimodal(3,bimodalNoOfBits,0)
          branchPredictor = Hybrid(chooserBits,gsharePredictor,bimodalPredictor)
    
    f = open(traceFile, "r")
    # Read each instruction from trace file
    for instruction in f:
        branchPC,actualPrediction = instruction.strip().split(' ')
        branchPredictor.predict(branchPredictor.getIndex(branchPC),actualPrediction,False)
        branchPredictor.updateBranchRegistry(actualPrediction)
    f.close()

    branchPredictor.display(traceFile)

    
   