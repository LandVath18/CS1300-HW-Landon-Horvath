temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ").lower()

if scale == "c":
    fahrenheit = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {fahrenheit:.1f}°F")

elif scale == "f":
    celsius = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {celsius:.1f}°C")

else:
    print("Invalid scale.")


print("\n")
