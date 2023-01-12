############## LIST COMPREHENSION ##########
# case when u create new list from previous list

# new_list = [new_item for item in list]
numbers = [1, 2, 3]
add_one = [n + 1 for n in numbers]          # ONE LINE OF CODE.
print(add_one)
####

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n*n for n in nums]
print(squared_numbers)

############ CONDITIONAL LIST COMPREHENSION

names = ['alex', 'beth', 'scottfield', 'pooh']

short_names = [name.upper() for name in names if len(name) < 5]

print(short_names)

### EVENS

evens = [ n for n in nums if n % 2 == 0]
print(evens)

#########
list1 = open("file1.txt")
nums_1 = list1.readlines()
list2 = open("file2.txt")
nums_2 = list2.readlines()
commons = [int(i.strip()) for i in nums_1 if i in nums_2]
print(commons)