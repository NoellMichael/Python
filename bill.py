print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0
if size == 'S':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = 15+2+1
    else:
      bill = 15+2
  else:
    bill = 15+1
elif size == 'M':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
       bill = 20+3+1
    else:
      bill = 20+3
  else:
    bill = 20
elif size == 'L':
  if add_pepperoni == 'Y':
    if extra_cheese == 'Y':
      bill = 25+3+1
    else:
      bill = 25+3
  else:
    bill = 25
else:
  print("invalid")
print(f"Your final bill is: ${bill}.")