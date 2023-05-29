import csv
fileApath = input("Enter the input file path: ")
fileBpath = input("Enter the output file path: ")
with open(fileApath, 'r') as fileA:
    with open(fileBpath, 'w', newline='') as fileB:
        reader = csv.reader(fileA)
        writer = csv.writer(fileB)
        writer.writerows(reader)
print("Completed copying.")
