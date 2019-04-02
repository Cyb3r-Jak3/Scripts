print "Change Counter"
print "Please enter the count count of each coin type"

quarters = input("quarters: ")
dimes = input("dimes: ")
nickels = input("nickels: ")
pennies =  input("pennies: ")

total = quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01

print "The total value is:", "$" + str(total)
