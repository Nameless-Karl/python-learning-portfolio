c0 = int(input("Only non-negative and non-zero integer numbers :"))
steps = 0

while True:
    if c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            steps += 1
            print (c0)
        else:
            c0 = 3 * c0 + 1
            steps += 1
            print(c0)
        continue
    else:
        print("Steps: ",steps)
        break
        
        
else:
    print("I do not know what is happening but you have this: " + c0)