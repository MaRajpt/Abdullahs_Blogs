########## FOR LOOPS #############

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")
# print(fruits)  # indentation is important 

########## CALCULATE AVERAGE HEIGHT USING LOOP ############


student_heights = input("Input a list of student heights ").split()

total = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])  # converting strings numbers to integers

number_of_students = 0

for n in range(0, len(student_heights)): 
    number_of_students += 1
     
print("total students",number_of_students)

for y in range(0, len(student_heights)): 
  total += student_heights[y]
  
print(total)

average = round(total/number_of_students)

print(f"The average of all students will be: {average}")