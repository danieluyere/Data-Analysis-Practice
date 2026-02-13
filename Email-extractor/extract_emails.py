import re

fname = input('Enter file name: ')

try:fhandle = open(fname)
except:
    print('Enter a valid text file, ending with: .txt')
    print('Using default file...')
    fhandle = open('survey_notes.txt')

count = 0
for line in fhandle:
    line = line.rstrip()

    emails = re.findall('\S+@\S+', line)
    
    if len(emails) < 1: #skips empty email lines
        continue
    
    for email in emails:
        print(email)
        count = count + 1


print(f'The total count of emails is {count}')


