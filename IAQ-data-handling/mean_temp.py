fhandle = open('dummy_iaq_log.txt') 

tempList = list() #stores temperature values after each iteration
total = 0
count = 0
for line in fhandle:
    line = line.rstrip()

    if not line.startswith('IAQ-001'): #filters header :)
        continue
    
    column = line.split(',')

    temp = column[3]
    temp = temp.strip() #ensures no white spaces
    temp = float(temp) #converts temperature to a float.

    tempList.append(temp)
    
for temp in tempList:
    total = total + temp
    count = count + 1

avg = total/count
favg = round(avg, 3)   
print('The mean average of temperatures is', favg)   