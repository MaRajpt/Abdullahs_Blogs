################    Grading Program     #############################

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades= {}

for grades in student_scores:
    if student_scores[grades] < 71 :
        student_grades[grades]= "Fail"
    elif student_scores[grades] < 81 :
        student_grades[grades]= "Acceptable"
    elif student_scores[grades] < 91 :
        student_grades[grades]= "Exceeds Expecttations"  
    else:
        student_grades[grades]= "Outstanding"

print(student_grades)
          
        









