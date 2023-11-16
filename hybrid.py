from counter import Counter

class Hybrid(Counter):
    def __init__(self,chooserBits,gsharePredictor,bimodalPredictor):
        # Initialising counters and chooser table and class members
        self.chooserBits = chooserBits
        self.gsharePredictor = gsharePredictor
        self.bimodalPredictor = bimodalPredictor
        self.chooserTable = [1] * pow(2,self.chooserBits)
        self.missCount = 0
        self.totalCount = 0

    def getIndex(self,branchPC):
        self.branchPc = branchPC
        # Calculating index for hybrid by extracting required bits from pc for chooser table
        binary = bin(int(branchPC, 16))[2:].zfill(32)
        return int(binary[-2-self.chooserBits: -2],2)
       

    def predict(self,index,actualPrediction,isReturnPrediction):
        self.totalCount += 1
        # getting predictions for current instruction from both gshare and bimodal predictors
        gsharePrediction = self.gsharePredictor.predict(self.gsharePredictor.getIndex(self.branchPc),actualPrediction,True)
        bimodalPrediction = self.bimodalPredictor.predict(self.bimodalPredictor.getIndex(self.branchPc),actualPrediction,True)
        # Value in chooser counter is greater than or equal to 2 choose gshare else bimodal
        if self.chooserTable[index] >=2 :
            # predict again and update prediction table and counter in gshare instance
            self.gsharePredictor.predict(self.gsharePredictor.getIndex(self.branchPc),actualPrediction,False)
            # update miss count
            if gsharePrediction != actualPrediction:
                self.missCount += 1
        else:
            # predict again and update prediction table and counter in bimodal instance
            self.bimodalPredictor.predict(self.bimodalPredictor.getIndex(self.branchPc),actualPrediction,False)
            # update miss count
            if bimodalPrediction != actualPrediction:
                self.missCount += 1
        # Update BHR in gshare irrespective of predictor chosed
        self.gsharePredictor.updateBranchRegistry(actualPrediction)
        
        # updating chooser table based on predictors predictions
        if gsharePrediction == actualPrediction and bimodalPrediction != actualPrediction:
            # increment chooser count if gshare is correct and bimodal is wrong
            self.chooserTable[index] = min(self.chooserTable[index]+1,3)
        elif gsharePrediction != actualPrediction and bimodalPrediction == actualPrediction:
            # decrement chooser count if gshare is wrong and bimodal is correct
            self.chooserTable[index] = max(0,self.chooserTable[index]-1)

    def getMissRate(self):
        # calculate miss rate and return
        return self.missCount*100/self.totalCount

    def display(self, traceFile):
        self.missRate = self.getMissRate()
        gShareNoOfBits = self.gsharePredictor.noOfIndexBits
        registerBits = self.gsharePredictor.noOfRegisterBits
        bimodalNoOfBits = self.bimodalPredictor.noOfIndexBits
        # printing output as required 
        print('''COMMAND
./sim hybrid {} {} {} {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL CHOOSER CONTENTS'''.format(self.chooserBits,gShareNoOfBits,registerBits,bimodalNoOfBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.chooserTable):
            print('{}\t{}'.format(count,index))
        print('FINAL GSHARE CONTENTS')
        for count,index in enumerate(self.gsharePredictor.predictorTable):
            print('{}\t{}'.format(count,index))
        print('FINAL BIMODAL CONTENTS')
        for count,index in enumerate(self.bimodalPredictor.predictorTable):
            print('{}\t{}'.format(count,index))


