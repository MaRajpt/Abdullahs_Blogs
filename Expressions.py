
from email.policy import strict
import re
from unicodedata import digit       # re regular expressions
# EXTREMELY USEFUL IN EXTRACTING INFO FROM TEXT SUCH AS CODE, LOG FILES, SPREAD SHEETS EVEN DOCUMENTS

# e.g use re to verify the format of email address and filter invalid IDs from the genuine ones

# re has either literals or metacharacters(characters with a special meaning).

#/////////////////////////////// IDENTIFIERS //////////////////////

# \d: matches any decimal digit [0-9] .

# \D: matches any non-decimal digit [^0-9] .

# \s: matches any white space charcters ( space, carriage return, ab, non-printable character).

# \S: matches non white chatacters.

# \w: matches alphanumeric characters. set of all the letters and numbers in both lower and uppercase

# \W: matches any non alphanumeric character.

#////////////////////////////  findall method /////////////////

import re
string1  = "hello my name is lyon"
# r is raw string literal, it chanages how the string literal is interpreted. such literals are stored as they appear
# r exmaple if we want to s = 'Hi\nHello' \n will be considered new line but if s = r'Hi\nHello'
# is used r will use \ are a character instead of new line command

print(re.findall(r"lyon",string1))


import re
string2 = "hello im 30 years old"

print(re.findall(r"\d",string2)) # but it return ['3','0'] istead of 30 there fore we use 
                                 # modifier +
                                 
# MODIFIERS are set of meta characters tha add functionality to identifiers

string2 = "hello im 30 years old"
# + modifier will get number of any lenght from string

print(re.findall(r"\d+",string2)) # 30 is returned

#////////////////////////////////////////// SEARCH ///////////////////////

import re
if re.search("awsome","you are an awesome person"):
    print("ur awesome indeed")
    

#/////////////////////////////////////////////// SPLIT //////////////////////////

# helps us split strings by occurrences of given patter

import re
result1=re.split(r's','awesome game')
# by using " " , we can split when there is space in the content e.g awsomespace 
result2=re.split(" ",'awesome game')
print(result1)
print(result2)










