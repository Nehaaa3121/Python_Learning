#The use of if-else statements increases the ability of for loop to complete the task effectively

for i in range(1,11):
    if i==3:
        print("add this song to the favs")
    else:
        print(i)
    
    #for fnding common mutliples
    for i in range(1,101):
        if i%8==0 and i%12==0:
            print(i)
            
            