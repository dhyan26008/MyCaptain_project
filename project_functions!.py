def most_frequent(string):
    freq_dict = {}

    for letter in string:
        if letter.isalpha():  # Only consider alphabetic characters
            freq_dict[letter] = freq_dict.get(letter, 0) + 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    for letter, count in sorted_freq:
        print(letter, "=", f"{count:02}")

input_string = input("Please enter a string: ")
most_frequent(input_string)




