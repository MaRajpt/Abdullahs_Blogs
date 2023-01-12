# Convert string to list in Python#

###                     Solution 1: Using Split()


str_1 = "Hire the top 1% freelance developers"
list_1 = str_1.split()
print(list_1)

#Output:
#['Hire', 'the', 'top', '1%', 'freelance', 'developers']


####                    Solution 2: Using list()

str_1 = "Hire freelance developers"


list_1 = list(str_1.strip(" "))
print(list_1)

#Output:
#['H', 'i', 'r', 'e', ' ', 'f', 'r', 'e', 'e', 'l', 'a', 'n', 'c', 'e', ' ', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', 's']



#//////////////

a = ["guava", "grapes", "plum"]

b = "plum"

print(len(a))
print(len(b))


#######  FIRST LETTER OF STRING TO BE CAPATILIZE USE TITLE

# string_name.title()

########## Remove spaces at the beginning and at the end of the string: #############
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

##############  Replace the word "bananas": ################

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

##############  Return all lines in the file, as a list where each line is an item in the list object: ####

f = open("demofile.txt", "r")

print(f.readlines())


#########################################################
