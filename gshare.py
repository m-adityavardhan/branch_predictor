from counter import Counter
class GShare(Counter):
    def getIndex(self, branchPC):
        binary = bin(int(branchPC, 16))[2:].zfill(32)
        indexBits = binary[-2-self.noOfIndexBits: -2]
        m,n  = indexBits[:-self.noOfRegisterBits],indexBits[-self.noOfRegisterBits:]
        low = int(n,2) ^ int(self.branchRegister,2)
        return int(m+bin(low)[2:].zfill(self.noOfRegisterBits),2)
    
    def display(self, traceFile):
        missRate = self.missCount*100/self.totalCount
        print('''COMMAND
./sim gshare {} {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL GSHARE CONTENTS'''.format(self.noOfIndexBits,self.noOfRegisterBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.predictorTable):
            print('{}\t{}'.format(count,index))
        
#         f = open('out.txt', "w")
#         f.write('''COMMAND
# ./sim gshare {} {} {}
# OUTPUT
# number of predictions:		{}
# number of mispredictions:	{}
# misprediction rate:		{:.2f}%
# FINAL GSHARE CONTENTS\n'''.format(self.noOfIndexBits,self.noOfRegisterBits,traceFile,self.totalCount,self.missCount,missRate))
#         for count,index in enumerate(self.predictorTable):
#             f.write('{}\t{}\n'.format(count,index))
#         f.close()
    
    def updateBranchRegistry(self,actualPrediction):
        if actualPrediction == 't':
            self.branchRegister = '1' + self.branchRegister[:-1]
        else:
            self.branchRegister = '0' + self.branchRegister[:-1]


