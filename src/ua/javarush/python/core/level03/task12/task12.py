# Grader

# Write a program that asks the user for their score and displays their grade according to the following scale:
# 90 and above: "Excellent"
# 75-89: "Good"
# 50-74: "Satisfactory"
# Less than 50: "Unsatisfactory"
# Use the if, elif, else statements.

### 🇺🇦 Ukrainian version:
# Оцінювач

# Напишіть програму, яка запитує у користувача кількість набраних балів і виводить його оцінку за наступною шкалою:
# 90 і вище: "Відмінно"
# 75-89: "Добре"
# 50-74: "Задовільно"
# Менше 50: "Незадовільно"
# Використовуйте оператор if elif else.

# Write your code here
points = int(input("Enter a points: "))
if points >= 90:
    print('Відмінно')
elif 75 <= points < 90:
    print('Добре')
elif 50 <= points < 75:
    print('Задовільно')
else:
    print('Незадовільно')