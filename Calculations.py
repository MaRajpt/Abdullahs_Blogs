#  2 + 3   "2" and "3" are called operands whereas '+' is called operator.

#   + plus - minis / division  * multiply  % modulo operator( returns the remainder)
#   // truncate operator return the quotient of the division operator.


#   FOLLOWING EXAMPLE WILL RETURN TRUE OR FALSE VALUE.

 
print(2**3)      # RAISE TO THE POWER  2 ** 3 = 8



print(6 % 2) # modular operator gives the remainder after division ( 6 % 2 will give 0)








x=4
y=7

print(x>y)      # FALSE WILL BE RETURNED.

# SIMILARLY

print(x<y)   # True

print(x==y) # FALSE

print(x!=y) # True


#######################################################################

# AND operator (return true if both of operand right and left sides are true).

# OR operator (return true if either of operands reft OR right side are true).

#NOT operator returns TRUE if operand is flase.


a   =   True
b   =   False

print('a and b is', a and b)

print('a and b is', a or b)

print('not a is', not a)

##############################################################

#       WALRUS operator " := " CAN assign variable inside expressions e.g print() instead 
#       of declaring a variable beforehand

#       print(a=6)  ERROR

print (a:=6)      # 6 will be returned  

print(g:=False)


numbers = [1,1,2,3,5,8,13,21,34,55]

result = [num + 3 for num in numbers if num % 2 ==0]

print(result)




#/////////////////////////////////////////////////

print("Welcome to tip calculator.")

bill = float(input("What was the total bill?\n"))

total_people = int(input("How many people to split the bill?\n"))

tip_percentage = int(input("What percentage tip wpuld you like to give? 10, 12 or 15\n"))

total_bill = bill*(tip_percentage/100) + bill

bill_split = round(total_bill/total_people,1) # using round fuction to round to 1 decimal place
                # BUT IF ANSEER HAS 1 DECIMAL POINT BY DEFAULT e.g 23.6 THE HOW TO SHOW 23.60 ?
                # BY USING FORMAT 

bill_split_form = "{:.2f}".format(bill_split )

print('Each person should pay: $',bill_split_form )

