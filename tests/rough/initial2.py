import sys

  
predic = sys.argv[1]
Bits = int(sys.argv[2])
file = sys.argv[3]

def smith(Bits,file):
    curr = int(2**Bits/2)
    pc = 0
    wrong_count = 0
    f = open(file,'r')
    for branch in f:
        pc = pc+1
        if curr >= 2**Bits/2: 
            char = 't'
        else:
            char = 'n'
        
        if branch.strip().split(' ')[1] != char:
            wrong_count = wrong_count+1
        
        if branch.strip().split(' ')[1] == 't':
             if curr != 2**Bits-1:
                curr = curr+1
        else:
            if curr !=0:
                curr = curr-1
    
    print("COMMAND")
    print("./sim smith ",Bits," ",file)
    print("OUTPUT")
    print("number of predictions:\t",pc)
    print("number of mispredictions:\t",wrong_count)
    print(f"misprediction rate:\t {wrong_count*100/pc:.2f}%")
    print("FINAL COUNTER CONTENT:          ",curr)

def bimodal(Bits,file):
    counter = [4]*2**Bits
    f = open(file,'r')
    pc = 0
    wrong_count =0
    for branch in f:
        pc = pc+1
        address = branch.strip().split(' ')[0]
        bin_address = bin(int(address,16))[2:].zfill(32)
        index = int(bin_address[slice(30-Bits,30)],2)
        if counter[index]>=4:
            char='t'
        else: 
            char='n'
        if branch.strip().split(' ')[1] != char:
            wrong_count = wrong_count+1

        if branch.strip().split(' ')[1] == 't':
             if counter[index] != 7:
                counter[index] = counter[index]+1
        else:
            if counter[index] !=0:
                counter[index] = counter[index]-1

    print("COMMAND")
    print("./sim bimodal ",Bits," ",file)
    print("OUTPUT")
    print("number of predictions:\t",pc)
    print("number of mispredictions:\t" ,wrong_count)
    print(f"misprediction rate:\t {wrong_count*100/pc:.2f}%")
    print("FINAL BIMODAL CONTENTS")
    for i in range(0,2**Bits):
        print(i," ",counter[i])


def gshare(Bits,gbits,file):
    gshare_reg = '0'*gbits
    counter = [4]*2**Bits
    pc = 0
    wrong_count =0
    f = open(file,'r')
    for branch in f:
        pc = pc+1
        address = branch.strip().split(' ')[0]
        bin_address = bin(int(address,16))[2:].zfill(32)
        key = int(bin_address[slice(30-gbits,30)],2)
        key = key ^ int(gshare_reg,2)
        m = bin_address[slice(30-Bits,30-gbits)]
        index = int(m+bin(key)[2:].zfill(gbits),2)
        if counter[index]>=4:
            char='t'
        else: 
            char='n'
        if branch.strip().split(' ')[1] != char:
            wrong_count = wrong_count+1

        if branch.strip().split(' ')[1] == 't':
            if counter[index] != 7:
                counter[index] = counter[index]+1
            gshare_reg = bin(int(gshare_reg,2)>>1)[2:].zfill(gbits)
            gshare_reg = gshare_reg.replace('0','1',1)
             
        else:
            if counter[index] !=0:
                counter[index] = counter[index]-1
            gshare_reg = bin(int(gshare_reg,2)>>1)[2:].zfill(gbits)
   
    print("COMMAND")
    print("./sim gshare ",Bits," ",gbits," ",file)
    print("OUTPUT")
    print("number of predictions:\t",pc)
    print("number of mispredictions:\t" ,wrong_count)
    print(f"misprediction rate:\t {wrong_count*100/pc:.2f}%")
    print("FINAL GSHARE CONTENTS")
    for i in range(0, 2**Bits):
        print(i,"   " ,counter[i])

