fhandle = open('dummy_iaq_log.txt')

next(fhandle) #skips header

count = 0 #tracks co2 exceedances
for line in fhandle:
    line = line.rstrip()

    if len(line) < 1: 
        continue #skip empty line and protect my code :)

    data = line.split(',')

    if len(data) < 3:
        continue #need atleast 3 valid data point to run

    timestamp = data[1]
    co2 = data[2]

    timestamp = timestamp.split()
    date = timestamp[0] 
    time = timestamp[1]

    try:
        co2 = int(co2) #attempt to convert co2 to integer
    except:
        print('not integer')
        continue

    if co2 > 1000:
        count = count + 1
        print(f'ALERT: {date} {time} - C02: {co2}')

print(f'The total CO2 exceedance above recommended threshold is {count}')
    
