# Pizza order

print("Thank you for choosing Python Pizza Deliveries!")
size = input('Size with capital letters: L, M, or S.').title() # What size pizza do you want? S, M, or L
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
L= 25
M= 20
S= 15
cheese_price = 1
if size== 'L' or 'M':
    pepperoni_price=3
else:
    pepperoni_price=2
if size== 'L':
    add_pepperoni = input('Would you like pepperoni: Y or N') # Do you want pepperoni? Y or N
    if add_pepperoni=='y':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y": 
            final_bill= int(L+pepperoni_price+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(L+pepperoni_price)
            print(f'Your final bill is: {final_bill}')
    elif add_pepperoni=='n':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y":
            final_bill= int(L+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(L)
            print(f'Your final bill is: {final_bill}')
elif size== 'M':
    add_pepperoni = input('Would you like pepperoni: Y or N') # Do you want pepperoni? Y or N
    if add_pepperoni=='y':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y": 
            final_bill= int(M+pepperoni_price+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(M+pepperoni_price)
            print(f'Your final bill is: {final_bill}')
    elif add_pepperoni=='n':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y":
            final_bill= int(M+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(M)
            print(f'Your final bill is: {final_bill}')
elif size== 'S':
    add_pepperoni = input('Would you like pepperoni: Y or N') # Do you want pepperoni? Y or N
    if add_pepperoni=='y':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y": 
            final_bill= int(S+pepperoni_price+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(S+pepperoni_price)
            print(f'Your final bill is: {final_bill}')
    elif add_pepperoni=='n':
        extra_cheese = input('Would you like cheese: Y or N') # Do you want extra cheese? Y or N
        if extra_cheese=="y":
            final_bill= int(L+cheese_price)
            print(f'Your final bill is: {final_bill}')
        else:
            final_bill= int(S)
            print(f'Your final bill is: {final_bill}')


