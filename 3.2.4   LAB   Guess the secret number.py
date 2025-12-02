secret_number = 777



print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    entry = int(input("\n\nEnter a random number: "))
    if entry == secret_number:
        print("\nWell done, muggle! You are free now.")
        break
    else:
        print("\nHa ha! You're stuck in my loop!")
        continue