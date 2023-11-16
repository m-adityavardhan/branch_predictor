import sys
from smith import  Smith
from bimodal import Bimodal
from gshare import GShare
from hybrid import Hybrid

if __name__=='__main__':
    # Reading command line arguments
    predictorName = sys.argv[1]
    noOfBits = int(sys.argv[2])
    traceFile = sys.argv[3]
        
    branchPredictor = None
    # Depending on which branch predictor simulator is instantiated w.r.t that. 
    if predictorName == 'smith':
            branchPredictor = Smith(noOfBits,0,0)            
    elif predictorName == 'bimodal':
            branchPredictor = Bimodal(3,noOfBits,0)                        
    elif predictorName == 'gshare':
            # For gshare command line arguments differ hence read again
            registerBits = int(sys.argv[3])
            traceFile = sys.argv[4]
            branchPredictor = GShare(3,noOfBits,registerBits) 
    else: # Hybrid Predictor
          # For hybrid command line arguments differ hence read again
          chooserBits = int(sys.argv[2])
          gShareNoOfBits = int(sys.argv[3])
          registerBits = int(sys.argv[4])
          bimodalNoOfBits = int(sys.argv[5])
          traceFile = sys.argv[6]
          # Creating instances for gshare and bimodal and passing it to hybrid instance
          gsharePredictor = GShare(3,gShareNoOfBits,registerBits) 
          bimodalPredictor = Bimodal(3,bimodalNoOfBits,0)
          branchPredictor = Hybrid(chooserBits,gsharePredictor,bimodalPredictor)
    
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

    # Displaying the output as required
    branchPredictor.display(traceFile)

    
   