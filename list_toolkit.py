numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

print("Original:", numbers)

print("First:", numbers[0], ", Last:", numbers[-1])

print("Middle 4:", numbers[3:7])

numbers.append(99)
print("After append:", numbers)

numbers.insert(0, 0)
print("After insert:", numbers)

numbers.remove(42)
print("After removing 42:", numbers)

removed = numbers.pop()
print("Popped value:", removed)

print(23 in numbers)

print("Index of 16:", numbers.index(16))

print("Final list:", numbers)
print("Length:", len(numbers))


print("\n")
