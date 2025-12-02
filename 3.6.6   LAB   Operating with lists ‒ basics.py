my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.

temp_list = []

for n in my_list:
    if n not in temp_list:
        temp_list.append(n)
my_list = temp_list

print("The list with unique elements only:")
print(my_list)





# Empty list

my_list =[]

# Loop to collect number into the list. 
for n in range(10):
    n = int(input("Lets build a list of 10 numbers: ")) # Input call
    my_list.append(n) # Add to list
    
print("Your list: ", my_list, "\nContains this much elements; ", len(my_list))

#
# Write your code here.

temp_list = []

for n in my_list:
    if n not in temp_list:
        temp_list.append(n)
my_list = temp_list

print("The list with unique elements only:")
print(my_list)

