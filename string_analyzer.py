sentence = input("Enter a sentence: ")

total_chars = len(sentence)
upper = 0
lower = 0
digits = 0
spaces = 0

# loop through each character
for ch in sentence:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Total characters:", total_chars)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Reversed:", sentence[::-1])


print("\n")
