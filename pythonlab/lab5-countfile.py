def count_letter_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            letter_count = {}

            for letter in content:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1

            return letter_count
    except FileNotFoundError:
        print("File not found.")
        return {}

# input
filename = input("Enter the filename: ")
result = count_letter_occurrences(filename)
# Print
print("Letter Occurrences:")
for letter, count in result.items():
    print(f"{letter}: {count}")