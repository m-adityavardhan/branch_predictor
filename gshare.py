from counter import Counter
class GShare(Counter):
    def getIndex(self, branchPC):
        #converting hex to binary
        binary = bin(int(branchPC, 16))[2:].zfill(32)
        # Extracting index bits from PC
        indexBits = binary[-2-self.noOfIndexBits: -2]
        # extracting bhr bits from pc
        m,n  = indexBits[:-self.noOfRegisterBits],indexBits[-self.noOfRegisterBits:]
        # calculating XOR between bhr and bhr bits from pc
        low = int(n,2) ^ int(self.branchRegister,2)
        # converting the Xor value back to binary and appending it to rest of index bits to return final index value
        return int(m+bin(low)[2:].zfill(self.noOfRegisterBits),2)
    
    def getMissRate(self):
        # calculate miss rate and return
        return self.missCount*100/self.totalCount

    def display(self, traceFile):
        self.missRate = self.getMissRate()
        # printing output as required 
        print('''COMMAND
./sim gshare {} {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL GSHARE CONTENTS'''.format(self.noOfIndexBits,self.noOfRegisterBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.predictorTable):
            print('{}\t{}'.format(count,index))
    
    def updateBranchRegistry(self,actualPrediction):
        # Updating BHR based on actual prediction
        if actualPrediction == 't':
            # Add 1 at left end and remove last(right most) bit from BHR
            self.branchRegister = '1' + self.branchRegister[:-1]
        else:
            # Add 0 at left end and remove last(right most) bit from BHR
            self.branchRegister = '0' + self.branchRegister[:-1]


