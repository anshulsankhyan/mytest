import re
import numpy as np
an = open('C:\\Users\\anshu\\Downloads\\a2p5z.txt')
lines = an.readlines(-1)
an.close()
print ('The task to perform\n1. account balances for different types of accounts.\n2. total amount of transaction (debit + credit) for different types of accounts.')
a = input('Enter the task\n') 
for line in lines:
    if a=='1':
        if 'Rs' in line:
            print(re.findall('Rs.([a-z0-9]+)', line) + re.findall('..-......', line))
    elif a=='2':
        if 'Avl bal' in line:
            print(re.findall('Avl/sbal.([a-z0-9]+)', line) + re.findall('..-......', line))
    else:
        break