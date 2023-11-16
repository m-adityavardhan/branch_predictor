from counter import Counter

class Smith(Counter):
    def getIndex(self,branchPC):
        # As only one counter return index 0
        return 0

    def getMissRate(self):
        # calculate miss rate and return
        return self.missCount*100/self.totalCount

    def display(self,traceFile):
        self.missRate = self.getMissRate()
        # printing output as required 
        print('''COMMAND
./sim smith {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL COUNTER CONTENT:		{}'''.format(self.noOfCounterBits,traceFile,self.totalCount,self.missCount,missRate,self.current_counter_value))
