class Counter():
    def __init__(self,noOfCounterBits,noOfIndexBits,noOfRegisterBits):
        self.noOfCounterBits = noOfCounterBits
        self.noOfIndexBits = noOfIndexBits
        self.noOfRegisterBits = noOfRegisterBits
        self.totalCount = 0
        self.missCount = 0
        self.max_counter_value = pow(2,self.noOfCounterBits)
        self.half_value = self.max_counter_value//2
        self.predictorTable = [self.half_value] * pow(2,self.noOfIndexBits)
        self.branchRegister = '0' * self.noOfRegisterBits
    
    def getIndex(self,branchPC):
        pass

    def predict(self,index,actualPrediction,isReturnPrediction):
        self.current_counter_value = self.predictorTable[index]
        if self.current_counter_value >= self.half_value:
            prediction = 't'
        else:
            prediction = 'n'

        if isReturnPrediction:
            return prediction
        
        self.totalCount += 1
        if actualPrediction != prediction:
            self.missCount += 1
        if actualPrediction == 't':
            self.current_counter_value = min(self.current_counter_value+1,self.max_counter_value-1)
        else:
            self.current_counter_value = max(0,self.current_counter_value-1)
        self.predictorTable[index] = self.current_counter_value
    
    def display(self,*args):
        pass

    def updateBranchRegistry(self,actualPrediction):
        pass
    


