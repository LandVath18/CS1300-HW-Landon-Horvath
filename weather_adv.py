temperature = int(input("Enter the current temperature (°F): "))
raining = input("Is it raining? (yes/no): ").lower()

if temperature > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temperature > 85:
    if raining == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temperature <= 85:
    if raining == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temperature <= 59:
    print("It's cold — bundle up!")

else:
    print("FREEZE WARNING: Roads may be icy!")
