# A list contain items seperated by commas
# items are enclosed within square bracket

list1= [2,4,5,6,7,2]

######               items could be numbers or strings

list2= [4,"hi",6,"me",78]

#######             itesms are identified using indexes

print(list2[0])

#######             access multiple values

a = list1[1:4]
print(a)

######          access all the elements

print(list1[:]) #output [2,4,5,6,7,2]

######          similarly to access items from index 0 we write

print(list1[:5])    #output [2,4,5,6,7]

#####           similarlt from specified index to the end

print(list1[2:])


piano_list = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_list[2:])       # OUTPUT ['c','d','e','g']

print(piano_list[2:5:2])   # OUTPUT ['c','e']

print(piano_list[::2])   # OUTPUT ['a','c','e','g']

print(piano_list[::-1])     # OUTPUT ['g','f','e','d','c','b','a']







###################################################################################################

#      UPDATE LIST ITEMS OR ASSIGN VALUES

list3 = [4,55,6,7,8,9,90,4]

list3[4] = 88

print(list3)  # prints updated list

#######  ADDIND ITEMS AT THE END USING append(), add as many elements as we wish even usin LOOP


list3.append(150)

print(list3)

list3.extend(["guava", "grapes", "plum"])  # adding 'a list' to end of existing list 

######### SIMILARLY DELETE LIST ITEMS USING del

del list3[3]

print(list3)

# REMOVE DOES THE SAME JOB BUT WE CALL ACTUAL ELEMTSN ISTEAD OF INDEX

list3.remove(4)
print(list3)        # 4 will be removed from the list



#########    

sum(list3)  # will sum the items
len(list3)  # will count the items


max(list3)      # to find max value item

min(list3)      # to find min value item


strings_list3 = ''.join(list3)  # CONVERT LIST INTO STRING