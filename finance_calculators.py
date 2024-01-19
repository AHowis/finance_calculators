import math

print("investment- to calculate the amount of interest you'll earn on your investment\n")

print("bond- to calculate the amount you'll have to pay on a home loan\n")

choice = input("Enter either investment or bond:\n").lower()


if choice == 'bond':
  print("You selected bond, please answer each question in £")
  pres_val = input("What is the present value of the house?\n")
  pres_val1 = int(pres_val)
  what_is_int = input("What is the annual interest rate?\n")
  what_is_int1 = int(what_is_int)
  how_long = input("How many months do you plan on taking to repay the bond?\n")
  how_long1 = int(how_long)
  i = (what_is_int1 / 100) / 12
  investment = (i * pres_val1)/(1 - (1 + i)**(-how_long1))
  print(f"You will have to repay £" + str(round(investment, 2)) + " each month\n")
  
elif choice == 'investment':
  print(f"You selected investment, please answer each question in £\n")
  P = input("How much money are you depositing?\n")
  P1 = int(P)
  i_rate = input("Whats the interest rate?\n")
  i_rate1 = float(i_rate)
  t = input("How many years are you planning on investing?\n")
  t1 = int(t)
  interest = input("Do you want simple or compound interest?\n").lower()
  r = i_rate1 / 100
  if interest == 'simple':
     A = P1 *(1 + r*t1)
     print("The total amount once interest has been applied is:\n" + str(A))
  if interest == 'compound':
    A1 = P1 * math.pow((1+r),t1)
    print(f"The total amount once interest has been applied is:\n" + str(round(A1, 2)))

else:
  print("You typed an invalid answer")
