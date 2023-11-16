from counter import Counter
class Bimodal(Counter):
    def getIndex(self, branchPC):
        binary = bin(int(branchPC, 16))[2:].zfill(32)
        return int(binary[-2-self.noOfIndexBits: -2],2)
        
    def display(self,traceFile):
        missRate = self.missCount*100/self.totalCount
        print('''COMMAND
./sim bimodal {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL BIMODAL CONTENTS'''.format(self.noOfIndexBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.predictorTable):
            print('{}\t{}'.format(count,index))
        
#         f = open('out.txt', "w")
#         f.write('''COMMAND
# ./sim bimodal {} {}
# OUTPUT
# number of predictions:		{}
# number of mispredictions:	{}
# misprediction rate:		{:.2f}%
# FINAL BIMODAL CONTENTS\n'''.format(self.noOfIndexBits,traceFile,self.totalCount,self.missCount,missRate))
#         for count,index in enumerate(self.predictorTable):
#             f.write('{}\t{}\n'.format(count,index))
#         f.close()
        