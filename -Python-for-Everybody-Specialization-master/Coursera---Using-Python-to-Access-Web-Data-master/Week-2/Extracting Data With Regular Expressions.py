import time
import re
start  = time.time()
file = open("regex_sum_417433.txt",'r')
sum = 0
for line in file:
    f = re.findall('[0-9]+',line)
    for num in f:
        if int(num) >= 0:
            sum = sum+int(num)

print(list)
end = time.time()

print("The total excecution Time for this code is sec", (end-start))


#Output : -
# Answer = 331308
