# using sys module
# Big O time complexity
# use of boolean




import sys
inputs = sys.stdin.readline().split()
n = int(inputs[0])
t = int(inputs[1])
sQueue = sys.stdin.readline().strip()
for sec in range(t):
    flag = False
    for i in range(n):
        if flag: 
            flag = False
            continue
        if sQueue[i] == "B" and i != n -1 and sQueue[i+1] == "G":
            sQueue = sQueue[:i] + sQueue[i+1] + sQueue[i] + sQueue[i+2:]
            flag = True
print(sQueue)
