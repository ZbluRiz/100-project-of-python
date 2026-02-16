value = 0
#enter the student scores
student_scores = input("enter stude scores separated by commas: ")
scores = [int(score) for score in student_scores.split(',')]

for i in scores:
    value += i
    
averages = value / len(scores)

while True:
    choice = input("type (descending/ascending) for sorting: ")
    
    if choice == 'ascending':
        scores = sorted(scores)
        break
    elif choice == 'descending':
        scores = sorted(scores,reverse=True)
        break
    else:
        print("input the right choice")
        break

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
print(f"Highest Scores: {max(scores)}")
print(f"Lowest Scores: {min(scores)}")
print(f"Average Student Score: {averages:.2f}")
print(f"Passing Students: {passing_students}")
print(f"Failing Students: {failing_students}")