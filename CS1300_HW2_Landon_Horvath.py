def create_profile_card():
    
    first_name = "Landon"
    last_name = "Horvath"
    birth_year = 2007
    hobby = "Fishing"

    current_year = 2026
    age = current_year - birth_year

    wide_border = "=" * 36 
    thin_border = "-" * 36

    print(wide_border)
    print("USER PROFILE CARD".center(36))
    print(wide_border)
    print(f"Name:  {first_name} {last_name}")
    print(f"Age:   {age}")
    print(f"Hobby: {hobby}")
    print(thin_border)
    print("Thank you for creating your profile!")
    print(wide_border)

create_profile_card()



print("=== TEXT ANALYZER ===")

sentence = input("Enter a sentence: ")

if not sentence.strip():
    print("\n--- Analysis Results ---")
    print("No sentence was entered.")
else:
    total_chars_with_spaces = len(sentence)
    total_chars_no_spaces = len(sentence.replace(" ", ""))
    
    words = sentence.split()
    num_words = len(words)
    
    vowels = 'aeiouAEIOU'
    num_vowels = sum(1 for char in sentence if char in vowels)
    
    uppercase = sentence.upper()
    lowercase = sentence.lower()
    

    reversed_sentence = sentence[::-1]
    
    starts_with_capital = sentence and sentence[0].isupper()
    
    ends_with_punctuation = sentence and sentence[-1] in '.!?'

    print("\n--- Analysis Results ---")
    print(f"Total characters (with spaces): {total_chars_with_spaces}")
    print(f"Total characters (without spaces): {total_chars_no_spaces}")
    print(f"Number of words: {num_words}")
    print(f"Number of vowels: {num_vowels}")
    print(f"Uppercase version: {uppercase}")
    print(f"Lowercase version: {lowercase}")
    print(f"Reversed: {reversed_sentence}")
    print(f"Starts with capital: {'Yes' if starts_with_capital else 'No'}")
    print(f"Ends with punctuation: {'Yes' if ends_with_punctuation else 'No'}")