#operators indicates what operation is to be performed while operands indicates on what the action or the operation should be performed.
#types of operatos 
#1. Arithmetic Operators, 2. Comparison Operators. 3. , Logical Operators, 4. Assignment Operatos , 5. Indetify operators 
#6. Membership operators, 7 , Bitwise Operators 

# Arithmetic Operation
# addition
print(2+3)

#substraction
print(8-6)

#exponential
print(2**10)

#multiplication
print(2*47)

#floor division
print(21//2)

#division
print(10/5)

#modulus
print(53%8)


#Comparison Operator

#Less than

print(3<4)

#equal to

print(4==4)

#greater than

print(4>2)

#not equal to

print(2+9 != 8+7)

#less than or equal to
print(4-2 <= 2-0)

#greater than or equal to
print(9>=10)

#Logical Operators
#And Operator : true if both the operands are true
#or operator : true id either of the operands is true
#not: true if operand is false

#And operator :
print(2>1 and 4<9)

#or operator 
print(2>1 or 3<1)


#Assignment operators 
 # = : x = 3
 # +=   :  x+=9 x= x+9
 # -= : x-=   x = x-6
 # x= *6  x= x*6
 
#identity operator are used to compare items to see if they are the same object with the same memory address
# type 1. Is , 2.Is not
a= 1234
b = 1234
print(a is b)

a= 1236
b = "enha"
print(a is not b)


# bitwise operator
# it used for the binary operations

# printing binary number
print(bin(19))

#And Operation
  # 0 ,0 = 0
  # 0 , 1 = 0
  # 1, 0 = 0
  # 1, 1 = 1
  
a= 10
b = 8
print( a & b) ## it should give output 8

# or operation
 # 0,0 = 0
 # 1,0 = 1
  # 0,1 = 1
  # 1, 1 = 1
x = 10
y = 8
print( x | y) # it should give output 8


#xor operator
 # 0 , 0 = 0
 # 1,0 = 1
 # 0,1 = 1
 # 1, 1= 0
print( a^ b) # it should  give output 2

# zero fill left shift
  # let suppose we are having 10 >> 2
  # so it will cut the last two values from end of 1010 ( binary of 10) and will put two zeros from starting :- 0010
  
print(10>>2) # it should give output 2
# right shift is vice versa of left shift
print(10<<2)


#Membership operator : used to check the presence of a sequence in an object
 # types 1. in , 2. not in 
 
v= " hello"
print("h" in  v) # it will give true

print("h" not in v) # it will give false

  