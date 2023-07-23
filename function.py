def most_frequent(input_string):
    
    letter_freq = {}

    for letter in input_string:

        if letter.isalpha():
            letter = letter.lower() 
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    for letter, frequency in sorted_freq:
        print(f"{letter}: {frequency}")

input_str = "Vanshika"
most_frequent(input_str)
