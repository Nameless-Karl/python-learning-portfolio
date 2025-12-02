name = input("Dear Citizen of USB, what is thine name? ")
income = float(input("How much in thalers, was your income?: "))
year = input("What year are you filing for? ")

tax_relief = 556.2

if tax_relief < income < 85528.00:
    
    tax = (income * 0.18) - tax_relief
    if tax < 0:
        tax = 0
    
elif income >= 85528.00:
    
    excess = income - 85528.00
    tax = 14839.2 + (excess * 0.32)
else:
    tax = 0
    
print(f"""
Hello {name.title()}, your tax for the year, {year} is: {round(tax) } thalers
""")
    