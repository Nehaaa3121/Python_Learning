# A loop means to repeat something in the exact same way
#Types of loops are :
# 1. For loop
#2. While loop
# 3. while true
# 4. Nested loop


#for loop is a loop that repeats something in a given range. The range has a starting point , ending point and a set int it.
# +1 is added to the endong point while defining a range

# structure of for loop :-

# for (varaible) int range (1,6):

for  i in range(1,6):
    print("hello world")
    
    #print number from 1 to 100
for i in range (1, 101):
      print(i)
      
      # for printing odd number from 1 to 100
      for i in range(1, 101 ,2):
          print(i)

#for printing even number from 1 to 100
for i in range (0, 101, 2):
    print(i)

# printing table of 25
n = 25
for i in range (1, 11):
 print( n, "x ", i , "=", n*i)