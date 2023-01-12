
## ERROS  1-LOGICAL(EXCEPTIONS)     2-SYANTAX ERRORS
# LOGICAL ERRORS ARISE DUE TO POOR UNDERSTANDING OF PROBLEM AND ITS SOLUTION
#e.g

from distutils.log import error
from logging.config import stopListening
from msilib.schema import ODBCSourceAttribute
from smtplib import SMTPRecipientsRefused
from subprocess import CREATE_NEW_CONSOLE


# a = 0
# b = 3
# print(b/a)      # gives error (logical error but syntax is correct)

#/////////////////// EXCEPTION ERROS
# zerodivision error: as above example

# importError: when imported librabry is not installed or has wrong name

# Index Error: when lenght is 10 but you access 11th then that error arises

# IndentationError: when indentation not specified

# Value Error: when fuction has valid arguments but argument values are invalid

# Exception: base calass for all exception, if you are not sure which exception may occur
#             you can use the base class, it will handle all of them.

# Type error: when incorrect function or operation applied to an object.

#################################### EXCEPTION HANDLING###########################

# when an exception suddenly occurs

# 1- Program execution sudddenly stops

# 2- the cemplete exception message along with the file name and line number of code is
#     printed on the console
    
#  3- all the calculations and operations performed till that point are lost   

try:
    print(language)
except NameError as e:
    print("Some error occured")
    
    
########################## FINALLY ###########################

# EXECUTED AFTER TRY AND EXCEPT BLOCK

# FINALLY BLOCK ALWAYS EXECUTES AFTER NORMAL TERMINAION OF TRY BLOCK OR AFTER TRY BLOCK 
# TERMInATES DUE TO SOME EXCEPTION

try:
    print(OurVariable)
except Exception:
    print('OurVariable is not defined')
finally:
    print('Output is printed successfully')


########## MANUALLY RAISING EXCEPTION   (using raise keyword)//////////////////

# raise Value Error("the list must have 5 elements")

def print_five_items(data):
    
    #len()  function returns # on items in the string or list or tuple etc
    
    if len(data) !=5:
        raise ValueError("The arguments must have five elements")
    
    # following for fucntion will desplay the items of list / tuple / string etc
    for item in data:
        print(item)
        
print_five_items([5,2,4])



