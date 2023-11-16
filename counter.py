class Counter():
    def __init__(self,noOfCounterBits,noOfIndexBits,noOfRegisterBits):
        # Initialising counters and prediction table and class members
        self.noOfCounterBits = noOfCounterBits
        self.noOfIndexBits = noOfIndexBits
        self.noOfRegisterBits = noOfRegisterBits
        self.totalCount = 0
        self.missCount = 0
        self.max_counter_value = pow(2,self.noOfCounterBits)
        self.half_value = self.max_counter_value//2
        self.predictorTable = [self.half_value] * pow(2,self.noOfIndexBits)
        self.branchRegister = '0' * self.noOfRegisterBits
    
    # dummy  function which will be overwritten by child classes
    def getIndex(self,branchPC):
        pass

    def predict(self,index,actualPrediction,isReturnPrediction):
        # Predicting the outcome based on current counter value
        self.current_counter_value = self.predictorTable[index]
        if self.current_counter_value >= self.half_value:
            prediction = 't'
        else:
            prediction = 'n'

        # If true then dont update the table,counter just return the prediction ( useful in hybrid predictor where prediction are required but no action is performed)
        if isReturnPrediction:
            return prediction
        
        self.totalCount += 1
        # updating miss count based on prediction
        if actualPrediction != prediction:
            self.missCount += 1
        # updating the counter based on actual prediction
        if actualPrediction == 't':
            # Incrementing counter but saturating it at max value
            self.current_counter_value = min(self.current_counter_value+1,self.max_counter_value-1)
        else:
            # decrementing counter but saturating it at 0
            self.current_counter_value = max(0,self.current_counter_value-1)
        # updating the counter value in prediction table
        self.predictorTable[index] = self.current_counter_value
    
    # dummy  function which will be overwritten by child classes
    def display(self,*args):
        pass

    # dummy  function which will be overwritten by child classes
    def updateBranchRegistry(self,actualPrediction):
        pass
    


