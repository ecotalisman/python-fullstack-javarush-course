"""
# Indenter to the Max

# Fix the indentation in the following code so that it correctly displays the status based on the score.

score = int(input("Enter your score: "))
if score >= 90:
print("Excellent")
else:
if score >= 75 and score < 90:
print("Good")
else:
if score >= 50 and score < 75:
print("Satisfactory")
else:
if score < 50:
print("Unsatisfactory")
"""

### 🇺🇦 Ukrainian version:
# Відступник на максималках

# Виправте відступи в наступному коді, щоб він коректно виводив статус залежно від кількості набраних балів.

score = int(input("Введіть кількість набраних балів: "))
if score >= 90:
    print("Відмінно")
else:
    if score >= 75 and score < 90:
        print("Добре")
    else:
        if score >= 50 and score < 75:
            print("Задовільно")
        else:
            if score < 50:
                print("Незадовільно")