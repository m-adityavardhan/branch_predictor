def smithOutputToFile(self,traceFile,missRate):        
        f = open('out.txt', "w")
        f.write('''COMMAND
./sim smith {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL COUNTER CONTENT:		{}'''.format(self.noOfCounterBits,traceFile,self.totalCount,self.missCount,missRate,self.current_counter_value))
        f.close()


def bimodalOutputToFile(self,traceFile,missRate):
        f = open('out.txt', "w")
        f.write('''COMMAND
./sim bimodal {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL BIMODAL CONTENTS\n'''.format(self.noOfIndexBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.predictorTable):
            f.write('{}\t{}\n'.format(count,index))
        f.close()


def gshareOutputToFile(self,traceFile,missRate):        
        f = open('out.txt', "w")
        f.write('''COMMAND
./sim gshare {} {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL GSHARE CONTENTS\n'''.format(self.noOfIndexBits,self.noOfRegisterBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.predictorTable):
            f.write('{}\t{}\n'.format(count,index))
        f.close()


def hybridOutputToFile(self,traceFile,missRate,gShareNoOfBits,registerBits,bimodalNoOfBits):        
        f = open('out.txt', "w")
        f.write('''COMMAND
./sim hybrid {} {} {} {} {}
OUTPUT
number of predictions:		{}
number of mispredictions:	{}
misprediction rate:		{:.2f}%
FINAL CHOOSER CONTENTS\n'''.format(self.chooserBits,gShareNoOfBits,registerBits,bimodalNoOfBits,traceFile,self.totalCount,self.missCount,missRate))
        for count,index in enumerate(self.chooserTable):
            f.write('{}\t{}\n'.format(count,index))
        f.write('FINAL GSHARE CONTENTS\n')
        for count,index in enumerate(self.gsharePredictor.predictorTable):
            f.write('{}\t{}\n'.format(count,index))
        f.write('FINAL BIMODAL CONTENTS\n')
        for count,index in enumerate(self.bimodalPredictor.predictorTable):
            f.write('{}\t{}\n'.format(count,index))
        f.close()