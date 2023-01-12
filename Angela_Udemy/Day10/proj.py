##################################  CALCULATOR PROJECT ##########################
import os
print( """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operations = {
    
    '+' : add,  ## NOTICE SINCE add NAMED FUCTION IS DECLARED ABOVE , VALUE (add) OF '+' KEYS DOSENT NEED
    '-' : sub,          #  ' ' AS NORMALY IT DO
    '*' : mult,
    '/' : div
    
    }


def main ():

        num1 = float(input("Please enter the first number: "))
        for symbol in operations:
            print(symbol)



        calc = True
        while calc == True:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("Please enter the next number: "))
            function = operations[operation_symbol]
            calculation = function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {calculation}")

            continue_calculation = input("Type 'y' to continue else 'n' if no: ")

            if continue_calculation == 'y':  
                num1 = calculation
            else:
                calc = False
                main()
         
            
main()      # BY PUTING EVERY THING IN A FUCTION WE CAN CALL IT TO RESET THE CODE
        
    
        
        

        
      
    
