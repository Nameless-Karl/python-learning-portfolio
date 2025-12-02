# Prompt the user to enter a word and assign it to the user_word variable.
word = input("Kindly enter a word: ").upper()

# Using the list() function to convert to list
user_word = list(word)

print(user_word)

# Declaring the list of my vowels
vowels = ["A", "E", "I", "O", "U"]

# Declaring an empty list for characters of interest
word_without_vowels = []

# looping through list of interest
for letter in user_word:
    # Comparing with list of vowels
    if letter in vowels:
        continue
    # Keeping characters of interest in new list
    else:
        word_without_vowels.append(letter)

# Printing new list
print(word_without_vowels)

# Assembling the word
new_word = "".join(word_without_vowels)

print(new_word)
