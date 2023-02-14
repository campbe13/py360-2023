# function to return a letter grade, given a numeric grade
# pmc
# 2023-02-14
'''
returns grade based on info in slides, copy here
'''
def letter_grade(score):
  if score < 60:
    grade = 'F'
  elif score < 70:
    grade = 'D'
  elif score < 80:
    grade = 'C'
  elif score < 90:
    grade = 'B'
  elif score <= 100:
    grade = 'A'
  else:
    grade = 'X'
  return grade

print("52 F", letter_grade(52))
print("65 D", letter_grade(65))
print("75 C", letter_grade(75))
print("85 B", letter_grade(85))
print("95 A", letter_grade(95))
print("105 X", letter_grade(105))
