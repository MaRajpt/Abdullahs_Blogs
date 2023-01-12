
# to ope na file function open() is used, to modify and read

# default syntax        file object = open(file_name, access_mode)

# access modes in python
# read #########  "r" read mode, default mode

# "r+"  ##########  opens and reads both, the file pointer will be beginning of the file

# write  /////////  "w" craete new file if it dosent exist, otherwise overwrite

# "w+"  //////////  is same as r+ but if file dosent exist a new one is made otehrwise file is overwritten

#append $$$$$$$$$$$$  "a" write the data to the end of the file, does not erase data, and file must exist for this mode

# "a+"  $$$$$$$$$$$$$  similar to w+ as it will crate new file if the files dosent exist other wise the file pointer 
#      is at the end of the file if it exists


#/////////////////////////////////////////////////////////////////////////////////////
# varraible path



# file object myFile

myFile = open("days.txt","r")

# THREE FUNCTIONS TO READ FILES IN PYTHON 
# read()    
# readline() # reads one entire line from the file
# readlines()

#   print(myFile.read(6)) 6 is no. of bytes we can assign t oread e.g 6 will read monday only 
#   () will read entire file

print(myFile.read())

print(myFile.readline()) 

####  example 2

# File_input=open("read.txt","r")
# data = File_input.readline()
# print(data)     # reads one line becoz realine was used


File_input=open("read.txt","r")
data = File_input.readlines()
print(data)     # run it ,as a list where each line is an item in the list object: 
#              ['Hello developer!\n', 'welcome to programmingHub.\n', 'AI loves to teach Python']

# x = bytes(2)
# print(x)

print(open())
