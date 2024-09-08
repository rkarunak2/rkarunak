# 1. Ask the user for their name and age, then greet them by name, and tell them how old they will be in 100 years. Use f-strings, not concatenation.

name = input("What is your name?").capitalize()
age = int(input("what is your age?"))
print(f"Hello, {name}, you will be {str(age+100)} in 100 years.")


# 2. Create a tip calculator program using functions and user input. Use a return statement in your function.

def tip_calculator(amount,tip_percent):
  return(round(amount+amount*tip_percent*0.01,2))
cost = float(input("what is the amount in the receipt? "))
tip = float(input("How much tip would you want to give? E.g 18,20,30 "))
total = tip_calculator(cost,tip)
print(total)
