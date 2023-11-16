from counter import Counter

class Hybrid(Counter):
    def __init__(self,chooserBits,gsharePredictor,bimodalPredictor):
        self.chooserBits = chooserBits
        self.gsharePredictor = gsharePredictor
        self.bimodalPredictor = bimodalPredictor
        self.chooserTable = [1] * pow(2,self.chooserBits)
        self.missCount = 0
        self.totalCount = 0

    def getIndex(self,branchPC):
        self.branchPc = branchPC
        binary = bin(int(branchPC, 16))[2:].zfill(32)
        return int(binary[-2-self.chooserBits: -2],2)
       

    def predict(self,index,actualPrediction,isReturnPrediction):
        self.totalCount += 1
        gsharePrediction = self.gsharePredictor.predict(self.gsharePredictor.getIndex(self.branchPc),actualPrediction,True)
        bimodalPrediction = self.bimodalPredictor.predict(self.bimodalPredictor.getIndex(self.branchPc),actualPrediction,True)
        if self.chooserTable[index] >=2 :
            self.gsharePredictor.predict(self.gsharePredictor.getIndex(self.branchPc),actualPrediction,False)
            if gsharePrediction != actualPrediction:
                self.missCount += 1
        else:
            self.bimodalPredictor.predict(self.bimodalPredictor.getIndex(self.branchPc),actualPrediction,False)
            if bimodalPrediction != actualPrediction:
                self.missCount += 1
        self.gsharePredictor.updateBranchRegistry(actualPrediction)
        if gsharePrediction == actualPrediction and bimodalPrediction != actualPrediction:
            self.chooserTable[index] = min(self.chooserTable[index]+1,3)
        elif gsharePrediction != actualPrediction and bimodalPrediction == actualPrediction:
            self.chooserTable[index] = max(0,self.chooserTable[index]-1)


    def display(self, traceFile):
        missRate = self.missCount*100/self.totalCount
        gShareNoOfBits = self.gsharePredictor.noOfIndexBits
        registerBits = self.gsharePredictor.noOfRegisterBits
        bimodalNoOfBits = self.bimodalPredictor.noOfIndexBits
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

                
#         f = open('out.txt', "w")
#         f.write('''COMMAND
# ./sim hybrid {} {} {} {} {}
# OUTPUT
# number of predictions:		{}
# number of mispredictions:	{}
# misprediction rate:		{:.2f}%
# FINAL CHOOSER CONTENTS\n'''.format(self.chooserBits,gShareNoOfBits,registerBits,bimodalNoOfBits,traceFile,self.totalCount,self.missCount,missRate))
#         for count,index in enumerate(self.chooserTable):
#             f.write('{}\t{}\n'.format(count,index))
#         f.write('FINAL GSHARE CONTENTS\n')
#         for count,index in enumerate(self.gsharePredictor.predictorTable):
#             f.write('{}\t{}\n'.format(count,index))
#         f.write('FINAL BIMODAL CONTENTS\n')
#         for count,index in enumerate(self.bimodalPredictor.predictorTable):
#             f.write('{}\t{}\n'.format(count,index))
#         f.close()


