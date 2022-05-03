import os
lines = []
with open(os.getcwd()+'/nicoculpable.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')   