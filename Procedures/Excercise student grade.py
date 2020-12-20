def calcPercent(mark, total):
    percentage = (mark /total) * 100 
    return percentage

def calcGrade(percentage):
    if percentage > 90:

        grade = 'A'

    elif percentage > 80:

        grade = 'B'

    elif percentage > 70:

        grade = 'C'

    elif percentage > 60:

        grade = 'D'

    elif percentage > 50:

        grade = 'E'

    else:

        grade = 'F'

    return grade


name =str(input("Enter your name: "))
homework =int(input("Enter your IT homework score: "))
assessment=int(input("Enter your assessment score: "))
exam=int(input("Enter your exam score: "))

totalscore = homework +  assessment + exam
percentage = calcPercent(totalscore, 175)
grade = calcGrade(percentage)

print(name, grade)

