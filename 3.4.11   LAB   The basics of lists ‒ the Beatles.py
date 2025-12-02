# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
add = int(input("How many singers do you want to add?: "))

for i in range(add):
    name = input("Name of singer: ")
    beatles.append(name)
print("Step 3:", beatles)

# step 4
del beatles[3:]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

