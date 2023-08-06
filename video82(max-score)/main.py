student_socres = [80, 60, 50, 65, 75, 55]
higest_score = 0
sum_score = 0
for score in student_socres:
    sum_score = sum_score+score
    if score > higest_score:
        higest_score = score

print("higest score is: %i" % higest_score)
print("sum of score is: %i" % sum_score)
