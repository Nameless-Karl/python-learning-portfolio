prompt = "Please type in  Spathiphyllum: "
flower = str(input("What house flower is best?\n\n" + prompt ))

if flower ==  'Spathiphyllum':
    print("\n\nNo, I want a big Spathiphyllum!")
elif flower ==  "SPATHIPHYLLUM":
    print("\n\nYes - Spathiphyllum is the best plant ever!")
else:
   print(f"""
   \n\nSpathiphyllum! Not {flower}
   """)
   