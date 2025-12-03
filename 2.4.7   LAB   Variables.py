# create the variables: john, mary, and adam;
# assign values to the variables.
# The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;

john = 7
mary = 8
adam = 3

# having stored the numbers in the variables,
# print the variables on one line, and separate each of them with a comma;

print(adam, john, mary)


# now create a new variable named total_apples equal to the addition of the three previous variables.

total_apples = john + mary + adam


# print the value stored in total_apples to the console;

print(total_apples)

# experiment with your code: create new variables, assign different values to them,
# and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.).
# Try to print a string and an integer together on one line,
# e.g., "Total number of apples:" and total_apples.

print("The total number of apples: ", total_apples)

# If there were 100 apples how many apples would they each have?
friends = [mary, john, adam]
for i in friends:
    share = (i/18) * 100
    print("The person with ",i, "apples now has ", round(share), " apples of 100.")
