

#unix epoch reference across programming community a simple program that can 
#tell how long it took to run the particular piece of code . 
#but before that you should know what unix epoch is for usin it you need to import
#time module and it has a function time.time()  which gives you the time in seconds which 
#has passed between epoch time and current. unix epoch : january 1 1970


import time 

def sum():
    sum = 0
    for i in range(1,100000000):
        sum = sum + 1
        
    return sum 
 
timestart = time.time()
print(timestart)

s = sum()#call to the function

timeend = time.time()
print(timeend)

timetaken = timeend - timestart

print (f" It took   {timetaken}   seconds to run the whole program .") #using f string 