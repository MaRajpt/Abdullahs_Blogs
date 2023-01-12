###################### LEAP YEAR EXERCISE ######################

def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0 :
            leap_year = True
        elif year % 400 == 0 :
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = False
    return leap_year
        
    
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
     
    if is_leap(year) == True:
        month_days[1] = 29
        return month_days[month-1]
    else:
        return month_days[month-1]
    
  
 
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

