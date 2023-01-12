

print("Welcome to tip calculator.")

bill = float(input("What was the total bill?\n"))

total_people = int(input("How many people to split the bill?\n"))

tip_percentage = int(input("What percentage tip wpuld you like to give? 10, 12 or 15\n"))

total_bill = bill*(tip_percentage/100) + bill

bill_split = round(total_bill/total_people,2) # using round function to round to 2 decimal places
                # BUT IF ANSWER HAS 1 DECIMAL POINT BY DEFAULT e.g 23.6 THE HOW TO SHOW 23.60 ?
                # BY USING FORMAT

bill_split_form = "{:.2f}".format(bill_split )

print('Each person should pay: $',bill_split_form )
