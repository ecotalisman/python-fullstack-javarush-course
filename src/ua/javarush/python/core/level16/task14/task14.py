# Anagrams

# Given two strings, determine whether they are anagrams (contain the same characters in the same quantities).

### 🇺🇦 Ukrainian version:

# Анаграми

# Дано дві строки. Необхідно визначити, чи є вони анаграмами (містять однакові символи в однаковій кількості).

def are_anagrams(str1, str2):
    # Write your code here
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    ch_count = {}
    for ch in str1:
        ch_count[ch] = ch_count.get(ch, 0) + 1
    for ch in str2:
        if ch in ch_count:
            ch_count[ch] -= 1
        else:
            return False
    return all(count == 0 for count in ch_count.values())

# Example usage:
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # True

str1 = "hello"
str2 = "bello"
print(are_anagrams(str1, str2))  # False
