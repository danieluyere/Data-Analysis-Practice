fhandle = open('classroom_iaq.txt')
next(fhandle) #skip header

classrooms_co2 = dict() #keeps track of classrooms and number of co2 exceedances
for line in fhandle:
    line = line.strip()
    
    if len(line) < 1: #skips empty line
        continue
    data = line.split(',')

    if len(data) < 3: 
        print('wrong formatting')
        continue

    classroom = data[0]
    co2 = data[2]

    try:
        co2 = int(co2)
    except:
        print('not int')
        continue

    if co2 > 1000:
        classrooms_co2[classroom] = classrooms_co2.get(classroom, 0) + 1
        #only triggers if co2 exceeds 1000

for key, val in sorted(classrooms_co2.items()):
    print(f'{key} exceeded 1000ppm {val} times')

# classrooms_list = list()
# for key, val in classrooms_co2.items():
#     flipT = (val, key) #turple = turple :)
#     classrooms_list.append(flipT) #adds flipped turple to list to enable proper sorting

# print(classrooms_list)