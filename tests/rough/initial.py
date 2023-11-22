import sys

if __name__=='__main__':
    predictor = sys.argv[1]
    count = 0
    total = 0

    if predictor  == 'smith':
        b = int(sys.argv[2])
        traceFile = sys.argv[3]
        max_value = 2**b
        half = curr = max_value//2

    if predictor == 'bimodal':
        m2 = int(sys.argv[2])
        traceFile = sys.argv[3]
        arrB = [4] * 2**m2

    if predictor == 'gshare':
        m1 = int(sys.argv[2])
        n = int(sys.argv[3])
        traceFile = sys.argv[4]
        arrG = [4] * 2**m1
        regis = '0' * n

    if predictor == 'hybrid':
        k = int(sys.argv[2])
        m1 = int(sys.argv[3])
        n = int(sys.argv[4])
        m2 = int(sys.argv[5])
        traceFile = sys.argv[6]
      
        arrB = [4] * 2**m2
        arrG = [4] * 2**m1
        chooser = [1] * 2**k
        regis = '0' * n

    f = open(traceFile, "r")
    # Read each instruction from trace file
    for instruction in f:
        total += 1
        pc,actual = instruction.strip().split(' ')
        binary = bin(int(pc, 16))[2:].zfill(32)
        if predictor == 'smith':
            if curr >= half:
                pred = 't'
            else:
                pred = 'n'
            if actual != pred:
                count += 1
            if actual == 't':
                curr = min(curr+1,max_value-1)
            else:
                curr = max(0,curr-1)

        elif predictor == 'bimodal':
            index  = int(binary[-2-m2: -2],2)
            curr = arrB[index]
            if curr >= 4:
                pred = 't'
            else:
                pred = 'n'
            if actual != pred:
                count += 1
            if actual == 't':
                curr = min(curr+1,7)
            else:
                curr = max(0,curr-1)
            arrB[index] = curr
        
        elif predictor == 'gshare':
            temp = binary[-2-m1: -2]
            m,nIndex  = temp[:-n],temp[-n:]
            low = int(nIndex,2) ^ int(regis,2)
            index = int(m+bin(low)[2:].zfill(n),2)
            curr = arrG[index]
            if curr >= 4:
                pred = 't'
            else:
                pred = 'n'
            if actual != pred:
                count += 1
            if actual == 't':
                curr = min(curr+1,7)
            else:
                curr = max(0,curr-1)
            arrG[index] = curr
            if actual == 't':
                update = '1' 
            else:
                update = '0' 
            regis = update + regis[:-1]
        else:  
            temp = binary[-2-m1: -2]
            m,nIndex  = temp[:-n],temp[-n:]
            low = int(nIndex,2) ^ int(regis,2)
            indexG = int(m+bin(low)[2:].zfill(n),2)
            currG = arrG[indexG]
            if currG >= 4:
                predG = 't'
            else:
                predG = 'n'

            indexB  = int(binary[-2-m2: -2],2)
            currB = arrB[indexB]
            if currB >= 4:
                predB = 't'
            else:
                predB = 'n'
            
            indexk = int(binary[-2-k:-2],2)
            if chooser[indexk] >= 2:
                if actual != predG:
                    count += 1
                if actual == 't':
                    currG = min(currG+1,7)
                else:
                    currG = max(0,currG-1)
                arrG[indexG] = currG
            else:
                if actual != predB:
                    count += 1
                if actual == 't':
                    currB = min(currB+1,7)
                else:
                    currB = max(0,currB-1)
                arrB[indexB] = currB          
 
            if actual == 't':
                update = '1' 
            else:
                update = '0' 
            regis = update + regis[:-1]

            if predG == actual and predB != actual:
                chooser[indexk] = min(chooser[indexk]+1,3)
            elif predB == actual and predG != actual:
                chooser[indexk] = max(0,chooser[indexk]-1)

    if predictor  == 'smith':
        print(f"COMMAND\n./sim smith {b} {traceFile}\nOUTPUT\nnumber of predictions:		{total}\nnumber of mispredictions:	{count}\nmisprediction rate:		{count*100/total:.2f}%\nFINAL COUNTER CONTENT:		{curr}\n")
    elif predictor == 'bimodal':
        print(f"COMMAND\n./sim bimodal {m2} {traceFile}\nOUTPUT\nnumber of predictions:		{total}\nnumber of mispredictions:	{count}\nmisprediction rate:		{count*100/total:.2f}%\nFINAL BIMODAL CONTENTS")
        for i in range(len(arrB)):
            print(i,arrB[i]) 
    elif predictor == 'gshare':
        print(f"COMMAND\n./sim gshare {m1} {n} {traceFile}\nOUTPUT\nnumber of predictions:		{total}\nnumber of mispredictions:	{count}\nmisprediction rate:		{count*100/total:.2f}%\nFINAL GSHARE CONTENTS")
        for i in range(len(arrG)):
            print(i,arrG[i])
    elif predictor == 'hybrid':
        print(f"COMMAND\n./sim hybrid {k} {m1} {n} {m2} {traceFile}\nOUTPUT\nnumber of predictions:		{total}\nnumber of mispredictions:	{count}\nmisprediction rate:		{count*100/total:.2f}%\nFINAL CHOOSER CONTENTS")
        for i in range(len(chooser)):
            print(i,chooser[i])
        print('FINAL GSHARE CONTENTS')
        for i in range(len(arrG)):
            print(i,arrG[i])
        print('FINAL BIMODAL CONTENTS')
        for i in range(len(arrB)):
            print(i,arrB[i])
