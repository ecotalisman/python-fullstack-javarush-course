# Fixing Closures

# Fix the closure code:

### 🇺🇦 Ukrainian version:

# Виправляємо замикання.

# Виправте код замикання:

# Write your code here
def create_multipliers_correct():
    # return [lambda x: i * x for i in range(5)]
    return [lambda x, i=i: i * x for i in range(5)]


for multiplier in create_multipliers_correct():
    print(multiplier(2))  # output: 0 2 4 6 8
