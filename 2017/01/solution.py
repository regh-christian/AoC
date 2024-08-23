import sys
from collections import defaultdict

with open("test.txt") as f:
    testdata = f.read().splitlines()

with open("input.txt") as f:
    inputdata = f.read().splitlines()

if sys.argv[1] == "test":
    data = testdata
else:
    data = inputdata

data = [int(x) for x in data]

def solution(part):
    total = 0
    
    for i in range(len(data)):
        
        if part == 1:
            if i >= 1:
                if data[i] > data[i - 1]:
                    total += 1            
            
        elif part == 2:
            if i >= 3:
                if sum(data[i-3:i]) > sum(data[i-4:i-1]):
                    total += 1

    return total
    
print("Part 1:", solution(1))
print("Part 2:", solution(2))