from counter import Counter

class Smith(Counter):
    def getIndex(self,branchPC):
        return 0
        
    def display(self,traceFile):
        missRate = self.missCount*100/self.totalCount
        print('''COMMAND
./sim smith {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL COUNTER CONTENT:		{}'''.format(self.noOfCounterBits,traceFile,self.totalCount,self.missCount,missRate,self.current_counter_value))
        
        
#         f = open('out.txt', "w")
#         f.write('''COMMAND
# ./sim smith {} {}
# OUTPUT
# number of predictions:		{}
# number of mispredictions:	{}
# misprediction rate:		{:.2f}%
# FINAL COUNTER CONTENT:		{}'''.format(self.noOfCounterBits,traceFile,self.totalCount,self.missCount,missRate,self.current_counter_value))
#         f.close()