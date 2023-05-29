def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            return last_n_lines
    except FileNotFoundError:
        print("File not found.")
        return []

#  filename
filename = input("Enter the filename: ")

# value for n
n = int(input("Enter the value for n: "))

# Call the function
result = read_last_n_lines(filename, n)

# Print
print(f"Last {n} lines of the file:")
for line in result:
    print(line.strip()) #Removing spaces at the beginning and at the end of the string
