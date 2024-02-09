# continue statemnt is used when you want to skip a particular condition
#break statement is used when you want to destrou a loop at certain condition and come out of the loop.

for i in range(1,101):
    if i%2==0:
        continue
    else:
       print(i)
for i in range(1,101):
            if i==9:
               break
else:
            print(i)