import re

f_name = input('Enter File name :')
f_handle = open(f_name)
total = 0
count = 0

for line in f_handle:
    number_list = re.findall('[0-9]+', line)
    for item in number_list:
        if int(item) >= 0:
            count = count + 1
            total += int(item)

print(count, 'numbers found', 'and the total sum is', total)