# Cat Chaos

# Write a program that stores a set of the 5 most popular cat names.
# The user must try to guess them. When a cat name is guessed correctly, it is removed from the set.
# The goal of the game is to guess all the names in as few attempts as possible.

### 🇺🇦 Ukrainian version:

# Котовасія

# Напиши програму, яка зберігає множину з 5 найпопулярніших імен котів.
# Користувач має намагатися відгадати їх. Коли він відгадує ім'я кота, воно вилучається з множини.
# Мета гри - відгадати всіх котів за якомога меншу кількість спроб.

# Write your code here
cat = {"Tom", "Barsik", "Simba", "Murzik", "Shadow"}
count = 0

while cat:
    guess = input("Guess my favorite Cat names: ").strip()
    count += 1
    print(f"Number of attempts: {count}")
    if guess in cat:
        cat.discard(guess)
        print(f"Correct! {guess} deleted. Remaining names: {len(cat)}")
    else:
        print("Try again")

print(f"Congratulations! You guessed all the names in {count} attempts.")
