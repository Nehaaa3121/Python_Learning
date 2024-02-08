#it is an infinite loop.
# to break a while true loop,break statement is used.

while True:
    num1 = int(input('enter a number here:'))
    num2 = int(input('enter second number here:'))
    print(num1 + num2)
    repeat = input(' do you want to stop the program:')
    if repeat == "yes":
        break 
         
        