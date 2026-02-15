#enter the student scores
student_scores = input("enter stude scores separated by commas: ")
scores = [int(score) for score in student_scores.split(',')]

#filter score by grades
grades = [
    "A" if score >= 90 else
    "B" if score >=80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "E" if score >= 50 else
    "F"
    for score in scores
]

passing_students= [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]

print("\n-Students Grade-")
for i,(score,grade) in enumerate(zip(scores,grades),start=1):
    print(f"Student {i} : Score = {score}, Grade = {grade}")

print("\n-Passing or Failling Students-")
print(f"Passing Students: {passing_students}")
print(f"Failing Students: {failing_students}")