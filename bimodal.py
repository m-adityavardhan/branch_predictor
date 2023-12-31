from counter import Counter
class Bimodal(Counter):
    def getIndex(self, branchPC):
        # Calculating index for bimodal by extracting required bits from pc
        binary = bin(int(branchPC, 16))[2:].zfill(32) #converting hex to binary
        # returning extracted bits
        return int(binary[-2-self.noOfIndexBits: -2],2)

    def getMissRate(self):
        # calculate miss rate and return
        return self.missCount*100/self.totalCount
  
    def display(self,traceFile):
        self.missRate = self.getMissRate()
        # printing output as required 
        print('''COMMAND
./sim bimodal {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL BIMODAL CONTENTS'''.format(self.noOfIndexBits,traceFile,self.totalCount,self.missCount,self.missRate))
        for count,index in enumerate(self.predictorTable):
            print('{}\t{}'.format(count,index))
        

        