a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("a < b < c :", expr1)
print("not (a > b or b > c) :", expr2)
print("a <= b and b <= c :", expr3)

if expr2 == expr3:
    print("De Morgan's correct: Expressions 2 and 3 match!")
else:
    print("Expressions 2 and 3 don't match.")
