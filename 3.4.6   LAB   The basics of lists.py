hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user

prompt = "Lets replace the middle number "
prompt +=  "with: "
new_num = int(input(prompt ))

# to replace the middle number with an integer number entered by the user.
hat_list[2] = new_num

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]


# Step 3: write a line of code that prints the length of the existing list.

print("The list has only ", len(hat_list), " elements")
print(hat_list)