def hybrid(Bits,m1bits,nbits,m2bits,file):
    gshare_reg = "0"*nbits
    hybrid_counter = [1]*2**Bits
    gshare_counter = [4]*2**m1bits
    bimodal_counter = [4]*2**m2bits
    pc = 0
    wrong_count =0
    f = open(file,'r')
    for branch in f:
        pc = pc+1
        address = branch.strip().split(' ')[0]
        bin_address = bin(int(address,16))[2:].zfill(32)
        hybrid_index = int(bin_address[slice(30-Bits,30)],2)
        
        bimodal_index = int(bin_address[slice(30-m2bits,30)],2)
        if bimodal_counter[bimodal_index] >= 4:
            bimodal_char = "t"
        else: 
            bimodal_char = "n"
        
        key = int(bin_address[slice(30-nbits,30)],2)
        key = key ^ int(gshare_reg,2)
        m = bin_address[slice(30-m1bits,30-nbits)]
        gshare_index = int(m+bin(key)[2:].zfill(nbits),2)
        if gshare_counter[gshare_index] >= 4:
            gshare_char = "t" 
        else:
            gshare_char = "n"
            
        if hybrid_counter[hybrid_index] >= 2:
            if branch.strip().split(' ')[1] != gshare_char:
                wrong_count = wrong_count+1
            if branch.strip().split(' ')[1] == 't':
                if gshare_counter[gshare_index] != 7:
                    gshare_counter[gshare_index] = gshare_counter[gshare_index]+1
            else:
                if gshare_counter[gshare_index] != 0:
                    gshare_counter[gshare_index] = gshare_counter[gshare_index]-1
        else:
            if branch.strip().split(' ')[1] != bimodal_char:
                wrong_count = wrong_count+1
            if branch.strip().split(' ')[1] == 't':
                if bimodal_counter[bimodal_index] != 7:
                    bimodal_counter[bimodal_index] = bimodal_counter[bimodal_index]+1
            else:
                if bimodal_counter[bimodal_index] != 0:
                    bimodal_counter[bimodal_index] = bimodal_counter[bimodal_index]-1
                        
        if branch.strip().split(' ')[1] == 't':
            gshare_reg = bin(int(gshare_reg,2)>>1)[2:].zfill(nbits)
            gshare_reg = gshare_reg.replace('0','1',1)
             
        else:
            gshare_reg = bin(int(gshare_reg,2)>>1)[2:].zfill(nbits)
      
        if branch.strip().split(' ')[1] == bimodal_char and branch.strip().split(' ')[1] != gshare_char: 
            if hybrid_counter[hybrid_index] != 0:
                hybrid_counter[hybrid_index] = hybrid_counter[hybrid_index] -1
                
        elif branch.strip().split(' ')[1] != bimodal_char and branch.strip().split(' ')[1] == gshare_char:
            if hybrid_counter[hybrid_index] != 3:
                hybrid_counter[hybrid_index] = hybrid_counter[hybrid_index] +1
       

    print("COMMAND")
    print("./sim hybrid ",Bits," ",m1bits," ",nbits," ",m2bits," ",file)
    print("OUTPUT")
    print("number of predictions:\t",pc)
    print("number of mispredictions:\t",wrong_count)
    print(f"misprediction rate:\t {wrong_count*100/pc:.2f}%")
    print("FINAL CHOOSER CONTENTS")
    for i in range(0, 2**Bits):
        print(i,"   " ,hybrid_counter[i])
    print("FINAL GSHARE CONTENTS")
    for i in range(0, 2**m1bits):
        print(i,"   " ,gshare_counter[i])
    print("FINAL BIMODAL CONTENTS")
    for i in range(0, 2**m2bits):
        print(i,"   " ,bimodal_counter[i])

if predic == "smith":
    smith(Bits ,file)
elif predic == "bimodal":
    bimodal(Bits,file)
if predic == "gshare":
    gbits = int(sys.argv[3])
    file = sys.argv[4]
    gshare(Bits,gbits,file)
elif predic == "hybrid":
    m1bits = int(sys.argv[3])
    nbits = int(sys.argv[4])
    m2bits = int(sys.argv[5])
    file = sys.argv[6]
    hybrid(Bits,m1bits,nbits,m2bits,file)    
